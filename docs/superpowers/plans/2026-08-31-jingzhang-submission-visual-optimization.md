# Jing-Zhang Submission Visual Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the validated Jing-Zhang submission into a spatially credible, bilingual competition package with a real-base masterplan, three differentiated key-area prototypes, four AI-supported urban scenarios, and four non-repetitive A0 boards while preserving every approved planning boundary and validation contract.

**Architecture:** Keep the five canonical figure filenames required by the submission manifest, but replace their contents with a shared bilingual visual system generated from B0, the registered detailed corridor map, existing GeoJSON, and approved text. Generate the reports and PDFs from those canonical figures, then refresh the manifest and rerun the official four-gate self-check before syncing only the submission directory into the Git worktree. Local build helpers stay in the project workspace; the pull-request diff remains scoped to `submissions/mrcrow/jingzhang-symbiotic-ai-belt/`.

**Tech Stack:** Python 3, Pillow, ReportLab, GeoJSON, Markdown/HTML, `pdfinfo`, `pdftoppm`, ImageMagick, and the repository's deterministic/spatial/visual/professional validators.

---

## File map and responsibility boundaries

### Local build sources and helpers

- Modify: `/Users/michaelwu/海淀京张规划/scripts/build_formal_figures.py` — sole generator for the five Chinese and five English canonical PNG figures.
- Create: `/Users/michaelwu/海淀京张规划/scripts/test_build_formal_figures.py` — source-contract, bilingual-contract, dimension, density, and output-name tests.
- Modify: `/Users/michaelwu/海淀京张规划/scripts/build_formal_pdfs.py` — sole generator for bilingual A3 booklets and four-page A0 boards.
- Create: `/Users/michaelwu/海淀京张规划/scripts/test_build_formal_pdfs.py` — board-layout and page-count tests.
- Read only: `/Users/michaelwu/海淀京张规划/docs/maps/jingzhang-corridor/base-and-layers-v1/base-clean.png` — B0 planning base.
- Read only: `/Users/michaelwu/海淀京张规划/docs/maps/jingzhang-corridor/jingzhang-corridor-amap-registered-v3.png` — registered detailed context source.
- Read only: `/Users/michaelwu/海淀京张规划/docs/maps/jingzhang-corridor/existing-condition-v2/jingzhang-analysis-axis-v2.geojson` — approved Jing-Zhang analysis axis.

### Formal package source of truth

All paths below are relative to `/Users/michaelwu/海淀京张规划/haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/`.

- Modify: `assets/figures/site-overview[.en].png` — real-base masterplan and overall spatial framework.
- Modify: `assets/figures/land-use-structure[.en].png` — east-west stitch, north-south green mobility, renewal actions, and status legend.
- Modify: `assets/figures/key-areas[.en].png` — three differentiated key-area spatial prototypes.
- Modify: `assets/figures/mobility-bluegreen[.en].png` — four scenario families, T01–T03, and the shared AI operating loop.
- Modify: `assets/figures/metrics-evidence[.en].png` — phasing, governance gates, metrics, R1–R7, and evidence boundaries.
- Modify: `proposal.md`, `proposal.en.md` — approved narrative, figure captions, and bilingual wording.
- Regenerate: `report/proposal.html`, `report/proposal.en.html` — offline reports derived from Markdown.
- Modify: `visual/index.html`, `visual/index.en.html` — concise visual index aligned with the new five-figure system.
- Regenerate: `drawings/a3-booklet.pdf`, `drawings/a3-booklet.en.pdf` — six-page derived booklets.
- Regenerate: `drawings/a0-boards.pdf`, `drawings/a0-boards.en.pdf` — four non-repetitive boards.
- Refresh: `manifest.json`, `self_check.json` — hashes and persisted four-gate evidence.
- Do not change unless a validator proves it necessary: `geometry/*.geojson`, `metrics.json`, `sources.json`, `standard_matrix.json`, `design_depth_matrix.json`, `compliance_matrix.json`, and `assumptions.json`.

### Git delivery target

