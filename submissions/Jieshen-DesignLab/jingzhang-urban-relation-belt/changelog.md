# 方案迭代记录 · 京张关系带 / Changelog - Jing-Zhang Relation Belt

本文件记录本投稿包的版本变化、已采纳的反馈与待复核事项。权威数据仍以包内 `geometry/*.geojson`、
`metrics.json`、`sources.json`、`assumptions.json` 与三个矩阵为准。

## v0.1.3 - 2026-09-01

### 修复 / Fixed（回应 2026-09-01 AI 评审的 3 项阻断）

- 版权：撤除文册第 24 页的市规自委公开发布照片（未取得可核验的再分发许可），换为参赛方自绘的蓝景地块
  区位示意图（底图 © OpenStreetMap contributors，ODbL 1.0）；`proposal.md`／`proposal.en.md`、
  `sources.json`（删除 `OFFICIAL-PHOTO-LANJING-BMPNR-20260612`）与 `report/copyright_statement.md`
  统一为「已移除」单一状态，OFFICIAL_PHOTO_USED = NO。
- 可读性：修复 `report/proposal.html` 离线中文渲染——字体注入脚本此前误改了 `font-family` 属性名，
  导致内嵌 Noto Sans SC 子集从未被应用；现已修正并重新注入，正文、标题、表格、注释离线均以内嵌字体显示。
- 可读性：修复 `drawings/a3-booklet.en.pdf` 首页顶部四色母公式标题重叠——该标题块改为按实测宽度自动
  排布并缩字号，页面其余几何、图位与中英页序不变；英文 A3 重新导出。

## v0.1.2 - 2026-08-31

### 修正 / Fixed

- 版权口径按 2026-08-31 最终裁决收口：`report/copyright_statement.md` 撤销“本包不包含任何生成式
  模型产出的写实影像／渲染图”的否定性声明，新增第 2a 节显名登记三组生成式概念设计示意图
  （T1 关键剖面 R75.2、T1 鸟瞰 R75.8、T2–T5 长断面 R76.2；性质＝conceptual design visualisation，
  非测绘证据）；`sources.json` 新增对应三条登记。
- 市规自委 2026-06-12 公开发布的蓝景丽家改造前照片按诚实口径登记（publicly released government
  image; source credited; reuse permission not independently verified），从“已排除素材”表移出，
  将随最终 28 页文册第 24 页进入交付件；百度全景截图维持排除。
- `proposal.md`／`proposal.en.md` 版权段同步上述两项；三张 Commons 影像的逐张许可（4.0×2＋3.0×1）
  口径此前已修正，本轮核对一致，上一版«待复核»第一项关闭。

### 待接入 / Pending integration

- 英文 28 页、FORMAL 五图（CN/EN）、A0 七板（CN/EN）与四份 PDF 尚未回流；回流以
  `79_FINAL_CN_MASTER_LOCK_v2` 为唯一中文母本，须分别等待 ENGLISH_MASTER_LOCK／FORMAL_CN_LOCK／
  A0_CN_LOCK 三个明确锁定后一次性接入。

## v0.1.1 - 2026-08-31

回应 PR #4328 的 AI Agent 评审（request-changes，七维加权分 72.0/100，评审锚定 commit
`36b68449bc6d0b910a56713a0452135c0fa8c44a`）。本次修订不改变设计主线：城市关系断面、
T1–T5 关系问题、ARRIVE/FACE/CROSS/USE、总体规划与 canonical extent 均未变动。

### 修复 / Fixed

- **中文 HTML 的 CJK 渲染故障（评审 P0）**：`report/proposal.html` 与 `visual/index.html`
  原先只声明系统中文字体、无 `@font-face`、包内无字体文件，在未安装中文字体的环境中全部
  回退为方框字。现内嵌 Noto Sans SC v2.04 子集（SIL Open Font License 1.1，许可 URL
  http://scripts.sil.org/OFL），按页取用字符做子集后以 base64 写入 `@font-face`，
  子集保留完整 name 表使许可声明随字体分发；未打包任何专有系统字体，无 CDN 与远程请求。
- **三处重点区域的用地语义**：原记录把三处官方重点区表述为本方案建议的用地性质，且
  `land_use_code` 与同一要素的 `dominant_existing_use_osm` 互相矛盾。现三处统一声明
  `proposes_land_use_change=false` 并补 `code_basis_zh`；正文相应改为「主导功能方向」。
  几何未动，全部指标不变。
- **影像许可口径**：三张现场影像更正为两张 CC BY-SA 4.0 ＋ 一张 CC BY-SA 3.0，
  `sources.json` 增加逐张 `items`（文件名、作者、许可、日期、URL）。上一版「待复核」项已关闭。

### 新增 / Added

- 区域创新协同关系矩阵：北纬社区、未来科学城、怀柔科学城、北京经开区、京津冀五个对象。
- 八要素 AI 生态图谱，并按评审要求增加「五类要素 × 三区两翼」映射表。
- 五大功能对应关系表，含「AI 治理全球话语权」的概念机制。
- agent.6 年度活动品牌层级与活动—社区—场景开放—测试验证—成果展示—转化通道闭环。
- S09/S10/S11 三个产业测试场景的最小验证协议，各 10 字段。
- P01–P12 的轻量实施字段（基线、下一阶段交付物、建议角色类别、前置依赖、可核验指标、当前不做）。
- T2 与 T4 的概念控制清单。
- 公共利益与包容性：老年人、儿童及照护者、行动障碍者、视听障碍者、无智能手机用户五类使用者。
- 历史来源四条：`SRC-HIST-JZ-BJWWJ`、`SRC-HIST-JZ-NCSTI`、`SRC-HIST-ZGC-KW`、
  `SRC-HIST-ZGC-CAS`，其中两条为官方主管机构（A 级）。

