# TAIZHOU corporate brand white-paper case

[简体中文](README.md) | [English](README.en.md)

This is the public, reproducible case for `aos-agent-skill-document`. It demonstrates how to turn a structured brief, corporate material, brand material, and a style pack into an editable DOCX, fixed-layout PDF, and rendered pages for complete visual inspection.

The case uses the TAIZHOU corporate system and the WANMIAN / 万棉尚品, GEERNA / 哥尔纳, and UIUP brand architecture. All operating figures, price bands, organizational responsibilities, and growth targets are marked `PLANNING ASSUMPTION / 企划模拟值` and must not be treated as verified corporate facts.

## Deliverables

| File | Purpose |
|---|---|
| `output/TAIZHOU品牌企业白皮书_示例版.docx` | Editable source preserving text, tables, and page structure |
| `output/TAIZHOU品牌企业白皮书_示例版.pdf` | 20-page fixed-layout public example |
| `output/TAIZHOU品牌企业白皮书_示例版_联系表.jpg` | One-image overview of rhythm and consistency across all 20 pages |
| `assets/chapter-gallery/` | Cover, contents, and four high-information chart pages |

## Three ways to use the case

### 1. Study the finished structure

Start with the complete contact sheet to understand the rhythm between cover, contents, section openings, evidence pages, tables, and closing pages. Then open the DOCX to inspect its editable structure.

![TAIZHOU 20-page contact sheet](output/TAIZHOU品牌企业白皮书_示例版_联系表.jpg)

### 2. Adapt the case to your own brand

Edit `brief.json` and `style-pack.json`, replace the corporate, brand, product, and visual content under `references/`, then run the one-command build. Do not replace the brand name alone; rewrite positioning, audience, product, price, visual, and operating logic together.

Suggested instruction:

```text
Use $aos-publish-document and follow the chapter rhythm and editorial design of the TAIZHOU case,
but use only the new brand material I provide. First build a fact list and missing-material list,
then produce a page blueprint. Generate editable DOCX and matching PDF, label all assumptions,
and complete rendering acceptance for every page.
```

### 3. Reproduce the full release workflow

Run from the repository root:

```bash
python examples/taizhou-white-paper/build_release.py \
  --output-dir examples/taizhou-white-paper/output \
  --qa-dir /tmp/taizhou-example-qa
```

The workflow runs:

```text
generate DOCX
-> enable high-fidelity images
-> scrub personal DOCX metadata
-> render every Word page
-> convert and scrub PDF metadata
-> render every PDF page
-> generate contact sheet
-> verify page count, dimensions, fonts, tables, and images
```

To generate only the unprocessed source DOCX:

```bash
python examples/taizhou-white-paper/generate_example.py \
  --brief examples/taizhou-white-paper/brief.json \
  --output /tmp/TAIZHOU-source.docx
```

## Six representative pages

The gallery contains exactly six images: cover, contents, corporate architecture, brand portfolio matrix, product development system, and user journey. Each crop removes the large lower-page whitespace and presents a 1900 × 1600-pixel enlarged detail. The source PDF pages are unchanged.

### Cover: page 1

The visual entry point uses minimal information to establish title, time range, content boundary, and English subtitle.

![Page 1 white-paper cover](assets/chapter-gallery/00-cover-page-01.png)

### Contents: page 3

The page presents six core chapters and the questions they answer, serving as both reader navigation and a scope check.

![Page 3 contents](assets/chapter-gallery/01-contents-page-03.png)

### Chart 1: page 4 / corporate architecture

The hierarchy connects leadership, two companies, and three brands in the most complete relationship view in the governance chapter.

![Page 4 corporate architecture](assets/chapter-gallery/02-governance-page-04.png)

### Chart 2: page 7 / brand portfolio matrix

A two-axis matrix distinguishes WANMIAN, GEERNA, and UIUP by user stage and brand value while showing a shared foundation and independent positioning.

![Page 7 brand portfolio matrix](assets/chapter-gallery/03-multi-brand-page-07.png)

### Chart 3: page 12 / product development system

The page connects user insight, material, merchandising, design development, pricing, production, and launch in one process and includes category allocation.

![Page 12 product development system](assets/chapter-gallery/04-product-material-page-12.png)

### Chart 4: page 17 / user journey

The journey maps awareness, interest, understanding, conversion, experience, and repurchase to content, channels, and user stages.

![Page 17 user journey](assets/chapter-gallery/05-media-operation-page-17.png)

## How the inputs work together

| Input | Question it answers | When to update |
|---|---|---|
| `brief.json` | What is the document, who is it for, how many pages, and what is delivered? | At the beginning of every project |
| `style-pack.json` | What colors, type sizes, spacing, and page rules apply? | After visual direction is approved |
| `references/taizhou-governance.md` | How do the company, organization, and governance operate? | After corporate facts are confirmed |
| `references/taizhou-content-library.md` | What are the brands, users, products, materials, and operating content? | Continuously during content research |
| `references/taizhou-visual-system.md` | How are corporate and brand identities visually distinguished? | After brand assets are approved |
| `references/taizhou-page-blueprint.md` | Which pages belong in full and compact editions? | Before final layout |

## What to replace for a new project

| TAIZHOU case field | Replace with |
|---|---|
| Corporate system, companies, and brand relationships | Actual organization, responsibilities, and brand portfolio |
| Three brand positions | Actual positioning, users, values, and channels |
| Product and material platform | Verified products, materials, processes, and evidence |
| Price bands and annual targets | Approved data or clearly labeled assumptions |
| Visual keywords and colors | Authorized logos, fonts, colors, and images |
| Five-year direction | A real roadmap with owners, dates, and metrics |

## More example instructions

### Diagnose content before layout

```text
Use $aos-publish-document to audit whether the supplied material can support six chapters: governance,
multi-brand strategy, product and material, visual system, media operations, and annual direction.
List facts, inferences, assumptions, and gaps. Do not generate the document yet. After source approval,
produce a 20-page blueprint.
```

### Preserve layout and update content only

```text
Use $aos-author-word with the TAIZHOU example as an editable structural reference. Preserve page size,
grid, heading hierarchy, table styles, and footer logic while rewriting the content from the new sources.
Do not copy TAIZHOU corporate facts, brand positioning, or operating data. Render every page and repair
pagination defects before delivery.
```

### Inspect PDF quality only

```text
Use $aos-process-pdf to inspect the TAIZHOU example PDF dimensions, metadata, and all 20 rendered pages.
Focus on Chinese fonts, fine table rules, light-colored text, image clarity, and chapter rhythm. Return
an issue list and do not modify the source.
```

### Expand to a 100+ page edition

```text
Use $aos-publish-document and read taizhou-page-blueprint.md to expand the 20-page compact case into a
100-130-page full edition. First create a chapter page budget and evidence-gap list. Do not fabricate
pages that lack factual or image support; identify them as missing-material items. Render and inspect
each chapter before merging the final DOCX and PDF.
```

## Acceptance baseline

- DOCX and PDF each contain 20 A4 pages;
- page order, headings, and primary tables align;
- DOCX contains no comments, tracked changes, or personal-author residue;
- PDF is unencrypted and contains no JavaScript, forms, or custom metadata;
- Chinese text renders normally with no boxes, clipping, overlaps, or unexpected blank pages;
- every simulated operating figure has an explicit label;
- representative pages are for quick review only; final delivery still requires individual page inspection.

Case content is available under CC BY 4.0. Trademark rights are outside the license scope.
