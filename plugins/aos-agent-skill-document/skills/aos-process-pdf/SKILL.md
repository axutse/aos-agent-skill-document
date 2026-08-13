---
name: aos-process-pdf
description: Create, inspect, render, compare, and visually verify professional PDF files. Use when Codex needs fixed-layout reports, print-ready exports, PDF metadata and page-geometry inspection, page rendering, contact sheets, PDF QA, or validation of PDF output converted from Word.
---

# AOS PDF Processing

Preserve vector content and verify both document structure and rendered appearance. Read [references/pdf-workflow.md](references/pdf-workflow.md) before complex PDF work.

## Workflow

1. Inspect page count, dimensions, rotation, encryption, metadata, forms, links, and image usage.
2. Use ReportLab for deterministic creation and pypdf for structural operations.
3. Preserve vector content unless rasterization is explicitly required.
4. Render the complete final PDF with Poppler.
5. Inspect every page at readable zoom; use a contact sheet only for overview.
6. Reopen and structurally verify any edited or generated PDF.
7. Scrub metadata before public release when personal metadata is not required.

## Commands

```bash
python scripts/inspect_pdf.py input.pdf --json
python scripts/scrub_pdf_metadata.py input.pdf public.pdf
python scripts/render_pdf.py public.pdf --output-dir render --dpi 200
python scripts/make_contact_sheet.py 'render/page-*.png' --output contact-sheet.jpg
```

## Quality rules

- Do not approve a PDF from extracted text alone.
- Confirm page count, dimensions, metadata policy, links/forms where applicable, and successful reopening.
- Inspect every page for clipping, overlaps, missing glyphs, incorrect page boxes, blur, or broken tables.
- Keep temporary PNGs outside final delivery unless requested.
- Use ASCII hyphens in generated technical text when renderer compatibility is uncertain.
