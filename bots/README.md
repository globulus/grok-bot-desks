# Creating a Grok Bot from this repo

The Grok Bot desktop/mobile app cannot be driven from GitHub. Do this once per desk.

1. Open Grok Bot → New → Create new agent.
2. Edit Profile using the matching file in `bots/`.
3. On the Bot computer, clone `https://github.com/globulus/grok-bot-desks` (or install the plugin).
4. Send the First message from that bot file.
5. Compare output to `fixtures/dry-runs/` and `fixtures/expected-dry-run.md`.
6. Share as template, strip secrets, paste URLs into `dist/SHARE_LINKS.md`.
7. Duplicate the Bot (or a second account) and add the template to confirm first-run.

Wave 1: no routines.
