# 方案迭代记录

## v0.2.0 - 2026-08-30 (CocoSgt Review Repairs)

- **Risk & Compliance Wording Alignment**: Renamed "无感安检" across the entire package (`proposal.md`, `proposal.en.md`, `compliance_matrix.json`, `design_depth_matrix.json`, `assumptions.json`, `risk.json`, `standard_matrix.json`, `report/*.html`, `visual/*.html`) to **"安检客流通行辅助与排队引导 / Security Flow Guidance & Queue Assistance"**. Explicitly clarified that statutory security screening is strictly conducted by human security personnel and statutory equipment, while AI provides passenger-flow diversion and queue time estimation based on anonymized aggregate data.
- **100% Full English Localization for All Figures**: Fully localized all district/node names, sub-panel descriptions, metric labels, confidence tags, axis titles, annotations, and legends into English (0 CJK characters) in `site-overview.en.png`, `land-use-structure.en.png`, `key-areas.en.png`, `mobility-bluegreen.en.png`, and `metrics-evidence.en.png`, maintaining substantive equivalence with Chinese versions.
- **Figure Readability & Drawing Overhauls**: Re-laid out and re-exported `drawings/a0-boards.pdf`, `drawings/a0-boards.en.pdf`, `drawings/a3-booklet.pdf`, and `drawings/a3-booklet.en.pdf` to eliminate all title-body, label-label, legend-warning, and axis-warning overlaps with zero right-edge clipping. All typography adheres to Title >= 18pt, labels/legends >= 13pt, annotations >= 11pt, with north arrows, scale bars, and prominent PROVISIONAL banners.
- **Font Embedding & Offline Previews**: Embedded WOFF CJK subset fonts in `report/proposal.html`, `visual/index.html`, `report/proposal.en.html`, and `visual/index.en.html`. Refreshed all 16 preview assets.
- **Self-Check & Manifest Update**: Verified against all four gates via `valroot/scripts/self_check_submission.py`, updated `self_check.json` and `manifest.json`.

## v0.1.0 - 2026-08-24

- Initial assembly (concept package) for qinghe-station-tod-gateway.
- Proposal drafted via DeepSeek Harness (dsh-x), session unknown; edited for structure.
- Geometry/metrics/matrices generated deterministically; figures from real package data.
- Valroot gates run on 2026-08-24 (results persisted in self_check.json).
