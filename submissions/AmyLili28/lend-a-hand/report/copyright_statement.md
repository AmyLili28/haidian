# 版权与生成说明

《京张·搭把手｜LEND A HAND》的中英文正文、公众号叙事、结构化几何、指标、矩阵、视觉识别、离线网页与 PDF 由 OpenAI Codex 在 AmyLili28 的方向与审阅要求下独立生成。

空间约束来自仓库已公开且明确标注为临时粗略的边界资料；外部官方资料与案例只作事实依据或机制比较，并在 sources.json 和正文中标注。两个同行公开方案仅作为图面和证据组织质量基准，未复制其文字、几何、标识或构图。

本版使用七张由 OpenAI ImageGen 通过 Codex 内置图像生成服务完成的无文字概念底图。六张为纯文字生成；`lh-human-interchange-v1.jpg` 是对同一会话中先前由 ImageGen 文字生成的草稿作二次编辑，只把入口改成连续无台阶界面，没有使用外部或用户上传参考图。客户端没有另行暴露精确服务模型标识；源 PNG 的 C2PA 记录为 OpenAI Media Service API 的 `gpt-image` softwareAgent version `2.0`，而 Pillow 转出的投稿 JPG 不再保留可见 C2PA，所以本文件与 `sources.json` 构成包内可读溯源链。

AmyLili28 确定“搭把手”的项目方向、人情味、独立空间图和无生成式假文字要求；Codex 将已批准的方案概念、任务书与临时空间关系转成提示词，完成输出选择或同会话编辑，并以 Pillow 组织最终图。生成流程没有上传场地照片、网页图片、地图瓦片、可识别真人、商标、同行图面或艺术家风格；唯一图像输入是 Human Interchange 的同会话自生成草稿。所有人物与地点均为合成设计情境，不代表真实受访者、已发生的服务或已确认的场地。

| 来源 ID | 底图与生成方式 | 提示词摘要 | 最终用途与限制 |
|---|---|---|---|
| `MEDIA-LH-CORRIDOR-AERIAL-V1` | `lh-corridor-aerial-v1.jpg`；文字生成 | 有人帮助点、可达步行、休息与蓝绿公共空间的京张走廊氛围 | `site-overview`、`metrics-evidence`；准确几何和指标由 Pillow 后叠，非现状或绩效证据 |
| `MEDIA-LH-AXONOMETRIC-V1` | `lh-axonometric-v1.jpg`；文字生成 | 可逆服务桌、公共前场与公园连续性的斜轴测概念空间 | `land-use-structure`；分区、面积和审批边界由 Pillow 后叠，非法定用地图 |
| `MEDIA-LH-CAPABILITY-LAB-V1` | `lh-capability-lab-v1.jpg`；文字生成 | 有人解释、可逆家具、无假文字的能力班次实验室 | `key-areas`、`culture-operations`；非已建或已运营设施 |
| `MEDIA-LH-HUMAN-INTERCHANGE-V1` | `lh-human-interchange-v1.jpg`；同会话自生成草稿的 ImageGen 二次编辑 | 有人接站、纸数并行、座椅与连续无台阶入口 | `key-areas`、`culture-operations`；非无障碍合规结论或场地批准 |
| `MEDIA-LH-REPAIR-WORKSHOP-V1` | `lh-repair-workshop-v1.jpg`；文字生成 | 专业带领、低风险修补、工具隔离与无品牌日常物件 | `key-areas`、`culture-operations`；非维修资格、保修或实际服务记录 |
| `MEDIA-LH-RESPONSIBILITY-ROUTE-V1` | `lh-responsibility-route-v1.jpg`；文字生成 | 绿地水岸中的可达责任接力、人工节点、休息和纸图协助 | `mobility-bluegreen`；路线、长度、入口和临时几何由 Pillow 后叠，非测绘路线 |
| `MEDIA-LH-SCENARIO-MOSAIC-V1` | `lh-scenario-mosaic-v1.jpg`；文字生成 | 十二格问路、解释、无障碍协助、低风险修补与维护动作 | `scenario-matrix`；A01-A12 动作与 S01-S12 合同由 Pillow 分层标注，不声称一一对应、访谈或完成验证 |

site-overview、land-use-structure、key-areas、mobility-bluegreen、culture-operations、scenario-matrix 与 metrics-evidence 的中英文最终 PNG 由独立升级脚本使用 Pillow 将准确标题、编号、数字、证据边界和临时几何索引后叠。scenario-matrix 左侧只以 A01-A12 中性描述底图可见动作，右侧独立列出正文 S01-S12 正式场景合同标题，并明确两者不一一对应、底图不构成已运行或已验证场景证据。其余安全门、生态验证、后台 Agent、试点运营与 RACI/运营矩阵图继续使用本包既有确定性绘制版本。四份 PDF 由 ReportLab 重新排版。未使用未经授权的人物肖像、企业标识、采访引语或长段受版权保护文本。

生成与复用依据登记为 `OPENAI-TERMS-OF-USE-2026-08-31` 和 `OPENAI-SERVICE-TERMS-2026-08-31`：在法律允许范围内，OpenAI 与用户之间的输出权利归用户或由 OpenAI 转让，但输出可能不唯一，提交者仍负责输入、输出、第三方权利和具体用途。本投稿不据此声称排他版权、必然可版权、无侵权、真人模型授权、场地清权、机构背书或后续商用许可。`COMMUNITY-DISPLAY-ONLY` 只覆盖本仓库投稿展示；任何其他复用、宣传、实施或商业使用均须另行核验。

离线 HTML 使用 visual/assets/JingZhangCJK.css 内嵌的 Noto Sans SC 字体子集，字体以 SIL Open Font License 1.1 授权，完整许可文本保存在该 CSS 注释中；页面不请求外部字体或 CDN。

提交采用 COMMUNITY-DISPLAY-ONLY 展示授权。该说明不改变任何第三方资料、法规文本、官方标识或仓库内容的既有权利，也不构成法律意见。
