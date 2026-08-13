#!/usr/bin/env python3
"""Render a DOCX to page PNGs through LibreOffice and Poppler."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from pypdf import PdfReader


def bundled_fontconfig(executable: str) -> Path | None:
    launcher = Path(executable).expanduser().resolve()
    for parent in (launcher.parent, *launcher.parents):
        candidates = [
            parent / "Resources" / "fontconfig" / "fonts.conf",
            parent / "native" / "libreoffice-headless" / "libreoffice" / "LibreOfficeDev.app" / "Contents" / "Resources" / "fontconfig" / "fonts.conf",
        ]
        for candidate in candidates:
            if candidate.is_file():
                return candidate
    return None


def convert_to_pdf(source: Path, output_pdf: Path) -> None:
    libreoffice = shutil.which("libreoffice") or shutil.which("soffice")
    if not libreoffice:
        raise SystemExit("LibreOffice/soffice not found on PATH")
    with tempfile.TemporaryDirectory(prefix="aos-docx-convert-") as tmp:
        temp_root = Path(tmp)
        home = temp_root / "home"
        profile = temp_root / "profile"
        home.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["HOME"] = str(home)
        fontconfig = bundled_fontconfig(libreoffice)
        if fontconfig and "FONTCONFIG_FILE" not in env:
            env["FONTCONFIG_FILE"] = str(fontconfig)
        command = [
            libreoffice,
            "--headless",
            f"-env:UserInstallation={profile.as_uri()}",
            "--convert-to",
            "pdf",
            "--outdir",
            str(temp_root),
            str(source),
        ]
        result = subprocess.run(command, env=env, capture_output=True, text=True)
        generated = temp_root / f"{source.stem}.pdf"
        if result.returncode != 0 or not generated.is_file():
            raise SystemExit(f"LibreOffice conversion failed:\n{result.stdout}\n{result.stderr}")
        shutil.copy2(generated, output_pdf)


def render_pdf(source: Path, output_dir: Path, dpi: int) -> list[Path]:
    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        raise SystemExit("pdftoppm not found on PATH; install Poppler first")
    page_count = len(PdfReader(source).pages)
    created: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="aos-docx-render-") as tmp:
        prefix = Path(tmp) / "page"
        command = [pdftoppm, "-png", "-r", str(dpi), str(source), str(prefix)]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(f"Page rendering failed:\n{result.stdout}\n{result.stderr}")
        rendered = sorted(Path(tmp).glob("page-*.png"), key=lambda p: int(p.stem.rsplit("-", 1)[1]))
        if len(rendered) != page_count:
            raise SystemExit(f"Expected {page_count} rendered pages, found {len(rendered)}")
        for image in rendered:
            page_number = int(image.stem.rsplit("-", 1)[1])
            destination = output_dir / f"page-{page_number:03d}.png"
            shutil.copy2(image, destination)
            created.append(destination)
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--dpi", type=int, default=170)
    parser.add_argument("--emit-pdf", action="store_true")
    args = parser.parse_args()

    source = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Input DOCX not found: {source}")
    if args.dpi < 36 or args.dpi > 600:
        raise SystemExit("DPI must be between 36 and 600")
    output_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="aos-docx-pdf-") as tmp:
        temp_pdf = Path(tmp) / f"{source.stem}.pdf"
        convert_to_pdf(source, temp_pdf)
        created = render_pdf(temp_pdf, output_dir, args.dpi)
        if args.emit_pdf:
            shutil.copy2(temp_pdf, output_dir / f"{source.stem}.pdf")
    print(f"Rendered {len(created)} pages to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