- Sync to: `/Users/michaelwu/海淀京张规划/haidian-submit-worktree/submissions/mrcrow/jingzhang-symbiotic-ai-belt/`.
- Branch: `submission/mrcrow-jingzhang-symbiotic-ai-belt`.
- Remote: `origin` = `https://github.com/mrcrow/haidian.git`.
- Existing PR: `https://github.com/open-city-ai/haidian/pull/4317`.

---

### Task 1: Lock the baseline and add failing figure-contract tests

**Files:**
- Create: `/Users/michaelwu/海淀京张规划/scripts/test_build_formal_figures.py`
- Read: `/Users/michaelwu/海淀京张规划/scripts/build_formal_figures.py`
- Read: the three source assets listed in the file map

- [ ] **Step 1: Confirm the current package is the validated baseline**

Run:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-formal-workspace
python3 - <<'PY'
import json
from pathlib import Path
p = Path('submissions/mrcrow/jingzhang-symbiotic-ai-belt')
m = json.loads((p / 'manifest.json').read_text(encoding='utf-8'))
s = json.loads((p / 'self_check.json').read_text(encoding='utf-8'))
assert m['package_state'] == 'ready_for_review'
assert m['validation_claim']['self_checked'] is True
assert s['ok'] is True
assert s['can_enter_formal_review'] is True
print('baseline-ready')
PY
```

Expected: `baseline-ready`.

- [ ] **Step 2: Write the failing figure-contract test**

Create the following test file:

```python
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageStat


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/build_formal_figures.py"
spec = importlib.util.spec_from_file_location("build_formal_figures", MODULE_PATH)
assert spec and spec.loader
figures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(figures)


class FormalFigureContractTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        sources = figures.source_contract()
        self.assertEqual(set(sources), {"base_clean", "amap_detail", "axis"})
        for path in sources.values():
            self.assertTrue(Path(path).is_file(), path)

    def test_bilingual_contract(self) -> None:
        self.assertEqual(figures.content_contract(figures.ZH), figures.content_contract(figures.EN))

    def test_render_all_contract(self) -> None:
        expected = {
            "site-overview.png", "site-overview.en.png",
            "land-use-structure.png", "land-use-structure.en.png",
            "key-areas.png", "key-areas.en.png",
            "mobility-bluegreen.png", "mobility-bluegreen.en.png",
            "metrics-evidence.png", "metrics-evidence.en.png",
        }
        with tempfile.TemporaryDirectory() as tmp:
            written = figures.render_all(Path(tmp))
            self.assertEqual({p.name for p in written}, expected)
            for path in written:
                with Image.open(path) as image:
                    self.assertEqual(image.size, (2400, 1500))
                    self.assertGreater(sum(ImageStat.Stat(image.convert("L")).var), 250)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the test and verify it fails for the missing contract API**

Run:

```bash
cd /Users/michaelwu/海淀京张规划
python3 -m unittest scripts/test_build_formal_figures.py -v
```

Expected: FAIL with `AttributeError` for `source_contract`, `content_contract`, or `render_all`.

---

### Task 2: Rebuild the five-figure bilingual visual system

**Files:**
- Modify: `/Users/michaelwu/海淀京张规划/scripts/build_formal_figures.py`
- Test: `/Users/michaelwu/海淀京张规划/scripts/test_build_formal_figures.py`
- Generate: the ten canonical PNG files in `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/assets/figures/`

- [ ] **Step 1: Add the real-base source contract and output API**

Add these constants and functions, preserving the existing color palette and font fallback:

