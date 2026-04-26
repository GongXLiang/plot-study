# Graph Report - raw/UltraPlot/ultraplot  (2026-04-26)

## Corpus Check
- 24 files · ~292,803 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 145 nodes · 221 edges · 12 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Scale & Transform System|Scale & Transform System]]
- [[_COMMUNITY_Tick Formatters & Locators|Tick Formatters & Locators]]
- [[_COMMUNITY_Geographic Axes (CartopyBasemap)|Geographic Axes (Cartopy/Basemap)]]
- [[_COMMUNITY_Projection Definitions|Projection Definitions]]
- [[_COMMUNITY_Colormap & Color Database|Colormap & Color Database]]
- [[_COMMUNITY_Core API & Entry Points|Core API & Entry Points]]
- [[_COMMUNITY_Legend System|Legend System]]
- [[_COMMUNITY_Cartesian Axes & Config|Cartesian Axes & Config]]
- [[_COMMUNITY_Polar  3D  Shared Axes|Polar / 3D / Shared Axes]]
- [[_COMMUNITY_GridSpec & Layout|GridSpec & Layout]]
- [[_COMMUNITY_Colorbar & Layout Solver|Colorbar & Layout Solver]]
- [[_COMMUNITY_Base Axes|Base Axes]]

## God Nodes (most connected - your core abstractions)
1. `_Scale` - 13 edges
2. `_CartopyFormatter` - 5 edges
3. `_GeoAxis` - 4 edges
4. `_GridlinerAdapter` - 4 edges
5. `_Colormap` - 4 edges
6. `LongitudeFormatter` - 4 edges
7. `LatitudeFormatter` - 4 edges
8. `_GeoLabel` - 3 edges
9. `GeoAxes` - 3 edges
10. `ContinuousColormap` - 3 edges

## Surprising Connections (you probably didn't know these)
- `_SharedAxes` --inherits--> `object`  [EXTRACTED]
  /home/runner/work/plot-study/plot-study/raw/UltraPlot/ultraplot/axes/shared.py →   _Bridges community 2 → community 8_
- `_Colormap` --inherits--> `object`  [EXTRACTED]
  /home/runner/work/plot-study/plot-study/raw/UltraPlot/ultraplot/colors.py →   _Bridges community 2 → community 4_
- `_Scale` --inherits--> `object`  [EXTRACTED]
  /home/runner/work/plot-study/plot-study/raw/UltraPlot/ultraplot/scale.py →   _Bridges community 2 → community 0_
- `_CartopyFormatter` --inherits--> `object`  [EXTRACTED]
  /home/runner/work/plot-study/plot-study/raw/UltraPlot/ultraplot/ticker.py →   _Bridges community 2 → community 1_

## Communities

### Community 0 - "Scale & Transform System"
Cohesion: 0.12
Nodes (23): CutoffScale, CutoffTransform, ExpScale, ExpTransform, FuncScale, FuncTransform, InverseScale, InverseTransform (+15 more)

### Community 1 - "Tick Formatters & Locators"  
Cohesion: 0.13
Nodes (20): _PlateCarreeFormatter, AutoCFDatetimeFormatter, AutoCFDatetimeLocator, AutoFormatter, _CartopyFormatter, CFDatetimeFormatter, CFTimeConverter, DegreeFormatter (+12 more)

### Community 2 - "Geographic Axes (Cartopy/Basemap)"
Cohesion: 0.2
Nodes (15): _BasemapAxes, _BasemapGridlinerAdapter, _CartopyAxes, _CartopyGridliner, _CartopyGridlinerAdapter, _CartopyGridlinerProtocol, _CartopyLabel, GeoAxes (+7 more)

### Community 3 - "Projection Definitions"
Cohesion: 0.19
Nodes (14): AzimuthalEquidistant, Gnomonic, LambertAzimuthalEqualArea, Aitoff, Hammer, KavrayskiyVII, NorthPolarAzimuthalEquidistant, NorthPolarGnomonic (+6 more)

### Community 4 - "Colormap & Color Database"
Cohesion: 0.2
Nodes (13): _ColorCache, ColorDatabase, _Colormap, ColormapDatabase, ContinuousColormap, DiscreteColormap, DiscreteNorm, DivergingNorm (+5 more)

### Community 5 - "Core API & Entry Points"
Cohesion: 0.19
Nodes (6): Cycle, _RefreshingRegistry, Figure, PlotAxes, CurvedText, _Crawler

### Community 6 - "Legend System"
Cohesion: 0.22
Nodes (8): _FeatureArtistLegendHandler, GeometryEntry, _GeometryEntryLegendHandler, Legend, LegendEntry, _LegendInputs, _ShapelyGeometryLegendHandler, UltraLegend

### Community 7 - "Cartesian Axes & Config"
Cohesion: 0.29
Nodes (5): _AxisFormatConfig, CartesianAxes, CartesianAxes, # NOTE: The matplotlib analogue to this file is actually __init__.py, ExternalAxesContainer

### Community 8 - "Polar / 3D / Shared Axes"
Cohesion: 0.25
Nodes (4): Axes3D, PolarAxes, _SharedAxes, ThreeAxes

### Community 9 - "GridSpec & Layout"
Cohesion: 0.33
Nodes (5): GridSpec, SubplotGrid, _SubplotSpec, list, MutableSequence

### Community 10 - "Colorbar & Layout Solver"
Cohesion: 0.33
Nodes (4): _TextKw, UltraColorbar, ColorbarLayoutSolver, UltraLayoutSolver

### Community 11 - "Base Axes"
Cohesion: 0.5
Nodes (4): Axes, _ExternalContext, _ExternalModeMixin, _TransformedBoundsLocator

## Knowledge Gaps
- **54 isolated node(s):** `_TransformedBoundsLocator`, `_ExternalContext`, `_AxisFormatConfig`, `CartesianAxes`, `_CartopyGridliner` (+49 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Configurator` connect `Colormap & Color Database` to `Cartesian Axes & Config`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Why does `_Scale` connect `Scale & Transform System` to `Geographic Axes (Cartopy/Basemap)`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **What connects `_TransformedBoundsLocator`, `_ExternalContext`, `_AxisFormatConfig` to the rest of the system?**
  _54 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Scale & Transform System` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._
- **Should `Tick Formatters & Locators` be split into smaller, more focused modules?**
  _Cohesion score 0.13 - nodes in this community are weakly interconnected._