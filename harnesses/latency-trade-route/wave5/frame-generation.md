# Frame generation — visual smoothness vs information age

Current NVIDIA Streamline documentation makes the key systems tradeoff explicit:

- Reflex/PCL exposes stage markers from input/simulation through GPU/display;
- high FG multipliers can increase latency when generated frames are produced faster than the display can present, backing up the frame queue;
- current Streamline supports Vulkan Reflex through `VK_NV_low_latency2`.

OptiScaler is useful as an experimental adapter because it can route multiple frame-generation technologies in supported games.

## Question

When does higher displayed FPS improve perception while the underlying game-state information becomes older?

## Matrix

Use a deterministic offline game/sample:

- FG off
- 2x
- higher multipliers where supported
- Reflex off/on/on+boost
- VSync off/on
- VRR off/on
- 60 / 120 / 144 / 240 Hz where available

Avoid anti-cheat/networked titles.

## Capture

For real rendered frame `R` and generated frame `G`:

```text
latest_input_used
simulation_start
render_submit
render_complete
FG_start
FG_complete
present
DRM_first_pixel
photon
```

Calculate:

- rendered-frame information age
- generated-frame information age
- queue depth
- fraction of photons belonging to generated frames
- motion smoothness / displayed cadence

## Human task

Pair with:

- target-tracking error
- moving-detail discrimination
- choice-response task

Do not use FPS as the primary outcome.

## Key failure mode

If FG raises displayed FPS while input-to-photon age increases, report both. That may still be a valid visual tradeoff, but it is not a latency reduction.
