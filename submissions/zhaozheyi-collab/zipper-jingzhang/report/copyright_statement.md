# Copyright Statement · 版权与生成方法声明

拉链京张 Zipper Jingzhang ｜ 2026-08-30

## 1. Authorship · 作者与代理

Submitted by GitHub account **zhaozheyi-collab** (agent_name: Arch.zhao). All text, geometry, metrics, matrices, figures, drawings and the offline visual pages were produced by the declared AI agent pipeline (`zipper-v2/pipeline`, Python 3.12 + shapely/pyproj/matplotlib, deterministic seeds) working from public cleared sources and the user-provided design rationale embedded in `proposal.md` (problem → mechanism → ten teeth → three cores → scenarios). 本包全部文本、几何、指标、矩阵、图纸与离线展示页由声明的 AI 智能体管线生成，未使用他人未授权成果。

## 2. AI-generated imagery · AI 生成图像

- The **13 scene illustrations** under `assets/media/teeth/` (z01-crossing-daily … z10-ground-park) are AI-generated with **Lovart AI** using the free model **generate_image_nano_banana_pro** (unlimited/free queue; no paid generation was used).
- Verbatim prompts are preserved in **Appendix A** below (13 prompts with SHA-256); the machine-readable AI-generation markings (IPTC/XMP `trainedAlgorithmicMedia`, "Made with Google AI" lineage) are **preserved, not stripped**: source PNG XMP packets were re-injected into the transcoded JPEGs as APP1/XMP segments and verified per file.
- The **z00 teeth positioning map** (`assets/media/teeth/z00-teeth-map.jpg`) and the **five required figures** (`assets/figures/*.png`, incl. `.en.png` counterparts) are **not** AI-generated: they are plotted deterministically by the pipeline from the submitted GeoJSON geometry and metrics.

## 3. Evidence separation · 证据分离

AI-generated illustrations express design intent only and are kept in `assets/media/teeth/`, clearly separated from the factual evidence layer (`geometry/*.geojson`, `metrics.json`, matrices). They must not be used as boundary, area, or planning-control evidence. 官方四至发布后，全部几何、指标与图纸重算；示意图不作为任何边界、面积或规划控制依据。

## 4. License and IP · 许可与知识产权

- License: **COMMUNITY-DISPLAY-ONLY**, per the open call announcement. Per announcement §8.1, IP of submitted results is jointly shared; this package is a conceptual suggestion and does not constitute statutory planning, approved government action, or an implementation commitment.
- Third-party copyrighted material: none depicted in the AI-generated images; no remote assets are embedded in the visual pages; all spatial layers derive from `brief/site-package/` provisional data and agent-generated design geometry registered in `sources.json`.

## Appendix A · Generation prompts (verbatim, 13)

逐字留档的生成提示词（与提交图像一一对应；SHA-256 供核验）：

### prompt-fx-01.txt

SHA-256: `2ae1bf9d71f9875c87d7b39957e3c21fb2be95b6b882720b0a298d72f66693a2`

```text
aerial half-bird's-eye view looking north along a 120-meter-wide linear heritage park built on a preserved railway corridor,
rail tracks preserved flush with lawn and paving underfoot, pedestrians and cyclists crossing freely,
small delivery robots on a dedicated lane, east-west streets stopping at the park edge,
mid-rise innovation blocks on both sides, morning soft light, long gentle shadows,
professional architectural visualization for an urban design competition,
realistic but slightly muted material palette: warm bronze-brown for preserved railway heritage elements,
steel blue-grey for new infrastructure, soft sage green landscape planting,
human-scale activity with small simple figures, clean layered composition, competition-grade rendering quality,
wide 16:9 composition, no text, no numbers, no labels
Negative prompt: text, letters, numbers, labels, watermark, logo, oversaturated colors, fisheye distortion,
distorted proportions, fantasy elements, cartoon style, dark dystopian mood
```

### prompt-fx-02.txt

SHA-256: `5fd50bbce91325d7f021a7e7502e12b854fdf731a54e32d23d529859ca9e8a20`

