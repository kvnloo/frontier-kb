---
id: homebase-audit-runtime
title: "Homebase audit: runtime"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
---

Source snapshot; relative evidence links resolve in /workspace/wt/homebase-engine-2026/docs/engine-audit/.

# Runtime engine and gameplay audit

## Verdict

**The current product is an autonomous pickleball facility exhibition, not yet a player-controlled sports game. Its RK4 flight integrator is real and is used in the running animation. Its scoring bridge is not reliable enough to treat the rendered match as a correct rules simulation.** Preserve and harden the useful numerical/rules modules before choosing a port; do not mechanically port the current animation/ball/rules boundary.

Scope: worktree `/workspace/wt/homebase-engine-2026`, HEAD `9d98e3e83dc50b808a872546b78b555e2f83cdb4`. Read project instructions, manifests, engine, tests, player/input/animation/render bridges, and relevant API entry points. No production source/test/config changes or commits. Existing dirty `dmms/dmms.db` was retained and updated additively after schema inspection. Audit task **53**; new open issues **AUDIT-RUNTIME-01 through AUDIT-RUNTIME-10**. No issue was fixed or marked resolved.

Evidence levels below distinguish executed counterexamples, static integration findings, and proposed acceptance criteria. “USAPA 2025” is the repository's stated target, **not independently established certification against an authoritative 2025 rulebook**.

## 1. Real baseline execution

Environment measured: Linux 7.2.2-1-cachyos x86_64, Intel Core i9-10900KF, Node **v26.5.0**, npm **12.0.2**. Local dependencies were initially absent. Initial `npm run test:engine` exited 127. `npm ci --ignore-scripts` then succeeded; the lockfile was not changed. Suppressing install scripts matters for the native benchmark dependency below.

| Command, run in audited worktree | Actual outcome | Scope / caveat |
|---|---|---|
| `npm run test:engine` | Exit 0; **27 files, 1,170 tests passed**, 12.04 s wall time | Vitest/jsdom, includes property, statistical, golden trajectory, adapter and bridge tests; not a human-playability or WebGL validation |
| `npm test` | Exit 1; **101 files passed, 2 failed; 2,320 tests passed, 2 failed; 1 unhandled error**, 16.75 s | Full root Vitest suite, not nested API/server test suites or Playwright |
| `npx vitest run tests/accessibility.test.jsx tests/facilityGenerator.test.jsx` | Exit 1; **34 passed, same 2 failed, same 1 unhandled error** | Reproduces failures outside full suite; not dismissed as cross-suite flakiness |
| `npx tsc --noEmit` | Exit 0 | `tsconfig.json:23-24` includes **only src/engine TypeScript**, excluding tests and the JS/JSX bridge |
| `npm run build` | Exit 0, Vite 7.3.1, 198 modules, 2.16 s | Main JS 1,055.41 kB / gzip 294.88 kB; >500 kB chunk warning |
| `npm run lint` | Exit 1; **1,000 errors, 6 warnings** | Repository-wide existing lint debt; no autofix used |
| `npm run benchmark -- --label runtime-audit --url http://127.0.0.1:5190` | Exit 1 | `better-sqlite3` native bindings missing after script-suppressed install; stock runner cannot initialize DB |

The two full-suite failures are `tests/accessibility.test.jsx` → Header → “day selector buttons have accessible text”, and `tests/facilityGenerator.test.jsx` → “navigates to twin page after generate”. The latter throws `TypeError: Cannot read properties of undefined (reading 'setItem')` at `src/services/configStorage.js:69`, called from `src/pages/FacilityGenerator.jsx:138`. Log this as a baseline failure; the audit does not establish that every production browser has the same localStorage failure. jsdom canvas-not-implemented diagnostics also appear. The intentionally simulated GPU-error test is not a newly discovered crash.

Measured `tests/engine/` total is **19,006 physical lines**, not “17k tests” and not 19,006 assertions. Passing engine tests do not falsify the integration counterexamples below. For example, `tests/engine/bridgeIntegration.test.ts:44-67` manually injects a valid serve/bounce sequence instead of executing a physical net fault through `updateBall`.

