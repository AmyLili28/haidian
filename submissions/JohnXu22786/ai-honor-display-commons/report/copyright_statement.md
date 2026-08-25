# 资产权利清单（Asset Rights Ledger，附于版权声明）

> 逐项登记本包各类资产的权利来源、许可与复用边界；与 sources.json 资产条目、manifest.json 角色注释及版权声明保持一致。概念阶段未完成商标检索的品牌名称仅作为内部工作代号。

## 1. 文字与正文（Text）

| 资产 | 来源 | 许可/权利状态 | 复用边界 |
|---|---|---|---|
| proposal.md（中文正式正文） | 智能体原创生成（DeepSeek Harness, dsh-x） | 原创，COMMUNITY-DISPLAY-ONLY | 本包展示与专业团队深化研究 |
| proposal.en.md（英文正式译文） | 由中文正文人工核对翻译 | 同上 | 同上；中英实质等值已人工核对 |

## 2. 图件（Figures）

| 资产 | 来源 | 许可/权利状态 | 复用边界 |
|---|---|---|---|
| assets/figures/site-overview.png（.en） | 由 geometry/metrics 数据确定性脚本生成 | 原创生成成果 | 本包展示；标注 provisional |
| assets/figures/land-use-structure.png（.en） | 同上（数据：geometry/land_use.geojson） | 同上 | 同上 |
| assets/figures/key-areas.png（.en） | 同上（数据：geometry/key_areas.geojson 等） | 同上 | 同上 |
| assets/figures/mobility-bluegreen.png（.en） | 同上（数据：geometry/roads|green_space|public_space） | 同上 | 同上 |
| assets/figures/metrics-evidence.png（.en） | 同上（数据：metrics.json） | 同上 | 同上 |
| assets/figures/ecosystem-map.png（.en） | 同上（概念图谱） | 同上 | 同上 |
| assets/figures/logo-jz.png（语言中立） | 原创标志概念 | 原创；商标清查前不对外使用 | 见品牌在先权利条款 |

## 3. 图纸（Drawings）

| 资产 | 来源 | 许可/权利状态 | 复用边界 |
|---|---|---|---|
| drawings/a0-boards.pdf（.en） | 确定性脚本生成，嵌入 Noto Sans SC 子集 | 原创生成成果；字体按 OFL 1.1 | 本包展示；非工程图纸 |
| drawings/a3-booklet.pdf（.en） | 同上 | 同上 | 同上 |

## 4. 字体（Fonts）

| 资产 | 来源 | 许可 | 复用边界 |
|---|---|---|---|
| Noto Sans SC 静态实例 wght400 + 逐页子集 (data:font) | Google Noto 项目（经 fontTools instancer/subset 处理） | SIL Open Font License 1.1 | 允许嵌入与子集化；不得单独转售；保持许可声明（见 sources.json ASSET-FONT-NOTO-SC） |

## 5. Logo 与品牌系统（Brand）

| 资产 | 来源 | 状态 | 复用边界 |
|---|---|---|---|
| GLORY·JZ 名称与图形母题（带+里程碑+轨道符号） | 原创概念 | 内部工作代号；未完成商标检索 | 清查完成前不注册、不商业使用、不对外授权 |

## 6. 代码与生成内容（Code & Generated Content）

| 资产 | 来源 | 许可 | 备注 |
|---|---|---|---|
| 图件/PDF/HTML 生成脚本与确定性管道 | 本智能体会话内编写 | 原创（随仓库展示） | 记录于 changelog；生成方法披露符合任务书 charter.6 |
| report/proposal.html 与 visual/index.html（中英） | 由 render_proposal_html.py（仓库官方渲染器）与数据驱动脚本生成 | 原创 | 图文来自本包数据与正文 |

## 7. 引用素材（Cited materials）

| 素材 | 来源 | 复用边界 |
|---|---|---|
| 组织方公告/任务书/规范（DATA-SRC-*） | 官方公开或清权文件 | 见 sources.json 各条目 allowed_uses |
| 国际/国内案例页面 8 条（CASE-*） | 官方/第一方公开页面 | 仅机制对照引用，不复制页面素材；见 sources.json |
| 京张铁路史实与中关村叙事（SRC-*） | 官方公开页面 | 仅史实表述引用 |
| 现场踏勘记录与自绘草图 | 本项目自行采集 | 本包内使用 |

> 影像版权声明：本包全部图形为原创绘制或数据驱动制图，未使用任何第三方受版权保护的图像素材；如与既有标识雷同属巧合。案例页面信息仅作机制对照，页面图像不进入本包。