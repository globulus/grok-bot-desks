# Plugin marketplace submissions

## Cursor

1. Repo must be public: https://github.com/globulus/grok-bot-desks (move to globulus when that account can own it; see OWNERSHIP.md)
2. Submit at https://cursor.directory/ and/or https://cursor.com/marketplace/publish
3. Open source, MIT, skills only (no MCP secrets)

## Grok Build (xai-org/plugin-marketplace)

After this repo is public, open a PR that appends one entry to `.grok-plugin/marketplace.json`:

```json
{
  "name": "grok-bot-desks",
  "description": "Flutter Mobile Engineer, Bug Repro Desk, and Job Application Desk skills. Never send, merge, submit, or invent facts without an explicit yes.",
  "category": "development",
  "source": {
    "source": "url",
    "url": "https://github.com/globulus/grok-bot-desks.git",
    "sha": "PIN_FULL_40_CHAR_SHA_AFTER_PUSH"
  },
  "homepage": "https://github.com/globulus/grok-bot-desks",
  "keywords": ["grok-bot-desks", "flutter", "bug-repro", "job-application"],
  "domains": ["github.com"]
}
```

Then:

```bash
python3 scripts/generate-plugin-index.py
python3 scripts/validate-catalog.py
python3 scripts/generate-plugin-index.py --check
```

Pin `sha` to `06494f201bb2263c1a958d78c152394c819fde96` (current `main` as of 2026-09-15).

Grok Build PR: https://github.com/xai-org/plugin-marketplace/pull/728 (replaces closed [#660](https://github.com/xai-org/plugin-marketplace/pull/660)).
