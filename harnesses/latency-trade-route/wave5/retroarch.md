# RetroArch — temporal rendering laboratory

RetroArch combines several latency/perception controls in one active OSS stack:

- Run-Ahead
- Preemptive Frames
- frame delay
- GPU hard sync
- swapchain image count
- black-frame insertion (BFI)
- adjustable dark-frame count

Current config/documentation exposes these controls directly. Current issue #18922 also documents severe BFI/netplay flicker interaction, so **exclude netplay entirely** from these experiments.

## Experiment A — freshness controls

Use one deterministic 60 Hz core/content pair.

Compare:

1. baseline
2. frame delay sweep
3. Run-Ahead 1/2/... only up to the content's actual internal lag
4. Preemptive Frames
5. combinations only after each feature is characterized alone

Measure:

- input -> photon t10/t50/t90
- frame-time tails
- emulation CPU
- missed/deadline frames
- correctness / audio artifacts

Goal: identify how much emulated-state latency can be removed before compute variance causes deadline misses.

## Experiment B — BFI / persistence

At compatible refresh rates compare:

- no BFI
- 120 Hz: 1 lit / 1 dark
- higher-Hz dark-frame patterns supported by current RetroArch

Measure physically:

- duty cycle
- photon t10/t50/t90
- brightness
- transition duration
- top/center/bottom scanout

Measure perceptually with the PsychoPy motion task:

- motion-identification accuracy
- threshold speed
- response time

## Experiment C — frame delay × BFI

Question:

Can later emulation/input sampling offset the latency cost introduced by waiting for a preferred strobe/light window?

Map the Pareto surface:

```text
input freshness
vs
motion clarity
vs
miss rate
vs
brightness
```

No upstream change until this surface is measured.
