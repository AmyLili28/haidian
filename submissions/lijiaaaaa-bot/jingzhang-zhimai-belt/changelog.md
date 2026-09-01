# 方案迭代记录

## v0.4.6 - 2026-09-01

### 改动摘要（关 CocoSgt 本轮 1 条阻断）

1. **对齐空 registry 摘要**：删除 `proposal.md` / `report/proposal.html` 中「formal 14 / background 7 / provisional-only 1」；写明评审侧 `source_registry_summary` 为 total=0、approved 列表为空。
2. **本包资料用途表**：公开原文直接引用 / 背景案例 / 临时几何 / 待 registry 审核四层分开，发布主体与访问路径可核，不自称 registry-approved。
3. **SOURCE-REGISTRY**：`sources.json` 改为只引用登记路径，不把当前 registry 当作已分类清单。

### 采纳反馈

- AI review `7b4cf8d`（85/100）风险与合规 1 项 blocking。

## v0.4.5 - 2026-09-01

### 改动摘要（关 CocoSgt 本轮 3 条阻断）

1. **canonical 10 场景登记**：`compliance_matrix.json#ai_scenario_registry` 固定 SC-01—SC-10 的中英名、服务对象、feature_id、数据边界、人工复核、运营主体与分期；proposal / visual / 框架图 / A3·A0 同一口径。
2. **6 个全球案例来源**：`sources.json` 增补 CASE-STANFORD / MILA / PUNGGOL / TSUKUBA / HETAO / KENDALL（发布主体、访问路径、使用状态=背景案例/设计类比）；正文案例表同步，不得当正式规划依据。
3. **图面临时边界警示**：site-overview、land-use-structure、key-areas、mobility-bluegreen、metrics-evidence 等独立地图/指标图内嵌「临时工作边界/非官方红线；数值须在官方几何发布后复算」；A3/A0/HTML 引用同步。

### 采纳反馈

- AI review `58984be`（73/100）风险与合规 + 表达完整度 3 项 blocking。

## v0.4.4 - 2026-08-31

### 改动摘要（离线 CJK 字体）

1. **包内嵌字体**：`visual/assets/cjk-font.css` 内嵌文泉驿微米黑子集（data:font/woff2，Apache-2.0 / GPL3 字体嵌入例外）；`cjk-font-license.json` 记录许可。
2. **HTML**：`visual/index.html`、`report/proposal.html` 引用本地 CSS，不加载远程字体/脚本/API；系统 CJK 仅作回退。
3. **manifest / self_check**：sha256 刷新。

### 采纳反馈

- AI review `81ced7e`（81/100）表达完整度 blocking：评审环境缺系统中文字体导致方框缺字。

## v0.4.3 - 2026-08-31

### 改动摘要（CI 路径合规）

1. **移除 PR 外路径变更**：删除 `scripts/regenerate_a0_boards.py`（participant PR 仅允许改 `submissions/lijiaaaaa-bot/`）；A0 PDF 与 `a0-01-preview.png` 已在 v0.4.1 生成完毕，本次无图件变更。
2. **manifest / self_check**：sha256 刷新。

### 采纳反馈

- CI run 33360607181 FAIL：`participant PRs may only change submissions/lijiaaaaa-bot/`。

## v0.4.2 - 2026-08-31

### 改动摘要（AI review 结构化补全）

1. **compliance_matrix.json**：`regional_synergy` 补 themes/I/O/spatial_interface/participants/disclaimer；新增 `honor_display_system`（HD-01–04）；`component_library` 补九项运营字段；`operational_governance` 补 owner_role/KPI/thresholds/exit_criteria。
2. **metrics.json**：`green_ratio`/`public_space_ratio` 标注 `metric_class=design_recalc` 与 definition_zh。
3. **proposal.md / visual/index.html**：面积口径、控规指标边界、治理矩阵 KPI/退出、英文 boundary disclaimers、HTML 指标标签修正。
4. **manifest / self_check**：sha256 刷新 + upstream self_check PASS。

### 采纳反馈

- AI review PR #4144 十项 blocking repair 结构化字段补全（v0.4/v0.4.1 基础上的 depth 增强）。

## v0.4.1 - 2026-08-31

### 改动摘要（A0-01 首板重排）

