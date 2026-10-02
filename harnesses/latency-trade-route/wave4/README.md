# E2E latency trade route — wave 4

Status: **triaged and staged, not executed**

Wave 4 calibrates the final display path:

```text
app present
 -> compositor
 -> DRM/KMS commit
 -> vblank / first-pixel-out
 -> panel scanout
 -> pixel transition
 -> photon sensor
```

## Core question

Which software timestamp best predicts the physical photon event?

Linux DRM defines its CRTC sequence/vblank timestamp around **the first pixel leaving the display engine for the display**. That is useful, but it is not yet the photon timestamp.

## Lanes

1. Frameprobe — physical mouse-to-photon ground truth
2. OSLTT — monitor response / system-latency cross-check
3. Linux DRM — CRTC sequence and vblank timestamp sampler
4. Hyprland/Aquamarine — VRR + direct-scanout + cursor transition timing
5. NVIDIA open kernel modules — VRR/vblank/pageflip state correlation
6. DXVK low-latency — externally validate `VK_EXT_present_timing` pacing
7. VRRTest — deterministic fixed/fluctuating/stutter display workload

## Shared decomposition

For frame `i`:

```text
t_input
t_app
t_present_request
t_compositor_feedback
t_drm_first_pixel
t_photon_top
t_photon_middle
t_photon_bottom
```

Derived:

```text
software_age      = t_drm_first_pixel - t_input
scanout_to_photon = t_photon - t_drm_first_pixel
total_age         = t_photon - t_input
```

Do not assume `actual_present`, DRM vblank, or a GPU fence equals the visible photon.

## Promotion

None. This wave exists to build a calibration layer for every previous experiment.
