# 方案迭代记录 · 京张关系带 / Changelog - Jing-Zhang Relation Belt

本文件记录本投稿包的版本变化、已采纳的反馈与待复核事项。权威数据仍以包内 `geometry/*.geojson`、
`metrics.json`、`sources.json`、`assumptions.json` 与三个矩阵为准。

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
