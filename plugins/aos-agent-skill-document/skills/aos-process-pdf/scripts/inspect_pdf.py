#!/usr/bin/env python3
"""Inspect PDF metadata, page geometry, links, images, and form fields."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from pypdf import PdfReader
from pypdf.generic import DictionaryObject


def _plain(value):
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _resource_counts(page) -> tuple[int, int]:
    resources = page.get("/Resources") or {}
    xobjects = resources.get("/XObject") if isinstance(resources, DictionaryObject) else None
    images = 0
    if xobjects:
        for ref in xobjects.values():
            try:
                if ref.get_object().get("/Subtype") == "/Image":
                    images += 1
            except Exception:
                continue

    links = 0
    for ref in page.get("/Annots") or []:
        try:
            if ref.get_object().get("/Subtype") == "/Link":
                links += 1
        except Exception:
            continue
    return images, links


def inspect(path: Path) -> dict:
    reader = PdfReader(path)
    pages = []
    if not reader.is_encrypted:
        for index, page in enumerate(reader.pages, start=1):
            images, links = _resource_counts(page)
            box = page.mediabox
            pages.append(
                {
                    "page": index,
                    "width_pt": round(float(box.width), 2),
                    "height_pt": round(float(box.height), 2),
                    "rotation": int(page.get("/Rotate", 0) or 0),
                    "images": images,
                    "links": links,
                }
            )

    metadata = {str(k): _plain(v) for k, v in (reader.metadata or {}).items()}
    fields = reader.get_fields() if not reader.is_encrypted else None
    return {
        "file": str(path),
        "size_bytes": path.stat().st_size,
        "pages": len(reader.pages) if not reader.is_encrypted else None,
        "encrypted": reader.is_encrypted,
        "metadata": metadata,
        "form_fields": len(fields or {}),
        "page_details": pages,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    source = Path(args.input).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Input PDF not found: {source}")

    report = inspect(source)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"File: {source}")
        print(f"Pages: {report['pages']}")
        print(f"Encrypted: {report['encrypted']}")
        print(f"Form fields: {report['form_fields']}")
        print(f"Metadata: {report['metadata']}")
        for page in report["page_details"]:
            print(
                f"Page {page['page']:03d}: {page['width_pt']} x {page['height_pt']} pt, "
                f"rotation={page['rotation']}, images={page['images']}, links={page['links']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