```python
BASE_CLEAN_PATH = ROOT / "docs/maps/jingzhang-corridor/base-and-layers-v1/base-clean.png"
AMAP_DETAIL_PATH = ROOT / "docs/maps/jingzhang-corridor/jingzhang-corridor-amap-registered-v3.png"
CANONICAL_OUTPUTS = {
    "overview": "site-overview",
    "actions": "land-use-structure",
    "keys": "key-areas",
    "scenarios": "mobility-bluegreen",
    "evidence": "metrics-evidence",
}
W, H = 2400, 1500


def source_contract() -> dict[str, Path]:
    return {
        "base_clean": BASE_CLEAN_PATH,
        "amap_detail": AMAP_DETAIL_PATH,
        "axis": AXIS_PATH,
    }


def content_contract(content: dict) -> tuple:
    return (
        len(content["three"]),
        len(content["connect"]),
        len(content["crossings"]),
        len(content["reqs"]),
        len(content["scenarios"]),
        tuple(len(item) for item in content["key_cards"]),
    )


def render_all(out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    renderers = {
        "overview": render_overview,
        "actions": render_land,
        "keys": render_keys,
        "scenarios": render_mobility,
        "evidence": render_metrics,
    }
    written: list[Path] = []
    for language, content, suffix in (("zh", ZH, ""), ("en", EN, ".en")):
        for key, renderer in renderers.items():
            output = out_dir / f"{CANONICAL_OUTPUTS[key]}{suffix}.png"
            renderer(content, language).save(output, optimize=True)
            written.append(output)
    return written
```

Update `main()` to call `render_all(OUT)` and print the ten returned paths.

- [ ] **Step 2: Add the shared real-base image helpers**

Implement these complete helper contracts:

```python
def cover_crop(path: Path, size: tuple[int, int], crop: tuple[float, float, float, float] | None = None) -> Image.Image:
    with Image.open(path) as source:
        image = source.convert("RGB")
    if crop is not None:
        left, top, right, bottom = crop
        image = image.crop((int(left * image.width), int(top * image.height), int(right * image.width), int(bottom * image.height)))
    scale = max(size[0] / image.width, size[1] / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    x = (resized.width - size[0]) // 2
    y = (resized.height - size[1]) // 2
    return resized.crop((x, y, x + size[0], y + size[1]))


def muted_map(path: Path, size: tuple[int, int], crop: tuple[float, float, float, float] | None = None) -> Image.Image:
    from PIL import ImageEnhance
    image = cover_crop(path, size, crop)
    image = ImageEnhance.Color(image).enhance(0.48)
    image = ImageEnhance.Contrast(image).enhance(0.88)
    return ImageEnhance.Brightness(image).enhance(1.08)


def paste_panel(canvas: Image.Image, panel: Image.Image, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    canvas.paste(panel.resize((x1 - x0, y1 - y0), Image.Resampling.LANCZOS), (x0, y0))
```

The high-detail context crops must remain labeled `context window / design model` and must never be labeled as statutory key-area boundaries.

- [ ] **Step 3: Replace F01 with the approved hybrid masterplan**

Implement `render_overview()` with the following fixed hierarchy:

1. B0 occupies at least 64% of the figure area.
2. The approved Jing-Zhang axis is the strongest line, in red with a white casing.
3. The six audit corridors are shown as state-coded cross-axis marks: solid green for verified existing/upgrade interfaces, dashed gold for candidate study interfaces; the legend explains that an audit point is not proof of a barrier.
4. Three colored circular functional markers show Zhongzhiyuan, Beijing AI Origin, and Dazhongsi; circles are labeled as functional cores, not redlines.
5. One detailed context inset demonstrates that the planning marks sit on a real urban fabric.
6. A right-side narrative block states the one-axis/three-core/four-connection logic and the AI role.
7. The footer repeats the provisional-model precision boundary.

Do not draw a new 2 km polygon, a new key-area polygon, or a new crossing geometry.

- [ ] **Step 4: Replace F02 with the spatial-construction action map**

Implement `render_land()` as a real-base action map plus a five-action legend:

- continuous green walking/cycling and accessibility repair;
- east-west stitch interfaces classified by state;
- all-age public-life and climate-comfort nodes;
- conditional adaptive reuse of existing buildings and ground floors;
- controlled robot, short-shuttle, delivery, and maintenance nodes.

Every action row must include `carrier`, `AI support`, and `gate`, and the construction sequence must read: `basic access and green life → adaptive reuse and shared interfaces → new construction only after evidence`.

