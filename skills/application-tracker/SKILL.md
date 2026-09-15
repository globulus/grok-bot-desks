---
name: application-tracker
description: Maintains a private job-application tracker file on the installer's Grok Bot computer (role, date, status, next action). Use when logging a role or asking what is in flight. This file must never be copied into a public Bot template.
---

# Application tracker

## When to use

Log a role, list open applications, or mark a status change. Data is local to the installer.

## Approval bar

- Default path: `/workspace/job-desk/tracker.md` (create the folder if needed).
- **Never** add tracker contents to a shareable template, skill, git commit of this plugin, or marketplace listing.
- Do not email reminders to anyone. Chat-only for status. The weekday `job-inbox-cycle` routine may add `drafted` rows; it must not mark `sent`.
- Mark `sent` only when `execute-approved-applications` succeeded for a named queue ID (`q-NNN`).
- Do not scrape their Gmail for applications unless they explicitly ask and approve each send/read.

## File format

```markdown
# Applications

| Company | Role | Source | Date | Status | Next action | Notes |
|---------|------|--------|------|--------|-------------|-------|
```

Status values: researching | drafted | sent | interview | offer | rejected | withdrawn

Notes may include a queue ID (`q-NNN`) once `job-inbox-cycle` has drafted the role.

## Sequence

1. Read the file if it exists; do not invent past rows.
2. Apply the requested add/update.
3. Show the updated table.
4. If they ask to export, write a copy under `/workspace/job-desk/` and remind them it is private.

## Failure

If they have not run first-run, create the folder and empty table after stating you are doing so on their computer only.
