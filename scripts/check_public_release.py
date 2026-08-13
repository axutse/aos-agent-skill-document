#!/usr/bin/env python3
"""Scan the repository for credentials, forbidden legacy content, and release hazards."""

from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path
from zipfile import BadZipFile, ZipFile

from pypdf import PdfReader

logging.getLogger("pypdf").setLevel(logging.ERROR)

SKIP_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "tmp"}
TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".json", ".yaml", ".yml", ".toml", ".xml", ".svg",
    ".html", ".css", ".js", ".ts", ".sh", ".gitignore",
}
OFFICE_SUFFIXES = {".docx"}
PDF_SUFFIXES = {".pdf"}
MAX_TRACKED_BYTES = 8 * 1024 * 1024
FORBIDDEN_BRAND = "美" + "尔" + "纳"
PLACEHOLDERS = ["[" + "TODO:", "YOUR_" + "GITHUB_USERNAME"]

SECRET_PATTERNS = {
    "provider-secret": re.compile(r"sk-[A-Za-z0-9][A-Za-z0-9_-]{15,}"),
    "github-token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "aws-access-key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "assigned-secret": re.compile(
        r"(?i)(?:api[_-]?key|access[_-]?token|password|secret)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    ),
}


def iter_files(root: Path, include_release_assets: bool):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if not include_release_assets and relative.parts[:1] == ("release-assets",) and path.suffix.lower() == ".pdf":
            continue
        yield path, relative


def text_from_docx(path: Path) -> str:
    parts: list[str] = []
    try:
        with ZipFile(path) as archive:
            for name in archive.namelist():
                if name.endswith((".xml", ".rels", ".txt")):
                    parts.append(archive.read(name).decode("utf-8", errors="ignore"))
    except BadZipFile:
        return ""
    return "\n".join(parts)


def text_from_pdf(path: Path) -> str:
    try:
        reader = PdfReader(path)
        if reader.is_encrypted:
            return ""
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception:
        return ""


def extract_searchable_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in OFFICE_SUFFIXES:
        return text_from_docx(path)
    if suffix in PDF_SUFFIXES:
        return text_from_pdf(path)
    if suffix in TEXT_SUFFIXES or path.name == ".gitignore":
        return path.read_text(encoding="utf-8", errors="ignore")
    return ""


def scan(root: Path, include_release_assets: bool) -> list[tuple[str, Path]]:
    findings: list[tuple[str, Path]] = []
    for path, relative in iter_files(root, include_release_assets):
        is_release_asset = relative.parts[:1] == ("release-assets",)
        if not is_release_asset and path.stat().st_size > MAX_TRACKED_BYTES:
            findings.append(("oversized-trackable-file", relative))
        if FORBIDDEN_BRAND in str(relative):
            findings.append(("forbidden-legacy-brand-in-path", relative))

        raw = path.read_bytes()
        raw_text = raw.decode("utf-8", errors="ignore")
        searchable = raw_text + "\n" + extract_searchable_text(path)
        if FORBIDDEN_BRAND in searchable:
            findings.append(("forbidden-legacy-brand", relative))
        for placeholder in PLACEHOLDERS:
            if placeholder in searchable:
                findings.append(("unfinished-placeholder", relative))
        for rule, pattern in SECRET_PATTERNS.items():
            if pattern.search(searchable):
                findings.append((rule, relative))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--include-release-assets", action="store_true")
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Repository root not found: {root}")

    findings = scan(root, args.include_release_assets)
    if findings:
        for rule, path in findings:
            print(f"FAIL {rule}: {path}")
        return 1
    scope = "repository and release assets" if args.include_release_assets else "trackable repository files"
    print(f"PASS: no release blockers found in {scope}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
