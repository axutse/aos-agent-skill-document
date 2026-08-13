# Security policy

## Supported version

Security fixes are applied to the latest published release.

## Report a problem

Do not open a public issue containing credentials, private documents, personal information, or an unredacted exploit sample. Use GitHub's [private vulnerability reporting form](https://github.com/axutse/aos-agent-skill-document/security/advisories/new) to contact the repository owner without exposing the report publicly.

## Repository guarantees

This plugin does not require an API key, network service, or authentication provider. Document processing runs through local Python libraries, LibreOffice, and Poppler.

Before each release, run:

```bash
python scripts/check_public_release.py --root .
```

Treat any credential pasted into chat, terminal output, issue text, or commit history as compromised and rotate it at the provider.
