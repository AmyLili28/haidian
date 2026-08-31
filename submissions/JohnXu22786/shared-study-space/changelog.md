# 方案迭代记录

## CocoSgt 5066574923 repair - 2026-08-31

- Human-facing provisional area and ratio displays were reduced to low-precision approximate values across both proposals, visual indexes, metric figures, HTML reports, and regenerated PDFs. The wording now identifies participant provisional model data, non-official issuance, and recomputation after official geometry/data release; machine precision remains confined to metrics.json/data-value attributes for reproducibility.
- The English proposal image links now point to the English figure counterparts so the English report and drawings cannot silently embed Chinese plates.
- The three key-area cards were re-laid out with explicit Exit, privacy, and human-fallback lines, bounded text wrapping, and a separate footer band; the bilingual key-area figures were regenerated and checked at output dimensions.
- A3 booklets and A0 boards were regenerated from the updated bilingual figures and low-precision display copy; local HTML, PDF, manifest, font, figure-QC, and four-gate checks are rerun after generation.

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
