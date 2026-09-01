# Design Media Rights and Evidence Boundary / 设计媒体权利与证据边界

## Scope / 范围

This note covers the 22 WebP files under `assets/media/design/`: fourteen Imagegen-generated or Imagegen-cleaned concept sections, aerial views, human views, and design-method diagrams; four participant-authored bilingual 4K analytical plates using structured submission data and already-registered concept support media; and four plan-oriented OpenFreeMap Positron / OpenStreetMap public-basemap composites with participant concept overlays. Dimensions, byte counts, and hashes are verified in `visual/assets/design-media-index.json`.

本说明覆盖 `assets/media/design/` 下的22张 WebP 文件：14张使用 Imagegen 生成或清理的概念剖面、鸟瞰、人视与设计方法图；4张以投稿结构化数据和已登记概念支撑媒体组成的参赛者自制双语4K分析图；以及4张本地导出的 OpenFreeMap Positron / OpenStreetMap 公开底图叠加参赛者概念标注的总平向图。全部文件的尺寸、字节数和哈希已在 `visual/assets/design-media-index.json` 中核验。

## Generation and processing / 生成与处理

- Generation service for the 14 Imagegen concept items: Codex built-in Imagegen / OpenAI image generation service. The four bilingual Agent-comparison/spatial-grammar plates are participant-authored analytical compositions; their support visuals are already-registered concept media and their labels/values come from the submitted structured evidence.
- Public-basemap source for the four map composites: OpenFreeMap Positron style with OpenStreetMap data; the exact style URL, bounds, source hashes and attribution are in `visual/assets/imagery-source-ledger.json`.
- Production/render date: 2026-08-29 to 2026-08-30 (Asia/Shanghai).
- Final packaging: concept PNGs and public-basemap rasters were converted to RGB WebP without changing their intended extent; compression does not create additional factual detail. The four public-basemap composites were re-hashed after conversion and their verified package hashes are recorded in the media index and imagery ledger.
- The files contain no raw satellite mosaic, remote tile cache, service response, CAD/GIS export, or directly redistributed reference photograph.

- 14张 Imagegen 概念媒体的生成服务：Codex 内置 Imagegen / OpenAI 图像生成服务。4张双语 Agent 比较/空间语法图为参赛者自制分析合成图；支撑视觉来自已登记概念媒体，图中文字与数值来自投稿结构化证据。
- 4张公开底图叠加图的来源：OpenFreeMap Positron 样式与 OpenStreetMap 数据；样式 URL、范围、源文件哈希和署名记录在 `visual/assets/imagery-source-ledger.json`。
- 制作/导出日期：2026-08-29 至 2026-08-30（Asia/Shanghai）。
- 最终打包：概念 PNG 与公开底图栅格已在不改变预期范围的前提下转换为 RGB WebP；压缩不会增加事实细节。4张公开底图叠加图转换后的哈希已经复核，并登记在媒体索引和影像台账中。
- 文件中不包含原始卫星拼图、远程瓦片缓存、服务响应、CAD/GIS 导出或直接再分发的参考照片。

The only explicitly logged local site-image inputs to the early north, central, and south site-grounded Imagegen concepts were the processed Sentinel-2 crops `zhongzhiyuan-context-neutral.png`, `ai-origin-context-neutral.png`, and `dazhongsi-context-neutral.png`. Their SHA-256 values — `96ec0c49098d63b6c89601b3f4154a789ef29ecaa14c0dc26e551e72a02c5029`, `1ece2413ba11b68f4097a80385b159bf5efd8c10c28a12e0777388cd7a037ca9`, and `a035e7c4d3863ecd7a1a132f31038adb8a83400e3939eb93dacbbdbfbdce867a` — match the archived Sentinel-2 imagery manifest. No Esri/Vantor image was uploaded for those generations. The later Esri/Vantor mosaic was used only for local human plausibility checking; it was not a recorded Imagegen input and neither it nor any crop, tile, service response, or reconstructable cache enters this package. OSM and public anchors supply orientation facts. Three earlier Wikimedia photo references are retained only as historical audit records in the imagery ledger; they were removed from the current v4.3 PPT and are not present in this repository package.

The generated outputs are retained under the OpenAI Terms of Use published/effective 2026-01-01: as between the user and OpenAI, the user owns Output and OpenAI assigns any rights it has in Output. The same terms leave responsibility for Input rights with the user and warn that output may not be unique. OpenAI Service Terms updated 2026-06-12 additionally require the necessary rights and consents for visual inputs and people. These terms support submission and display of the generated output but do not convert the images into site evidence or a legal opinion.

