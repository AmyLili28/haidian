# 版权、许可与素材权属声明 / Copyright, Licensing and Material Provenance

本文件登记本投稿包**实际使用**的每一项外部素材、数据、字体与工具链，逐项记录来源、作者、许可、
用途、修改方式与取得日期。凡许可不明确的素材一律不进入本包；已发现并移除的条目在文末「已排除素材」
一节中显名登记，不作静默处理。

This file registers every external asset, dataset, font and toolchain component **actually used** in
this submission, item by item, with its source, author, licence, use, modification and retrieval
date. Anything whose licence is not established is kept out of the package; items found and removed
are named explicitly in the final section rather than dropped silently.

- 投稿包：`submissions/Jieshen-DesignLab/jingzhang-urban-relation-belt`
- 参赛方 / Entrant：Jieshen-DesignLab
- 声明日期 / Statement date：2026-08-31
- 机器可读来源清单 / Machine-readable source list：本包 `sources.json`（本文件与其逐条对应）

---

## 1. 参赛方原创内容 / Original work by the entrant

本方案的**全部设计判断、分析方法、图纸版式、正文文本、GeoJSON 设计图层（land_use、public_space、
phasing 及 roads 中的概念性慢行主廊道）、五张核心派生图、A3 文册与 A0 展板的版面与生成脚本、
离线展示页**，均为参赛方原创。

- 著作权人 / Copyright holder：Jieshen-DesignLab（参赛方）
- 声明的使用许可 / Declared licence：`COMMUNITY-DISPLAY-ONLY`（见 `proposal.md` front matter）——
  允许主办方、承办方与征集组织机构为本次开源征集的接收、校验、评审与公开展示目的使用与复制；
  其他用途须另行取得参赛方书面许可。
- AI 辅助声明 / AI assistance：本投稿包由 AI agent 生成与组织（`agent.json` 中声明模型为
  `claude-opus-5`）。设计判断、事实核验口径与取舍由参赛方负责；AI 参与内容包括：空间数据处理与面积
  复算脚本、图面与版式生成脚本、正文与展示页的组织与撰写、三个矩阵与自检流程的执行。本包含有三组**显名登记的生成式概念设计示意图**（T1 关键关系剖面 R75.2、T1 核心节点鸟瞰 R75.8、
  T2–T5 长断面 R76.2，登记见第 2a 节）：均为参赛方在项目自定几何、事实约束与人工复核下指令
  生成／编辑，属概念表达，**不是现场照片，不作为测绘证据，不用于边界或尺寸核验**。除此之外的
  所有地图与图示均由本包内 GeoJSON 与 metrics.json 程序派生；照片来源逐张登记于第 3 节。

---

## 2. 空间与事实数据 / Spatial and factual data

| 来源 ID | 素材 | 作者 / 发布者 | 许可 | 用途 | 修改方式 | 取得日期 |
| --- | --- | --- | --- | --- | --- | --- |
| `DATA-SRC-OSM-JINGZHANG-BASE` | OpenStreetMap 京张走廊南段矢量数据（建筑、道路、绿地、轨道、水体） | OpenStreetMap contributors | **ODbL 1.0** | 本包 `buildings`/`roads`/`green_space`/`constraints` 图层的现状底层；主线关系分析的空间底图 | 一次性冻结导出后按临时边界裁切、分类与重命名字段；逐要素保留 `osmid` 以便回溯 | 2026-08-24 |
| `BOUNDARY-SOURCE` | `brief/site-package/geometry/provisional_boundaries.geojson` | 本仓库维护者（open-city-ai/haidian） | 仓库内公开资料，按仓库规则用于本征集 | 本包 `site_boundary` 的唯一几何来源 | 坐标系统一为 EPSG:4326；面积在 EPSG:4548 下复算；不改动几何形状 | 2026-08-31 |
| `KEY-AREA-SOURCE` | 同上文件中的三处重点区域临时 polygon | 同上 | 同上 | 本包 `key_areas` 的几何来源 | 同上 | 2026-08-31 |
| `SITE-PACKAGE` | `brief/site-package/`（任务书、枚举、schema、design_brief） | 本仓库维护者 | 仓库内公开资料 | 范围定义、字段枚举、复算坐标系与成果要求 | 未修改，仅引用 | 2026-08-31 |
| `SOURCE-REGISTRY` | `data/source_registry.json` | 本仓库维护者 | 仓库内公开资料 | 区分 formal 可用、仅作背景与仅供临时使用的资料 | 未修改，仅引用 | 2026-08-31 |
| `PROCESSED-FACT-PACK` | `data/processed/agent_fact_pack.md` 等处理资料 | 本仓库维护者 | 仓库内公开资料 | 任务清单、范围结构与缺口清单的导航层 | 未修改，仅引用 | 2026-08-31 |
| `OFFICIAL-ANNOUNCEMENT` | 《百年京张AI创新带城市设计国际方案征集资格预审公告》 | 北京市规划和自然资源委员会海淀分局 | 官方公开发布的政府公告文本 | 三层范围、三处重点区域、任务 1.3/1.4/1.5 与成果深度要求 | 未复制原文图件，仅引用文字要求 | 2026-08-31 |
| `AGENT-TASKBOOK` | `brief/site-package/agent_taskbook.json` 面向智能体任务书 | 本仓库维护者 | 仓库内公开资料 | agent.1–agent.6 必答任务、评审维度与统一边界条款 | 未修改，仅引用 | 2026-08-31 |
| `MAINLINE-RELATION-ANALYSIS` | 参赛方自有的城市关系断面分析、五断面问题定义、四类关系机制与 T1 深化成果 | Jieshen-DesignLab | 参赛方自有成果，随本投稿授权按 `COMMUNITY-DISPLAY-ONLY` 使用 | 本方案正文与全部图纸的设计内容来源 | 为本投稿重新排版与降采样 | 2026-08-31 |

