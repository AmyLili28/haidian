# Design Media Rights and Evidence Boundary / 设计媒体权利与证据边界

## Scope / 范围

This note covers the WebP files under `assets/media/design/`. The current package has sixteen Imagegen-generated or Imagegen-cleaned concept sections, aerial views, human views, and design-method diagrams plus four plan-oriented OpenFreeMap Positron / OpenStreetMap public-basemap composites with participant concept overlays. All four map composites are packaged and their final WebP dimensions, byte counts, and hashes are verified in `visual/assets/design-media-index.json`.

本说明覆盖 `assets/media/design/` 下的 WebP 文件。当前包包含16张使用 Imagegen 生成或清理的概念剖面、鸟瞰、人视与设计方法图，以及4张本地导出的 OpenFreeMap Positron / OpenStreetMap 公开底图叠加参赛者概念标注的总平向图。4张公开底图叠加图均已进入包内，其最终 WebP 尺寸、字节数和哈希已在 `visual/assets/design-media-index.json` 中核验。

## Generation and processing / 生成与处理

- Generation service for the 16 concept items: Codex built-in Imagegen / OpenAI image generation service.
- Public-basemap source for the four map composites: OpenFreeMap Positron style with OpenStreetMap data; the exact style URL, bounds, source hashes and attribution are in `visual/assets/imagery-source-ledger.json`.
- Production/render date: 2026-08-29 to 2026-08-30 (Asia/Shanghai).
- Final packaging: concept PNGs and public-basemap rasters were converted to RGB WebP without changing their intended extent; compression does not create additional factual detail. The four public-basemap composites were re-hashed after conversion and their verified package hashes are recorded in the media index and imagery ledger.
- The files contain no raw satellite mosaic, remote tile cache, service response, CAD/GIS export, or directly redistributed reference photograph.

- 16张概念媒体的生成服务：Codex 内置 Imagegen / OpenAI 图像生成服务。
- 4张公开底图叠加图的来源：OpenFreeMap Positron 样式与 OpenStreetMap 数据；样式 URL、范围、源文件哈希和署名记录在 `visual/assets/imagery-source-ledger.json`。
- 制作/导出日期：2026-08-29 至 2026-08-30（Asia/Shanghai）。
- 最终打包：概念 PNG 与公开底图栅格已在不改变预期范围的前提下转换为 RGB WebP；压缩不会增加事实细节。4张公开底图叠加图转换后的哈希已经复核，并登记在媒体索引和影像台账中。
- 文件中不包含原始卫星拼图、远程瓦片缓存、服务响应、CAD/GIS 导出或直接再分发的参考照片。

Some wide-area and district images were generated with reviewed site context as a morphological constraint. Sentinel-2, OSM, public anchors, cleared public photographs, and a local-only Esri/Vantor reference were used at different stages of internal interpretation. The raw Esri/Vantor mosaic, crops, tiles, service responses, and reconstructable cache remain excluded from this public package. Because a competition-specific determination on generated derivatives has not been independently issued, final public/commercial rights review remains pending; this limitation is not converted into a claim of clearance.

部分宽域与片区图在生成时把已复核的场地上下文作为城市肌理约束；内部判读阶段分别使用过 Sentinel-2、OSM、公开锚点、清权公开照片和仅限本地参考的 Esri/Vantor 影像。Esri/Vantor 原始拼图、裁片、瓦片、服务响应及可重建缓存均未进入本公开包。由于尚无针对“生成式衍生图”的赛事专项独立权利结论，最终公开/商业权利复核仍为待办；本说明不会把该待办改写成已清权结论。

Context attribution: Contains modified Copernicus Sentinel data 2026. Public-basemap composites retain the exact line `© OpenStreetMap contributors · OpenFreeMap`; OpenStreetMap data are under ODbL 1.0 and OpenFreeMap service/style terms apply. Local interpretation reference: Source: Esri, Vantor, Earthstar Geographics, and the GIS User Community; raw reference excluded from distribution.

上下文署名：Contains modified Copernicus Sentinel data 2026。公开底图叠加图保留统一署名 `© OpenStreetMap contributors · OpenFreeMap`；OpenStreetMap 数据遵循 ODbL 1.0，OpenFreeMap 服务/样式条款适用。本地判读参考：Source: Esri, Vantor, Earthstar Geographics, and the GIS User Community；原始参考不进入公开分发。

## Public basemaps and contextual photographs / 公开底图与场地语境照片

The four plan-oriented files — `overall-masterplan-4k.webp`, `north-local-plan-4k.webp`, `central-local-plan-4k.webp`, and `south-local-plan-4k.webp` — use locally rendered OpenFreeMap Positron / OpenStreetMap public cartography as a legible context layer, with participant labels, temporary study extents and concept overlays. They are packaged static display composites, not live map views: no remote tile request, tile cache, service response, or reconstructable tile bundle is included. The exact source PNG hashes, bounds, bearing, package path, dimensions, byte counts, and verified final WebP hashes are in `visual/assets/imagery-source-ledger.json#public_map_records` and `visual/assets/design-media-index.json#public_context_assets`.

