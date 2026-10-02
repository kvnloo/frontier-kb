# Frameprobe — physical ground truth

Repository: https://github.com/frameprobe/frameprobe

Frameprobe uses an RP2040 to generate a USB HID mouse event and a photodiode to detect the resulting screen brightness transition. Its existing Linux test data already covers X11 vs Wayland, VRR, and DXVK.

## Goal

Use the same physical trigger to calibrate software timestamps from Waves 1-3.

## Matrix

- compositor: Hyprland / gamescope / another compositor baseline where practical
- path: native Wayland / XWayland
- VRR: off / on
- VSync: off / on
- present mode: FIFO / mailbox / immediate where available
- refresh: 60 / 120 / 144 / 240+
- DXVK latency path: baseline / present-timing / low-latency mode
- cursor: hardware / software where relevant

## Sensor placement

Measure at:

- top
- center
- bottom

The vertical delta reveals scanout direction and duration.

Never compare panel modes with a sensor moved between runs.

## Correlation

For each run retain:

- frameprobe raw ADC CSV
- frameprobe computed latency
- gamescope trace
- DRM CRTC sequence/vblank trace
- application present IDs/timestamps where available
- environment receipt

## Main outputs

1. error distribution of each software timestamp vs photon;
2. top-to-bottom scanout duration;
3. VRR effect on scanout-to-photon;
4. whether display timing stays causal during missed frames;
5. whether present-timing improves actual input-to-photon or merely frame pacing.

## First result worth trusting

A software timestamp is a useful proxy only after its error to photon is measured across several refresh/VRR states.