Persistent evidence: [engine-baseline.log](evidence/engine-baseline.log), [runtime-probe.log](evidence/runtime-probe.log), [browser-results.json](evidence/browser-results.json). Additional full raw command logs remain under `/tmp/homebase-*-baseline.log`, `/tmp/homebase-typecheck.log`, `/tmp/homebase-build.log`, `/tmp/homebase-lint.log`, `/tmp/homebase-failures-rerun.log`, `/tmp/homebase-stock-benchmark.log` for this session.

## 2. Runtime trace: what actually drives the scene

1. `src/main.jsx:7-12` mounts React StrictMode and BrowserRouter. `src/App.jsx:17-21` routes to `DigitalTwinPage`; `src/pages/DigitalTwinPage.jsx:22-45` supplies a facility configuration and wraps the twin in an error boundary.
2. `src/hooks/useDigitalTwin.js:87-105` builds courts, players, scoreboards and balls and creates **enabled-by-default EngineAdapter** over `COURT_DEFS`. `:107-108` exposes context to the UI; `:132-139` connects orbit/court-selection controls; `:156-158` starts the animation loop.
3. `src/animation/animationLoop.js:19-20,274-282` runs an actual **60 Hz fixed accumulator**. Each tick updates players, scoreboards, spectators, then balls (`:158-165`). This corrects the impression that the entire current runtime is simply variable-delta legacy animation.
4. Ball flight is subdivided to at most **1/120 s** in `src/animation/updateBall.js:123-139`. It calls `tickCourtBall`, which calls `_rk4.rk4Step` in `src/utils/physics.js:117-127`. Net detection and first ground bounce use that engine (`:129-149`). **RK4 is therefore used in gameplay/exhibition, not merely an unused exported class.** The standalone `PhysicsEngine.integrate` accumulator is *not* the integration method called by this bridge.
5. Real player animation reaches a timer/proximity contact and sets `ball.returnReady` (`src/animation/playerStateMachine.js:283-294,346-355`); `updateBall.js:140-170` reports a hit then launches an AI return. This is coupled animation, not a fully prerecorded animation, but not a physical paddle impact either.
6. The ball's `rallyEnded` flag drives the next scoreboard tick. `src/animation/updateScoreboards.js:32-54` calls `processRallyEnd`, copies engine score into legacy `scoreData`, syncs the serve and starts/reset games. `:75-82` redraws the texture atlas and jumbotron. `src/components/ui/GameScoreboard.jsx:27-78` separately reads the selected court's engine and match-score data. These are distinct consumers, not a single authoritative scoreboard view model.
7. `src/animation/SimState.js:61-115` snapshots **render meshes**, not full game state; `:141-168` interpolates matrices/positions and `:174-195` writes them back to rendering. This is render interpolation, **not replay serialization**.

### XState claim

`src/engine/MatchStateMachine.ts:9,38` imports XState and exports a machine definition. However `CourtEngine.ts:108` instantiates `MatchStateTracker`, whose `send` uses its own hand-built transition table (`MatchStateMachine.ts:127-166`). Thus “XState CourtEngine” overstates the runtime: a TypeScript facade with manual trackers and an XState definition is present, not an XState actor orchestrating the simulation. The render bridge still owns ball life-cycle decisions.

## 3. Correctness findings and executed counterexamples

### Critical: terminal ball cause is lost before scoring — AUDIT-RUNTIME-01

`src/utils/physics.js:133-138` ends the visual rally on a net hit but stores no net-fault event/cause. Out-of-bounds follows the same pattern at `:160-170`. `updateBall.js:132-138` reports only the bounce that transitions into `bounce_pause`; an out-of-bounds terminal bounce does not take that path. `EngineAdapter.ts:144-154` assumes any unprocessed ending is **unreturned** and calls `CourtEngine.onBallUnreturned`, which faults `lastBounceSide` (`CourtEngine.ts:372-383`).

