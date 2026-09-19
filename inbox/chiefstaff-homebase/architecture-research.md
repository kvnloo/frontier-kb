---
id: homebase-audit-architecture-research
title: "Homebase audit: architecture-research"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
---

Source snapshot; relative evidence links resolve in /workspace/wt/homebase-engine-2026/docs/engine-audit/.

# Multi-sport playable engine: architecture and starting-point research

## Decision summary

**Recommendation, not an observation about the existing code:** prototype Unreal as the actual gameplay runtime and dedicated authoritative server—not merely a viewer for a permanently authoritative TypeScript simulation. Use Blender for authoring. Start with a thin game-owned C++ domain layer and sport plugins; use Unreal's gameplay, animation, networking and profiling facilities where they fit. Use Lyra selectively for production framework patterns and the Game Animation Sample selectively for locomotion. Neither is an open-source sports engine.

Keep Godot as the serious permissively licensed alternative, especially if browser delivery, a smaller native runtime, or unrestricted engine redistribution becomes a hard requirement. Evaluate O3DE when full open-source engine control and an organization capable of owning substantial C++ engine integration outweigh turnkey workflow priorities. These are suitability judgments, not measured performance rankings.

Do not buy or fork an entire engine to obtain a tennis rules implementation. Do not impose a generic ECS on a handful of athletes. Do not mistake attractive facility rendering, rigid-body integration, or a research environment for a shippable sports game.

### Scope and evidence boundaries

- Research retrieved **2026-09-14 UTC**. GitHub metadata, latest default-branch commits, latest-release endpoints, README files and license contents were read live. Dates below are observed commit dates, not inferred from stars or repository `updated_at`. A recent commit establishes activity, not test quality, staffing, release support or fitness for this product.
- Existing TypeScript pickleball rules/physics adapters and Three.js facility presentation are **delegation context**, not code findings from this research. Their correctness and migration value require the independent local audit. No existing runtime benchmarks were performed here.
- Requested sports: tennis, badminton, football and basketball. **Football is treated provisionally as association football** in the examples; confirm whether association, American, futsal or multiple variants are required. Other facility sports are not enumerated. No facility inventory is invented.
- No engine was built or benchmarked, and no sample asset bundle was downloaded. Unreal sample maintenance evidence is official documentation, not authenticated sample source inspection. The direct Epic legal pages were blocked by a security check; an accessible Epic Unreal EULA hosted by Steam was read instead. Package-specific sample/Fab terms still require verification at acquisition.[31]

## 1. Runtime and sample comparison

| Starting point | Verified public evidence | Recommended use and limits |
|---|---|---|
| **Unreal + Lyra** | Epic describes a modular core/plugins architecture, multiplayer/cross-play, a customized Gameplay Ability System, and example shooter/party modes. Epic says its plugins are updated with UE development.[15] UE source access requires Epic/GitHub account linkage and agreement to the EULA.[32] | Preferred high-fidelity runtime candidate. Create a game-owned derivative/sample baseline or adopt selected patterns: experience selection, input, player lifecycle, teams, UI, feature plugins and multiplayer setup. Do not preserve shooter assumptions merely because Lyra implements them. A Lyra derivative creates upgrade/merge work; a smaller clean project borrowing patterns may be cheaper. |
| **Game Animation Sample** | Officially a motion-capture/motion-matching example for responsive traversal, locomotion, ledge scaling and vaulting, with extensible character retargeting and migratable assets/systems.[16] | Animation reference and selective content migration, not the base game architecture and not a sports contact library. No retrieved evidence establishes that its full animation stack is turnkey multiplayer-safe. Build and test sport-specific hits, catches, dribbles and paired contacts. |
| **Godot** | MIT engine; commit `2f698aa5fe`, 2026-09-13; latest-release response `4.7.2-stable`, 2026-08-18. Official license page describes commercial use and the requirement to retain license notices.[1][30] Official docs support glTF and direct Blender import via an export process.[21] | Best first OSS engine alternative. Use the engine as a pinned dependency, own the game project, extend through supported native extension mechanisms before forking the engine. Budget original sports animation tooling and networking integration. Do not assume its visual ceiling or frame rate from engine branding. |
| **O3DE** | Root license permits Apache-2.0 or, at the user's option, MIT; third-party terms remain separate. Commit `80f4714164`, 2026-09-08; release `2605.0`, 2026-05-27.[2] Networking documentation describes AzNetworking and a Multiplayer Gem with entity replication, local prediction, input handlers and reliable/unreliable RPCs.[22] | Viable OSS C++ runtime, but choose only after proving build, asset iteration, animation and multiplayer workflows with the actual team. Prefer game Gems over an engine fork. Existing features are not proof of a cheaper sports production path than Unreal/Godot. |