- [ ] **Step 5: Replace F03 with three differentiated key-area prototypes**

Implement `render_keys()` with three equal columns. Each column contains a detailed registered-map context crop, a schematic spatial overlay, and four short fields: `people/time`, `physical actions`, `AI service`, `decision gate`.

Use these context crops only as non-statutory windows:

```python
CORE_CROPS = {
    "zhongzhiyuan": (0.0, 0.02, 1.0, 0.34),
    "origin": (0.0, 0.28, 1.0, 0.70),
    "dazhongsi": (0.0, 0.64, 1.0, 1.0),
}
```

The approved role and scale labels are immutable:

```python
(“众智园”, “192.1 ha”, “创新孵化核心”)
(“北京 AI 原点社区”, “104.3 ha”, “人才活力核心”)
(“大钟寺 AI 产业聚集区”, “72.0 ha”, “产业聚集核心”)
```

The chain at the bottom must read: `learning → research → incubation → testing → life feedback → adoption → industrialization → feedback`.

- [ ] **Step 6: Replace F04 with four scenario families and the shared AI loop**

Implement `render_mobility()` as four scenario quadrants:

- S1 education and incubation;
- S2 daily livability and weekend all-age use;
- S3 people-first intelligent mobility including T01 service robots, T02 low-speed shared shuttles, and T03 last-mile delivery;
- S4 extreme-weather shelter, supplies, personnel, and mobility support.

Each quadrant must visibly bind `spatial carrier → AI service → responsible operator`. A central loop must read `resource/status → demand → match → handoff → confirmation → review`, with `human decision for high-risk tasks` outside the loop.

- [ ] **Step 7: Replace F05 with implementation, metrics, R1–R7, and evidence gates**

Implement `render_metrics()` with:

- near/mid/long-term project packages;
- access, usage, response-time, completion, all-age coverage, and green-mobility indicators;
- official-text scale separated from provisional-model metrics;
- R1–R7 shown exactly once each with its board location;
- recalculation triggers for official boundaries, regulatory plans, tenure, road redlines, municipal infrastructure, and heritage controls.

- [ ] **Step 8: Update the Chinese and English content dictionaries**

Add a `scenarios` list with four items to both `ZH` and `EN`, make the dictionaries structurally identical under `content_contract()`, and update text to reflect:

- Zhan Tianyou spirit as the cultural value line, with railway as carrier;
- companies and incubators providing recurring frontier lectures and real project feedback to students;
- AI Origin Community as daily life and resilience, not only talent programming;
- Dazhongsi as adoption/industrialization and controlled night logistics;
- no claim that the three core shapes are official boundaries.

- [ ] **Step 9: Run tests until the full figure contract passes**

Run:

```bash
cd /Users/michaelwu/海淀京张规划
python3 -m unittest scripts/test_build_formal_figures.py -v
python3 scripts/build_formal_figures.py
```

Expected: all three tests PASS and ten `2400 x 1500` PNG paths are printed.

- [ ] **Step 10: Perform a contact-sheet visual check**

Run:

```bash
cd /Users/michaelwu/海淀京张规划
/opt/homebrew/bin/magick montage \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/assets/figures/site-overview.png \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/assets/figures/land-use-structure.png \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/assets/figures/key-areas.png \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/assets/figures/mobility-bluegreen.png \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/assets/figures/metrics-evidence.png \
  -thumbnail 900x -tile 2x -geometry +18+18 \
  work-temp/jingzhang-opt-20260831-figures.jpg
```

Expected: one five-panel contact sheet with no clipped labels, blank panels, repeated filler figures, or illegible legends.

---

### Task 3: Align the bilingual proposal and visual index with the approved design

**Files:**
- Modify: `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/proposal.md`
- Modify: `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/proposal.en.md`
- Modify: `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/visual/index.html`
- Modify: `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/visual/index.en.html`
- Regenerate: `report/proposal.html`, `report/proposal.en.html`