**ODbL 1.0 归属声明（必须随本包一并保留）：**
本包中的现状建筑、道路、绿地、轨道与水体数据 © OpenStreetMap contributors，依 Open Database
License 1.0 提供（<https://www.openstreetmap.org/copyright>）。由该数据派生的任何数据库若被再分发，
须同样以 ODbL 1.0 提供。本包中由 OSM 派生的图层为 `geometry/buildings.geojson`、
`geometry/roads.geojson`（其中 310 段现状中心线）、`geometry/green_space.geojson` 与
`geometry/constraints.geojson`。**OSM 数据不是道路红线、用地边界、产权边界或任何法定控制线。**

---

## 2a. 生成式概念设计示意图 / Generative concept visualisations

下列三组图像由生成式图像模型在参赛方给定的几何底稿、事实约束与逐轮人工审计下生成／编辑，
性质均为：*conceptual design visualisation generated/edited under project-defined geometry, factual constraints and human review; not survey evidence and not a source for boundary or dimensional verification*。
它们不是现场照片，不进入任何面积、边界或尺寸论证；相关事实（标高、垂直交通等）在正文中
单独标注核验状态。

| 来源 ID | 图像 | 生成轮次与方式 | 人工复核记录 | 用于 |
| --- | --- | --- | --- | --- |
| `GEN-T1-SECTION-R752` | T1 关键关系剖面（垂直公共铰链） | R75.2，imagegen 定向编辑 | R75.2 审计（SECTION PASS） | 文册 P25／P27、PAGE00 |
| `GEN-T1-AERIAL-R758` | T1 核心节点鸟瞰 | R75.8，imagegen 精确对象编辑（第一次生成，作者指定冻结） | R75.8 报告 | 文册 P27（辅助图） |
| `GEN-T2T5-LONG-SECTIONS-R762` | T2–T5 现状／未来长断面 ×8 | R76.1 生成、R76.2 定向修复（imagegen） | R76.2 各断面审计 | 文册 P18–P21 |

---

## 3. 现场影像 / Site photographs

最终文册第 24 页使用四张现场影像：三张取自 Wikimedia Commons（`sources.json` 中登记为
`B14-COMMONS-IMAGERY`），许可明确、可署名，页面上**逐张印出作者与许可**；另一张为政府公开发布
影像（见表末行与 `OFFICIAL-PHOTO-LANJING-BMPNR-20260612`），按诚实口径登记。