**License classification:** Unreal, Lyra and the Game Animation Sample belong in the **Epic-licensed/source-available, not OSS** bucket. Access to source is not an OSI-style permission grant. Unreal's EULA calls the technology proprietary and regulates distribution and incompatible licenses.[31][32] Treat the exact downloaded sample/content terms as a release gate: do not label all sample assets MIT, assume every animation can be redistributed independently, or assume every Fab item uses identical terms. Commercial royalty/seat obligations depend on the agreement and use case; obtain a current legal review rather than basing the business plan on a headline percentage.

## 2. Maintained OSS building blocks—not a compulsory stack

Use **one coherent runtime**. The following are alternatives or narrowly scoped dependencies, not a shopping list to integrate simultaneously. Unless stated otherwise, live API results reported repositories as not archived.

| Project | License evidence; observed activity | Fit; dependency / fork / reference decision |
|---|---|---|
| **Jolt Physics** | MIT. Commit `6f5f7749e0`, 2026-09-12; release `v5.6.0`, 2026-07-11. README documents CCD and deterministic simulation with explicit limitations; it names shipped game usage.[3] | Strong standalone CPU rigid-body dependency candidate. Pin and wrap it; do not fork by default. A sports ball/shuttle still needs calibrated custom forces and contact laws. Do not inject a second physics authority into Unreal simply to use Jolt; first test the engine's native path. |
| **NVIDIA PhysX** | BSD-3-Clause. Commit `4f2103c3a9`, 2026-08-28. Latest release endpoint returned `ovphysx-0.5.11`, 2026-08-28—not a claim that this is the appropriate standalone SDK package.[4] | Credible alternative rigid-body SDK, particularly when already supplied by a chosen runtime. Verify the exact SDK/component, supported platforms and dependency notices. Not an automatic improvement over Unreal's physics. |
| **EnTT** | MIT. Commit `85c6bba014`, 2026-07-22; release `v4.0.0`, 2026-07-23.[5] | Optional lightweight C++ ECS/registry dependency for a measured need or standalone headless domain. Not a game engine, networking solution, rules framework or mandatory architecture. |
| **Flecs** | License file explicitly MIT, including contributor notices, despite API SPDX `NOASSERTION`. Commit `9e874bca2c`, 2026-09-13; release `v4.1.6`, 2026-06-29.[6] | Optional ECS tooling/query/scheduling candidate. Choose it *instead of* EnTT if its workflow wins a spike. Avoid a duplicate ECS-to-Actor identity/state layer without a demonstrated reason. |
| **GameNetworkingSockets** | BSD-3-Clause. Commit `a424b7db64`, 2026-08-26; release `v1.6.0`, 2026-06-03. README documents reliable/unreliable messaging, fragmentation and encryption.[7] | Strong standalone transport dependency; it is not gameplay replication, reconciliation, matchmaking, anti-cheat or a replay system. Verify which Steam services require separate integration/access rather than assuming the OSS library includes hosted services. In Unreal prefer native networking first. |
| **Yojimbo** | BSD-3-Clause. Commit `272153a10f`, 2026-09-14; release `v1.13.5`, same date. README scopes it to client/server games in C++.[8] | Alternative transport/message layer to evaluate for a standalone C++ server; not an extra transport to stack onto GameNetworkingSockets. Product still owns authority, snapshots and gameplay prediction. |
| **BehaviorTree.CPP** | MIT. Commit `9b63b50598`, 2026-08-31; release `4.9.0`, 2026-02-11.[9] | Optional inspectable decision framework for standalone AI. Not a sports coach, tactical policy or trained model. Use Unreal-native decision tools first in an Unreal game unless portability has concrete value. |

