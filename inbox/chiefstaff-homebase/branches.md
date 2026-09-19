---
id: homebase-audit-branches
title: "Homebase audit: branches"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
---

Source snapshot; relative evidence links resolve in /workspace/wt/homebase-engine-2026/docs/engine-audit/.

# Homebase branch and engine audit

Audit completed (UTC): `2026-09-14T05:15:23.317359+00:00`.

## Outcome

**No newer committed TypeScript rules/physics engine was found.** Every inventoried tip and existing detached HEAD has the same `src/engine` Git tree. The differences worth considering are animation/integration, player presentation, camera input, and uncommitted oracle tests—not a replacement engine.

- Inventory: **103 local refs + 106 remote-tracking refs = 209 refs**, 105 distinct commits, 100 conservative source/test/config content groups.
- GitNexus: **13/100 committed integration groups indexed and verified**, representing 18 content-equivalent commits and 35 refs; **2 additional dirty-source snapshots** indexed separately.
- Prioritized coverage: **1/1 engine trees, 2/2 engine-test content variants**, and all 73 observed present-file blob variants across animation, controls, engine tests and `src/scene/players.js`. This is **not** every integration combination.
- **87 integration groups remain unindexed.** They are fully inventoried and explicitly marked below. Broad source grouping deliberately retains asset initialization/hook and test differences.
- Recommendation: keep `feat/engine-usapa-2026` / `feat/optimize` at the audited `9d98e3e` as the focused engine base. Consider individual presentation/input commits and recover the dirty oracle/property tests after review; do not merge a whole asset lane to obtain an engine that is already identical.
- This was a source/graph audit, not a test run or a measured performance comparison. No runtime, mutation, visual, or USAPA-2026 conformance pass is claimed.

## Scope, lineage and safety

Canonical repository: `/mnt/zer0models/workspace/zer0/products/homebase-pickleball`. Confirmed Homebase `src/engine/PhysicsEngine.ts`, `EngineAdapter.ts`, and `tests/engine/`; **pickleball-palace-builder was not indexed**.

Read canonical `CLAUDE.md` and saved each selected revision’s available `CLAUDE.md`/`AGENTS.md` under `evidence/`. Explicit read-only/no-commit authorization overrides the repository’s routine DMMS/commit workflow for this audit: no DMMS writes, commits, merges, stashes, resets, pruning, or changes to existing application source were performed. Indexing used newly created detached audit worktrees, unique aliases and a serialized lock. Existing dirty sources were only read/copied.

- `origin`: fetch succeeded with `--no-prune --no-write-fetch-head` and automatic Git GC disabled.
- `operation-autopilot`: fetch failed with “Repository not found”; its existing remote-tracking refs were still included but cannot be asserted current. Authentication prompts were disabled; no credentials were guessed.
- Seven pre-existing worktree registrations were captured before audit worktree creation: five existing directories, including two clean detached treehouse worktrees at `959a96b`; two `/tmp` registrations were stale/prunable and were not pruned. The stale detached `3f6bd126` commit was conservatively included too.
- The refs/commits audit is a point-in-time snapshot of tips and recorded worktrees, not an assertion that every historical ancestor/reflog object was indexed.

## Content identity and method

All committed `src/engine` trees: `0362d2e5e0411ab9cc0d9542efdcab77c4699b6a` (19 files, 4577 source lines).

Engine-test Git trees: `5510dd0d17679b60747c8445d1205fc32aebcc0d`, `aa5ff2936490d2346bc375dc0fb331ee93dcdb2a`. The only changed path within `tests/engine` is `facilityLayout.test.js`; this is a facility-layout expectation difference, not an alternate rules/physics oracle.

Primary grouping hashes canonical JSON manifests of Git tree entries `(path, mode, type, blob hash)` using SHA-256, with separate engine/test/integration hashes. Scope is all `src/`, all `tests/`, package manifests/lock and listed Vitest/Vite/TypeScript root configs; exact selected entries are retained per group in `inventory.json`. This conservative superset prevents a shared engine commit from hiding a changed adapter consumer, input handler, test fixture or initialization hook. A narrower gameplay discovery manifest still yields 91 variants, largely because of asset initialization in `useDigitalTwin.js`; it is not used to pretend those variants were indexed.

