# grok-bot-desks

Agent Plugin (skills) for three [Grok Bot](https://x.ai/bot/marketplace) templates. Author: [globulus](https://github.com/globulus). Live clone: [globulus/grok-bot-desks](https://github.com/globulus/grok-bot-desks) until the globulus transfer is accepted ([OWNERSHIP.md](OWNERSHIP.md)).

| Bot                                                        | Category    | Listing                                                                                                                                                                                              |
| ---------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Flutter Mobile Engineer](bots/flutter-mobile-engineer.md) | Engineering | Reviews Flutter PRs, writes an `fvm`-first test plan, and flags iOS/Android release hygiene. Works from a repo or a pasted diff, and never opens a PR without you.                                   |
| [Bug Repro Desk](bots/bug-repro-desk.md)                   | Engineering | Turns a ticket or screenshot into a repro pack: exact steps, expected vs actual, env, and screenshots. Uses staging and a fresh test account. Never production customer data.                        |
| [Job Application Desk](bots/job-application-desk.md)       | Personal    | Turns a job description into a match score with evidence, a tailored resume, and a first-message draft. Optional weekday inbox from public sources. Sends or submits only named queue IDs. |

Share links (filled after you publish templates in the Grok Bot app): [dist/SHARE_LINKS.md](dist/SHARE_LINKS.md).

Wave 2 (App Store Ship + backlog): [wave2/README.md](wave2/README.md).

## Install the plugin

**Cursor:** clone this repo, then symlink or copy it to `~/.cursor/plugins/local/grok-bot-desks` and reload. Or submit via [cursor.directory](https://cursor.directory/) / [marketplace publish](https://cursor.com/marketplace/publish) once listed.

**Grok Build:** clone, then add the folder as a plugin directory, or install from a marketplace entry when the [xai-org/plugin-marketplace](https://github.com/xai-org/plugin-marketplace) PR lands.

**Grok Bot:** see [Create a Bot](#create-a-bot-in-the-grok-bot-app) below.

```text
plugin.json
skills/…/SKILL.md
bots/          # Grok Bot profiles and first messages
testkit/       # generic validate / serve / score harness
testpacks/     # per-bot fixtures, mock sites, scenarios, rubrics
dist/          # Grokyard, X, marketplace submission text
```

## Create a Bot in the Grok Bot app

Requires the [Grok Bot](https://docs.x.ai/grok-bot/get-started) desktop or mobile app (not grok.com chat alone). Docs: [Create and manage Bots](https://docs.x.ai/grok-bot/bots).

1. Open **Grok Bot** and sign in with your Cursor account.
2. **New** (or `Cmd/Ctrl+N`) → **Create new agent**.
3. **Bot actions → Edit Profile**: name, title, description, and avatar from the matching file in [`bots/`](bots/) (e.g. [`bots/job-application-desk.md`](bots/job-application-desk.md)).
4. Enable the skills listed in that file (clone this repo onto the Bot computer, or install the plugin).
5. Paste the **First message** from that file into the chat, or the harness block from `testpacks/<bot-id>/scenario.md`.

To reopen an existing Bot: select it in the sidebar (or **Show hidden chats** if you hid it).

After a good dry run: **Share as template** → strip secrets (checklists in each bot file) → paste the public x.ai link into [`dist/SHARE_LINKS.md`](dist/SHARE_LINKS.md) → add the template on a fresh Bot copy and confirm first-run still works.

Flutter and Bug Repro desks: do not enable routines. Job Application Desk may add a weekday `job-inbox-cycle` routine after `sources.md` has a public/rss row; send/submit still needs named queue IDs. More detail: [`bots/README.md`](bots/README.md).

## Access the Bot computer (Agent Computer)

Bots run on a **shared cloud computer** (browser, filesystem, terminal)—not your laptop by default. All Bots on your account share that computer (`/workspace`, browser sessions, logins). Docs: [Use the computer and apps](https://docs.x.ai/grok-bot/computer-and-apps).

1. Open the Bot conversation in the Grok Bot app.
2. Open **Agent Computer** from that conversation to view the cloud desktop.
3. Ask the Bot to run terminal commands there, or use **takeover** when you need to type a password, passkey, 2FA, or CAPTCHA yourself, then return control.

Local Mac/Windows execution is separate (**Settings → General → Agent → Execution on Local Computer**) and is not required for the harness. `127.0.0.1` in harness URLs means localhost **on the cloud computer**, not your laptop.

## End-to-end test (harness)

CI cannot drive the Grok Bot app. E2E is: Bot app + mock server on Agent Computer + scenario paste + score the evidence pack. Full kit docs: [testkit/README.md](testkit/README.md).

| Pack | Port | Scenario |
|------|------|----------|
| `job-application-desk` | 8765 | [`scenario.md`](testpacks/job-application-desk/scenario.md) (zero POSTs) · [`scenario-inbox.md`](testpacks/job-application-desk/scenario-inbox.md) (one named-ID POST) |
| `flutter-mobile-engineer` | 8766 | [`testpacks/flutter-mobile-engineer/scenario.md`](testpacks/flutter-mobile-engineer/scenario.md) |
| `bug-repro-desk` | 8767 | [`testpacks/bug-repro-desk/scenario.md`](testpacks/bug-repro-desk/scenario.md) |

**On the Bot computer** (Agent Computer / ask the Bot to run this):

```bash
# clone if needed, then from the plugin root:
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -e ./testkit
python3 -m grok_bot_testkit serve --pack job-application-desk
```

Leave `serve` running. In the Bot chat, paste the matching `testpacks/<bot-id>/scenario.md`. The Bot should write an evidence pack under that pack’s `evidence_root` (e.g. `/workspace/job-desk/runs/harness-1/`).

**On your laptop** (or anywhere you can run Python), after copying the run folder out:

```bash
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -e ./testkit
python3 -m grok_bot_testkit score --pack job-application-desk path/to/harness-1
```

Pass = rubric green (structure + safety). Compare tone to `testpacks/<bot-id>/fixtures/dry-run-example.md` and [testpacks/expected-dry-run.md](testpacks/expected-dry-run.md).

**Structural CI only** (no Bot app):

```bash
python3 -m grok_bot_testkit validate
python3 -m grok_bot_testkit score --pack job-application-desk testpacks/job-application-desk/golden/sample-run
python3 -m grok_bot_testkit score --pack job-application-desk --rubric rubric-inbox.yaml testpacks/job-application-desk/golden/inbox-run
```

## Approval bar (all desks)

Never send, spend, merge, submit to stores, or invent employment facts without an explicit yes. For Job Application Desk, that yes is a named queue ID list (`approve: q-003`), not approve-all. Resume, tracker, sources, and queue stay on the installer's computer and must not copy with the template.

## License

MIT