- [ ] **Step 1: Update the Chinese proposal around the five canonical figures**

Preserve the current front matter and evidence markers. Revise the bodies so that:

- `site-overview.png` follows the problem → masterplan → four connections text;
- `land-use-structure.png` follows the physical construction and state-classification text;
- `key-areas.png` follows the three immutable role/scale subsections;
- `mobility-bluegreen.png` follows the four scenario families and T01–T03 text;
- `metrics-evidence.png` follows phasing, governance, R1–R7, and evidence-boundary text.

Include this exact planning boundary sentence in the Chinese report:

```markdown
本项目以 B0 作为总体制图底图，以已校准的高细节地图作为局部现状证据；M0 仅用于自定 2 公里设施盘点范围参照，不采用其中的重点区划分。2 公里范围和三处重点区图形均为工作模型，不是主办方法定边界或官方红线。
```

- [ ] **Step 2: Apply the same information contract to the English proposal**

Include this exact English counterpart:

```markdown
B0 is the overall mapping base, while the registered detailed map provides local existing-condition evidence. M0 is used only as a reference for the self-defined 2 km facility inventory and not for its key-area divisions. The 2 km extent and the three key-area shapes are working models, not organizer-issued statutory boundaries or official redlines.
```

Keep `translation_of`, `translation_file`, all source IDs, standard IDs, depth IDs, data IDs, and metric IDs synchronized.

- [ ] **Step 3: Rebuild both visual indexes without changing metric data attributes**

Use five sections matching the five canonical figures. The HTML must remain offline-only and retain these exact metric attributes:

```html
data-metric="site_area_sqm" data-value="11412825.386"
data-metric="green_ratio" data-value="0.123423"
data-metric="public_space_ratio" data-value="0.073281"
```

The three key-area cards must use 192.1 ha, 104.3 ha, and 72.0 ha with their approved roles. The four-scenario section must state the human-decision boundary for high-risk tasks.

- [ ] **Step 4: Regenerate the bilingual HTML reports**

Run:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-formal-workspace
python3 scripts/render_proposal_html.py submissions/mrcrow/jingzhang-symbiotic-ai-belt
```

Expected: paths for `report/proposal.html` and `report/proposal.en.html`, with no remote-resource error.

- [ ] **Step 5: Check required content and forbidden overclaims**

Run:

```bash
cd /Users/michaelwu/海淀京张规划
rg -n "192\.1|104\.3|72\.0|R1|R7|B0|M0|2 公里|2 km|human|人工" \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/proposal.md \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/proposal.en.md
rg -n "官方红线|official redline|法定边界|statutory boundar" \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/proposal.md \
  haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/proposal.en.md
```

Expected: approved scale and boundary disclaimers are present; no sentence claims that provisional shapes are official.

---

### Task 4: Recompose the A3 booklets and four A0 boards

**Files:**
- Create: `/Users/michaelwu/海淀京张规划/scripts/test_build_formal_pdfs.py`
- Modify: `/Users/michaelwu/海淀京张规划/scripts/build_formal_pdfs.py`
- Regenerate: four PDFs under `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/drawings/`

- [ ] **Step 1: Load and follow the PDF skill before changing or generating PDFs**

Read `/Users/michaelwu/.codex/plugins/cache/openai-primary-runtime/pdf/26.826.12353/skills/pdf/SKILL.md` completely. Use its required render-and-inspect workflow for the four final PDF files.

- [ ] **Step 2: Write the failing layout test**

Create:

```python
from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/build_formal_pdfs.py"
spec = importlib.util.spec_from_file_location("build_formal_pdfs", MODULE_PATH)
assert spec and spec.loader
pdfs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pdfs)


