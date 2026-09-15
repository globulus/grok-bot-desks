---
name: job-sources
description: Maintains a private list of public job-board URLs and RSS feeds on the installer's Grok Bot computer. Use when adding, listing, or editing sources for job-inbox-cycle. Never copies this file into a public Bot template. Never logs into LinkedIn, Greenhouse, or Lever to discover postings.
---

# Job sources

## When to use

Add or edit where `job-inbox-cycle` should look for public postings. Data is local to the installer.

## Approval bar

- Default path: `/workspace/job-desk/sources.md` (create the folder if needed).
- **Never** add source contents, saved-search cookies, or login URLs with credentials to a shareable template, skill, git commit of this plugin, or marketplace listing.
- Types: `public` (HTML listing or posting), `rss` (feed), `login` (always skip — paste required).
- Do not scrape LinkedIn, Greenhouse, Lever, or any login wall. Mark those rows `login`.
- Cap **5 new preps per `job-inbox-cycle` run** (enforced by that skill, recorded here as a reminder).

## File format

```markdown
# Job sources

| Name | URL | Type | Notes |
|------|-----|------|-------|
```

Type values: public | rss | login

## Sequence

1. Read the file if it exists; do not invent past rows.
2. Apply the requested add/update. If they paste a LinkedIn or ATS login URL, set Type to `login` and say it will be skipped until they paste the JD.
3. Show the updated table.
4. Remind them `job-inbox-cycle` will not run as a routine until at least one `public` or `rss` row exists.

## Failure

If they have not run first-run, create the folder and empty table after stating you are doing so on their computer only.
