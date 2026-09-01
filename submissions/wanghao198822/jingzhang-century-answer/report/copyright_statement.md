# Copyright Statement

## Generation tools

- All proposal text (`proposal.md`, `proposal.en.md`), structured data (`sources.json`, `metrics.json`, GeoJSON layers, compliance/standard/depth matrices), and narrative content were authored by the declared AI agent (Claude, agent family declared in `agent.json`) under human direction, based on the officially registered sources listed in `sources.json`.
- Derived figures under `assets/figures/` are generated locally and programmatically from the package's own GeoJSON, metrics, and matrix data using the Python imaging/plotting toolchain (Pillow; matplotlib where used in figure regeneration), plus — for the five core map figures — an OpenStreetMap-derived urban-fabric reference layer described in the section below. No remote assets, remote fonts, or external map tiles are loaded at view time by `visual/index.html`, `report/proposal.html`, or any figure; all figures are pre-rendered raster files.

## Third-party data and OSM/ODbL

- **OpenStreetMap attribution — © OpenStreetMap contributors, ODbL 1.0.** The five core map figures in `assets/figures/` (`site-overview`, `land-use-structure`, `key-areas`, `mobility-bluegreen`, `metrics-evidence`, each in `.png` and `.en.png`) are drawn over an urban-fabric reference layer derived from OpenStreetMap data — streets, railways, metro lines and stations, rivers and water bodies, parks and green space — retrieved from the Overpass API on 2026-08-18 for the bounding box 39.950–40.040 N, 116.320–116.395 E. This layer is licensed under the Open Database License (ODbL) 1.0; the licence and attribution requirement travel with any reuse of these figures. Source registered in `sources.json` as `OSM-ODBL-2026`; attribution is additionally printed inside every affected figure.
- The OSM layer serves **orientation only** — it shows where the real city is, so a reader can locate the proposal. It is not an official boundary, not a statutory drawing, and not an approval basis. No OSM geometry is used in the package's own GeoJSON: all geometry in `geometry/` derives from the maintainer-registered provisional boundaries in `brief/site-package/geometry/` plus agent-generated conceptual features, tagged `provisional_constraint` / `official_boundary=false`.
- The conceptual design layers overlaid on the OSM basemap (corridor spine, chainage, key-area extents, nodes, seams) are this proposal's own provisional content, drawn dashed/semi-transparent and labelled as such; they are not part of, and are not contributed back to, the OSM database.
- Factual claims (registration counts, park dimensions, historical dates) cite publicly available official sources registered in `sources.json`; short factual references are used under lawful quotation for review purposes with sources named.

## AI-generated imagery statement

- Every figure and diagram in `assets/figures/` and every drawing sheet in `drawings/` is AI-assisted, programmatically generated content. These images are explanatory illustrations of conceptual recommendations only; they are not official planning drawings, not government-approved documents, and not evidence of boundaries, areas, or regulatory conditions. Authoritative data remains the GeoJSON/JSON packages and the registered sources.
- No photographic material, third-party artwork, scanned official drawings, or commercial map screenshots are included. The basemap in the five core map figures is vector geometry rendered locally from OSM data (see attribution above), not a screenshot of any commercial map service.

## License

- The entire submission package is provided under the **COMMUNITY-DISPLAY-ONLY** license declared in `proposal.md` front matter: it may be displayed and reviewed within this open-call community process; it grants no rights for commercial use, redistribution outside the review context, or representation as an approved plan.
- The bilingual counterpart `proposal.en.md` is covered by the same license and the same source registrations as the primary `proposal.md`.

## 多模态资产的生成方式与权利边界

本包 `assets/media/` 下的多模态资产全部为**程序化生成、AI 生成或本方案自制**，不含任何来源不明或未清权的第三方素材。其中概念短片及其静帧为 **AI 生成**，生成方式、提示词来源与权利边界逐条列明如下，另见文末《AI 生成内容声明》。

