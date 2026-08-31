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
| Noto Sans SC（HTML 中文渲染，Regular/Bold 静态子集） | Google Noto Fonts（github.com/google/fonts，OFL 目录） | 按页面实际用字（1031 字符）经 fontTools instancer + pyftsubset 子集化为 woff2，以 base64 data URI 内联进 4 个 HTML 页面（不依赖宿主机中文字体，file:// 与 http 离线均可读） | SIL Open Font License 1.1 授权，允许捆绑与再分发；版权声明与许可证全文见本文件附录 A |
| Hiragino Sans GB（图件中文渲染） | macOS 系统字体 | 本机 matplotlib 渲染进 PNG 位图 | 位图像素化输出，不随包分发字体文件 |
| STHeiti Light / Medium（PDF 排版） | macOS 系统字体 | reportlab 以子集形式嵌入 PDF | 仅文档内嵌子集用于阅读显示；不随包再分发字体二进制 |
| Helvetica（PDF 西文） | reportlab 内置核心字体 | 西文段落 | 随 PDF 规范自由使用 |

说明：系统字体在本机用于文档渲染与 PDF 内嵌子集属于常规文档使用场景；Noto Sans SC 为 OFL 开源授权字体，其 woff2 子集内嵌于本包 HTML 页面随包分发，符合许可证第 1、2 条（捆绑分发须附版权声明与许可证全文，见附录 A）；系统字体未用于商标注册或 Logo 矢量定稿（Logo 为程序化演示绘制，VI 定稿可由专业团队以开源授权字体重制）。

## 4. 构建工具链

Python 3.9（shapely 2.0.7 / pyproj 3.6.1 / matplotlib 3.9.4 / Pillow 11.3.0 / reportlab / pymupdf 仅用于本地质检渲染）。全部构建脚本随本包工作过程保留于提交历史；HTML 无任何远程资源、CDN、跟踪或表单。

## 5. 未使用与禁止事项

- 未使用任何企业 Logo、商标、人物肖像、论文图像或受版权保护的图片素材。
- 未使用非公开政府数据、企业内部数据或个人隐私数据。
- 不声称官方批准、审定控规、最终权属或实施承诺。

## 附录 A：Noto Sans SC 字体版权声明与许可证全文（SIL Open Font License 1.1）

本包 HTML 页面内嵌的 Noto Sans SC Regular/Bold 静态子集（woff2）基于 Google Noto Fonts 项目文件（https://github.com/google/fonts/tree/main/ofl/notosanssc ）子集化生成，依 SIL Open Font License 1.1 随包分发。许可证全文如下（未经修改）：

```
Copyright 2014-2021 Adobe (http://www.adobe.com/), with Reserved Font Name 'Source'

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is copied below, and is also available with a FAQ at:
https://scripts.sil.org/OFL


-----------------------------------------------------------
SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
-----------------------------------------------------------

PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide
development of collaborative font projects, to support the font creation
efforts of academic and linguistic communities, and to provide a free and
open framework in which fonts may be shared and improved in partnership
with others.

The OFL allows the licensed fonts to be used, studied, modified and
redistributed freely as long as they are not sold by themselves. The
fonts, including any derivative works, can be bundled, embedded, 
redistributed and/or sold with any software provided that any reserved
names are not used by derivative works. The fonts and derivatives,
however, cannot be released under any other type of license. The
requirement for fonts to remain under this license does not apply
to any document created using the fonts or their derivatives.

DEFINITIONS
"Font Software" refers to the set of files released by the Copyright
Holder(s) under this license and clearly marked as such. This may
include source files, build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the
copyright statement(s).

"Original Version" refers to the collection of Font Software components as
distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to, deleting,
or substituting -- in part or in whole -- any of the components of the
Original Version, by changing formats or by porting the Font Software to a
new environment.

"Author" refers to any designer, engineer, programmer, technical
writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS
Permission is hereby granted, free of charge, to any person obtaining
a copy of the Font Software, to use, study, copy, merge, embed, modify,
redistribute, and sell modified and unmodified copies of the Font
Software, subject to the following conditions:

1) Neither the Font Software nor any of its individual components,
in Original or Modified Versions, may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled,
redistributed and/or sold with any software, provided that each copy
contains the above copyright notice and this license. These can be
included either as stand-alone text files, human-readable headers or
in the appropriate machine-readable metadata fields within text or
binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font
Name(s) unless explicit written permission is granted by the corresponding
Copyright Holder. This restriction only applies to the primary font name as
presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
Software shall not be used to promote, endorse or advertise any
Modified Version, except to acknowledge the contribution(s) of the
Copyright Holder(s) and the Author(s) or with their explicit written
permission.

5) The Font Software, modified or unmodified, in part or in whole,
must be distributed entirely under this license, and must not be
distributed under any other license. The requirement for fonts to
remain under this license does not apply to any document created
using the Font Software.

TERMINATION
This license becomes null and void if any of the above conditions are
not met.

DISCLAIMER
THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
OTHER DEALINGS IN THE FONT SOFTWARE.
```
