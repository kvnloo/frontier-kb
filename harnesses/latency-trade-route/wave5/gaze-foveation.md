# Eye tracking / foveation — gaze information age

Useful OSS surfaces:

- EyeTrackVR — active open VR eye-tracking platform with current Linux work
- Pupil Core — open-source eye tracking with a real-time API
- OpenXR `XR_EXT_eye_gaze_interaction`
- Monado / ALVR for later integration experiments

## Core metric

Treat gaze like mouse input:

```text
gaze_age_at_shading =
time foveated region is chosen - eye sample timestamp

gaze_age_at_photon =
photon time - eye sample timestamp
```

## Pipeline

Instrument:

```text
camera exposure
 -> frame arrival
 -> eye model inference
 -> gaze estimate
 -> transport/API
 -> OpenXR gaze sample
 -> foveation-center selection
 -> render
 -> photon
```

## Experiment A — sensor/inference latency

Use a moving calibration target.

Record camera frame timestamp, inference completion and emitted gaze timestamp.

Sweep:

- model size
- camera FPS
- mono/stereo where supported
- CPU/GPU inference path

Score accuracy **and** latency.

## Experiment B — stale-fovea tolerance

Replay recorded gaze traces and intentionally delay them by controlled amounts.

Measure the point where the high-resolution region visibly lags eye motion using:

- objective region error in degrees/pixels
- human detection task
- rendered workload savings

## Experiment C — gaze prediction

Offline only first.

Compare:

- latest sample
- constant-velocity prediction
- short-horizon filtered prediction

Report angular error by horizon and gaze-to-photon age.

Do not deploy prediction unless it improves error at the actual render-to-photon horizon, not only average offline error.
