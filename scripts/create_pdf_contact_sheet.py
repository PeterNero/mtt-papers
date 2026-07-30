"""Create a numbered contact sheet from rendered PDF page images."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("image_dir", type=Path)
    parser.add_argument("--pattern", default="page-*.png")
    parser.add_argument("--output", default="contact.png")
    parser.add_argument("--thumb-width", type=int, default=500)
    parser.add_argument("--thumb-height", type=int, default=690)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = sorted(args.image_dir.glob(args.pattern))
    if not files:
        raise SystemExit(f"no images match {args.pattern!r} in {args.image_dir}")

    thumbs = [
        ImageOps.contain(
            Image.open(path).convert("RGB"),
            (args.thumb_width, args.thumb_height),
        )
        for path in files
    ]
    rows = (len(thumbs) + 1) // 2
    row_heights = [
        max(
            thumbs[2 * row].height,
            thumbs[2 * row + 1].height if 2 * row + 1 < len(thumbs) else 0,
        )
        for row in range(rows)
    ]

    gutter = 20
    column_width = args.thumb_width + gutter
    canvas = Image.new(
        "RGB",
        (2 * column_width - gutter, sum(row_heights) + gutter * (rows + 1)),
        "white",
    )
    draw = ImageDraw.Draw(canvas)

    for index, page in enumerate(thumbs):
        row, column = divmod(index, 2)
        x = column * column_width
        y = gutter + sum(row_heights[:row]) + row * gutter
        canvas.paste(page, (x, y))
        draw.text(
            (x + 4, y + 4),
            str(index + 1),
            fill="red",
            stroke_width=2,
            stroke_fill="white",
        )

    output = args.image_dir / args.output
    canvas.save(output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