Historical engine changes were traced with `git log --all -- src/engine tests/engine`: initial rules engine `fa6e4a6`; animation/rules bridge `10e5517`; horizontal-court bounds correction `9841268`; advanced tests `a919165`; analytics `ef555f0`; facility tests `b64101a`; kiosk/layout update `72ebfd5`. Every inventoried tip contains the same final rules/physics source content.

## Integration and input/AI paths

- Physics runtime: `src/utils/physics.js` imports `PhysicsEngine` and `selectShot` through `src/engine/index.ts`; `tickCourtBall` is called by `src/animation/updateBall.js`. The pure TS engine is not an unused alternative simulator.
- Rules events: `updateBall` sends serve/bounce/hit events to `EngineAdapter`; `updatePlayers` sends player positions; `updateScoreboards` consumes rally endings, synchronizes legacy `scoreData`, and renders through the score atlas. `useDigitalTwin` initializes the adapter. Preserve this event-to-score pipeline.
- AI/player decisions: `ShotSelection.ts`, `SeededRng.ts`, `playerStateMachine.js`, `playerApproach.js`, `playerHelpers.js`, `playerAnimations.js`, `updatePlayers.js`, `src/scene/players.js`, and later `playerFigures.js`. No separate newer committed AI rules engine was found.
- Input discovered from event-handler source, rather than directory guesses: `src/components/DigitalTwin.jsx`, `src/components/ui/RobotDashboard.jsx`, `src/components/ui/ScheduleGrid.jsx`, `src/components/ui/SlidePanel.jsx`, `src/components/ui/robot/DPad.jsx`, `src/controls/orbitControls.js`, `src/controls/spectatorCameraMode.js`, `src/hooks/useFocusTrap.js`. These are UI/robot/camera inputs, not evidence of a full human paddle-control implementation.
- Review supporting integration tests outside `tests/engine`: gameplay behavior, ball/score coupling, physics edge cases, scoreboard behavior, scene/player figures and spectator camera tests. All are retained in the broad content manifests.

## Key branch differences and recommendations

| Lane / audited tip | Evidence and value | Recommendation |
|---|---|---|
| `feat/optimize`, `feat/engine-usapa-2026` — `9d98e3e` (G44) | Fixed-timestep/interpolated animation, benchmark infrastructure; robot angle interpolation and renderer guards; court-side kiosk scoring. Same core engine as every lane. | Best focused starting point for engine work; no branch switch needed. Performance is not benchmark-verified here. |
| `main` / detached treehouse — `959a96b` (G52) | Same full source/test/config content as remote `operation-autopilot/main` tip `90ff6c5a`, despite distinct commits. Compared with optimize: older interpolation/benchmark details and floating billboard behavior. | No engine upgrade. Do not replace optimize’s integration with this snapshot. |
| `facilityOS/checkpoint` — `98d3b28f` (G56) | Older variable-delta animation; lacks optimize’s `SimState` and benchmark files. Robot-camera rendering includes fog save/restore behavior. | Facility reference, not superior rules/physics base; consider camera behavior only as a scoped integration change with tests. |
| Photoreal Blender — `e45f0db3` (G50) | Source/test/config-equivalent to other Blender/dream tips; same engine. Shares older gameplay integration with facility checkpoint, but broad source differs. | Keep as asset source, not engine base. Dirty additions below are separate from this commit. |
| `origin/cursor/visual-critic-drone-7c9e` — `9556b25a` (G55) | Adds FPV capture/benchmark integration, not engine changes. | Optional inspection/capture tooling only. |
| `fm/homebase-players` — `51f2b5c4` (G31) | Merged torso/legs presentation and player scene tests, no new rules or shot selection. | Optional visual cherry-pick, retaining tests and prerequisites. |
| `fm/homebase-hawkeye-trails` — `850b8523` (G49) | Rally sample recording, replay state and score-atlas display integration. | Useful event visualization; inspect complete commit dependencies and scoreboard reset behavior before porting. |
| `fm/homebase-player-figures` — `e9ce5f40` (G85) | Adds RESTING player state, first-frame resting figures, transitions into READY and back after matches; threads figure option through updatePlayers; scene tests. Also inherits camera/replay work. | Strongest discovered player-behavior delta; cherry-pick the specific commit only if persistent figures are wanted. Not a better physics engine. |
| `fm/homebase-facility-scoreboards` — `de6c91c2` (G80) | New facility scoreboard scene/test coverage and inherited presentation changes; distinct spectator updates. | Broader presentation candidate, not a focused engine base. |
| G03, G65, G02, G05 | Scoreboard, court-scoreboard, window-glass and contact-shadow lanes cover additional observed animation/control variants. | Treat as rendering/integration changes, not engine replacements. |

