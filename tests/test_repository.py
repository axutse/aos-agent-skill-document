from __future__ import annotations

import json
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "aos-agent-skill-document"


def test_manifest_and_marketplace_are_consistent() -> None:
    manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    marketplace = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    assert manifest["name"] == "aos-agent-skill-document"
    assert manifest["version"] == project["project"]["version"] == "0.1.0"
    assert manifest["skills"] == "./skills/"
    assert marketplace["name"] == "aos-agent-skills"
    assert marketplace["plugins"][0]["name"] == manifest["name"]
    assert marketplace["plugins"][0]["source"]["path"] == "./plugins/aos-agent-skill-document"
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## [0.1.0]" in changelog


def test_three_skills_have_metadata() -> None:
    expected = {"aos-publish-document", "aos-author-word", "aos-process-pdf"}
    actual = {path.name for path in (PLUGIN / "skills").iterdir() if path.is_dir()}
    assert actual == expected
    for name in expected:
        skill = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        interface = (PLUGIN / "skills" / name / "agents" / "openai.yaml").read_text(encoding="utf-8")
        assert f"name: {name}" in skill
        assert "description:" in skill
        assert f"${name}" in interface


def test_public_release_scanner_passes() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_public_release.py"), "--root", str(ROOT)],
        check=True,
    )


def test_release_pdf_is_git_ignored() -> None:
    ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "release-assets/*.pdf" in ignore
    assert (ROOT / "release-assets" / "README.md").is_file()
