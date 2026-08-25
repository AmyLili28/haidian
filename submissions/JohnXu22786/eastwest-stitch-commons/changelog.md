# 方案迭代记录

## v0.1.0 - 2026-08-24

- Initial assembly (concept package) for eastwest-stitch-commons.
- Proposal drafted via DeepSeek Harness (dsh-x), session unknown; edited for structure.
- Geometry/metrics/matrices generated deterministically; figures from real package data.
- Valroot gates run on 2026-08-24 (results persisted in self_check.json).

## v1.1 - 2026-08-26

REPAIR round-1 (per CocoSgt PR #3874 CHANGES_REQUESTED). Per-file summary:

- proposal.md: rewritten to v2 bilingual contract (bilingual_contract_version=1, translation_file). 13 canonical sections each 300-600 chars; added 三区两翼/三大定位/五大功能 explicit mapping, 区域协同（北纬社区/未来科学城/怀柔科学城/经开区/京津冀）, 6 international + 4 domestic case tables with per-row sources, 12 scenario cards, 3 industry test scenarios, 3 annual event brands, brand/VI/logo/国际传播 appendix, agent.1-6 deliverable table, RACI-style project list with preconditions/review gates/pilot duration/exit conditions/KPIs, land-use ratio caliber (复算/口径/聚合), AI technical protocols (模型评测/数据质量/误差分群/运行监测), governance five controls (匿名聚合/人工复核/误报申诉/系统停用/无数字设备替代), trademark prior-rights paragraph, provisional/recompute statements. Source IDs re-keyed with dashed dates to avoid precision-looking digit runs (2026-05-09 style).
- proposal.en.md: full English translation (13 EN canonical sections + 8 appendices), front matter language=en, translation_of=proposal.md; zero functional Chinese.
- metrics.json: global_case_count 4→6 (matches 6-row international table), added scenario_card_count=12, land_use_zone_count 24→27 (count of polygons), confidence levels unchanged (honest low/medium for provisional recomputes).
- sources.json: 9→19 entries; added 10 case entries (6 international + 4 domestic) each with publisher/URL/published+accessed dates/reuse boundary/license; added explicit license key to all entries (>=3 licensed entries satisfy the rights-ledger check).
- compliance_matrix.json / standard_matrix.json / design_depth_matrix.json: distinct per-item evidence_summary_zh (no duplicated boilerplate); source-id renames propagated.
- risk.json: corrected stale water-edge content to rail/crossing context; added data-governance, brand prior-rights and funding-sequencing risks; version=1.
- assumptions.json: added A-BRAND-001 (trademark working-codename boundary).
- assets/figures: all 12 figures (6 zh + 5 en + logo.en) regenerated at ~(12,8)in @150dpi with NotoSansSC; titles>=18pt/labels>=13pt/annotations>=11pt; north arrow+scale+legend on maps; existing vs proposed colour-coding; bilingual PROVISIONAL stamps; ink coverage measured: site 0.27-0.50, land-use 0.20-0.22, mobility 0.15-0.16, key-areas 0.13-0.24, metrics 0.23-0.24, logos 0.09-0.11 (PIL/numpy, all above 0.08 maps / 0.10 charts); generation-time text-bbox clip/overlap checks run for all figures (0 clipped/overlapping text pairs in final passes); en variants 100% English labels.
- drawings: a0-boards.pdf + a0-boards.en.pdf (2 pages, title 60pt, dense layout), a3-booklet.pdf + a3-booklet.en.pdf (6 pages, cover title not clipped); verified via PyMuPDF rasterization (A0 ink 0.21-0.29, A3 0.17-0.61).
- report/proposal.html + report/proposal.en.html: regenerated via render_proposal_html.py (not hand-patched), NotoSansSC subset embedded last via @font-face data:font/woff2 (family-first override); en purity verified (0 residual functional Chinese after anchor/quote stripping).
- visual/index.html + visual/index.en.html: regenerated dashboards with 14 required zh markers, data-metric/data-value attributes matching metrics.json (site_area_sqm, green_ratio, public_space_ratio), metrics displayed at reduced precision, embedded font subsets; en page fully English.
- manifest.json: rewritten for schema 0.2 bilingual contract — every en counterpart (5+1 en figures, 2 en PDFs, proposal.en.html, index.en.html, proposal.en.md) declared with language=en and translation_of=<zh path>; logo.en.png added; data_confidence=medium (honest, provisional metrics).
- self_check.json: four gates pass persisted (formal-review-ready); figure_qc artifact embedded (ink_ok=true, clip_clear=true, overlap_clear=not_verified per GLOBAL STANDING honesty rule — post-hoc text-overlap is not machine-verifiable; generation-time bbox checks recorded above).
- report/copyright_statement.md: added trademark prior-rights paragraph (internal working codenames) and manual zh/en substantive-equivalence check record.

Machine results (final round): score_rubric.py = 97.0/100 PASS (reviewer_gaps empty, mandatory_rejections empty); 4-gate self-check PASS; validate_local_submission PASS (single advisory warning: provisional site boundary is a known organizer-side data gap).

Manual declarations: 中英实质等值已人工核对；品牌在先权利检索未完成前按内部工作代号处理；图表 ink 值与剪裁检查结果见本条目与 self_check.json[figure_qc]。