### Candidate cherry-picks (none applied)

- `51f2b5c4d0f373910a2a4af474097deecfacb233`: player mesh polish + scene tests.
- `75e9feed4c55c639d31848d05b68972ce343d62a`: ball/trail/particle appearance + scene tests and mock/setup changes. “Upgrade ball system” does **not** change `PhysicsEngine` or `src/utils/physics.js`.
- `850b8523a1ddc020f05e5d2f15b0ebd413890f12`: Hawkeye replay. Bring the replay module, ball/scoreboard wiring, atlas/test support as a coherent change; do not cherry-pick only an import.
- `f38c85d2b7d657da2b74284853231ae48fc9dc4c`: spectator camera input/toggle, damped follow and utility tests. Optional camera feature, not player movement controls.
- `e9ce5f40c833151fe6793debb50b8efac1530640`: RESTING figures/state lifecycle + tests. Check interaction with serve-readiness, scene reinitialization and court state transitions.
- Existing `10e5517` and `9841268` bridge/bounds fixes are already represented by the common engine tree; do not reapply them as newly discovered upgrades.

All recommendations are source-based candidates, not approved clean cherry-picks. Review complete commit file/test payloads in Git; the saved `evidence/G*-history.txt` and scoped `G*-integration.diff` files are starting points, not full commit patches. Run engine/integration/visual tests before accepting any change.

## Uncommitted work that branch-tip comparison would miss

- **D5 — photoreal worktree live snapshot:** all existing TypeScript engine files still match its committed engine byte-for-byte. Adds `src/engine/aceFacilityOs.js` (facility/session simulation, not a replacement pickleball rules engine), ACE scene integration, and `src/twin-adapter/README.md` (a thin-client policy document, not implemented new control code).
- **More relevant than another engine branch:** untracked `tests/engine/oracle/conformance.golden.test.ts` adds public-CourtEngine scenarios for serve fault, two-bounce and kitchen volley; `tests/engine/properties/kitchen.property.test.ts` adds a fast-check NVZ-volley property. Their 2026 citations are assertions in source, not independently rulebook-verified by this audit. Recover/review the supporting oracle/rulebook docs separately before treating these as compliance evidence.
- **D0 — canonical dirty snapshot:** config-storage source/test edits only among initial relevant changes; no TypeScript engine upgrade.
- Both snapshots copied source/tests/config into new detached audit worktrees without touching the originals. They are not atomic filesystem snapshots and are not commits or cherry-pickable changes. Copied-byte SHA-256 manifests and base identities are in `dirty-snapshots.json`. No tests were executed; these are discovered test assets, not green results.

## GitNexus evidence and limitations

GitNexus version: **1.6.12**. Each indexed group ran `npx --yes gitnexus analyze --index-only --name <unique-alias> --workers 2`, then `status`, domain `query`, `context PhysicsEngine`, `context EngineAdapter`, and `impact`. Queries/contexts target the absolute detached worktree with `-r`, avoiding ambiguous shared basenames. No context-file injection or self-commit was requested.

Every completed primary index below was checked for: successful command exits; status up-to-date; exact expected commit prefix; both class contexts `found`; and covered-file freshness. All committed audit worktrees were read back clean. Machine checks are in `verification.json`, exact argv/exits/logs in `index-results.json` and `dirty-index-results.json`.

