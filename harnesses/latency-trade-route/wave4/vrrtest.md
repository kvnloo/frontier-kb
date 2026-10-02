# VRRTest — deterministic display workload

Repository: https://github.com/Nixola/VRRTest

VRRTest supports:

- fixed target FPS
- busy-wait pacing
- VSync toggling
- fluctuating framerate
- injected random stutter
- high-contrast per-frame square patterns

## Why use it

It can generate controlled timing disturbances without game simulation noise.

## Experiments

1. fixed FPS inside VRR range;
2. sweep through VRR minimum;
3. sweep through VRR maximum;
4. sinusoidal framerate;
5. random stutter;
6. busy-wait on/off.

Capture DRM first-pixel timing and photodiode output simultaneously.

## Outputs

- requested period
- physical refresh period
- duplicated physical refreshes
- missed application frames
- LFC pattern
- brightness/flicker changes under long VRR front porch
- software timestamp error

This becomes the display-controller test signal for compositor and driver work.