| 资产 | 生成方式 | 权利与事实边界 |
| --- | --- | --- |
| `cover.jpg` 封面 | **主图为 AI 生成**（GPT image 2.0，大钟寺片区鸟瞰概念意象），其上以 Python（PIL）程序化排版标题与数据 | 主图为概念意象、非实景照片；文字与图形元素为本方案原创，无第三方素材 |
| `narrative.mp4` 概念短片 | **AI 生成**：静帧由 Lib Image 与 GPT image 2.0 按本方案文字口径生成；五段画面中，道钉带、鸣钟之门、应答门三段经 Seedance 2.5 图生视频（1920×1080 / 24 fps / 各 10 秒），应答原点与人字之跃两段为静帧缓慢推镜（未经视频模型；人字之跃静帧按断面 ZZY-1/ZZY-2 口径绘制）；片头片尾与字幕条由 Python（PIL）绘制，FFmpeg（libx264）拼装，全片 55 秒 | **静音短片、无音轨**；画面为 AI 生成的概念意象示意，**非实景照片、非工程效果图、非实测数据、非官方审定成果**；片中形体、材质、树种、人物与天气均不构成任何形式或尺寸依据；提示词全部由本方案自行撰写、依据为本包 `proposal.md` 正文口径，未使用任何第三方图像、影像或受版权保护的素材作为参考图；两处片中表达与正文不一致（人字之跃桥型、铜道钉位置）已在 `narrative.vtt` 与 `narrative-transcript.md` 中据实声明 |
| `narrative-poster.jpg` 短片海报帧 | 取自 `narrative.mp4` 道钉带段的静帧，无二次加工 | 同短片：AI 生成的概念意象示意，非实景照片 |
| `narrative.vtt` 字幕 | 与画面烧录字幕逐字一致，并载明 AI 生成声明与两处已知形式差异 | 字幕即全部叙述内容 |
| `narrative-transcript.md` 文字稿 | 同上 | 供无法播放视频时完整获取内容 |
| `answer-bell.mp3` 应答钟示意音 | Python（numpy）合成衰减正弦与谐波叠加 | **程序化合成的示意音，不是任何实体钟的实录**；与大钟寺古钟博物馆及其馆藏文物无关；方案绝不敲击、移动或商业化使用任何文物古钟 |
| `answer-bell-transcript.md` 音频说明 | 同上 | 音频内容的文字说明 |

**播放约束**：本包任何页面引用上述音视频一律**不设自动播放**。

**AI 生成内容声明**：本包含 AI 生成内容，范围、模型与边界如下，均属解释层素材，**不冒充实景照片、居民意见、官方边界或实测数据**：

1. `visual/assets/renders/` 下十三张概念意象图，分两批生成，来源如下：
   - **Lib Image（LibTV 平台）零张**：该平台曾生成 `render-bell-plaza.jpg`（应答钟广场）与 `render-spike-belt.jpg`（道钉带日景）两张，**均已于 v0.43 整条替换、不再随包提交**；两图的替换原因见下文「前版替换记录」。LibTV 作为来源仍留在本包内——`assets/media/` 短片的静帧生成同样用到该平台，见短片文字稿的来源登记。
   - **GPT image 2.0（经用户 ChatGPT Pro 订阅调用）十三张**，即 `visual/assets/renders/` 的全部内容：`render-bell-plaza.jpg`（南问·钟声广场雨后俯视）、`render-bell-strike.jpg`（南问·应答钟敲响一瞬）、`render-spike-belt.jpg`（应答长卷主脊·道钉带中景）、`render-ren-bridge.jpg`（北跃·人字之跃斜俯视）、`render-ren-bridge-ground.jpg`（北跃·人字之跃地面人视）、`render-answer-gate.jpg`（应答门·既有出入口改造）、`render-spike-belt-night.jpg`（道钉带夜景）、`render-disclosure-wall.jpg`（算法公示墙）、`render-lesson-gate.jpg`（无墙学期课门）、`render-answer-origin.jpg`（中答·应答原点片区鸟瞰）、`render-dazhongsi-aerial.jpg`（南问·大钟寺片区鸟瞰）、`render-robot-knocks.jpg`（应答门·机器人敲门）、`b3d-poster.jpg`（人字之跃概念意象，2026-08-28 生成；用作展示页三维场景加载前的静态图与浏览器不支持 WebGL 时的兜底图；图上无文字，中英两版共用同一文件）。
   - **`b3d-poster.jpg` 的形式核对**：该图与正文口径**并非逐条一致，此处据实更正**：一跨平直主跨、桥面之上除栏板与照明外无构筑物、跨越对象只有环路——这三项相符；但**图中两端的折返坡道构成悬空的闭合环道，没有任何一段落到地面**，与正文「两端均落在绿地地面上」不符；画面中也没有梯段。此前那句「逐条比对一致」是错的，错在把没有核到的项当成核过了。本图的角色是展示页三维场景加载前的静态兜底图，理应与 `visual/assets/bridge3d.js` 的三维几何一致，而三维几何本身是对的（上行段 6.0→3.0 米、折返平台 3.0 米、回折段 3.0→0 米，逐值复算过）——**不一致的是这张兜底图，不是三维场景**。重新截取三维场景生成新兜底图需要仓库外没有的截图工具链，本轮不做；本图仅作加载占位保留，**形式与尺寸一律以断面 ZZY-1／ZZY-2、`bridge3d.js` 与正文为准**。此前该位置曾放置确定性脚本绘制的正投影技术图，本轮按效果优先替换为本图；绘图脚本 `build-staging/make_b3d_form.py` 保留在仓库外的构建目录，不随包提交。
   - **前版替换记录（v0.43 起，包内不再保留任何「判为不采用」的留档图）**：本包此前的体例是把一张不采用的图仍随包提交、在 manifest 与展示页标注「判为不采用」，理由是当时没有可替代的正确图；**v0.43 起替代图已全部到位，该留档件随之整条替换、不再随包提交**，旧图不再出现在包内任何位置。逐张记录如下，以免读者从早期版本产生误解。**① `render-ren-bridge`**：初版为下承式桁架桥，与「桥不做塔、不做拱、不做门架」等口径不符；第二版两端画成封闭矩形环道（绕圈上升），与「每侧只设一处折返，两段坡道在平面上并排展开、不上下叠置，也不出现多层盘旋」不符；第三版（近正俯视航拍）实为走不到地面的桥——四个端头无一落地，而当时的声明称它「经逐条比对与正文一致、两端均落在环路两侧绿地内」，**那句话是假的**；第四版（2026-08-30 板梁人视）落地问题已解决，但据实声明过三项不符（梯段一跑到顶、道钉位于步道中部、远端不在框内）。**现版为 v0.43 的斜俯视与地面人视两张**，其逐条核对结论写在 manifest 与展示页图注里，相符项与不符或无法核实项一并列出。**② `render-answer-gate`**：旧图表现为青铜卷轴（巨型「应答簿」）纪念门，与正文「46 座社区出入口」的定义不符，曾作为唯一的留档件随包提交；现版为既有围栏上开洞的改造式门，旧图已整条替换、不随包提交。**③ `render-bell-plaza`、`render-spike-belt`**：旧图为 LibTV 生成，前者的钟体带文物古钟形制特征、固定座椅与乔木进入仪式核心，后者的钉面直径画到几十厘米量级；两图均于 v0.43 整条替换、不随包提交。
   - **提示词全部由本方案自行撰写**，其中人字之跃一张的几何条件（抬升 6 米、单侧坡道展开 128 米、两段并排折返、占地 66×9 米、两端落地）取自本包断面图件 ZZY-1／ZZY-2 的数值；大钟寺一带的空间关系取自 OSM 实测（觉生寺与地铁 13 号线大钟寺站相距约 676 米、方位约 115°，13 号线走向约 175°）。
   - **边界（重要）**：以上十三张均为**意象图，不是图纸**。它们由文字提示词生成，**未经坐标配准，不由本包 `geometry/*.geojson` 派生**，因而不表达用地性质、不表达地块边界、不表达任何要素的精确位置与尺寸；个别画面与正文数值吻合，是提示词约束的结果而非几何生成的结果。凡涉及用地、边界、尺寸与位置的表达，一律以 `assets/figures/` 下的规划图件与断面图件为准。
