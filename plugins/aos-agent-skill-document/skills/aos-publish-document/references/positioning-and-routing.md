# Positioning, routing, and delivery contract

Use this reference to explain the plugin clearly and select the smallest workflow that fulfills the request.

## Positioning

Position AOS Agent Skill · Document as a skills-only document publishing workflow for Codex and compatible agents. It combines source understanding, editable document authoring, fixed-layout export, local rendering, metadata review, and page-by-page visual QA.

Do not position it as:

- a new language model or model router;
- an online Office suite or cloud conversion API;
- a replacement for Microsoft Word or Adobe Acrobat;
- a source of factual, legal, financial, copyright, or trademark approval;
- a guarantee of visual QA when the required local renderers are unavailable.

The plugin does not require an API key and does not add an external model connection.

## Routing

| Request shape | Route |
|---|---|
| Turn source material into a complete publication | `$aos-publish-document` |
| Produce both DOCX and PDF with final QA | `$aos-publish-document`, then load the format workflows it needs |
| Create or modify DOCX as the main artifact | `$aos-author-word` |
| Inspect, clean, render, or verify PDF as the main artifact | `$aos-process-pdf` |
| Audit a PDF before deciding whether to modify it | `$aos-process-pdf`, report first and preserve the input |

Do not mechanically invoke all three skills. Use the publishing skill as the entry point for end-to-end work and the format skill directly for focused tasks.

## Minimum input contract

Infer these items from context when safe, and ask only when a missing choice would materially change the deliverable:

1. document purpose and audience;
2. source files or source directory;
3. required output formats;
4. language, approximate length, page size, and style;
5. facts, terms, sections, or layout that must remain unchanged;
6. metadata and public-release policy.

## Default output contract

For end-to-end publishing, produce or report:

1. source inventory and material gaps;
2. section or page plan for long documents;
3. editable DOCX when requested;
4. fixed-layout PDF when requested;
5. structural inspection results;
6. readable-zoom inspection of every rendered page;
7. corrections followed by re-rendering;
8. final artifact paths and a concise acceptance summary.

Do not keep temporary page images or contact sheets in the final delivery unless requested. Treat a contact sheet as an overview only; it never replaces individual page inspection.

## Boundaries and disclosures

- Preserve verified source meaning and label unverified business figures as `PLANNING ASSUMPTION / 企划模拟值`.
- Do not invent missing facts to fill a page.
- Preserve the original input for edit requests and save changes to a new path unless the user explicitly authorizes overwrite.
- Disclose structural-only QA when LibreOffice or Poppler is unavailable.
- Require human approval for legal, financial, factual, copyright, trademark, and final publication decisions.