**Executed:** create a real adapter, call `onServeHit`, fly an active ball into the net using `tickCourtBall`, then call `processRallyEnd`. The ball ended, but the resulting fault was **double_bounce on team 2**, and **team 1 was awarded 1-0-2 for serving into the net**. Exact result is in `evidence/runtime-probe.log`. This is not a disputed interpretation of a rule or an inference from comments.

Also, engine faults found mid-flight/mid-hit do not immediately stop the visual ball: `updateBall.js:134,147-149,168-170` ignores returned engine events and continues/launches the shot. The two authorities can disagree until a separate visual termination occurs.

### High: NVZ integration identifies a different player — AUDIT-RUNTIME-02

`updatePlayers.js:73-75` reports positions under **p0, p1, ...**. `updateBall.js:147,168` reports every hitter under **player**. `NVZTracker.ts:30-40` initializes an unknown key as outside the NVZ with established feet.

**Executed:** after a legal serve/return/two-bounce setup, position `p0` inside the kitchen. A volley by key `player` emits no fault and does not end the rally; the identical volley by key `p0` emits `nvz_volley`, ends the rally, and changes serve.

A second static bug compounds this: `src/scene/players.js:41-47` sets numeric sides **1/2**, but `updatePlayers.js:74` compares `home.side` to strings **top/left**, so every position update is reported as team 2. Position reporting is additionally restricted to approach/swing/volley (`updatePlayers.js:23-28`), omitting recovery/kitchen-retreat momentum tracking. Fixing IDs alone is insufficient.

### High: post-bounce/contact physics are exhibition approximations — AUDIT-RUNTIME-03, -10

* `src/utils/physics.js:101-112` uses vertical Euler settling in `bounce_pause`, stops advancing horizontal position and does **not** report/count further floor contacts. `:173-175` resets the count immediately on entering pause. The second contact therefore does not implement the comment in `updateBall.js:152`; a real-time timeout (`:159-178`) stands in for failed return. The ball can visually bounce repeatedly while remaining returnable.
* `launchReturnShot` overwrites contact height (`physics.js:369-371`), then prescribes a new velocity. No swept paddle plane, angular/linear paddle velocity, contact normal, impact point or equipment collision response is calculated.
* Actual contact checks are horizontal center-distance <1.2 m and swing-time thresholds (`playerStateMachine.js:286-294,348-355`). Volley entry checks height <1.5 m (`:255-258`), but the contact check itself does not recompute a paddle/ball 3D intersection.
* Serves are activated after a fixed 1.05 s timer (`updateBall.js:42-45,93-102`). Despite the “behind baseline” comment, initial ball position is 0.3 m **inside** the baseline (`physics.js:205-215,232-234`). The runtime does not supply a validated physical foot/paddle/waist-contact state. Standalone rule helpers do not make foot faults or partner contact observable.
* `physics.js:163` can terminate a rally solely because rally count exceeds 30. `:164-165` assigns a near-line eagle-eye visual call from a rally-count expression, not authoritative line-contact geometry.

For a stylized sports game, assisted targeting can be intentional. It must be explicit gameplay policy feeding commands and contact constraints, rather than invisible teleport/rebounce allowances that invalidate rules.

### High: net geometry is orientation/radius incorrect — AUDIT-RUNTIME-05

`PhysicsEngine.ts:418-427` always calculates lateral sag from **world X**, even for a net perpendicular to X, and compares center height to net height without ball radius. It has no lateral extent rejection, so the net behaves as an infinite plane for collision. Ground bounce also resolves after penetration rather than finding time of impact (`:307-365`); it reports a bounce even at the ground with upward velocity. No general continuous collision detector for paddle, net posts, player bodies, walls or equipment is present in this path.

**Executed rotation counterexample:** equivalent horizontal/vertical trajectories at 0.88 m height and 3 m lateral displacement yielded horizontal `hitNet:false, netHeight:0.8636` versus vertical `hitNet:true, netHeight:0.9128125984`. A rotated court must not change the same contact outcome.

### High: rally scoring depends on event encoding — AUDIT-RUNTIME-04