The analyzer explicitly reports **truncated execution-flow exploration**. Class contexts also miss some JS-to-TS edges through barrel imports. Therefore low impact or missing callers is not unused code. Supplemental `tickCourtBall`, `selectShot`, `updateBall`, `updatePlayers` and player/camera contexts plus direct source inspection trace the real bridge. An initial supplemental lookup for `updateSpectatorCamera` failed; source discovery corrected it to `updateSpectatorCameraMode`, whose successful log is retained.

| Group | Commit | Covered files | Query processes | Status + contexts |
|---|---|---:|---:|---|
| G44 | `9d98e3e8` | 391 | 5 | verified; [status](evidence/G44-1-status.log) |
| G52 | `959a96b4` | 391 | 5 | verified; [status](evidence/G52-1-status.log) |
| G56 | `98d3b28f` | 386 | 5 | verified; [status](evidence/G56-1-status.log) |
| G50 | `e45f0db3` | 395 | 5 | verified; [status](evidence/G50-1-status.log) |
| G55 | `9556b25a` | 396 | 5 | verified; [status](evidence/G55-1-status.log) |
| G31 | `51f2b5c4` | 401 | 5 | verified; [status](evidence/G31-1-status.log) |
| G85 | `e9ce5f40` | 456 | 5 | verified; [status](evidence/G85-1-status.log) |
| G49 | `850b8523` | 408 | 5 | verified; [status](evidence/G49-1-status.log) |
| G03 | `04000e7d` | 399 | 5 | verified; [status](evidence/G03-1-status.log) |
| G65 | `b26978ee` | 438 | 5 | verified; [status](evidence/G65-1-status.log) |
| G80 | `de6c91c2` | 462 | 5 | verified; [status](evidence/G80-1-status.log) |
| G02 | `0340d0dc` | 429 | 5 | verified; [status](evidence/G02-1-status.log) |
| G05 | `10f16a07` | 419 | 5 | verified; [status](evidence/G05-1-status.log) |
| D0 | `9d98e3e8` | 391 | 5 | verified; [status](evidence/D0-1-status.log) |
| D5 | `e45f0db3` | 409 | 5 | verified; [status](evidence/D5-1-status.log) |

## Complete committed content-group ledger

All refs, full commit IDs, component hashes, blob manifests, exact changed-path lists and group membership are in `inventory.json`. Short refs here omit duplicate remote names for readability; **unindexed means not graph-audited**, regardless of shared engine files.

