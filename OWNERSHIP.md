# Ownership

Intended GitHub owner: [globulus](https://github.com/globulus).

This clone is public at [gordan-glavas-codecons/grok-bot-desks](https://github.com/gordan-glavas-codecons/grok-bot-desks) because the CLI session was authenticated as that account. `globulus` could not be used as `--owner` from that token.

To finish the move:

1. Sign in to GitHub as **globulus**.
2. Accept the repository transfer if GitHub emailed one, **or** create `globulus/grok-bot-desks` and push:

```bash
cd /Users/gordan/Documents/GitHub/grok-bot-desks
git remote set-url origin https://github.com/globulus/grok-bot-desks.git
git push -u origin main
```

3. Update `plugin.json` `homepage` / `repository` to `https://github.com/globulus/grok-bot-desks` and retarget the plugin-marketplace PR SHA.