These licenses describe the inspected root files, not every bundled asset, optional plugin, SDK or transitive dependency. Maintain an SBOM and notices per pinned build. A fork is justified by a reproducible blocking defect or necessary platform feature, with a maintainer and upstream plan; otherwise prefer pinned upstream dependencies and small adapters.

## 3. Actual sports repositories: useful, but not ready-made multi-sport production foundations

| Repository | Verified status / license | Honest scope and disposition |
|---|---|---|
| **Google Research Football** | **Archived**. Commit `3d9e754720`, 2025-06-17; latest release `v2.10.2`, 2022-01-25. Root Apache-2.0; the inspected `third_party/gfootball_engine/LICENSE` uses the Unlicense/public-domain dedication text.[10] | README explicitly identifies an RL research environment based on Gameplay Football. Useful reference or isolated research fork for observations/actions, scenarios and multi-agent evaluation. Not a maintained commercial football foundation or modern production animation stack. Audit bundled fonts/assets separately. |
| **RoboCup Soccer Simulator / rcssserver** | Not archived, but latest default-branch commit `ce870013f2` and latest release `rcssserver-19.0.0` both 2024-03-25. LGPL-3.0 root license.[26] | Research/education multi-agent soccer simulator, not a high-fidelity athlete game. Reference for agent protocols, reproducible competitions and tactical experiments. Do not describe current maintenance as proven simply because it is unarchived. |
| **MinimumTennis** | MIT; commit `af086427c9`, 2025-04-14; not archived.[36] | Real playable simplified tennis, with deliberately primitive character presentation for experiments and a documented subset/variant of tennis scoring. Useful reference or bounded prototype fork after build verification—not evidence of a current, complete production tennis stack. |
| **VR-Tennis** | MIT; **archived**; commit `b650132226`, 2016-02-10.[35] | README calls this a first Unity/HTC Vive VR game test. Historical interaction reference only. |
| **Unreal tennis prototypes** | `utkualkan4112/TennisGame`: commit `6c29ae81a5`, 2024-03-30; `Fletman/UE4-Tennis`: `1dae38759e`, 2019-03-08. GitHub license endpoints did not supply a license for either.[28][29] | First is a smartphone-IMU racket prototype; second describes a basic UE4 tennis game. Publicly visible code is **not permission to reuse**. Not OSS recommendations; request explicit licensing before copying. |
| **CoachAI+ badminton** | `KuangDW/CoachAI-Plus`, commit `4fd05934f1`, 2025-01-28; no license supplied by the inspected endpoint.[33] | Research environment for player styles, strategy optimization and evaluation, with player movement/rule constraints. Interesting behavioral research reference, not a cleared OSS gameplay foundation or verified real-time 3D shuttle/contact model. |
| **react-native-basketball** | MIT; commit `6b59d6c30a`, 2017-07-25; not archived.[34] | README describes a Facebook basketball mini-game clone and React Native 0.45.1. Small hoop-shot interaction reference, not maintained team basketball, defense, fouls or possession simulation. |
| **Blobby Volley 2** | GPL-2.0 root license; commit `c28c5fa878`, 2026-07-06; not archived; latest-release API supplied no release.[27] | Actual multiplayer ball game with documented dedicated server; useful sports networking/game-loop reference. Its stylized head-to-head gameplay is not athlete biomechanics or regulation volleyball. Do **not** copy GPL implementation into an Unreal product. Volleyball here is a research comparison, not an asserted facility sport. |
| **RLGym** | Apache-2.0; commit `2fc8d43566`, 2026-05-16; no latest release returned.[11] | RL API/ecosystem for Rocket League and related simulation components. Useful training-interface reference, **not** an OSS replacement for the proprietary game or human football. Inspect simulator and visualization packages separately. |
| **Stunt Rally 3** | GPL-3.0; commit `fe3ecd73ff`, 2026-04-18; release `3.3`, 2024-12-29.[13] | Maintained playable racing comparison for content and simulation tooling, not one of the requested facility sports. Reference only for the proposed Unreal path; no GPL code transplant. |

