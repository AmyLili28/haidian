# 方案迭代记录

## v0.1.0 - 2026-08-24

- Initial assembly (concept package) for circular-zero-waste-belt.
- Proposal drafted via OpenCode CLI (opencode), session ses_fcd5fed4affe6TLFqHpZd8xJKD; edited for structure.
- Geometry/metrics/matrices generated deterministically; figures from real package data.
- Valroot gates run on 2026-08-24 (results persisted in self_check.json).

## v2.0 - 2026-08-26

Round-2 repair per CocoSgt review (55.0 CHANGES_REQUESTED @ 2026-08-24). Per-file summary:

- **proposal.md**: v2 bilingual contract activated (bilingual_contract_version 1, translation_file proposal.en.md); official three-tier scope hierarchy stated (43.6 km² / 11.4 km² / 368.4 ha) with package sub-scope located; five regional synergy interfaces (北纬社区/未来科学城/怀柔科学城/经开区/京津冀); six global cases with per-item sources; AI ecosystem atlas + industry–space mapping + eight-mechanism table; six personas, 12 scenario cards, 3 industry test scenarios (protocol/threshold/decommissioning), AI technical protocols (模型评测/数据质量/误差分群/运行监测); key-population service journeys; three AI landmark catalogues, honor display, 8-family component library, wayfinding system; brand/VI section with logo + international-communication copy; RACI implementation matrix (roles, thresholds, gates, maintenance, decommission, annual review); 4 annual programs; developer community, scenario opening flow, conversion paths; land-use single caliber with 复算/口径/聚合 statements and “不代表现状或法定规划” callout; cost tiers; trademark prior-rights statement; precision cleaned (no 7+ digit runs, no 4-decimal values).
- **proposal.en.md**: full substantive translation with front matter (language en, translation_of proposal.md); 13 required EN sections; zero Chinese characters.
- **metrics.json**: persona_count 6, global_case_count 6, annual_program_count 4, ai_scenario_card_count 12; six land-use ratio metrics (single caliber) with formulas/confidence/recompute triggers; spatial metrics unchanged.
- **sources.json**: six case sources (CASE-SZ-2019, CASE-SH-2019, CASE-JP-2000, CASE-DK-2019, CASE-SG-2019, CASE-EU-2020 — publisher/URL/dates/license each) + four asset sources (font OFL 1.1, logo/figures, PDF/HTML, geometry/tooling) with licenses.
- **report/copyright_statement.md**: full asset rights ledger (author, generation method, license, attribution, restrictions, mapping) + trademark prior-rights section.
- **compliance_matrix.json / standard_matrix.json**: evidence summaries updated to point at the new distinct content (12 cards, 6 cases, 4 programs, 6 personas, 8 mechanisms).
- **assets/figures/**: all 5 canonical figures regenerated (zh+en) with basemap/legend/scale/north/flow lines/concept cards; new ai-ecosystem-map (+en) and logo (+en); every figure carries the bilingual PROVISIONAL stamp; figsize 12–16.8 in @150 dpi, titles ≥18 pt, labels/legends ≥13 pt; text-bbox overlap/clip verified zero at generation time (renderer window-extent checks); ink measured 0.11–0.77, edge-clip 0.0 (see self_check.json figure_qc).
- **drawings/**: a0-boards.pdf & a3-booklet.pdf regenerated (A0 title ≥60 pt, A3 cover title not clipped, page-layout overflow verified 0) + new en counterparts a0-boards.en.pdf, a3-booklet.en.pdf.
- **report/proposal.html / report/proposal.en.html**: rendered from the md pair via render_proposal_html.py; Noto Sans SC subsets embedded (SIL OFL 1.1) via fontTools; check_font_coverage: 0 missing CJK; en page contains no Chinese.
- **visual/index.html / visual/index.en.html**: new single-caliber content (12 cards, 6 cases, 6 personas, 8 mechanisms, land-use classes per geometry); data-metric attributes match metrics.json; en page 100% English; CJK fonts embedded.
- **manifest.json**: all en counterparts registered (language=en + translation_of); validation_claim.data_confidence = mixed_provisional_and_conceptual (provisional model data, never ‘high’).
- **self_check.json**: four gates re-run and persisted (formal-review-ready); figure_qc added with real ink/edge-clip measurements and generation-time text-bbox verification (overlap_clear=true).

Verification: score_rubric 100.0/100, mandatory_rejections [], reviewer_gaps []; deterministic/spatial/visual/professional gates all PASS; check_font_coverage ALL_FONTS_OK.