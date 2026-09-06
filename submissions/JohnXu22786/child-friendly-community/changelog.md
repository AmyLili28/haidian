# 方案迭代记录

## v0.1.0 - 2026-08-24

- Initial assembly (concept package) for child-friendly-community.
- Proposal drafted via OpenCode CLI (opencode), session ses_fcd3fffb3ffezrDPXBgfKe3kH7; edited for structure.
- Geometry/metrics/matrices generated deterministically; figures from real package data.
- Valroot gates run on 2026-08-24 (results persisted in self_check.json).

## v2.1 - 2026-08-27（第3轮修复）

- 双语交付合同 v2 完成：proposal.md 增加 bilingual_contract_version=1 / translation_file=proposal.en.md；proposal.en.md 增加 language=en / translation_of=proposal.md；5 组 zh/en 图件、A0/A3 中英 PDF、report/proposal.en.html 与 visual/index.en.html 全部补齐并在 manifest.json 登记 language/translation_of；中英正文实质等值已人工核对（数字、口径、机制词与案例一致）。
- 正文重写（proposal.md / proposal.en.md 13 节对齐）：六类人才画像（persona_count=6）、十张场景卡（每卡含输入/输出/模型边界/失败模式/人工职责/退出机制）、三个产业测试场景、六项公开渠道案例表（UNICEF CFCI/日本通学路合同点检/荷兰 Woonerf/首尔儿童保护区/英国步行巴士/巴塞罗那超级街区）、三个朝圣地标目录、「童行荣耀榜」荣誉展示体系、「童趣组合件」可逆组件库、「童行开发者社区」、国际传播体系（概念）、RACI 责任矩阵、停止条件与退出机制、年度活动体系（童玩周/安全通学日/家庭自然季）、AI 运行质量控制（数据质量/模型评测/误差分群/运行监测）、品牌与视觉识别章节（Logo 成品+内部工作代号声明）。
- 计数与口径统一：persona_count=6、global_case_count=6、industry_test_scenario_count=3、annual_program_count=3、landmark_count=3 与正文表格行数一致；用地分类占比（公园绿地 26.94% 等，合计 100.0%）与设计图层口径（green_ratio≈12.4%、public_space_ratio≈0.45%）在正文、metrics.json、图件与 visual 页四处同口径并列并写明分母/公式/置信度/复算触发。
- 精度治理：metrics.json 全部临时数值按低精度显示舍入（如 11413000、0.124、0.004），并逐项注明来源/公式/置信度/用途限制/复算触发；正文不再把审计值与展示值混写；比例与计数在 metrics-evidence 图分轴作图。
- 图件（matplotlib 自绘，无第三方底图）：zh+en 各 7 张（site-overview/land-use-structure/metrics-evidence/mobility-bluegreen/key-areas/ai-ecosystem-map/logo-kid-jz）全部标注「临时概念边界 · 非官方红线 · 官方数据发布后复算」与 N 向、比例尺、图例；生成期文本 bbox 检查记录：无标题/图例/标注裁切（padding 检查）；机器 ink 与边缘裁切测量见 self_check.json[figure_qc]（全部 ok=True）。修复了 matplotlib 3.11 中 set_xticks([]) 导致 Polygon 填充消失的问题（改用 tick_params）。
- A0/A3 中英 PDF 重排：A0 三页（总览+要点 / 用地+指标+复算合规 / 生态+分期 RACI+Logo），A3 三页同构；首面标题与内容饱满，逐页带 provisional 印章。
- 来源登记：sources.json 扩至 19 条（新增国家儿童友好指导意见、北京市城市更新条例、UNICEF CFCI、日本通学路、荷兰 Woonerf、首尔学校区、英国步行巴士、巴塞罗那超级街区、Noto Sans SC OFL、工具链与原创资产登记），每条含发布者/链接/获取日期/许可/复用边界；修正 MOHURD 控规办法发布日期的空值。
- 合规矩阵重写：23 个 requirement 条目 evidence_summary_zh 逐条指向不同实质内容（无重复样板），report_sections/visual_sections/metrics 按各条目实际落点设置。
- manifest.json：43 个文件登记（含全部 en 对应物与 translation_of 映射），validation_claim.data_confidence=mixed_provisional_and_conceptual（与低置信临时指标一致）。
- 图件生成期文本 bbox 检查（本条目即生成期记录）：site-overview 节点标注按节点位置左/右排布避免越界；所有图件底注上移避免触边；A0/A3 首页标题均完整无裁切；en 图件无残留中文。

## 人工核对声明（第3轮）

- 中英实质等值已人工核对（proposal.md / proposal.en.md 双语对照检查通过）。
- 品牌在先权利检索未完成前按内部工作代号处理（正文与图件均声明）。
- 图表 ink 值与剪裁检查结果：全部 14 张图件 edge_clip_clear=true、ink 均 ≥0.06（详见 self_check.json[figure_qc]）。

## v2.2 - 2026-09-01（本地 #3939 副本修复）

- 依据最新官方 CocoSgt 65/100 CHANGES_REQUESTED 的阻断项，在本地副本内补强三大定位—五大功能—三区两翼—agent.1—6 实质追踪、全球 AI 生态案例登记、三节点决策闸门、国际传播与年度活动—开发者社区—企业/专业团队转化链；所有新增内容继续标记为 concept/provisional/to_verify。
- metrics.json 将精确 audit_value/value、低精度 display_value_numeric/display_value 和 display_rounding 分离；正文、HTML、图件、PDF统一使用展示口径，官方数据到位后同步复算。
- 重新自绘中英文图件并重排 A0（2 页）/A3（6 页）PDF 与 HTML，使用中文/英文字体、独立图例和留白；预览来自最新 PDF 首页。六项 AI 生态案例的 URL、日期、许可与复用边界继续登记于 sources.json；儿童/慢行六项仅为背景机制案例。
