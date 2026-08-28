from __future__ import annotations

import base64
import binascii
import os
import signal
import shutil
import subprocess
import tempfile
import time
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
CHROMIUM_TIMEOUT_SECONDS = 60
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PNG_TRAILER = b"\x00\x00\x00\x00IEND\xaeB`\x82"


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


def screenshot_is_ready(path: Path) -> bool:
    """Return true only after Chromium has created a recognizable PNG."""

    try:
        if path.stat().st_size <= len(PNG_SIGNATURE) + len(PNG_TRAILER):
            return False
        with path.open("rb") as handle:
            if handle.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
                return False
            handle.seek(-len(PNG_TRAILER), 2)
            return handle.read(len(PNG_TRAILER)) == PNG_TRAILER
    except OSError:
        return False


def terminate_process_tree(
    process: subprocess.Popen[str], *, process_group_id: int | None = None
) -> tuple[str, str]:
    """Stop Chromium and collect output without leaving renderer children."""

    if os.name != "nt" and process_group_id is None:
        try:
            process_group_id = os.getpgid(process.pid)
        except ProcessLookupError:
            pass

    def signal_tree(*, force: bool) -> None:
        if os.name == "nt":
            try:
                result = subprocess.run(
                    ["taskkill", "/PID", str(process.pid), "/T"]
                    + (["/F"] if force else []),
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    check=False,
                    timeout=5,
                )
                if result.returncode == 0:
                    return
            except (OSError, subprocess.TimeoutExpired):
                pass
        elif process_group_id is not None:
            try:
                os.killpg(
                    process_group_id,
                    signal.SIGKILL if force else signal.SIGTERM,
                )
                return
            except (OSError, ProcessLookupError):
                pass
        try:
            (process.kill if force else process.terminate)()
        except ProcessLookupError:
            pass

    if process.poll() is None:
        signal_tree(force=False)

    try:
        stdout, stderr = process.communicate(timeout=5)
    except subprocess.TimeoutExpired as exc:
        signal_tree(force=True)
        try:
            return process.communicate(timeout=5)
        except subprocess.TimeoutExpired as killed_exc:
            stdout = killed_exc.stdout or exc.stdout or ""
            stderr = killed_exc.stderr or exc.stderr or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode("utf-8", errors="replace")
            if isinstance(stderr, bytes):
                stderr = stderr.decode("utf-8", errors="replace")
            return stdout, stderr
    return stdout or "", stderr or ""


def run_chromium(
    executable: str,
    source: Path,
    profile: Path,
    *,
    screenshot: Path | None = None,
    dump_dom: bool = False,
) -> subprocess.CompletedProcess[str]:
    command = [
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
    ]
    if screenshot is not None:
        command.append(f"--screenshot={screenshot}")
    if dump_dom:
        command.append("--dump-dom")
    # Keep screenshot and DOM inspection in separate browser modes. Chrome for
    # macOS can keep a combined --screenshot/--dump-dom invocation alive.
    command.append(source.resolve().as_uri())

    capture_output = dump_dom
    popen_options: dict[str, object] = {
        "stdout": subprocess.PIPE if capture_output else subprocess.DEVNULL,
        "stderr": subprocess.PIPE if capture_output else subprocess.DEVNULL,
        "text": True,
        "encoding": "utf-8",
        "errors": "replace",
    }
    if os.name == "nt":
        popen_options["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        popen_options["start_new_session"] = True

    process = subprocess.Popen(command, **popen_options)
    process_group_id = process.pid if os.name != "nt" else None
    try:
        if screenshot is not None:
            deadline = time.monotonic() + CHROMIUM_TIMEOUT_SECONDS
            while process.poll() is None:
                if screenshot_is_ready(screenshot):
                    stdout, stderr = terminate_process_tree(
                        process, process_group_id=process_group_id
                    )
                    note = "Chromium was terminated after the complete screenshot was verified."
                    stderr = f"{stderr}\n{note}" if stderr else note
                    return subprocess.CompletedProcess(command, 0, stdout, stderr)
                if time.monotonic() >= deadline:
                    stdout, stderr = terminate_process_tree(
                        process, process_group_id=process_group_id
                    )
                    note = "Chromium did not produce a complete screenshot before timeout"
                    stderr = f"{note}\n{stderr}" if stderr else note
                    return subprocess.CompletedProcess(command, 124, stdout, stderr)
                time.sleep(0.1)

        try:
            stdout, stderr = process.communicate(timeout=CHROMIUM_TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            stdout, stderr = terminate_process_tree(
                process, process_group_id=process_group_id
            )
            note = "Chromium did not finish DOM inspection before timeout"
            stderr = f"{note}\n{stderr}" if stderr else note
            return subprocess.CompletedProcess(command, 124, stdout, stderr)
        return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)
    finally:
        if process.poll() is None:
            terminate_process_tree(process, process_group_id=process_group_id)


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

            embedded_screenshot_run = run_chromium(
                executable,
                embedded_html,
                root / "chrome-profile-embedded-screenshot",
                screenshot=embedded_png,
            )
            embedded_dom_run = run_chromium(
                executable,
                embedded_html,
                root / "chrome-profile-embedded-dom",
                dump_dom=True,
            )
            self.assertEqual(
                0,
                embedded_screenshot_run.returncode,
                embedded_screenshot_run.stderr[-2000:]
                or embedded_screenshot_run.stdout[-2000:],
            )
            self.assertTrue(
                screenshot_is_ready(embedded_png),
                "Chromium did not write a complete screenshot",
            )
            self.assertEqual(
                0,
                embedded_dom_run.returncode,
                embedded_dom_run.stderr[-2000:] or embedded_dom_run.stdout[-2000:],
            )
            self.assertRegex(
                embedded_dom_run.stdout,
                r'data-fonts-ready=["\']true["\']',
                "Chromium DOM did not report document.fonts.ready",
            )
            self.assertRegex(
                embedded_dom_run.stdout,
                r'data-fonts-check=["\']true["\']',
                "Chromium DOM did not report document.fonts.check",
            )

            fallback_run = run_chromium(
                executable,
                fallback_html,
                root / "chrome-profile-fallback",
                screenshot=fallback_png,
            )
            self.assertEqual(
                0,
                fallback_run.returncode,
                fallback_run.stderr[-2000:] or fallback_run.stdout[-2000:],
            )
            self.assertTrue(
                screenshot_is_ready(fallback_png),
                "Chromium did not write a complete screenshot",
            )

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