Searches covered tennis, badminton and basketball as well as football. The inspected results did **not establish a maintained, permissively licensed, production-quality game covering the requested human sports**. This is a bounded search conclusion, not a claim that none exists. Search results containing historical commercial source dumps/decompilations were not treated as licensed starting points.

The accessible Unreal EULA explicitly lists GPL, LGPL (except merely dynamically linking a shared library), and CC BY-SA as examples of incompatible licenses under its stated conditions.[31] Reference means studying behavior, architecture and interfaces, then writing original code—not copying implementation and relabeling it. Review copyleft integration and asset rights with counsel.

## 4. Proposed production architecture

The following is a design recommendation, not a claim that it already exists in Homebase.

```text
Blender source + licensed motion capture + facility metadata
            -> validated asset import/cook -> runtime data assets

Common game runtime
  session / identity / input / camera / UI / accessibility / audio
  authoritative match clock / command validation / snapshots / replay
  athlete intent / locomotion / animation-contact bridge / telemetry
       |
       +-- Tennis: rules + ball flight/bounce + racket contact + tactics
       +-- Badminton: rules + shuttle flight/orientation + racket contact
       +-- Football variant: rules + ball/foot/body contact + team tactics
       +-- Basketball: rules + possession/dribble/hoop contact + team tactics
       +-- Further sport modules only after requirements are confirmed

Engine services: rendering, collision queries, base dynamics, animation,
network transport, asset streaming, tooling and profiler
```

### Common contracts, sport-specific behavior

Define a small sport interface around match initialization, legal commands, fixed-step evolution, observation production, event adjudication and snapshot/restore. Share identity, clocks and event envelopes, **not one universal ball equation or giant rule switch**. Rule code should be testable without renderer/editor dependencies; visual actors consume state instead of deciding who scored.

- **Tennis:** require calibrated flight, spin and surface response; racket contact must consider racket pose/velocity and contact location. Separate service, rally, scoring and competition-format rules.
- **Badminton:** do not reskin the tennis sphere. Plan for strong speed-dependent drag, shuttle orientation/stability and a distinct rebound/contact model. Determine the necessary fidelity through measured trajectories and player perception.
- **Association football (provisional):** support foot/body contact, rolling/sliding, contested possession and off-ball formations. Offside/fouls/restarts depend on event timing and rule version, not merely collision callbacks.
- **Basketball:** reconcile controlled possession and dribble intent with free flight, hand contact, rim/backboard interactions and contested catches. Traveling, double dribble, fouls, clocks and scoring need temporal state, not a boolean `hasBall`.

These are engineering requirements to validate; no force coefficients, regulation dimensions or legal rule text are asserted here. Select the governing body, competition variant and effective rule edition before encoding them.

Use an explicit ordered event pipeline: input intents -> athlete/control update -> force integration and swept contacts -> timestamped contact events -> sport adjudication -> committed match events -> presentation. Define tie-breaking for events in the same tick, including fractional time of impact. Do not let unordered engine callbacks decide line calls or possession.

### Authority, ticks and replay

A fixed simulation step separates physics behavior from variable rendering; unbounded catch-up work can produce the “spiral of death.”[24] Unreal's networked physics documentation describes predictive interpolation and resimulation, including cached per-physics-tick history and CPU/memory costs.[17] Its Character Movement documentation details client saved moves, server checks and corrections.[18]

**Recommended protocol:**

