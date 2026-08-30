# 方案迭代记录

## v0.1.0 - 2026-08-24

- Initial assembly (concept package) for shared-study-space.
- Proposal drafted via OpenCode CLI (opencode), session ses_fccf668c5ffe6hPp4wXGoiL8SK; edited for structure.
- Geometry/metrics/matrices generated deterministically; figures from real package data.
- Valroot gates run on 2026-08-24 (results persisted in self_check.json).

## round-3 repair - 2026-08-27

Per-file summary of the repair round addressing CocoSgt 2026-08-24 CHANGES_REQUESTED (52.0/100):

- proposal.md: rewritten to close every listed gap — six persona rows matching persona_count=6; six sourced case rows matching global_case_count=6; ten scenario cards (SC-01..SC-10); three industry test protocols (IT-01..IT-03) with hypothesis/maturity/IO/space/precision threshold/risk-isolation/exit; annual program table (3 brands) matching annual_program_count=3; named original mechanisms in 「」 (自习舱分时预约/学习空间使用公约/学习积分/联席议事/学习社群备案与导师结对/年度学习活动公示); brand/VI section pointing to logo-brand.png; agent.2 seven-factor ecosystem atlas; agent.4 honor-display system + component library + three AI landmark directory; agent.5 history/wayfinding + international communication; agent.6 developer community + scenario open operation + talent/enterprise pathways; AI technical protocols (模型评测/数据质量/误差分群/运行监测); official three-tier scope hierarchy (43.6/11.4 sq km/368.4 ha) with this package's sub-scope located under them; precision cleaned (provisional values as 约 numbers, ratios vs counts separated); trademarks treated as internal working codenames; multilingual front matter with bilingual_contract_version 1 + translation_file.
- proposal.en.md: full English translation (all 13 EN sections), front matter language=en + translation_of=proposal.md.
- metrics.json: persona_count=6, global_case_count=6, added scenario_card_count=10; all counts backed by visible text; area metrics confidence stays low/medium.
- assets/figures: regenerated zh + en site-overview/land-use-structure/key-areas/mobility-bluegreen/metrics-evidence/ai-ecosystem-atlas + neutral brand-logo; all at 150 dpi with title>=18pt, labels>=13pt, provisional stamp (both languages), scale bar + north arrow on spatial sheets, single land-use caliber; per-figure ink/clip measured (ink 0.06–0.36, edge-clip <0.02).
- drawings: regenerated a0-boards / a3-booklet (zh) and added en counterparts embedding the regenerated figures.
- report/proposal.html + report/proposal.en.html: re-rendered from the new zh/en markdown, CJK font subset embedded (Noto Sans SC OFL-1.1).
- visual/index.html + visual/index.en.html: regenerated (zh 14 visual-review markers; en 100% English) embedding regenerated figures + data-metric declarations; fonts embedded.
- sources.json: added per-case traceable entries (6 cases), asset-ledger licensed entries (font/logo/figures/code), trademark prior-rights statement.
- assumptions.json: A-IP-001 updated to internal-working-codename wording.
- compliance_matrix.json / standard_matrix.json: refreshed agent.1-6 and standard evidence summaries to reference the new shipped content; standard_matrix evidence summaries now distinct.
- manifest.json: registered all zh/en counterparts with language + translation_of per 0.2 schema; data_confidence=medium.
- self_check.json: four gates re-run; figure_qc refreshed with real ink/edge-clip measurements.

## round-4 repair - 2026-08-30

Per-file summary of the repair round addressing CocoSgt 72.0 review for PR #3979:

- drawings/a0-boards.pdf + drawings/a0-boards.en.pdf: Complete layout overhaul. Redesigned to 4 dense, full-bleed A0 landscape sheets (46.81 x 33.11 in / 1189 x 841 mm) filling the entire canvas with zero microscopic clustering and zero empty whitespace. Prominently structured hero maps, 3 key node sub-boards, 10 scenario cards, 3 industry test protocols, seven-factor innovation ecosystem diagrams, RACI matrices, and dual-axis metric summaries. Title (>=32pt), labels (>=18pt), text (>=14pt), and PROVISIONAL stamp banners placed with perfect readability.
- drawings/a3-booklet.pdf + drawings/a3-booklet.en.pdf: Complete redesign of cover page with clean hierarchical typography eliminating all title/subtitle overlap. Set generous margins and crisp layout across all 8 landscape pages embedding all canonical bilingual figures with zero edge clipping.
- assets/figures: Regenerated all 7 canonical figure pairs (14 PNGs in zh + en): site-overview, key-areas, mobility-bluegreen, land-use-structure, metrics-evidence, ai-ecosystem-atlas, and logo-brand. All figures updated with unified Two Wings ("中关村科技服务翼 / Zhongguancun Technology Service Wing" & "小月河场景赋能翼 / Xiaoyuehe Scenario Empowerment Wing") and Three Nodes ("织学馆 / STU-HALL #0E7C82", "学研谷 / STU-VALLEY #C47B1A", "夜读室 / STU-NIGHT #2E5E96") naming. Dual-axis metrics scale separation implemented; residual characters cleaned. Ink coverage measured between 0.101 and 0.616 (all >= 0.08) and edge-clip ratio 0.0000 across all 14 figures.
- report/proposal.html + report/proposal.en.html + visual/index.html + visual/index.en.html: Fonts embedded with embed_fonts.py (Noto Sans SC OFL-1.1 subset). Previews refreshed in visual/assets/previews/.
- self_check.json + manifest.json: Four gates self-check re-run and passed deterministically. All file hashes and figure_qc verified.
