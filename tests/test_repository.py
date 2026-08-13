from __future__ import annotations

import json
import shutil
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
    assert manifest["version"] == project["project"]["version"] == "0.1.5"
    assert manifest["skills"] == "./skills/"
    assert marketplace["name"] == "aos-agent-skills"
    assert marketplace["plugins"][0]["name"] == manifest["name"]
    assert marketplace["plugins"][0]["source"]["path"] == "./plugins/aos-agent-skill-document"
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## [0.1.5]" in changelog


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
    english_readme = (ROOT / "README.en.md").read_text(encoding="utf-8")
    example_readme = (ROOT / "examples" / "taizhou-white-paper" / "README.md").read_text(
        encoding="utf-8"
    )
    cookbook = ROOT / "docs" / "usage-cookbook.md"
    getting_started = ROOT / "docs" / "getting-started.md"
    assert cookbook.is_file()
    assert getting_started.is_file()
    assert "docs/usage-cookbook.md" in readme
    assert "docs/getting-started.md" in readme
    assert 'docs/assets/readme-hero.svg' in readme
    assert 'docs/assets/readme-hero.en.svg' in english_readme
    for hero in ("readme-hero.svg", "readme-hero.en.svg"):
        hero_text = (ROOT / "docs" / "assets" / hero).read_text(encoding="utf-8")
        assert "<title" in hero_text
        assert "<desc" in hero_text
        assert "-apple-system" in hero_text
    tutorial = getting_started.read_text(encoding="utf-8")
    assert "codex plugin marketplace add axutse/aos-agent-skill-document" in tutorial
    assert "`/plugins`" in tutorial
    assert "codex plugin marketplace upgrade aos-agent-skills" in tutorial
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


def test_social_preview_matches_github_recommendations() -> None:
    preview = ROOT / "docs" / "assets" / "social-preview.png"
    assert preview.is_file()
    assert preview.stat().st_size < 1_000_000

    from PIL import Image

    with Image.open(preview) as image:
        assert image.format == "PNG"
        assert image.size == (1280, 640)


def test_chinese_and_english_documentation_are_paired() -> None:
    pairs = [
        (ROOT / "README.md", ROOT / "README.en.md"),
        (ROOT / "CHANGELOG.md", ROOT / "CHANGELOG.en.md"),
        (ROOT / "docs" / "getting-started.md", ROOT / "docs" / "getting-started.en.md"),
        (ROOT / "docs" / "usage-cookbook.md", ROOT / "docs" / "usage-cookbook.en.md"),
        (ROOT / "docs" / "feature-matrix.md", ROOT / "docs" / "feature-matrix.en.md"),
        (
            ROOT / "docs" / "skillhub-publishing.md",
            ROOT / "docs" / "skillhub-publishing.en.md",
        ),
        (
            ROOT / "examples" / "taizhou-white-paper" / "README.md",
            ROOT / "examples" / "taizhou-white-paper" / "README.en.md",
        ),
    ]
    for chinese, english in pairs:
        assert chinese.is_file()
        assert english.is_file()
        chinese_text = chinese.read_text(encoding="utf-8")
        english_text = english.read_text(encoding="utf-8")
        assert "[English]" in chinese_text or ">English<" in chinese_text
        assert "[简体中文]" in english_text or ">简体中文<" in english_text

    english_readme = (ROOT / "README.en.md").read_text(encoding="utf-8")
    english_example = (
        ROOT / "examples" / "taizhou-white-paper" / "README.en.md"
    ).read_text(encoding="utf-8")
    assert "Version 0.1.5" in english_readme
    assert "docs/getting-started.en.md" in english_readme
    assert "docs/usage-cookbook.en.md" in english_readme
    gallery_files = {
        "00-cover-page-01.png",
        "01-contents-page-03.png",
        "02-governance-page-04.png",
        "03-multi-brand-page-07.png",
        "04-product-material-page-12.png",
        "05-media-operation-page-17.png",
    }
    for filename in gallery_files:
        assert f"examples/taizhou-white-paper/assets/chapter-gallery/{filename}" in english_readme
        assert f"assets/chapter-gallery/{filename}" in english_example

    bilingual_reference = (
        PLUGIN
        / "skills"
        / "aos-publish-document"
        / "references"
        / "bilingual-delivery.md"
    )
    assert bilingual_reference.is_file()
    assert "references/bilingual-delivery.md" in (
        PLUGIN / "skills" / "aos-publish-document" / "SKILL.md"
    ).read_text(encoding="utf-8")


def test_skillhub_distribution_builds_from_canonical_sources() -> None:
    output = ROOT / "dist" / "skillhub-test" / "aos-agent-skill-document"
    if output.exists():
        shutil.rmtree(output)
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_skillhub_package.py"),
            "--output",
            str(output),
        ],
        check=True,
    )
    try:
        files = {path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file()}
        assert len(files) == 27
        assert "SKILL.md" in files
        assert "scripts/inspect_docx.py" in files
        assert "scripts/inspect_pdf.py" in files
        assert "references/bilingual-delivery.md" in files
        assert "assets/apple-editorial.json" in files
        skillhub_skill = (output / "SKILL.md").read_text(encoding="utf-8")
        assert "slug: aos-agent-skill-document" in skillhub_skill
        assert "version: 0.1.5" in skillhub_skill
        gallery_files = {
            "00-cover-page-01.png",
            "01-contents-page-03.png",
            "02-governance-page-04.png",
            "03-multi-brand-page-07.png",
            "04-product-material-page-12.png",
            "05-media-operation-page-17.png",
        }
        for filename in gallery_files:
            assert f"assets/chapter-gallery/{filename}" in files
            assert (
                f"examples/taizhou-white-paper/assets/chapter-gallery/{filename}"
                in skillhub_skill
            )
        assert "assets/readme-hero.svg" in files
        assert "assets/readme-hero.en.svg" in files
        assert "assets/social-preview.png" in files
        assert (output / "scripts" / "inspect_docx.py").read_bytes() == (
            PLUGIN / "skills" / "aos-author-word" / "scripts" / "inspect_docx.py"
        ).read_bytes()
    finally:
        shutil.rmtree(output)