1. Dedicated server owns canonical positions, contact outcomes, possession, clock, score and rules. Client messages carry sequence number, intended simulation tick and bounded input intent—not trusted score or contact results. Validate rate, action legality and reachability.
2. Choose a fixed match/physics cadence through measurement. Treat 60/120 Hz as experiment candidates, not benchmarks or promises. Expensive contact sweeps/substeps may run within a match tick; snapshots can be less frequent. Specify units and phase ordering explicitly and never advance authoritative time from render `deltaTime`.
3. Predict local movement and selected ball interactions. Buffer inputs, acknowledge processed sequences and restore/replay unacknowledged inputs when corrected. Interpolate remote athletes with a bounded delay. Separate cosmetic smoothing from authoritative collision state.
4. Test native engine prediction/resimulation before building a parallel rollback framework. Coordinate character and ball histories; predicting one while treating the other as unrelated replicated motion can break contact feel. Motion matching/root motion must not silently create a second movement authority.
5. Define fairness for late strikes and contested catches: bounded historical validation, approved rewind window, reject/adjust rules and feedback. Do not simply rewind the whole world for each client or trust client-reported racket hits. Measure the trade-off between visible contact and server truth under asymmetric latency.
6. Persist match seed, tick cadence, commands, committed events, periodic authoritative keyframes, physics build/config hash, rule-pack ID, schema version and content versions. Input-only replay is acceptable only after same-build/platform determinism is demonstrated. Keep snapshot-assisted replay for drift recovery and debugging.
7. Quantize network state deliberately; define event IDs so rollback/retransmit cannot duplicate scores, audio, achievements or analytics. Bound history memory and resimulation work. Record corrections and divergence, not just disconnects.

A fixed tick is **not proof of cross-platform bitwise determinism**. Floating-point math, solver ordering, parallel execution and engine upgrades must be tested. Jolt itself directs users to limitations on its deterministic simulation claims.[3] Do not promise deterministic lockstep across arbitrary Unreal/Chaos builds.

### Animation, contact and adaptive AI

Motion matching solves selection of appropriate motion from a database; the retrieved sample focuses on traversal, not tennis strokes or basketball handoffs.[16] The hard production work is a contact-aware animation set and controller:

- Author/obtain acceleration, braking, lateral movement, pivots, reaches, strokes, kicks, dribbles, catches, jumps, landings and recoveries appropriate to each sport. Budget left/right handedness, equipment and athlete proportion variation.
- Label clips with phase, contact point/time, feasible velocity, stance and recovery metadata. Blend/warp only within defined limits; excessive warping hides missing motion coverage and breaks biomechanics.
- Predict interception, choose a feasible action, align through motion/IK, then validate a swept racket/foot/hand contact against the authoritative ball trajectory. Animation contact markers are proposals/windows, not unconditional hit events. Never let an arbitrary late animation notify grant an impossible hit.
- Paired collisions, tackles/screens and contested catches need explicit conflict resolution, animation fallbacks and interruption rules. Full ragdoll simulation is not a replacement for playable athlete control.
- Separate strategy (positioning/shot/pass choice), trajectory planning, movement and contact execution. Start with inspectable scripted/state-machine/utility policies, plus sport-specific trajectory solvers. Add learned policies only with reproducible evaluation and dataset/model rights.
- “Adaptive” difficulty should adjust reaction latency, anticipation quality, tactical diversity and execution error within declared constraints. Do not secretly give bots impossible contact reach, knowledge of hidden client input or different physical laws. Adapt at stable boundaries and log the policy/config version.

### Data assets and rule versioning

Unreal's Asset Manager provides primary/secondary asset organization, discovery and load management.[23] Recommended cross-runtime source schemas can compile into Unreal Primary Data Assets; do not require JSON parsing in the per-tick hot path.

| Schema | Minimum contract |
|---|---|
| `SportDefinition` | stable sport/variant ID; schema version; physics model ID; rule-pack ID; supported player/team arrangements; equipment and animation capability requirements |
| `RulePack` | governing body; competition edition/effective date; authoritative source URL; semantic version; score/restart/foul/clock configuration; adjudicator implementation hash; test-fixture version |
| `EquipmentProfile` | units; mass/geometry/inertia; collision proxy; material/contact response; force-model parameters and valid ranges; calibration provenance |
| `AthleteProfile` | rig version; proportions; handedness; movement/contact capability bounds; stamina/error settings; animation-set compatibility |
| `ContactAction` | intent; compatible sport/equipment; phase windows; target contact transform; reachable set; impulse/force constraints; IK/warp limits; interruption and network policy |
| `FacilitySportPlacement` | verified facility/space ID; surveyed coordinate frame and units; sport variant; boundary/line geometry; surface profile; clearance/obstacle zones; evidence/provenance and verification status |
| `MatchManifest` | engine/simulation build; content and schema hashes; selected rule pack; seed; tick cadence; roster; facility configuration; AI policy version |

