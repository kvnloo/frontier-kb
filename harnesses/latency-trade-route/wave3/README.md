# E2E latency trade route — wave 3

Status: **triaged and staged, not executed**

Wave 3 moves upstream in the pipeline:

```text
mouse sensor
 -> USB/HID
 -> kernel input timestamp
 -> userspace event read
 -> library event queue
 -> engine/compositor dispatch
 -> simulation/cursor update
 -> render/present
 -> display
```

## Core question

At 125 / 500 / 1000 / 2000 / 4000 / 8000 Hz input rates:

- which layers process O(events)?
- which batch?
- which coalesce?
- which preserve the newest sample?
- where does queue age grow?
- where does CPU overhead begin causing *more* latency than the higher polling rate removes?

## Lanes

1. SDL — buffered raw input and event-age distribution
2. Godot — merged high-polling Windows fix, accumulation, captured vs visible cursor
3. Hyprland/Aquamarine — cursor-plane vs software-cursor amplification
4. MangoHud — observer effect and display-latency measurement feasibility
5. Linux evdev/HID — kernel-event -> userspace-read age
6. GLFW — unbuffered Win32 raw input as a control case
7. Wine/Proton — Linux input to Windows game API bridge

## Shared output

For each layer report:

```text
event_rate
events_received
events_consumed
events_coalesced
mean_event_age
p50/p95/p99/p99.9 event_age
CPU time/event
CPU utilization
wakeups/sec
context switches/sec
frame p50/p95/p99/p99.9
display/input latency when available
```

An optimization is not a win if it lowers CPU usage by consuming older input.

## Promotion

None. These packets are for local/downstream evidence gathering only.
