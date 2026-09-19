---
id: homebase-first-principles-complexity-charter
title: "Homebase first-principles loop: less machinery, better human outcomes"
type: inbox
status: active
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [computer-science, mathematics, physics, simulation]
confidence: medium
tags: [homebase, architecture, complexity, causal-models, human-outcomes]
---

# Question

What is the smallest model and ownership structure that preserves the human capabilities, causal correctness and explicit fidelity commitments of Homebase M1?

The user asks for a deliberate first-principles cycle across mathematics, physics, reality, ideas, attention, introspection and human benefit. Translate surprising analogies into falsifiable engineering claims. Do not sell a golden universal engine, a consciousness theory or metaphysics as a measured result. This is a research extension, not authorization to rewrite production or move its acceptance gates.

Related: [[homebase-local-twin-research]], [[homebase-engine-critical-path]]. Existing cycles address multi-rate/FMI and CCD/event ordering. Build on those rather than repeating engine shopping.

## Context and inspected evidence

Research workspace: /workspace/frontier-kb. Product worktree, read-only for this cycle: /workspace/wt/homebase-engine-2026. G1 patch is under independent review; preserve all dirty files. No production changes, database writes, commits, pushes, merges, installs or GPU work in this cycle.

Fresh parent inspection on 2026-09-14 found:

- `src/animation/updateScoreboards.js:13-36` owns and advances game-over cooldown and resets game/serve state.
- `src/animation/updateScoreboards.js:40-63` consumes the result, records game wins and starts the next rally inside scoreboard update. Lines 83-90 draw the projection in the same function.
- `docs/engine-audit/g2-state-ownership.md:9-13` documents absent full production restore and split ownership. This report is read-time inventory, not a live conformance guarantee.
- The inventory's sections 3-5 document multiple representations of serve/bounce/match state, athlete animation scalars that affect physical motion, pending NVZ obligations and provisional ball-dead outcomes. Re-read actual relevant source before attributing current behavior.
- `g0/benchmark-manifest-v1.json` defines proposed acceptance; host inventory is not gameplay profiling. No new speed, capacity, fidelity or maintainability win has been measured here.

QMD lexical searches for `homebase kernel research` and `homebase` returned no results in this session. Direct bounded file discovery located the notes; absence from QMD is not absence from the KB. Do not re-index the live product graph.

## Competing architecture hypotheses

A. Keep the current engine and bridges; repair and document each seam. Lowest immediate migration cost; might retain redundant authority and future restore cost.

B. One game-owned session, one owner per authoritative fact, thin runtime integration. Reuse existing math/rules; lifecycle advances without UI; views are projections. Small direct modules and explicit calls before introducing a general bus or plugin framework. Different sports retain different dynamics and rules. Ownership need not imply one huge object, one thread, a pure whole-world copy or a new engine.

C. Broad generic event-sourced/ECS kernel. Might earn its cost for actual concurrency/reuse, but risks a second engine, schema/identity duplication and event dispatch indirection. Compare against B rather than assuming sophistication means simpler.

D. Runtime-native ownership only, with minimal headless domain seam. Could cost less than a portable language-agnostic kernel; prove whether headless/replay requirements genuinely require broader portability.

Current parent hypothesis is B with a narrow native integration comparison later, not a verified winner. The decisive accounting is total cost of delivering, explaining, testing and maintaining intended behavior, not source lines alone.

## Sequential perspective passes

Use one bounded serial researcher. Each pass produces: insight; implication for the actual source; counterargument; a discriminating observation. These are decision summaries, not purported access to a model's hidden cognition.

1. Mathematics / state sufficiency. A compressed state is useful only if omitted history cannot change relevant future responses to allowed inputs. This is a proposed contract over tested conditions, not proof that a handful of tests establishes universal equivalence. Pending momentum, serve order and RNG cursor are examples of relevant history. Do not derive duplicate state away until dependency and round-trip tests justify it.
2. Physics / hybrid systems. Continuous flight alternates with discrete contact, possession, serve and adjudication transitions. Research whether exact event localization plus explicit phase transitions is simpler than bolting corrections onto a universal tick. Do not infer that all dynamics are analytically solvable or that a discrete-event simulator eliminates active contact integration.
3. Causality / counterfactuals. Delete a renderer, UI consumer or telemetry sink: which domain facts must remain identical? Change a true input: which facts should change? Use this to distinguish projection, control and authority.
4. Information theory / history. Current sufficient state, commands, committed results and occasional checkpoints serve different needs. Logging every simulation detail is not the same as maintaining enough information for reproducible recovery. Quantify bounded retention/backpressure requirements before proposing a message bus.
5. Distributed systems / transactions. Even a local application has delayed observers. Define finality and identity at adjudication boundaries. A physically dead ball is not necessarily a finalized rally if a rule obligation survives. Test whether direct ownership avoids much of the machinery needed to reconcile independent mutable replicas.
6. Programming-language and maintenance perspective. Compare direct functions/modules with actors, ECS, event sourcing and a portable framework using actual change propagation and state ownership. Fewer files is not necessarily fewer concepts; more types are not necessarily more safety. Preserve an executable reference while extracting a seam.
7. Control / perception-action loop. Responsiveness is the full input-to-contact-to-feedback loop, not solver accuracy alone. Evaluate bounded assistance, legibility and tactical consequences without claiming unmeasured human benefit or cheating contact rules.
8. Attention / rendering. Budget visual and audio detail by what helps people perceive and act. Rendering visibility must not decide authoritative outcomes. Reduced visual work is allowed only within approved fidelity/accessibility requirements; exact background matches remain exact. Approximate background activity must be labelled and unable to silently contaminate exact claims.
9. Epistemology / digital twins. Separate measured facility facts, authored assets, inferred parameters and invented scenario data. A prettier model is not more certain. Does provenance plus a calibrated sparse model provide more decision value than a dense uncalibrated world?
10. Product / human benefit. Compare recreational play, practice/learning, accessibility and facility decision support as distinct outcome classes. Do not expand M1 to promise every one. Prefer hypotheses about better agency, understanding, connection and reduced wasted time over engagement/time-in-app as default success.
11. Philosophy / introspection. Treat this conversation as an asynchronous information exchange supporting a shared external record, not evidence of merged minds or subjective AI awareness. Explain transformer context/token processing only at a high level; subjective experience is debated and cannot be settled by an eloquent self-report. Translate the useful analogy: preserving causal evidence beats trying to keep every detail mentally present.
12. Adversarial minimalism. Argue against the current favorite. When would moving ownership cost more than keeping a seam? Which distinctions are irreducible (e.g. current score vs a historical displayed score)? What one result would make us abandon the proposed simplification?

