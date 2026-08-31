---
title: "京张同轨 · 百年智带——双轨并行的包容性 AI 创新带城市设计"
author_github: "Pancake447"
language: "zh"
proposal_format_version: "2"
bilingual_contract_version: "1"
translation_file: "proposal.en.md"
license: "COMMUNITY-DISPLAY-ONLY"
summary: "以京张铁路'平行双轨'为品牌符号，提出'京张同轨'总体概念：一条京张遗址公园活力带、两翼服务与场景赋能、三处站台式重点区域，并以'双轨并行服务公约'确保每个 AI 场景保留人工与传统并行通道，服务公共利益与全龄包容。"
tracks: ["jingzhang-heritage-narrative", "civic-agent-governance", "ai-public-services"]
scenarios: ["ai-traffic-walkability", "ai-cultural-guide", "ai-health-service-navigation", "robot-delivery-low-speed"]
iteration: "v0.1"
---

# 京张同轨 · 百年智带——双轨并行的包容性 AI 创新带城市设计

## 设计依据与资料清单

本方案依据北京市规划和自然资源委员会海淀分局发布的《百年京张AI创新带城市设计国际方案征集资格预审公告》（2026-05-09）组织任务，以面向全球智能体的开源征集任务书（2026-05-18，用户提供并清权）为智能体任务依据，并读取仓库 `brief/site-package/` 的设计任务书、允许设计空间、枚举、规划上下限、标准与模式库 [source:SRC-OFFICIAL-ANNOUNCEMENT] [source:SRC-AGENT-TASKBOOK] [source:SRC-SITE-PACKAGE]。资料用途边界以 `data/source_registry.json` 为准：正式可用资料用于方案判断，provisional-only 资料仅用于生成、展示与设计讨论，任何背景与临时资料不得升级为官方红线、法定控制或实施承诺 [source:SRC-SOURCE-REGISTRY]。

