#!/usr/bin/env python3
"""Regenerate A0 landscape exhibition boards for a submission package.

Produces drawings/a0-boards.pdf with readable print-scale layout (esp. A0-01)
and an optional first-board PNG preview.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date
from pathlib import Path

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# A0 landscape (1189 × 841 mm)
PAGE_W = 3370.39
PAGE_H = 2383.94
MARGIN = 52
FOOTER_H = 200
TITLE_H = 210

FONT_CANDIDATES = [
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
]

LEGEND_ITEMS = [
    (colors.HexColor("#4A90D9"), "统筹研究范围（43.6 km²）"),
    (colors.HexColor("#D94A4A"), "总体设计范围（11.4 km²）"),
    (colors.HexColor("#E8C547"), "重点区域（369.3 ha）"),
    (colors.HexColor("#8B4513"), "京张铁路遗址走廊（慢行脊）"),
]

BOUNDARY_WARNING = (
    "⚠ 临时工作边界警示：本图基于 provisional 工作边界编制，仅供方案讨论与评审；"
    "不作为法定规划控制依据。正式红线发布后须重算全部几何与指标。"
)

SOURCE_ATTRIBUTION = (
    "底图：天地图 1:100 万公众版 + 开放路网（OSM/天地图裁切参考）｜"
    "审图号：京 S(2025)041 号｜坐标：EPSG:4326 展示 / EPSG:4548 面积复算"
)


def register_cjk_font() -> str:
    for path in FONT_CANDIDATES:
        if not Path(path).exists():
            continue
        name = "CJK"
        try:
            if path.endswith(".ttc"):
                pdfmetrics.registerFont(TTFont(name, path, subfontIndex=0))
            else:
                pdfmetrics.registerFont(TTFont(name, path))
            return name
        except Exception:
            continue
    return "Helvetica"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def draw_image_fit(
    c: canvas.Canvas,
    img_path: Path,
    x: float,
    y: float,
    w: float,
    h: float,
    border: bool = True,
) -> None:
    if not img_path.is_file():
        c.setFillColor(colors.HexColor("#F5F5F5"))
        c.rect(x, y, w, h, fill=1, stroke=0)
        c.setFillColor(colors.grey)
        c.setFont("Helvetica", 24)
        c.drawCentredString(x + w / 2, y + h / 2, f"Missing: {img_path.name}")
        return
    with Image.open(img_path) as img:
        iw, ih = img.size
    scale = min(w / iw, h / ih)
    dw, dh = iw * scale, ih * scale
    ox = x + (w - dw) / 2
    oy = y + (h - dh) / 2
    if border:
        c.setStrokeColor(colors.HexColor("#333333"))
        c.setLineWidth(2)
        c.rect(x, y, w, h, fill=0, stroke=1)
    c.drawImage(ImageReader(str(img_path)), ox, oy, dw, dh, preserveAspectRatio=True, mask="auto")


def draw_title_block(c: canvas.Canvas, font: str, board_id: str, title: str, subtitle: str = "") -> None:
    y_top = PAGE_H - MARGIN
    c.setFillColor(colors.HexColor("#1A1A2E"))
    c.setFont(font, 52)
    c.drawString(MARGIN, y_top - 58, f"{board_id} · {title}")
    c.setFillColor(colors.HexColor("#333355"))
    c.setFont(font, 34)
    c.drawString(MARGIN, y_top - 108, "京张智脉共生带城市设计方案")
    if subtitle:
        c.setFillColor(colors.HexColor("#555577"))
        c.setFont(font, 26)
        c.drawString(MARGIN, y_top - 148, subtitle)
    c.setStrokeColor(colors.HexColor("#1A1A2E"))
    c.setLineWidth(3)
    c.line(MARGIN, PAGE_H - TITLE_H, PAGE_W - MARGIN, PAGE_H - TITLE_H)


def draw_legend(c: canvas.Canvas, font: str, x: float, y: float, w: float, h: float) -> None:
    c.setFillColor(colors.white)
    c.setStrokeColor(colors.HexColor("#333333"))
    c.setLineWidth(1.5)
    c.rect(x, y, w, h, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#1A1A2E"))
    c.setFont(font, 24)
    c.drawString(x + 16, y + h - 36, "图例 Legend")
    row_h = (h - 50) / len(LEGEND_ITEMS)
    for i, (color, label) in enumerate(LEGEND_ITEMS):
        ry = y + h - 58 - (i + 1) * row_h + row_h / 2 - 8
        c.setFillColor(color)
        c.rect(x + 20, ry, 28, 18, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#222222"))
        c.setFont(font, 20)
        c.drawString(x + 58, ry + 2, label)


def draw_warning_and_footer(c: canvas.Canvas, font: str, compile_date: str) -> None:
    fy = MARGIN
    warn_h = 72
    c.setFillColor(colors.HexColor("#FFF8E1"))
    c.setStrokeColor(colors.HexColor("#E65100"))
    c.setLineWidth(2)
    c.rect(MARGIN, fy + FOOTER_H - warn_h - 12, PAGE_W - 2 * MARGIN, warn_h, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#BF360C"))
    c.setFont(font, 22)
    c.drawString(MARGIN + 16, fy + FOOTER_H - warn_h + 24, BOUNDARY_WARNING)

    c.setFillColor(colors.HexColor("#444444"))
    c.setFont(font, 18)
    c.drawString(MARGIN, fy + 48, SOURCE_ATTRIBUTION)
    c.drawRightString(PAGE_W - MARGIN, fy + 48, f"编制日期 Compile date: {compile_date}")
    c.drawString(MARGIN, fy + 16, "编制：lijiaaaaa-bot · Cursor Agent · 京张智脉共生带 formal submission")


def draw_content_bottom(c: canvas.Canvas) -> float:
    return MARGIN + FOOTER_H


def draw_content_top(c: canvas.Canvas) -> float:
    return PAGE_H - TITLE_H - 16


def page_a0_01(c: canvas.Canvas, font: str, root: Path, compile_date: str) -> None:
    draw_title_block(
        c, font, "A0-01", "总体设计结构",
        "三核 + 京张慢行脊 + 10 场景节点 · 三层范围空间总览",
    )
    bottom = draw_content_bottom(c)
    top = draw_content_top(c)
    usable_h = top - bottom
    usable_w = PAGE_W - 2 * MARGIN

    legend_w = 520
    inset_w = 640
    hero_w = usable_w - inset_w - 24
    hero_h = usable_h - 16

    hero_x = MARGIN
    hero_y = bottom + 8
    draw_image_fit(c, root / "assets/figures/site-overview.png", hero_x, hero_y, hero_w, hero_h)

    inset_x = MARGIN + hero_w + 24
    inset_h = hero_h * 0.55
    draw_image_fit(c, root / "assets/figures/framework.png", inset_x, hero_y + hero_h - inset_h, inset_w, inset_h)

    legend_h = hero_h - inset_h - 20
    draw_legend(c, font, inset_x, hero_y, inset_w, legend_h)

    draw_warning_and_footer(c, font, compile_date)
    c.showPage()


def page_single_figure(
    c: canvas.Canvas,
    font: str,
    root: Path,
    board_id: str,
    title: str,
    subtitle: str,
    figure: str,
    compile_date: str,
    extra_lines: list[str] | None = None,
) -> None:
    draw_title_block(c, font, board_id, title, subtitle)
    bottom = draw_content_bottom(c)
    top = draw_content_top(c)
    draw_image_fit(c, root / figure, MARGIN, bottom + 8, PAGE_W - 2 * MARGIN, top - bottom - 16)
    if extra_lines:
        c.setFillColor(colors.HexColor("#333355"))
        c.setFont(font, 22)
        ey = bottom + FOOTER_H - 90
        for line in extra_lines:
            c.drawString(MARGIN, ey, line)
            ey -= 28
    draw_warning_and_footer(c, font, compile_date)
    c.showPage()


def page_key_areas(c: canvas.Canvas, font: str, root: Path, compile_date: str) -> None:
    draw_title_block(c, font, "A0-05", "三处重点区域详细设计", "索引 + 分区放大详图")
    bottom = draw_content_bottom(c)
    top = draw_content_top(c)
    usable_h = top - bottom
    usable_w = PAGE_W - 2 * MARGIN

    index_h = usable_h * 0.38
    detail_h = usable_h - index_h - 20
    draw_image_fit(c, root / "assets/figures/key-areas.png", MARGIN, top - index_h, usable_w, index_h)

    detail_w = (usable_w - 40) / 3
    for i, name in enumerate(["key-area-001.png", "key-area-002.png", "key-area-003.png"]):
        dx = MARGIN + i * (detail_w + 20)
        draw_image_fit(c, root / "assets/figures" / name, dx, bottom + 8, detail_w, detail_h - 8)

    draw_warning_and_footer(c, font, compile_date)
    c.showPage()


def page_ai_scenarios(c: canvas.Canvas, font: str, compile_date: str) -> None:
    draw_title_block(c, font, "A0-06", "AI 场景与实施运营", "10 场景卡 + 治理机制")
    bottom = draw_content_bottom(c)
    top = draw_content_top(c)

    scenarios = [
        ("01", "开源发布站", "众智园 · 标准治理展示"),
        ("02", "智能体沙盒", "安全治理 · 合规测试"),
        ("03", "慢行诊断屏", "AI+ 交通 · 步行可达"),
        ("04", "人才管家驿站", "原点社区 · 校企转化"),
        ("05", "安全治理剧场", "全栈创新 · 政策对话"),
        ("06", "校企转化客厅", "成果发布 · 开源协作"),
        ("07", "数据要素剧场", "大钟寺 · 国际路演"),
        ("08", "低碳算力廊", "端侧算力 · 绿色算力"),
        ("09", "京张记忆站", "铁路文脉 · 朝圣地标"),
        ("10", "全球 AI 活动周", "四季活动 · 国际传播"),
    ]

    cols = 2
    rows = 5
    cell_w = (PAGE_W - 2 * MARGIN - 20) / cols
    cell_h = (top - bottom - 20) / rows
    for idx, (num, name, loc) in enumerate(scenarios):
        col = idx % cols
        row = idx // cols
        x = MARGIN + col * (cell_w + 20)
        y = top - (row + 1) * cell_h
        c.setFillColor(colors.HexColor("#F8F9FC"))
        c.setStrokeColor(colors.HexColor("#4A90D9"))
        c.setLineWidth(1.5)
        c.rect(x, y, cell_w - 10, cell_h - 8, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#1A1A2E"))
        c.setFont(font, 28)
        c.drawString(x + 18, y + cell_h - 52, f"场景 {num} · {name}")
        c.setFillColor(colors.HexColor("#555577"))
        c.setFont(font, 22)
        c.drawString(x + 18, y + cell_h - 88, loc)

    draw_warning_and_footer(c, font, compile_date)
    c.showPage()


def build_pdf(submission_dir: Path, out_path: Path) -> None:
    font = register_cjk_font()
    compile_date = date.today().isoformat()
    c = canvas.Canvas(str(out_path), pagesize=(PAGE_W, PAGE_H))
    c.setTitle("京张智脉共生带城市设计方案 - A0 展板")
    c.setAuthor("京张智脉共生带设计团队")

    page_a0_01(c, font, submission_dir, compile_date)

    page_single_figure(
        c, font, submission_dir,
        "A0-02", "用地与城市更新", "用地布局与更新项目清单摘要",
        "assets/figures/land-use-structure.png", compile_date,
        ["更新项目 JZ-01~06：大钟寺站城一体、清河界面、原点社区、众智园全栈创新等"],
    )
    page_single_figure(
        c, font, submission_dir,
        "A0-03", "交通、轨道、慢行与市政支撑", "道路网络与蓝绿慢行复合系统",
        "assets/figures/mobility-bluegreen.png", compile_date,
    )
    page_single_figure(
        c, font, submission_dir,
        "A0-04", "京张遗址公园活力带与蓝绿公共空间", "遗址走廊 + 蓝绿系统",
        "assets/figures/mobility-bluegreen.png", compile_date,
        ["京张铁路遗址公园为一带主轴；清河—小月河蓝绿廊道组织慢行与雨洪韧性"],
    )
    page_key_areas(c, font, submission_dir, compile_date)
    page_ai_scenarios(c, font, compile_date)
    page_single_figure(
        c, font, submission_dir,
        "A0-07", "指标复核与合规响应", "metrics + 矩阵摘要",
        "assets/figures/metrics-evidence.png", compile_date,
    )

    c.save()


def render_preview(pdf_path: Path, preview_path: Path) -> None:
    import shutil
    import subprocess

    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        return
    prefix = preview_path.with_suffix("")
    subprocess.run(
        [pdftoppm, "-png", "-f", "1", "-l", "1", "-r", "120", str(pdf_path), str(prefix)],
        check=True,
        capture_output=True,
    )
    generated = Path(f"{prefix}-1.png")
    if generated.is_file():
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        generated.replace(preview_path)


def update_manifest(submission_dir: Path) -> None:
    manifest_path = submission_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for item in manifest.get("files", []):
        rel = item.get("path")
        if not rel or rel == "manifest.json":
            continue
        path = submission_dir / rel
        if path.is_file():
            item["sha256"] = sha256(path)
    manifest["generated_at"] = date.today().isoformat() + "T12:00:00Z"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission_dir", type=Path, help="Path to submission package root")
    parser.add_argument("--preview", action="store_true", help="Also write drawings/a0-01-preview.png")
    parser.add_argument("--update-manifest", action="store_true", help="Refresh sha256 in manifest.json")
    args = parser.parse_args()

    root = args.submission_dir.resolve()
    out_pdf = root / "drawings" / "a0-boards.pdf"
    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    old_size = out_pdf.stat().st_size if out_pdf.is_file() else 0
    build_pdf(root, out_pdf)
    new_size = out_pdf.stat().st_size
    print(f"Wrote {out_pdf} ({old_size} -> {new_size} bytes)")

    if args.preview:
        preview = root / "assets" / "figures" / "a0-01-preview.png"
        render_preview(out_pdf, preview)
        if preview.is_file():
            print(f"Wrote preview {preview} ({preview.stat().st_size} bytes)")

    if args.update_manifest:
        update_manifest(root)
        print("Updated manifest.json sha256")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