| 文件 | 内容 | 作者 | 许可 | 来源 | 修改方式 | 取得日期 |
| --- | --- | --- | --- | --- | --- | --- |
| `Exit_A_of_Dazhong_Si_Station_(Feb_2025).jpg` | 大钟寺站 A 口（2025-02-22 摄） | RobertSchwandI | **CC BY-SA 4.0** | <https://commons.wikimedia.org/wiki/File:Exit_A_of_Dazhong_Si_Station_(Feb_2025).jpg> | 仅等比缩放与 JPEG 重编码置入版面，未裁切、未调色、未合成 | 2026-08-31 |
| `Exit_B_of_Dazhongsi_Station_(20210409120947).jpg` | 大钟寺站 B 口（2021-04-09 摄） | N509FZ | **CC BY-SA 4.0** | <https://commons.wikimedia.org/wiki/File:Exit_B_of_Dazhongsi_Station_(20210409120947).jpg> | 同上 | 2026-08-31 |
| `Outside_Dazhongsi_Station_in_Beijing.JPG` | 大钟寺站站外 | Siyuwj | **CC BY-SA 3.0** | <https://commons.wikimedia.org/wiki/File:Outside_Dazhongsi_Station_in_Beijing.JPG> | 同上 | 2026-08-31 |
| `04_蓝景丽家改造前照片_规自委发布_20260612.jpg` | 蓝景丽家地块改造前（更新窗口期语境） | 北京市规划和自然资源委员会（公开发布，2026-06-12） | **政府公开发布影像；已注明来源；再分发许可未经独立核实** / publicly released government image; source credited; reuse permission not independently verified | <https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/zxzt/csgx/csgxfjszt/fjsztalzs/202606/t20260612_4698370.html> | 仅等比缩放与 JPEG 压缩 | 2026-08-31 |

**CC BY-SA 归属与同协议共享声明：** 上述三张影像分别依 CC BY-SA 4.0 与 CC BY-SA 3.0 提供；本包在
使用处保留原作者署名、许可名称与来源链接。任何人再使用这三张影像，须继续保留同样的署名与许可，
并按同一协议共享其改编作品。**本包的其他部分不因此改变许可**：三张影像作为独立作品被汇编引用，
其许可只约束影像本身。

**口径核对（2026-08-31 已闭合）：** `proposal.md`「风险、版权与合规说明」与 `sources.json` 条目
`B14-COMMONS-IMAGERY` 均已按实际许可逐张登记（两张 CC BY-SA 4.0 ＋ 一张 CC BY-SA 3.0），与本表一致。

---

## 4. 案例引用素材 / Case-study references

`sources.json` 中登记的六个国际创新区案例条目——`CASE-KENDALL-SQUARE`、`CASE-STATION-F`、
`CASE-KINGS-CROSS`、`CASE-22AT-BARCELONA`、`CASE-MARS-TORONTO`、`CASE-SEOUL-AI-HUB`——
**只用于文字层面的机制引用**，全部在 `sources.json` 中标记为 `usable_for_formal=background_only`。
本包**不复制、不改编、不嵌入**这些案例的照片、总平面图、渲染图或任何受版权保护的图件；正文中出现的
只有参赛方自行撰写的机制描述与可公开核验的来源链接。

---

## 5. 字体 / Fonts

本包不内嵌、不再分发任何字体文件。A3/A0 PDF 中的文字以**位图光栅化**方式呈现（页面为 JPEG 图像），
因此 PDF 内不含字体子集；离线展示页只声明本机通用字体族，不加载任何远程字体。

| 字体 | 用途 | 许可与再分发状态 | 是否随包分发 |
| --- | --- | --- | --- |
| Microsoft YaHei（微软雅黑） | 中文图面、A3/A0 中文页面的光栅化排版 | Microsoft 随 Windows 授权，**不可再分发**；本包仅在本地渲染时使用，未随包分发字体文件 | 否 |
| Segoe UI | 英文图面与英文页面的光栅化排版 | 同上 | 否 |
| DejaVu Sans | matplotlib 内置回退字体（数学与少量符号） | Bitstream Vera / DejaVu 许可（自由使用与再分发） | 否（未随包分发） |
| 展示页 CSS 字体族 | `visual/index.html`、`visual/index.en.html` | 仅声明 `"Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", "Segoe UI", system-ui, ...` 等**系统字体族名**，由阅读者本机解析；**不加载任何 webfont** | 否 |

---

## 6. 软件与工具链 / Software and toolchain

以下工具用于生成本包的几何、指标、图面、PDF 与展示页。它们**不随本包再分发**，此处登记版本与许可
以保证结果可复现。