class FormalPdfContractTest(unittest.TestCase):
    def test_a0_board_contract(self) -> None:
        self.assertEqual(
            [item["hero"] for item in pdfs.A0_BOARD_LAYOUTS],
            ["site-overview", "key-areas", "mobility-bluegreen", "metrics-evidence"],
        )
        self.assertEqual(len(pdfs.A0_BOARD_LAYOUTS), 4)

    def test_generated_page_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            pdfs.build_all(out)
            expected = {
                "a3-booklet.pdf": 6,
                "a3-booklet.en.pdf": 6,
                "a0-boards.pdf": 4,
                "a0-boards.en.pdf": 4,
            }
            for name, pages in expected.items():
                result = subprocess.run(["/opt/homebrew/bin/pdfinfo", str(out / name)], check=True, capture_output=True, text=True)
                page_line = next(line for line in result.stdout.splitlines() if line.startswith("Pages:"))
                self.assertEqual(int(page_line.split(":", 1)[1]), pages)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the test and verify the new layout API is missing**

Run:

```bash
cd /Users/michaelwu/海淀京张规划
python3 -m unittest scripts/test_build_formal_pdfs.py -v
```

Expected: FAIL for missing `A0_BOARD_LAYOUTS` or `build_all`.

- [ ] **Step 4: Implement the non-repetitive A0 layout contract**

Add:

```python
A0_BOARD_LAYOUTS = [
    {"hero": "site-overview", "support": "land-use-structure", "title_key": "board_1"},
    {"hero": "key-areas", "support": None, "title_key": "board_2"},
    {"hero": "mobility-bluegreen", "support": None, "title_key": "board_3"},
    {"hero": "metrics-evidence", "support": None, "title_key": "board_4"},
]
```

Board 1 uses a 68/32 hero/support split. Boards 2–4 use one large unique hero figure plus a narrow board-specific summary strip; they must not repeat another full figure as filler. Titles must answer, in order: why Jing-Zhang, how the three cores collaborate, how the city and AI operate, and how implementation is governed and verified.

- [ ] **Step 5: Implement the six-page A3 contract and shared build API**

Add:

```python
A3_PAGE_FIGURES = [
    "site-overview",
    "land-use-structure",
    "key-areas",
    "mobility-bluegreen",
    "metrics-evidence",
]


def build_all(out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs = [
        ("zh", build_a3, out_dir / "a3-booklet.pdf"),
        ("en", build_a3, out_dir / "a3-booklet.en.pdf"),
        ("zh", build_a0, out_dir / "a0-boards.pdf"),
        ("en", build_a0, out_dir / "a0-boards.en.pdf"),
    ]
    for language, builder, path in outputs:
        builder(language, path)
    return [path for _language, _builder, path in outputs]
```

Each A3 booklet is six pages: cover plus the five canonical figures. Update `TEXT["zh"]` and `TEXT["en"]` to use the approved four-board titles, four scenario families, three-core roles, and evidence boundary.

- [ ] **Step 6: Run PDF tests and generate the formal PDFs**

Run:

```bash
cd /Users/michaelwu/海淀京张规划
python3 -m unittest scripts/test_build_formal_pdfs.py -v
python3 scripts/build_formal_pdfs.py
```

Expected: both tests PASS; four output paths are printed; A3 files have 6 pages and A0 files have 4 pages.

- [ ] **Step 7: Render all PDF pages for visual QA**

Run:

```bash
cd /Users/michaelwu/海淀京张规划
mkdir -p work-temp/jingzhang-opt-20260831-pdf
/opt/homebrew/bin/pdftoppm -jpeg -r 90 haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/drawings/a0-boards.pdf work-temp/jingzhang-opt-20260831-pdf/a0-zh
/opt/homebrew/bin/pdftoppm -jpeg -r 90 haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/drawings/a0-boards.en.pdf work-temp/jingzhang-opt-20260831-pdf/a0-en
/opt/homebrew/bin/pdftoppm -jpeg -r 90 haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/drawings/a3-booklet.pdf work-temp/jingzhang-opt-20260831-pdf/a3-zh
/opt/homebrew/bin/pdftoppm -jpeg -r 90 haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/drawings/a3-booklet.en.pdf work-temp/jingzhang-opt-20260831-pdf/a3-en
/opt/homebrew/bin/magick montage work-temp/jingzhang-opt-20260831-pdf/*.jpg -thumbnail 620x -tile 4x -geometry +14+14 work-temp/jingzhang-opt-20260831-pdf/contact.jpg
```

