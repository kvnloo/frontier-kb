# Photon metric contract

Frameprobe's current analyzer gives us three useful physical landmarks:

- `t10`: transition onset when safely above sensor/display noise;
- `t50`: midpoint crossing, used as the primary robust latency metric;
- `t90`: near-settled transition.

It also detects strong periodic temporal-light modulation and applies a one-period comb filter before crossing detection when modulation would corrupt the midpoint measurement.

## Why retain all three

```text
input -> t10 = earliest measurable display response
input -> t50 = robust display-response latency
input -> t90 = near-settled response
t90 - t10   = physical transition duration
```

For gaming/perception experiments, these answer different questions.

A strobe mode might improve motion clarity while:

- delaying t10;
- narrowing the emitted-light window;
- leaving t50 similar;
- changing t90;
- changing perceived edge clarity.

Do not collapse them into one "latency" number.

## Physical correlation record

For every physical trial retain:

```text
trigger_press_us
usb_delivery_us          # where supported
latest_input_sample
app_present_id
app_target_present
compositor_present
drm_first_pixel
photon_t10
photon_t50
photon_t90
sensor_vertical_position
refresh_hz
vrr_state
strobe_mode
brightness
transition_direction
```

## Derived metrics

```text
usb_to_t10
usb_to_t50
usb_to_t90
drm_to_t10
drm_to_t50
transition_time = t90 - t10
software_before_scanout = drm_first_pixel - usb_delivery
```

When testing sensor placement at different vertical positions:

```text
scanout_delta = photon_same_transition_bottom - photon_same_transition_top
```

This gives a direct physical estimate of top-to-bottom scanout.

## Temporal-light modulation

Backlight strobing, PWM, OLED brightness dips, and similar modulation can create false threshold crossings.

Always retain raw ADC traces. If a filter is used, report:

- detected modulation period;
- raw trace;
- filtered trace;
- crossing method.

## Perceptual follow-up

Only after this metric contract is stable should we compare:

- full persistence vs strobing;
- strobe phase;
- duty cycle;
- brightness;
- refresh rate;
- VRR.

The optimization target can then explicitly trade:

```text
information freshness
motion clarity
transition duration
brightness
flicker / temporal modulation
```

rather than optimizing a single synthetic latency number.
