# Creating a Grok Bot from this repo

The Grok Bot desktop/mobile app cannot be driven from GitHub. Do this once per desk. Root overview: [../README.md](../README.md).

## Open or create the Bot

1. Install and sign in to the [Grok Bot app](https://docs.x.ai/grok-bot/get-started).
2. **New** → **Create new agent** (or select an existing Bot in the sidebar).
3. **Bot actions → Edit Profile** using the matching file in this folder.
4. Enable the skills listed in that profile.

## Open Agent Computer

1. With the Bot conversation open, choose **Agent Computer**.
2. That is the shared cloud desktop (browser / files / terminal)—not your laptop.
3. Use **takeover** for passwords, 2FA, or CAPTCHAs, then return control.

Docs: [Use the computer and apps](https://docs.x.ai/grok-bot/computer-and-apps).

## Install this plugin on the Bot computer

In Agent Computer (or by asking the Bot):

```bash
cd /workspace   # or another durable folder
git clone https://github.com/globulus/grok-bot-desks
cd grok-bot-desks
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -e ./testkit
```

## Run a harness e2e

1. Start mocks on the **Bot computer**: `python3 -m grok_bot_testkit serve --pack <bot-id>`
2. Paste `testpacks/<bot-id>/scenario.md` (or the First message from the bot file) into chat.
3. Copy the evidence pack from `{evidence_root}/<run-id>/` off the computer.
4. Score: `python3 -m grok_bot_testkit score --pack <bot-id> path/to/run`
5. Compare structure to `testpacks/<bot-id>/fixtures/dry-run-example.md` and `testpacks/expected-dry-run.md`.

| Bot id | Profile | Port |
|--------|---------|------|
| `job-application-desk` | [job-application-desk.md](job-application-desk.md) | 8765 |
| `flutter-mobile-engineer` | [flutter-mobile-engineer.md](flutter-mobile-engineer.md) | 8766 |
| `bug-repro-desk` | [bug-repro-desk.md](bug-repro-desk.md) | 8767 |

## Publish

Share as template → strip secrets → paste URLs into [`dist/SHARE_LINKS.md`](../dist/SHARE_LINKS.md) → duplicate the Bot (or a second account) and add the template to confirm first-run.

Wave 1: no routines. Harness details: [../testkit/README.md](../testkit/README.md).
