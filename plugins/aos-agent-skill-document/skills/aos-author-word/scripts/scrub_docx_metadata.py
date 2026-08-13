#!/usr/bin/env python3
"""Remove personal and machine metadata from a DOCX package."""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

CP_NS = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
DC_NS = "http://purl.org/dc/elements/1.1/"
DCTERMS_NS = "http://purl.org/dc/terms/"
EP_NS = "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def scrub_core(data: bytes, author: str) -> bytes:
    root = etree.fromstring(data)
    creator = root.find(f"{{{DC_NS}}}creator")
    if creator is not None:
        creator.text = author
    last_modified_by = root.find(f"{{{CP_NS}}}lastModifiedBy")
    if last_modified_by is not None:
        last_modified_by.text = ""
    for xpath in [f"{{{DCTERMS_NS}}}created", f"{{{DCTERMS_NS}}}modified"]:
        node = root.find(xpath)
        if node is not None:
            root.remove(node)
    revision = root.find(f"{{{CP_NS}}}revision")
    if revision is not None:
        revision.text = "1"
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def scrub_app(data: bytes) -> bytes:
    root = etree.fromstring(data)
    for local_name in ("Company", "Manager"):
        node = root.find(f"{{{EP_NS}}}{local_name}")
        if node is not None:
            node.text = ""
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def scrub_word_xml(data: bytes) -> bytes:
    root = etree.fromstring(data)
    for element in root.iter():
        for attribute in list(element.attrib):
            if attribute.startswith(f"{{{W_NS}}}rsid"):
                del element.attrib[attribute]
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def scrub_content_types(data: bytes) -> bytes:
    root = etree.fromstring(data)
    for node in list(root):
        if node.get("PartName") == "/docProps/custom.xml":
            root.remove(node)
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def scrub_root_rels(data: bytes) -> bytes:
    root = etree.fromstring(data)
    for node in list(root):
        if str(node.get("Type", "")).endswith("/custom-properties"):
            root.remove(node)
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--author", default="")
    args = parser.parse_args()

    source = Path(args.input).expanduser().resolve()
    destination = Path(args.output).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Input DOCX not found: {source}")
    if source == destination:
        raise SystemExit("Input and output must be different files")
    destination.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(source, "r") as incoming, ZipFile(destination, "w", ZIP_DEFLATED) as outgoing:
        for item in incoming.infolist():
            if item.filename == "docProps/custom.xml":
                continue
            data = incoming.read(item.filename)
            if item.filename == "docProps/core.xml":
                data = scrub_core(data, args.author)
            elif item.filename == "docProps/app.xml":
                data = scrub_app(data)
            elif item.filename == "[Content_Types].xml":
                data = scrub_content_types(data)
            elif item.filename == "_rels/.rels":
                data = scrub_root_rels(data)
            elif item.filename.startswith("word/") and item.filename.endswith(".xml"):
                data = scrub_word_xml(data)
            new_item = deepcopy(item)
            outgoing.writestr(new_item, data)
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
