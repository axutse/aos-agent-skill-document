# DOCX Workflow

## Contents

1. Authoring model
2. Styles and sections
3. Images and diagrams
4. Tables
5. Headers, footers, and navigation
6. High-fidelity settings
7. Rendering and QA

## 1. Authoring model

Use `python-docx` for paragraphs, runs, styles, tables, images, headers, footers, and section configuration. Use OOXML only when the library does not expose a needed feature.

Create semantic styles for:

- Cover title
- Section number
- Heading 1 / 2 / 3
- Thesis or conclusion text
- Body text
- Caption
- Table header and body
- Data labels

Do not simulate spacing with repeated blank paragraphs.

## 2. Styles and sections

Use new sections only for:

- Portrait/landscape changes
- Margin changes
- Different headers/footers
- Page-number restarts

Keep ordinary consecutive pages in the same section.

Use `keep_with_next` for headings and prevent table rows from splitting when readability requires it.

## 3. Images and diagrams

Before inserting an image:

1. Inspect pixel dimensions.
2. Crop unused internal whitespace.
3. Confirm the intended printed size.
4. Estimate effective DPI.
5. Insert proportionally.

Prefer native text and tables for information that must remain sharp. If using raster diagrams, export at 300-400 DPI at the final intended size.

For Chinese documents, select an installed CJK font explicitly. The bundled renderer discovers the Codex LibreOffice fontconfig file when present; on CI, install a CJK package such as Noto Sans CJK before rendering. Never commit or redistribute commercial font files.

## 4. Tables

Use native Word tables. Keep borders minimal. Repeat header rows on multi-page tables. Avoid tiny type. Split complex matrices when necessary.

## 5. Headers, footers, and navigation

Use understated headers and footers. Hide or simplify them on covers, section openers, and full-bleed visual pages. Use real heading styles so Word navigation and TOC generation work.

## 6. High-fidelity settings

Run:

```bash
python scripts/set_docx_high_fidelity.py input.docx output.docx
```

This adds Word settings that discourage image compression and set a high default image DPI.

## 7. Rendering and QA

Render with LibreOffice:

```bash
python scripts/render_docx.py input.docx --output-dir render --emit-pdf
```

Inspect every page. Build a contact sheet only for overview; inspect suspicious pages individually at full resolution.
