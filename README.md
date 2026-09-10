# grok-bot-desks

Agent Plugin (skills) for three [Grok Bot](https://x.ai/bot/marketplace) templates. Author: [globulus](https://github.com/globulus). Live clone: [gordan-glavas-codecons/grok-bot-desks](https://github.com/gordan-glavas-codecons/grok-bot-desks) until the globulus transfer is accepted ([OWNERSHIP.md](OWNERSHIP.md)).

| Bot | Category | Listing |
|-----|----------|---------|
| [Flutter Mobile Engineer](bots/flutter-mobile-engineer.md) | Engineering | Reviews Flutter PRs, writes an `fvm`-first test plan, and flags iOS/Android release hygiene. Works from a repo or a pasted diff, and never opens a PR without you. |
| [Bug Repro Desk](bots/bug-repro-desk.md) | Engineering | Turns a ticket or screenshot into a repro pack: exact steps, expected vs actual, env, and screenshots. Uses staging and a fresh test account. Never production customer data. |
| [Job Application Desk](bots/job-application-desk.md) | Personal | Turns a pasted job description into a match score with evidence, a tailored resume, and a first-message draft. Works from a paste or a public posting link, and never applies or emails without you. |

Share links (filled after you publish templates in the Grok Bot app): [dist/SHARE_LINKS.md](dist/SHARE_LINKS.md).

Wave 2 (App Store Ship + backlog): [wave2/README.md](wave2/README.md).

## Install the plugin

**Cursor:** clone this repo, then symlink or copy it to `~/.cursor/plugins/local/grok-bot-desks` and reload. Or submit via [cursor.directory](https://cursor.directory/) / [marketplace publish](https://cursor.com/marketplace/publish) once listed.

**Grok Build:** clone, then add the folder as a plugin directory, or install from a marketplace entry when the [xai-org/plugin-marketplace](https://github.com/xai-org/plugin-marketplace) PR lands.

**Grok Bot:** create a Bot, paste the standing rules from `bots/<desk>.md`, clone this repo onto the Bot computer (or install the plugin), enable the listed skills, send the "First message" from that file.

```text
plugin.json
skills/…/SKILL.md
bots/          # Grok Bot profiles and first messages
fixtures/      # fake ticket, resume, JD — no PII
dist/          # Grokyard, X, marketplace submission text
```

## Create the three Bots (Grok Bot app)

Requires the [Grok Bot](https://docs.x.ai/grok-bot/bots) app.

1. New → Create new agent.
2. Bot actions → Edit Profile: name, title, description from `bots/*.md`.
3. Paste the **First message** from that file (it clones https://github.com/gordan-glavas-codecons/grok-bot-desks).
4. Iterate until the dry run matches [fixtures/expected-dry-run.md](fixtures/expected-dry-run.md).
5. Share as template → strip secrets (checklists in each bot file) → copy the public x.ai link into `dist/SHARE_LINKS.md`.
6. Add the template on a fresh Bot copy and confirm first-run still works.

Do not enable routines in wave 1.

## Approval bar (all desks)

Never send, spend, merge, submit to stores, or invent employment facts without an explicit yes. Job Application resume/tracker files stay on the installer's computer and must not copy with the template.

## License

MIT