## Bounded executable question

Prefer the smallest observational-dependence probe over a new engine benchmark:

Does disabling scoreboard projection in the real physical-contact/lifecycle scenario change future domain state or ability to start a new rally? Can the present direct API already separate drawing from lifecycle, or would it need an ownership extraction?

Inspect source, existing `tests/engine/rallyTransaction.test.ts`, manifest and test commands before running anything. Use only a new isolated research harness path and inert rendering sinks if a safe probe is possible, never injected end-of-rally events presented as collision evidence. Do not edit existing source or independent review tests. Reuse production physics and rules; report precisely what is bypassed. Current and proposed implementations are different: a baseline coupling probe alone does not prove a candidate fix or speedup.

Resource policy: read lightweight host status first. At most two CPU workers and 120 seconds per experiment; no full suites/builds competing with independent review. Under pressure produce an executable experiment specification instead, explicitly unexecuted. Do not invent outputs or build a toy replacement and call it production evidence.

## Independent review addendum

The independent G1 review returned after this cycle was launched. Parent read the report, the complete independent test source, and raw counterexample output at:

- `/workspace/wt/homebase-engine-2026/docs/engine-audit/step3-independent-review.md`
- `/workspace/wt/homebase-engine-2026/tests/engine/step3IndependentReview.test.ts`
- `/workspace/wt/homebase-engine-2026/docs/engine-audit/evidence/step3-independent-counterexamples.log`

Verdict: candidate not accepted. Four independent counterexamples failed. They are distinct from the implementer's passing focused suite; do not imply that suite covered these cases.

- R1 HIGH: a real physical net terminal fact exists, but no immutable rules result is produced until scoreboard consumption. The test isolates bridge timing; it does not validate all net-touch rules or geometry.
- R2 HIGH: a copied dead-ball state made before provisional resolution has no stable result identity. Delivering that stale copy after a new rally begins yields an extra transaction and score changing from 1-0 to 2-0. Setup includes explicit rule events, and the terminating ground contacts run through actual production physics; do not describe the entire setup as naturally played.
- R3 HIGH: an old pre-reset transaction passed through the real scoreboard updater changes a new live rally from serve_bounced to serve_pending. This is a lifecycle-composition test with injected setup facts, not physical collision evidence.
- R4 MEDIUM: center exit can certify feet established even while the supplied support envelope overlaps the NVZ. This was already an excluded geometry/conformance limitation, not a newly established regression in the bounded step-3 recovery fix.

These results strengthen the case for testing authority/identity seams; they do not establish that a broad new kernel or full event-sourcing system is required. Prefer existing R1-R3 as concrete discriminators over inventing duplicate probes. Separately compare the smallest local boundary correction with broader extraction costs. Preserve independent tests as an oracle; research must not modify or weaken them. No production remediation has been authorized by this addendum, and no G1 acceptance is claimed.

## Complexity evidence

Record source-backed counts if feasible, otherwise name the missing measurement. Useful proposed dimensions:

- Independent writers per authoritative fact.
- Distinct representations needing synchronization and whether they are truly redundant.
- Cross-layer authority edges and implicit ordering dependencies.
- Module/global mutable state affecting a second session.
- Files/concepts touched for one fixed real behavior change.
- Snapshot boundary and validation complexity; reproducible-failure localization effort.
- Total runtime integration, migration and maintenance cost, not merely domain LOC.

These are diagnostic dimensions, not a weighted universal score or a proven cognitive-load measure. Do not equate fewer states with correctness when the state encodes necessary rule history.

## Deliverables and continuation

Write a new uniquely named first-principles cycle note under `inbox/chiefstaff-homebase/` with valid frontmatter. Include:

- Concise conclusion with uncertainty and an ASCII ownership sketch.
- Source-grounded current duplication/coupling map; no invented public APIs.
- Perspectives, serious counterarguments and shortlist of things not to build.
- Retrieved primary source URLs/passages for substantive literature claims, with failed retrievals recorded honestly. Public network fetches must not transmit facility context or location.
- A deletion ledger: keep, derive, relocate, or remove; each row names evidence and acceptance needed.
- One next falsifiable experiment, or the executed narrow probe with raw evidence and exact limitations.
- Separate observed facts, mathematical/conceptual deductions, architecture proposals and human-benefit hypotheses.

Append a decision row using the existing ledger format after reading its current end. Update only the research atlas with a link and concise synthesis; do not revise G0-G7 criteria or the active patch. Run the KB schema validator; distinguish local Markdown persistence from database ingestion (not authorized for this cycle).

Stop this bounded cycle after producing the verified note and experiment disposition. Existing every-two-hour job continues its normal schedule; do not create a duplicate recurring job or unlimited agent fan-out. Subsequent scheduled cycles should select a single unresolved simplification hypothesis from the note rather than merely repeating all perspectives.
