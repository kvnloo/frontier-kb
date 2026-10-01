# Hyprland / Aquamarine cursor-path experiment

Live reference: hyprwm/Hyprland discussion 14434.

Goal: measure whether high-rate pointer motion turns into excessive compositor work when the hardware cursor path is unavailable.

Sweep mouse report rates and compare hardware-cursor and software-cursor paths. Record compositor CPU, wakeups, damage operations, cursor-buffer/KMS activity, frame-time tails, and event-to-visible-cursor age where measurable.

Key question: which operation scales with input event rate? A 1000 Hz logical cursor does not require 1000 full scene composites per second.

If a regression reproduces, bisect Aquamarine first, then Hyprland. No upstream promotion in this wave.
