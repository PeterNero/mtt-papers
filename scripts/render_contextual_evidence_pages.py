#!/usr/bin/env python3
"""Render the changed evidence pages and make review contact sheets."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
MAP_PATH = ROOT / "catalog" / "contextual-evidence-map.json"
DEFAULT_OUTPUT = ROOT / "tmp" / "pdfs" / "contextual-evidence-review"
HEADING = "Computational Evidence and Reproducibility"
TERMINAL = "No imported row changes theorem ownership"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def resolve_executable(value: str | None) -> str:
    if value:
        path = Path(value).resolve()
        if path.is_file():
            return str(path)
        raise RuntimeError(f"pdftoppm does not exist: {path}")
    resolved = shutil.which("pdftoppm")
    if not resolved:
        raise RuntimeError("pdftoppm is unavailable")
    return resolved


def evidence_span(pdf_path: Path) -> tuple[int, int, int]:
    reader = PdfReader(pdf_path)
    texts = [page.extract_text() or "" for page in reader.pages]
    starts = [
        index
        for index, text in enumerate(texts)
        if HEADING in text
    ]
    if len(starts) != 1:
        raise RuntimeError(
            f"{pdf_path}: expected one evidence heading, found {len(starts)}"
        )
    start = starts[0]
    ends = [
        index
        for index, text in enumerate(texts[start:], start)
        if TERMINAL in text
    ]
    if not ends:
        raise RuntimeError(
            f"{pdf_path}: evidence terminal statement is absent"
        )
    return start + 1, ends[0] + 1, len(texts)


def render_page(
    pdftoppm: str,
    pdf_path: Path,
    page: int,
    output_path: Path,
    dpi: int,
) -> None:
    prefix = output_path.with_suffix("")
    command = [
        pdftoppm,
        "-f",
        str(page),
        "-l",
        str(page),
        "-singlefile",
        "-png",
        "-r",
        str(dpi),
        str(pdf_path),
        str(prefix),
    ]
    completed = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if completed.returncode:
        raise RuntimeError(
            f"render failed for {pdf_path}, page {page}: "
            f"{completed.stdout.strip()}"
        )
    if not output_path.is_file():
        raise RuntimeError(f"renderer did not create {output_path}")


def review_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
    ]
    for path in candidates:
        if path.is_file():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def make_contact_sheets(
    items: list[dict[str, Any]],
    output: Path,
    sheet_size: int = 4,
) -> list[str]:
    contact_paths: list[str] = []
    font = review_font(15)
    thumb_width = 440
    thumb_height = 623
    label_height = 48
    margin = 18
    columns = 2
    rows = 2
    sheet_width = margin + columns * (thumb_width + margin)
    sheet_height = margin + rows * (
        label_height + thumb_height + margin
    )
    for sheet_index in range(0, len(items), sheet_size):
        batch = items[sheet_index : sheet_index + sheet_size]
        sheet = Image.new("RGB", (sheet_width, sheet_height), "white")
        draw = ImageDraw.Draw(sheet)
        for index, item in enumerate(batch):
            row, column = divmod(index, columns)
            x = margin + column * (thumb_width + margin)
            y = margin + row * (label_height + thumb_height + margin)
            label = (
                f"{item['paper_id'][:48]}\n"
                f"PDF page {item['page']} of {item['total_pages']}"
            )
            draw.multiline_text(
                (x, y),
                label,
                fill="black",
                font=font,
                spacing=2,
            )
            with Image.open(item["image"]) as page_image:
                page = page_image.convert("RGB")
                page.thumbnail((thumb_width, thumb_height))
                page_x = x + (thumb_width - page.width) // 2
                page_y = y + label_height
                sheet.paste(page, (page_x, page_y))
        contact_path = (
            output
            / f"contact-{sheet_index // sheet_size + 1:02d}.png"
        )
        sheet.save(contact_path)
        contact_paths.append(str(contact_path.resolve()))
    return contact_paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdftoppm")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dpi", type=int, default=120)
    args = parser.parse_args()

    try:
        pdftoppm = resolve_executable(args.pdftoppm)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    document = read_json(MAP_PATH)
    output = args.output.resolve()
    pages_output = output / "pages"
    pages_output.mkdir(parents=True, exist_ok=True)

    items: list[dict[str, Any]] = []
    failures: list[str] = []
    for paper_id in sorted(document["papers"]):
        pdf_path = PAPERS / paper_id / "main.pdf"
        try:
            start, end, total_pages = evidence_span(pdf_path)
            for page in range(start, end + 1):
                image_path = pages_output / f"{paper_id}-p{page}.png"
                render_page(
                    pdftoppm,
                    pdf_path,
                    page,
                    image_path,
                    args.dpi,
                )
                items.append(
                    {
                        "paper_id": paper_id,
                        "page": page,
                        "total_pages": total_pages,
                        "image": str(image_path.resolve()),
                    }
                )
        except Exception as exc:
            failures.append(f"{paper_id}: {exc}")

    contact_sheets = make_contact_sheets(items, output)
    manifest = {
        "papers": len(document["papers"]),
        "rendered_pages": len(items),
        "contact_sheets": contact_sheets,
        "failures": failures,
        "items": items,
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "papers": len(document["papers"]),
                "rendered_pages": len(items),
                "contact_sheets": len(contact_sheets),
                "failures": len(failures),
            },
            indent=2,
        )
    )
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