| 组件 | 版本 | 许可 | 用途 |
| --- | --- | --- | --- |
| CPython | 3.12.10 | PSF License | 全部生成脚本的运行环境 |
| matplotlib | 3.11.0 | Matplotlib License（BSD 兼容） | 五张核心派生图、A3/A0 版面页的绘制 |
| Shapely | 2.1.2 | BSD-3-Clause | GeoJSON 几何解析、面积与拓扑计算 |
| PyProj | 3.7.2（PROJ 9.5.1） | MIT（PROJ 为 MIT） | EPSG:4326 → EPSG:4548 坐标转换与面积复算 |
| Pillow | 12.2.0 | MIT-CMU | 图像重采样、JPEG 编码与解码体积核验 |
| PyMuPDF | 1.28.0（MuPDF 1.29.0） | AGPL-3.0 | A3/A0 PDF 的页面组装与体积核验 |

**AGPL-3.0 说明：** PyMuPDF 以 AGPL-3.0 提供，本包**仅作为本地命令行工具使用**，未修改其源码、未
提供网络服务、未随包分发其二进制或源码，因此不触发 AGPL 的源码提供义务。本包产出的 PDF 文件本身
不受 AGPL 约束。

**PDF 内嵌字体状态：** 由于 A3/A0 页面以光栅图像置入，PDF 中**没有任何内嵌字体子集**，不存在字体
再分发问题。

---

## 7. 已排除素材（发现并移除，显名登记） / Excluded material

下列素材在主线成果中曾被使用，但其**再分发许可未确立**，因此**不进入本投稿包**的任何交付件。
排除方式为：整页移除，并由参赛方自绘的替代页承担同一说明职责。

| 素材 | 原位置 | 排除原因 | 处理方式 |
| --- | --- | --- | --- |
| 街景平台全景截图（`09_站前全景尝试.png`，百度全景，2026-08 截取） | 主线现场观察页 BOARD_14 | **商业地图平台截图，无可援引的再分发许可**；平台服务条款未授权第三方在投稿成果中复制与公开展示 | 连同 BOARD_14 整页从 A3 文册与 A0 展板中移除 |
| 蓝景丽家地块改造前照片（市规自委 2026-06-12 公开发布） | 主线现场观察页 BOARD_14 | 官方公开发布不等于授予再分发许可 | **2026-08-31 裁决后移出本表**：按“政府公开发布影像、注明来源、再分发许可未经独立核实”的诚实口径在第 3 节登记，并在最终文册第 24 页使用 |
| 上海定位漂移的街景测试截图 | 主线工作过程 | 定位错误且无许可，主线已判废 | 从未进入成果版 |

**最终版口径：** 最终 A3 文册为 28 页设计文册，其第 24 页《T1 场地事实与现场》直接承载现场影像
并逐张印出来源与许可；百度全景截图仍被排除，未进入任何交付件。

---

## 8. 不含内容的否定性声明 / Negative declarations

本包**不包含**：
未经授权的商标与标识；随包分发的字体文件；人物肖像可识别且未取得同意的影像；第三方论文、书籍或
报告中的图表与插图；商业地图底图或其截图；付费数据库导出的数据；任何被当作现场照片或测绘证据使用的影像（本包的生成式概念示意图见第 2a 节，均显名登记、不作证据用）；任何非公开的政府数据、企业内部数据或个人数据。

This package contains **no** unlicensed trademark or logo; no redistributed font file; no image in
which an identifiable person appears without consent; no figure or illustration taken from a
third-party paper, book or report; no commercial map basemap or screenshot thereof; no data
exported from a paid database; and no image passed off as a site photograph or as survey evidence (the generative concept
visualisations in this package are declared in section 2a and are not used as evidence); and no non-public government data, internal corporate data or
personal data.

---

## 9. 使用与再分发条件摘要 / Summary of conditions for reuse

1. 本包整体按 `COMMUNITY-DISPLAY-ONLY` 提供，供本次开源征集的接收、校验、评审与公开展示使用。
2. 其中由 OpenStreetMap 派生的数据库部分按 **ODbL 1.0** 提供；再分发派生数据库须同样以 ODbL 1.0 提供，
   并保留 © OpenStreetMap contributors 归属。
3. 其中三张现场影像按 **CC BY-SA 4.0 / CC BY-SA 3.0** 提供；再使用须保留原作者署名与许可，并按同一
   协议共享改编作品。
4. 参赛方原创的设计判断、图纸版式、正文与脚本，其他用途须另行取得参赛方书面许可。
5. 本声明与 `sources.json` 逐条对应；两者不一致时，以本声明与 `sources.json` 中的许可字段为准，
   `proposal.md` 正文中的概括表述不作为许可依据。
