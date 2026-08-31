# Copyright Statement（版权与资产权利声明）

本包（jingzhang-culture-signage，round-1 修复版）全部提交内容的权利状态如下，逐项与 sources.json 资产条目、manifest.json 角色注释保持一致：

1. **文字与版面（本包原创）**：proposal.md、proposal.en.md、各矩阵、指标体系与本文档均由申报智能体（JohnXu22786 / dsh-haidian-agent）原创或改写，仅用于社区展示与评审，遵循 COMMUNITY-DISPLAY-ONLY 许可。
2. **图件、图纸与Logo原型（本包原创生成）**：assets/figures/*.png、drawings/*.pdf 由程序化方式生成，图形语汇（道钉—钢轨—站牌）为本包原创概念；不做任何机构标志的叠加使用。中文主品牌为章痕·京张叙事导视带，英文主品牌为 ZHANGHEN · JINGZHANG NARRATIVE WAYFINDING BELT；WAYMARK·JZ 仅为内部工作代号。概念阶段未完成商标检索与法律审查，品牌与图形仅用于本包评审展示，不对外注册、不商业使用、不作政府背书表示，正式使用前完成检索与在先权利核验。
3. **字体（许可明确）**：全部 HTML 与图件使用 Noto Sans SC（SIL Open Font License 1.1）静态子集版本，允许子集化与 base64 内嵌；来源与许可见 sources.json 条目 ASSET-FONT-NOTOSANSS。
4. **第三方素材（未使用未清权素材）**：本包未使用任何未经授权的老照片、口述史录音、旧时刻表、地图瓦片或第三方图标。拟用于实际展示的历史素材在逐项史实核验、授权、知情同意与撤回记录到位前，一律以明确占位或公共领域替代物处理（见 ASSET-HISTORY-PLACEHOLDER）。
5. **引用与案例**：组织方公告、任务书、专业规范与六个全球案例（高线公园、自由之路、柏林墙之路、新加坡铁道走廊、清溪川、首钢园）均登记来源机构页面、发布/获取时间与复用边界；案例仅作方法借鉴，不推断其运营数据可复用于本项目。
6. **隐私与监控边界**：方案不采集身份可识别信息，不进行个体识别式追踪，禁止过度监控；人流密度感知仅处理匿名聚合数据并明示保留周期与访问权限。
7. **概念边界**：本包为概念建议与参考方案，不替代法定规划，不含容积率、建筑高度、拆改留、投资预算、客流容量或工程可行性结论；全部面积与比例为 provisional 低置信度取整值，官方数据发布后整体复算并刷新图件与指标。

中英双语版本（proposal.md / proposal.en.md、图件与 PDF）已逐条人工核对实质等价；任何歧义以中文版为准并在修订时同步。

## Asset rights ledger / 资产权利台账

Status: package-review record, provisional and non-official. This ledger records the intended reuse boundary for every shipped visual asset; it is not a trademark clearance, copyright opinion, permit, or licence grant.

### 1. Package-created visual assets

| Asset set | Files covered | Origin and rights basis | Allowed use in this package | Restriction / action before public implementation |
|---|---|---|---|---|
| Core diagrams | `assets/figures/key-areas*.png`, `mobility-bluegreen*.png`, `land-use-structure*.png`, `metrics-evidence*.png`, `pilot-matrix*.png` | Programmatically drawn from package geometry and authored labels; no external image, map tile, logo or photograph is embedded. | Review, comparison and concept communication inside this submission; bilingual counterparts are translation-equivalent. | Re-run after official GIS, access, heritage and land-use data are supplied; do not present provisional geometry as an official map. |
| Site and system diagrams | `assets/figures/site-overview*.png`, `positioning-functions-zones*.png`, `ai-ecosystem-map*.png`, `persona-ai-map*.png` | Package-authored schematic diagrams; labels and relationships are design propositions, not copied artwork. | Concept review and internal stakeholder discussion. | Professional and stakeholder verification is required before public wayfinding, procurement or operational claims. |
| Node cards and identity | `assets/figures/node-*.png`, `assets/figures/logo-jz*.png` | Package-authored vector-like raster compositions using generic railway motifs (spike, rail, station board) and text; no third-party mark is reproduced. | Package review and design exploration only. | Trademark search, identity review, accessibility review and institutional approval are required before external branding or fabrication. |
| Drawings | `drawings/a0-boards*.pdf`, `drawings/a3-booklet*.pdf` | Rendered from the package-authored diagrams and proposal text; no third-party photograph or page image is included. | Review circulation and print proofing for this submission. | Reissue after official geometry and professional sign/heritage/safety review; do not treat as construction documents. |
| HTML and visual index | `report/proposal*.html`, `visual/index*.html` | Package-authored text and diagrams. The embedded font is a license-cleared open-source font asset retained by the existing package build; it is used only for rendering text. | Offline review of the submitted package. | Keep the embedded font notice and verify the final font licence and language coverage before a public deployment. |

### 2. Text, data and source boundaries

| Material | Record | Rights / provenance status | Use boundary |
|---|---|---|---|
| Official announcements and standards | Source IDs beginning `DATA-SRC-` in `sources.json` | Attributed local snapshots or official public pages; the source record is the provenance, not a blanket reuse licence for page chrome, images or third-party editorial material. | Quote only the stated task, policy or terminology; do not copy page imagery or infer approval, redlines or project-specific legal conclusions. |
| Provisional geometry | `geometry/*.geojson` and package-derived maps | Repository-maintained design/provisional data, with confidence and limitations recorded in the source/metric text. | Schematic analysis, ratio checking and package review only; replace and recompute when official GIS/CAD is supplied. |
| Historical photographs, archives and sound | None embedded in this package | Not cleared for reuse. | Placeholders or public-domain substitutes only until item-level permission, attribution and withdrawal terms are recorded. |
| Oral-history and participant data | None embedded; future collection is proposed only | Consent, withdrawal and retention terms are not yet executed. | No collection or public release under this package without an approved protocol and human review. |
| Brand names and logo concept | Chinese primary: `章痕·京张叙事导视带`; English primary: `ZHANGHEN · JINGZHANG NARRATIVE WAYFINDING BELT`; `WAYMARK·JZ` is internal codename only | Trademark and prior-rights search is incomplete. | Review display only; no registration, commercial use, institutional endorsement or public rollout before clearance. |

### 3. Release controls

1. The package owner must keep `sources.json`, this ledger and the manifest synchronized when an asset is replaced, translated or newly licensed.
2. A future public release must record the asset-level source, creator, licence/permission, attribution, expiry or withdrawal condition, and reviewer in this ledger before publication.
3. The Chinese and English assets are paired by filename and `translation_of` metadata where applicable. A translation change requires visual QA for clipping, missing glyphs and item-by-item substantive equivalence.
4. All visual and data claims remain participant-proposed, provisional and non-official where marked in the proposal; this ledger does not upgrade any source, geometry, metric or brand claim.
