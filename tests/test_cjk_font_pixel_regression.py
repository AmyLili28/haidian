from __future__ import annotations

import base64
import binascii
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FONT_FIXTURE = REPO_ROOT / "tests" / "fixtures" / "codex-cjk-fixture.ttf.b64"
FONT_FAMILY = "Codex CJK Fixture"
SAMPLE_GLYPHS = "一一一"
WINDOW_SIZE = "640,320"
GLYPH_CROP = (20, 20, 620, 200)
MIN_CHANGED_PIXELS = 500
MIN_CHANGED_FRACTION = 0.01


def find_chromium() -> str | None:
    """Find a Chromium-compatible executable without requiring one in CI."""

    configured = os.environ.get("CHROMIUM_BIN")
    candidates = [configured] if configured else []
    candidates.extend(
        shutil.which(name)
        for name in (
            "chromium",
            "chromium-browser",
            "google-chrome",
            "google-chrome-stable",
            "chrome",
        )
    )
    candidates.extend(
        [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]
    )
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        candidates.append(
            str(Path(local_app_data) / "Google" / "Chrome" / "Application" / "chrome.exe")
        )
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(Path(candidate))
    return None


def fixture_base64() -> str:
    return "".join(
        line.strip()
        for line in FONT_FIXTURE.read_text(encoding="ascii").splitlines()
        if line.strip()
    )


def test_page(*, embedded: bool, font_payload: str) -> str:
    """Build a self-contained page for the same Chromium screenshot path."""

    if embedded:
        font_face = f"""
@font-face {{
  font-family: \"{FONT_FAMILY}\";
  src: url(\"data:font/ttf;base64,{font_payload}\") format(\"truetype\");
  font-style: normal;
  font-weight: 400;
  font-display: block;
}}
"""
        glyph_family = f'"{FONT_FAMILY}"'
        settle_script = f"""
<script>
(async () => {{
  const face = '400 144px "{FONT_FAMILY}"';
  const text = {SAMPLE_GLYPHS!r};
  try {{
    await document.fonts.load(face, text);
    await document.fonts.ready;
    const ready = document.fonts.status === "loaded";
    const checked = document.fonts.check(face, text);
    document.documentElement.dataset.fontsReady = String(ready);
    document.documentElement.dataset.fontsCheck = String(checked);
    document.getElementById("status").textContent =
      `fonts.ready=${{ready}} fonts.check=${{checked}}`;
  }} catch (error) {{
    document.documentElement.dataset.fontsReady = "false";
    document.documentElement.dataset.fontsCheck = "false";
    document.getElementById("status").textContent = "font loading failed";
  }}
  document.documentElement.classList.add("settled");
}})();
</script>
"""
    else:
        font_face = ""
        glyph_family = "sans-serif"
        settle_script = ""
    html_class = " class=\"settled\"" if not embedded else ""

    return f"""<!doctype html>
<html{html_class}>
<head>
<meta charset="utf-8">
<style>
{font_face}
html, body {{
  margin: 0;
  width: 640px;
  height: 320px;
  overflow: hidden;
  background: white;
}}
#stage {{
  padding: 20px;
  visibility: visible;
}}
html:not(.settled) #stage {{
  visibility: hidden;
}}
#glyph {{
  width: 600px;
  height: 180px;
  color: black;
  font-family: {glyph_family};
  font-size: 144px;
  font-style: normal;
  font-weight: 400;
  line-height: 1;
  white-space: nowrap;
}}
#status {{
  font-family: sans-serif;
  font-size: 14px;
  line-height: 20px;
  color: #555;
}}
</style>
</head>
<body>
<main id="stage">
<div id="glyph">{SAMPLE_GLYPHS}</div>
<div id="status">fallback-only</div>
</main>
{settle_script}
</body>
</html>
"""


def run_screenshot(
    executable: str,
    source: Path,
    screenshot: Path,
    profile: Path,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            executable,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--hide-scrollbars",
            "--no-first-run",
            "--no-default-browser-check",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=3000",
            "--force-device-scale-factor=1",
            f"--window-size={WINDOW_SIZE}",
            f"--user-data-dir={profile}",
            f"--screenshot={screenshot}",
            # --dump-dom observes the DOM from this same navigation; the
            # screenshot and font assertions therefore share one browser run.
            "--dump-dom",
            source.resolve().as_uri(),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        timeout=60,
    )


class CjkFontPixelRegressionTests(unittest.TestCase):
    def test_embedded_cjk_font_is_loaded_and_changes_chromium_pixels(self) -> None:
        executable = find_chromium()
        if executable is None:
            self.skipTest("Chromium is unavailable")
        try:
            from PIL import Image, ImageChops
        except ImportError:  # pragma: no cover - Pillow is a review dependency.
            self.skipTest("Pillow unavailable")

        payload = fixture_base64()
        try:
            font_bytes = base64.b64decode(payload, validate=True)
        except (ValueError, binascii.Error) as exc:
            self.fail(f"invalid base64 font fixture: {exc}")
        self.assertGreater(len(font_bytes), 0, "font fixture must not be empty")
        self.assertLess(len(font_bytes), 4096, "font fixture should remain tiny")

        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            embedded_html = root / "embedded.html"
            fallback_html = root / "fallback.html"
            embedded_png = root / "embedded.png"
            fallback_png = root / "fallback.png"
            embedded_html.write_text(
                test_page(embedded=True, font_payload=payload), encoding="utf-8"
            )
            fallback_html.write_text(
                test_page(embedded=False, font_payload=""), encoding="utf-8"
            )

            embedded_run = run_screenshot(
                executable, embedded_html, embedded_png, root / "chrome-profile"
            )
            self.assertEqual(
                0,
                embedded_run.returncode,
                embedded_run.stderr[-2000:] or embedded_run.stdout[-2000:],
            )
            self.assertTrue(embedded_png.is_file(), "Chromium did not write screenshot")
            self.assertRegex(
                embedded_run.stdout,
                r'data-fonts-ready=["\']true["\']',
                "Chromium DOM did not report document.fonts.ready",
            )
            self.assertRegex(
                embedded_run.stdout,
                r'data-fonts-check=["\']true["\']',
                "Chromium DOM did not report document.fonts.check",
            )

            fallback_run = run_screenshot(
                executable, fallback_html, fallback_png, root / "fallback-profile"
            )
            self.assertEqual(
                0,
                fallback_run.returncode,
                fallback_run.stderr[-2000:] or fallback_run.stdout[-2000:],
            )
            self.assertTrue(fallback_png.is_file(), "Chromium did not write screenshot")

            with Image.open(embedded_png) as embedded_image, Image.open(
                fallback_png
            ) as fallback_image:
                self.assertEqual(embedded_image.size, fallback_image.size)
                embedded_crop = embedded_image.convert("RGB").crop(GLYPH_CROP)
                fallback_crop = fallback_image.convert("RGB").crop(GLYPH_CROP)
                diff = ImageChops.difference(embedded_crop, fallback_crop)
                changed_pixels = sum(diff.convert("L").histogram()[17:])

            crop_pixels = (GLYPH_CROP[2] - GLYPH_CROP[0]) * (
                GLYPH_CROP[3] - GLYPH_CROP[1]
            )
            self.assertGreater(
                changed_pixels,
                MIN_CHANGED_PIXELS,
                "embedded and fallback glyphs are unexpectedly identical",
            )
            self.assertGreater(
                changed_pixels / crop_pixels,
                MIN_CHANGED_FRACTION,
                "pixel difference is below the regression threshold",
            )


if __name__ == "__main__":
    unittest.main()
