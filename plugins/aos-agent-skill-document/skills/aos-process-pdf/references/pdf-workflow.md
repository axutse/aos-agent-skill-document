# PDF Workflow

## Contents

1. Inspect
2. Choose the operation
3. Edit or create
4. Render
5. Compare
6. Deliver

## 1. Inspect

Run:

```bash
python scripts/inspect_pdf.py input.pdf
```

Check page count, page sizes, metadata, encryption, forms, and image-heavy pages.

## 2. Choose the operation

Use:

- PyMuPDF for rendering, page manipulation, annotations, and redaction workflows
- pypdf for merge, split, metadata, and page-box operations
- ReportLab for deterministic programmatic creation
- DOCX-first authoring for long text-heavy business documents

## 3. Edit or create

Preserve vector content whenever possible. Do not rasterize the entire PDF unless the task explicitly requires it.

## 4. Render

```bash
python scripts/render_pdf.py input.pdf --output-dir render --dpi 200
```

Use 300 DPI for print-sensitive inspection.

## 5. Compare

For edited documents, render both versions and compare representative pages or use an image-diff tool. Check page boxes, fonts, links, forms, and hidden content when relevant.

## 6. Deliver

Remove temporary files from the deliverable directory. Deliver only the requested final artifact unless the user asks for QA material.