Standard side-out scoring and server sequencing have substantial passing tests and are useful foundations (`ScoreKeeper.ts:81-110,141-167`). Do not infer that optional rally scoring is correct. `processFault` never checks `rallyScoring`, whereas `processWinner` does (`:117-139`).

**Executed:** under `new ScoreKeeper(11,2,true,true)`, a serving-team net fault gives the receiving team **0** points, while an equivalent receiving-team `winner` gives **1**. The claimed serving-only winning-point handling is also ineffective: both branches add the point (`:120-128`) followed by unconditional `checkGameOver` (`:157-163`). Version the desired scoring variant and test normalized outcomes against it rather than treating code comments as rules authority.

### Medium: game-over display and match completion — AUDIT-RUNTIME-06

`updateScoreboards.js:39-50` syncs the old match games count, records the game win, immediately resets the engine, zeros legacy points, and only *then* starts the supposed final-score cooldown. The call/server number fields set by `EngineAdapter.ts:310-315` are not resynced on this reset; games-won texture values lag. Therefore the comment “show final score briefly” does not describe the state being rendered. `CourtEngine.ts:95` stores `bestOf`, but no other runtime use was found; `EngineAdapter.ts:332-343` only accumulates games won. There is no enforced best-of match finish.

`EngineAdapter.ts:181-187` also infers the scoring team from the **post-transition** serving team, so metadata can incorrectly name a scorer after a side-out even when no point changed; already-processed rallies lose `sideOut` event information at `:144-147`. Consumers should receive an immutable before/after scoring transaction, not reconstruct outcome from current serve.

## 4. Spin, AI, input and networking

### Spin: implementation present, default gameplay disconnected

`PhysicsEngine.ts:128-155,211-244` implements RK4 with optional Magnus acceleration and spin propagation/decay. `:103-110` defaults `enableSpin` to false. The live singleton is `new PhysicsEngine()` (`physics.js:24`), and the bridge constructs six position/velocity fields without spin (`:118,143`). The ball state contains no spin fields (`:56-87`). Therefore **gravity + drag RK4 is live; Magnus/spin/bounce-friction gameplay is not enabled**. The `BounceModel` spin path is gated by enabled, present, **nonzero** spin (`PhysicsEngine.ts:314-329`), so even a spin-enabled zero-spin ball takes the frictionless default bounce path.

### AI: heuristic automated play, not adaptive opponents

`src/engine/ShotSelection.ts:74-164,169-186,196-335` weights and randomly selects shot types. The bridge calls it (`physics.js:336-359`) but passes `playerX/playerZ` equal to the **ball** position and selects `playerSide` from relative Z even on horizontal courts. Target bias is applied to randomized targets, and minimum-speed/net-clearance clamps can override the selected shot (`:361-391`). No opponent positions, tactical team state, learned policy or search over opponent response is passed.

`src/animation/playerApproach.js:20-68` assigns the nearest player on each side, limited to 3.5 m from the intended target. `:85-113` uses a fixed blend of home/landing/net positions, not an RK4 intercept solve. `_findNetClearAngle` (`physics.js:28-52`) repeatedly runs a separate **Euler** mini-simulation, not the same RK4 integrator. This can be both an accuracy mismatch and a contact-time CPU spike; it must be measured separately before replacing integrators.

### Input: no athlete command/control path found

The real canvas controls select a court and orbit the camera (`useDigitalTwin.js:132-139`). Keyboard shortcuts open management panels (`DigitalTwin.jsx:196-221`); WASD is explicitly reserved for the **cleaning robot**, with `src/components/ui/robot/DPad.jsx` handling robot movement. Searches for keyboard/gamepad/pointer gameplay integration found no player ownership, move/aim/swing/serve command queue into the sports simulation. Timers, schedule state and AI drive both teams. Calling this a playable pickleball game today would be misleading.

### Networking: business APIs, not match transport

Source search for `WebSocket`, `socket.io`, `RTCPeerConnection`, and related transport calls found no authoritative multiplayer match loop in src/api/server code. Existing calls include `src/services/profileService.js:7-36`, floor-plan analysis (`floorPlanAnalyzer.js:164`), and `api/src/routes/{profiles,facilities,courts,bookings,robots,cleaning,analytics}.ts`: profile/facility/business operations. These are not player-input transport, server ticks, replication, rollback, matchmaking, ownership or anti-cheat. Nested API/server tests were not executed; this is a sports-runtime integration conclusion, not an audit of every backend feature.

