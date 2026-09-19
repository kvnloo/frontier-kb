---
id: homebase-engine-critical-path
title: "Homebase local multi-sport twin: critical path and acceptance plan"
type: atlas
status: proposed
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, planning, tdd]
---

# Goal
Deliver a locally runnable, replayable facility twin in which a human can complete a regulation-profile pickleball match against a bot, while facility state persists, and the same simulation contracts support executable badminton and basketball slices without modifying the shared kernel for sport-specific rules. Prove correctness and fit on the actual PC before scaling sports or replacing more of the runtime.

This is milestone M1, not a promise to finish every sport. Long-term goal: a validated multi-sport facility simulation with authored assets, sport-specific contact and AI, persistent operations and reproducible optimization. A custom kernel is a candidate solution, not the success metric.

## Evidence and scope
See [[homebase-local-twin-research]], [[inbox/chiefstaff-homebase/runtime]], and /workspace/wt/homebase-engine-2026/docs/engine-audit/redesign-step-1.md. Candidate correctness patch has 14 regression tests; engine suite 1,184 passing; full suite retains two known failures and one unhandled error. Patch is not yet committed or fully accepted. Original code is an exhibition, not human gameplay. Scheduling experiment proved equivalence only for independent synthetic facility accounting; no reliable speedup. Production full-state restore remains absent through inspected APIs.

Production-game lessons here are recommendations grounded in Epic runtime/animation/networking documentation and local audit, not a claim all AAA studios use TDD or the same architecture. Source pointers: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine ; https://dev.epicgames.com/documentation/en-us/unreal-engine/networked-physics-overview ; https://dev.epicgames.com/documentation/en-us/unreal-engine/game-animation-sample-project-in-unreal-engine ; https://fmi-standard.org/docs/3.0/ . FMI is a contract reference, not a required dependency.

## Product assumptions to freeze
Provisional M1 is native desktop, offline/local authority, standard controller or keyboard/mouse, one playable court with a verified facility shell and representative background operation. Not VR, photoreal entire-facility full-fidelity simulation, or online multiplayer. Inventory actual spaces/sport variants; confirm football code before adding it. Pick governing bodies and exact rule editions, including pickleball 2026 primary sources, before claiming conformance. Enumerate target resolution, visual preset, active/background court counts, occupants and background workload in a versioned benchmark manifest. Do not fabricate facility occupancy/dimensions or expose its location.

Proposed initial performance targets, NOT measured achievements: packaged 1080p play at 60 FPS with p95 frame time at most 16.7 ms; local simulation p99 tick below its selected tick interval; product peak resident RAM at most 8 GiB and VRAM at most 8 GiB; no sustained catch-up backlog. Confirm feasibility against measured asset workload and host co-resident processes before locking. Report worst frames and input latency, not just percentiles. Set input-to-visible-response threshold after measuring actual display/input path; simulation responsiveness alone is not end-to-end latency. Select physics cadence from contact convergence tests, not a fixed universal rate. Never silently relax budgets or fidelity after optimization starts.

## Critical dependency chain
G0 scope + baseline -> G1 authoritative contact/result -> G2 owned state/replay -> G3 headless sport boundary -> G4 small native/runtime integration comparison -> G5 playable pickleball slice -> G6 different-sport proofs + facility scheduling -> G7 packaged acceptance.

Rules research, asset calibration and profiler preparation can run beside G1-G3. Full migration, mass asset polish, learned AI and an engine fork cannot replace these gates. Use one integration owner and separate worktrees for competing implementations. No automatic merges/pushes from research.

## G0: Lock acceptance and baseline
Owner: product/integration lead with rules and measurement reviewers.
Artifacts: match/benchmark manifest; actual facility inventory; issue-to-test matrix; explicit known-failure ledger; reviewed current patch.
Actions: independently review step-1 diff; rerun regressions; verify official rule edition and score variants; reproduce or isolate known full-suite failures without hiding them; profile actual packaged target when available. Do not treat old software-rendered browser FPS as GPU baseline.
Gate: every M1 criterion has an owner, scenario and measurement; baseline executable and versioned; zero unexplained failures in the milestone path. Repository failures need fixes or justified bounded quarantine with a real gate, never blanket ignoring.

