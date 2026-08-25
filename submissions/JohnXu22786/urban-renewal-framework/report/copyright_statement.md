# Copyright Statement 与资产权利台账（Asset Rights & Generation Ledger）

## 版权声明

本包提交的全部正文、几何、图件、PDF 与静态 HTML 资产均由声明的 AI 智能体生成或使用 sources.json 中登记的公开/用户提供并经清理的来源；visual/index.html 不引用任何远程资产。引用公开资料均标注来源与获取时间；原创内容保留作者权利；不引用未授权资料；与既有标识或名称雷同属巧合。

## 品牌在先权利与使用边界

本方案未在概念阶段完成官方商标检索：「更新枢（RENEW·JZ）」「留改坊」「单元坊」「督行亭」及 Logo 图形与双语标语均按内部工作代号处理；对外使用、申报注册或正式命名前须完成在先权利清查与相关方许可。与 sources.json 资产条目（ASSET-LOGO-RENEW-JZ 等）及 manifest.json 角色说明保持一致。本声明不构成官方商标检索结论。

## 逐资产权利台账（与 sources.json 资产条目一一对应）

| 资产类别 | 资产/文件 | 生成方式 | 权利状态 | 许可与署名（license 字段） | 复用限制 |
| --- | --- | --- | --- | --- | --- |
| Logo/标识 | assets/figures/logo-update-hub.png | AI概念提示+matplotlib 绘制 | 本包作者原创概念 | COMMUNITY-DISPLAY-ONLY；署名 JohnXu22786 / dsh-haidian-agent | 仅方案展示；检索完成前不对外注册、不正式命名 |
| 名称/标语 | 「更新枢（RENEW·JZ）」「留改坊」「单元坊」「督行亭」及双语标语 | AI生成+人工整理 | 本包作者原创概念 | COMMUNITY-DISPLAY-ONLY | 内部工作代号；对外使用前须在先权利清查 |
| 字体 | HTML 内嵌子集（Noto Sans SC） | 从 Noto Sans SC 静态版子集化 | 第三方开放许可 | SIL Open Font License 1.1（Google Fonts） | OFL 允许内嵌与子集化；不得转售或改名分发字体本体 |
| 图标/图形元素 | 图件中的示意图标（节点、慢行、绿带等符号） | matplotlib 矢量绘制 | 本包作者原创 | COMMUNITY-DISPLAY-ONLY | 仅方案展示；不使用第三方图标库素材 |
| 图片 | 全部 PNG 图件（assets/figures/*.png 中文+英文共 14 张） | AI概念提示+matplotlib 确定性绘制 | 本包作者原创 | COMMUNITY-DISPLAY-ONLY | 图内不含第三方照片与网络图片素材 |
| 地图底图 | geometry/*.geojson 概念图形 | 依据公告文字口径与 provisional 边界生成 | 本包作者原创（provisional） | COMMUNITY-DISPLAY-ONLY | 仅概念展示与机器校验；不作为官方边界、红线或审批依据 |
| 数据 | metrics.json / sources.json 等结构化记录 | 确定性脚本计算与人工核验 | 本包作者整理 | COMMUNITY-DISPLAY-ONLY | 引用公开来源均登记出处与访问日期；官方数据发布后复算 |
| 代码 | 生成脚本（matplotlib/几何计算，仓库 scripts 目录） | 本包作者编写 | 本包作者原创 | 按仓库规则 | 仅在仓库内复用 |
| AI 生成内容 | 方案正文、双语文本、叙事文案 | deepseek-v4-flash（dsh-x）生成+人工复核 | 本包作者按征集规则提交 | COMMUNITY-DISPLAY-ONLY | AI 生成内容已人工复核；不用于误导性事实主张 |
| 案例参考 | 案例表及 sources.json 案例条目 | 公开网页核验（2026-08-25 访问） | 引用对象归各机构所有 | 仅浏览级引用，不复制内容 | 仅概念借鉴；正式引用前须事实交叉核验 |

特殊声明：本包未使用任何未经授权的人物肖像、商标图形、论文图表或版权图片；图件与正文中的铁路历史叙事仅引用公开史料方向性表述，不歪曲历史事实。清单随方案迭代逐件更新；新增资产须先在 sources.json 登记再进入 manifest.json。