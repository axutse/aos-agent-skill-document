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
    assert manifest["version"] == project["project"]["version"] == "0.1.1"
    assert manifest["skills"] == "./skills/"
    assert marketplace["name"] == "aos-agent-skills"
    assert marketplace["plugins"][0]["name"] == manifest["name"]
    assert marketplace["plugins"][0]["source"]["path"] == "./plugins/aos-agent-skill-document"
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## [0.1.1]" in changelog


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


def test_usage_docs_and_chapter_gallery_are_complete() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    example_readme = (ROOT / "examples" / "taizhou-white-paper" / "README.md").read_text(
        encoding="utf-8"
    )
    cookbook = ROOT / "docs" / "usage-cookbook.md"
    getting_started = ROOT / "docs" / "getting-started.md"
    assert cookbook.is_file()
    assert getting_started.is_file()
    assert "docs/usage-cookbook.md" in readme
    assert "docs/getting-started.md" in readme
    tutorial = getting_started.read_text(encoding="utf-8")
    assert "codex plugin marketplace add axutse/aos-agent-skill-document" in tutorial
    assert "codex plugin add aos-agent-skill-document@aos-agent-skills" in tutorial
    assert "$aos-publish-document" in tutorial
    assert "$aos-author-word" in tutorial
    assert "$aos-process-pdf" in tutorial

    positioning = (
        PLUGIN
        / "skills"
        / "aos-publish-document"
        / "references"
        / "positioning-and-routing.md"
    )
    assert positioning.is_file()
    assert "references/positioning-and-routing.md" in (
        PLUGIN / "skills" / "aos-publish-document" / "SKILL.md"
    ).read_text(encoding="utf-8")

    gallery = ROOT / "examples" / "taizhou-white-paper" / "assets" / "chapter-gallery"
    expected = {
        "00-cover-page-01.png",
        "01-contents-page-03.png",
        "02-governance-page-04.png",
        "03-multi-brand-page-07.png",
        "04-product-material-page-12.png",
        "05-media-operation-page-17.png",
    }
    actual = {path.name for path in gallery.glob("*.png")}
    assert actual == expected
    assert len(actual) == 6
    assert not (gallery / "chapter-gallery.jpg").exists()
    for filename in expected:
        assert f"examples/taizhou-white-paper/assets/chapter-gallery/{filename}" in readme
        assert f"assets/chapter-gallery/{filename}" in example_readme