| Group | Representative | Local branch (or remote-only) | Members | Broad changed paths vs optimize | GitNexus |
|---|---|---|---:|---:|---|
| G01 | `008bd48c` | fm/homebase-path-lights | 1 | 138 | **not indexed** |
| G02 | `0340d0dc` | fm/homebase-window-glass | 1 | 63 | verified |
| G03 | `04000e7d` | fm/homebase-scoreboards | 1 | 21 | verified |
| G04 | `0d17cad5` | fm/homebase-court-lighting | 1 | 89 | **not indexed** |
| G05 | `10f16a07` | fm/homebase-contact-shadows | 1 | 53 | verified |
| G06 | `142b85ab` | fm/homebase-landscaping | 1 | 120 | **not indexed** |
| G07 | `17268fc9` | fm/homebase-court-signage | 1 | 75 | **not indexed** |
| G08 | `17cdd731` | fm/homebase-coolers | 1 | 106 | **not indexed** |
| G09 | `1815ef04` | fm/homebase-planters | 1 | 140 | **not indexed** |
| G10 | `1cf4571e` | fm/homebase-paddle-racks | 1 | 81 | **not indexed** |
| G11 | `1fd32a39` | fm/homebase-ada-curb-ramps | 1 | 170 | **not indexed** |
| G12 | `214b0acc` | fm/homebase-bike-lockers | 1 | 154 | **not indexed** |
| G13 | `219a20c1` | fm/homebase-lost-and-found | 1 | 182 | **not indexed** |
| G14 | `292d6578` | fm/homebase-trash-bins | 1 | 85 | **not indexed** |
| G15 | `2abbad59` | fm/homebase-security-cameras | 1 | 148 | **not indexed** |
| G16 | `2c9734e6` | fm/homebase-ticket-booth | 1 | 152 | **not indexed** |
| G17 | `2d2f5bf2` | fm/homebase-env-ibl | 1 | 48 | **not indexed** |
| G18 | `32ec16c4` | fm/homebase-facility-signage | 1 | 122 | **not indexed** |
| G19 | `33994785` | fm/homebase-umpire-figures | 1 | 102 | **not indexed** |
| G20 | `390f85e7` | fm/homebase-benches | 1 | 132 | **not indexed** |
| G21 | `399e5ece` | fm/homebase-wifi-signs | 1 | 186 | **not indexed** |
| G22 | `39a15e4c` | fm/homebase-plaza-umbrellas | 1 | 166 | **not indexed** |
| G23 | `3e7af65d` | fm/homebase-walkway-benches | 1 | 198 | **not indexed** |
| G24 | `3f6bd126` | fm/homebase-web-gfx | 1 | 10 | **not indexed** |
| G25 | `41d98dfd` | fm/homebase-facility-fountains | 1 | 110 | **not indexed** |
| G26 | `47043af5` | fm/homebase-court-windscreens | 1 | 77 | **not indexed** |
| G27 | `4936804e` | fm/homebase-rideshare-pickup | 1 | 190 | **not indexed** |
| G28 | `4b94c969` | fm/homebase-overhead-banners | 1 | 98 | **not indexed** |
| G29 | `4d842ac1` | fm/homebase-locker-rooms | 1 | 108 | **not indexed** |
| G30 | `4e6e864c` | fm/homebase-stroller-parking | 1 | 184 | **not indexed** |
| G31 | `51f2b5c4` | fm/homebase-players | 1 | 26 | verified |
| G32 | `53a86001` | fm/homebase-walkway-bike-repair | 1 | 204 | **not indexed** |
| G33 | `53c33d04` | fm/homebase-shade-canopies | 1 | 144 | **not indexed** |
| G34 | `56a4bee9` | fm/homebase-ev-chargers | 1 | 180 | **not indexed** |
| G35 | `58e9f89d` | fm/homebase-first-aid-stations | 1 | 176 | **not indexed** |
| G36 | `5f81e603` | fm/homebase-first-aid | 1 | 116 | **not indexed** |
| G37 | `613c9500` | fm/homebase-parking-lot | 1 | 118 | **not indexed** |
| G38 | `671e8a2e` | fm/homebase-water-fountains | 1 | 83 | **not indexed** |
| G39 | `695ff834` | fm/homebase-vending-machines | 1 | 112 | **not indexed** |
| G40 | `6a057e37` | fm/homebase-handrails | 1 | 156 | **not indexed** |
| G41 | `6cefab9e` | fm/homebase-fog | 1 | 57 | **not indexed** |
| G42 | `6e2c9c02` | fm/homebase-ball-carts | 1 | 79 | **not indexed** |
| G43 | `712dd26e` | fm/homebase-walkway-emergency-phones | 1 | 206 | **not indexed** |
| G44 | `9d98e3e8` | feat/engine-usapa-2026, feat/optimize | 2 | 0 | verified |
| G45 | `75e9feed` | fm/homebase-ball | 1 | 30 | **not indexed** |
| G46 | `785c2ecc` | fm/homebase-plaza-vending-machines | 1 | 164 | **not indexed** |
| G47 | `78f535e6` | fm/homebase-fire-hydrants | 1 | 150 | **not indexed** |
| G48 | `7d0ed846` | fm/homebase-flagpoles | 1 | 130 | **not indexed** |
| G49 | `850b8523` | fm/homebase-hawkeye-trails | 1 | 42 | verified |
| G50 | `e45f0db3` | fm/homebase-blender, fm/homebase-blender-daytime, fm/homebase-dream-photoreal, fm/homebase-dream-photoreal-blender | 4 | 33 | verified |
| G51 | `8e241b8e` | fm/homebase-roof-lights | 1 | 59 | **not indexed** |
| G52 | `959a96b4` | main | 2 | 19 | verified |
| G53 | `9361c95a` | fm/homebase-spectator-benches | 1 | 61 | **not indexed** |
| G54 | `9538a39b` | fm/homebase-shuttle-stop | 1 | 192 | **not indexed** |
| G55 | `9556b25a` | refs/remotes/origin/cursor/visual-critic-drone-7c9e | 1 | 26 | verified |
| G56 | `98d3b28f` | facilityOS/checkpoint | 1 | 32 | verified |
| G57 | `9a4864cf` | fm/homebase-jumbotron | 1 | 36 | **not indexed** |
| G58 | `a01acbd5` | fm/homebase-wayfinding-arrows | 1 | 158 | **not indexed** |
| G59 | `a0ca710e` | fm/homebase-bike-racks | 1 | 126 | **not indexed** |
| G60 | `a1e79630` | fm/homebase-kitchen-nets | 1 | 73 | **not indexed** |
| G61 | `aca8428b` | fm/homebase-walkway-trash-receptacles | 1 | 194 | **not indexed** |
| G62 | `ad99a75b` | fm/homebase-dumpsters | 1 | 128 | **not indexed** |
| G63 | `b1631ec4` | fm/homebase-lightmap-bake | 1 | 45 | **not indexed** |
| G64 | `b23d55ef` | fm/homebase-walkway-pet-waste-stations | 1 | 200 | **not indexed** |
| G65 | `b26978ee` | fm/homebase-court-scoreboards | 1 | 73 | verified |
| G66 | `b968ece2` | fm/homebase-bollards | 1 | 140 | **not indexed** |
| G67 | `bb51890f` | fm/homebase-spectators | 1 | 18 | **not indexed** |
| G68 | `bc56e455` | fm/homebase-walkway-bike-racks | 1 | 192 | **not indexed** |
| G69 | `c0c653f8` | fm/homebase-overlays | 1 | 16 | **not indexed** |
| G70 | `c13a5e3c` | fm/homebase-picnic-tables | 1 | 142 | **not indexed** |
| G71 | `c61db266` | fm/homebase-spectator-figures | 1 | 96 | **not indexed** |
| G72 | `c6461375` | fm/homebase-materials | 1 | 24 | **not indexed** |
| G73 | `c6f3a1b0` | fm/homebase-walkway-sunscreen-dispensers | 1 | 210 | **not indexed** |
| G74 | `c8a28697` | fm/homebase-robot-gfx | 1 | 16 | **not indexed** |
| G75 | `cd98d7bb` | fm/homebase-cameras | 1 | 24 | **not indexed** |
| G76 | `ce1af0b7` | fm/homebase-restrooms | 1 | 178 | **not indexed** |
| G77 | `d7d61558` | fm/homebase-walkway-hand-sanitizer-dispensers | 1 | 212 | **not indexed** |
| G78 | `d88a123d` | fm/homebase-god-rays | 1 | 65 | **not indexed** |
| G79 | `da8f82b9` | fm/homebase-court-reflections | 1 | 71 | **not indexed** |
| G80 | `de6c91c2` | fm/homebase-facility-scoreboards | 1 | 100 | verified |
| G81 | `e0b5794a` | fm/homebase-recycling-bins | 1 | 168 | **not indexed** |
| G82 | `e372d378` | fm/homebase-walkways | 1 | 124 | **not indexed** |
| G83 | `e49cd5cc` | fm/homebase-walkway-aed-cabinets | 1 | 214 | **not indexed** |
| G84 | `e5057c44` | fm/homebase-emergency-phones | 1 | 162 | **not indexed** |
| G85 | `e9ce5f40` | fm/homebase-player-figures | 1 | 93 | verified |
| G86 | `e9dc0950` | fm/homebase-ball-machines | 1 | 114 | **not indexed** |
| G87 | `eae75237` | fm/homebase-crosswalk-markings | 1 | 172 | **not indexed** |
| G88 | `eb20a1e3` | fm/homebase-trash-cans | 1 | 134 | **not indexed** |
| G89 | `eb859f99` | fm/homebase-umbrellas | 1 | 104 | **not indexed** |
| G90 | `eee79bc5` | fm/homebase-ssao | 1 | 55 | **not indexed** |
| G91 | `f0454e70` | fm/homebase-drinking-fountains | 1 | 136 | **not indexed** |
| G92 | `f088d58e` | fm/homebase-walkway-phone-charging | 1 | 208 | **not indexed** |
| G93 | `f2984aa5` | fm/homebase-speed-bumps | 1 | 174 | **not indexed** |
| G94 | `f38c85d2` | fm/homebase-spectator-camera | 1 | 69 | **not indexed** |
| G95 | `f8165d96` | fm/homebase-walkway-newspaper-racks | 1 | 202 | **not indexed** |
| G96 | `f897f9c1` | fm/homebase-atm-kiosk | 1 | 188 | **not indexed** |
| G97 | `f97f0b4b` | fm/homebase-walkway-planter-boxes | 1 | 196 | **not indexed** |
| G98 | `f9d6198c` | fm/homebase-info-kiosks | 1 | 146 | **not indexed** |
| G99 | `faa2898f` | fm/homebase-bloom | 1 | 55 | **not indexed** |
| G100 | `ff8c8fb9` | fm/homebase-bottle-fillers | 1 | 160 | **not indexed** |

