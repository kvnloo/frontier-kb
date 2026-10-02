# NVIDIA open kernel modules — VRR / vblank correlation

Useful current issues include:

- open-gpu-kernel-modules #913: VRR low-FPS signal loss
- #1289 / #1371: display/KMS lockups around blank/wake and flip handling

The latency lane should avoid conflating these reliability bugs with normal frame-pacing behavior, but their traces expose useful KMS boundaries.

## Goal

On a stable non-destructive workload, correlate:

- compositor VRR state
- NVIDIA DRM page-flip/vblank events
- CRTC sequence timestamp
- present timing
- photon timestamp

## Matrix

- VRR off/on
- inside VRR range
- near minimum VRR
- below minimum VRR
- near maximum VRR
- fixed refresh

Avoid repeated DPMS stress while doing latency experiments.

## Metrics

- first-pixel timestamp interval
- pageflip -> first-pixel relation
- frame repeat / LFC behavior
- present-to-photon error
- low-FPS transition behavior
- GPU clock / display clock state where observable

## Important

A low-FPS VRR path may intentionally repeat frames or use LFC. Model that explicitly rather than labeling every repeated physical refresh as a dropped application frame.
