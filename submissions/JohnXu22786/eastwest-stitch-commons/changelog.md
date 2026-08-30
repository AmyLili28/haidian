# 方案迭代记录

## v0.2.0 - 2026-08-30 (Round 2 CocoSgt Review Repairs)

- **官方两翼命名对齐与规范化**：全面恢复任务书官方两翼标准命名「中关村科技服务翼 / Zhongguancun Technology Service Wing」与「小月河场景赋能翼 / Xiaoyuehe Scenario Empowerment Wing」；在所有中英文文本（`proposal.md`, `proposal.en.md`）、合规矩阵（`compliance_matrix.json`, `standard_matrix.json`）、图件（`assets/figures/*.png`）、图册（`drawings/*.pdf`）与 HTML 看板中保持完全一致；自拟的「高校智力界面 / 国际生活界面」严格降格为局部微观形态界面，绝不替代官方两翼。
- **AI 创新生态与八大要素机制闭环**：彻底消除「六环/七项」逻辑歧义，系统建立支撑百年京张AI创新带的八大要素机制（土地、空间、产业、资金、人才、算力、数据、场景），严密映射三大重点区域与官方两翼，坚决不编造未经核实的企业入驻协议或资金预算；新增生成 `ai-innovation-ecosystem.png` 与 `ai-innovation-ecosystem.en.png` 架构图谱。
- **法规适用范围收窄与自设治理规则声明**：收窄《中华人民共和国无障碍环境建设法》第三十九条引用范围（明确法定义务仅适用于医疗、社保等法定场所），将人工导览台与现场指导明确声明为自设人本设计治理规则；收窄《生成式人工智能服务管理暂行办法》引用范围（明确非生成式感知系统不直接适用），将人工复核、匿名聚合、误报申诉与一键停用明确声明为自设设计治理标准。
- **图件可读性与版式重构**：重新绘制并机器校验全部 12 张图件，消除 `site-overview.en.png`、`key-areas.en.png`、`land-use-structure.en.png` 与 `metrics-evidence.en.png` 中的文字重叠与坐标轴遮挡问题；重构 `a0-boards.pdf` 与 `a0-boards.en.pdf` 排版，设置安全边距（x: 0.04-0.96）彻底消除画布边缘截断；通过 `embed_fonts.py` 为全部 HTML 页面内嵌 Noto Sans SC WOFF 字体。
- **双语交付物与四大门禁验证**：将 `proposal.en.md` 扩充为与 `proposal.md` 逐节对应的完整英文方案；更新 `compliance_matrix.json`（23项）、`standard_matrix.json`（7项）、`risk.json`（8维度人工复核）、`metrics.json`（单一口径指标）；更新 `manifest.json` 哈希清单并通过四大门禁自检（deterministic/spatial/visual/professional 全部 PASS）。

## v0.1.0 - 2026-08-24

- Initial assembly (concept package) for eastwest-stitch-commons.
- Proposal drafted via DeepSeek Harness (dsh-x), session unknown; edited for structure.
- Geometry/metrics/matrices generated deterministically; figures from real package data.
- Valroot gates run on 2026-08-24 (results persisted in self_check.json).
