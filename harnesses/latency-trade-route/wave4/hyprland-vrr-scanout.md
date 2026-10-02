# Hyprland / Aquamarine — VRR, direct scanout and cursor transitions

Live references:

- Hyprland discussion 12013: VRR cursor stutter
- discussion 13236: VRR breaks without direct scanout + captured cursors
- discussion 14124: severe transient stutter when cursor visibility toggles direct scanout
- discussion 14729: VRR mode causing ~51 FPS behavior on newer Intel panels

## Goal

Measure state-transition cost rather than steady-state FPS only.

## States

```text
composited + cursor visible
composited + cursor captured
direct scanout + cursor hidden
direct scanout -> composited
composited -> direct scanout
VRR off
VRR on
tearing off/on where valid
```

## Capture

For every transition record:

- input event time
- direct-scanout eligibility change
- render damage decision
- atomic commit time
- DRM flip/vblank time
- compositor presentation feedback
- physical photon transition if frameprobe is attached

## Key question

Why can a cursor visibility/focus change perturb several subsequent frames instead of one transition frame?

If the transient lasts multiple frames, look for persistent state:

- color-management path change
- buffer/plane reallocation
- clock/power transition
- swapchain reconfiguration
- VRR state transition
- queued stale frames

## Gate

No renderer change until the first persistent state divergence is identified.
