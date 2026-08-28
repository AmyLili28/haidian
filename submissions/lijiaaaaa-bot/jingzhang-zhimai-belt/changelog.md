# 方案迭代记录

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
