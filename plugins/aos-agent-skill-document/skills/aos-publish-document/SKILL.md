---
name: aos-publish-document
description: Coordinate end-to-end professional document publishing across editable Word and fixed PDF deliverables. Use when Codex needs to turn source materials into publication-ready reports, white papers, proposals, manuals, brand books, or other business documents through content planning, DOCX authoring, PDF conversion, metadata review, and page-by-page visual QA. Prefer this orchestration skill when the request spans both content structure and final deliverables, especially when both DOCX and PDF are required.
---

# AOS Document Publishing

Produce polished documents through a deterministic `plan -> author -> render -> inspect -> revise -> verify` loop.

## Position the work

Act as a document publishing orchestrator, not as a replacement for Word, Acrobat, factual review, legal review, or rights clearance. Combine Codex reasoning with local document tools, preserve editability where required, and treat rendered-page verification as part of the deliverable rather than an optional preview.

Read [references/positioning-and-routing.md](references/positioning-and-routing.md) when selecting among the three AOS skills, explaining scope to the user, or defining the input and output contract.

## Route the work

- Use `$aos-author-word` when editability, semantic styles, tracked document structure, or DOCX delivery matters.
- Use `$aos-process-pdf` for fixed-layout creation, PDF inspection, metadata checks, rendering, page operations, or print-ready verification.
- Use both when the user requests DOCX and PDF: author the DOCX first, verify it, export the PDF, and verify the PDF again.
- Do not invoke all three skills mechanically. Use this skill as the orchestration entry point and load the format-specific workflow only when the task requires it.

## Required workflow

1. Inspect all supplied sources before drafting.
2. Confirm format, page size, language, editability, style, and delivery requirements from context.
3. Build a section and page plan for long documents.
4. Preserve verified names, figures, terminology, and source meaning. Mark simulated values clearly.
5. Apply a coherent editorial system. Read [references/editorial-design.md](references/editorial-design.md) for premium reports and white papers.
6. Render the complete final document.
7. Inspect every page at readable zoom; a contact sheet is only an overview.
8. Fix clipping, overlaps, broken tables, missing glyphs, blurry images, weak hierarchy, and incorrect headers or footers.
9. Re-render after each layout-sensitive change.
10. Run metadata and secret checks before public release.
11. Deliver only requested final artifacts unless QA outputs are requested.

## Editorial defaults

- Use conclusion-first titles and one dominant idea per page.
- Keep type, spacing, grid, table geometry, and accent colors consistent.
- Prefer native text and tables over screenshots when content must remain crisp or editable.
- Label simulated data as `PLANNING ASSUMPTION / 企划模拟值`.
- Never redistribute font files, credentials, private records, or unapproved third-party source documents.
- Use [assets/apple-editorial.json](assets/apple-editorial.json) as the default style pack when the user asks for an Apple-inspired editorial treatment.

## Final gate

Read [references/qa-checklist.md](references/qa-checklist.md) and approve the artifact only after all applicable content, layout, image, table, navigation, metadata, and PDF checks pass.