## G1: Complete authoritative contact-to-result transaction
Owner: simulation engineer; independent rules reviewer.
Build one tracer bullet at a time: first/second ground contact, high-speed net/line tests, fault, winner, side-out, game point and new-serve lifecycle. Timestamp events with stable match/rally/entity IDs, tick and fractional contact time; define same-time ordering. Store immutable rally results and make presentation consumption idempotent. Remove timer/visual settling as score authority. Existing timeout fallback remains a migration target, not a permanent design.
Gate: real collision -> rules -> scoreboard tests pass for legal and illegal plays, rotated/translated courts, delayed/duplicate delivery and last-point/reset display. No event injection masquerading as a collision test. Sourced rule fixtures independently specify expected outcomes.

## G2: Simulation-owned state and replay
Owner: kernel/state engineer.
Own tick, stable athlete IDs, balls, rules/state machines, timers, cooldowns, command queue, pending contacts and per-system RNG in a session. Move hidden module globals behind owned state. Version snapshots and commands; validate units, schemas and IDs at boundaries. Rendering never owns authoritative data.
Gate: run -> snapshot -> destroy session -> restore -> continue yields matching events, scores and trajectories versus uninterrupted execution on same build/platform. Exercise snapshots immediately before/after contacts, scoring and rate transitions; new session cannot inherit old state. Persist build/rules/content versions. Reject incompatible checkpoints explicitly. Cross-platform bitwise determinism is not promised; require snapshot-assisted recovery where necessary.

## G3: Extract minimal headless sport contract
Owner: domain architect/integration engineer.
Candidate concepts (not existing API names): initialize, submit validated intent, fixed-step advance, committed events, observe, snapshot/restore. Shared services provide clock, IDs, scheduling, state persistence and engine service interfaces. Sport modules own rules, equipment/flight/contact models, scoring and tactics. Avoid universal BallModel or giant sport switch. Facility operations have their own eligible clock domain.
Gate: headless full pickleball scenario and renderer-backed scenario agree on domain outcomes; no render imports in domain; same commands drive bots and humans. Contract tests execute real module implementations. Cross-language golden data is independently sourced; current TS behavior is not truth when incorrect.

## G4: Decide runtime with a small competing slice
Owner: runtime engineer; profiler reviewer.
Compare preferred Unreal native game-owned domain path with the existing TS baseline under equivalent semantics. Include Godot native extension candidate if OSS is a binding product requirement; do not build every engine in parallel. Evaluate existing-runtime scheduler improvements before broader custom kernel. Spike one controllable athlete, ball/contact, headless runner and checkpoint. Record build/reimport/debug costs and license/platform constraints as well as runtime cost.
Gate: demonstrably working packaged candidate on actual PC with replay/correctness parity and measured resource cost. Write ADR choosing runtime/language and what is deliberately not forked. Choose C++ for Unreal integration if it wins; Rust/ECS/GPU compute are not goals. No language choice based on isolated RK4 microbenchmarks. Heavy installation/builds require resource scheduling and separate approval where needed.

## G5: Playable pickleball vertical slice
Owner: gameplay engineer and technical animator; human playtest reviewer.
Blender-author assets use validated scale, axes, court anchors, collision proxies, rigs, sockets and animation contact metadata. Deliver controls, camera, movement, anticipation, serve, strike selection, recovery, opponent, score UI and next-point transitions. Contact windows/assistance have explicit reach and timing bounds; animation notifies alone cannot grant contact. Start with inspectable tactical/utility AI, not GPU training.
Gate: human completes match against bot, including both players serving/winning/faulting, legal kitchen ground strokes and illegal volleys. Restart and save/restore work. Capture playable build, replay and profiler trace. Human tests cover responsiveness, contact believability, readability and tactical diversity separately from numerical accuracy. Automated input scripts do not substitute for playtesting.

## G6: Prove cross-sport and local-twin architecture
Owner: sport-module engineers plus facility engineer, isolated modules.
Badminton slice: shuttle-specific drag/orientation, racket contact, trajectory calibration and ground termination. Basketball slice: possession/free flight, dribble, release, rim/backboard, catch and a selected temporal violation. These are explicitly slices, not complete regulation games. Tennis and football modules follow after these architectural differences are proven.
Add one actual verified facility operation with event-driven or lower-rate scheduling and persistent state. Keep active court physics unchanged. Define how far-field/detail transitions conserve the domain facts and bound uncertainty. Do not reduce fidelity for a match whose authoritative outcome must remain exact; either continue exact headless simulation or explicitly mark approximate background activity. Test coupling events and same-time transitions, not only independent room counters.
Gate: both sport slices run through the same headless/state/replay contracts; no sport-specific conditional branches added to shared kernel, except justified general contract evolution reviewed and tested across all modules. Facility save/load and transition scenarios preserve declared invariants. Measured workload is actual or clearly labeled synthetic and never extrapolated as facility capacity.

