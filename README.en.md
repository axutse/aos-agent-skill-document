# AOS Agent Skill · Document

[简体中文](README.md) | [English](README.en.md)

Current version: `0.1.3`

[![Release](https://img.shields.io/github/v/release/axutse/aos-agent-skill-document)](https://github.com/axutse/aos-agent-skill-document/releases)
[![CI](https://github.com/axutse/aos-agent-skill-document/actions/workflows/validate.yml/badge.svg)](https://github.com/axutse/aos-agent-skill-document/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An open-source document skill package for Codex and compatible agents. It turns professional document work into a verifiable process: plan the content, create or revise Word, export PDF, inspect every rendered page, scrub metadata, and deliver both editable and fixed-layout artifacts.

```text
plan -> author -> render -> inspect -> revise -> verify
```

## Positioning

`AOS Agent Skill · Document` is an **agent-oriented document publishing workflow plugin**. It is not an online Office suite, a cloud conversion service, or a general-purpose chatbot. It combines Codex's ability to understand source material with local document tools, upgrading “generate a file” into a complete generate-render-inspect-fix-verify delivery loop.

It is designed for:

- individuals, content teams, brand teams, and consultancies that need reliable DOCX and PDF output;
- deliveries that must keep Word editable while maintaining consistent PDF appearance;
- repeatable reports, white papers, proposals, manuals, and brand documents;
- pre-publication review of pages, metadata, privacy, and credential residue.

It does not:

- replace Microsoft Word, Adobe Acrobat, or final human sign-off;
- prove business figures, factual sources, copyright, or trademark rights;
- promise complete rendering QA when LibreOffice or Poppler is unavailable;
- upload files to an external model or conversion API. The plugin itself requires no API key.

The default delivery contract is: **source review + content/page plan + editable DOCX + fixed-layout PDF + full-page visual QA + public-release checks**. The skills reduce that scope when the user requests only part of the workflow.

## Implemented capabilities

| Area | Capability | Status |
|---|---|:---:|
| Content planning | Read multiple sources and build a fact list, section structure, and page budget | ✅ |
| Word | Create DOCX or revise an existing Word file while preserving styles and editability | ✅ |
| Word | Headings, contents, tables, images, sections, headers, footers, and page numbers | ✅ |
| PDF | Inspect page count, dimensions, rotation, encryption, links, forms, and metadata | ✅ |
| Visual QA | Render every DOCX/PDF page, inspect individually, repair, and re-verify | ✅ |
| Public release | Remove author data, comments, tracked changes, and personal metadata | ✅ |
| Bilingual delivery | Chinese, English, and aligned separate Chinese-English editions | ✅ |
| Batch delivery | Accept one sample, then generate a batch under locked rules | ✅ |
| Open case | 20-page editable sample, 149-page full case, generator, and QA images | ✅ |
| Local processing | No additional API key and no external conversion service | ✅ |

See the [feature scope matrix](docs/feature-matrix.en.md) for conditions, dependencies, and out-of-scope capabilities.

The project ships as both a Codex Plugin and a standalone SkillHub skill. See [SkillHub publishing](docs/skillhub-publishing.en.md) for package generation and version synchronization.

## See the result first

The open TAIZHOU case includes a 20-page editable DOCX, matching PDF, complete contact sheet, and reproducible generator. The six enlarged crops below show the cover, contents, corporate architecture, brand portfolio, product development, and user journey pages.

<table>
  <tr>
    <td width="50%"><strong>Cover / Page 1</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/00-cover-page-01.png" alt="TAIZHOU white paper cover"></td>
    <td width="50%"><strong>Contents / Page 3</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/01-contents-page-03.png" alt="TAIZHOU white paper contents"></td>
  </tr>
  <tr>
    <td width="50%"><strong>Corporate architecture / Page 4</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/02-governance-page-04.png" alt="TAIZHOU corporate architecture"></td>
    <td width="50%"><strong>Brand portfolio / Page 7</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/03-multi-brand-page-07.png" alt="TAIZHOU brand portfolio matrix"></td>
  </tr>
  <tr>
    <td width="50%"><strong>Product development / Page 12</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/04-product-material-page-12.png" alt="TAIZHOU product development system"></td>
    <td width="50%"><strong>User journey / Page 17</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/05-media-operation-page-17.png" alt="TAIZHOU user journey"></td>
  </tr>
</table>

See the [TAIZHOU case guide](examples/taizhou-white-paper/README.en.md) for high-resolution pages, chapter notes, and adaptation instructions. Download the complete 149-page case from the [v0.1.3 Release](https://github.com/axutse/aos-agent-skill-document/releases/tag/v0.1.3).

## Included skills

| Skill | Best suited for | Primary output |
|---|---|---|
| `$aos-publish-document` | Building a white paper, report, proposal, manual, or brand book from source material | DOCX + PDF + page acceptance |
| `$aos-author-word` | Creating, revising, repairing, or preparing Word for public release | Editable DOCX, optional PDF |
| `$aos-process-pdf` | Inspecting, cleaning, rendering, or verifying an existing PDF | Processed PDF + inspection report |

When both Word and PDF are required, prefer `$aos-publish-document`. It verifies the DOCX first, then converts and verifies the PDF.

The three skills are not competing programs. `$aos-publish-document` is the orchestration entry point, while the other two provide focused Word and PDF workflows. See [Installation to first delivery](docs/getting-started.en.md) for the decision rules, input template, and complete first-run tutorial.

## Start in 3 minutes

> First-time users should open the [complete getting-started guide](docs/getting-started.en.md), which includes installation checks, three end-to-end walkthroughs, updates, uninstall, and troubleshooting.

### 1. Install

```bash
codex plugin marketplace add axutse/aos-agent-skill-document
codex plugin add aos-agent-skill-document@aos-agent-skills
```

Start a new Codex task after installation so the new skill metadata is available in context.

### 2. Prepare the input

At minimum, provide:

- the document goal, such as a brand white paper, annual report, or project proposal;
- the source file or directory;
- whether you need DOCX, PDF, or both;
- language, page count, style, and deadline requirements.

When available, also provide the brand name, section list, verified data, images, logo, colors, and terms that must not be changed.

### 3. Copy your first instruction

```text
Use $aos-publish-document to read all supplied source material. First create a section and page plan,
then produce an approximately 20-page English brand white paper. Use a concise editorial style,
conclusion-first headings, and generous whitespace. Deliver an editable DOCX and matching PDF,
remove personal metadata, and inspect every page for fonts, images, tables, page numbers, headers,
footers, clipping, and overlaps. Mark any unverified business figures as planning assumptions.
```

### 4. Accept the result

A complete delivery normally includes:

- an editable DOCX;
- a fixed-layout PDF;
- page-count, size, metadata, and font inspection results;
- a conclusion from full-page rendering QA;
- a contact sheet or QA images only when explicitly requested.

## Common use cases

### Build a brand white paper from scratch

```text
Use $aos-publish-document to turn the brand introduction, product information, organization chart,
and images in the source directory into a 24-page brand white paper. First produce the contents and
page blueprint and verify the information sources. Finish the DOCX, export the PDF, and visually
inspect every page. Keep one dominant conclusion per page.
```

### Revise an existing Word file without breaking its structure

```text
Use $aos-author-word to revise sections 2, 5, and 8 of this Word document. Preserve the current
styles, headers, footers, table of contents, and pagination. Update only the specified content.
Scrub author and revision metadata, render every page, and report the changes.
```

### Audit a PDF before publication

```text
Use $aos-process-pdf to inspect page count, dimensions, rotation, encryption, forms, links, and
metadata. Render every page and identify missing glyphs, blurry images, clipping, overlaps, and
unexpected blank pages. Do not modify the file yet; return a prioritized issue list first.
```

### Turn an internal report into a public version

```text
Use $aos-publish-document to prepare this internal report for public release. Remove comments,
tracked changes, personal metadata, credentials, and customer data while preserving approved
content. Deliver DOCX and PDF plus a concise pre-publication review summary.
```

### Generate multiple reports from one layout

```text
Use $aos-publish-document with the approved reference document as the layout standard. Read the
project data directory and create separate DOCX and PDF files for each project. Keep sections,
type sizes, spacing, tables, and page numbering consistent while preserving project-specific titles,
data, and images. Generate and accept one sample before processing the remaining projects.
```

For annual reports, proposals, SOPs, brand guidelines, and batch delivery prompts, see the [use-case and prompt cookbook](docs/usage-cookbook.en.md).

## What the TAIZHOU case contains

[`examples/taizhou-white-paper/`](examples/taizhou-white-paper/) provides:

- `brief.json`: title, audience, page count, brands, and assumption policy;
- `style-pack.json`: colors, typography hierarchy, page grid, and editorial rules;
- `references/`: corporate governance, multi-brand, product/material, visual system, and page blueprint sources;
- `generate_example.py`: generates DOCX from structured inputs;
- `build_release.py`: generates, scrubs, converts, renders, and validates the complete delivery;
- `output/`: 20-page DOCX, PDF, and full contact sheet;
- `assets/chapter-gallery/`: cover, contents, and four high-resolution chart pages.

The case uses only the TAIZHOU, WANMIAN / 万棉尚品, GEERNA / 哥尔纳, and UIUP architecture. All built-in business figures are marked `PLANNING ASSUMPTION / 企划模拟值`.

## Reproduce the case locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/taizhou-white-paper/build_release.py \
  --output-dir examples/taizhou-white-paper/output \
  --qa-dir /tmp/taizhou-example-qa
```

DOCX rendering requires LibreOffice; PDF rendering requires Poppler. The build generates DOCX, enables high-fidelity image settings, scrubs metadata, exports PDF, renders all pages, and generates a contact sheet.

## Repository layout

```text
.
├── .agents/plugins/marketplace.json
├── README.md / README.en.md
├── docs/
│   ├── feature-matrix.md / feature-matrix.en.md
│   ├── getting-started.md / getting-started.en.md
│   ├── skillhub-publishing.md / skillhub-publishing.en.md
│   └── usage-cookbook.md / usage-cookbook.en.md
├── distributions/skillhub/
│   └── aos-agent-skill-document/SKILL.md
├── plugins/aos-agent-skill-document/
│   ├── .codex-plugin/plugin.json
│   ├── assets/
│   └── skills/
│       ├── aos-publish-document/
│       ├── aos-author-word/
│       └── aos-process-pdf/
├── examples/taizhou-white-paper/
├── release-assets/
├── scripts/
├── tests/
└── .github/workflows/validate.yml
```

## Development and validation

```bash
python scripts/check_public_release.py --root .
pytest
```

The release check scans for common credential patterns, unfinished placeholders, non-TAIZHOU brand residue, Office/PDF text, and oversized Git files.

## Data and security

- The plugin requires no API key and does not connect to an external model or service.
- Do not commit credentials, private contracts, customer data, identity information, or unlicensed fonts.
- Treat any credential pasted into chat, terminal output, an issue, or commit history as compromised and rotate it at the provider.
- Before public release, inspect content, file properties, comments, revisions, attachments, and PDF metadata.

## License

- Code, skills, scripts, and repository documentation: MIT
- `examples/taizhou-white-paper/`: CC BY 4.0
- The licenses do not grant rights to TAIZHOU or case-brand trademarks
