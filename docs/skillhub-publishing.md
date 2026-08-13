# SkillHub 发布说明

[简体中文](skillhub-publishing.md) | [English](skillhub-publishing.en.md)

本仓库同时支持 Codex Plugin 和 SkillHub 单 Skill 两种发行方式。两者共用同一套核心脚本与参考资料，不需要手工维护两份功能代码。

## 两种发行形态

| 渠道 | 发行单位 | 适合用户 |
|---|---|---|
| Codex Plugin | 一个插件，内部包含三项专用 Skill | 使用 Codex Plugin/Marketplace 的用户 |
| SkillHub | 一个统一的 `aos-agent-skill-document` Skill | 使用 SkillHub 或兼容 Agent 的用户 |

SkillHub 版本把完整出版、Word 和 PDF 三套工作流合并到一个 Skill 中，通过任务路由选择需要的脚本。

## 构建发行包

在仓库根目录执行：

```bash
python scripts/build_skillhub_package.py
```

输出目录：

```text
dist/skillhub/aos-agent-skill-document/
├── SKILL.md
├── assets/
├── references/
└── scripts/
```

`dist/` 已被 Git 忽略。构建器从 `plugins/aos-agent-skill-document/` 的规范源文件复制脚本、参考资料和资产，从而避免发行包与 Codex Plugin 出现功能漂移。

## 发布前预检

安装 SkillHub CLI：

```bash
curl -fsSL https://skillhub.cn/install/install.sh | bash -s -- --cli-only
```

执行本地预检：

```bash
skillhub publish dist/skillhub/aos-agent-skill-document \
  --host https://api.skillhub.cn \
  --dry-run
```

预期输出：

```text
✓ Dry-run passed: aos-agent-skill-document@0.1.4
```

## 登录和正式发布

发布者需要先在 SkillHub 完成登录、实名认证，并在个人中心创建 API Token。不要把 Token 写入仓库、聊天、终端日志或 CI 明文配置。

```bash
skillhub login --key "$SKILLHUB_KEY" --host https://api.skillhub.cn
skillhub auth whoami --host https://api.skillhub.cn
skillhub publish dist/skillhub/aos-agent-skill-document \
  --host https://api.skillhub.cn \
  --changelog "新增功能范围清单、双语文档和 SkillHub 独立发行包"
```

发布成功会返回 `status=pending_review`，代表已提交平台审核；审核通过后才会在技能广场公开显示。

官方流程见 [通过 CLI 和 Agent 发布 Skill](https://skillhub.cn/tutorials#publish-via-cli)。

## 版本同步规则

- Codex Plugin、`pyproject.toml`、SkillHub `SKILL.md` 和 GitHub Release 使用同一个 SemVer。
- SkillHub 更新必须保持 `slug: aos-agent-skill-document` 不变。
- 每次发布前重新构建发行包并执行 `--dry-run`。
- GitHub 和 SkillHub 的更新日志应描述同一批功能变化。
- SkillHub 审核状态与 GitHub Release 状态分别记录，不把“已提交审核”描述成“已公开上架”。
