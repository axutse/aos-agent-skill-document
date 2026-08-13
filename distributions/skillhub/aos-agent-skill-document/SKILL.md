---
slug: aos-agent-skill-document
displayName: AOS Agent Skill · Document
version: 0.1.5
summary: 将资料制作或整理为经过全页渲染验收的专业 Word 与 PDF，支持中文、英文和中英双版本。
description: 面向白皮书、报告、提案、手册和品牌文档的端到端出版工作流，覆盖内容规划、可编辑 DOCX、PDF 转换、元数据清理和逐页视觉验收。
tags: [文档, Word, PDF, 白皮书, 报告, 双语, 视觉验收]
license: MIT
homepage: https://github.com/axutse/aos-agent-skill-document
---

# AOS Agent Skill · Document

> 让 Agent 交付完成的文档，而不只是生成一个文件。

规划内容 · 创建或修改 Word · 导出 PDF · 逐页检查 · 清理公开发布信息

![AOS Agent Skill Document：从资料到 Word、PDF 与逐页视觉验收](https://raw.githubusercontent.com/axutse/aos-agent-skill-document/main/docs/assets/readme-hero.svg)

## 一眼看懂

`AOS Agent Skill · Document` 是面向 Codex 与兼容 Agent 的开源文档出版工作流。它把内容理解与本地文档工具组合成一条可验证链路：

```text
PLAN  ->  AUTHOR  ->  RENDER  ->  INSPECT  ->  REVISE  ->  VERIFY
规划       制作        渲染         检查         修复         验收
```

| 能力 | 说明 |
|---|---|
| 完整交付 | 从资料与页面计划，到可编辑 DOCX、固定版式 PDF 和验收结论 |
| 本地优先 | 不依赖外部转换服务；Skill 本身不需要 API Key |
| 视觉验收 | 渲染全部页面，逐页检查缺字、裁切、重叠、断表、模糊和异常空白 |
| 公开发布 | 检查作者信息、评论、修订记录、个人元数据、隐私与常见密钥残留 |
| 中英双语 | 支持中文、英文或两套独立版本，保持术语、数据和图表对齐 |
| 可重复制作 | 先验收一个样本，再按锁定的版式、章节和字段规则批量生成 |

默认交付契约：**源资料检查 + 内容与页面计划 + 可编辑 DOCX + 固定版式 PDF + 全页视觉验收 + 公开发布检查**。如果只需要其中一部分，Skill 会按要求缩小范围。

## 先看成果

TAIZHOU 开源案例包含 20 页可编辑 DOCX、对应 PDF、完整联系表和可重复运行的生成器。下面严格展示 6 张放大页面：封面、目录，以及企业架构、品牌组合、商品开发和用户旅程四张高信息量图表页。

### 首页 · 第 1 页

品牌主张与出版物层级。

![TAIZHOU 白皮书首页](https://raw.githubusercontent.com/axutse/aos-agent-skill-document/main/examples/taizhou-white-paper/assets/chapter-gallery/00-cover-page-01.png)

### 目录 · 第 3 页

章节结构与阅读路径。

![TAIZHOU 白皮书目录](https://raw.githubusercontent.com/axutse/aos-agent-skill-document/main/examples/taizhou-white-paper/assets/chapter-gallery/01-contents-page-03.png)

### 企业架构 · 第 4 页

治理关系与职责结构。

![TAIZHOU 企业架构图](https://raw.githubusercontent.com/axutse/aos-agent-skill-document/main/examples/taizhou-white-paper/assets/chapter-gallery/02-governance-page-04.png)

### 品牌组合 · 第 7 页

多品牌定位矩阵。

![TAIZHOU 品牌组合矩阵](https://raw.githubusercontent.com/axutse/aos-agent-skill-document/main/examples/taizhou-white-paper/assets/chapter-gallery/03-multi-brand-page-07.png)

### 商品开发 · 第 12 页

商品与材料工作流。

![TAIZHOU 商品开发系统](https://raw.githubusercontent.com/axutse/aos-agent-skill-document/main/examples/taizhou-white-paper/assets/chapter-gallery/04-product-material-page-12.png)

### 用户旅程 · 第 17 页

内容触点与运营闭环。

![TAIZHOU 用户旅程](https://raw.githubusercontent.com/axutse/aos-agent-skill-document/main/examples/taizhou-white-paper/assets/chapter-gallery/05-media-operation-page-17.png)

[查看高清案例与复刻方法](https://github.com/axutse/aos-agent-skill-document/tree/main/examples/taizhou-white-paper) · [下载 149 页完整案例](https://github.com/axutse/aos-agent-skill-document/releases/tag/v0.1.5)

## 已实现能力

| 范围 | 已实现能力 | 状态 |
|---|---|:---:|
| 内容规划 | 多资料读取、事实清单、章节结构、页面预算 | ✅ |
| Word | 新建或局部修改 DOCX，保留样式与可编辑结构 | ✅ |
| Word | 标题、目录、表格、图片、分节、页眉页脚、页码 | ✅ |
| PDF | 页数、尺寸、旋转、加密、链接、表单、元数据检查 | ✅ |
| 视觉验收 | DOCX/PDF 全页渲染、逐页检查、修复后重新验收 | ✅ |
| 公开发布 | 清理作者信息、评论、修订记录和个人元数据 | ✅ |
| 双语交付 | 中文、英文、两套独立中英文版本及术语对齐 | ✅ |
| 批量交付 | 先生成样本，确认后按统一规则批量制作 | ✅ |
| 开源案例 | 20 页可编辑样例、149 页完整案例、生成器、QA 图片 | ✅ |
| 本地处理 | 不需要额外 API Key，不上传到外部转换服务 | ✅ |

[查看完整功能条件与暂不支持范围](https://github.com/axutse/aos-agent-skill-document/blob/main/docs/feature-matrix.md)

## 3 分钟开始

### 1. 安装

把下面这句话发送给支持 SkillHub 的 Agent：

```text
请根据 https://skillhub.cn/install/skillhub.md，
安装 @user_6152932a/aos-agent-skill-document。
```

也可以使用 SkillHub CLI：

```bash
skillhub install aos-agent-skill-document --namespace user_6152932a
```

### 2. 准备输入

最低限度只需说明文档目标与受众、原始资料所在文件或目录、需要 DOCX/PDF/两者，以及语言、页数、风格和截止要求。资料较完整时，再提供品牌名称、章节清单、已验证数据、图片、Logo、颜色和不能改动的术语。

### 3. 复制第一条指令

```text
使用 aos-agent-skill-document，读取我提供的全部资料，先给出章节与页面计划，
再制作一份 20 页左右的中文品牌白皮书。风格简洁、结论先行、留白充分。
输出可编辑 DOCX 和对应 PDF，清理个人元数据，并逐页检查字体、图片、表格、
页码、页眉页脚、裁切和重叠问题。经营数字如果未经验证，标记为企划模拟值。
```

[打开完整入门教程](https://github.com/axutse/aos-agent-skill-document/blob/main/docs/getting-started.md) · [查看更多提示词](https://github.com/axutse/aos-agent-skill-document/blob/main/docs/usage-cookbook.md)

## 使用案例

### 从零制作品牌白皮书

```text
使用 aos-agent-skill-document，把资料目录中的品牌介绍、产品信息、组织架构和图片
整理为一份 24 页品牌白皮书。先输出目录和页面蓝图，确认信息来源，完成 DOCX 后
导出 PDF。每页只表达一个核心判断，并逐页完成视觉验收。
```

### 修改现有 Word，不破坏原有结构

```text
使用 aos-agent-skill-document，修改这份 Word 的第 2、5、8 节。保留现有样式、
页眉页脚、目录和分页，只更新指定内容。修改后清理作者与修订元数据，
渲染全部页面并报告变化。
```

### 只读检查准备公开的 PDF

```text
使用 aos-agent-skill-document，检查这个 PDF 的页数、页面尺寸、旋转、加密、表单、
链接和元数据，渲染全部页面，找出缺字、模糊图片、裁切、重叠和异常空白页。
不要改文件，先给我问题清单和修复优先级。
```

### 将内部报告整理为公开版本

```text
使用 aos-agent-skill-document，把内部报告整理为可公开版本。删除评论、修订记录、
个人元数据、密钥和客户隐私，保留可公开内容，输出 DOCX 与 PDF，
并生成公开前检查摘要。
```

### 批量生成同版式报告

```text
使用 aos-agent-skill-document，以已确认的参考文档为版式标准，读取数据目录中的项目资料，
按项目分别生成 DOCX 与 PDF。先生成一个样本并验收，再按锁定的章节、字号、间距、
表格和页码规则处理剩余项目。
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

## 开源与安全

- GitHub 项目主页：[axutse/aos-agent-skill-document](https://github.com/axutse/aos-agent-skill-document)
- 代码、Skill、脚本和仓库文档使用 MIT License。
- `examples/taizhou-white-paper/` 案例内容使用 CC BY 4.0。
- 许可证不授予 TAIZHOU 或案例品牌的商标权。
- 不要把凭据、私有合同、客户资料、身份信息或未获授权字体写入公开版本。
