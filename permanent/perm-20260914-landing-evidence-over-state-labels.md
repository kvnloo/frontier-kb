---
id: perm-20260914-landing-evidence-over-state-labels
title: "Landing evidence over state labels: verify claims against the world, not the flag"
type: permanent
status: draft
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [ai-ml, engineering-process, evals]
confidence: high
tags: [permanent, verification, credit-gates, evidence, maintenance]
---

# Landing evidence over state labels: verify claims against the world, not the flag

## Idea (atomic)

Any claim of the form "X is done / dead / fixed / superseded" must name a **landed artifact** — a merge commit on the default branch whose content is provably present on main — never just a state flag. State labels (`state_reason: completed`, task status "done", eval "passed") record *how someone clicked*, not what shipped. Three out of eighteen in the first real-world trial were wrong.

## The trial: hermes-agent #111084 (2026-09-14)

The stale-duplicate wave inventoried 18 open issues labeled `duplicate` whose canonicals were all `state_reason: completed`. teknium1 executed the close pass but first re-verified every pair against actual landing evidence. Three stayed open:

1. **#91203** — canonical #67358 was `completed` because the **reporter retracted** the crash claim (exit 75 = planned restart). Nothing landed for the crash path. The "completed" flag measured the reporter's change of mind, not a fix.
2. **#42199** — canonical #37505 was `completed` because the **reporter closed it**. Releases are still arm64-only DMGs; the Intel build request is unresolved. The flag measured thread closure, not a fix.
3. **#72485** — canonical #37566 really did land something: PR #44642 "bundle JetBrains Mono for the **terminal pane**". But the dupe asks for OpenDyslexic in the **chat/UI** face. A landed fix for the wrong component. The flag measured *a* fix, not *the* fix.

Final tally: 15 issues + 3 PRs closed, 3 kept open as live reports. Without the landing-evidence check, all 18 would have closed and three live bug classes would have read as untracked.

## The verdict taxonomy

The verifier (`landing_evidence.py`, in the maintenance-shift goal's `consolidation/`) classifies each (dupe, canonical) pair:

| Verdict | Meaning | Action |
|---|---|---|
| `LANDED` | Merged PR to main found; spot-checked content present on `origin/main` | Close dupe, cite SHA + PR |
| `COMPLETED-NOT-LANDED` | `completed` but no merged PR references the canonical | Investigate; usually reporter/maintainer closed without a fix |
| `REPORTER-CLOSED` | `closed_by == issue author` | Do not close the dupe — the class may still be live |
| `OPEN-ANCHOR` | Canonical still open | Keep as anchor; close dupes naming it, never past it |
| `WRONG-FACE` | Manual: landing PR fixed a different component than the dupe reports | Keep open; record the mismatch |
| `NEEDS-REVIEW` | No evidence either way | Human call |

Two implementation notes that generalize: (a) finding the landing PR needs **timeline cross-references AND repo-wide title/body search** — timelines miss PRs that reference the issue only in prose; (b) the wrong-face check is inherently a **component-match judgment** — an agent can extract the PR's component from title/body, but comparing it against the dupe's report is semantic work the loop should flag explicitly rather than bury.

## Why this belongs next to the credit gates

[[permanent/perm-20260914-harness-evolver]] says credit is measured on the sealed battery, never on the evolver's self-report: the same epistemic stance. A patch that "passes the open battery" is a state flag; a patch that transfers on held-out task families is landing evidence. The maintenance-shift version is the same idea at smaller scope:

- **State flag**: `state_reason: completed` / "agent says task done" / "eval passed on the training split".
- **Landing evidence**: merge commit on main + content present / human-verified diff + tests green on a clean tree / transfer on the sealed battery.

Any future "X is done" claim in any harness gets this treatment: name the artifact or it didn't happen.

## Kill criteria / non-goals

- Not a call to distrust maintainers — teknium1's judgment is the ground truth the taxonomy was extracted *from*. The taxonomy operationalizes his check so bots can run it before he has to.
- Not proof of correctness — landing evidence proves the fix *shipped*, not that it *worked*. That is the next rung (behavioral verification), not this one.

## Related

- [[permanent/perm-20260914-harness-evolver]] — the generalized loop; credit gates are the same "measure the world, not the label" stance
- [[notes/hermes-landing-evidence-waves]] — the Hermes-specific instantiation: verifier design, wave format, case study
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]] — credit gates in the Evolver context