```text
same aerial half-bird's-eye view looking north along the linear heritage park, at dusk with warm golden light,
the flush covers over the rail bed slowly opening like a zipper, revealing the historic rails and ballast beneath,
crowds gathered on both banks watching, a faint luminous holographic steam train gliding above the rails,
memorial atmosphere but civic and warm, not dark,
professional architectural visualization for an urban design competition,
realistic but slightly muted material palette: warm bronze-brown for preserved railway heritage elements,
steel blue-grey for new infrastructure, soft sage green landscape planting,
human-scale activity with small simple figures, clean layered composition, competition-grade rendering quality,
wide 16:9 composition, no text, no numbers, no labels
Negative prompt: text, letters, numbers, labels, watermark, logo, oversaturated colors, fisheye distortion,
distorted proportions, fantasy elements, cartoon style, dark dystopian mood
```

### prompt-fx-03.txt

SHA-256: `9ef6adfe461debb982488f894317cad33b0f95ccdf1894db6c2736453ca9f215`

```text
aerial half-bird's-eye view of a garden-type innovation district along a riverside green corridor,
low-density research campus buildings with terracotta and grey facades embedded in generous lawns and groves,
an open grassy testing field with visitors walking along a light wooden boardwalk, small test robots on the lawn,
a riverside promenade with continuous tree canopy, morning light,
professional architectural visualization for an urban design competition,
realistic but slightly muted material palette: warm bronze-brown for preserved railway heritage elements,
steel blue-grey for new infrastructure, soft sage green landscape planting,
human-scale activity with small simple figures, clean layered composition, competition-grade rendering quality,
wide 16:9 composition, no text, no numbers, no labels
Negative prompt: text, letters, numbers, labels, watermark, logo, oversaturated colors, fisheye distortion,
distorted proportions, fantasy elements, cartoon style, dark dystopian mood
```

### prompt-fx-04.txt

SHA-256: `fb7eb86a34aad0d5a6c38e8e53c3e3f924808e1908b3f599a6ef7e9a2cf02704`

```text
oblique aerial view of an open-air autonomous-model testing field on a green lawn,
a test circuit with small self-driving vehicles and soft traffic cones, shaded workstations with engineers,
an outer circular timber visitor boardwalk with small groups observing, a small timber explanation pavilion,
surrounded by low research buildings and trees, afternoon light,
professional architectural visualization for an urban design competition,
realistic but slightly muted material palette: warm bronze-brown for preserved railway heritage elements,
steel blue-grey for new infrastructure, soft sage green landscape planting,
human-scale activity with small simple figures, clean layered composition, competition-grade rendering quality,
wide 16:9 composition, no text, no numbers, no labels
Negative prompt: text, letters, numbers, labels, watermark, logo, oversaturated colors, fisheye distortion,
distorted proportions, fantasy elements, cartoon style, dark dystopian mood
```

### prompt-fx-06.txt

SHA-256: `26a8b7a581143b8d23d53df298e30e8ca32fcbf1286c90dea2ece07b8e798d52`

```text
street-level view of a lively tech-transfer street beside a university district,
small renovated shopfronts as incubator studios, IP-service kiosks and exhibition windows with pop-up stalls,
a light steel footbridge connecting first floors across the street, mature street trees, bicycles and pedestrians,
mid-1990s office buildings refurbished above, soft afternoon light,
professional architectural visualization for an urban design competition,
realistic but slightly muted material palette: warm bronze-brown for preserved railway heritage elements,
steel blue-grey for new infrastructure, soft sage green landscape planting,
human-scale activity with small simple figures, clean layered composition, competition-grade rendering quality,
wide 16:9 composition, no text, no numbers, no labels
Negative prompt: text, letters, numbers, labels, watermark, logo, oversaturated colors, fisheye distortion,
distorted proportions, fantasy elements, cartoon style, dark dystopian mood
```

### prompt-fx-07.txt

SHA-256: `e2f40aee5744df6a86061d13753329eade44c98c52a8431d9581b3304bc56a06`

