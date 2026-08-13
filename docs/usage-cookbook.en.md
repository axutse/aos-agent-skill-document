# Use-case and prompt cookbook

[简体中文](usage-cookbook.md) | [English](usage-cookbook.en.md)

This cookbook provides document instructions that can be copied directly. Each prompt defines inputs, outputs, and acceptance criteria, replacing vague requests such as “make it look more professional” with verifiable requirements.

## Select a skill

| Task | Skill |
|---|---|
| Plan and build DOCX + PDF from scratch | `$aos-publish-document` |
| Work only with Word or require an editable delivery | `$aos-author-word` |
| Inspect or process only fixed-layout PDF | `$aos-process-pdf` |
| Revise Word, then deliver PDF | Start with `$aos-author-word`, then use `$aos-process-pdf` |

## What a complete instruction should contain

Specify, in order:

1. task type and audience;
2. source material and factual sources;
3. language, page count, page size, and style;
4. content that must remain and content that must not appear;
5. whether DOCX, PDF, or both are required;
6. metadata, confidentiality, and publication scope;
7. rendering, page-by-page inspection, and final acceptance conditions.

## Use case 1: corporate brand white paper

For publishing a combined corporate introduction, brand strategy, product system, and five-year direction.

```text
Use $aos-publish-document to read the corporate introduction, organization chart, brand positioning,
product material, operating plan, and images in the source directory. Create a 24-page English
corporate brand white paper for business partners.

First return a fact list, planning-assumption list, missing-material list, section structure, and
page budget. After confirmation, generate an editable DOCX and matching PDF. Use conclusion-first
headings, clear tables, and generous whitespace, with one dominant conclusion per page. Scrub personal
metadata and inspect every page for fonts, images, tables, page numbers, clipping, and overlaps.
```

Acceptance: corporate and brand relationships are explicit; assumptions are labeled; DOCX and PDF page order is aligned.

## Use case 2: annual operating report

For business review, metric explanation, annual strategy, and next-year action planning.

```text
Use $aos-publish-document to build an annual operating report from the annual data workbook,
department reviews, and management conclusions. Do not invent figures. Every metric must show its
period, unit, and source; use one consistent definition for year-over-year, period-over-period, and
target variance. Deliver a landscape 16:9 PDF and editable DOCX with an executive summary, metrics,
problems, causes, actions, owners, and timeline. Label all charts clearly and render-check every page.
```

Acceptance: metric definitions are consistent; conclusions trace to data; every action has an owner and date.

## Use case 3: project proposal and solution

For client proposals, internal project approval, and technical solutions.

```text
Use $aos-publish-document to turn the requirements, interview notes, and current-system material into
a project proposal. Include background, current state, objectives, scope, solution, milestones, roles,
risks, budget assumptions, and acceptance criteria. Clearly separate confirmed requirements, proposed
solutions, and open questions. Deliver editable DOCX and review PDF, keep all tables editable, and
inspect long-table pagination, heading hierarchy, and page numbers.
```

Acceptance: scope boundaries are clear; assumptions are not presented as facts; risks and acceptance criteria are executable.

## Use case 4: SOP, policy, or employee manual

For workflows, job standards, approval policies, and operating manuals.

```text
Use $aos-author-word to convert the existing policies, chat records, and process notes into a formal
SOP. Use numbered headings, roles, prerequisites, operating steps, exception handling, approval gates,
record retention, and version information. Preserve all verified rules and do not add unapproved
policy. Deliver a DOCX with an automatic table of contents and convert it to PDF. Inspect numbering,
cross-references, pagination, headers, footers, and table continuity.
```

Acceptance: steps are executable; role and approval boundaries are explicit; contents, numbering, and version information are correct.

## Use case 5: localized revision of an existing Word file

For updating specified sections, figures, or images without reformatting the entire document.

```text
Use $aos-author-word to modify only the Market Analysis, Annual Objectives, and Action Plan sections.
Preserve the original theme, styles, contents, headers, footers, sections, and page numbers. Copy the
source file before making localized changes; do not rebuild unaffected sections. Return a change
summary, remove comments, revisions, and personal metadata, then render every page to inspect pagination.
```

Acceptance: unspecified content is unchanged; contents and page numbers update correctly; no comments or revisions remain.

## Use case 6: PDF public-release review

