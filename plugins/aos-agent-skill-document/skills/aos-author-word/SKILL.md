---
name: aos-author-word
description: Create, edit, inspect, convert, and visually verify professional Microsoft Word DOCX files while preserving editable structure. Use when Codex needs to author or locally revise reports, white papers, proposals, manuals, policies, brand books, tables, images, sections, headers, footers, high-fidelity image settings, DOCX-to-PDF conversion, metadata cleanup, or final page-by-page Word rendering QA. Prefer this skill when DOCX is the primary artifact and full publication orchestration is unnecessary.
---

# AOS Word Authoring

Use semantic Word structure and complete visual verification. Read [references/docx-workflow.md](references/docx-workflow.md) before complex authoring or section work.

Treat DOCX editability and preservation of existing structure as the primary contract. Do not rebuild an entire document when the user requests localized edits, and do not claim complete visual QA when LibreOffice rendering is unavailable.

## Workflow

1. Preserve the original file and make localized changes for edit requests.
2. Use `python-docx` for normal authoring and targeted OOXML only where required.
3. Use real paragraph styles, list definitions, sections, headers, footers, and native tables.
4. Set explicit page geometry, margins, image size, and table widths instead of relying on defaults.
5. Run `set_docx_high_fidelity.py` before final rendering.
6. Run `inspect_docx.py` and resolve unexpected metadata, sections, media, or settings.
7. Render the DOCX with `render_docx.py` and inspect every PNG page.
8. Re-render after each layout-sensitive change.
9. Run `scrub_docx_metadata.py` before external publication when personal metadata is not required.

## Commands

```bash
python scripts/inspect_docx.py input.docx --json
python scripts/set_docx_high_fidelity.py input.docx output.docx
python scripts/scrub_docx_metadata.py input.docx public.docx
python scripts/render_docx.py public.docx --output-dir render --emit-pdf
python scripts/lo_convert_to_pdf.py public.docx output.pdf
```

## Quality rules

- Do not deliver a DOCX solely because text extraction succeeds.
- Inspect every rendered page for clipping, overlaps, glyph substitution, broken tables, image blur, page breaks, headers, footers, and numbering.
- Keep tables editable and images proportional.
- Remove comments, tracked changes, private metadata, and placeholders unless the user requests them.
- If LibreOffice is unavailable, perform structural QA and disclose that render QA could not run.
