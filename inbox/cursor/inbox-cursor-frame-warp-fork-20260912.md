---
id: inbox-cursor-frame-warp-fork-20260912
title: "kvnloo/FPSWarpDemo is the LTT-lineage late-warp fork; already identical to NVlabs"
type: inbox
status: draft
created: 2026-09-12
updated: 2026-09-12
node: cursor
harnesses: [cursor]
domains: [physics, cs]
tags: [inbox, fpswarpdemo, late-warp, fpsci, nvidia]
confidence: high
---

# The fork: NVIDIA late warp, not Stinger's Unity demo

## Context

LTT ([I'm Embarrassed I Didn't Think of This..](https://www.youtube.com/watch?v=IvqrlgKuowE), 2022-12) covered **desktop async reprojection**: Comrade Stinger's Unity demo (mirrored at [Floris0106/AsyncTimewarp](https://github.com/Floris0106/AsyncTimewarp), archived). `kvnloo` does **not** fork AsyncTimewarp.

What `kvnloo` *does* have, starred and forked:

| Repo | Parent | Role |
|---|---|---|
| [kvnloo/FPSWarpDemo](https://github.com/kvnloo/FPSWarpDemo) | [NVlabs/FPSWarpDemo](https://github.com/NVlabs/FPSWarpDemo) | SIGGRAPH 2021 ETech "Gaming at Warp Speed" browser demo. Hosted: https://nvlabs.github.io/FPSWarpDemo/ |
| [kvnloo/PC-Optimization-Hub](https://github.com/kvnloo/PC-Optimization-Hub) | [BoringBoredom/PC-Optimization-Hub](https://github.com/BoringBoredom/PC-Optimization-Hub) | End-to-end input-lag handbook (mouse → USB → engine → present → panel) |

Paper for the demo: Boudaoud, Knowles, Kim, Spjut, *Gaming at Warp Speed: Improving Aiming with Late Warp*, SIGGRAPH 2021 ETech, doi:[10.1145/3450550.3465347](https://doi.org/10.1145/3450550.3465347). Method paper: Kim et al., HPG 2020, doi:[10.1145/3406187](https://doi.org/10.1145/3406187).

## Sync with upstream (done)

```
gh api repos/kvnloo/FPSWarpDemo/compare/NVlabs:main...kvnloo:main
# ahead_by: 0, behind_by: 0, status: identical
```

Last shared commit: `86026f23` (2021-06-10) "Merge branch 'main' of https://github.com/NVlabs/WebFPSci into main". NVlabs/FPSWarpDemo itself is frozen. **No merge/push on the fork.**

Sibling [NVlabs/WebFPSci](https://github.com/NVlabs/WebFPSci) *did* move. Five commits after the shared ancestor, not present on FPSWarpDemo:

| Date | SHA | Message |
|---|---|---|
| 2021-10-01 | `c1f8165` | negative wrap case for camera azimuth |
| 2023-10-18 | `a5ebb8f` | miss particle config/controls |
| 2023-10-25 | `d775010` | miss-particle copy-paste fix |
| 2023-12-05 | `aabe83a` | `css/main.css` + instructions table |
| 2024-11-06 | `0464cbf` | quick fix for `drawc2p` (click-to-photon overlay) |

Late-warp math in `js/fps.js` is **the same** on both trees. FPSWarpDemo adds experiment-mode UI (`T` / `0` / `80` / `80W` conditions, ~80 ms delay, results banner). Blind-merging WebFPSci would clobber that (~430-line `fps.js` diff). Cherry-pick the C2P fix only if anyone still measures with the overlay.

Native lab: [NVlabs/FPSci](https://github.com/NVlabs/FPSci) last push 2024-07-01. Not forked. WebFPSci last push 2024-11-06. Not forked.

## What the demo actually warps

From `js/fps.js` (fork tree, `latewarp` path):

1. `RawInputState` queues mouse/keyboard by `frameDelay` frames (simulated pipeline delay).
2. Game camera consumes the delayed queue; `rawInputState.cameraRotation` is the **undelayed** pose.
3. When `latewarp`: `renderer.setRenderTarget(renderedImage)` then `renderer.render(scene, camera)`.
4. Homography on a full-screen quad:

```
recentCameraToWorld = R(rawInputState.cameraRotation)
recentWorldToCamera = inverse(recentCameraToWorld)
oldWorldToCamera = camera.matrixWorld with translation zeroed
warpTransform = P * recentWorldToCamera * oldWorldToCamera * P^-1
```

5. Present `warpScene` through an orthographic camera. Fragment shader is a plain `texture(uScene, texCoord)` — **no inpaint, no depth, no motion vectors**. Edge holes stay holes (HPG 2020 RN). Reticle is parented to `warpCamera` so the crosshair is not double-warped.

Conditions: ground truth (0 ms) → ~80 ms delay → ~80 ms delay + late warp. That is the HPG 2020 protocol in a browser.

## LTT vs this fork vs Reflex 2

| | LTT / Stinger AsyncTimewarp | FPSWarpDemo / HPG 2020 | Reflex 2 Frame Warp (marketed) |
|---|---|---|---|
| Timing | Async: extra frames at display Hz even if game is 30 FPS | Sync: warp the just-rendered frame | Sync: warp just before scan-out |
| Hole fill | Stretch edges (optional) | None (RN) | "latency-optimized predictive rendering" using camera + color + depth from prior frames |
| Translation | Optional in the Unity demo | Rotation only | Camera (mouse/controller); HUD/weapon via no-warp mask |
| Status | 2022 demo | Frozen 2021 OSS | Announced CES 2025; still "coming soon" 2026-09 |

## Next action

Leave the fork as a clean upstream mirror. If we want a living research copy: new branch on `kvnloo/FPSWarpDemo` that cherry-picks WebFPSci `0464cbf` and documents the Reflex 2 lineage in a `RESEARCH.md` (do not rewrite NVIDIA README). Cursor did not push to that repo.

## Links

- https://github.com/kvnloo/FPSWarpDemo
- https://github.com/NVlabs/FPSWarpDemo
- https://github.com/NVlabs/WebFPSci
- https://github.com/NVlabs/FPSci
- https://github.com/Floris0106/AsyncTimewarp
- https://www.youtube.com/watch?v=IvqrlgKuowE
- https://www.youtube.com/watch?v=VvFyOFacljg
- https://www.youtube.com/watch?v=f8piCZz0p-Y
- [[inbox/cursor/inbox-cursor-gfx-input-latency-sota-20260912]]