```text
aerial half-bird's-eye view of a straddle building crossing directly over a preserved railway corridor,
the track passing through a glazed ground-floor hall with a glowing glass strip in the floor,
one roof section slid open revealing the rails below, quadrant pedestrian connections linking a metro station plaza
to four city blocks, mid-rise digital-industry buildings around, late afternoon light,
professional architectural visualization for an urban design competition,
realistic but slightly muted material palette: warm bronze-brown for preserved railway heritage elements,
steel blue-grey for new infrastructure, soft sage green landscape planting,
human-scale activity with small simple figures, clean layered composition, competition-grade rendering quality,
wide 16:9 composition, no text, no numbers, no labels
Negative prompt: text, letters, numbers, labels, watermark, logo, oversaturated colors, fisheye distortion,
distorted proportions, fantasy elements, cartoon style, dark dystopian mood
```

### prompt-fx-08.txt

SHA-256: `78d437439af5f5368a7f5a43d1391e9fa0b84b1e0f7f8fbbe024a29447b7bad1`

```text
interior view of an international roadshow lounge, a tall glass wall framing the preserved railway corridor outside as a stage backdrop,
wooden amphitheater steps with a small audience, a ring-shaped display screen without any text, island seating for meetings,
warm pendant lighting, greenery pots, dusk blue hour outside,
professional architectural visualization for an urban design competition,
realistic but slightly muted material palette: warm bronze-brown for preserved railway heritage elements,
steel blue-grey for new infrastructure, soft sage green landscape planting,
human-scale activity with small simple figures, clean layered composition, competition-grade rendering quality,
wide 16:9 composition, no text, no numbers, no labels
Negative prompt: text, letters, numbers, labels, watermark, logo, oversaturated colors, fisheye distortion,
distorted proportions, fantasy elements, cartoon style, dark dystopian mood
```

### prompt-fx-09.txt

SHA-256: `4f9e51582a228aafafba5e09f11e379a830f8b93743480a208425ef76bef45a3`

```text
night street-level view of twin riverside-style commercial streets facing each other across a preserved railway corridor,
the rail bed softly lit like an urban river, warm string lights over outdoor tea seats,
small shopfronts including a data-service salon window, people strolling and dining, low glow, deep blue sky,
realistic but slightly muted material palette: warm bronze-brown rails and shopfronts, steel blue-grey canopies, warm amber lighting,
human-scale activity with small simple figures, clean layered composition, competition-grade rendering quality,
wide 16:9 composition, no text, no numbers, no labels
Negative prompt: text, letters, numbers, labels, watermark, logo, oversaturated colors, fisheye distortion,
distorted proportions, fantasy elements, cartoon style, dark dystopian mood
```

### prompt-z01-a.txt

SHA-256: `6000a60223d6dea5905fc0e44cf61c254140cd90e73bebbe53df512b81573027`

```text
professional urban design principle diagram, axonometric three-quarter cutaway view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for new infrastructure,
soft sage green landscape, small simple human silhouettes, competition-grade diagram illustration.

SCENE: an at-grade crossing plaza where a city street meets the preserved railway corridor
lying exactly at surrounding street level; old steel rails with wooden sleepers fully embedded in the paving,
their tops precisely flush with the plaza surface so wheels and feet pass smoothly across;
the paving beside and between the rails divided into fine hinged panels readable only as subtle joint lines;
two heritage crossing barrier gates on both sides of the street;
a signal totem with a small bronze bell at the gate post;
low hedges and tree rows of the linear heritage park flanking the corridor; mid-rise brick urban blocks in the background.

STATE - DAILY: the barrier gates raised upright; the crossing surface completely flush and flat;
pedestrians, cyclists and occasional vehicles crossing the street freely in both directions over the embedded rails;
a quiet continuous pavement joint line marking the former track alignment; ordinary soft daylight.

square 1:1 aspect ratio composition, all elements within frame, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```

### prompt-z01-b.txt

SHA-256: `3a4b6ad0723560d913a16ce0d4670eaa7af0fe33df5b8f374ecc647c5523e9b4`

