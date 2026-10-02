# OSLTT — display response and system latency cross-check

Repository: https://github.com/OSRTT/OSLTT

OSLTT is open hardware + firmware + desktop software intended as an open-source alternative to tools such as LDAT. It can perform monitor and end-to-end latency measurements.

## Why pair it with frameprobe

Frameprobe is ideal for our custom timestamp correlation.

OSLTT is useful for:

- panel response characterization;
- standardized monitor transition measurements;
- independent hardware/software cross-check;
- future experiments around strobing and perceived transition timing.

## First experiment

On one display mode:

1. characterize black->white and gray->gray transition distribution;
2. measure overshoot/settling separately from first detectable transition;
3. run input-to-photon measurement;
4. compare with frameprobe on the same screen location and brightness state.

## Biological/display follow-up

Only after the timing rig is calibrated:

- compare full-persistence vs backlight-strobe modes;
- quantify latency cost of strobe phase;
- quantify motion clarity vs photon delay;
- test brightness / threshold dependence;
- distinguish first visible transition from full pixel settling.

This is the bridge to the perceptual side of the project.

## Important

A "faster first transition" and "clearer perceived motion" are different objectives. Keep both metrics.