Expected: 20 rendered pages total and one contact sheet. Inspect for missing Chinese glyphs, clipped text, excessive white space, repeated board content, unreadable legends, and incorrect bilingual pairings.

---

### Task 5: Refresh hashes and run the official four-gate validation

**Files:**
- Modify automatically: `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/manifest.json`
- Modify automatically: `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/self_check.json`
- Read: all formal package files

- [ ] **Step 1: Refresh all declared hashes and invalidate the old self-check**

Run:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-formal-workspace
python3 scripts/refresh_submission_manifest.py submissions/mrcrow/jingzhang-symbiotic-ai-belt --json
```

Expected: `"ok": true` and `"validation_claim_self_checked": false`.

- [ ] **Step 2: Run and persist the four-gate self-check**

Run:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-formal-workspace
PYTHONPATH=.review-deps python3 scripts/self_check_submission.py \
  submissions/mrcrow/jingzhang-symbiotic-ai-belt \
  --repo-root . \
  --pr-author mrcrow \
  --pr-author-id 2879021 \
  --mark-self-checked \
  --json
```

Expected:

```json
{
  "ok": true,
  "review_status": "formal-review-ready",
  "can_enter_formal_review": true,
  "self_checked_manifest_updated": true
}
```

All four gates must be `pass`: deterministic validation, spatial review, visual packaging, and professional evidence.

- [ ] **Step 3: Verify the persisted readiness contract**

Run:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-formal-workspace
python3 - <<'PY'
import json
from pathlib import Path
p = Path('submissions/mrcrow/jingzhang-symbiotic-ai-belt')
m = json.loads((p / 'manifest.json').read_text(encoding='utf-8'))
s = json.loads((p / 'self_check.json').read_text(encoding='utf-8'))
assert m['package_state'] == 'ready_for_review'
assert m['validation_claim']['self_checked'] is True
assert s['ok'] is True
assert s['can_enter_formal_review'] is True
assert all(item['result'] == 'pass' for item in s['checks'])
print('formal-review-ready')
PY
```

Expected: `formal-review-ready`.

---

### Task 6: Sync the validated package and review the exact pull-request diff

**Files:**
- Copy from: `haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/`
- Copy to: `haidian-submit-worktree/submissions/mrcrow/jingzhang-symbiotic-ai-belt/`
- Archive locally, then remove from the PR tree: `haidian-submit-worktree/docs/superpowers/specs/2026-08-31-jingzhang-submission-visual-optimization-design.md`
- Archive locally, then remove from the PR tree: `haidian-submit-worktree/docs/superpowers/plans/2026-08-31-jingzhang-submission-visual-optimization.md`

- [ ] **Step 1: Sync only the validated submission package**

Run:

```bash
cd /Users/michaelwu/海淀京张规划
rsync -a haidian-formal-workspace/submissions/mrcrow/jingzhang-symbiotic-ai-belt/ haidian-submit-worktree/submissions/mrcrow/jingzhang-symbiotic-ai-belt/
```

Expected: the worktree package matches the formal source of truth; no files outside the submission directory are overwritten.

- [ ] **Step 2: Archive the internal planning documents outside the pull-request tree**

Create `/Users/michaelwu/海淀京张规划/docs/superpowers/specs/` and `/Users/michaelwu/海淀京张规划/docs/superpowers/plans/` if absent, then copy the approved design spec and this implementation plan there. Verify both archive files exist before removing the Git-worktree copies.

Run after verification:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-submit-worktree
git rm docs/superpowers/specs/2026-08-31-jingzhang-submission-visual-optimization-design.md
git rm docs/superpowers/plans/2026-08-31-jingzhang-submission-visual-optimization.md
```

Expected: the files remain available under `/Users/michaelwu/海淀京张规划/docs/superpowers/`, while the final PR diff contains no `docs/superpowers/` paths. The earlier local spec commit remains recoverable in Git history.

