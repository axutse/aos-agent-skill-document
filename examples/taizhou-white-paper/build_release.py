#!/usr/bin/env python3
"""Build, sanitize, render, and package the public TAIZHOU DOCX/PDF example."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
WORD_SCRIPTS = ROOT / "plugins" / "aos-agent-skill-document" / "skills" / "aos-author-word" / "scripts"
PDF_SCRIPTS = ROOT / "plugins" / "aos-agent-skill-document" / "skills" / "aos-process-pdf" / "scripts"


def run(*arguments: object) -> None:
    subprocess.run([sys.executable, *(str(item) for item in arguments)], check=True)


def build(output_dir: Path, qa_dir: Path, dpi: int) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    qa_dir.mkdir(parents=True, exist_ok=True)
    final_docx = output_dir / "TAIZHOU品牌企业白皮书_示例版.docx"
    final_pdf = output_dir / "TAIZHOU品牌企业白皮书_示例版.pdf"
    contact_sheet = output_dir / "TAIZHOU品牌企业白皮书_示例版_联系表.jpg"

    with tempfile.TemporaryDirectory(prefix="taizhou-example-build-") as tmp:
        temp_root = Path(tmp)
        source_docx = temp_root / "source.docx"
        high_fidelity_docx = temp_root / "high-fidelity.docx"
        docx_render = qa_dir / "docx-render"
        pdf_render = qa_dir / "pdf-render"

        run(HERE / "generate_example.py", "--brief", HERE / "brief.json", "--output", source_docx)
        run(WORD_SCRIPTS / "set_docx_high_fidelity.py", source_docx, high_fidelity_docx)
        run(WORD_SCRIPTS / "scrub_docx_metadata.py", high_fidelity_docx, final_docx, "--author", "TAIZHOU")
        run(WORD_SCRIPTS / "render_docx.py", final_docx, "--output-dir", docx_render, "--dpi", dpi, "--emit-pdf")
        converted_pdf = docx_render / f"{final_docx.stem}.pdf"
        run(
            PDF_SCRIPTS / "scrub_pdf_metadata.py",
            converted_pdf,
            final_pdf,
            "--title",
            "TAIZHOU品牌企业白皮书",
            "--author",
            "TAIZHOU",
            "--subject",
            "Public multi-brand fashion-enterprise example",
            "--keywords",
            "TAIZHOU, WANMIAN, GEERNA, UIUP",
        )
        run(PDF_SCRIPTS / "render_pdf.py", final_pdf, "--output-dir", pdf_render, "--dpi", dpi)
        run(
            PDF_SCRIPTS / "make_contact_sheet.py",
            str(pdf_render / "page-*.png"),
            "--output",
            contact_sheet,
            "--columns",
            4,
            "--thumb-width",
            320,
        )
        run(WORD_SCRIPTS / "inspect_docx.py", final_docx, "--json")
        run(PDF_SCRIPTS / "inspect_pdf.py", final_pdf, "--json")

    print(f"DOCX: {final_docx}")
    print(f"PDF: {final_pdf}")
    print(f"Contact sheet: {contact_sheet}")
    print(f"QA pages: {qa_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=HERE / "output")
    parser.add_argument("--qa-dir", type=Path, required=True)
    parser.add_argument("--dpi", type=int, default=130)
    args = parser.parse_args()
    if args.dpi < 72 or args.dpi > 300:
        raise SystemExit("DPI must be between 72 and 300")
    build(args.output_dir.expanduser().resolve(), args.qa_dir.expanduser().resolve(), args.dpi)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
