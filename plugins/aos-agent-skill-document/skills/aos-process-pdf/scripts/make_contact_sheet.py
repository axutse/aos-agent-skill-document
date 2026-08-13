#!/usr/bin/env python3
import argparse
import glob
import math
from pathlib import Path
from PIL import Image, ImageDraw


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a labeled contact sheet from page images.")
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--output", required=True)
    parser.add_argument("--columns", type=int, default=5)
    parser.add_argument("--thumb-width", type=int, default=280)
    args = parser.parse_args()

    files = []
    for pattern in args.inputs:
        matches = sorted(glob.glob(pattern))
        files.extend(matches or [pattern])
    files = [Path(p) for p in files if Path(p).is_file()]
    if not files:
        raise SystemExit("No input images found")

    thumbs = []
    label_h = 28
    for p in files:
        image = Image.open(p).convert("RGB")
        ratio = args.thumb_width / image.width
        height = max(1, int(image.height * ratio))
        image = image.resize((args.thumb_width, height), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (args.thumb_width, height + label_h), "white")
        canvas.paste(image, (0, 0))
        ImageDraw.Draw(canvas).text((6, height + 5), p.name, fill="black")
        thumbs.append(canvas)

    rows = math.ceil(len(thumbs) / args.columns)
    cell_h = max(t.height for t in thumbs)
    sheet = Image.new("RGB", (args.columns * args.thumb_width, rows * cell_h), "#DDDDDD")
    for i, thumb in enumerate(thumbs):
        x = (i % args.columns) * args.thumb_width
        y = (i // args.columns) * cell_h
        sheet.paste(thumb, (x, y))
    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=92)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
