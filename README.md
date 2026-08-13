# AOS Agent Skill · Document

当前版本：`0.1.1`

[![Release](https://img.shields.io/github/v/release/axutse/aos-agent-skill-document)](https://github.com/axutse/aos-agent-skill-document/releases)
[![CI](https://github.com/axutse/aos-agent-skill-document/actions/workflows/validate.yml/badge.svg)](https://github.com/axutse/aos-agent-skill-document/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

面向 Codex 与兼容 Agent 的开源文档技能包。它把专业文档工作收敛为一条可验证流程：规划内容、创建或修改 Word、导出 PDF、逐页检查画面、清理元数据，最后交付可编辑文件与固定版式文件。

```text
plan -> author -> render -> inspect -> revise -> verify
```

## 项目定位

`AOS Agent Skill · Document` 是一套面向 Agent 的**文档出版工作流插件**，不是在线 Office、云端转换服务或通用聊天机器人。它把 Codex 的内容理解能力与本地文档工具组合起来，让“生成文件”升级为“生成、渲染、检查、修复、再验收”的完整交付。

它适合：

- 需要稳定产出 DOCX 与 PDF 的个人、内容团队、品牌团队和咨询团队；
- 需要保留 Word 可编辑性，同时保证 PDF 画面一致的交付；
- 需要把报告、白皮书、提案、手册和品牌文档做成可复用流程的场景；
- 需要公开发布前检查页面、元数据、隐私和密钥残留的项目。

它不负责：

- 替代 Microsoft Word、Adobe Acrobat 或人工最终签审；
- 自动证明业务数字、事实来源、版权和商标授权；
- 在未安装 LibreOffice 或 Poppler 时承诺完整渲染验收；
- 上传文件到外部模型或转换 API。插件本身不需要 API Key。

默认交付契约是：**源资料检查 + 内容/页面计划 + 可编辑 DOCX + 固定版式 PDF + 全页视觉验收 + 公开发布检查**。用户只需要其中一部分时，技能会按要求缩小范围。

## 先看成果

TAIZHOU 公开案例包含 20 页可编辑 DOCX、对应 PDF、完整联系表和可重复运行的生成器。下面严格展示 6 张局部放大图：封面、目录，以及企业架构、品牌组合、商品开发和用户旅程四张高信息量图表页。

<table>
  <tr>
    <td width="50%"><strong>首页 / 第 1 页</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/00-cover-page-01.png" alt="TAIZHOU 白皮书首页"></td>
    <td width="50%"><strong>目录 / 第 3 页</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/01-contents-page-03.png" alt="TAIZHOU 白皮书目录"></td>
  </tr>
  <tr>
    <td width="50%"><strong>企业架构 / 第 4 页</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/02-governance-page-04.png" alt="TAIZHOU 企业架构图"></td>
    <td width="50%"><strong>品牌组合 / 第 7 页</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/03-multi-brand-page-07.png" alt="TAIZHOU 品牌组合矩阵"></td>
  </tr>
  <tr>
    <td width="50%"><strong>商品开发 / 第 12 页</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/04-product-material-page-12.png" alt="TAIZHOU 商品开发系统"></td>
    <td width="50%"><strong>用户旅程 / 第 17 页</strong><br><img src="examples/taizhou-white-paper/assets/chapter-gallery/05-media-operation-page-17.png" alt="TAIZHOU 用户旅程"></td>
  </tr>
</table>

更多高清页面、章节说明与复刻方法见 [TAIZHOU 案例说明](examples/taizhou-white-paper/README.md)。完整 149 页案例可从 [v0.1.1 Release](https://github.com/axutse/aos-agent-skill-document/releases/tag/v0.1.1) 下载。

## 包含的技能

| Skill | 最适合的任务 | 主要输出 |
|---|---|---|
| `$aos-publish-document` | 从零制作白皮书、报告、提案、手册或品牌文档 | DOCX + PDF + 页面验收 |
| `$aos-author-word` | 新建、修改、修复或公开发布 Word | 可编辑 DOCX，可选 PDF |
| `$aos-process-pdf` | 检查、清理、渲染或验证现有 PDF | 处理后 PDF + 检查结果 |

如果同时需要 Word 和 PDF，优先使用 `$aos-publish-document`。它会先完成并验证 DOCX，再转换和验证 PDF。

三项技能不是三个互相冲突的程序：`$aos-publish-document` 是总编排入口，另外两项分别完成 Word 与 PDF 的专业处理。完整的选择规则、输入模板和首次交付步骤见 [从安装到首次交付](docs/getting-started.md)。

## 3 分钟开始使用

> 第一次使用建议打开 [完整入门教程](docs/getting-started.md)，其中包含安装验证、三个完整操作案例、更新、卸载和故障排查。

### 1. 安装

```bash
codex plugin marketplace add axutse/aos-agent-skill-document
codex plugin add aos-agent-skill-document@aos-agent-skills
```

安装后新建一个 Codex 任务，使新的 Skill 元数据进入上下文。

### 2. 准备输入

最低限度只需提供：

- 文档目标，例如品牌白皮书、年度报告或项目提案；
- 原始资料所在文件或目录；
- 希望交付 DOCX、PDF，还是两者都要；
- 语言、页数、风格和截止要求。

资料较完整时，建议一并提供品牌名称、章节清单、已验证数据、图片、Logo、颜色和不能改动的术语。

### 3. 复制第一条指令

```text
使用 $aos-publish-document，读取我提供的全部资料，先给出章节与页面计划，
再制作一份 20 页左右的中文品牌白皮书。风格简洁、结论先行、留白充分。
输出可编辑 DOCX 和对应 PDF，清理个人元数据，并逐页检查字体、图片、表格、
页码、页眉页脚、裁切和重叠问题。经营数字如果未经验证，标记为企划模拟值。
```

### 4. 验收结果

一次完整交付通常应包括：

- 可编辑 DOCX；
- 固定版式 PDF；
- 页数、尺寸、元数据和字体检查结果；
- 全页渲染验收结论；
- 用户明确要求时提供页面联系表或 QA 图片。

## 常用使用案例

### 从零制作品牌白皮书

```text
使用 $aos-publish-document，把资料目录中的品牌介绍、产品信息、组织架构和图片
整理为一份 24 页品牌白皮书。先输出目录和页面蓝图，确认信息来源，完成 DOCX 后
导出 PDF。每页只表达一个核心判断，并逐页完成视觉验收。
```

### 修改现有 Word，不破坏原有结构

```text
使用 $aos-author-word，修改这份 Word 的第 2、5、8 节。保留现有样式、页眉页脚、
目录和分页，只更新指定内容。修改后清理作者与修订元数据，渲染全部页面并报告变化。
```

### 检查准备公开的 PDF

```text
使用 $aos-process-pdf，检查这个 PDF 的页数、页面尺寸、旋转、加密、表单、链接和
元数据，渲染全部页面，找出缺字、模糊图片、裁切、重叠和异常空白页。不要改文件，
先给我问题清单和修复优先级。
```

### 将内部报告整理为公开版本

```text
使用 $aos-publish-document，把内部报告整理为可公开版本。删除评论、修订记录、个人
元数据、密钥和客户隐私，保留可公开内容，输出 DOCX 与 PDF，并生成公开前检查摘要。
```

### 批量生成同版式报告

```text
使用 $aos-publish-document，以已确认的参考文档为版式标准，读取数据目录中的项目资料，
按项目分别生成 DOCX 与 PDF。保持章节、字号、间距、表格和页码一致，同时保留每个项目
自己的标题、数据和图片。先生成一个样本并验收，再处理剩余项目。
```

更多场景，包括年度报告、项目提案、SOP 手册、品牌规范和批量交付，见 [使用案例与提示词手册](docs/usage-cookbook.md)。

## TAIZHOU 案例包含什么

[`examples/taizhou-white-paper/`](examples/taizhou-white-paper/) 提供：

- `brief.json`：标题、受众、页数、品牌和模拟值规则；
- `style-pack.json`：颜色、字体层级、页面网格和编辑设计规则；
- `references/`：企业治理、多品牌、商品材料、视觉系统和页面蓝图；
- `generate_example.py`：从结构化资料生成 DOCX；
- `build_release.py`：生成、清理、转换、渲染并验证完整交付；
- `output/`：20 页 DOCX、PDF 与完整联系表；
- `assets/chapter-gallery/`：封面、目录和四张高清图表代表页面。

案例只使用 TAIZHOU、WANMIAN / 万棉尚品、GEERNA / 哥尔纳和 UIUP 架构。所有内置经营数字均为 `PLANNING ASSUMPTION / 企划模拟值`。

## 本地复现案例

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/taizhou-white-paper/build_release.py \
  --output-dir examples/taizhou-white-paper/output \
  --qa-dir /tmp/taizhou-example-qa
```

DOCX 渲染需要 LibreOffice，PDF 渲染需要 Poppler。构建流程会生成 DOCX、应用高清图片设置、清理元数据、导出 PDF、渲染全部页面并生成联系表。

## 仓库结构

```text
.
├── .agents/plugins/marketplace.json
├── docs/
│   ├── getting-started.md
│   └── usage-cookbook.md
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

## 开发与验证

```bash
python scripts/check_public_release.py --root .
pytest
```

发布检查会扫描常见密钥格式、未完成占位内容、非 TAIZHOU 品牌残留、Office/PDF 文本及超大 Git 文件。

## 数据与安全

- 插件不需要 API Key，也不连接外部模型或服务。
- 不要提交凭据、私有合同、客户资料、身份信息或未获授权的字体文件。
- 曾经粘贴到聊天、终端、Issue 或提交历史的密钥，应在提供商处撤销并重新生成。
- 公开前同时检查正文、文件属性、评论、修订记录、附件和 PDF 元数据。

## License

- 代码、Skill、脚本和仓库文档：MIT
- `examples/taizhou-white-paper/`：CC BY 4.0
- 许可证不授予 TAIZHOU 或案例品牌的商标权
