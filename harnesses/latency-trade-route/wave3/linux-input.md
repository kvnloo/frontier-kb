# Linux input event-age floor

Goal: measure the earliest userspace-visible part of the input path.

For each evdev SYN_REPORT, record the kernel event timestamp and userspace read timestamp, then compute kernel-to-read age.

Sweep input report rates and repeat under controlled CPU contention. Compare scheduler configurations from Wave 1.

Record event-age p50/p95/p99/p99.9, read batch size, wakeups, scheduler delay, CPU migrations, and IRQ rate where available.

This does not measure sensor-to-USB latency; external hardware is still required for the full physical input floor.

No upstream promotion in this wave.