Never silently overwrite a rule pack used by saved matches. Freeze its version/hash for match duration and replay. Separate official competitive variants from house rules, drills and accessibility modes. Migrations should explicitly preserve or reject old replays, not reinterpret them under the newest scorer.

## 5. Blender-to-runtime pipeline

Unreal documents FBX import for meshes, animations, materials and textures; the animation sample documents skeletal import, IK rigs and retargeting.[20][16] Godot documents Blender/glTF import workflows.[21]

**Recommended authoring contract:** retain `.blend` source, exported intermediates and provenance; pin Blender/exporter/runtime importer versions. Validate scale/units, axes, applied transforms, pivots, normals, UVs, material slots, skeleton/rest pose, socket conventions and collision proxies. Use semantic court/hoop/net anchors, not hand-entered offsets spread across code. Test an exported calibration cube and a skeletal contact clip inside the target runtime before building a large asset library.

Separate visual facility meshes from certified gameplay surfaces/line geometry and collision. Set budgets for texture memory, material slots, mesh detail, skinning, cloth and animation databases. Create LOD/collision variants appropriate to target hardware. Track source licenses for motion capture, textures, fonts, logos, sound and scans separately from code. High-end rendering cannot repair missing contact animations or inaccurate playable dimensions.

## 6. Validation roadmap and decision gates

This is a proposed roadmap with measurable gates—not completed validation or fabricated benchmark results.

1. **Requirements and baseline:** confirm target platforms, local/online modes, player counts, controller/VR requirements, realistic vs arcade contact, facility inventory and football variant. Reproduce existing TypeScript behavior and capture fixtures before deciding what to port. Do not equate preserving rules knowledge with preserving its language/runtime forever.
2. **Runtime bake-off:** build the same small court, athlete and ball interaction in Unreal and Godot; include O3DE only if OSS engine ownership is a serious decision criterion. Test packaged runtime plus headless server, asset reimport, debugging and automated tests. Record developer effort as well as frame/memory/network cost.
3. **One playable vertical slice:** tennis or current pickleball can expose racket interception, footwork, timing, flight, bounce, scoring, serve transitions and camera. Include a human and a competent bot, full point-to-next-point flow, a packaged build and a repeatable replay. No camera-only demo qualifies.
4. **Prove architectural differences:** implement badminton flight/contact and basketball possession/hoop contact spikes before claiming “multi-sport.” Follow with team-sport positioning and contested contacts. A second spherical-ball reskin does not validate the abstraction.
5. **Multiplayer gate:** two real clients plus dedicated server; then intended maximum players. Sweep measured latency, jitter, loss, reordering and asymmetric links. Record contact disagreement rate, correction distance/frequency, input-to-response latency, replay divergence, server tick tails and resimulation cost. Test reconnects, malicious inputs and disconnect during scoring.
6. **Sport correctness/calibration:** versioned golden rule scenarios; property tests for legal scoring/state transitions; boundary/line-contact cases; high-speed swept-collision tests; trajectory/bounce comparisons with documented measurements; frame-rate independence; same-build replay hashes with snapshot fallback. Expert/player review validates feel and tactics separately from mathematical consistency.
7. **Performance and content gate:** profile target hardware in packaged builds, including worst-case cameras and facility density. Unreal Insights is the official tracing/profiling suite, with timing, memory and networking analysis facilities.[19] Track CPU game/physics/animation work, GPU time, memory residency, streaming stalls, network bytes, server tick tail latency and catch-up backlog. Establish budgets from platform targets and test scenes, not invented universal numbers.
8. **Scale and release:** headless CI regression suites, long-running bot matches, content import validation, replay compatibility, crash reproduction bundles, accessibility and fairness reviews, dependency notices and package-specific license sign-off. Add each further sport only with its own rule/physics/animation fixtures and verified facility placement.

### Fork / dependency / reference policy

