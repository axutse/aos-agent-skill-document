#!/usr/bin/env python3
"""Remove PDF metadata while preserving page content and interactive objects."""

from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--title", default="")
    parser.add_argument("--author", default="")
    parser.add_argument("--subject", default="")
    parser.add_argument("--keywords", default="")
    args = parser.parse_args()

    source = Path(args.input).expanduser().resolve()
    destination = Path(args.output).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Input PDF not found: {source}")
    if source == destination:
        raise SystemExit("Input and output must be different files")

    reader = PdfReader(source)
    if reader.is_encrypted:
        raise SystemExit("Decrypt the PDF before scrubbing metadata")
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.metadata = None
    writer.xmp_metadata = None
    retained = {
        "/Title": args.title,
        "/Author": args.author,
        "/Subject": args.subject,
        "/Keywords": args.keywords,
    }
    writer.add_metadata({key: value for key, value in retained.items() if value})
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as stream:
        writer.write(stream)

    reopened = PdfReader(destination)
    if len(reopened.pages) != len(reader.pages):
        raise SystemExit("Page count changed during metadata scrub")
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