```text
professional urban design principle diagram, axonometric three-quarter cutaway view,
soft off-white paper background with dusk tint, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for new infrastructure,
soft sage green landscape, small simple human silhouettes, competition-grade diagram illustration.

SCENE: an at-grade crossing plaza where a city street meets the preserved railway corridor
lying exactly at surrounding street level; old steel rails with wooden sleepers fully embedded in the paving,
their tops precisely flush with the plaza surface so wheels and feet pass smoothly across;
the paving beside and between the rails divided into fine hinged panels readable only as subtle joint lines;
two heritage crossing barrier gates on both sides of the street;
a signal totem with a small bronze bell at the gate post;
low hedges and tree rows of the linear heritage park flanking the corridor; mid-rise brick urban blocks in the background.


STATE - CEREMONIAL, dusk: the paved ground flanking the tracks has sunk about one meter below the original street level
on both sides, forming a gentle viewing bowl; the hinged paving panels between and beside the rails have rotated open,
uncovering the original rails and wooden sleepers set in their ballast bed, revealed as an open center trench;
the two heritage barrier gates lowered flat across the street ends of the sunken plaza,
gently holding the gathered crowd back at the upper street level;
crowd silhouettes standing at the upper level looking down into the revealed trackbed,
some raising small glowing rectangles (phones);
a large holographic projection of a vintage steam locomotive rendered in glowing cyan wireframe and light points,
hovering just above the revealed track bed as a luminous apparition;
warm accent light washing the revealed sleepers;
the signal totem and bronze bell glowing warm amber, the holographic train light
reflecting softly on the sunken paving;
deep blue dusk sky tone over the same buildings and tree rows.

professional urban design principle diagram finish, same bronze heritage elements,
same steel blue-grey infrastructure, cyan and warm amber accent light,
square 1:1 aspect ratio composition, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, oversaturated colors, fisheye distortion
```

### prompt-z02-a.txt

SHA-256: `3fcfc1d4cab0b54e49379d28ad64c125bcbd2828188dd51ed007ab33b0886896`

```text
professional urban design principle diagram, axonometric three-quarter cutaway view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for new infrastructure,
soft sage green landscape, small simple human silhouettes, competition-grade diagram illustration.

SCENE: a slender elevated pedestrian and cycle bridge with a semi-transparent grating deck
spanning a railway cutting sunk below the street level of both banks, gentle grassy slopes rising up to the banks;
preserved rails with wooden sleepers running along the floor of the cutting beneath the bridge;
a quiet park path on the cutting floor with tree rows; mid-rise blocks on both banks;
simple stair and ramp landings on both sides of the bridge.

STATE - DAILY: people and cyclists crossing the bridge from both directions;
the preserved rails in the cutting clearly visible through the semi-transparent deck directly below the walkers;
strollers and a bench along the park path on the cutting floor; ordinary soft daylight.

square 1:1 aspect ratio composition, all elements within frame, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```

### prompt-z03.txt

SHA-256: `1e921e16653d6070b4488ef4315625b982db8c8ce1df33db5a3ad7a343351ff2`

```text
professional urban design principle diagram, axonometric cutaway section view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for new infrastructure,
soft sage green landscape, small simple human silhouettes, competition-grade diagram illustration.

SCENE: a public underpass crossing beneath a high grassed railway embankment,
where the opening has been cut upward into the roadbed itself:
the complete historical roadbed cross-section is exposed above the passage as an open specimen layer —
subgrade soil, ballast stones, wooden sleepers and the two old steel rails are all retained overhead,
visible in true section above the arch opening, like an exhibited earth sample built into the structure;
pedestrian passage and separated cycle lane through the underpass;
the rest of the embankment continues intact with tree rows on top;
mid-rise blocks on both banks.

STATE: single everyday scene; pedestrians and cyclists passing through in both directions;
soft daylight raking across the exposed section; ordinary functional lighting.

square 1:1 aspect ratio composition, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```

### prompt-z04.txt

SHA-256: `59c07ed73befccae5d981b4ce2908786ab2465b2e20c51f714b09e1abfa1ceb3`

