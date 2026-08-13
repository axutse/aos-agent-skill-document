# Installation to first delivery

[简体中文](getting-started.md) | [English](getting-started.en.md)

This guide is for first-time users of `AOS Agent Skill · Document`. By the end, you will understand what it solves, how to install it, how to select a skill, how to write an executable instruction, and how to accept the output.

## 1. Understand the positioning

This is a **skills-only document publishing plugin**. It does not provide a new chat model and does not upload files to a third-party conversion site. It gives Codex a professional document workflow and uses local Python, LibreOffice, and Poppler tools for file processing and visual inspection.

The workflow is:

```text
read sources -> plan structure -> create/revise DOCX -> render every page
             -> inspect and fix -> export PDF -> render again -> deliver
```

“Generated successfully” only means that a file can be opened. “Accepted for delivery” also requires checking every page for fonts, images, tables, pagination, headers, footers, clipping, overlaps, and metadata.

### Good fits

- brand white papers, corporate reports, annual reports, proposals, and solution documents;
- operating manuals, policies, training materials, and brand guidelines;
- localized Word revisions, structural repair, and public-release cleanup;
- PDF structure inspection, page rendering, metadata cleanup, and visual QA;
- batch delivery from a shared layout.

### Not a replacement for

- all interactive editing features in Word or Acrobat;
- human legal, financial, factual, copyright, or brand-rights review;
- establishing the truth of business data without a source;
- complete visual QA when local rendering tools are unavailable.

## 2. Prerequisites

Minimum requirements:

- an installed and working Codex environment;
- Python 3.10 or later;
- LibreOffice recommended for creating or revising DOCX;
- Poppler recommended for inspecting PDF pages.

Install the local rendering tools with Homebrew on macOS:

```bash
brew install --cask libreoffice
brew install poppler
```

The plugin itself requires no API key. Do not commit credentials, customer data, or unauthorized source files to a public repository.

## 3. Install the plugin

Run:

```bash
codex plugin marketplace add axutse/aos-agent-skill-document
codex plugin add aos-agent-skill-document@aos-agent-skills
```

Then inspect the installed plugins:

```bash
codex plugin list
```

The list should contain `aos-agent-skill-document`. After installation or update, **start a new Codex task** so that the current skill metadata is loaded into the task context.

## 4. Select the right skill

| Your task | Skill | Typical delivery |
|---|---|---|
| Build a complete document from source material | `$aos-publish-document` | DOCX + PDF + acceptance summary |
| Create or revise Word | `$aos-author-word` | Editable DOCX, optional PDF |
| Inspect or process PDF | `$aos-process-pdf` | PDF + structural/visual report |

Use this decision tree when unsure:

```text
Do you need a complete document from content planning through final delivery?
├─ Yes -> $aos-publish-document
└─ No
   ├─ The primary artifact is DOCX -> $aos-author-word
   └─ The primary artifact is PDF  -> $aos-process-pdf
```

`$aos-publish-document` is the orchestration entry point. It loads the Word and PDF workflows as needed; users do not need to invoke all three skills in sequence.

## 5. Prepare source material

Keep related files in one project directory and identify that path in the instruction. At minimum, specify:

1. document purpose and audience;
2. source file or directory;
3. delivery format: DOCX, PDF, or both;
4. language, approximate page count, page size, style, and deadline;
5. content that must be preserved, must not be rewritten, or must be labeled.

Copy this input template:

```text
Use $aos-publish-document.

Goal: create a [document type] for [audience/use case].
Sources: read all relevant material in [file or directory path].
Content: include [sections/topics] and do not change [names/figures/terms].
Specification: [language], approximately [page count] pages, [A4/Letter], [style].
Delivery: [DOCX/PDF/both].
Acceptance: inspect every page for fonts, images, tables, page numbers, headers, footers,
            clipping, and overlaps; remove personal metadata, comments, revisions, and secrets.
Data policy: label any unverified business figures as planning assumptions; do not present them as facts.
```

## 6. First complete run: build a white paper

### Step 1: place the sources in the project

Example:

```text
my-white-paper/
├── source/
│   ├── brand-introduction.docx
│   ├── product-data.xlsx
│   ├── organization.md
│   └── images/
└── output/
```

### Step 2: give Codex the task

```text
Use $aos-publish-document to read all sources in the source directory and create a 20-page English
brand white paper for business partners. Produce a section and page plan before authoring. Use a
clean editorial design and keep one dominant conclusion per page. Write outputs to the output
directory and deliver an editable DOCX plus matching PDF. Preserve official names and verified
figures; label unverified operating figures as planning assumptions. Render every page, inspect
fonts, images, tables, page numbers, headers, footers, clipping, overlaps, and unexpected blanks,
then remove author, comment, revision, and sensitive metadata.
```

