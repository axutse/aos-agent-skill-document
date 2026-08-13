# Release assets

`TAIZHOU品牌企业白皮书_完整案例版.pdf` is prepared locally in this directory as the 149-page full case.

The PDF is intentionally ignored by Git so normal clones remain lightweight. Before attaching it to a GitHub Release:

1. Run `python scripts/check_public_release.py --root . --include-release-assets`.
2. Render all 149 pages and inspect them.
3. Confirm the TAIZHOU publication scope and trademark notice.
4. Publish its SHA-256 checksum in the release notes.

Prepared checksum: `afa118f68075fb59cb62f6fe0291f2ae9c1e57761f6439360c540f2e2562423c`. The same value is stored in `SHA256SUMS.txt`.
