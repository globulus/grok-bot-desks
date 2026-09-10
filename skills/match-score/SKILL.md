---
name: match-score
description: Scores a master resume against a parsed job description with evidence for and against each must-have. Use after parse-jd. Never inflates experience or invents employers, dates, titles, or metrics.
---

# Match score

## When to use

A parsed JD plus the installer's master resume (file on their computer or paste). Output is a decision aid, not an application.

## Approval bar

- Every "for" claim must point at a resume line.
- Never upgrade "familiar with" to "expert".
- Never infer employment that is not on the resume.
- Gaps are first-class output, not something to hide.

## Sequence

1. Require `parse-jd` output or parse first.
2. For each must-have: FOR (resume evidence) / AGAINST (missing or weak) / UNKNOWN.
3. Overall: strong / mixed / weak, with the single assumption most likely to fail a screen.
4. Questions the candidate should ask (from posting holes).
5. Do not recommend applying if must-haves are mostly AGAINST; still produce the table.

## Output format

```markdown
# Match score

Role:
Resume source: [path or "paste"]

## Must-haves
| Requirement | Verdict | Evidence |
| | FOR/AGAINST/UNKNOWN | |

## Overall
strong | mixed | weak
Screen-fail risk: [one sentence]

## Gaps to be honest about
-

## Questions to ask them
-

## What I did not do
Invent experience, submit, email
```
