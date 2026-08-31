# 京张关系带 · 成果导读 / Jing-Zhang Relation Belt - reading guide

本文件是本投稿包的**导读**，不是主体方案文本。主体方案文本是 `proposal.md`（中文主稿）与
`proposal.en.md`（英文译稿）；权威数据是 `geometry/*.geojson`、`metrics.json`、`sources.json`、
`assumptions.json` 与三个矩阵。本文件只回答一个问题：**这一包东西应该从哪儿开始看、各部分之间是
什么关系。**

This file is a reading guide, not the proposal itself. The proposal is `proposal.md` with its
English counterpart `proposal.en.md`; the authoritative data is the GeoJSON layers, `metrics.json`,
`sources.json`, `assumptions.json` and the three matrices. This file only answers one question:
where to start, and how the parts relate.

## 一句话主张 / The claim in one sentence

京张沿线不缺资源、不缺绿地、不缺设施，缺的是这些系统与京张之间的关系；本方案把设计对象从
「再造一个园区」改为「提高既有创新资源之间的交换条件」。

The corridor does not lack assets, green space or facilities. What it lacks is the relation between
those systems and the Jing-Zhang corridor itself; this proposal changes the object of design from
building another park to raising the exchange conditions between assets that already exist.

## 建议的阅读顺序 / Suggested reading order

1. `visual/index.html`（中文）或 `visual/index.en.html`（英文）——离线展示页，十四个模块一次看完
   总览、三层范围、重点区域、用地、交通慢行、蓝绿公共空间、建筑、更新项目、AI 场景、核心指标、
   任务覆盖、自检状态、来源与假设。
2. `assets/figures/` 五张核心派生图——全部由本包 GeoJSON 与 `metrics.json` 程序派生，每张有明确
   主叙事、图例、来源注、临时边界说明与一句设计判断。
3. `proposal.md`——主体论证，十三个必选章节，每个判断带机器可读证据引用。
4. `drawings/a3-booklet.pdf`（25 页）与 `drawings/a0-boards.pdf`（7 张 A0）——展示成果；英文版为
   `a3-booklet.en.pdf`（42 页，每张主线图页配英文对照页）与 `a0-boards.en.pdf`。
5. `compliance_matrix.json` / `standard_matrix.json` / `design_depth_matrix.json`——任务覆盖、
   专业标准与成果深度的机器可读证据链。
6. `self_check.json`——四门本地 gate 的可回读运行记录。

## 必须一并读到的三条边界 / Three limits that must be read with everything else

1. **边界是临时的。** 本包全部范围线来自组织方提供的临时粗略边界（`official_boundary=false`、
   `geometry_role=provisional_constraint`、`boundary_precision=provisional_rough`），不是官方红线；
   全部面积与比例是低置信度设计模型值，官方几何发布后整体复算。
2. **深度是不均的。** 三处官方重点区域中，只有大钟寺（T1）完成对象级空间深化，另两处为概念级
   空间控制建议。这一差异如实声明，不作平均包装。
3. **落地建议全部是概念建议。** 本方案不给出控规调整、容积率、建筑高度、具体地块拆改留、工程线位、
   市政管线、投资测算、开发时序或审批判断，也不声称任何政府承诺、企业入驻、已批准活动、已落实投资
   或已确定运营单位。
