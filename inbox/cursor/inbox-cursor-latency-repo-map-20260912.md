---
id: inbox-cursor-latency-repo-map-20260912
title: "kvnloo repos that actually touch gfx/input latency (and what to fork next)"
type: inbox
status: draft
created: 2026-09-12
updated: 2026-09-12
node: cursor
harnesses: [cursor]
domains: [cs, physics, ai-ml]
tags: [inbox, github, latency, forks]
confidence: high
---

# Related GitHub (pulled, not vendored)

Scanned all 652 `kvnloo` owner repos (name + description + parent). Pulled READMEs / trees for the latency-relevant ones. Did **not** create new GitHub forks.

## Already owned — keep in sync

| Fork | Parent | vs upstream (2026-09-12) | Why it matters |
|---|---|---|---|
| [FPSWarpDemo](https://github.com/kvnloo/FPSWarpDemo) | NVlabs/FPSWarpDemo | **identical** (frozen 2021-06-10) | The late-warp demo. See [[inbox/cursor/inbox-cursor-frame-warp-fork-20260912]] |
| [PC-Optimization-Hub](https://github.com/kvnloo/PC-Optimization-Hub) | BoringBoredom/PC-Optimization-Hub | **identical** (fork push 2026-08-23; parent last push 2026-06-27) | Best OSS map of the full click-to-photon chain. Reflex / Anti-Lag 2 / VRR / xHCI IMOD / mouse DPI-poll |
| [Hyprland](https://github.com/kvnloo/Hyprland) | hyprwm/Hyprland | **identical** | Wayland compositor; present path + explicit sync interact with NVIDIA latency |
| [open-gpu-kernel-modules](https://github.com/kvnloo/open-gpu-kernel-modules) | NVIDIA/open-gpu-kernel-modules | compare API 404 (branch/SHA skew); still the Linux display/GPU scheduling tree | 615.71.09 is where `VK_NV_low_latency2` on Wayland landed |
| [nvidia-container-toolkit](https://github.com/kvnloo/nvidia-container-toolkit) | NVIDIA/nvidia-container-toolkit | not re-diffed this wave | GPU containers; not click-to-photon |

PC-Optimization-Hub files worth citing (parent tree):

- `README.md` — 12 ms vs 20 ms → 182 ms aiming (NVIDIA); ~1–2 ms dragging JND; 0.3 ms jitter JND
- `content/data collection/nvidia-reflex-end-to-end-system-latency-pipline.png`
- `content/xhci imod/xhci imod.md`
- `content/peripherals/mouse faq.md`

## Same Three.js stack as FPSWarpDemo (application surface)

FPSWarpDemo *is* a Three.js first-person late-warp. These kvnloo trees are the natural place to reuse the RN warp (offscreen target + homography quad), not to re-fork NVIDIA:

| Repo | Notes |
|---|---|
| [kvnloo/cod](https://github.com/kvnloo/cod) | Original browser FPS, code-only assets. Same class of camera as FPSWarpDemo |
| [kvnloo/claude-of-duty-ii](https://github.com/kvnloo/claude-of-duty-ii) | Fork of luckeyfaraday/claude-of-duty; Three.js FPS |
| [kvnloo/GameBlocks](https://github.com/kvnloo/GameBlocks) | Fork of xt4d/GameBlocks; **ahead 14 / behind 0** of parent — local work. Agent-oriented 3D game blocks |
| [kvnloo/three.js](https://github.com/kvnloo/three.js) | Fork of mrdoob/three.js (`dev`) |
| [kvnloo/threejs-game-skills](https://github.com/kvnloo/threejs-game-skills) | Agent skills for playable Three.js games |
| [kvnloo/valorant](https://github.com/kvnloo/valorant) | Empty-ish personal repo; not the Riot tree |

A HITL to port FPSWarpDemo's `latewarp` path into `cod` / GameBlocks would be a living demo; the NVlabs demo itself is frozen.

## NVIDIA / graphics adjacent, not latency-primary

newton (NVIDIA Warp physics — **different "warp"**), SoL-Pi, holohub, GR00T-WholeBodyControl, omniverse-dsx-blueprint, 3d-guided-genai-rtx, vgpu, spark, openshaders, motion-bricks.cpp. Leave them out of this wave.

## Not owned — recommended tracking forks (do not auto-create)

| Upstream | Why |
|---|---|
| [NVIDIA-RTX/Streamline](https://github.com/NVIDIA-RTX/Streamline) | 2.14.1; `sl.reflex`, `kBufferTypeNoWarpMask`, DLSS-G, `VK_NV_low_latency2`. This is the real product SDK |
| [NVIDIA-RTX/REFLEX](https://github.com/NVIDIA-RTX/REFLEX) | Standalone Low Latency SDK + Unity plugin + Vulkan lib; PDF updated 2026-09-01 |
| [NVIDIA-RTX/Streamline_Sample](https://github.com/NVIDIA-RTX/Streamline_Sample) | Reference integration, same cadence as Streamline |
| [NVlabs/FPSci](https://github.com/NVlabs/FPSci) | Native Windows aim-science harness (G3D); 2024-07 |
| [NVlabs/WebFPSci](https://github.com/NVlabs/WebFPSci) | 5 commits FPSWarpDemo lacks, including C2P fix |
| [Floris0106/AsyncTimewarp](https://github.com/Floris0106/AsyncTimewarp) | The actual LTT Unity project (archived). Historical only |
| [viitana/projector](https://github.com/viitana/projector) | Vulkan async-reprojection experiment (ASW-like, not Frame Warp) |
| GameStream / PresentMon / CapFrameX / SpecialK | Measurement + present-path injection; not pulled this wave |

Starred (not forked): NVlabs/FPSWarpDemo — already forked.

## Autoresearch poll URLs (for CoS to add to `data/sources.yaml`)

Cursor does not write `data/sources.yaml`. Candidates:

```yaml
latency:
  fpswarpdemo: https://github.com/NVlabs/FPSWarpDemo
  webfpsci: https://github.com/NVlabs/WebFPSci
  fpsci: https://github.com/NVlabs/FPSci
  streamline: https://github.com/NVIDIA-RTX/Streamline
  reflex_sdk: https://github.com/NVIDIA-RTX/REFLEX
  reflex_product: https://www.nvidia.com/en-us/geforce/technologies/reflex/
  pc_opt_hub: https://github.com/BoringBoredom/PC-Optimization-Hub
  kim2020: https://doi.org/10.1145/3406187
  nvidia_linux_615: https://www.nvidia.com/en-us/drivers/details/278450/
```

## Next action

No further git on the owned forks this wave. CoS: (1) promote SOTA to literature, (2) decide whether to fork Streamline/REFLEX, (3) optional living late-warp in `cod`.

## Links

- [[inbox/cursor/inbox-cursor-frame-warp-wave-20260912]]
- [[inbox/cursor/inbox-cursor-frame-warp-fork-20260912]]
- [[inbox/cursor/inbox-cursor-gfx-input-latency-sota-20260912]]
- https://github.com/kvnloo/FPSWarpDemo
- https://github.com/kvnloo/PC-Optimization-Hub
