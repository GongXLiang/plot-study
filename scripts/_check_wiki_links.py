import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
wiki_dir = ROOT / "graphify-out/wiki"
raw_dir = ROOT / "raw"

wiki_files = {f.name for f in wiki_dir.glob("*.md")}
wiki_basenames = {f.stem for f in wiki_dir.glob("*.md")}
raw_basenames = {}
for f in raw_dir.rglob("*.md"):
    raw_basenames[f.stem] = f

broken = []
for md_file in wiki_dir.glob("*.md"):
    content = md_file.read_text(encoding="utf-8")
    links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", content)
    for link in links:
        link = link.strip()
        if not link:
            continue
        if "/" in link or "\\" in link:
            target = md_file.parent / link
            if not target.exists():
                if not (target.parent / (target.name + ".md")).exists():
                    broken.append((md_file.name, link))
        else:
            if link in wiki_basenames or (link + ".md") in wiki_files or link in raw_basenames:
                continue
            broken.append((md_file.name, link))

if broken:
    print(f"Found {len(broken)} potentially broken wikilink(s):\n")
    current_file = None
    for fname, link in sorted(broken):
        if fname != current_file:
            print(f"\n{fname}:")
            current_file = fname
        print(f"  - [[{link}]]")
else:
    print("All wikilinks in graphify-out/wiki/ appear to resolve correctly.")
