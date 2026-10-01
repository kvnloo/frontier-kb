# Monado — motion-to-photon pacer controller experiment

## Why Monado

Monado already exposes the conceptual model we want:

```text
wake_up -> begin -> submit -> present -> display/photon
```

Its compositor pacer stores predicted wake, desired present, actual present, predicted display, compositor render time, present margin and present-to-display offset.

## Hypothesis

The pacer's safety margin should be evaluated as a control system:

- too large => old tracking/input information at display;
- too small => missed frame;
- a miss => controller backs off;
- stable success => controller should cautiously reclaim freshness.

## Experiment

Replay or run a stable compositor workload while sweeping:

- initial margin
- missed-frame backoff
- non-miss adjustment
- compositor-time cap
- artificial CPU jitter
- artificial GPU jitter

For every frame calculate:

```text
wake_error       = actual_wake - predicted_wake
present_error    = actual_present - desired_present
display_age      = predicted_display - latest_tracking_sample
margin_used      = desired_present - compositor_done
```

## Stress patterns

Use deterministic injected disturbances:

1. one 2 ms CPU spike every 120 frames;
2. one 4 ms GPU spike every 240 frames;
3. burst of 5 elevated frames;
4. sinusoidal service-time drift;
5. random heavy-tail jitter.

## Compare controllers

Offline first:

- current controller
- fixed margin
- EWMA margin
- rolling p99 service-time margin
- asymmetric controller: fast backoff after miss, slow reclaim after success

Score:

- information age p50/p95/p99
- miss rate
- recovery time after disturbance
- oscillation amplitude

## Gate

Only touch the pacer implementation if an offline controller dominates current behavior over multiple disturbance families rather than one synthetic trace.