1. **A0 PDF 重生成**：新增 `scripts/regenerate_a0_boards.py`（ReportLab + Hiragino Sans GB），重排 A0-01 首板——核心总览图占满内容区、图例/临时边界警示/底图来源可读；同步修复原 8 页中第 3 页空白问题，现为 7 页 A0-01~07。
2. **首板预览**：输出 `assets/figures/a0-01-preview.png` 供评审快速查看。
3. **manifest / self_check**：sha256 刷新 + upstream self_check PASS。

### 采纳反馈

- AI review 表达完整度第 2 项：A0-01 打印尺度可读性。

## v0.4 - 2026-08-31

### 改动摘要（AI review 10 项修复）

1. **metrics.json**：重点区域 canonical 口径 369.268 ha；新增 `key_detailed_design_area_ha`；phase_001/002/003 补全 definition、horizon、JZ 关联；`phase_1_area_sqm` 修正为 phase_001 alias。
2. **assumptions.json**：A-CONTROLS-001 将 green_ratio/public_space_ratio 移出法定控规项，标注为设计复算指标。
3. **proposal.md**：新增英文命名层级、区域协同表、荣誉展示体系、公共空间组件库、运营治理矩阵（JZ-01–06 × 四季）、英文传播单元（tagline + 128w intro）。
4. **结构化数据**：区域协同、组件库、运营治理矩阵嵌入 `compliance_matrix.json`。
5. **新图件**：`regional-synergy.png`、`logo-naming-direction.png`（matplotlib 生成）。
6. **HTML 字体**：`visual/index.html`、`report/proposal.html` 离线 CJK 字体栈（PingFang SC / Hiragino Sans GB / Microsoft YaHei / Noto Sans SC）。
7. **A0 PDF**：仓库无 A0 再生成脚本，保留现有 `drawings/a0-boards.pdf`；变更记录于本 changelog。
8. **self_check**：upstream `self_check_submission.py --mark-self-checked` 刷新。

### 采纳反馈

- AI review CHANGES_REQUESTED（68/100）十项 blocking repair 逐项落地。

## v0.3 - 2026-08-28

### 改动摘要

- 概念建筑由 16 增至 **25** 栋（三核各补 3 栋），`buildings-massing.png` 与 metrics 同步刷新。
- `proposal.md` 压缩「资料清单与合规证据」重复段落，删除与开篇重叠的「三层范围工作框架（详）」。
- 全量 upgrade（`--skip-hero`）+ manifest sha256 刷新 + self_check PASS。

### 采纳反馈

- 参考独立评审建议：建筑体量、正文去重；西界 key area 已 clip 在 SITE 内，保留 provisional 警示。

## v0.2 - 2026-08-27

### 改动摘要

- 新增 `A-DATA-CONTEXT-001`：明确 existing_condition 与 design_proposal 图层分工，禁止 OSM bulk import 混计。
- `proposal.md` 补充「现状参考与设计图层分工」短节；道路层仍为 OSM/天地图裁切参考（≤120 段），建筑层保持 agent 概念 footprint。
- 冲刺前全量 upgrade（`--skip-hero`）+ self_check + manifest 刷新。

### 采纳反馈

- 暂无 maintainer 正式反馈；参考 bit40303 披露风格，仅采纳「分层披露 + 证据链」做法，未采纳 bulk OSM 建筑导入。

### 暂未采纳或待复核事项

- 官方红线、三处重点区 official polygon、控规强度与道路红线仍待组织方发布。
- 可选：`geometry/existing_buildings.geojson` 轻量 OSM 裁切（需新增脚本，当前未做）。

### 公开资料与合规说明

- 不提交涉密/内部空间数据；OSM 道路裁切遵循 ODbL 开放来源，仅作概念参考，不替代测绘或审批成果。

## v0.1 - 2026-08-20

### 改动摘要

- 创建方案初稿：三核 + 京张慢行脊 + 10 场景节点；GeoJSON 设计图层、五张核心 UST 图、A3/A0 与 HTML 展示。

### 采纳反馈

- Goal 循环第 3 轮：Gate1/self_check 全 PASS；KEY_AREA_PROVISIONAL 为 minor 提示。

### 暂未采纳或待复核事项

- 具体建设强度、道路线位、设施落位和权属判断均需基于公开资料进一步复核。

### 公开资料与合规说明

- 本版本仅使用公开任务书和可公开资料，不包含个人隐私、涉密资料、内部图件或未审定规划控制指标。