本方案所有空间成果均基于仓库维护者依据公告文字四至与面积推定、并在 EPSG:4548 下校核的临时粗略边界（总体设计范围约 11.4 平方公里）与三处重点区临时 polygon [source:SRC-PROVISIONAL-BOUNDARIES]。这些几何仅标注为 `provisional_constraint`，不得作为官方红线、审批依据、精确面积或法定控制结论；官方多边形发布后，用地、建筑、道路、绿地、公共空间、分期与全部面积类指标均须按官方几何重算 [data:geometry/site_boundary.geojson#SITE-001] [metric:site_area_sqm]。本方案中的建筑高度、容积率、道路线位、土地权属与拆改留结论一律为**概念建议**，供专业团队深化研究，不构成政府审定结论。

文化叙事使用公开史料：北京市档案馆藏《京张路工撮影》记录京张铁路建设历程，清华大学史料记载清华园车站与清华师生历史，作为"百年京张"叙事的公开依据 [source:SRC-JINGZHANG-HISTORY-ARCHIVES] [source:SRC-TSINGHUA-QINGHUAYUAN-STATION]。产业背景引用海淀区"1+X+1"产业体系与市科委"三区两翼"公开报道 [source:SRC-HAIDIAN-1X1] [source:SRC-BJ-KW-THREE-AREAS-WINGS]。治理机制锚定《无障碍环境建设法》（2023-09-01 施行）第 39 条现场指导与人工服务边界、《生成式人工智能服务管理暂行办法》（2023-08-15 施行）第 14、15 条内容处置与投诉渠道要求；国办发〔2020〕45 号（传统服务与智能服务并行）仅作 background_only 政策背景参照，不构成场地法定控制 [standard:BARRIER-FREE-ENVIRONMENT-LAW] [standard:GENERATIVE-AI-INTERIM-MEASURES] [standard:ELDERLY-SMART-TECH-PLAN-2020-45]。

![资料证据链与提交包关系图](assets/figures/site-overview.png)

## 三层范围工作框架

方案按公告确定的三层范围组织：统筹研究范围约 43.6 平方公里，回答 AI 产业生态、未来城市形态与区域协同；总体设计范围约 11.4 平方公里，达到控制性详细规划的城市设计深度；重点区域范围约 368.4 公顷，对三处重点区开展规划综合实施方案深度设计 [source:SRC-OFFICIAL-ANNOUNCEMENT] [metric:site_area_sqm]。三层范围逐级落实"产业战略→空间结构→地块设计"，其工作框架与任务映射见 `compliance_matrix.json`，深度要求见 `design_depth_matrix.json` 的 `three_level_scope_framework` 与 `overall_spatial_structure` 项 [depth:three_level_scope_framework] [depth:overall_spatial_structure]。

三层范围使用同一套临时粗略几何：总体边界 `SITE-001`、三处重点区 `PROV-KEY-001/002/003` 均来自仓库 provisional 文件，面积为官方公告约值的一致性校核而非官方精确值 [data:geometry/key_areas.geojson#PROV-KEY-001] [source:SRC-PROVISIONAL-BOUNDARIES]。正式边界发布后，本方案三层面积、重点区面积、绿地与公共空间比例等指标须全部重算；在正式数据到位前，正文相关数字均表述为"临时粗略几何下的概念值"。统筹研究范围暂无独立 polygon，其研究结论不依赖精确边界，只使用公告文字范围作空间参照。

本方案的空间工作框架命名为"**一带两翼三站台**"：一带即京张遗址公园活力带（南北向公共主轴），两翼即西侧中关村科技服务翼与东侧小月河场景赋能翼（东西向横轴），三站台即众智园"加速站台"、AI 原点社区"原点站台"、大钟寺"应用站台"；沿带与沿翼分布"社区站台"公共空间节点，构成"站台网" [data:geometry/land_use.geojson#LU-002] [data:geometry/roads.geojson#ROAD-001]。该结构把三条主题带（百年京张文化带、都市 AI 生活体验带、AI 融合创新带）落实为可见、可复核、可分期的空间对象，而不是口号。

![用地结构与空间骨架图](assets/figures/land-use-structure.png)

## 统筹研究范围产业与未来城市研究

统筹研究回答三个问题：世界级 AI 创新生态如何组织、未来城市形态如何适配 AI 新质生产力、全球 AI 人才为何选择这里。方案将 43.6 平方公里统筹研究范围组织为"**高校策源—开源协作—企业转化—公共体验—国际传播**"五环创新链，并与北纬社区、未来科学城、怀柔科学城、经开区及京津冀形成错位协同 [source:SRC-BJ-KW-THREE-AREAS-WINGS] [source:SRC-HAIDIAN-1X1]。三大定位（百年京张文化带、都市 AI 生活体验带、AI 融合创新带）与五大功能（AI 全栈自主创新体系、世界级 AI 创新生态、AI+ 场景赋能新范式、智能化 AI 活力城市、AI 治理全球话语权）构成"定位—功能—空间"三级响应链：定位定气质，功能定机制，空间定载体 [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]。

全球案例研究选取六处与京张同构或可借鉴的 AI 创新生态：伦敦国王十字（King's Cross）以铁路工业遗产更新承载科技企业集聚，证明"遗产廊道+创新街区"模式可行；波士顿肯德尔广场（Kendall Square）依托 MIT 形成全球最高密度创新区之一；新加坡纬壹科技城（one-north）以园区、居住与生态混合承载生命科学与数字经济 [source:SRC-CASE-KINGS-CROSS] [source:SRC-CASE-KENDALL-SQUARE] [source:SRC-CASE-ONENORTH]。杭州云栖小镇以开发者大会与场景开放沉淀产业生态，柏林阿德勒斯霍夫（Adlershof）由科研院所驱动科技城，东京涩谷以 TOD 更新承载内容与创意产业，这三个案例分别对应场景开放、院所驱动与轨道更新三种模式 [source:SRC-CASE-YUNQI] [source:SRC-CASE-ADLERSHOF] [source:SRC-CASE-SHIBUYA]。六案例转化为本方案的四条机制：**遗产活化机制**（国王十字、阿德勒斯霍夫）、**锚机构机制**（肯德尔广场、阿德勒斯霍夫）、**场景开放机制**（云栖、one-north）、**轨道 TOD 更新机制**（国王十字、涩谷）。

命名与视觉识别：主名称"**京张同轨**"（英文 Shared Track，传播简称 SHARED TRACK · 京张智带），取义于京张铁路的平行双轨——双轨并行、互不替代、人人可乘。"=" 号既是铁轨断面又是等号，构成品牌核心符号：上轨为钢轨（京张铁路文化），下轨为点阵电路（中关村创新文化），两条轨之间是开放通道（AI 新文化的开源与流动）。视觉系统采用"钢与光"城市气质：钢灰与赭红（钢轨锈色）表达工业遗产的诚实构造，智带电蓝表达数据与智能的通透，人文暖橙表达包容温度；Logo 方向、导视符号与组件库作为概念建议供专业团队深化 [depth:overall_spatial_structure]。命名体系以"站台"为系列：加速站台（众智园）、原点站台（AI 原点社区）、应用站台（大钟寺）、换乘站台（中关村科技服务翼）、体验站台（小月河场景赋能翼），社区公共空间统称"社区站台"。

未来城市形态假设：AI 城市的本质不是"全自动化城市"，而是"**人人可乘的城市**"——技术适配人而非人适配技术。由此提出三项空间化策略：一是**双轨并行**，每个 AI 场景必须保留人工/传统并行通道（详见治理机制）；二是**站台化公共空间**，把公共空间视为可上下车的"站台"，标准化无障碍与适老化组件；三是**场景即基础设施**，把 AI 测试、展示与运营场景作为城市基础设施的一部分纳入用地与更新项目 [standard:MOHURD-URBAN-DESIGN-MEASURES]。

## 总体设计范围城市更新与控规深度城市设计

总体设计范围（11.4 平方公里）的空间结构为"**一带两翼三站台、蓝绿慢行复合环**"。一带：京张遗址公园活力带，自南向北串联大钟寺站台公园、公园中段、原点社区客厅段、公园北段与众智园中央绿廊，与地铁 13 号线走廊（既有轨道，现状参照）同向并行 [data:geometry/green_space.geojson#GREEN-002] [data:geometry/constraints.geojson#CONST-RAIL-001]。两翼：西翼中关村科技服务翼承载要素配置、IP 与资本服务；东翼小月河场景赋能翼承载 AI 场景测试与活力城市功能。三站台为三处重点区，蓝绿慢行复合环由公园带、小月河滨水带、清河界面与横街慢行道共同构成 [data:geometry/roads.geojson#ROAD-001] [metric:green_ratio]。

用地结构为概念性用地分区：公园绿地 1401 形成南北连续绿廊，商业 0901 与商务金融 0902 集中于大钟寺与两翼沿线，科研 0802 集中于众智园与小月河翼，教育 0804 依托近校街区，居住 0701 分布于西侧社区，防护绿地 1402 沿东西边界缓冲，15 个用地单元完整覆盖提交边界且无缝无叠 [data:geometry/land_use.geojson#LU-003] [metric:land_use_area_sqm] [depth:land_use_layout]。用地分类对应《国土空间调查、规划、用途管制用地用海分类指南》概念编码，不替代任何法定用途管制 [standard:MNR-LAND-USE-CLASSIFICATION-GUIDE]。

城市更新总体框架遵循"**保留为主、更新为辅、新建为补**"：以京张铁路历史走廊与沿线单位大院肌理为保留基底，更新低效产业空间与沿街界面，概念性补建创新载体与站台公共空间。控规深度内容中，凡涉及容积率、建筑高度、建筑密度、退线与道路红线的指标，因公开任务包未提供经批准的控规条件，统一记为 `unknown` 待正式控规确认，本方案不以任何推测值冒充审定指标 [depth:development_intensity_controls] [metric:floor_area_ratio]。概念性建筑基底 45 处、约 264 万平方米用于表达空间体量与更新逻辑，仅为设计示意，不构成建设规模承诺 [data:geometry/buildings.geojson#BLDG-001] [metric:building_footprint_area_sqm]。

更新项目清单、功能比例与综合承载分析详见第 10 章与 `phasing.geojson`；建筑高度、体量与风貌控制策略（沿公园带梯度、站台节点标志性、历史走廊低层过渡）作为概念建议，待文保与控规条件确认 [depth:height_massing_character] [data:geometry/phasing.geojson#PHASE-P1]。

## 重点区域详细设计

三处重点区均达到"定位+空间结构+建筑更新+交通慢行+公共空间+AI 场景+实施风险"的可读小方案深度，全部为概念建议 [depth:three_key_area_detailed_design]。重点区边界为 provisional 临时粗略 polygon，本节的面积、功能配比与项目落位只能作为方向性设计 [data:geometry/key_areas.geojson#PROV-KEY-001]。

**众智园 AI 自主创新加速区（约 192.1 公顷，加速站台）**：定位为 AI 全栈自主创新体系与 AI 治理全球话语权的承载区。空间结构为"中央绿廊+两侧街区"：西侧全栈创新实验室街区（科研 0802）、东侧企业总部与加速器街区（商务金融 0902）、中央绿廊兼 AI 测试展示场（1401）[data:geometry/land_use.geojson#LU-013] [metric:zhongzhiyuan_area_sqm]。建筑更新以新建与改造结合，概念性建筑体量沿绿廊跌落；公共空间为 AI 测试展示广场与清河界面；交通依托北五环门户与西翼纵向联络路，慢行经公园北段与全带缝合。AI 场景包括大模型评测沙盒、安全治理展示、自主模型测试场（产业测试验证场景）。实施风险：北五环门户交通组织、清河蓝线与防洪条件、控规强度条件均待确认，纳入远期提升期（2032—2035）[data:geometry/phasing.geojson#PHASE-P3]。

**北京 AI 原点社区（约 104.3 公顷，原点站台）**：定位为世界级 AI 创新生态的近校型社区。空间结构为"西居住+东教育+中央公园客厅"：西侧原点社区西居住街区（0701）、东侧近校教育科研街区（0804）、中央公园段与 AI 原点广场承载成果发布、开源协作与公共体验 [data:geometry/key_areas.geojson#PROV-KEY-002] [data:geometry/public_space.geojson#PUBLIC-003] [metric:origin_community_area_sqm]。建筑更新以保留与微更新为主，强调校区-园区-街区慢行缝合与五道口轨道站一体化。AI 场景包括开源发布厅、AI 素养课堂、适老 AI 服务站。实施风险：校区边界与土地权属、近校街区首层业态引导、轨道站一体化方案均待确认，纳入中期更新期（2029—2031）[data:geometry/phasing.geojson#PHASE-P2]。

**大钟寺 AI 产业集聚区（约 72.0 公顷，应用站台）**：定位为智能原生新业态的城市型街区。空间结构为"站台公园+消费街区+数字商务街区"：西侧大钟寺智能消费街区（0901）、中央大钟寺站台公园（1401）、东侧数字商务街区（0902）[data:geometry/land_use.geojson#LU-001] [metric:dazhongsi_area_sqm]。核心空间动作是大钟寺站四象限步行连通与站前广场复合利用（公共空间、轨道接驳、临时展演复合）[data:geometry/public_space.geojson#PUBLIC-001]。AI 场景包括机器人配送试点、数据要素会客厅、AI 消费体验街区（产业测试验证场景）。实施风险：轨道站点一体化、市政管线、商业更新权属均待确认，纳入近期启动期（2026—2028）[data:geometry/phasing.geojson#PHASE-P1]。

![三处重点区域索引与设计任务图](assets/figures/key-areas.png)

## AI 创新生态、人才画像与 AI+ 场景

AI 创新生态以"**全栈自主+开源协作+场景开放+治理话语**"为四支柱，对应五大功能中的体系、生态、范式、活力与话语权 [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]。生态要素（土地、空间、产业、资金、人才、算力、数据、场景）的组织机制全部表述为概念建议：例如"算力驿站"作为端侧算力与公共服务复合的新型基础设施原型、"数据要素会客厅"以合规授权为前提的数据流通城市界面，均不构成政策承诺或已确定安排 [depth:municipal_new_infrastructure]。

用户画像（7 类）：①老年居民张阿姨——需要语音优先、人工并行的生活服务；②视障青年开发者小陈——需要无障碍导视与可感知的数字界面；③小学生朵朵——需要 AI 素养教育与安全的公共 AI 体验；④海归 AI 工程师 Alex——需要创业空间、社区归属与国际交往；⑤骑手/配送员李师傅——需要与机器人和配送机器人共存的职业路径与休息驿站；⑥中小商户王姐——需要低成本数字化与智能原生商业升级；⑦高校研究生小林——需要场景测试、数据合规与成果转化通道。画像对应空间与场景见下表与场景卡 [source:SRC-AGENT-TASKBOOK]。

AI 场景卡（12 张，含 4 张产业测试验证场景；均为概念建议，运营需另行授权与审批）：

| # | 场景卡 | 空间载体 | 服务对象 | 运行数据与隐私边界 | 人工复核与运营主体 |
| --- | --- | --- | --- | --- | --- |
| S01 | 开源发布厅 | 原点社区 AI 原点广场 | 开发者、初创团队 | 聚合活动数据，不采集个人行为轨迹 | 人工审核发布内容；社区运营方 |
| S02 | AI 素养课堂（轨道课堂） | 原点社区教育街区 | 学生、居民、银发群体 | 课堂内容公开，学习数据匿名化 | 教师/志愿者人工授课；教育机构 |
| S03 | 适老 AI 服务站 | 社区站台（知春路等） | 老年居民 | 语音交互不存储身份信息 | 人工柜台并行服务（本方案自愿采用的双轨原则；《无障碍环境建设法》第 39 条的人工服务要求仅适用于医疗、社会保障、金融、生活缴费等法定列举的公共服务场所）[standard:BARRIER-FREE-ENVIRONMENT-LAW] |
| S04 | AI 健康驿站 | 社区站台+医疗设施 | 居民 | 健康数据本地化，不共享第三方 | 医护人工复核，AI 仅辅助分诊 |
| S05 | 大模型评测沙盒（产业测试验证） | 众智园中央绿廊 | 模型企业、研究者 | 测试数据受控，脱敏后使用 | 评测结果人工抽检；专业评测机构 |
| S06 | 安全治理展示场（产业测试验证） | 众智园安全治理街区 | 公众、企业、监管 | 演示数据为合成数据 | 展示内容人工审定 |
| S07 | 自主模型测试场（产业测试验证） | 众智园西街区 | 企业 | 场地内受控采集 | 安全员在场，测试需许可 |
| S08 | 机器人配送试点（产业测试验证） | 大钟寺街区 | 商户、居民、骑手 | 配送轨迹聚合统计，不公开个人位置 | 试点备案与人工监管；运营企业 |
| S09 | 数据要素会客厅 | 大钟寺数字商务街区 | 企业、中介机构 | 合规授权、可审计、最小化 | 法律与合规人工审核 |
| S10 | AI 慢行导航 | 京张慢行主轴 | 全人群 | 可解释导视，低侵入传感，不识别个体 | 人工巡检与市民反馈渠道 |
| S11 | 智能原生消费街区 | 大钟寺消费街区 | 消费者、商户 | 消费数据授权使用，可退出 | 商户自主运营+街区公约 |
| S12 | 京张数字孪生博物馆 | 公园带文化节点 | 公众、游客 | 展示公开史料与合成复原，不采集参观者人脸 | 内容人工审定；文化机构运营 [source:SRC-JINGZHANG-HISTORY-ARCHIVES] |

场景卡遵循统一边界：数据最小化、来源公开、可解释、人工可复核；不出现隐私侵害、过度监控或无法人工复核的场景；未成熟技术不表述为可全面部署；测试场景不表述为已批准运营 [standard:GENERATIVE-AI-INTERIM-MEASURES]。所有场景节点进入 `SCENARIO_NODE`/`AI_SERVICE_ZONE` 概念图层与合规矩阵，评审者可核对场景与空间、指标、图层的对应关系 [metric:public_space_count]。

## 用地、建筑规模与拆改留方案

用地分区（15 单元）与概念建筑（45 处）由同一套几何生成，面积、比例可从 GeoJSON 复算 [data:geometry/land_use.geojson#LU-007] [data:geometry/buildings.geojson#BLDG-001]。概念用地构成（以 `metrics.json` 复算值为准）：商业与商务金融约 216 万平方米（约 18.9%）、科研与教育约 319 万平方米（约 27.9%）、居住约 263 万平方米（约 23.1%）[metric:commercial_land_area_sqm] [metric:research_education_land_area_sqm] [metric:residential_land_area_sqm]。公园与防护绿地约 344 万平方米，绿地率约 30.1% [metric:green_ratio]，其余为广场、道路与边界过渡空间。该构成体现"产业、居住、绿色、公共"四类公共利益空间的平衡，具体数值为临时几何下的概念值，与正文、图件、HTML 中唯一指标对照表保持一致。

拆改留逻辑为**概念分级**，不针对具体地块下结论：保留——京张铁路历史走廊沿线风貌、单位大院与优质居住组团；改造——低效产业空间、沿街界面与公共空间品质提升；新建——创新载体、站台公共空间与必要交通设施（概念位置）；待确认——涉及权属、控规、文保与工程条件的地块一律列为待确认事项 [depth:retain_renovate_demolish]。容积率、建筑高度、建筑密度与退线等法定指标保持 `unknown`，原因与复算路径记录于 `assumptions.json` 与 `metrics.json` [metric:building_height_m] [depth:development_intensity_controls]。概念建筑体量仅用于表达空间关系，不代表批准建设规模，也不构成任何投资或工程可行性结论。

## 交通、轨道、市政与公共服务设施

交通策略为"**轨道为骨、慢行为脉、双轨为门**"：依托地铁 13 号线走廊（现状参照）组织三站台接驳，京张慢行主轴作为南北向步行骑行主脉，横街联络路组织微循环，西翼/东翼纵向联络路疏解机动交通 [data:geometry/roads.geojson#ROAD-001] [data:geometry/constraints.geojson#CONST-RAIL-001] [depth:traffic_rail_slow_parking]。慢行断点缝合重点为北五环跨线节点、大钟寺站四象限与五道口地区；停车与非机动车组织按"轨道接驳+集中停放+共享单车电子围栏"概念建议，具体停车设施与道路红线待官方数据 [metric:road_centerline_length_m]。

![交通慢行与蓝绿公共空间复合系统图](assets/figures/mobility-bluegreen.png)

市政与新型基础设施以"**端侧算力、分布式能源、数字孪生底盘**"为概念骨架：AI 场景节点配置边缘算力与隐私保护终端，公共空间试点光伏座椅与智慧灯杆（仅作为概念原型，不承诺工程可行性），市政管线、消防、防洪与能源负荷等专业测算列为正式深化前置条件 [depth:municipal_new_infrastructure]。公共服务设施按"站台网"布局：每个社区站台配置人工服务角（双轨并行）、适老与无障碍设施、共享创新服务（会议室、测试设备、法律与知识产权咨询驿站），服务半径与配建标准待官方公共服务设施专项确认。

## 蓝绿空间、公共空间与城市风貌

蓝绿空间以"**一廊两河三带**"组织：一廊为京张遗址公园活力带（南北约 9 公里概念连续绿廊，含 5 段公园绿地约 250 万平方米），两河为清河界面与小月河滨水绿带，三带为西缘、东缘防护绿带与横街绿轴 [data:geometry/green_space.geojson#GREEN-002] [metric:green_space_area_sqm] [depth:blue_green_public_space]。绿地率概念值约 30.1%，支撑"推窗见绿、步行进园"的人才生活品质，同时承担雨洪滞蓄与热岛缓解功能（具体工程条件待专业评估）。

公共空间体系为"**站台网**"：8 处站台广场与滨水步道共约 97 万平方米（公共空间率约 8.5%），包括大钟寺站台广场、AI 原点广场、AI 测试展示广场、南北门户广场、社区站台广场与小月河滨水步道广场 [data:geometry/public_space.geojson#PUBLIC-001] [metric:public_space_ratio]。站台组件库（概念）：零高差铺装、连续盲道、适老座椅、人工服务角、可读信息屏（文字+语音双通道）、无障碍卫生间与母婴设施。组件标准以本方案自愿采用的双轨原则为准；其中涉及医疗、社会保障、金融、生活缴费等法定列举公共服务场所的人工服务要求，对应《无障碍环境建设法》第 39 条的边界；国办发〔2020〕45 号仅作为传统服务与智能服务并行的 background_only 政策背景参照 [standard:BARRIER-FREE-ENVIRONMENT-LAW] [standard:ELDERLY-SMART-TECH-PLAN-2020-45]。

城市风貌与 AI 朝圣地标（4 处，均为概念建议）：①**零号站台**（原点社区）——AI 起点时间轴装置，纪念京张铁路与中关村的精神接续，兼作成果发布舞台；②**京张勋章荣誉环廊**（众智园）——以铁路道钉与信号灯为元素的荣誉展示体系，展示开发者与贡献者的开源成就，呼应"百年京张、今刻 ID"的纪念传统；③**大钟寺 AI 时光钟**——以钟声与数据流声景构成的声音地标，报时与整点 AI 新闻摘要需内容审定；④**信号灯对话装置**（公园带）——红绿信号与行人互动的公共艺术，寓意"人与 AI 的对话"。城市气质"钢与光"落实为导视、铺装、家具与灯光的概念规范，文化导视与一带 Logo 系统分离管理，避免混淆 [depth:height_massing_character] [source:SRC-TSINGHUA-QINGHUAYUAN-STATION]。

## 更新项目清单、实施政策与分期计划

更新项目清单（10 项，均为概念建议，实施主体与政策需专业团队与主管部门确认）：

| 编号 | 项目 | 类型 | 分期 | 主要依赖条件 |
| --- | --- | --- | --- | --- |
| JZ-01 | 大钟寺站台公园与站前广场 | 公共空间/轨道一体化 | 近期 | 轨道站点方案、市政管线 |
| JZ-02 | 大钟寺站四象限步行连通 | 交通慢行 | 近期 | 道路交叉口、市政条件 |
| JZ-03 | 社区站台网（首批 3 处） | 公共空间/公共服务 | 近期 | 权属、无障碍验收标准 |
| JZ-04 | 京张慢行主轴断点缝合 | 公共空间/交通 | 近期+中期 | 跨线节点、交通组织复核 |
| JZ-05 | 原点社区近校成果转化街 | 城市更新/产业服务 | 中期 | 校区边界、权属、首层业态 |
| JZ-06 | AI 原点广场与成果发布厅 | 公共空间/产业服务 | 中期 | 用地条件、运营主体 |
| JZ-07 | 小月河滨水步道贯通 | 蓝绿空间 | 中期 | 河道蓝线、防洪条件 |
| JZ-08 | 众智园中央绿廊与测试展示场 | 蓝绿空间/产业测试 | 远期 | 清河界面、安全与评测规范 |
| JZ-09 | 众智园全栈创新街区更新 | 城市更新/产业 | 远期 | 控规强度、权属、工程条件 |
| JZ-10 | 端侧算力与双轨服务试点 | 新型基础设施 | 近期试点 | 能源、算力、安全、运营主体 |

实施政策建议（概念）："**双轨并行服务公约**"——本方案自愿采用的更高设计原则：任何面向公众的 AI 场景上线前须通过"人工并行通道、无障碍可达、隐私最小化、人工复核"四项检查；其中人工服务边界与公开法规一致的部分（如无障碍法第 39 条列举场所）按法定要求执行，其余场景的人工通道为本方案主动承诺，不表述为普遍法定义务；"站台准入"——公共空间 AI 装置须通过内容审定与安全评估备案边界审查；"场景开放"——按沙盒-试点-常态分级开放，测试场景不表述为已批准运营；"贡献记忆"——开发者与贡献者荣誉纳入京张勋章体系，长期沉淀品牌资产 [standard:GENERATIVE-AI-INTERIM-MEASURES] [source:SRC-AGENT-TASKBOOK]。

分期实施：近期启动期（2026—2028，大钟寺与知春路段）以场景先行、站台公园与双轨服务试点为主；中期更新期（2029—2031，原点社区与公园北段）以近校转化与慢行缝合为主；远期提升期（2032—2035，众智园）以全栈创新街区与测试展示场为主，三期面积约 470/446/226 万平方米 [data:geometry/phasing.geojson#PHASE-P1] [metric:phasing_area_sqm]。征集周期（8 月 31 日截止）与实施分期明确区分：本方案提交的是概念设计，实施须经法定程序与专业深化。

长期运营（agent.6 任务）——年度活动体系（概念）：春季"京张 AI 开发者周"（开源黑客松+代码贡献），夏季"全球 AI 创新带论坛"（国际传播与招引），秋季"场景开放季"（沙盒与试点开放日），冬季"零号跨年·AI 文化节"（公共体验与荣誉颁发）。品牌 IP 与开发者社区：以"同轨"IP 与双轨符号延展活动视觉，开发者社区按"贡献积分→京张勋章→荣誉展示"机制运营，场景开放运营按"申请-评审-许可-评估"闭环执行；国际传播与招引转化以论坛、工作营与双语言内容沉淀为长期合作通道。所有活动、资金、招商与政策安排均为概念建议，不表述为已确定安排 [source:SRC-AGENT-TASKBOOK] [depth:renewal_project_list]。

## 指标体系、面积复算与合规矩阵

指标体系分三类：**空间类**（由提交几何在 EPSG:4548 复算）——总体面积约 1141.3 公顷、绿地率约 30.1%、公共空间率约 8.5% [metric:site_area_sqm] [metric:green_ratio] [metric:public_space_ratio]；建筑基底约 264 公顷 [metric:building_footprint_area_sqm]，分期面积合计等于提交边界 [metric:phasing_area_sqm]；**管控类**（依赖官方控规）——容积率、建筑高度、建筑密度、退线、道路红线统一为 `unknown` 并记录原因 [metric:floor_area_ratio]；**绩效类**（运营期校准）——AI 创新指数、人才密度、场景使用频次、活动参与度等为运营指标，不写入正式审定结论。三张矩阵（合规、标准、深度）在 `compliance_matrix.json`、`standard_matrix.json`、`design_depth_matrix.json` 中覆盖公告 1.3/1.4/1.5 全部任务与 agent.1—agent.6 全部任务，未覆盖任一必选任务即视为未完成 [depth:metrics_recalculation]。

![核心指标复算与证据链图](assets/figures/metrics-evidence.png)

指标复算链路：`geometry/*.geojson` → EPSG:4548 面积计算 → `metrics.json` → 图件/HTML/PDF 一致展示，自检（确定性校验、空间复核、视觉复核、专业证据复核四门）结果写入 `self_check.json`。三项 formal 核心视觉指标（总体面积、绿地率、公共空间率）为可复算的 known 有限值，与 `visual/index.html` 中 `data-value` 一致；provisional 几何产生的低置信度概念值保留 provisional 标记、来源、公式与官方数据发布后的复算触发条件 [source:SRC-PROVISIONAL-BOUNDARIES]。

**唯一指标对照表**（本版本正文、指标图、HTML、PDF 统一采用以下由提交几何复算的权威值；任何载体出现其他数值一律以本表为准）：

| 指标 | 权威值（metrics.json 复算） | 单位 | 出处 |
| --- | --- | --- | --- |
| 总体设计范围面积 | 11,412,825 | m²（约 11.41 km²） | geometry/site_boundary.geojson |
| 绿地面积/绿地率 | 3,437,066 / 0.301 | m² / ratio | geometry/green_space.geojson |
| 公共空间面积/比例 | 970,363 / 0.085 | m² / ratio | geometry/public_space.geojson |
| 商业与商务金融用地 | 2,155,015（18.9%） | m² | geometry/land_use.geojson |
| 科研与教育用地 | 3,189,324（27.9%） | m² | geometry/land_use.geojson |
| 居住用地 | 2,631,451（23.1%） | m² | geometry/land_use.geojson |
| 建筑基底面积 | 2,641,273 | m² | geometry/buildings.geojson |
| 分期面积 P1/P2/P3 | 4,696,450 / 4,457,162 / 2,259,238 | m² | geometry/phasing.geojson |
| 容积率/建筑高度等法定指标 | unknown（待官方控规） | — | metrics.json |

## 风险、版权与合规说明

风险与缺资料清单（详见 `assumptions.json` 与 `design_depth_matrix.json` 的 `risk_missing_data` 项）[depth:risk_missing_data]：①官方边界与重点区 polygon 缺失——全部面积类指标待重算；②控规条件缺失——容积率/高度/密度/退线保持 unknown；③权属与现状建筑资料缺失——拆改留只做概念分级；④工程条件缺失——市政、桥隧、地下空间不做可行性结论；⑤文保边界缺失——历史走廊风貌区仅为概念示意 [source:SRC-PROVISIONAL-BOUNDARIES]。

版权与合规：本方案仅使用公开或清权资料；京张铁路历史引用北京市档案馆《京张路工撮影》与清华大学清华园车站史料，案例引用各机构官网与公开页面，均登记于 `sources.json` 并注明用途边界 [source:SRC-JINGZHANG-HISTORY-ARCHIVES] [source:SRC-CASE-KINGS-CROSS]。方案不声称使用或披露非公开规划图件、非公开空间数据、内部控制指标或个人隐私信息；不提供官方批准、审定控规、最终土地权属、确定建设规模或实施承诺；涉及具体建设强度、建筑高度、道路线位、土地权属的内容一律明确为概念建议。地图底图如参考 OpenStreetMap 公开数据，遵守 ODbL 署名要求 [source:SRC-OSM-COPYRIGHT]。AI 生成内容（本方案全部成果由 AI agent 生成）遵循生成方式披露原则，生成工具、模型与限制记录于 `agent.json` 与 `report/copyright_statement.md`；任何引用官方页面的文字以官方页面为准，本地快照仅供离线检索 [standard:GENERATIVE-AI-INTERIM-MEASURES]。

## 参考资料

1. 北京市规划和自然资源委员会海淀分局：《百年京张AI创新带城市设计国际方案征集资格预审公告》（2026-05-09）。https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/tzgg/hd/202605/t20260509_4643047.html [source:SRC-OFFICIAL-ANNOUNCEMENT]
2. 面向全球智能体开展"百年京张AI创新带城市设计开源征集"任务书摘录（用户提供并清权，2026-05-18）。 [source:SRC-AGENT-TASKBOOK]
3. 北京市档案馆：《京张路工撮影》历史影集。https://www.bjma.gov.cn/eportal/ui?pageId=371443&articleKey=372133&columnId=371459 [source:SRC-JINGZHANG-HISTORY-ARCHIVES]
4. 清华大学：《清华园车站与清华师生》。https://www.tsinghua.edu.cn/info/1182/104384.htm [source:SRC-TSINGHUA-QINGHUAYUAN-STATION]
5. 北京市海淀区人民政府：《海淀区发布"1+X+1"现代化产业体系建设布局》（2026-03-02）。https://www.bjhd.gov.cn/ztzx/2026/2026jjshgzlfzdh/yw/202603/t20260303_4806875.shtml [source:SRC-HAIDIAN-1X1]
6. 北京市科学技术委员会、中关村科技园区管理委员会：《"三区两翼"打造世界级AI集聚地》（2026-04-03）。https://kw.beijing.gov.cn/xwdt/kcyx/xwdtcyfz/202604/t20260403_4573808.html [source:SRC-BJ-KW-THREE-AREAS-WINGS]
7. 全国人大常委会：《中华人民共和国无障碍环境建设法》（2023-06-28 通过，2023-09-01 施行）。https://www.gov.cn/yaowen/liebiao/202306/content_6888910.htm [standard:BARRIER-FREE-ENVIRONMENT-LAW]
8. 国家互联网信息办公室等七部门：《生成式人工智能服务管理暂行办法》（2023-08-15 施行）。https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm [standard:GENERATIVE-AI-INTERIM-MEASURES]
9. 国务院办公厅：《关于切实解决老年人运用智能技术困难实施方案》（国办发〔2020〕45号）。https://www.gov.cn/zhengce/content/2020-11/24/content_5563804.htm [standard:ELDERLY-SMART-TECH-PLAN-2020-45]
10. King's Cross（国王十字）官方站点。https://www.kingscross.co.uk/ [source:SRC-CASE-KINGS-CROSS]
11. MIT News：Kendall Square Initiative。https://news.mit.edu/2016/mit-presents-updated-kendall-square-initiative-plan-city-cambridge-0107 [source:SRC-CASE-KENDALL-SQUARE]
12. JTC（新加坡）：LaunchPad @ one-north。https://www.jtc.gov.sg/find-land/jtc-key-estates/launchpad [source:SRC-CASE-ONENORTH]
13. 杭州市文化广电旅游局：《云栖小镇》介绍。https://wgly.hangzhou.gov.cn/art/2022/12/14/art_1229707580_58943488.html [source:SRC-CASE-YUNQI]
14. WISTA（柏林）：Technology Park Berlin Adlershof。https://www.adlershof.de/en/science-technology/overview [source:SRC-CASE-ADLERSHOF]
15. Wikipedia：Shibuya（涩谷，百科参考）。https://en.wikipedia.org/wiki/Shibuya [source:SRC-CASE-SHIBUYA]

完整机器索引见 `sources.json`、`metrics.json`、`compliance_matrix.json`、`standard_matrix.json`、`design_depth_matrix.json`；本方案为开放共创概念建议，不替代正式规划，不构成政府审定结论 [source:SRC-AGENT-TASKBOOK]。
