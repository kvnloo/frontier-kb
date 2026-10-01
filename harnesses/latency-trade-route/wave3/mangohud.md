# MangoHud observer-effect experiment

Live references: MangoHud issues 2117 and 2142.

Goal: quantify the measurement overhead before using MangoHud as part of the latency lab.

Use A/B/B/A runs for no overlay, minimal overlay, detailed frametime overlay, and mangoapp where relevant. Repeat with VRR off/on and high-rate mouse movement.

Record application CPU, overlay CPU, wakeups, context switches, frame-time tails, GPU utilization, and present cadence.

Separately inventory existing display-timing sources (gamescope timing, Vulkan present timing, compositor feedback, DRM/pageflip timestamps) to see whether display latency can be shown without adding a high-frequency polling loop.

No upstream promotion in this wave.