早期北、中、南三张场地约束 Imagegen 概念图中，项目记录明确列出的本地场地图像输入只有 Sentinel-2 处理裁片 `zhongzhiyuan-context-neutral.png`、`ai-origin-context-neutral.png` 与 `dazhongsi-context-neutral.png`。其 SHA-256 分别为 `96ec0c49098d63b6c89601b3f4154a789ef29ecaa14c0dc26e551e72a02c5029`、`1ece2413ba11b68f4097a80385b159bf5efd8c10c28a12e0777388cd7a037ca9` 和 `a035e7c4d3863ecd7a1a132f31038adb8a83400e3939eb93dacbbdbfbdce867a`，与归档 Sentinel-2 影像清单一致。上述生成没有上传 Esri/Vantor 图像。后续 Esri/Vantor 拼图只用于本地人工合理性核对，不是已记录的 Imagegen 输入；拼图、裁片、瓦片、服务响应及可重建缓存均未进入本包。OSM 和公开锚点只提供方位事实。三张早期 Wikimedia 照片仅在影像台账保留为历史审计记录，已从当前 v4.3 PPT 移除，也未进入本仓库包。

生成输出依据 2026-01-01 发布/生效的 OpenAI Terms of Use 保留：在用户与 OpenAI 之间，用户拥有 Output，OpenAI 将其在 Output 中拥有的权利转让给用户；同一条款仍由用户负责 Input 权利，并提示输出可能不唯一。2026-06-12 更新的 OpenAI Service Terms 进一步要求视觉输入及人物具备必要权利/同意。上述条款支持本次赛事提交和展示生成输出，但不把图像转化为场地证据，也不构成法律意见。

Official terms: `https://openai.com/policies/terms-of-use/` (published/effective 2026-01-01) and `https://openai.com/policies/service-terms/` (updated 2026-06-12). Context attribution: `Contains modified Copernicus Sentinel data 2026`. Every public-basemap composite uses `© OpenStreetMap contributors | OpenFreeMap © OpenMapTiles`; OpenStreetMap data are under ODbL 1.0, and OpenFreeMap states that commercial usage is allowed and requires printed/video attribution `OpenFreeMap © OpenMapTiles Data from OpenStreetMap`. Local interpretation reference: `Source: Esri, Vantor, Earthstar Geographics, and the GIS User Community`; raw reference excluded from distribution.

官方条款：`https://openai.com/policies/terms-of-use/`（2026-01-01 发布/生效）与 `https://openai.com/policies/service-terms/`（2026-06-12 更新）。上下文署名：`Contains modified Copernicus Sentinel data 2026`。每张公开底图叠加图使用 `© OpenStreetMap contributors | OpenFreeMap © OpenMapTiles`；OpenStreetMap 数据遵循 ODbL 1.0，OpenFreeMap 官方说明允许商业使用，印刷/视频需署名 `OpenFreeMap © OpenMapTiles Data from OpenStreetMap`。本地判读参考：`Source: Esri, Vantor, Earthstar Geographics, and the GIS User Community`；原始参考不进入公开分发。

## Public basemaps and contextual photographs / 公开底图与场地语境照片

The four plan-oriented files — `overall-masterplan-4k.webp`, `north-local-plan-4k.webp`, `central-local-plan-4k.webp`, and `south-local-plan-4k.webp` — use locally rendered OpenFreeMap Positron / OpenStreetMap public cartography as a legible context layer, with participant labels, temporary study extents and concept overlays. They are packaged static display composites, not live map views: no remote tile request, tile cache, service response, or reconstructable tile bundle is included. The exact source PNG hashes, bounds, bearing, package path, dimensions, byte counts, and verified final WebP hashes are in `visual/assets/imagery-source-ledger.json#public_map_records` and `visual/assets/design-media-index.json#public_context_assets`.

四个总平向文件——`overall-masterplan-4k.webp`、`north-local-plan-4k.webp`、`central-local-plan-4k.webp` 和 `south-local-plan-4k.webp`——使用本地导出的 OpenFreeMap Positron / OpenStreetMap 公开制图作为可读上下文层，并叠加参赛者标注、临时研究范围和概念层；它们现已作为静态显示合成图进入包内，而非在线地图，不包含远程瓦片请求、瓦片缓存、服务响应或可还原的瓦片包。源 PNG 哈希、范围、方向、包内路径、尺寸、字节数及已核验的最终 WebP 哈希记录在 `visual/assets/imagery-source-ledger.json#public_map_records` 与 `visual/assets/design-media-index.json#public_context_assets`。

Three Wikimedia Commons photographs by N509FZ were used in earlier external-PPT drafts at historical slides S14, S18, and S22. They have been removed from the current v4.3 PPT and replaced by participant-generated concept media, so no current PPT slide or repository artifact depends on them. Their source pages, capture details, licenses, hashes, and historical placements remain in `visual/assets/imagery-source-ledger.json#public_context_photo_records` solely as an audit trail; they are excluded from `visual/assets/design-media-index.json#public_context_assets` and from the package media count.

作者 N509FZ 的三张 Wikimedia Commons 照片曾用于较早的外部 PPT 草稿历史页 S14、S18、S22；当前 v4.3 PPT 已全部移除并以参赛者生成的概念媒体替换，因此现役 PPT 和仓库成果均不再依赖这些照片。来源页、拍摄信息、许可、哈希与历史页位仅保留在 `visual/assets/imagery-source-ledger.json#public_context_photo_records` 作为审计轨迹；它们已从 `visual/assets/design-media-index.json#public_context_assets` 和包内媒体计数中移除。

