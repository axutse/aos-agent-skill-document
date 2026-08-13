---
name: aos-process-pdf
description: Create, inspect, render, compare, clean, and visually verify professional PDF files while preserving fixed-layout fidelity. Use when Codex needs print-ready exports, PDF metadata and page-geometry inspection, page rendering, contact sheets, structural checks, public-release QA, or validation of PDF output converted from Word. Prefer this skill when PDF is the primary artifact or when the user requests an audit before any modification.
---

# AOS PDF Processing

Preserve vector content and verify both document structure and rendered appearance. Read [references/pdf-workflow.md](references/pdf-workflow.md) before complex PDF work.

Treat fixed-layout integrity and full-page inspection as the primary contract. Do not infer visual correctness from extracted text, and do not modify an audit-only input until the user approves the reported repair scope.

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
