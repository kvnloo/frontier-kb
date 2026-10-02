# EyeTrackVR — camera backpressure and gaze freshness

Current live issue: https://github.com/EyeTrackVR/EyeTrackVR/issues/155

The issue reports camera framerate degrading over hours while logs emit:

`Capture queue backpressure ...`

Current main already contains several latency-oriented mechanisms:

- the capture loop drains sources to avoid stale hardware buffering;
- output queues drop the oldest frame when full;
- captured frames carry a `time.perf_counter()` timestamp;
- `EyeProcessor` computes tracking output latency from capture timestamp to tracking completion;
- GUI preview emission is throttled independently from tracking.

That makes this a very good freshness experiment rather than a generic FPS bug.

## Experiment A — long-run age drift

Run 2-4 hour soaks with fixed camera/input conditions.

Sample every second:

- camera FPS
- tracking output FPS
- tracking output latency
- capture queue size
- process CPU/RSS
- camera source type
- tracking model
- configured max tracking Hz

Question:

Does reported FPS degrade because capture slows, tracking slows, or queue age grows?

## Experiment B — queue policy

Replay a deterministic recorded eye video through:

1. current drop-oldest policy;
2. an offline simulated FIFO policy;
3. latest-frame-only policy.

Do not alter upstream code initially.

For every processed sample calculate:

```text
capture_to_tracking_ms
frame_number_age
frames_skipped
tracking_output_rate
```

The correct low-latency policy may intentionally skip more frames.

## Experiment C — model-size frontier

Current 2026 releases expose multiple NEXT models, including Lite variants.

Sweep model variants and report jointly:

- tracking accuracy on the same recorded sequence
- inference latency
- output FPS
- CPU/GPU utilization
- gaze age

Do not call the fastest model better unless gaze error remains acceptable.

## Experiment D — gaze-to-photon

Once an OpenXR/foveation consumer exists, propagate the capture timestamp through the output path.

Target receipt:

```text
camera_capture
tracking_done
OSC/API_send
consumer_receive
fovea_center_applied
render_submit
photon
```

Then calculate true gaze age at photon.

## Hardware safety

If physical EyeTrackVR IR hardware is used, follow the project's documented IR-emitter safety guidance; do not improvise higher-power/focused emitters for latency testing.

## Promotion

None until long-run traces identify the first timestamp whose age drifts.
