#!/usr/bin/env python3
"""Render PDF pages to numbered PNG files with Poppler."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from pypdf import PdfReader


def render_pdf(source: Path, output_dir: Path, dpi: int, first: int, last: int | None) -> list[Path]:
    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        raise SystemExit("pdftoppm not found on PATH; install Poppler first")

    reader = PdfReader(source)
    if reader.is_encrypted:
        raise SystemExit("Encrypted PDFs require decryption before rendering")
    page_count = len(reader.pages)
    end = page_count if last is None else min(last, page_count)
    if first < 1 or end < first:
        raise SystemExit(f"Invalid page range: {first}-{end} for {page_count} pages")

    output_dir.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="aos-pdf-render-") as tmp:
        prefix = Path(tmp) / "page"
        command = [
            pdftoppm,
            "-png",
            "-r",
            str(dpi),
            "-f",
            str(first),
            "-l",
            str(end),
            str(source),
            str(prefix),
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(f"PDF rendering failed:\n{result.stdout}\n{result.stderr}")
        for rendered in sorted(Path(tmp).glob("page-*.png"), key=lambda p: int(p.stem.rsplit("-", 1)[1])):
            page_number = int(rendered.stem.rsplit("-", 1)[1])
            destination = output_dir / f"page-{page_number:03d}.png"
            shutil.copy2(rendered, destination)
            created.append(destination)
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--first-page", type=int, default=1)
    parser.add_argument("--last-page", type=int)
    args = parser.parse_args()

    source = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Input PDF not found: {source}")
    if args.dpi < 36 or args.dpi > 600:
        raise SystemExit("DPI must be between 36 and 600")

    created = render_pdf(source, output_dir, args.dpi, args.first_page, args.last_page)
    print(f"Rendered {len(created)} pages to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