四个总平向文件——`overall-masterplan-4k.webp`、`north-local-plan-4k.webp`、`central-local-plan-4k.webp` 和 `south-local-plan-4k.webp`——使用本地导出的 OpenFreeMap Positron / OpenStreetMap 公开制图作为可读上下文层，并叠加参赛者标注、临时研究范围和概念层；它们现已作为静态显示合成图进入包内，而非在线地图，不包含远程瓦片请求、瓦片缓存、服务响应或可还原的瓦片包。源 PNG 哈希、范围、方向、包内路径、尺寸、字节数及已核验的最终 WebP 哈希记录在 `visual/assets/imagery-source-ledger.json#public_map_records` 与 `visual/assets/design-media-index.json#public_context_assets`。

The three contextual photographs referenced in external PPT slides S14, S18 and S22 are Wikimedia Commons files by N509FZ, each marked CC BY-SA 4.0. Only the inherited slide-frame crop was made; no generative alteration was applied. Their source pages, direct URLs, capture dates, dimensions, hashes, attribution strings, slide placement and third-party-rights caveats are recorded in `visual/assets/imagery-source-ledger.json#public_context_photo_records` and `visual/assets/design-media-index.json#public_context_assets`. They remain external-PPT references and are not copied into this repository submission package; if later packaged, the package path, manifest hash and share-alike notice must be refreshed.

外部 PPT 第 S14、S18、S22 页引用的三张场地语境照片均来自 Wikimedia Commons，作者为 N509FZ，许可均为 CC BY-SA 4.0。仅按既有页面图片框裁剪，未作生成式改动。来源页、直链、拍摄日期、尺寸、哈希、署名串、页面落位和第三方权利提示记录在 `visual/assets/imagery-source-ledger.json#public_context_photo_records` 与 `visual/assets/design-media-index.json#public_context_assets`。它们目前仅作为外部 PPT 语境引用，不复制进本仓库投稿包；如后续纳入投稿包，必须重新登记包内路径、manifest 哈希和同方式共享说明。

The OSM/OpenFreeMap composites and the photographs are contextual communication aids. They do not establish an official boundary, survey, cadastral fact, building height, ownership, heritage control line, engineering condition, approval, implementation status or public acceptance. OpenStreetMap ODbL obligations, OpenFreeMap terms, CC BY-SA attribution/share-alike obligations, and separate rights of people, buildings, signs, vehicles, venues and property remain applicable. No competition-specific or commercial clearance is claimed by this note.

OSM/OpenFreeMap 叠加图与照片均为语境传播辅助材料，不证明官方边界、测绘、地籍事实、建筑高度、权属、文保控制线、工程现状、审批、实施状态或公众接受。OpenStreetMap 的 ODbL 义务、OpenFreeMap 条款、CC BY-SA 的署名/同方式共享义务，以及人物、建筑、标识、车辆、场地和物业的独立权利仍然适用。本说明不主张已取得赛事专项或商业清权。

## Mandatory reading rule / 强制阅读规则

Every design-media item is a **communication composite**: either an AI-generated/AI-cleaned concept expression or a public-basemap raster with participant concept overlay. Neither category is a site photograph, survey drawing, official redline, statutory plan, official rendering, construction drawing, field validation record, or proof of approval, procurement, operation, performance, or public acceptance. Apparent buildings, roads, water, landscape, people, dimensions, and distances are illustrative. The authoritative audit layer remains `geometry/*.geojson`, `metrics.json`, the structured matrices, and the persisted self-check; all spatial anchoring and release decisions remain subject to professional review and `HumanDecision`.

所有设计媒体均为 **传播合成图**：要么是 AI 生成/清理的概念表达，要么是公开底图栅格与参赛者概念叠加。两类都不是现场照片、测绘图、官方红线、法定规划、官方效果图、施工图、现场验证记录，也不证明审批、采购、运行、绩效或公众接受。画面中的建筑、道路、水体、景观、人物、尺寸与距离均为示意。权威审计层仍为 `geometry/*.geojson`、`metrics.json`、结构化矩阵与已持久化自检；所有空间终锚和发布决定仍须专业复核与 `HumanDecision`。

## Rights status / 权利状态

The project retains the 16 concept outputs as proposal-owned generated media subject to the generation service terms. The four basemap composites remain subject to OpenStreetMap ODbL 1.0, OpenFreeMap service/style terms and the attribution above. The three photographs remain CC BY-SA 4.0 context references with attribution/share-alike obligations and separate third-party-rights review; they are not copied into this repository package. This note is a provenance and risk disclosure, not a legal opinion. Before public release or commercial reuse, the responsible submitter should retain this note and complete the competition/platform-specific review of generated-output, map-data and reference-use terms.

项目依生成服务条款将16张概念媒体作为方案自有生成媒体保留。4张公开底图叠加图受 OpenStreetMap ODbL 1.0、OpenFreeMap 服务/样式条款及上述署名约束；3张照片为带署名/同方式共享义务的 CC BY-SA 4.0 语境引用，不复制进本仓库投稿包，且需单独复核第三方权利。本说明是来源与风险披露，不构成法律意见。公开发布或商业复用前，责任提交人应保留本说明，并完成赛事/平台对生成输出、地图数据和参考资料使用条款的专项复核。