### 自检记录 / Self-check record

- `CJK_HTML_RENDER_CHECK = PASS`。验证方法不是本机直接渲染（本机装有中文字体，证明不了任何事），
  而是把四份 HTML 复制一份、从每条 `font-family` 删除全部系统字体名后只留内嵌字体，再离线渲染并
  逐项人工检查：标题、导航、正文、表格、code label、证据标记上标、图注均无方框、无裁切、无重叠。
- `BILINGUAL_CROSS_CHECK = PASS`，42 项自动核对全部一致，覆盖章节数、小节数、表格数、嵌入图数量与
  中英配对、三项核心指标数值、unknown 指标表述、五个证据状态词、临时边界警示、T1–T5 映射、
  四类关系动作、本轮八个新增块、史料 source_id 集合，以及中英各若干条禁用表述的清零核验。
  五组中英图逐对比对 SHA-256 全部不同，非同字节复制。

### 仍然保留的边界 / Still declared

- 官方红线、三处重点区域精确 polygon、控规指标、道路红线与市政条件仍未公开；全部空间结论仍为
  低置信度设计模型值，官方几何发布后整体复算。
- 组织方临时边界与京张事实轴线存在偏移（`A-CORRIDOR-BOUNDARY-DIVERGENCE-001`）；两套来源均
  保留原始位置，不人为修正。
- 英文 A3/A0 的主线图面仍为中文，以每张展板配整页英文对照说明缓解；该项属双语契约的解释风险，
  待主线视觉换版时一并处理。

## v0.1.0 - 2026-08-31

首次 formal 提交。

### 新增 / Added

- `proposal.md`（中文主稿）与 `proposal.en.md`（英文译稿）：十三个必选章节，proposal_format_version 2、
  bilingual_contract_version 1；每个必选章节至少一条机器可读证据引用。
- `geometry/` 九个图层：`site_boundary`、`key_areas`、`land_use`、`buildings`、`roads`、`green_space`、
  `public_space`、`constraints`、`phasing`，均为 EPSG:4326 GeoJSON，面积在 EPSG:4548 下复算。
- `metrics.json`：13 项 known 指标由本包图层程序复算；3 项因官方数据缺口保持 `status=unknown`、
  `value=null`（`floor_area_ratio`、`building_height_limit_m`、
  `retain_renovate_demolish_parcel_count`）。
- `assets/figures/` 五张核心派生图及其英文副本，共 10 个 PNG，全部由 GeoJSON 与 `metrics.json`
  程序派生，单张与累计解码体积均在校验上限内。
- `visual/index.html` 与 `visual/index.en.html`：离线静态展示页，无 CDN、无远程字体、无远程图片、
  无 iframe、无表单、无任何网络请求；三项核心指标以 `data-metric`/`data-value` 声明并与
  `metrics.json` 逐位一致。
- `drawings/a3-booklet.pdf`（25 页）、`drawings/a3-booklet.en.pdf`（42 页）、
  `drawings/a0-boards.pdf`（7 张 A0）、`drawings/a0-boards.en.pdf`（7 张 A0）。
- `compliance_matrix.json` 覆盖公告 1.3/1.4/1.5 共 17 条与 agent.1–agent.6 共 6 条；
  `standard_matrix.json` 覆盖 6 项强制专业标准；`design_depth_matrix.json` 覆盖 15 项核心成果深度项。
- `report/copyright_statement.md`：逐项登记外部素材、数据、字体与工具链的来源、作者、许可、用途、
  修改方式与取得日期，并显名登记已排除素材。
- `report/narrative.md`：成果导读。

### 已知边界与声明 / Declared limits

- 官方红线、三处重点区域精确 polygon、控规地块指标、道路红线与市政条件截至提交时均未公开，本包
  使用仓库提供的临时粗略边界，全部空间结论为低置信度设计模型值。
- 三处重点区域的设计深度不同：大钟寺（T1）完成对象级空间深化，北京 AI 原点社区（T2）与众智园
  （T4）为概念级空间控制建议。
- 已提交的连续公共空间主轴图层目前只覆盖走廊南段，北段的连续化由五个断面与站前到达控制带表达；
  该几何缺口在图 1、图 4 与展示页中均已显名标注。

### 已排除 / Removed

- 主线现场观察页中的一张街景平台全景截图与一张官方发布照片，因再分发许可未确立，未进入本投稿包；
  其说明职责由参赛方自绘的 A3 文册第 A4 页承担，该页只使用三张署名清楚的 Wikimedia Commons 影像。

### 待复核 / To be re-checked

- `proposal.md`「风险、版权与合规说明」与 `sources.json` 条目 `B14-COMMONS-IMAGERY` 将三张现场影像
  统一表述为 CC BY-SA 4.0；实际为两张 CC BY-SA 4.0 ＋ 一张 CC BY-SA 3.0，以
  `report/copyright_statement.md` 为准，正文口径待修订。
- 官方红线与控规条件发布后，全部图层、指标、图纸与展示页整体复算并重出，而不是局部修补。
