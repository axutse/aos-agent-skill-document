# SkillHub publishing

[简体中文](skillhub-publishing.md) | [English](skillhub-publishing.en.md)

This repository supports both a Codex Plugin and a standalone SkillHub distribution. Both are generated from the same canonical scripts and references, avoiding manual maintenance of duplicate functionality.

## Two distribution forms

| Channel | Distribution unit | Intended users |
|---|---|---|
| Codex Plugin | One plugin containing three focused skills | Codex Plugin/Marketplace users |
| SkillHub | One unified `aos-agent-skill-document` skill | SkillHub and compatible Agent users |

The SkillHub edition combines publishing, Word, and PDF workflows in one skill and routes each task to the required scripts.

## Build the package

Run from the repository root:

```bash
python scripts/build_skillhub_package.py
```

Output:

```text
dist/skillhub/aos-agent-skill-document/
├── SKILL.md
├── assets/
├── references/
└── scripts/
```

`dist/` is ignored by Git. The builder copies scripts, references, and assets from the canonical `plugins/aos-agent-skill-document/` source so that the SkillHub package cannot silently drift from the Codex Plugin.

## Local validation

Install SkillHub CLI:

```bash
curl -fsSL https://skillhub.cn/install/install.sh | bash -s -- --cli-only
```

Run the dry-run:

```bash
skillhub publish dist/skillhub/aos-agent-skill-document \
  --host https://api.skillhub.cn \
  --dry-run
```

Expected result:

```text
✓ Dry-run passed: aos-agent-skill-document@0.1.5
```

## Authenticate and publish

The publisher must sign in to SkillHub, complete real-name verification, and create an API Token in the personal dashboard. Never place the token in the repository, chat, terminal logs, or plain-text CI configuration.

```bash
skillhub login --key "$SKILLHUB_KEY" --host https://api.skillhub.cn
skillhub auth whoami --host https://api.skillhub.cn
skillhub publish dist/skillhub/aos-agent-skill-document \
  --host https://api.skillhub.cn \
  --changelog "Added a feature scope matrix, bilingual documentation, and a standalone SkillHub package"
```

A successful submission returns `status=pending_review`. This means the version entered platform review; it becomes publicly visible only after approval.

See SkillHub's official [CLI and Agent publishing guide](https://skillhub.cn/tutorials#publish-via-cli).

## Version synchronization

- Use the same SemVer for the Codex Plugin, `pyproject.toml`, SkillHub `SKILL.md`, and GitHub Release.
- Keep `slug: aos-agent-skill-document` unchanged for every SkillHub update.
- Rebuild the package and run `--dry-run` before every release.
- GitHub and SkillHub changelogs should describe the same feature set.
- Track SkillHub review status separately from GitHub Release status; do not describe a pending submission as publicly listed.
