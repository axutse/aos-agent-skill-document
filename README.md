# AOS Agent Skill · Document

当前版本：`0.1.0`

[![Release](https://img.shields.io/github/v/release/axutse/aos-agent-skill-document)](https://github.com/axutse/aos-agent-skill-document/releases)
[![CI](https://github.com/axutse/aos-agent-skill-document/actions/workflows/validate.yml/badge.svg)](https://github.com/axutse/aos-agent-skill-document/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

面向 Codex 与兼容 Agent 的开源文档技能包：规划、创建、编辑、检查、渲染和验证专业 Word/PDF，并附带可重复生成的 TAIZHOU 品牌企业白皮书案例。

![TAIZHOU 20 页公开案例联系表](examples/taizhou-white-paper/output/TAIZHOU品牌企业白皮书_示例版_联系表.jpg)

## 包含的技能

| Skill | 作用 |
|---|---|
| `aos-publish-document` | 选择 DOCX-first 或 PDF-first 路线，统一出版设计与最终验收 |
| `aos-author-word` | 创建、修改、检查、清理元数据、渲染和转换 DOCX |
| `aos-process-pdf` | 检查、清理元数据、渲染和验证 PDF，生成页面联系表 |

所有工作流都遵循：

```text
plan -> author -> render -> inspect -> revise -> verify
```

## TAIZHOU 开源案例

[`examples/taizhou-white-paper/`](examples/taizhou-white-paper/) 提供：

- 结构化 `brief.json`
- Apple-inspired 编辑设计 Style Pack
- 20 页可编辑 DOCX
- 20 页对应 PDF
- 全页联系表
- 可重复运行的 Python 生成器
- TAIZHOU 企业治理、多品牌、商品材料和视觉系统参考内容

案例只使用 TAIZHOU、WANMIAN / 万棉尚品、GEERNA / 哥尔纳和 UIUP 架构。所有内置经营数字均为企划模拟值。

149 页完整 TAIZHOU 案例在发布准备目录中作为 GitHub Release 附件管理，不进入 Git 历史。

## 仓库结构

```text
.
├── .agents/plugins/marketplace.json
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

## 安装

### 从本地仓库测试

```bash
codex plugin marketplace add /absolute/path/to/aos-agent-skill-document
codex plugin add aos-agent-skill-document@aos-agent-skills
```

安装后新建一个 Codex 任务，让新的 Skill 元数据进入上下文。

### 从 GitHub 安装

```bash
codex plugin marketplace add axutse/aos-agent-skill-document
codex plugin add aos-agent-skill-document@aos-agent-skills
```

## 使用示例

```text
使用 $aos-publish-document，根据我的资料制作一份 Apple 风格品牌白皮书，
输出可编辑 DOCX 和 PDF，并逐页检查排版。
```

```text
使用 $aos-author-word，检查并修改这份 Word 报告，保留原有结构，
清理个人元数据并完成渲染验收。
```

```text
使用 $aos-process-pdf，检查这个 PDF 的页数、尺寸、元数据、链接、
字体渲染和模糊页面，并生成联系表。
```

## 开发与验证

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_public_release.py --root .
pytest
python examples/taizhou-white-paper/build_release.py \
  --output-dir examples/taizhou-white-paper/output \
  --qa-dir /tmp/taizhou-example-qa
```

DOCX 渲染需要 LibreOffice，PDF 渲染需要 Poppler。

## 数据与安全

- 插件不需要 API Key，也不连接外部模型或服务。
- 仓库不应包含凭据、私有合同、客户资料、身份信息或字体文件。
- 发布检查会扫描常见密钥格式、占位内容、非 TAIZHOU 品牌残留、Office/PDF 文本及超大 Git 文件。
- 任何曾经粘贴到聊天、终端、Issue 或提交历史的密钥都应在提供商处撤销并重新生成。

## License

- 代码、Skill、脚本和仓库文档：MIT
- `examples/taizhou-white-paper/`：CC BY 4.0
- 许可证不授予 TAIZHOU 或案例品牌的商标权
