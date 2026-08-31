# 版权与生成说明

本投稿包的中文和英文正文、结构化 JSON/GeoJSON、数据驱动图件、离线 HTML、A3/A0 图纸与中性视觉标记由 Codex × AmyLili28 为本次开源征集生成。提交包按仓库的展示与共创许可语境提供；任何后续复用仍需保留来源、贡献者与状态边界。

`assets/media/second-encounter-cover-v1.png` 由 OpenAI ImageGen 于 2026-08-30 生成，提示词要求其作为编辑式建筑概念插画，表现同一公共 AI 服务空间的两次相遇。它不包含真实场地测绘、可识别人物、授权商标或官方标识，不得被解释为现状照片、公众意见、正式规划或已批准效果图。图中出现的纸面痕迹仅为不可读的概念性纹理，不承载事实信息。

十二张中文图件及十二张英文图件由同一 GeoJSON、指标与方案结构通过 Pillow 确定性绘制。`assets/identity/second-encounter-mark.svg` 为无文字的原创中性符号，由两条轨迹、回返弧线和橙色修复节点构成。Pillow 中文图件使用当前 macOS 系统提供的 STHeiti，英文区域协同图与人物回访图使用系统 Arial；均仅输出栅格结果，不分发该系统字体。PDF 由 ReportLab 生成；中文使用当前系统 `/System/Library/Fonts/Supplemental/Arial Unicode.ttf` 并嵌入子集，英文使用 PDF 标准 Helvetica；未把系统字体文件放入投稿包，也不对其外部再分发权作授权声明。

离线 HTML 使用随包提供的 `visual/assets/JingZhangCJK.css`。该 CSS 以 data URI 内嵌 Noto Sans SC 字符子集，并在文件头完整保留 SIL Open Font License 1.1 文本；不依赖远程字体服务。子集只为保证本投稿中现有中英文字符在离线 Linux／macOS／Windows 环境可读，不改变字体名称来暗示官方授权，也不用于商标或政府标识。

外部事实与案例仅通过 `sources.json` 中登记的公开链接引用；未复制外部网页图片、地图瓦片、字体、商标或同行方案资产。同行方案仅用于差异化比较，并已在来源表中注明。所有空间落地建议均为概念建议、参考方案或可供专业团队深化研究，不替代正式规划，不构成政府审定结论。
