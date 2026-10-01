# wgpu — acquire / present latency regressions

## Live surfaces

- `#9559`: Vulkan fence wait added to fix NVIDIA FIFO stutter caused a reported AMD/Windows acquire-latency regression.
- `#9937`: wgpu 29 -> 30 reproducer reports higher wall time around presentation.
- `#9856`: public API cannot yet pair a submitted frame with actual display presentation.

## Why this is useful

The current reports are on other platforms/hardware. A NVIDIA/Linux result is useful even when the answer is "does not reproduce" because it separates generic Vulkan synchronization cost from Windows/DWM or vendor-specific behavior.

## Experiment A — #9559 cross-vendor reproduction

Compare the code path immediately before and after the fence-wait change.

Matrix:

- revision: pre-wait / wait
- present mode: Immediate / FIFO / FIFO-relaxed where available
- `desired_maximum_frame_latency`: 1 / 2 / 3
- compositor: native Wayland and XWayland if the reproducer permits
- VRR: off / on

Measure per frame:

- `Surface::get_current_texture` wall time
- encode+submit wall time
- present-call wall time
- whole loop
- p50 / p95 / p99 / p99.9
- GPU utilization / clocks

Do not assume NVIDIA should be faster: #9559 exists because a fix for an NVIDIA FIFO problem had a very different AMD/Immediate effect.

## Experiment B — #9937 A29/B30/B30/A29

Use the issue's minimal clear-only reproducer unchanged first.

Required order:

```text
wgpu 29
wgpu 30
wgpu 30
wgpu 29
```

Then repeat with randomized order.

If the present-call delta reproduces, use `perf` + Vulkan validation/timestamps to determine whether the time moved into:

- queue submission;
- fence/semaphore management;
- swapchain image ownership;
- actual WSI call;
- Rust-side bookkeeping.

## Experiment C — frame-specific feedback feasibility

Do not design an API yet.

Instead record what each Linux backend can already supply:

- present ID
- requested target time
- actual present time
- dropped/not-presented status
- clock domain
- correlation to app monotonic clock

The goal is an evidence table for the future #9856 API discussion.

## Gate

No code change until either #9559 or #9937 reproduces locally, or the feedback inventory finds an already-available backend signal wgpu is discarding.
