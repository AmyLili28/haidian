# 版权、来源与权利台账（Copyright & Rights Ledger）

登记日期：2026-08-29。本包许可：`COMMUNITY-DISPLAY-ONLY`（manifest.json）。本文件为评审所需的逐资产版权与来源证明索引；来源与许可的机器可读登记见 `sources.json`。

## 1. 数据与基础资料

| 资产 | 作者/权利人 | 获取方式 | 使用边界 |
| --- | --- | --- | --- |
| 资格预审公告、智能体任务书、三区两翼/海淀1+X+1 背景 | 征集组织方/用户提供（清权） | 仓库 `brief/`、`data/` | 按来源登记用途使用；本方案不为其添加任何官方背书 |
| `brief/site-package/geometry/provisional_boundaries.geojson` | 组织方发布的临时粗略边界 | 仓库公开文件 | 仅用于生成、展示与自检（provisional_only） |
| 全球案例（斯坦福研究园、剑桥科技园、Station F、one-north、22@、Quayside） | 各机构官网公开页面 | 公开网页，仅引用事实性机制描述 | 不复制受版权保护的文本与图像；逐项一手来源见 sources.json |

## 2. 本方案原创资产（agent 生成）

| 资产 | 生成方式（模型/工具） | 权利与再分发 |
| --- | --- | --- |
| 命名系统「京张智脉/Jing-Zhang AI Vein」、节点级命名、双语传播文案 | ZCode GLM Plus 原创生成 | 本包许可下可再分发；不含任何已注册商标 |
| Logo「脉动之轨」、辅助图形、VI 色彩（#17493B / #2F3E8C / #C9A227） | matplotlib/reportlab 程序化绘制 | 原创图形，无第三方素材 |
| 全部 GeoJSON 设计图层（land_use/green_space/public_space/buildings/roads/phasing/constraints 增量部分） | shapely 2.0.7 + pyproj 3.6.1 在 EPSG:4548 下程序化生成 | 设计提案，非现状测绘；不含组织方数据 |
| 12 张图件（5 张必答 + brand-vi，中英双语） | matplotlib 3.9.4 渲染 | 本包许可下可再分发 |
| A3 文册（9 页）与 A0 展板（中英双语 PDF） | reportlab 排版，嵌入上述自制 PNG | 本包许可下可再分发 |
| 离线 HTML 总览与报告页 | 手写 HTML/CSS，无远程依赖 | 本包许可下可再分发 |

## 3. 字体权利（重点披露）

| 字体 | 来源 | 使用方式 | 嵌入与再分发 |
| --- | --- | --- | --- |
| Hiragino Sans GB（图件中文渲染） | macOS 系统字体 | 本机 matplotlib 渲染进 PNG 位图 | 位图像素化输出，不随包分发字体文件 |
| STHeiti Light / Medium（PDF 排版） | macOS 系统字体 | reportlab 以子集形式嵌入 PDF | 仅文档内嵌子集用于阅读显示；不随包再分发字体二进制 |
| Helvetica（PDF 西文） | reportlab 内置核心字体 | 西文段落 | 随 PDF 规范自由使用 |

说明：系统字体在本机用于文档渲染与 PDF 内嵌子集属于常规文档使用场景；本包未分发任何字体文件，也未将字体用于商标注册或 Logo 矢量定稿（Logo 为程序化演示绘制，VI 定稿可由专业团队以开源授权字体重制）。

## 4. 构建工具链

Python 3.9（shapely 2.0.7 / pyproj 3.6.1 / matplotlib 3.9.4 / Pillow 11.3.0 / reportlab / pymupdf 仅用于本地质检渲染）。全部构建脚本随本包工作过程保留于提交历史；HTML 无任何远程资源、CDN、跟踪或表单。

## 5. 未使用与禁止事项

- 未使用任何企业 Logo、商标、人物肖像、论文图像或受版权保护的图片素材。
- 未使用非公开政府数据、企业内部数据或个人隐私数据。
- 不声称官方批准、审定控规、最终权属或实施承诺。
