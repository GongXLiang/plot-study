#!/usr/bin/env python3
"""
Auto-repair broken wikilinks in graphify-out/wiki/.
Run this after `graphify update` or `graphify --wiki` to prevent orphan pages.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "graphify-out/wiki"
RAW_DIR = ROOT / "raw"


def normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower().replace("'", ""))


def build_index():
    """Index all existing markdown files for fast lookup."""
    wiki_files = {}
    for f in WIKI_DIR.glob("*.md"):
        wiki_files[normalize(f.stem)] = f
        wiki_files[normalize(f.name)] = f
        # Also allow partial match by stem words
        wiki_files[f.stem] = f

    raw_files = {}
    for f in RAW_DIR.rglob("*.md"):
        raw_files[normalize(f.stem)] = f
        raw_files[normalize(f.name)] = f
        raw_files[f.stem] = f
        raw_files[f.name] = f

    return wiki_files, raw_files


def fix_plain_refs(content: str) -> str:
    """
    Convert bare `raw/reference/...` text in Key Concepts / Source Files
    sections into proper wikilinks.
    """
    # Key Concepts: - **Concept** (N connections) — `raw/reference/...`
    content = re.sub(
        r"^(\s*-\s+\*\*.*?\*\*.*?)`raw/reference/([^`]+)`(.*)$",
        lambda m: f"{m.group(1)}[[../../raw/reference/{m.group(2).strip()}]]{m.group(3)}"
        if "[[" not in m.group(0) else m.group(0),
        content,
        flags=re.MULTILINE,
    )
    # Source Files: - `raw/reference/...`
    content = re.sub(
        r"^(\s*-\s+)`raw/reference/([^`]+)`(.*)$",
        lambda m: f"{m.group(1)}[[../../raw/reference/{m.group(2).strip()}]]{m.group(3)}"
        if "[[" not in m.group(0) else m.group(0),
        content,
        flags=re.MULTILINE,
    )
    # God node header: > God node · N connections · `raw/reference/...`
    content = re.sub(
        r"(> God node · \d+ connections ·) `raw/reference/([^`]+)`",
        lambda m: f"{m.group(1)}[[../../raw/reference/{m.group(2).strip()}]]"
        if "[[" not in m.group(0) else m.group(0),
        content,
    )
    return content


def resolve_link(link_text: str, source_file: Path, wiki_files, raw_files) -> str | None:
    """
    Try to resolve a wikilink target to an existing file.
    Returns the replacement link text, or None if it should be plain-texted.
    """
    link = link_text.strip()
    if not link:
        return None

    # Already has a path separator -> resolve relative to source
    if "/" in link or "\\" in link:
        target = source_file.parent / link
        if target.exists():
            return link
        if (target.parent / (target.name + ".md")).exists():
            return link
        return None

    # 1. Exact basename match in wiki/
    if (WIKI_DIR / (link + ".md")).exists():
        return link

    # 2. Exact normalized stem match in wiki/
    nlink = normalize(link)
    if nlink in wiki_files:
        return wiki_files[nlink].stem

    import os

    # 3. Exact normalized stem match in raw/
    if nlink in raw_files:
        rel = os.path.relpath(str(raw_files[nlink]), str(source_file.parent)).replace("\\", "/")
        return rel

    # 4. Fuzzy: raw file whose normalized stem contains the normalized link (or vice versa)
    for key, f in raw_files.items():
        if isinstance(key, str) and key.startswith("."):
            continue  # skip paths
        if nlink in key or key in nlink:
            rel = os.path.relpath(str(f), str(source_file.parent)).replace("\\", "/")
            return rel

    # 5. Fuzzy: wiki file whose normalized stem contains the normalized link (or vice versa)
    for key, f in wiki_files.items():
        if isinstance(key, str) and key.startswith("."):
            continue
        if nlink in key or key in nlink:
            return f.stem

    return None


def fix_file(md_file: Path, wiki_files, raw_files) -> int:
    content = md_file.read_text(encoding="utf-8")
    original = content

    # Step 1: fix bare `raw/reference/...` text into wikilinks
    content = fix_plain_refs(content)

    # Step 2: fix existing broken [[wikilinks]]
    pattern = re.compile(r"\[\[([^\]|]+)(\|[^\]]+)?\]\]")

    def replacer(m):
        inner = m.group(1).strip()
        pipe = m.group(2) or ""
        resolved = resolve_link(inner, md_file, wiki_files, raw_files)
        if resolved is None:
            # Demote to plain text
            display = pipe[1:] if pipe else inner
            return display
        if resolved == inner:
            return m.group(0)
        return f"[[{resolved}{pipe}]]"

    content = pattern.sub(replacer, content)
    if content != original:
        md_file.write_text(content, encoding="utf-8")
        return 1
    return 0


def main():
    wiki_files, raw_files = build_index()
    fixed = 0
    for md_file in sorted(WIKI_DIR.glob("*.md")):
        fixed += fix_file(md_file, wiki_files, raw_files)
    print(f"Checked {len(list(WIKI_DIR.glob('*.md')))} wiki files, modified {fixed}.")


if __name__ == "__main__":
    main()
