# 方案迭代记录

## v1.1 - 2026-09-01

- 修复 intake 校验：frontmatter scenarios 对齐官方场景注册表（6 个合法 id）
- 增厚「用地、建筑规模与拆改留方案」章节并拆分 4 连证据标记
- geometry 九个图层的 layer/source_type/confidence/building_type 对齐官方枚举
- metrics.json 增加顶层 units；standard_matrix 补全 10 项必填字段
- compliance_matrix 重写为 requirements 结构，覆盖 23 项公告与智能体任务
- manifest 哈希统一为纯 sha256 口径并列入 manifest 自身；删除两个 README 占位文件
- 报告 HTML 补全 <main> 主结构标签

## v1.0 - 2026-08-31

- 首次提交：以稷下书院多智能体辩论框架为核心设计理念
- 三种哲学人格（名家/道家/墨家）分别主持三个重点区域，辩论走廊连接三所讲堂
- 12张场景卡、3处朝圣地标、5类用户画像、8个全球AI创新生态案例
- 全部几何为 provisional_constraint，待官方数据复算；中英双语提交
