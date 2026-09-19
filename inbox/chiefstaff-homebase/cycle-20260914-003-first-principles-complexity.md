---
id: homebase-first-principles-complexity-cycle-003
title: "Cycle 003 verification: scoreboard-independence claim rejected"
type: inbox
status: rejected
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [computer-science, simulation]
confidence: high
tags: [homebase, architecture, complexity, verification, rejected-research]
---

# Disposition

The scheduler completed, but the delivered research conclusion is **not accepted**. The original note's claimed schema validation failed on readback, and its scoreboard-independence conclusion is not supported by the cited test setup. This is a verification correction, not a new executed research cycle, a performance result or permission to change production.

Exact original note bytes and the original decision ledger are preserved under `evidence/cycle-003-verification/`, with SHA-256 identities in `originals.json`. The original cron response is `/workspace/hermes-home/profiles/chiefstaff/cron/output/2ac5f8f5e041/2026-09-14_03-12-17.md:547-552`.

## What failed verification

1. The delivered note contained 113 literal backslash-n sequences instead of proper Markdown/frontmatter line breaks. The repository validator reported all six required keys missing: created, id, status, title, type and updated. Its claim that schema validation passed was false for the actual saved file.
2. It conflated disabling draw sinks with removing the entire scoreboard updater. `updateScoreboards` still owns game-over cooldown, result consumption, serve synchronization and new-rally/reset transitions. Omitting that function is not equivalent to keeping its lifecycle calls while suppressing drawing.
3. `rallyTransaction.test.ts:14-22` supplies an inert canvas and jumbotron sink but executes the real `updateScoreboards` function. It does not mock out `renderScoreAtlas` as the original note claimed. Passing such tests does not prove that removing the updater preserves future domain state.
4. It promoted proposed names, `updateScoreboardState` and `drawScoreboards`, into an inventory of existing implementation and a benchmark target. A source search during verification found neither symbol in the product `src/` tree. They may be proposal labels only.
5. It supplied no preserved command/output for an on/off observational comparison, no retrieved external primary-source passages, and no measurement supporting better responsiveness or input latency. The original comparative experiment is therefore **not evidenced as executed**. Do not reuse its claimed human-benefit or causal-equivalence assertions as facts.
6. The existence of independent failing counterexamples does not prove general test-oracle correctness or implementation correctness. Those tests remain separate evidence with explicit scope.

## Grounded observations retained

- `/workspace/wt/homebase-engine-2026/src/animation/updateScoreboards.js:13-36` advances game-over cooldown and can reset the game.
- The same file's lines 40-63 consume results, synchronize display/serve data, record game wins and start the next rally. Lines 83-91 draw after a change. There are also direct legacy-ball/cooldown mutations; not every state write is hidden behind the adapter.
- `/workspace/wt/homebase-engine-2026/tests/engine/rallyTransaction.test.ts:8-34` is an actual physics/rules/scoreboard fixture with inert rendering sinks. That is useful evidence for separating drawing concerns, not proof of lifecycle independence from the updater.
- The preserved independent R2/R3 counterexamples concern provisional identity and historical projection affecting newer domain state. See `docs/engine-audit/step3-independent-review.md` in the product worktree.
- Since this research job ran, the parent produced a separately tested R1 net-bridge candidate. Its provenance is `docs/engine-audit/review-r1-net-bridge.md`; do not credit that production change or its measurements to this research cycle. Its acceptance status belongs to that report.

## Proposal only

Compare the cheapest local repair with a thin game-owned lifecycle boundary before inventing a new kernel. Drawing should consume a projection, but extracting drawing alone does not establish replay ownership, safe stale-event delivery or session isolation. Current score and an old displayed score can legitimately differ; they are not automatically redundant state to delete.

Strongest counterargument: moving functions into new modules may merely rename the same authority coupling, add synchronization machinery, and cost more than repairing the existing explicit calls. A larger abstraction earns its cost only if executable behavior and change-propagation evidence improve while fidelity is fixed.

## Next falsifiable question — unexecuted

On the pinned production baseline, compare the same physical-contact/lifecycle scenario with (A) normal updater calls, (B) the updater retained with inert draw sinks, and (C) updater calls withheld. Record domain events, immutable results, score, game/rally state and ability to accept the next serve. Distinguish delayed legal adjudication from missing lifecycle advancement. Reuse existing counterexamples rather than inventing a replacement sport engine or weakening them.

Only after establishing the coupling baseline should a separately authorized minimal lifecycle extraction be compared. Preserve the command tape, source hashes and actual output. Correctness is the first discriminator; timing hypothetical APIs or mock rendering cannot establish packaged performance or human responsiveness. No new comparison was executed in this verification follow-up.

## Validation and publication boundary

The replacement note uses real frontmatter newlines. Repository schema results and exact preservation checks are recorded in `evidence/cycle-003-verification/verification.json`. This follow-up changes only the cycle note and its ledger row, preserving rejected source artifacts; it does not ingest into the operational database, modify production, commit, push, change the cron schedule or accept G1/M1.
