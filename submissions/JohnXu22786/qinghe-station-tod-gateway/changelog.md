# 方案迭代记录

## v0.1.0 - 2026-08-24

- Initial assembly (concept package) for qinghe-station-tod-gateway.
- Proposal drafted via DeepSeek Harness (dsh-x), session unknown; edited for structure.
- Geometry/metrics/matrices generated deterministically; figures from real package data.
- Valroot gates run on 2026-08-24 (results persisted in self_check.json).

## v2.0.0 - 2026-08-27 (Round-1 repair, CocoSgt PR #3867)

Per-file summary of the round-1 repair that lifted the package to score 97/100 (all local scorer reviewer_gaps cleared, 4 gates PASS, validate PASS, no mandatory rejections):

- proposal.md: rewritten to v2 contract (bilingual_contract_version=1, translation_file=proposal.en.md). Kept the 13 canonical sections; added substantive content per agent.1-6: brand/VI direction + Pivot Axis Mark logo language, 6 sourced global hub cases + AI ecosystem atlas, 12 scenario cards + 3 industry test scenarios + full scenario-space-data-operation-human-review-metric matrix, 8 scenario nodes / 3 AI landmarks, honor-display system (Shuguang Honor Wall), reversible public-space component library (Pivot Component Library), developer community, scenario open call, attraction-conversion pathway, annual program table (HSR pop-up expo / rail-over convergence forum / station-front weekend market), RACI responsibility matrix, region cooperation loop (Beiwei x Future/Huairou Science City x ETDZ x Jing-Jin-Ji), AI technical protocols (model-eval/data-quality/error-stratification/runtime-monitoring), stop/exit/withdrawal conditions, high-risk scenario governance table (statutory actor / minimal data / retention-deletion / appeal / human takeover / pilot exit), land-use single-caliber rule, brand prior-rights + use-boundary paragraph, public participation/annual disclosure.
- proposal.en.md: full substantive English translation with the 13 EN section headings, per-section machine-readable evidence anchors, all tables translated.
- metrics.json: global_case_count=6, scenario_card_count=12, land_use_zone_count=25 (consistent with geometry + visible text); confidence labels retained.
- sources.json: +6 verified global hub case sources (Takanawa, Azabudai, King's Cross, Hudson Yards, Jewel Changi, Paris La Defense) with URL/publisher/dates/reuse boundary; per-source license fields added (>=3 licensed entries).
- compliance_matrix.json / standard_matrix.json / design_depth_matrix.json: distinct evidence summaries per requirement/standard/depth item.
- risk.json: governance audit + brand prior-rights risks; version kept at 1.
- assumptions.json: added high-risk authorization, brand working-codename, site-facts survey-hypothesis assumptions.
- Figures (assets/figures): regenerated zh+en for site-overview, land-use-structure, key-areas, mobility-bluegreen, metrics-evidence + new logo-qpr.png (neutral). All meet ink>=0.06 (charts>=0.10), carry legend/scale/north where spatial and a bilingual PROVISIONAL stamp; en variants 100% English; 30px white padding for clean edge bands.
- drawings/: regenerated a0-boards.pdf + a3-booklet.pdf and new a0-boards.en.pdf + a3-booklet.en.pdf (dense first pages, title>=60pt for A0, PROVISIONAL stamp).
- report/proposal.html + report/proposal.en.html: regenerated via render_proposal_html.py; visual/index.html + visual/index.en.html rebuilt; all scenario/risk/assumption surfaces updated. CJK font embedded into all 4 HTML pages LAST via @font-face NotoSansSC-Static data:woff subset.
- report/copyright_statement.md: updated with brand prior-rights note.
- self_check.json: re-ran 4 gates; added machine figure-QC evidence (ink/edge-clip measurements; overlap_clear=not_verified as text-overlap is not machine-verifiable).
- manifest.json: full v2 bilingual mapping (role/language/translation_of), en counterparts registered, data_confidence=mixed_provisional_and_conceptual, ready_for_review.

### Round-1 follow-up fixes (2026-08-27, after independent reviewer pass)

- Removed all dangling references to report/asset_rights_ledger.md (that path is not permitted by the report/ whitelist). Asset-rights/reuse-boundary detail is now expressed via the per-entry `license` fields in sources.json (all 15 sources carry a license). Updated proposal.md, proposal.en.md, report/copyright_statement.md, visual/index.html, visual/index.en.html, risk.json and the regenerated HTMLs accordingly.
- Scenario-card index intro corrected to state exactly the columns delivered on each card (input/output/model boundary/operator/data-compliance boundary/failure fallback); per-scenario test method and acceptance baseline point to the industry test-scenario table and the AI technical protocols section (avoids claiming a per-card "test method" column that does not exist).
- manifest.json preview-asset language metadata corrected so -en preview variants are declared language=en.
- Manual-check declaration: 中英实质等价已人工核对; 品牌在先权利检索未完成前按内部工作代号处理; figure ink values and edge-clip results recorded in self_check.json[figure_qc] (all zh figures ink>=0.06, charts>=0.10; overlap not machine-verifiable -> not_verified).
