---
id: inbox-cursor-gfx-input-latency-sota-20260912
title: "SOTA graphics and input latency, 2026-09: Reflex 1 shipping, Frame Warp still vapor, chain is end-to-end"
type: inbox
status: draft
created: 2026-09-12
updated: 2026-09-12
node: cursor
harnesses: [cursor]
domains: [physics, cs, ai-ml, neuroscience]
tags: [inbox, latency, reflex, frame-warp, dlss, vulkan, oled, sota]
confidence: high
---

# SOTA: click-to-photon, not FPS

## Claim (one sentence)

The competitive latency stack in 2026 is **Reflex Low Latency (or Anti-Lag 2 / XeLL) + just-in-time present + high-Hz OLED**, with **post-render late warp / Frame Warp still unreleased** as a shipping game feature; 8 kHz mice and extra generated frames are second-order unless the rest of the chain is already short.

## Pipeline (what actually costs milliseconds)

End-to-end click-to-photon ≈

`mouse MCU + debounce` → `USB/2.4 GHz` → `xHCI interrupt moderation` → `OS + game sim` → `CPU render-submit` → **GPU render queue** → `render` → `flip/present` → `scanout` → `panel GtG/MPRT`.

Vendor "low latency" modes attack the **render queue** (just-in-time submit via `slReflexSleep` / NvAPI sleep). Frame Warp attacks **after render**, sampling the latest camera and warping before scan-out. Async reprojection (LTT / VR ASW / SteamVR motion smoothing) instead **inserts extra frames at refresh rate**. Do not collapse these three.

Human-performance floor (NVIDIA esports group, FPSci):

