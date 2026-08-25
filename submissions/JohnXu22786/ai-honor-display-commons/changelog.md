# 方案迭代记录

## v0.1.0 - 2026-08-24

- Initial assembly (concept package) for ai-honor-display-commons.
- Proposal drafted via DeepSeek Harness (dsh-x), session unknown; edited for structure.
- Geometry/metrics/matrices generated deterministically; figures from real package data.
- Valroot gates run on 2026-08-24 (results persisted in self_check.json).

## v1.1.0 - 2026-08-25

（REPAIR ROUND-1，回应评审 CocoSgt 43.0/100 CHANGES_REQUESTED）

- **双语合同补齐（item 1）**：proposal.md 升级 proposal_format_version=2 + bilingual_contract_version=1 + translation_file=proposal.en.md；proposal.en.md 增加 language=en + translation_of=proposal.md 前置；补齐并登记英文对应件——6 张 .en.png 图、a0-boards.en.pdf、a3-booklet.en.pdf、report/proposal.en.html、visual/index.en.html，manifest.json 全部登记 language/translation_of；中英正文实质等值已逐节人工核对。
- **字体与HTML（item 2）**：NotoSansSC-VF 经 fontTools instancer 取 wght400 静态实例，四页 HTML（报告中英+视觉中英）按实际字形逐页 pyftsubset 并以 data:font base64 内嵌、font-family 置首；中英文 HTML 均由仓库 render_proposal_html.py 渲染后最后嵌入字体；en 页功能中文残余 0（品牌引注除外）。
- **agent.1-agent.2（item 3）**：新增三区两翼协同回路与区域协同机制（北纬社区/未来科学城/怀柔科学城/经开区/京津冀）并空间化于总览图；品牌识别与视觉系统章节 + logo-jz.png；全球/国内案例扩充至 8 个形成生态图谱（ecosystem-map 图件）+ 产业—空间—要素机制表；每案例逐条登记 sources.json。
- **agent.3-agent.4（item 4）**：10 张 AI 场景卡总表 + 3 个产业测试验证场景表；重点区域图中补充空间界面、节点平面、绿带断面与组件原型；正文补充东西缝合、南北贯通、大钟寺智能原生业态与三处朝圣地标表述。
- **agent.5-agent.6（item 5）**：京张铁路—中关村—AI 新文化史实来源登记（国家铁路局/国铁集团/园林绿化局/市规自委/市科委）；三级导视与符号系统、国际传播文案（GLORY·JZ — where a century of rail meets a generation of AI）；年度活动品牌表、开发者社区运营、场景开放、公共体验、内容治理与长期转化机制（人才—企业—开发者转化路径）。
- **图件重绘（item 6）**：全部 6 组中文+英文图件按 figsize(12,8)@150dpi 重绘，配图例、比例尺、指北针、空间语境、节点放大、剖面与组件原型；比例与计数分轴显示；provisional 数值降低精度显示并就近标注来源/置信/复算触发；A0 首版标题 88pt、图件逐张机器 QC（ink/剪裁/文字重叠）。
- **案例与权利溯源（item 7）**：sources.json 新增 13 条（5 条史实/规划 + 8 条案例官方页面），全部带发布者/链接/日期/复用边界；资产权利清单并入 report/copyright_statement.md（字体 OFL 1.1、Logo 内部工作代号、生成内容、代码逐项登记）；确定性/空间/视觉/专业证据四门自检全部 PASS 并持久化。
- **评分回应（item 8）**：七维 24 项 required repairs 逐项落实：三区两翼与区域词、每年表、案例表、场景卡表、测试表、品牌章节+Logo、权利清单、en 全套对应件、图件 ink≥0.06、figure_qc 证据、manifest en 映射、HTML 字体内嵌、双语完整性、data_confidence=medium、牵头/协作与停止/退出条件、案例可溯源来源、精度显示、AI 技术协议（模型评测/基准测试/误报率/运行监测）、生态图谱、开发者社区、国际传播、荣誉/组件库表述、用地口径/聚合规则。
- 图生成期文字包围盒重叠检查：13 张 PNG 全部 0 重叠、0 出界剪裁（机器测量并记入 self_check.json[figure_qc]，overlap_clear=true）。
- 品牌在先权利与使用边界：未完成商标检索前 GLORY·JZ 等名称仅作内部工作代号（版权声明与风险章节双重声明）。