# SDL — high-polling input scaling

## Context

Historical issue `libsdl-org/SDL#8756` identified per-event Win32 `GetRawInputData` as pathological for high-polling mice. PR `#8770` merged buffered `GetRawInputBuffer`.

Current SDL 3 also assigns nanosecond event timestamps and Linux evdev derives timestamps from kernel `input_event` timestamps.

Current open raw-input tracking issue:
https://github.com/libsdl-org/SDL/issues/9409

## Experiment A — buffered vs historical unbuffered Win32 path

Compare:

- parent of merge `8fe4a45edf7fcba60b15e44132d701a5afd1e70c`
- current SDL
- 125 / 1000 / 4000 / 8000 Hz
- raw relative mode
- stationary vs continuous motion

Measure:

- `SDL_PumpEvents` duration
- events per pump
- event timestamp -> callback timestamp age
- event queue depth
- CPU/event
- frame-time tails

This produces a clean historical demonstration of why batching matters.

## Experiment B — Linux timestamp fidelity

SDL Linux evdev obtains the kernel event timestamp and maps it into the SDL tick clock domain.

For each motion event record:

```text
kernel-derived SDL timestamp
SDL event dispatch time
application consumption time
```

Cross-check the same device using a direct `/dev/input/eventX` reader.

Questions:

- does event age remain flat as polling rate rises?
- is batching happening below SDL?
- does Wayland/X11 add measurable age relative to direct evdev?
- does relative mode change event count or only routing?

## Experiment C — aggregation semantics

At very high poll rates compare:

- every motion event consumed
- application-side integrated-delta coalescing once per simulation tick
- newest-event-only semantics for position-like input

Score both CPU and displayed information age.

## Gate

Do not propose more SDL batching unless current SDL itself shows queue-age growth or excessive per-event cost.