- Spjut et al. 2019, SIGGRAPH Asia briefs, doi:[10.1145/3355088.3365170](https://doi.org/10.1145/3355088.3365170): **30 ms** click-to-photon beats raising refresh above 60 Hz for targeting.
- Spjut, Boudaoud, Kim 2020/2021 ([blog](https://developer.nvidia.com/blog/aiming-faster-in-games-with-low-computer-system-latency/), [case study](https://research.nvidia.com/publication/2021-05_case-study-first-person-aiming-low-latency-esports)): 12 ms vs 20 ms → median aiming completion **1.348 s vs 1.530 s** (Δ 182 ms, p=0.001). Trend continues toward 0.
- Kim et al. HPG 2020, doi:[10.1145/3406187](https://doi.org/10.1145/3406187): +80 ms added latency; rotation-naive warp recovered **81%** of the aiming penalty, rotation-oracle **89%**, translation+rotation oracle **94%**. Guard-band holes were visible to every subject and **did not** kill the aiming gain. Source: FPSci.
- Boudaoud et al. SIGGRAPH 2021 ETech: the [FPSWarpDemo](https://nvlabs.github.io/FPSWarpDemo/) you forked.

## Layer SOTA (2026-09-12)

### 1. Engine queue: shipping

| IHV | Mode | What it is | Availability |
|---|---|---|---|
| NVIDIA | Reflex Low Latency / Boost | `slReflexSleep` + markers; collapse GPU queue; Boost keeps clocks up in CPU-bound | Hundreds of games; GeForce 900+; driver 456.38+ |
| AMD | Anti-Lag 2 (also branded toward FSR Latency Reduction 2.0) | Same idea, SDK | Thin game list (CS2 / Dota 2 / a few others); Anti-Lag 1 is driver-wide queue=1 |
| Intel | XeLL | Same idea; required companion to XeSS FG | Uncommon; Optiscaler can inject |

Standalone SDK: [NVIDIA-RTX/REFLEX](https://github.com/NVIDIA-RTX/REFLEX) (v1.8 2025-02-06; integration PDF updated **2026-09-01**). README still only lists Low Latency + frame limiter + PCL stats — **no Frame Warp API**.

Preferred integration: [NVIDIA-RTX/Streamline](https://github.com/NVIDIA-RTX/Streamline) **2.14.1** (2026-09-08):

- Vulkan Reflex via **`VK_NV_low_latency2`**, NvAPI v1 fallback; pre-Turing Vulkan Reflex removed.
- DLSS Dynamic Multi Frame Generation + VSync documented; FG-off + VSync previously leaked frames into the DXGI flip queue (fixed 2.12).
- Preferred pace: `slReflexSleep`, not `GetFrameLatencyWaitableObject`, when `sl.dlss_g` is loaded.
- Compatibility matrix in `docs/ProgrammingGuideReflex.md` §9: VSync On + VRR Off + FG Off → **no** Reflex latency reduction.

Linux (2026-09-09): NVIDIA driver **615.71.09** adds `VK_NV_low_latency` revision 2 so Proton can enable Reflex in Vulkan-native titles using `NvLowLatencyVk.dll`, and fixes `VK_NV_low_latency2` on `VK_KHR_wayland_surface` / `VK_KHR_display`. kvnloo already forks [open-gpu-kernel-modules](https://github.com/kvnloo/open-gpu-kernel-modules).

### 2. Late warp / Frame Warp: announced, not shipping

NVIDIA Reflex 2 (CES 2025): Frame Warp samples latest mouse/controller, warps the just-rendered frame immediately before present, inpaints disocclusions. Marketed numbers (NVIDIA, not independently replicated in a shipping build):

- THE FINALS, RTX 5070, 4K max + GI: **56 → 27 (Reflex) → 14 ms** (Frame Warp). Headline "up to 75%".
- VALORANT, RTX 5090, 800+ FPS CPU-bound: **< 3 ms** PC latency.

As of this capture, [nvidia.com/geforce/technologies/reflex](https://www.nvidia.com/en-us/geforce/technologies/reflex/) still labels Frame Warp **"coming soon"**. THE FINALS / VALORANT were named at announce; neither has a public toggle. Developer portal asks studios to register for integration notification. Test-build leftovers reportedly appeared in ARC Raiders / THE FINALS; PureDark assembled an unofficial demo (2025-10) on RTX 20+ — NVIDIA did not ship it.

Public Streamline **headers** today:

- `sl::kBufferTypeNoWarpMask = 54` — "Mask for pixels to skip warping" (gun/arms/HUD).
- No `bReflexWarpAvailable` / `useReflexMatrices` in current `sl_dlss_g.h` (checked v2.4 through 2.14.1 public headers). Older DLSS-G guides (v2.9–2.10 era) *documented* those fields and pointed at a `ProgrammingGuideReflex2.md` that is **404 on every public tag**. Treat Frame Warp as **driver/NGX-side**, not a complete public SDK.

This is **not** async reprojection. Extra interpolated frames (DLSS FG / MFG, FSR FG, XeSS FG, Smooth Motion) **add** latency unless Reflex/XeLL is on. Frame Warp updates the *real* frame; FG invents frames in between.

Closest published inpainting cousin: ExtraNet (Fu et al., SIGGRAPH Asia 2021, doi:[10.1145/3478513.3480531](https://doi.org/10.1145/3478513.3480531)) — extrapolated-frame shading + hole mark from G-buffer; ~8 ms @ 720p. Reflex 2's "predictive rendering" is described in similar language (camera + color + depth from prior frames). Do not claim ExtraNet **is** Frame Warp; the product paper is not public.

### 3. Peripheral + bus

From [PC-Optimization-Hub](https://github.com/BoringBoredom/PC-Optimization-Hub) (kvnloo fork identical to upstream 2026-08-23):

- Higher DPI + polling reduces motion-to-photon until the sensor actually emits a packet every poll (MouseTester interval plot).
- 8 kHz theoretical floor is **0.125 ms** poll / **~0.44 ms** average USB vs 1 kHz. Igor's Lab: debounce and frame wait dominate; 1 kHz with 0 ms debounce can beat 8 kHz with 1 ms debounce. Do not buy 8 kHz until the rest of the chain is < a frame.
- Disable xHCI Interrupt Moderation (`content/xhci imod/`).
- 2.4 GHz mice: ~0.5–2 ms extra vs wired in TPU reviews; RGB on the MCU steals cycles.

### 4. Display

SID 2025: first 27"/31.5" **480 Hz OLED** with DFR gate driver, MPRT **1.7 ms** in game mode (doi:[10.1002/sdtp.18085](https://doi.org/10.1002/sdtp.18085)). Metrology (2025): OLED 10–90% can be **82–324 µs** depending on whether you measure one scan line or the whole addressing window — line-scan time scales with refresh; 60 Hz often still clocks as 120 Hz. Panel GtG is no longer the 5–15 ms TN/VA problem; **scanout + OS + queue** are.

VRR/VSync: smoothness vs latency. Reflex + VSync-on without VRR does not reduce latency (Streamline matrix). Cap FPS with Reflex limiter (`frameLimitUs` / `minimumIntervalUs`) rather than a random in-game cap.

### 5. Linux compositor caveat

gamescope + NVIDIA explicit sync (`linux_drm_syncobj`) has a long-running mouse-motion stall ([ValveSoftware/gamescope#1626](https://github.com/ValveSoftware/gamescope/issues/1626)). Workarounds: `ENABLE_GAMESCOPE_WSI=1`, disable `VK_KHR_present_wait`, or `drm_debug_disable_explicit_sync`. Driver 615's Wayland low-latency2 fix does **not** automatically fix gamescope. kvnloo Hyprland fork is identical to `hyprwm/Hyprland`.

### 6. Measurement (only metric that matters)

- NVIDIA LDAT / G-SYNC Reflex Analyzer (click-to-photon, compatible mice).
- FrameView, PresentMon, CapFrameX: PC latency + pacing. Reflex/Anti-Lag 2 can **hurt 1% lows / pacing** while helping average latency (FPS Review 2026-08) — always plot both.
- FPSci / FPSWarpDemo `showC2P` overlay for controlled studies.
- Software PCL markers (`slPCLSetMarker` / `PCLSTATS_PCL_LATENCY_PING`) are vendor-agnostic in Streamline.

## Fact vs interpretation

- **Fact:** Queue-control low-latency modes are the deployed SOTA and are required companions to frame generation on NVIDIA/Intel.
- **Fact:** Independent human-subject evidence for *late warp helping aim* is the 2020 HPG study (up to 94% of an 80 ms penalty). NVIDIA's 75% / 14 ms / <3 ms Frame Warp numbers are vendor demos from 2025, not a 2026 shipping-game measurement.
- **Interpretation:** The interesting open problem is **inpainting + no-warp HUD at <1 ms**, not another reprojection shader. FPSWarpDemo is RN. Product Frame Warp is RN + ExtraNet-class fill. Async 240 Hz from 30 FPS (LTT) is still unimplemented on the desktop outside VR compositors.

## Next action

Promote to `literature/` with `sources:` pointing at the DOIs and Streamline 2.14.1 changelog. Permanent claims:

- Late warp recovers most of an 80 ms aiming penalty even without hole fill (Kim 2020).
- Sub-20 ms still moves completion time (Spjut 2021).
- Frame Warp is not a 2026 shipping dependency.

## Links

- https://www.nvidia.com/en-us/geforce/news/reflex-2-even-lower-latency-gameplay-with-frame-warp/
- https://www.nvidia.com/en-us/geforce/technologies/reflex/
- https://developer.nvidia.com/performance-rendering-tools/reflex
- https://github.com/NVIDIA-RTX/Streamline
- https://github.com/NVIDIA-RTX/REFLEX
- https://research.nvidia.com/sites/default/files/pubs/2020-07_Post-Render-Warp-with/HPG_2020_Latewarp_AuthorVersion_0.pdf
- https://casual-effects.com/research/Kim2020Latency/index.html
- [[inbox/cursor/inbox-cursor-frame-warp-fork-20260912]]
- [[inbox/cursor/inbox-cursor-latency-repo-map-20260912]]
