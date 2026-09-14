---
id: hermes-landing-evidence-waves
title: "Landing-evidence waves: the verifier, the wave format, and the #111084 case study"
type: permanent
status: draft
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [ai-ml, engineering-process]
confidence: high
tags: [hermes, maintenance, waves, verification, landing-evidence]
---

# Landing-evidence waves: the verifier, the wave format, and the #111084 case study

Concrete Hermes instantiation of [[permanent/perm-20260914-landing-evidence-over-state-labels]]: how a wave issue proves its claims before a maintainer has to, and the tooling that makes it cheap. Read the permanent note first for the generalized principle; this note is the Hermes-specific build.

## Case study: wave 1 (#111084), executed by teknium1 2026-09-14

- **Inventory**: 18 open issues labeled `duplicate` whose canonicals were `state_reason: completed`, plus exclusions verified honest (#13924 open/duplicate; #10251 closed `not_planned`).
- **Execution**: teknium1 re-verified each pair against actual landing evidence (merge commit on main), caught 3 where "completed" lied, kept them open with the evidence written out.
- **Result**: 15 issues closed with landed SHA + PR cited each; 3 PRs (#28837, #31038, #36877) closed as superseded; 3 issues kept open as live reports (#91203, #42199, #72485).
- **Community pattern**: independent verification comments arrived before execution (KeyArgo, harshmoney123) and caught real gaps — the #44562→#45403 open-canonical case and the superseded-PR batching. A verifier that reproduces those checks pre-publication is the durable asset.

## The verifier: `landing_evidence.py`

Lives at `~/workspace/goals/hermes-agent-maintenance-shift/consolidation/landing_evidence.py` (also documented in that goal's `AGENTS.md` lessons). Usage:

```bash
landing_evidence.py --pairs 43437:9816 91203:67358 44562:45403 \
  --wrong-face "72485=PR fixed terminal-pane font picker, dupe asks for chat/UI OpenDyslexic" \
  --out le_wave2.json
```

Pipeline per (dupe, canonical) pair:

1. **Canonical state**: `state` + `state_reason` + `closed_by` via the issues API. Open → `OPEN-ANCHOR` immediately (the #45403 lesson: never close a dupe past an open canonical).
2. **Reporter-closed detect**: `closed_by == issue author` → `REPORTER-CLOSED`. Covers retractions and unilateral reporter closures.
3. **Landing PR discovery**: merged PRs (base=main) referencing the canonical, from **two sources** — issue-timeline `cross-referenced` events AND repo-wide search `type:pr "#N"` (title/body). The AGENTS.md lesson: timelines miss PRs that reference the issue only in prose.
4. **Content spot-check**: take the landing PR's first changed file, check its added lines against `origin/main:<path>` in the local clone. Proves the fix is *on main*, not just merged somewhere.
5. **Wrong-face override**: caller-supplied `--wrong-face` notes downgrade `LANDED` to `WRONG-FACE` with the mismatch recorded. This step is semantic (compare the PR's component against the dupe's report); the script surfaces the PR title so a human or a dedicated component-match pass can judge.

Verdict table and the six verdicts are defined in the permanent note.

### Caveat: the shallow clone

`~/workspace/hermes/hermes-agent` is a shallow clone, so `git merge-base --is-ancestor` is unreliable — that is why the verifier uses merged-to-main PRs + content-on-main checks instead of ancestry. Any future full-clone setup could re-add the ancestry rung; it is strictly stronger when history is complete.

## The wave format (for maintainers' one-click review)

Proven by waves #111084 / #111126 / #111128 / #111133 / #111153 (2026-09-14):

1. **One core claim, stated up front** — collapses N issues into one maintainer decision.
2. **Verification table** — every inventory entry carries its verifier verdict + landing SHA/PR or the reason it is excluded. No "trust me" entries.
3. **Close candidates grouped** with exact suggested close-comment text per group (`Duplicate of #N, which landed in <sha> (#PR). Reopen if still seeing this on current main.`).
4. **Keep-open anchors named explicitly** — open canonicals are preserved as anchors, with their dupes referencing them.
5. **Contention section, honest** — open PRs touching any entry, framed as conformance cases or superseded carriers, never hidden.
6. **What this is not** — boundary crispness against sibling waves (prevents god-issue merge).

## Standing posture

- Kevin's standing rule: **no public issue/comment/reply without his explicit approval of the exact draft**. Verifier output and wave drafts are handed to the parent agent; posting is a separate approval step.
- Verifier runs are read-only: GitHub API reads + local clone reads only.
- Wave 2 sweep (stale duplicates beyond wave 1's inventory, every pair through the verifier) is in flight; its inventory lands as `wave2_verified.json` and draft as `wave_stale2_draft.md` in the goal's `consolidation/`.

## Related

- [[permanent/perm-20260914-landing-evidence-over-state-labels]] — the generalized principle: name the artifact or it didn't happen
- [[permanent/perm-20260914-harness-evolver]] — credit gates: the same stance at the Evolver scale
