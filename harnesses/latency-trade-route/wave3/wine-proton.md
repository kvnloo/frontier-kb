# Wine / Proton raw-input latency experiment

## Why this lane matters

This is the compatibility-layer bridge between Linux input delivery and Windows game input APIs.

Useful references:

- ValveSoftware/wine issue 60: long-running proposal around lower-latency input paths
- Proton issue 7090: high-rate mouse movement and post-alt-tab stutter
- Proton issue 10091: 2026 report where mouse movement caused severe FPS drops with ntsync enabled and disabling ntsync avoided the symptom
- Proton issue 9655: recent raw-input / DirectInput interaction showing how multiple input paths can interfere

## First experiment

Use one deterministic Windows input test application under Wine/Proton and compare:

- native Linux SDL probe
- Wine raw input
- DirectInput where the test supports it
- XWayland vs native Wayland path where available
- polling-rate sweep
- ntsync on/off
- CPU contention off/on

Record:

- Linux evdev event age
- Wine/Proton process CPU
- input callback/message rate inside the Windows test
- frame-time tails
- scheduler wakeups/context switches
- integrated mouse delta correctness

## Key question

Does queue age appear before Wine, inside the Wine input/wineserver path, or only in the game/event loop?

Do not treat a frametime drop alone as proof of input latency. Correlate it with event age and message-processing cost.

No upstream promotion in this wave.