## 5. Determinism and replay — AUDIT-RUNTIME-07

Useful pieces exist: fixed simulation ticks, pure numerical functions, and `SeededRng.ts:20-21`. **Executed:** reseeding and rerunning `HeadlessSimulator.simulateGame(true)` produces identical serialized result/event data within this Node runtime.

That is not full gameplay replay:

* Default RNG captures `Math.random` at module load (`SeededRng.ts:12`). Benchmark later reassigns `Math.random` (`benchmarkMode.js:83-85`), **not** that captured function, so its advertised seed does not seed engine `rng()` calls. It runs after scene construction as well (`useDigitalTwin.js:150-154`).
* RNG is module-global, not per match/court, and exposes no save/restore state. Other courts and animation calls can change subsequent draws.
* `NVZTracker.ts:155` records wall-clock `Date.now`; full state snapshots are not time-independent. Simulation speed also uses different clocks/caps for ball, player and cooldown (`animationLoop.js:80-82,158-165`; `updateBall.js:54-59`). Long frames >250 ms are discarded (`animationLoop.js:254-255`).
* Player state is module-global and reused when player count matches (`updatePlayers.js:13-20`); serve/pause timers and initialized flags are module-global (`updateBall.js:28-35`). Independent sessions/remounts cannot assume a clean state simply by rebuilding the adapter.
* `EngineAdapter.ts:355-358,384-388` exposes a bounded event log; it is not a tick-indexed input log or replay format. `SimState` snapshots only render values, not rule state, RNG, timers, ball velocities or player state machines.

Required replay contract: versioned initial state + fixed tick inputs + per-match RNG state + authoritative event order + canonical state hash + snapshot/restore. Test same command stream under different render rates, pause/resume, session remounts, court counts and target runtimes. Cross-language floating-point bit-identical replay is **not** established by these tests.

## 6. Actual performance measurements and limits

### CPU/headless probes

A temporary harness bundled the actual repository modules with installed esbuild, outside production source:

```sh
./node_modules/.bin/esbuild /tmp/homebase-runtime-probe.ts --bundle --platform=node --format=esm --outfile=/tmp/homebase-runtime-probe.mjs
node /tmp/homebase-runtime-probe.mjs
```

No engine code was replaced. Exact temporary harness sources are preserved as audit text: [runtime-probe-source.txt](evidence/runtime-probe-source.txt) and [browser-harness-source.txt](evidence/browser-harness-source.txt). Copy these back to the `/tmp` filenames above to reproduce on the same worktree. The harness performed the counterexamples above, a seeded batch warmup plus five measured 10,000-game batches, and a 100,000-step RK4 warmup plus five measured million-step loops. Timed data below is wall-clock `performance.now`, rounded for presentation; full data in `runtime-probe.log`.

| Measured workload | Five runs (ms) | Interpretation |
|---|---|---|
| `HeadlessSimulator.simulateBatch(10000)`, seed runtime-audit | 2246.665, 2414.734, 2360.549, 2646.181, 2212.099 | Median **2360.549 ms**, ~**4236 games/s**; final batch 10,000/10,000 completed |
| `PhysicsEngine.rk4Step`, 1,000,000 steps, dt=1/120, default no spin | 1696.214, 1288.302, 1332.012, 1303.572, 1209.542 | Median **1303.572 ms**, **1.304 microseconds/step**; final state finite |

**The headless game benchmark does not run physics, player movement, collision, rendering, or actual AI shot flight.** `HeadlessSimulator.ts:183-245` injects valid bounce/hit positions and random terminal events. It is a rules/event-throughput workload, not 10,000 rendered matches. Its final stats were 4918 team-1 wins, 5082 team-2 wins, mean 31.0072 rallies/game; not real gameplay balance evidence. RK4 microbenchmark is an extended free-flight loop without ground/net/paddle checks and is not a frame-time estimate. CPU timing was not isolated from other host work and no confidence interval or cross-hardware conclusion is claimed.

