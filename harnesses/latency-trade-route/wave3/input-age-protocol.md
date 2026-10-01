# Shared input-age protocol

## Definition

For an input event with source timestamp `t_event` and a consumer timestamp `t_consume`:

```text
event_age = t_consume - t_event
```

For a rendered frame, define:

```text
frame_input_age = display_time - newest_input_timestamp_used_by_frame
```

These are more useful than throughput alone.

## Poll-rate sweep

Where hardware permits:

```text
125 -> 500 -> 1000 -> 2000 -> 4000 -> 8000 Hz
```

Use the same physical movement pattern when possible. A mechanical jig is ideal; otherwise use repeated fixed-duration high-speed sweeps and enough trials to model variance.

## CPU counters

Capture:

- cycles
- instructions
- task-clock
- context-switches
- cpu-migrations
- page-faults
- scheduler wakeups
- process/thread CPU
- IRQ rate if available

## Event counters

For each layer:

- source reports
- received events
- dispatched callbacks
- coalesced/dropped events
- queue depth if observable

## Experimental distinction

**Batching** preserves multiple samples but processes them together.

**Coalescing** intentionally discards intermediate samples.

For latency-sensitive camera control, newest-sample preservation can be more important than preserving every intermediate sample.

A useful policy candidate is:

```text
preserve buttons/wheels exactly;
for motion, retain integrated delta + newest timestamp.
```

Do not implement that policy until traces show event-queue age is the bottleneck.
