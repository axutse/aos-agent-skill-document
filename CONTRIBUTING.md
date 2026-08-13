# Contributing

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Install LibreOffice and Poppler when testing DOCX/PDF rendering.

## Change requirements

1. Keep each `SKILL.md` concise and move detailed procedures into `references/`.
2. Add deterministic scripts only when they eliminate repeated or fragile work.
3. Do not add credentials, private documents, font files, or unlicensed assets.
4. Keep TAIZHOU example data explicitly marked as planning assumptions.
5. Render and inspect every page of changed DOCX/PDF examples.
6. Run the release scanner and test suite before opening a pull request.

```bash
python scripts/check_public_release.py --root .
pytest
```

For changes that affect Word rendering, rebuild the case and inspect all generated pages at 100% zoom.
