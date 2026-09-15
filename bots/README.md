# Creating a Grok Bot from this repo

The Grok Bot desktop/mobile app cannot be driven from GitHub. Do this once per desk.

1. Open Grok Bot → New → Create new agent.
2. Edit Profile using the matching file in `bots/`.
3. On the Bot computer, clone `https://github.com/globulus/grok-bot-desks` (or install the plugin).
4. Install the testkit once: `python3 -m pip install -e ./testkit`.
5. Send the First message from that bot file (or paste `testpacks/<bot-id>/scenario.md`).
6. Compare structure to `testpacks/<bot-id>/fixtures/dry-run-example.md` and `testpacks/expected-dry-run.md`.
7. Optionally score an exported evidence pack: `python3 -m grok_bot_testkit score --pack <bot-id> path/to/run`.
8. Share as template, strip secrets, paste URLs into `dist/SHARE_LINKS.md`.
9. Duplicate the Bot (or a second account) and add the template to confirm first-run.

Wave 1: no routines. See [testkit/README.md](../testkit/README.md) for the generic harness.
