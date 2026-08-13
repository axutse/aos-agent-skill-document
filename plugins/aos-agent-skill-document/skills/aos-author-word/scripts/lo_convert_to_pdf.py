#!/usr/bin/env python3
import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


def bundled_fontconfig(executable: str) -> Path | None:
    launcher = Path(executable).expanduser().resolve()
    for parent in (launcher.parent, *launcher.parents):
        candidates = [
            parent / "Resources" / "fontconfig" / "fonts.conf",
            parent / "native" / "libreoffice-headless" / "libreoffice" / "LibreOfficeDev.app" / "Contents" / "Resources" / "fontconfig" / "fonts.conf",
        ]
        for candidate in candidates:
            if candidate.is_file():
                return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert an Office document to PDF with LibreOffice.")
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()

    src = Path(args.input).expanduser().resolve()
    dst = Path(args.output).expanduser().resolve()
    if not src.is_file():
        raise SystemExit(f"Input file not found: {src}")
    libreoffice = shutil.which("libreoffice") or shutil.which("soffice")
    if not libreoffice:
        raise SystemExit("LibreOffice/soffice not found on PATH")

    dst.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="doc-studio-lo-") as tmp:
        tmp_path = Path(tmp)
        env = os.environ.copy()
        env["HOME"] = str(tmp_path / "home")
        Path(env["HOME"]).mkdir(parents=True, exist_ok=True)
        fontconfig = bundled_fontconfig(libreoffice)
        if fontconfig and "FONTCONFIG_FILE" not in env:
            env["FONTCONFIG_FILE"] = str(fontconfig)
        profile = tmp_path / "profile"
        cmd = [
            libreoffice,
            "--headless",
            f"-env:UserInstallation={profile.as_uri()}",
            "--convert-to",
            "pdf",
            "--outdir",
            str(tmp_path),
            str(src),
        ]
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(f"LibreOffice conversion failed:\n{result.stdout}\n{result.stderr}")
        generated = tmp_path / f"{src.stem}.pdf"
        if not generated.is_file():
            raise SystemExit(f"LibreOffice did not create the expected PDF: {generated}")
        shutil.copy2(generated, dst)
    print(dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