- **Fork/derive the game project:** own the product's C++/Blueprint code and sport modules. A Lyra-derived game is reasonable if its lifecycle/features demonstrably reduce work; retain upstream provenance and isolate customizations.
- **Use engines and libraries as pinned dependencies:** prefer project/plugin/extension boundaries. An engine fork adds permanent build, merge, security and platform-support obligations.
- **Use samples as selective references/content:** Game Animation Sample for locomotion/retargeting; Lyra for gameplay framework; sports research projects for observations, scenarios and evaluation ideas.
- **Do not import incompatible or unlicensed code:** GPL sports games are architectural/behavioral references for an Unreal path, and absent licenses require permission. Root OSS licenses do not establish ownership of every bundled asset.
- **Migration:** port only independently verified rules/algorithms and fixtures from the current TypeScript system when native runtime authority is selected. Keep TypeScript where it earns its place—web facility tools, configuration, services or test utilities—not as an ideological constraint. Avoid two concurrently authoritative match implementations.

## Open decisions / unresolved evidence

Target devices, facility inventory, sport variants, multiplayer scale and intended fidelity remain unspecified. Repository presence and release recency do not establish integration cost; no candidate was compiled or exercised in this research. Unreal source and sample bundle versions were not inspected behind account access. Direct Epic legal endpoints remained blocked; the accessible Steam-hosted agreement supports the proprietary/incompatible-license discussion, but current acquisition-specific terms must be checked before adoption.[31]

## Sources

[1] https://github.com/godotengine/godot — godotengine/godot
[2] https://github.com/o3de/o3de — o3de/o3de
[3] https://github.com/jrouwe/JoltPhysics — jrouwe/JoltPhysics
[4] https://github.com/NVIDIA-Omniverse/PhysX — NVIDIA-Omniverse/PhysX
[5] https://github.com/skypjack/entt — skypjack/entt
[6] https://github.com/SanderMertens/flecs — SanderMertens/flecs
[7] https://github.com/ValveSoftware/GameNetworkingSockets — ValveSoftware/GameNetworkingSockets
[8] https://github.com/mas-bandwidth/yojimbo — mas-bandwidth/yojimbo
[9] https://github.com/BehaviorTree/BehaviorTree.CPP — BehaviorTree/BehaviorTree.CPP
[10] https://github.com/google-research/football — google-research/football
[11] https://github.com/rlgym/rlgym — rlgym/rlgym
[13] https://github.com/stuntrally/stuntrally3 — stuntrally/stuntrally3
[15] https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine — Lyra
[16] https://dev.epicgames.com/documentation/en-us/unreal-engine/game-animation-sample-project-in-unreal-engine — Game Animation Sample
[17] https://dev.epicgames.com/documentation/en-us/unreal-engine/networked-physics-overview — Networked physics
[18] https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine — Network movement
[19] https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine — Unreal Insights
[20] https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-content-pipeline — FBX pipeline
[21] https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html — Godot Blender import
[22] https://docs.o3de.org/docs/user-guide/networking — O3DE multiplayer
[23] https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine — Unreal asset management
[24] https://gafferongames.com/post/fix_your_timestep — Fixed timestep
[26] https://github.com/rcsoccersim/rcssserver — rcsoccersim/rcssserver
[27] https://github.com/danielknobe/blobbyvolley2 — danielknobe/blobbyvolley2
[28] https://github.com/utkualkan4112/TennisGame — utkualkan4112/TennisGame
[29] https://github.com/Fletman/UE4-Tennis — Fletman/UE4-Tennis
[30] https://godotengine.org/license — Godot license
[31] https://store.steampowered.com/eula/3855380_eula_0 — Epic license on Steam
[32] https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine — Epic downloading source
[33] https://github.com/KuangDW/CoachAI-Plus — KuangDW/CoachAI-Plus
[34] https://github.com/FaridSafi/react-native-basketball — FaridSafi/react-native-basketball
[35] https://github.com/me4502/VR-Tennis — me4502/VR-Tennis
[36] https://github.com/open-video-game-library/MinimumTennis — open-video-game-library/MinimumTennis
