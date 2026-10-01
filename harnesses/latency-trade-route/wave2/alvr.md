# ALVR — decompose CachyOS/NVIDIA latency sawtooth

## Live surface

https://github.com/alvr-org/ALVR/issues/3393

The report describes CachyOS/Linux sessions where ALVR latency ramps from near zero to >1 s and logs repeatedly warn that prediction latency is being clamped. The reporter reproduced it across multiple NVIDIA driver generations, so a simple "615 driver regression" explanation is already weakened.

## Goal

Find the first stage whose queue age grows monotonically.

ALVR's motion-to-photon path is roughly:

```text
tracking poll
 -> tracking transport
 -> SteamVR/game
 -> compose
 -> encode
 -> network
 -> decode
 -> client compositor/reprojection
 -> runtime submit
 -> vsync/display
```

## First-pass matrix

Keep game workload trivial.

- transport: wired / Wi-Fi if hardware allows
- codec: H.264 / HEVC; AV1 only on supported hardware
- server frame pacing: off / on
- max buffering frames: minimum / default / +1
- target refresh: 72 / 90 / 120 where headset supports it
- compositor extras: disable OVR Advanced Settings and other injected drivers

## Capture

At minimum record time series for:

- game render
- server compositor
- encode
- network
- decode
- client compositor
- total latency
- prediction value
- streamer FPS
- dropped frames / packet loss
- encoder queue depth if observable

Use 5-10 minutes so a sawtooth period is visible, but keep all settings fixed during a run.

## Classification

If only encode grows:
- encoder backpressure.

If encode is flat and network grows:
- transport/buffering.

If all transport stages are flat but prediction grows:
- clock/prediction bookkeeping.

If client compositor grows:
- decode/display pacing.

If total resets sharply after reaching a threshold:
- search for a bounded accumulator, wrap/reset, or resynchronization event.

## Cross-check

Repeat one known-bad run with WiVRn or another runtime only to localize the fault domain. Do not treat a different runtime being smooth as proof ALVR is wrong; it merely narrows shared vs ALVR-specific layers.

## Gate

No upstream comment until the first increasing queue is identified.
