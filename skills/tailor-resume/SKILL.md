---
name: tailor-resume
description: Rewrites resume bullets to a job description and shows every change. Use after match-score. Never invents titles, dates, employers, or metrics. Never submits an application.
---

# Tailor resume

## When to use

The user wants a JD-aligned resume draft from their master resume.

## Approval bar

- Reorder, trim, and rephrase only. No new employers, titles, dates, degrees, or numbers.
- If a keyword is not evidenced, omit it or put it under a "not claimed" note — do not insert it.
- Show a change log. If you cannot point at a master-resume source for a bullet, delete it.
- Output is a draft file on **their** computer, not a public template asset.

## Sequence

1. Read master resume from the path set in first-run (default `/workspace/job-desk/master-resume.md`).
2. Use `parse-jd` keywords only where evidence exists.
3. Prefer the posting's nouns in bullets that already describe that work.
4. Keep length honest; do not turn a 1-page resume into 4 pages of fluff.
5. Write tailored copy + change log.

## Output format

```markdown
# Tailored resume (draft)

Target role:
Source: [master path]

## Resume
[full draft]

## Change log
| Original | New | Why (JD line) | Source bullet |
| | | | |

## Refused to add
Keywords with no evidence
```

## Failure

If there is no master resume, run `first-run-job-desk` instead of guessing a career.
