---
id: inbox-cursor-frame-warp-wave-20260912
title: "Frame warp / Reflex latency wave: fork found, upstream already identical, SOTA ingested"
type: inbox
status: draft
created: 2026-09-12
updated: 2026-09-12
node: cursor
harnesses: [cursor]
domains: [physics, cs, ai-ml]
tags: [inbox, latency, reflex, frame-warp, nvidia, sota]
confidence: high
---

# Frame warp / input-latency wave (2026-09-12)

## Context

Scanned `kvnloo` (652 owner repos). The LTT-adjacent fork is **[kvnloo/FPSWarpDemo](https://github.com/kvnloo/FPSWarpDemo)** ← [NVlabs/FPSWarpDemo](https://github.com/NVlabs/FPSWarpDemo) (SIGGRAPH 2021 ETech late-warp demo on Web FPSci). It is **not** a fork of Comrade Stinger's Unity AsyncTimewarp; it is the NVIDIA research demo that productized into Reflex 2 Frame Warp.

Upstream sync: `NVlabs:main...kvnloo:main` is **identical** (ahead 0 / behind 0). Last commit on both: `86026f23` 2021-06-10. No git write was required.

Related kvnloo forks already at upstream: [PC-Optimization-Hub](https://github.com/kvnloo/PC-Optimization-Hub) (input-lag handbook), [Hyprland](https://github.com/kvnloo/Hyprland). See [[inbox/cursor/inbox-cursor-latency-repo-map-20260912]].

SOTA (2026-09-12): Reflex Low Latency + `VK_NV_low_latency2` is shipping; **Reflex 2 Frame Warp is still "coming soon"** (~20 months after CES 2025). Full stack: [[inbox/cursor/inbox-cursor-gfx-input-latency-sota-20260912]]. Fork internals: [[inbox/cursor/inbox-cursor-frame-warp-fork-20260912]].

## Fact vs interpretation

- **Fact:** FPSWarpDemo implements rotation-only post-render warp (HPG 2020 "Rotation-Naive"): render to an offscreen target, then a full-screen quad with `P * R_recent^-1 * R_old * P^-1`. No hole fill, no depth, no translation.
- **Fact:** NVIDIA's marketed Frame Warp is the same late-sample-then-warp idea plus inpainting, claimed 56→27→14 ms on THE FINALS and <3 ms in VALORANT. Public product page still says "coming soon" as of this capture.
- **Interpretation:** LTT's 2022 video ([IvqrlgKuowE](https://www.youtube.com/watch?v=IvqrlgKuowE)) demonstrated *asynchronous* reprojection (display-rate extra frames, VR ASW). Reflex 2 is *synchronous* late warp (one warp per rendered frame, just before present). Same family, different timing model.

## Next action

CoS promote:

1. Literature notes from the SOTA capture (Kim 2020, Spjut 2019/2021, Streamline 2.14.1, Reflex 2 status).
2. Optional HITL: cherry-pick NVlabs/WebFPSci 2021-10 → 2024-11 (5 commits; C2P draw fix) into `kvnloo/FPSWarpDemo` without losing the experiment-mode UI.
3. Optional HITL: fork `NVIDIA-RTX/Streamline` + `NVIDIA-RTX/REFLEX` for SDK tracking (user does not own them).
4. Atlas stub under physics/cs once literature is promoted. Cursor does not write `literature/`, `permanent/`, or `atlas/`.

## Links

- [[inbox/cursor/inbox-cursor-frame-warp-fork-20260912]]
- [[inbox/cursor/inbox-cursor-gfx-input-latency-sota-20260912]]
- [[inbox/cursor/inbox-cursor-latency-repo-map-20260912]]
- https://github.com/kvnloo/FPSWarpDemo
- https://nvlabs.github.io/FPSWarpDemo/
- https://research.nvidia.com/publication/2021-08_gaming-warp-speed-improving-aiming-late-warp