### Step 3: observe the execution stages

A normal run should:

1. list the sources read and any material gaps;
2. produce a section structure or page blueprint;
3. generate and structurally inspect DOCX;
4. render and repair all DOCX pages;
5. convert to PDF and inspect its structure and all pages again;
6. return final file paths and a concise acceptance summary.

If the agent generates files but does not render and inspect them, continue with:

```text
Continue with final acceptance. Do not inspect text alone. Render every page, review each one at a
readable zoom, fix all blocking defects, render again, and report the final state of page count,
dimensions, metadata, and visual issues.
```

## 7. Second walkthrough: revise an existing Word file only

Use this when an approved template exists and only localized changes are allowed:

```text
Use $aos-author-word to revise report.docx and update only sections 2, 5, and 8. Preserve the
existing styles, table of contents, headers, footers, section order, and pagination; do not rebuild
the template. Save the result as output/report-public.docx without overwriting the source. Remove
author, comment, and revision metadata. Render every page and focus on table-of-contents page numbers,
tables that cross pages, image proportions, headers, footers, and pagination changes caused by the
new paragraphs. List the actual changes and the final acceptance result.
```

The critical constraints are: do not overwrite the source, identify the sections to change, and state which layout must remain intact.

## 8. Third walkthrough: audit a PDF without modifying it

Use this before public release or when diagnosing a problem:

```text
Use $aos-process-pdf to inspect proposal.pdf. Do not modify the file yet. Check page count, dimensions,
rotation, encryption, forms, links, metadata, and image usage. Render every page at 200 DPI and inspect
at a readable zoom for missing glyphs, blurry images, clipping, overlaps, incorrect page boxes,
unexpected blank pages, and table defects. Classify findings as blocking, recommended, or acceptable,
and propose the smallest repair scope.
```

Approve the issue list before asking the agent to repair and write a new file. This prevents accidental overwrite or unnecessary scope expansion.

## 9. Accept the final delivery

Confirm at least the following:

- files reopen successfully and DOCX remains editable;
- page counts and content match the requirements;
- every page was inspected individually, not only through a contact sheet;
- no text or image clipping, object overlap, missing glyphs, broken tables, or unexpected blank pages;
- images are not visibly stretched or unnecessarily low-resolution;
- page numbers, contents, headers, footers, and section order are correct;
- comments, revisions, author, company, and sensitive metadata follow the release policy;
- unverified figures, placeholders, and simulated values are clearly labeled;
- the final directory contains only requested deliverables.

A contact sheet is useful for reviewing overall rhythm, but it never replaces page-by-page inspection.

## 10. Bilingual delivery

For a Chinese-English deliverable, state whether you want two separate files, paired sections, or side-by-side pages. Separate files are the safest default for long documents because Chinese and English wrap differently.

```text
Use $aos-publish-document to produce separate Simplified Chinese and English editions from the same
verified source set. Keep section order, figures, tables, captions, page identifiers, and assumption
labels aligned. Build a terminology glossary before translation. Do not translate registered names
unless an approved English name is supplied. Render and inspect both editions independently, and
report any page-count or pagination differences.
```

## 11. Update and uninstall

Reinstall after refreshing the remote marketplace information:

```bash
codex plugin add aos-agent-skill-document@aos-agent-skills
```

Start a new Codex task after the update. To uninstall:

```bash
codex plugin remove aos-agent-skill-document
```

## 12. Troubleshooting

### The skills do not appear after installation

Run `codex plugin list`, then start a new Codex task. An existing task may still have pre-installation metadata.

### DOCX is generated but no page images or visual QA appear

Confirm that LibreOffice is installed. Without it, only structural checks are possible; complete Word rendering QA cannot be claimed.

### PDF rendering fails

Confirm that `pdftoppm` is available:

```bash
pdftoppm -v
```

If unavailable on macOS, run `brew install poppler`.

### The result does not match expectations

Add page size, page count, audience, reference style, content that must remain, and content that must not change. For existing files, explicitly require “save to a new file; do not overwrite the source.”

### Does it require a model API key?

No. The plugin contains workflows, references, and local processing scripts. It does not add an external model route or online conversion service.

## 13. Next steps

- Copy more complete prompts from the [use-case and prompt cookbook](usage-cookbook.en.md)
- Review the [TAIZHOU white-paper case](../examples/taizhou-white-paper/README.en.md)
- Reproduce the bundled case using the [local build instructions](../examples/taizhou-white-paper/README.en.md#3-reproduce-the-full-release-workflow)
