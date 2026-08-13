# Feature scope matrix

[简体中文](feature-matrix.md) | [English](feature-matrix.en.md)

Status: `✅ Implemented` means the repository contains a workflow or script; `◐ Conditional` requires local software, sufficient input, or human confirmation; `— Not included` is outside the current release.

## Content planning and publishing

| Capability | Status | Conditions and notes |
|---|:---:|---|
| Read and organize multiple source files | ✅ | Handles documents, workbooks, images, and Markdown that the Agent can access |
| Classify facts, inferences, assumptions, and gaps | ✅ | Unverified business figures default to `PLANNING ASSUMPTION` |
| Plan sections, page blueprints, and page budgets | ✅ | Long documents are planned before authoring |
| White papers, reports, proposals, manuals, and brand guidelines | ✅ | Use `$aos-publish-document` |
| Batch generation under a shared layout | ✅ | Generate and accept one sample before the batch |
| Chinese-only or English-only documents | ✅ | Deliver in the language requested by the user |
| Separate aligned Chinese and English editions | ✅ | Establish a glossary and verify both editions independently |
| Side-by-side bilingual pages | ◐ | Suitable for short content; separate editions are safer for long documents |
| Certification of business facts | — | Source owners and human reviewers must confirm truthfulness |
| Final legal, financial, copyright, or trademark approval | — | The skill can inspect and flag issues but cannot replace professional sign-off |

## Word / DOCX

| Capability | Status | Conditions and notes |
|---|:---:|---|
| Create editable DOCX from scratch | ✅ | Uses semantic headings, paragraphs, lists, and tables |
| Apply localized revisions to an existing Word file | ✅ | Preserves the source and writes a new file by default |
| Preserve styles, sections, headers, footers, and page numbers | ✅ | Prefer localized changes over rebuilding unrelated content |
| Automatic contents, heading hierarchy, and numbering | ✅ | Requires structured Word styles |
| Native editable tables and image layout | ✅ | Uses explicit widths, proportions, and page geometry |
| High-fidelity image settings | ✅ | Includes a deterministic processing script |
| Inspect author, company, and personal metadata | ✅ | Can scrub these fields before public release |
| Remove comments and tracked changes | ✅ | Public editions exclude them unless requested |
| Convert DOCX to PDF | ✅ | Requires LibreOffice |
| Render and inspect every Word page | ◐ | Requires LibreOffice; otherwise only structural QA is possible |
| Live control of the desktop Word UI | — | The skill edits files and does not automate Word's interface |
| Macros, VBA, and complex embedded-object development | — | No dedicated workflow in the current release |

## PDF

| Capability | Status | Conditions and notes |
|---|:---:|---|
| Inspect page count, dimensions, and rotation | ✅ | Can emit structured JSON results |
| Inspect encryption, forms, links, and metadata | ✅ | Supports pre-publication audits |
| Scrub PDF metadata | ✅ | Preserves approved title and author information |
| Render every PDF page | ◐ | Requires Poppler / `pdftoppm` |
| Page-by-page visual acceptance | ✅ | Checks missing glyphs, clipping, overlaps, blur, and unexpected blanks |
| Contact sheet generation | ✅ | Overview only; never replaces individual page inspection |
| Re-verify PDF converted from Word | ✅ | DOCX and PDF are accepted independently |
| OCR for scanned documents | — | OCR is not bundled; connect an OCR tool or service first |
| Electronic seal or certificate-based PDF signing | — | Signing is not included |
| Full interactive Acrobat editing | — | Does not replace Adobe Acrobat |

## Quality, security, and distribution

| Capability | Status | Conditions and notes |
|---|:---:|---|
| Render, repair, and re-render loop | ✅ | Layout-sensitive changes require another inspection |
| Metadata and common credential-pattern scanning | ✅ | The repository includes a public-release scanner |
| Private and customer-data warnings | ✅ | The user must still confirm publication rights |
| Local Python document processing | ✅ | The plugin itself requires no API key |
| External cloud conversion | — | Files are not uploaded to a third-party converter by default |
| 20-page open TAIZHOU sample | ✅ | Includes DOCX, PDF, contact sheet, and generator |
| 149-page complete TAIZHOU case | ✅ | Available as a GitHub Release asset |
| Codex Plugin installation | ✅ | Install through the repository marketplace |
| SkillHub single-skill distribution | ✅ | Generated from the same canonical sources to avoid duplicate maintenance |

## Minimum dependencies

| Task | Required or recommended dependency |
|---|---|
| Structured DOCX/PDF inspection and scripts | Python 3.10+ and `requirements.txt` |
| DOCX-to-PDF conversion and Word rendering | LibreOffice |
| PDF page rendering | Poppler |
| Codex Plugin use | A Codex environment with Plugin/Skill support |
| SkillHub installation and publication | SkillHub CLI and a platform account |

When a dependency is unavailable, the Agent must disclose which checks were completed and must not describe structural checks as complete visual QA.
