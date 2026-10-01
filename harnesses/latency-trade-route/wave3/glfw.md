# GLFW high-polling control experiment

Live reference: glfw/glfw issue 2684.

Current Win32 raw mouse handling is a useful control against SDL's buffered raw-input design.

Build equivalent minimal event-loop programs against current GLFW and SDL. Sweep 125/1000/4000/8000 Hz where hardware permits.

Measure event-pump wall time, events per second, CPU per event, frame-time tails, process CPU, and event age where timestamps permit.

The purpose is to quantify the cost difference between per-message raw-input handling and buffered acquisition, not to promote a patch in this wave.
