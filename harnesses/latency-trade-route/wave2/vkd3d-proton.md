# vkd3d-proton — swapchain latency depth vs GPU starvation

## Current seam

vkd3d-proton's current swapchain uses present-wait / present-timing support and exposes `VKD3D_SWAPCHAIN_LATENCY_FRAMES`.

The project documents why it returned to a default internal depth of 3: forcing 2 frames caused enough vblank-aligned CPU delay in some games to make the GPU appear idle, lower clocks, and create a feedback loop.

That is exactly the class of system-level interaction this trade route should study.

## Hypothesis

There is no globally optimal queue depth.

The best depth is a function of:

- CPU simulation variance
- GPU service-time variance
- refresh period
- VRR
- power-management response
- presentation timing precision

A tighter queue can lower median information age while worsening p99 latency if it repeatedly starves the GPU.

## Matrix

For one deterministic DX12 workload:

- `VKD3D_SWAPCHAIN_LATENCY_FRAMES=1,2,3,4`
- VRR off / on
- fixed refresh at at least two refresh rates
- `VKD3D_CONFIG=no_staggered_submit` off / on where relevant
- GPU power policy fixed vs normal policy

## Capture

Per frame:

- CPU begin
- first queue submit
- GPU begin/end
- present enqueue
- present wait completion
- actual present if available
- GPU utilization
- graphics/memory clocks
- frame latency
- missed deadline

Also capture the time derivative of GPU clocks around each starvation event.

## Analysis

Look for the causal sequence:

```text
tight frame-latency gate
 -> CPU delayed by present completion
 -> GPU queue drains
 -> clocks fall
 -> next GPU service time rises
 -> deadline miss
 -> queue/latency expands
```

If that sequence exists, queue depth should be treated as a controller parameter rather than a constant.

## Future follow-up

If data supports it, prototype an offline adaptive policy first. Do not modify vkd3d-proton until replaying the captured workload predicts a better depth reliably.
