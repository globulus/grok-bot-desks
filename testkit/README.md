# grok-bot-testkit

Generic harness for [Grok Bot](https://docs.x.ai/grok-bot/bots) dry-runs: mock HTTP sites, evidence packs, and rubric scoring.

CI cannot drive the Grok Bot app. This kit supports:

1. **`validate`** — structural checks on `skills/` and `testpacks/` (fully automated)
2. **`serve`** — mock sites on the **Bot computer** (semi-automated e2e)
3. **`score`** — deterministic assertions on an exported evidence pack

## Install

From the plugin repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ./testkit
```

Or run without installing (after `pip install PyYAML` in a venv):

```bash
PYTHONPATH=testkit/src python3 -m grok_bot_testkit validate
```

## CLI

```bash
python3 -m grok_bot_testkit validate
python3 -m grok_bot_testkit list-packs
python3 -m grok_bot_testkit serve --pack job-application-desk
python3 -m grok_bot_testkit score --pack job-application-desk path/to/run
python3 -m grok_bot_testkit score --pack job-application-desk --rubric rubric-inbox.yaml path/to/inbox-run
```

## Testpack layout

Each bot gets `testpacks/<bot-id>/`:

```text
bot.yaml       # id, skills, port, evidence_root, artifacts, routes
scenario.md    # paste into the Bot for e2e
scenario-inbox.md  # optional second paste (job desk named-ID submit)
rubric.yaml    # score rules
rubric-inbox.yaml  # optional extra rubric; pass with score --rubric
fixtures/      # safe fake inputs (no real PII)
sites/         # mock HTML served by `serve`
golden/        # optional committed evidence packs for CI score
```

### `bot.yaml`

| Field | Meaning |
|-------|---------|
| `id` | Must match directory name |
| `skills` | Skill folder names under `skills/` |
| `port` | Unique localhost port for `serve` |
| `evidence_root` | Where the Bot should write runs on its computer |
| `artifacts` | Logical name → path under the run dir |
| `routes` | Mock HTTP routes (`static`, `login_wall`, `log_post`) |

Built-in harness routes (always on): `/_harness/health`, `/_harness/evidence`, `/_harness/reset`.

### Evidence pack

Under `{evidence_root}/<run-id>/`:

```text
manifest.json
artifacts/…
logs/…          # copy harness *.log files here before scoring
notes.md        # optional
```

`manifest.json` fields: `bot_id`, `skills_run`, `urls_hit`, `started_at`, `finished_at`, `pack_version`.

### Rubric rule types

`file_exists`, `heading_present`, `regex_present`, `regex_absent`, `json_equals`, `json_path`, `log_count`, `status_in`, `strings_subset_of_fixture`, `manifest_skills_include`, `no_phone_like`.

Set `severity: soft` for warnings; default is `hard` (fails the score).

## Operator e2e loop

CI cannot open the Grok Bot app. You run mocks on the Bot’s **cloud** computer, paste a scenario in chat, then score the evidence pack locally.

### 1. Open the Bot and Agent Computer

1. In the [Grok Bot app](https://docs.x.ai/grok-bot/get-started), open or create the Bot ([create/manage Bots](https://docs.x.ai/grok-bot/bots)).
2. From the conversation, open **Agent Computer** ([computer and apps](https://docs.x.ai/grok-bot/computer-and-apps)).
3. That desktop is shared across your Bots. `127.0.0.1` in scenarios is localhost **there**, not on your laptop.

### 2. Install and serve on the Bot computer

Clone this plugin onto the cloud computer (e.g. under `/workspace`), then:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ./testkit
python3 -m grok_bot_testkit serve --pack job-application-desk
```

Leave the server running. Ports: job-application-desk `8765`, flutter-mobile-engineer `8766`, bug-repro-desk `8767`.

### 3. Paste the scenario

Paste `testpacks/<bot-id>/scenario.md` into the Bot chat (or the First message from `bots/<desk>.md`, which points at harness mode). Job Application Desk also has `scenario-inbox.md` for the weekday-inbox + named-ID submit path.

The Bot should hit the mock sites, refuse unsafe actions (unless the inbox scenario names a queue ID), and write an evidence pack under that pack’s `evidence_root`.

### 4. Score the evidence pack

Copy `{evidence_root}/<run-id>/` off Agent Computer, then on your machine:

```bash
python3 -m grok_bot_testkit score --pack <bot-id> path/to/run
python3 -m grok_bot_testkit score --pack job-application-desk --rubric rubric-inbox.yaml path/to/inbox-1
```

Exit 0 = pass. Soft rules print as warnings; hard rules fail the score.

Also in the root [README](../README.md): create Bot, Agent Computer, and e2e overview.

## Adding a fourth bot

Add `testpacks/<new-id>/` with `bot.yaml`, `scenario.md`, `rubric.yaml`, fixtures, and optional sites. No testkit core changes required if you only need existing rule types and handlers.

## Schemas

JSON Schema documents live in `src/grok_bot_testkit/schema/` for documentation and future strict validation.
