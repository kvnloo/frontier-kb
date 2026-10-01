# E2E latency trade route — wave 2

Status: **triaged and staged, not yet executed**

The purpose of this wave is to prepare experiments that maximize information gain before opening or promoting anything upstream.

## Queue

1. **wgpu** — cross-vendor acquire/present regression reproduction
   - https://github.com/gfx-rs/wgpu/issues/9559
   - https://github.com/gfx-rs/wgpu/issues/9937
   - https://github.com/gfx-rs/wgpu/issues/9856
2. **vkd3d-proton** — frame-latency depth vs starvation / present timing
3. **ALVR** — CachyOS/NVIDIA >1 s latency sawtooth decomposition
   - https://github.com/alvr-org/ALVR/issues/3393
4. **Mesa WSI** — validate `VK_EXT_present_timing` clock / pacing behavior across Wayland and X11/XWayland
5. **Monado** — motion-to-photon pacer margin / missed-frame controller
6. **LatencyFleX** — re-test old VSync limitation now that Linux present timing exists

## Shared outcome metric

Do not optimize FPS in isolation.

Primary quantity:

```text
information age at display =
display/photon timestamp - latest input/tracking state incorporated into frame
```

Secondary quantities:

- deadline miss rate
- frame-time p50 / p95 / p99 / p99.9
- wake -> run delay
- CPU queue age
- GPU queue age
- present request -> actual present
- actual present -> display/photon estimate
- queue depth
- GPU clock / utilization feedback

## Experiment discipline

- freeze exact commit, driver, kernel, compositor, refresh, VRR and power mode;
- warm up before measurement;
- prefer A/B/B/A or randomized order;
- record raw samples, not only averages;
- treat p99/p99.9 regressions as first-class;
- separate a pacing win from a latency win;
- do not infer root cause until the first divergent timestamp is located.

## Promotion gate

None of these experiments are intended for upstream promotion yet.

Promote only after a packet contains:

1. exact reproducer;
2. raw trace / CSV;
3. environment receipt;
4. repeated result;
5. smallest causal hypothesis consistent with the trace.