## Core engine manifest

| File | Lines | Blob |
|---|---:|---|
| `src/engine/Aerodynamics.ts` | 179 | `91a46e6959c51c1bbf75f61722c548ed60e2aeb2` |
| `src/engine/BounceModel.ts` | 124 | `7e0269394b3b62737758f08539786c59a87a428a` |
| `src/engine/CourtEngine.ts` | 548 | `6a6d5f305489ed434fdb62f3fa6a5cf81bdd76b6` |
| `src/engine/EngineAdapter.ts` | 392 | `4e405ddea16a61a73cc3a0781d8b00ea5702ff9b` |
| `src/engine/FaultDetector.ts` | 421 | `0342b4e8bf5c43672727e99392ef51625661f5a9` |
| `src/engine/HeadlessSimulator.ts` | 278 | `90ad5c6b8423e71567d8b012363b255978e1b4b0` |
| `src/engine/MatchStateMachine.ts` | 219 | `4cb385a732f59d8fc5a9417d4a79f0a5162d2c5b` |
| `src/engine/NVZTracker.ts` | 232 | `4c2ee13ae7200c9b6e9a6ce4f9450a2b44fc488b` |
| `src/engine/PhysicsEngine.ts` | 568 | `f35d31d6c5cffb51fb170e78aa5b8f31e29eb3c3` |
| `src/engine/RallyStateMachine.ts` | 201 | `220f791801de7c3c374b2d90ee6c75b06d92870f` |
| `src/engine/ScoreKeeper.ts` | 257 | `d39ace1f66767d543ca6a160ac9de27c0b731e50` |
| `src/engine/SeededRng.ts` | 27 | `ba38496fa8383893106e6ad9d818e0d7e0fe300b` |
| `src/engine/ServeSequence.ts` | 144 | `7a49aab25cb808c4480ffedf7baf3e69268b2aa9` |
| `src/engine/ShotSelection.ts` | 339 | `8e7ad087b7e3d3672456a9c22ab392454c5efa64` |
| `src/engine/TwoBounceRule.ts` | 177 | `60947eb7fd84063bc441cd3d9287c3f77e666ff4` |
| `src/engine/constants.ts` | 102 | `02b3bbb29ba2bdd564d307aede8889df58f07ea9` |
| `src/engine/index.ts` | 86 | `5d79716aa59e7d604e920ce3ff81ddc97e0309e7` |
| `src/engine/scoringOracle.ts` | 106 | `bd9cd6f53f47e3eafc4e0d2a4e016c1a60e4feee` |
| `src/engine/types.ts` | 177 | `5fcb1f1ed5425db468ea5b3e93c0d7ed847c6947` |

## What remains

- Optional: index the 87 explicitly unindexed integration combinations if their asset-hook interactions matter to the next task. No unindexed committed engine-tree variant remains.
- Run tests/benchmarks and visual verification before promoting a presentation branch or accepting any cherry-pick. Resolve the failed remote if fresh operation-autopilot tips are required.
- Review and preserve the dirty oracle/property test assets with their owner; this audit neither committed nor relocated originals.
- Audit detached worktrees and GitNexus indexes are retained for reproducibility under `/workspace/wt/homebase-audit-*`; removing them later is a separate cleanup action. Existing worktree status readbacks are retained in JSON; concurrent parent work may change its own source or add sibling audit reports, so this audit does not attribute every external status delta to itself.
