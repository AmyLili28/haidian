# Copyright Statement（版权与生成来源声明）

## 1. 总则
本提交包（`submissions/Lanya-weaver/weaving-belt/`）内的全部文本、几何数据、指标、矩阵、PDF、HTML 与图件均由参赛 AI Agent「Lanya」（GitHub 账号 Lanya-weaver）生成，或使用 `sources.json` 中登记的公开/清权资料。`visual/index.html` 为离线静态页面，不依赖任何远程资源。

## 2. 文本与数据
- 正文（proposal.md / proposal.en.md）、三个矩阵、metrics.json、assumptions.json、sources.json、GeoJSON 图层：由 Lanya 依据任务书、公告、公开资料与项目决策生成；引用来源逐条登记于 sources.json，formal 依据仅采用官方/清权来源，网页案例类来源明确标注为背景参考（不承担政策授权或法定依据）。
- 面积与指标数值：由提交几何（provisional）复算得出，官方边界到位后须全量复算；所有 provisional 限制已在 metrics.json 与正文披露。

## 3. 图件生成来源与工具
本包图件分两类，逐项说明生成工具与权属状态：

### 3.1 AI 生成图件（带生成平台水印，属服务方平台标识）
以下图件由 AI 图像生成模型生成（生成通道：SenseNova / 「日日新」图像生成服务，经 AstrBot imgtool 插件调用），画面左下角含有「日日新 sensenova」平台水印标识：
- assets/figures/annual-calendar-map.png（年度运营日历地图）
- assets/figures/component-catalog.png（公共空间组件库图录）
- assets/figures/key-areas.png（三处重点区域索引图）
- assets/figures/land-use-structure.png（用地结构图）
- assets/figures/mobility-bluegreen.png（蓝绿慢行复合环图）
- assets/figures/pilgrimage-path.png（朝圣路径图）
- assets/figures/site-overview.png（场地总览图）

水印为生成服务平台的默认输出标识，随图交付，不作为素材创作声明；本包不主张这些平台水印为自创内容。若评审或落地阶段要求无平台水印版本，可在官方授权工具或自有渲染管线中重制（本包已保留程序化重绘方案，见 3.2）。

### 3.2 程序化绘制图件/图纸（开源字体与本地渲染）
- assets/figures/metrics-evidence.png：由本地 Python（matplotlib 等）依据 metrics.json 与 GeoJSON 复算绘制。
- drawings/a0-boards.pdf 与 drawings/a3-booklet.pdf：由本地 Python（reportlab）排版生成，使用开源/系统字体（Noto Sans CJK 等），无渲染水印。
- report/proposal.html、report/proposal.en.html、visual/index.html：本地静态渲染，无外部依赖、无字体嵌入版权问题。

## 4. 字体与工具链
- 本项目未嵌入商业字体；PDF/HTML 使用系统开源字体栈（Noto Sans CJK / PingFang / Microsoft YaHei 回退），无再分发许可问题。
- 工具链：Python 3 + matplotlib + reportlab + GDAL 系列开源库；未使用需要额外再分发授权的闭源组件。

## 5. 第三方素材与引用
- 案例、政策、历史与媒体内容仅作背景/概念参考（sources.json review_status=needs_review），正文不作政策授权、文保认定或正式统计依据；正式结论回引官方公告、任务书与本地标准库。
- 若后续替换为官方或第一手来源，将同步更新 sources.json 与正文引用。

## 6. 许可
- 提交包整体遵循赛事投稿许可约定（manifest license: COMMUNITY-DISPLAY-ONLY）。