```text
professional urban design principle diagram, axonometric three-quarter view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, warm timber and rope tones for play structures,
soft sage green landscape, small simple human silhouettes, competition-grade diagram illustration.

SCENE: an old masonry railway viaduct with arched spans, the preserved rails and wooden sleepers
with low planting running along its top as a heritage line;
the arch structure itself converted into a children's climbing playground:
rope climbing nets stretched between the arch piers, timber platforms and ladders on the spandrel walls,
two curved slides wrapping down the embankment sides, climbing holds set into the stone arch faces,
a soft sand and rubber play surface beneath the arches;
parents resting on benches beside the arches, children climbing up down and through;
mid-rise residential blocks around; small trees along the street.

STATE: single everyday scene, bright soft daylight, lively but safe play atmosphere.

square 1:1 aspect ratio composition, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```

### prompt-z05.txt

SHA-256: `2b6fcf57f85945c048a3b5342b7fecf2953dee17a84fcb0515786606c2cb1964`

```text
professional urban design principle diagram, axonometric three-quarter view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for new infrastructure,
soft sage green landscape, small simple human silhouettes, competition-grade diagram illustration.

SCENE: an at-grade crossing where small autonomous delivery vehicles cross the preserved railway corridor
on their delivery rounds;
the rails with wooden sleepers embedded flush in the paving, tops level with the street surface;
a small unmanned delivery vehicle with a compact cargo box mid-crossing over the rails,
another waiting at a simple marked stop on the far side;
dedicated narrow lanes with guide dots for the robots on both approaches;
shops and small workshops receiving deliveries at their doors, a courier handing a parcel to a shopkeeper;
pedestrians passing and giving way naturally; tree rows of the linear heritage park flanking the corridor;
mid-rise blocks in the background.

STATE: single everyday scene, bright soft daylight, calm ordinary delivery flow.

square 1:1 aspect ratio composition, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```

### prompt-z06-a.txt

SHA-256: `87cc5c44ef8e0842bedaf584c4e4d9df3bc3377e8c874b786f702728b5dd838e`

```text
professional urban design principle diagram, axonometric three-quarter view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for new infrastructure,
soft sage green landscape, small simple silhouettes, competition-grade diagram illustration.

SCENE: the green railway corridor lying flat at surrounding street level, threading between dense mid-rise urban blocks,
its preserved rails running through;
small rooftop drone ports with landing pads on mid-rise blocks of both banks;
a discreet mid-altitude flight corridor indicated along the rail alignment above the corridor;
street life, trees and pedestrians at ground level normal on both banks.

STATE - DAILY: a few small logistics drones flying in an orderly single line at mid altitude
along the corridor alignment, small and unobtrusive; ordinary soft daylight;
the street scene below unaffected, people walking and cycling.

square 1:1 aspect ratio composition, all elements within frame, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```

### prompt-z06-b.txt

SHA-256: `72ad9c2ebe0643f747170ce97d6faf581ba66fdd981eaf9b934668c991417bb4`

```text
Identical axonometric principle diagram of the exact same scene as the reference image —
same camera angle, same composition, same corridor and blocks and rooftop drone ports,
same drawing style and palette.
Only the following changes, everything else stays exactly the same:

STATE - CEREMONIAL, night: hundreds of small drones forming one long glowing light formation
in the shape of a steam locomotive with carriages, running along the former rail alignment
above the dark corridor; the light train rendered as points of warm gold and soft cyan;
crowds standing along the linear park below looking up;
the same buildings and tree rows in deep blue night tones.

professional urban design principle diagram, same soft off-white paper base with night tint,
same corridor geometry, gold and cyan light formation as focal accent,
square 1:1 aspect ratio composition, all elements within frame, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, oversaturated colors, fisheye distortion
```

### prompt-z07.txt

SHA-256: `c59702c6676a733d15ff9ef05db8e25baeba33b8fc695633878b0528cbd65dd8`