The OSM/OpenFreeMap composites are contextual communication aids. They do not establish an official boundary, survey, cadastral fact, building height, ownership, heritage control line, engineering condition, approval, implementation status or public acceptance. OpenStreetMap ODbL obligations, OpenFreeMap attribution, and separate rights of people, buildings, signs, vehicles, venues and property remain applicable. The four static map composites are cleared for competition submission, public repository display, and redistribution as part of this attributed static package under those terms. The historical Wikimedia records neither enter nor support the current package.

OSM/OpenFreeMap 叠加图是语境传播辅助材料，不证明官方边界、测绘、地籍事实、建筑高度、权属、文保控制线、工程现状、审批、实施状态或公众接受。OpenStreetMap 的 ODbL 义务、OpenFreeMap 署名，以及人物、建筑、标识、车辆、场地和物业的独立权利仍然适用。四张静态底图叠加图按上述条款完成赛事提交、公开仓库展示及作为本署名静态包组成部分再分发的复核；历史 Wikimedia 记录既不进入、也不支撑当前包。

## Mandatory reading rule / 强制阅读规则

Every design-media item is a **communication composite**: either an AI-generated/AI-cleaned concept expression or a public-basemap raster with participant concept overlay. Neither category is a site photograph, survey drawing, official redline, statutory plan, official rendering, construction drawing, field validation record, or proof of approval, procurement, operation, performance, or public acceptance. Apparent buildings, roads, water, landscape, people, dimensions, and distances are illustrative. The authoritative audit layer remains `geometry/*.geojson`, `metrics.json`, the structured matrices, and the persisted self-check; all spatial anchoring and release decisions remain subject to professional review and `HumanDecision`.

所有设计媒体均为 **传播合成图**：要么是 AI 生成/清理的概念表达，要么是公开底图栅格与参赛者概念叠加。两类都不是现场照片、测绘图、官方红线、法定规划、官方效果图、施工图、现场验证记录，也不证明审批、采购、运行、绩效或公众接受。画面中的建筑、道路、水体、景观、人物、尺寸与距离均为示意。权威审计层仍为 `geometry/*.geojson`、`metrics.json`、结构化矩阵与已持久化自检；所有空间终锚和发布决定仍须专业复核与 `HumanDecision`。

## Rights status / 权利状态

`rights_review_status = cleared_for_current_competition_submission_repository_display_and_attributed_package_redistribution`.

The 18 concept outputs (14 Imagegen items and four participant-authored bilingual analytical plates) are participant-owned generated/composed media for proposal communication under the cited OpenAI terms and recorded source boundaries. The four static basemap composites remain under OpenStreetMap ODbL 1.0 and OpenFreeMap attribution/terms; required attribution is visible in the figures and preserved in the registries. Noto Sans SC is embedded and redistributed under SIL OFL 1.1, which permits use, embedding, modification, and redistribution subject to its conditions and prohibition on selling the font by itself. The front-matter token `COMMUNITY-DISPLAY-ONLY` limits the participant-authored proposal's intended community-display reuse; it does not add a restriction to, supersede, or relicense underlying OSM/OpenFreeMap data, the font, or any other third-party component. Downstream users must keep each component's original terms and attribution.

The responsible submitter has completed the competition-specific review for the assets actually included in this repository package and clears them for this competition submission, public repository/gallery display, and redistribution as part of this attributed package. This statement is scoped to the current hashed package; it is not a legal opinion, does not cover material outside the current hashed package, and does not grant blanket commercial rights for extraction, remixing, or reuse outside the package. The current external-PPT third-party photograph count is zero; three historical reference photographs are retained only as non-packaged audit records and have been removed from the current deck. A materially changed asset, new input, removed attribution, standalone map/font redistribution, or another platform/use requires a fresh review.

`rights_review_status = cleared_for_current_competition_submission_repository_display_and_attributed_package_redistribution`。

18张概念输出（14张 Imagegen 媒体与4张参赛者自制双语分析图）依据上述 OpenAI 条款和已登记来源边界，作为参赛者自有生成/合成媒体用于方案传播。4张静态底图叠加图继续受 OpenStreetMap ODbL 1.0 与 OpenFreeMap 署名/条款约束，所需署名已在图面和台账保留。Noto Sans SC 按 SIL OFL 1.1 内嵌和再分发；该许可允许使用、嵌入、修改和再分发，但不得单独出售字体。front matter 中的 `COMMUNITY-DISPLAY-ONLY` 只限定参赛者自有方案的预期社区展示复用；它不会对 OSM/OpenFreeMap 数据、字体或其他第三方组成施加额外限制，不会覆盖原许可，也不会为其重新许可。下游使用者必须继续保留各组成的原始条款与署名。

责任提交人已对本仓库包实际包含的资产完成赛事专项复核，并允许其用于本赛事提交、公开仓库/画廊展示以及作为本署名包组成部分的再分发。本声明仅绑定当前哈希包，不构成法律意见，也不授予脱离本包后单独提取、混编或另作商业复用的概括性权利。已从当前 PPT 移除的三张历史 Wikimedia 照片不属于本包内容。若资产、输入、署名、单独地图/字体分发或平台/用途发生实质变化，必须重新复核。