### Headless browser: successful, explicitly software-rendered

The installed Playwright browser initially did not exist. `npx playwright install chromium` downloaded its archive but exceeded 180 s before completion. An available **system `/usr/bin/chromium`** was used instead. Default Vite base `/mvp_homebase/` and BrowserRouter without basename (`vite.config.js:7`, `main.jsx:9`, `App.jsx:21`) caused benchmark attempts to time out / lose the query. A command-line-only override recovered execution:

```sh
npm run dev -- --host 127.0.0.1 --port 5190 --strictPort --base /
# HTTP health check returned 200
node /tmp/homebase-browser-audit.mjs
```

Temporary Playwright harness used headless system Chromium, viewport 1280×720, arguments `--no-sandbox --use-angle=swiftshader --enable-unsafe-swiftshader`; URL `/?benchmark=true`; waited for `window.__benchmarkComplete`; extracted actual `__benchmarkResults`. **GPU renderer verified:** ANGLE Vulkan SwiftShader (Subzero), not the host's hardware GPU.

Latest run: **600 samples after 60 warmup frames**, mean **74.942 ms**, p50 **66.700 ms**, p95 **133.200 ms**, p99 **216.700 ms**, ~**13.34 FPS**. Quantiles here use sorted sample index `floor((n-1)*p)` except median. At extraction: **184 draw calls, 10,288 triangles, 41.18 MiB JS heap**; no uncaught page errors; material warnings about emissive properties on MeshBasicMaterial. Read-only inspection of the live React ref confirmed **11 in-play courts, 44 spawned players, 7 active balls, 64 adapter log events**. Thus this was actual running scene/gameplay, not just a blank canvas benchmark. These counts are a snapshot at completion, not assertions that all balls were active in every frame.

An earlier successful software run had mean 66.164 ms, p50 66.6 ms, p95 100 ms, p99 133.2 ms, 178 draw calls and 9294 triangles. Variation is expected: this benchmark does not actually seed the engine, collection uses elapsed wall time, and software rendering is sensitive to host load. Do not call either run a native GPU or prospective port performance result.

Harness limitations: `benchmarkMode.js:115-116` discards frames >250 ms; its “gcPauses” is only a >2× rolling-mean frame heuristic (`:132-138`), **not measured GC**. The latest heuristic count was 1. Robot cameras are disabled (`:73-74`), and the default performance mode is not the stock runner's uncapped GPU-flags configuration. The stock runner also fails first at native DB initialization; no `perf/perf.db` result was invented. Full Playwright E2E, native GPU profiling, input latency, networking latency and mutation testing remain **unrun**. Stock-browser installation/native DB runner were blocked; successful software fallback does not erase those limits.

### Performance priorities supported by inspection

The real optimization boundary is larger than RK4. `PhysicsEngine.rk4Step` allocates derivatives/results; `physics.js:118` allocates input state. `playerApproach.js:27,61` creates per-tick maps/records despite “zero allocation” comments. Shot angle search is nested repeated simulation (`physics.js:28-52`). Event logs shift arrays (`EngineAdapter.ts:387-388`). Render interpolation copies full mesh matrices (`SimState.js:121-168,174-195`). Optional robot cameras perform synchronous GPU readback and CPU pixel conversion (`animationLoop.js:323-350`), disabled in measured browser runs. Instrument those costs and allocation/GC before changing language, SIMD layout or numerical method. Instanced players and fixed-tick/interpolated rendering are useful foundations already present.

## 7. Playable multi-sport gaps and recommended boundary before a port

The current engine hardcodes pickleball geometry/config (`CourtEngine.ts:77-95`), pickleball shot policy (`ShotSelection.ts`), a two-team serve sequence and NVZ rule facade. No tennis/badminton/basketball/football sport module was found in inspected runtime source. Extending dimensions alone is not a multi-sport engine.