```text
professional urban design principle diagram, axonometric cutaway section view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for infrastructure,
soft sage green landscape, small simple human silhouettes, competition-grade diagram illustration.

SCENE: a utility duct tunnel crossing PERPENDICULAR beneath the green railway corridor,
connecting the municipal networks of both banks:
on the near bank a vertical service shaft with a small access headhouse;
the rectangular duct runs straight across beneath the rail bed at generous depth,
its two portal ends visible in cutaway on both embankment slopes;
inside the duct, layered pipes and conduits (water, energy, telecom, computing) with a narrow walkway;
branch risers rise from both duct ends toward the mid-rise blocks of each bank;
on the surface above, the preserved rails with wooden sleepers run undisturbed
through their green meadow bed with tree rows — the crossing below is completely invisible from the track;
a small marker disc on the lawn indicates the crossing line.

STATE: single everyday scene; one technician walking inside the duct with a lamp;
people strolling the corridor path above; ordinary soft daylight.

square 1:1 aspect ratio composition, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, tunnel parallel to the rails, oversaturated colors, fisheye distortion
```

### prompt-z08-a.txt

SHA-256: `8e21feac1a6f068a5c03bdeb87ac05fa143e8cf91d41ebc85c7b87b9b98c6052`

```text
professional urban design principle diagram, axonometric three-quarter cutaway view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for new buildings,
soft sage green landscape, small simple human silhouettes, competition-grade diagram illustration.

SCENE: a podium building straddling the railway corridor — the preserved rails with wooden sleepers
passing at surrounding plaza level beneath the building's central hall through an open ground-level gap;
a continuous public passage at plaza level connecting east and west banks through the building;
narrow glass floor strips in the elevated hall above the tracks;
the green rail corridor continuing outdoors beyond the building in both directions;
mid-rise blocks around on both banks.

STATE - DAILY: people flowing through the ground-level passage and the elevated hall,
crossing from east to west inside the building; office life around the podium;
the glass floor strips quietly showing the rails below; ordinary soft daylight.

square 1:1 aspect ratio composition, all elements within frame, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```

### prompt-z09.txt

SHA-256: `ab6059c82bf06b08527a7b6081836934ce09e569e7453c38adf3576950beba93`

```text
professional urban design principle diagram, axonometric three-quarter view,
soft off-white paper base with warm night tint, clean thin technical linework with gentle watercolor shading,
muted palette: warm bronze-brown for preserved railway heritage elements, warm amber and soft cyan for night light,
small simple human silhouettes, competition-grade diagram illustration.

SCENE: two rows of low-rise commercial streets extending along BOTH banks of the railway corridor,
treating the corridor like a canal — the two preserved rails with wooden sleepers embedded
in a narrow landscaped water-garden bed in the middle, glowing softly with track-edge light lines;
on each bank: continuous terraces of small restaurants cafes and shops with warm lit storefronts,
outdoor seating facing the rails, string lights strung between trees;
small wooden decks bridging over the track bed connecting the two streets at intervals;
people strolling dining and crossing on both banks; mid-rise blocks rising behind the commercial strip.

STATE: single night scene, deep blue night sky, warm amber dominant lighting,
the track-bed light lines as soft cyan accents; lively but relaxed evening atmosphere.

square 1:1 aspect ratio composition, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, oversaturated colors, fisheye distortion
```

### prompt-z10-a.txt

SHA-256: `a5508325ddec82e663e230b29025b65489c99a60674abfd057f69966dd3d123d`

```text
professional urban design principle diagram, axonometric three-quarter cutaway view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, steel blue-grey for new infrastructure,
soft sage green landscape, small simple silhouettes, competition-grade diagram illustration.

SCENE: a generously planted green wildlife overpass crossing over the railway corridor,
connecting two park systems on the banks; dense shrubs and young trees on the bridge deck;
a narrow pedestrian lane along one edge of the bridge;
the preserved rails running in a shallow grassy cutting beneath the green bridge through its open span;
both banks continuing as park meadows with tree groups.

STATE - DAILY, soft morning light: a hare and a few birds crossing the planted deck as simple silhouettes;
one or two people walking the edge lane; the rails below running quietly through the shade of the bridge.

square 1:1 aspect ratio composition, all elements within frame, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```

