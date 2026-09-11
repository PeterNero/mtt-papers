"""Render full changed manuscripts and small, numbered review sheets."""
from pathlib import Path
import argparse
import json
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paper_ids", nargs="+")
    args = parser.parse_args()
    records = []
    for pid in args.paper_ids:
        output = ROOT / "tmp" / "revision-review" / pid
        output.mkdir(parents=True, exist_ok=True)
        document = fitz.open(ROOT / "papers" / pid / "main.pdf")
        images = []
        for number, page in enumerate(document, 1):
            image = output / f"page-{number:03}.png"
            page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2)).save(image)
            images.append(image)
        for start in range(0, len(images), 8):
            sheet = Image.new("RGB", (1680, 1210), "#cccccc")
            draw = ImageDraw.Draw(sheet)
            for j, image in enumerate(images[start:start + 8]):
                thumb = Image.open(image).convert("RGB")
                thumb.thumbnail((410, 570))
                x, y = (j % 4) * 420, (j // 4) * 605
                sheet.paste(thumb, (x, y + 25))
                draw.text((x + 5, y + 5), f"Page {start + j + 1}", fill="black")
            sheet.save(output / f"sheet-{start // 8 + 1:02}.png")
        records.append({"paper_id": pid, "pages": len(document), "rendered_all_pages": True})
    (ROOT / "tmp/revision-review/manifest.json").write_text(json.dumps(records, indent=2))
    print(json.dumps(records))


if __name__ == "__main__":
    main()