2. `assets/media/narrative.mp4` 概念短片及其海报帧 `narrative-poster.jpg`——静帧由 Lib Image 与 GPT image 2.0 生成；道钉带、鸣钟之门、应答门三段经 Seedance 2.5 图生视频，各 10 秒；应答原点与人字之跃两段为静帧缓慢推镜、未经视频模型；另有 Python 绘制的片头片尾与字幕条，全片 55 秒。

全部提示词由本方案自行撰写，依据为本包 `proposal.md` 正文口径；除上述已注明的 CC 许可参考图外，未使用任何第三方图像、影像、音频或受版权保护的素材作为输入。AI 生成画面仅用于表达空间意象，**不作为形式、尺寸、材料、树种或工程做法的设计依据**；凡与正文口径不一致之处，一律以断面图与正文为准，已知差异已在 `narrative.vtt` 与 `narrative-transcript.md` 中逐条声明。

**第三方开源组件声明**：本包随附 three.js r160 压缩运行库（`visual/assets/three.min.js`，MIT 许可，版权归 three.js 作者），仅用于「人字之跃」三维示意的本地离线渲染，无网络请求、无数据上传；其 MIT 许可允许随包分发，原始许可文本见 https://github.com/mrdoob/three.js/blob/dev/LICENSE 。

本包另随附一个开源中文字体子集 `visual/assets/fonts/notosanssc-subset.css`（223,958 字节，约 218.7 KB）——**包内任何目录都不允许字体扩展名**（`visual/assets/**` 仅收 `.css`／`.js`／`.json`／`.svg`／图片，`assets/**` 仅收图片），故字体以 **WOFF2 子集（解码后 167,488 字节，约 163.6 KB）经 `data:` URI 内嵌于该 CSS**，四个 HTML 以 `<link>` 共用同一份、数据只存一份。原字体为 **Noto Sans SC**（思源黑体简体中文；版权 © 2014, 2015 Adobe Systems Incorporated，由 Google 以 Noto 系列发行），许可 **SIL Open Font License 1.1**。版权与许可字段取自字体文件自身的 name 表（nameID 0 / 13 / 14），许可证全文见 http://scripts.sil.org/OFL 。**该字体未声明保留字体名（Reserved Font Name），故 OFL 1.1 允许子集化与改名**：本包按四个必需 HTML 的实际用字子集化为 1551 个码位，字体族名改为「NotoSansSC Subset」，以便与系统上同名字体相区分、并可验证页面用的确实是随包字体。**用途**：`report/proposal.html`、`report/proposal.en.html`、`visual/index.html`、`visual/index.en.html` 四个 HTML 以 `@font-face` 引用它，使中文在**没有安装中文字体的环境**（例如评审所用的离线容器）中仍能正常显示，而不是回退失败成方框。OFL 允许随包分发；字体仅用于文字显示，不作任何再授权主张。

除 three.js 与上述字体外，本包不含任何其他第三方代码库或字体。