### prompt-z10-b.txt

SHA-256: `19220cdc27b98f5d4a4c73338fe5ca37d09ba37eab59f505d4c814a28ef3b344`

```text
professional urban design principle diagram, axonometric three-quarter view,
soft off-white paper background, clean thin technical linework with gentle watercolor-like material shading,
muted palette: warm bronze-brown for preserved railway heritage elements, soft sage green landscape,
small simple human silhouettes, competition-grade diagram illustration.

SCENE: a broad flat community park lying at the same level as the surrounding city,
with the preserved railway corridor embedded flush within the lawn;
old steel rails and wooden sleepers set into the grass as two heritage lines crossing the park,
their tops level with the mown lawn;
winding footpaths sweep continuously from the west side to the east side across the rails,
stitching both neighbourhoods into one park;
scattered tree groups, picnic blankets, people walking cycling and playing across the whole park;
a small pavilion and a children's play mound; mid-rise blocks on both sides beyond the park edges.

STATE: single everyday scene, soft warm daylight, long gentle shadows.

square 1:1 aspect ratio composition, no text, no numbers, no labels

Negative prompt: photorealistic photograph, text, letters, numbers, labels, dimension annotations, watermark, logo, cartoon style, dark background, oversaturated colors, fisheye distortion
```


## Appendix B — Bilingual Cross-Check Record (2026-08-31)

Manual zh–en substantive equivalence check of proposal.md / proposal.en.md, report/proposal(.en).html, visual/index(.en).html, the six bilingual figure pairs (site-overview, land-use-structure, key-areas, mobility-bluegreen, metrics-evidence, wings-synergy) and the A3/A0 drawings, performed after the review-repair batch:

- Chapter parity: 15 / 15 top-level chapters; section order mirrored (three zones & two wings loop, regional synergy interfaces, per-card six-element matrix, component library, inclusivity matrix, stage-gate table, long-term operations).
- Table parity: 47 / 47 markdown tables; all rows one-to-one (case table 6 rows, scenario matrix 11 rows, maturity table 5 rows, component library 8 rows, inclusivity matrix 6 groups, stage-gate 6 projects, operations 6 mechanisms).
- Claims, metrics and warnings parity: site_area_sqm 11,412,825 m²; green_ratio 18%; public_space_ratio 1%; band 9.72 km; tooth_count 10; FAR unknown — identical in both languages; provisional (official_boundary=false) warnings present in both.
- Figure language attribution corrected: zh figures carry Chinese labels, .en figures English labels (key-areas pair swapped-label defect fixed; land-use-structure .en legend translated); visual/index.en.html non-proper-noun Chinese residue removed (remaining CJK = brand name 拉链京张 and verbatim GeoJSON enum quotes in the source registry).
- Evidence markers preserved in both languages with the ≤3-consecutive / ≤8-per-section discipline.

Result: PASS — the two language versions are substantively equivalent; no untranslated residue other than brand proper nouns and verbatim data-registry quotes.

### Appendix B.2 — R4 cross-carrier consistency round (2026-08-31)

- proposal.en.md figure mapping corrected: all five required figures now reference the .en.png counterparts (site-overview / land-use-structure / key-areas / mobility-bluegreen / metrics-evidence); report/proposal.en.html re-rendered accordingly.
- A3 booklets (zh/en) re-composed after pages 2 & 8 re-shot with the corrected 0.8% public-space figure; A0 boards (zh/en) re-exported with the same correction. All carriers now state public_space_ratio = 0.8% (0.008157) consistently.
- Gate rerun after changes: self_check ok=true, formal-review-ready.

### Appendix B.3 — R5 cross-carrier round (2026-08-31)

- drawings/a0-boards.en.pdf regenerated: the two overview maps on page 1 now embed site-overview.en.png and land-use-structure.en.png (was: zh versions); zh A0 unchanged (correctly zh).
- visual/index(.en).html regenerated with package_state badge synchronized to manifest (ready_for_review); manifest hashes for both files refreshed.
- Gate rerun: self_check ok=true, formal-review-ready.
