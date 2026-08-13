#!/usr/bin/env python3
"""Build the standalone SkillHub package from canonical Codex plugin sources."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "aos-agent-skill-document"
TEMPLATE = ROOT / "distributions" / "skillhub" / "aos-agent-skill-document"
DEFAULT_OUTPUT = ROOT / "dist" / "skillhub" / "aos-agent-skill-document"


REFERENCE_SOURCES = (
    PLUGIN / "skills" / "aos-publish-document" / "references",
    PLUGIN / "skills" / "aos-author-word" / "references",
    PLUGIN / "skills" / "aos-process-pdf" / "references",
)

SCRIPT_SOURCES = (
    PLUGIN / "skills" / "aos-author-word" / "scripts",
    PLUGIN / "skills" / "aos-process-pdf" / "scripts",
)

ASSET_FILES = (
    PLUGIN / "assets" / "icon.svg",
    PLUGIN / "skills" / "aos-publish-document" / "assets" / "apple-editorial.json",
    ROOT / "docs" / "assets" / "readme-hero.svg",
    ROOT / "docs" / "assets" / "readme-hero.en.svg",
    ROOT / "docs" / "assets" / "social-preview.png",
)

GALLERY_SOURCE = (
    ROOT / "examples" / "taizhou-white-paper" / "assets" / "chapter-gallery"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def validated_output(path: Path) -> Path:
    resolved = path.resolve()
    allowed_root = (ROOT / "dist").resolve()
    if resolved == allowed_root or allowed_root not in resolved.parents:
        raise ValueError(f"output must be inside {allowed_root}")
    return resolved


def copy_unique_files(sources: tuple[Path, ...], destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    for source_dir in sources:
        for source in sorted(source_dir.iterdir()):
            if not source.is_file():
                continue
            if source.name in seen:
                raise ValueError(f"duplicate package filename: {source.name}")
            seen.add(source.name)
            shutil.copy2(source, destination / source.name)


def build(output: Path) -> Path:
    output = validated_output(output)
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    shutil.copy2(TEMPLATE / "SKILL.md", output / "SKILL.md")
    copy_unique_files(REFERENCE_SOURCES, output / "references")
    copy_unique_files(SCRIPT_SOURCES, output / "scripts")

    assets = output / "assets"
    assets.mkdir()
    for source in ASSET_FILES:
        shutil.copy2(source, assets / source.name)

    gallery = assets / "chapter-gallery"
    shutil.copytree(GALLERY_SOURCE, gallery)

    file_count = sum(1 for path in output.rglob("*") if path.is_file())
    print(f"Built SkillHub package: {output}")
    print(f"Files: {file_count}")
    return output


if __name__ == "__main__":
    build(parse_args().output)