| Sport | Reusable foundation | Missing sport-specific contracts / acceptance cases |
|---|---|---|
| **Pickleball** | Side-out scoring/serve modules, two-bounce/NVZ helpers, RK4 drag, court geometry, animated rendering | Player input/ownership; real hitter IDs; reliable terminal events; serve legality/foot contacts; continuous paddle/net/ground contacts; physical second-bounce termination; singles/doubles formation; momentum/partner NVZ; rally-scoring variant; best-of completion; deterministic replay |
| **Tennis** | Numerical integrator, common racket contact framework, court coordinate transforms, renderer/input abstractions | Different ball mass/drag/spin/bounce; first/second serve and service lets; deuce/advantage, games/sets/tiebreak variants; singles/doubles lines, changeovers; appropriate movement/reach and stroke policy. Pickleball's NVZ/two-bounce rules must not leak in |
| **Badminton** | Racket/input/contact and generic match lifecycle abstractions | Shuttlecock's strongly different aerodynamic model and orientation/stability; no ground-bounce rally continuation; distinct service court/height rules, rally scoring and interval/end-change variants; high-speed overhead contacts and shuttle interception |
| **Basketball** | Simulation clock, entity identity, general contacts, rendering and transport interfaces | Possession and hands/ball constraints; dribble, travel/double-dribble; rim/backboard/net scoring volumes; 1/2/3-point logic; shot/game clocks, periods, inbound/free throws; team movement, body contact/fouls and player switching |
| **Association football / soccer** | General ball physics, field transforms, team/input/net transport concepts | Foot/head/body contact, controllable possession/dribble, tackles/fouls; whole-ball goal/line decisions; offside; restarts, goalkeeper/penalty-area rules; formations, team AI, match clock and substitutions |
| **American football** | Generic simulation/input/entity/transport concepts only | Distinct elongated ball, throws/catches/possession; downs, distance, scrimmage, snap; legal pass eligibility, forward-pass limits; tackles/contact, dead-ball/spotting; touchdowns/tries/field goals/safeties; clock/play clock and formations |

**“Football” is unresolved product scope. Soccer and American football are separate sport modules with different possession/contact/rules models; do not silently choose one or estimate both as one port.** Proposed acceptance cases above are architectural requirements, not claims of implemented rules or exhaustive governing-body rulebooks.

Recommended seam, without rewriting now:

1. **Authoritative simulation:** own ball/player/equipment state, collision/contact events and fixed ticks independently of Three.js. Normalize court/field coordinates. Share common numerical math and collision primitives, not all sport rules. Choose continuous/swept contacts for fast ball/equipment pairs.
2. **Sport package:** versioned equipment/aerodynamic and surface models, field geometry, legal-action policy, possession/serve model, score/match reducer, and sport AI. Use semantic facts (`groundContact`, `paddleContact` with player ID, `netContact`, `out`, `goalCrossing`) rather than ambiguous `rallyEnded` flags.
3. **Input and AI:** both produce the same tick-stamped action command format. Separate assistance (aim/approach/contact grace) from mechanics so single-player feel and networking authority are testable.
4. **Projection:** render immutable snapshots, interpolate positions/orientations, and animate toward authoritative contacts. Publish one immutable scoring transaction/view model to React and 3D texture consumers. Never let a scoreboard decide rally outcomes.
5. **Replay first, networking second:** snapshot/restore every authoritative field and per-match RNG, then validate deterministic command replay. Later add server authority, input sequencing, snapshots, prediction/interpolation and correction. Use measured product latency needs to choose rollback rather than assuming every sport shares a lockstep model.
6. **Port gates:** retain numerical/rules test corpus, add real bridge regressions for every executed counterexample, rotated/transformed-court metamorphic tests, replay hashes under multiple render schedules, and at least one complete human-controlled match. Compare *the same inputs and semantic outcomes* across languages. Benchmark CPU tick percentiles/allocations, AI prediction cost, GPU frame breakdown and input-to-contact latency separately.

The evidence supports fixing ownership and contracts before pursuing a faster implementation language. A fast rules microbenchmark cannot compensate for awarding a point to a serve into the net.