## G7: Acceptance and expansion decision
Owner: independent verifier/integration lead.
Run packaged build at frozen manifest and hardware preset. Exercise held-out layouts/seeds, boundary scenarios, session restoration, long-running bot matches, content reload and telemetry absence. Proposed soak is 60 minutes with bounded memory growth and no unexplained state divergence; define tolerance before run. Separate quiet-host baseline from an explicit co-resident-workload profile. Freeze reference clips/scenarios and report p50/p95/p99 CPU/GPU/tick times, memory, stalls, contact disagreements and input latency.
Gate: M1 goal demonstrated; all critical defects resolved; no unexplained acceptance failure; logs/build/replay reproducible. If budget missed, return to measured bottleneck with correctness locked, not a wholesale rewrite. Online multiplayer is a subsequent gate with server/two-client latency/jitter/loss tests; authority and command boundaries are designed now but netcode does not block offline M1.

## TDD and evaluation process
Use vertical RED -> GREEN -> REFACTOR per behavior. RED must be expected behavioral failure, not fixture/import error. Small pure tests cover domain math; real integration tests cover contact through score; replay and metamorphic tests cover transformed worlds, rate independence, session isolation and duplicate events. Calibration validates trajectories/contact against measurements and uncertainty, not merely implementation self-consistency. Use mutation checks selectively on critical adjudication to prove tests reject broken logic. Test game builds and human experience as separate gates. Do not TDD artistic appearance through brittle pixel tests; validate import contracts and use locked-camera visual review for art.

Every change record includes hypothesis, expected behavior, source/rule provenance, RED output, minimal diff, GREEN output, broader regression, replay artifact and relevant profiler comparison. Independently review critical rules/event fixtures so optimizer and implementation do not co-author a self-confirming oracle. Fix test flakiness at source and retain failure seeds.

Fast lane per edit: affected unit/integration tests and typecheck. Integration lane per accepted unit: engine suite, full affected app suite, snapshot scenarios and build. Scheduled lane: headless soak, held-out fixtures, targeted mutation, asset validation and packaged performance. Gate passes reflect exact scope, never a test-count vanity metric.

## Autoresearch contract
Scheduled research continues every two hours. Each cycle asks one question and may propose one bounded experiment; no autonomous production promotion. Objective is a constrained Pareto frontier over frame/tick tails, latency, RAM/VRAM, build/iteration effort and calibration error. Correctness and fidelity are hard constraints, not score penalties that can be traded away.

Before any optimization: pin baseline/candidate code and content, command tape, hardware/load profile, seeds, measurement settings and holdouts. Compare paired repeated samples with order balancing, report uncertainty and effect size, keep raw failures. JITless diagnostic results do not select a production runtime. Holdout access belongs to verifier; after repeated inspection rotate/add unseen scenarios. Promote only independently verified relevant wins. On plateau switch hypotheses/subsystems; do not churn changes or claim reduced work equals speedup.

## Immediate queue
1. Review candidate step-1 changes and close only findings actually proven fixed.
2. Add physical second-bounce -> immutable rally -> delayed scoreboard regression, RED first.
3. Add snapshot/restore across that exact scenario with session RNG/timers included.
4. Define benchmark manifest and capture a target-hardware baseline.
5. Publish G3 contract from executable experience; then authorize bounded native/runtime spike.

Do not attach a completion date until G0 inventories assets, target modes and capacity. Forecast using time spent on the first accepted end-to-end unit, with technical-animation acquisition and native toolchain setup as explicit schedule risks. Gate sequence is the committed plan; calendar estimates remain estimates.

## Goal text for a tracker
"M1: Deliver a locally runnable, replayable Homebase facility twin with one complete human-vs-bot pickleball match, badminton and basketball proof slices on shared sport contracts, and a reproducible target-PC correctness/performance report. No sport-specific rules in the shared kernel; no unexplained acceptance failures; no full-engine rewrite without a measured need."