- [ ] **Step 3: Verify final diff scope and file integrity**

Run:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-submit-worktree
git diff --check
git status --short
git diff --name-only upstream/main...HEAD
git diff --name-only
```

Expected: after staging the intended changes, every final changed path is under `submissions/mrcrow/jingzhang-symbiotic-ai-belt/`; the internal planning documents cancel out of the final branch diff.

- [ ] **Step 4: Run the repository validator against the synced worktree copy**

Run:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-submit-worktree
PYTHONPATH=/Users/michaelwu/海淀京张规划/haidian-formal-workspace/.review-deps \
python3 scripts/self_check_submission.py \
  submissions/mrcrow/jingzhang-symbiotic-ai-belt \
  --repo-root . \
  --pr-author mrcrow \
  --pr-author-id 2879021 \
  --json
```

Expected: `ok=true`, `formal-review-ready`, and four passing gates without modifying the synced package.

---

### Task 7: Commit, push, and verify the existing PR update

**Files:**
- Stage only: `submissions/mrcrow/jingzhang-symbiotic-ai-belt/**`
- Do not stage: `.superpowers/**`, `work-temp/**`, local build helpers, or any unrelated file

- [ ] **Step 1: Stage the exact final package and inspect the staged summary**

Run:

```bash
cd /Users/michaelwu/海淀京张规划/haidian-submit-worktree
git add submissions/mrcrow/jingzhang-symbiotic-ai-belt
git status --short
git diff --cached --stat
git diff --cached --check
```

Expected: only the submission package and the intentional deletion that cancels the local `docs/superpowers` additions are staged; `git diff --cached --check` is silent.

- [ ] **Step 2: Commit the optimized submission**

Run:

```bash
git commit -m "feat: refine Jing-Zhang spatial design submission"
```

Expected: one commit containing the rebuilt bilingual figures, reports, PDFs, manifest, and self-check, plus removal of the internal planning docs from the final PR tree.

- [ ] **Step 3: Verify the final branch diff before network mutation**

Run:

```bash
git diff --name-only upstream/main...HEAD
git log -3 --oneline
```

Expected: every net changed path is under `submissions/mrcrow/jingzhang-symbiotic-ai-belt/`; the latest commit is `feat: refine Jing-Zhang spatial design submission`.

- [ ] **Step 4: Push the existing branch**

Run:

```bash
git push origin submission/mrcrow-jingzhang-symbiotic-ai-belt
```

Expected: the existing PR 4317 updates; no new PR is created.

- [ ] **Step 5: Verify PR checks once without busy polling**

Run:

```bash
gh pr checks 4317 --repo open-city-ai/haidian
```

Expected: checks are visible for the new head commit. A queued or pending state is acceptable immediately after push; any completed failure must be diagnosed before claiming submission completion.

---

## Self-review against the approved specification

- Spec sections 2–3 (goal, boundaries, R1–R7): covered by Tasks 2, 3, and 5.
- Spec section 4 (hybrid masterplan): covered by Task 2 Steps 1–3.
- Spec section 5 (three differentiated cores): covered by Task 2 Step 5 and Task 3.
- Spec section 6 (three-part AI binding and four scenarios): covered by Task 2 Step 6 and Task 3.
- Spec section 7 (four A0 narratives): covered by Task 4.
- Spec section 8 (scope control): enforced by the file map, Task 2 prohibitions, and Task 6 diff-scope check.
- Spec section 9 (content, spatial, visual, and delivery verification): covered by Tasks 1, 2, 4, 5, and 6.
- Spec section 10 (implementation sequence): preserved by Tasks 1–7.
- Placeholder scan: no `TBD`, `TODO`, `implement later`, unspecified error handling, or undefined task reference remains.
- Type consistency: `source_contract`, `content_contract`, `render_all`, `A0_BOARD_LAYOUTS`, `A3_PAGE_FIGURES`, and `build_all` are introduced before later tasks use them.
