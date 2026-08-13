---
slug: aos-agent-skill-document
displayName: AOS Agent Skill · Document
version: 0.1.3
summary: 将资料制作或整理为经过全页渲染验收的专业 Word 与 PDF，支持中文、英文和中英双版本。
description: 面向白皮书、报告、提案、手册和品牌文档的端到端出版工作流，覆盖内容规划、可编辑 DOCX、PDF 转换、元数据清理和逐页视觉验收。
tags: [文档, Word, PDF, 白皮书, 报告, 双语, 视觉验收]
license: MIT
homepage: https://github.com/axutse/aos-agent-skill-document
---

# AOS Agent Skill · Document

将专业文档任务执行为可验证的出版流程：

```text
plan -> author -> render -> inspect -> revise -> verify
```

## 定位

把本 Skill 作为文档出版工作流使用，而不是在线 Office、外部转换服务、事实认证工具或专业签审服务。使用本地文档工具创建或修改可编辑 Word、导出固定版式 PDF、检查元数据，并在交付前逐页渲染验收。

本 Skill 自身不需要 API Key。除非用户明确要求并授权，不得把文件上传到外部模型或转换服务。

## 支持范围

- 从多份资料制作白皮书、报告、提案、手册和品牌文档；
- 新建或局部修改 DOCX，保留样式、表格、分节、页眉页脚和页码；
- 检查 PDF 的页数、尺寸、旋转、加密、表单、链接和元数据；
- 清理 Word/PDF 的个人元数据、评论和修订记录；
- 渲染全部页面，检查缺字、裁切、重叠、模糊、断表和异常空白页；
- 分别制作并验收中文、英文或两套独立中英文版本；
- 先验收样本，再按锁定规则批量生成同版式文档。

不包含扫描件 OCR、PDF 电子签章、Word/Acrobat 桌面界面自动化、业务事实认证和法务财务最终审批。

## 路由任务

根据任务选择最小工作流：

1. **完整出版**：从源资料到 DOCX、PDF 和全页验收。读取 `references/positioning-and-routing.md`、`references/editorial-design.md` 和 `references/qa-checklist.md`。
2. **Word 为主**：新建或修改 DOCX。读取 `references/docx-workflow.md`，使用 `scripts/inspect_docx.py`、`scripts/set_docx_high_fidelity.py`、`scripts/scrub_docx_metadata.py`、`scripts/render_docx.py` 和 `scripts/lo_convert_to_pdf.py`。
3. **PDF 为主**：审计、清理或渲染 PDF。读取 `references/pdf-workflow.md`，使用 `scripts/inspect_pdf.py`、`scripts/scrub_pdf_metadata.py`、`scripts/render_pdf.py` 和 `scripts/make_contact_sheet.py`。
4. **中英双版本**：读取 `references/bilingual-delivery.md`，先建立术语表，并分别验收每种语言的文件。

不要机械执行所有脚本。先根据用户的输入、输出和验收要求选择需要的步骤。

## 必需工作流

1. 在起草前检查全部输入资料，列出事实、推断、模拟值和缺失项。
2. 从上下文确认用途、读者、语言、页面尺寸、页数、风格、可编辑性和交付格式。
3. 为长文档建立章节结构和页面预算。
4. 保留已验证名称、数字、术语和原始含义；把未验证经营数字标记为 `PLANNING ASSUMPTION / 企划模拟值`。
5. 使用一致的编辑设计、标题层级、网格、表格和颜色系统。
6. 需要 DOCX 与 PDF 时，先完成并验收 DOCX，再转换和验收 PDF。
7. 结构检查之后渲染全部最终页面；联系表只能用于总览。
8. 在可读缩放下逐页检查裁切、重叠、缺字、模糊图片、断表、分页和页眉页脚。
9. 修复任何布局敏感问题后重新渲染并再次检查。
10. 公开发布前检查元数据、评论、修订记录、个人信息和常见密钥格式。
11. 最终只交付用户要求的文件，并报告路径、页数、验证结果和仍需人工确认的事项。

## Word 命令

```bash
python scripts/inspect_docx.py input.docx --json
python scripts/set_docx_high_fidelity.py input.docx output.docx
python scripts/scrub_docx_metadata.py input.docx public.docx
python scripts/render_docx.py public.docx --output-dir render --emit-pdf
python scripts/lo_convert_to_pdf.py public.docx output.pdf
```

DOCX 转 PDF 和 Word 页面渲染需要 LibreOffice。若不可用，只完成结构检查并明确披露限制。

## PDF 命令

```bash
python scripts/inspect_pdf.py input.pdf --json
python scripts/scrub_pdf_metadata.py input.pdf public.pdf
python scripts/render_pdf.py public.pdf --output-dir render --dpi 200
python scripts/make_contact_sheet.py 'render/page-*.png' --output contact-sheet.jpg
```

PDF 页面渲染需要 Poppler。联系表不能替代对每张页面图片的单独检查。

## 双语交付

用户没有指定版式时，为长文档默认输出两个独立语言版本。翻译前锁定公司、品牌、产品、指标和章节术语；没有正式译名时保留注册名称。保持事实、数字、单位、表格、图注和模拟值标签对齐，但不要为了强求相同页数而缩小到不可读字号。

分别重新打开、渲染和验收每个语言版本，不得因为中文版通过就自动批准英文版，反之亦然。

## 最终验收

- DOCX 可以重新打开并保持可编辑；
- PDF 可以重新打开，页数、尺寸和加密状态符合要求；
- 所有页面均在可读缩放下单独检查；
- 无缺字、裁切、重叠、断表、图片拉伸或异常空白页；
- 目录、页码、标题、页眉页脚和章节顺序正确；
- 评论、修订记录、个人元数据和敏感信息符合发布策略；
- 模拟值、占位内容和仍需人工确认事项得到清楚标记。

只有全部适用检查通过后，才能把文件描述为已完成视觉验收。