For the final web-release check of a report, white paper, contract draft, or downloadable resource.

```text
Use $aos-process-pdf and do not modify the file yet. Inspect PDF page count, dimensions, rotation,
encryption, JavaScript, forms, links, metadata, and font rendering. Render every page and inspect for
missing glyphs, blur, clipping, overlaps, unexpected blanks, incorrect page numbers, and low-resolution
images. Return findings grouped as release blocking, high priority, and recommended. Generate a cleaned
public version only after I approve the scope.
```

Acceptance: structural and visual inspection are both complete; each issue has a page, cause, and action.

## Use case 7: convert internal material into a public edition

For removing sensitive data, revision history, and personal metadata before external release.

```text
Use $aos-publish-document to convert the internal report into a public edition. Build a deletion list
and remove customer identifiers, internal accounts, credentials, unreleased prices, comments, tracked
changes, author, and last-modifier metadata. Do not merely cover text visually; confirm it is removed
from document structure. Deliver public DOCX and PDF, reopen both, run credential scanning, and complete
page-by-page visual acceptance.
```

Acceptance: sensitive content is not only visually hidden; Office packages and PDF metadata are checked; the public edition reads independently.

## Use case 8: batch reports from one layout

For recurring store, customer, project, or product reports.

```text
Use $aos-publish-document with the approved reference report as the structural and visual standard.
Read the data directory and generate one DOCX and PDF per project. Keep sections, type sizes, spacing,
tables, headers, footers, and file naming consistent; replace only project-specific data, conclusions,
and images. Generate one sample first, accept every page, lock the rules, and then process the rest.
Check page count, metadata, and rendering for every file and return a summary manifest.
```

Acceptance: sample before batch; no project data leaks into another report; failed items are recorded rather than silently skipped.

## Use case 9: brand visual guidelines

For centralized logo, color, typography, photography, packaging, and digital interface rules.

```text
Use $aos-publish-document to build brand visual guidelines from authorized brand assets. Include brand
idea, logo clear space and misuse, color, typography, layout, graphics, photography, packaging, social
media, and digital-interface examples. Do not present unsupported mockups as official rules; label them
as proposed examples. Deliver editable DOCX and high-resolution PDF, and inspect image clarity, color
labels, captions, and consistency across page breaks.
```

Acceptance: rules and examples are clearly distinguished; asset rights are known; images and color values are usable.

## Use case 10: long-document quality review

For a finished long report that is about to go online, to print, or into an archive.

```text
Use $aos-process-pdf for final quality review. Generate a low-resolution contact sheet to inspect the
overall rhythm, then inspect every page at readable zoom. Verify section opening pages, contents page
numbers, headers, footers, blank pages, tables across pages, image clarity, font substitution, widows,
orphans, and clipping. Return a page-sorted issue table with severity, description, and suggested fix.
```

Acceptance: the contact sheet is overview only; final conclusions come from page-by-page inspection; every blocker is located.

## Use case 11: separate Chinese and English editions

For publishing two language editions from one verified source set.

```text
Use $aos-publish-document to produce separate Simplified Chinese and English editions. First establish
a bilingual glossary for company names, brands, products, metrics, section titles, and assumption labels.
Keep the section order, facts, figures, tables, captions, and page identifiers synchronized. Do not
translate registered names without an approved equivalent. Deliver editable DOCX and PDF for each
language. Render and inspect all four artifacts independently, and report intentional differences in
page count, line wrapping, and pagination.
```

Acceptance: terminology is consistent; figures and facts align; each edition receives independent visual QA.

## Common weak instructions

### Too little information

```text
Make me a premium white paper.
```

Problem: no audience, sources, page count, output format, or acceptance criteria.

### Generation without verification

```text
Turn this content into PDF.
```

Problem: a successful conversion does not prove correct pages; add metadata, font, and page-by-page checks.

### Treating assumptions as facts

```text
Fill in any missing data for me.
```

Problem: public documents must distinguish facts, inferences, and assumptions. Structure may be completed; corporate facts must not be fabricated.

## Recommended delivery clause

Append this to an instruction:

```text
Before delivery, reopen every final file and complete structural and page-by-page visual inspection.
Do not place test files, temporary renderings, caches, credentials, personal metadata, or unauthorized
assets in the final delivery directory. Report output paths, page counts, validation results, and any
items that still require human confirmation.
```
