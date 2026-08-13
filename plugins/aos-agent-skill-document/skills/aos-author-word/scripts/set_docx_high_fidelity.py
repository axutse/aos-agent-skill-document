#!/usr/bin/env python3
import argparse
import shutil
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from lxml import etree

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NSMAP = {"w": W_NS}


def patch_settings(data: bytes) -> bytes:
    root = etree.fromstring(data)
    if root.find("w:doNotCompressPictures", namespaces=NSMAP) is None:
        node = etree.Element(f"{{{W_NS}}}doNotCompressPictures")
        root.append(node)
    dpi = root.find("w:defaultImageDpi", namespaces=NSMAP)
    if dpi is None:
        dpi = etree.Element(f"{{{W_NS}}}defaultImageDpi")
        root.append(dpi)
    dpi.set(f"{{{W_NS}}}val", "330")
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def main() -> int:
    parser = argparse.ArgumentParser(description="Disable Word image compression and set high default image DPI.")
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()

    src = Path(args.input).expanduser().resolve()
    dst = Path(args.output).expanduser().resolve()
    if not src.is_file():
        raise SystemExit(f"Input DOCX not found: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(src, "r") as zin, ZipFile(dst, "w", ZIP_DEFLATED) as zout:
        names = set(zin.namelist())
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/settings.xml":
                data = patch_settings(data)
            zout.writestr(item, data)
        if "word/settings.xml" not in names:
            raise SystemExit("DOCX package is missing word/settings.xml")
    print(dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
