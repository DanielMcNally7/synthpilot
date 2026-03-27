"""
Surge XT Parameter Schema
Source-confirmed from OpenSoundControl.cpp, SurgePatch.cpp, SurgeStorage.h.

OSC TYPE RULE (source-confirmed):
  ALL values must be sent as OSC float32.
  - value_type = "float_norm" → normalized 0.0–1.0
  - value_type = "int"        → raw integer as float (e.g. float(1) for Sine osc)
                                 Surge calls intScaledToFloat() internally on receive
  - value_type = "bool"       → 0.0 (off/false) or 1.0 (on/true)

OSCILLATOR TYPES (source-confirmed from SurgeStorage.h):
  0=Classic  1=Sine  2=Wavetable  3=S&H Noise  4=AudioInput(avoid!)
  5=FM3  6=FM2  7=Window  8=Modern  9=String  10=Twist  11=Alias

FILTER TYPES (source-confirmed):
  0=LP12  1=LP24  2=LP Moog  7=HP12  8=HP24  11=BP12  12=BP24  13=Notch
"""

OSC_TYPES = {
    "Classic":   0,
    "Sine":      1,   # source-confirmed: ot_sine=1 (NOT 4 — 4=AudioInput)
    "Wavetable": 2,
    "SH_Noise":  3,
    "FM3":       5,
    "FM2":       6,
    "Window":    7,
    "Modern":    8,
    "String":    9,
    "Twist":     10,
    "Alias":     11,
}

# ─── CLASSIC OSCILLATOR (type=0) param meanings ──────────────────────────────
# param1 = Sawtooth amount  (0=none → 1=full saw)
# param2 = Pulse amount     (0=none → 1=full square)
# param3 = Triangle amount  (0=none → 1=full triangle)
# param4 = Pulse width      (0.5=50% duty cycle)
# param5 = Hard sync        (0=off)
# param6 = Unison detune cents
# param7 = Unison voices (normalized: 0=1 voice, 1=16 voices)
# NOTE: all params at 0 = no waveform components = silence. Set at least one > 0.

# ─── SINE OSCILLATOR (type=1) param meanings ─────────────────────────────────
# param1 = Feedback         (0=pure sine, higher=harmonics/buzz)
# param2 = FM from routing  (0=off)
# param3 = Internal filter  (0=off)
# param6 = Unison detune cents
# param7 = Unison voices

# ─── FM2 OSCILLATOR (type=6) param meanings ──────────────────────────────────
# param1 = Ratio A  param2 = Ratio B  param3 = M1 depth
# param4 = M2 depth  param5 = Feedback

# ─── OSC ROUTE values ─────────────────────────────────────────────────────────
# 0=Filter1 only  1=Both filters  2=Filter2 only

# ─── OSCILLATORS ─────────────────────────────────────────────────────────────
OSC1 = {
    "osc1_type": {
        "osc_path": "/param/a/osc/1/type",
        "value_type": "int",
        "values": OSC_TYPES,
        "description": "Osc 1 type. INT: 0=Classic, 1=Sine, 2=Wavetable, 5=FM3, 6=FM2, 8=Modern, 9=String. NEVER 4.",
    },
    "osc1_octave": {
        "osc_path": "/param/a/osc/1/octave",
        "value_type": "int",
        "range": (-3, 3),
        "description": "Octave offset. INT: -3 to +3. 0=no shift.",
    },
    "osc1_pitch": {
        "osc_path": "/param/a/osc/1/pitch",
        "value_type": "float_norm",
        "description": "Pitch fine offset. 0.5=center (no shift). 0.0=-7st, 1.0=+7st.",
    },
    "osc1_param1": {
        "osc_path": "/param/a/osc/1/param1",
        "value_type": "float_norm",
        "description": "Classic: Sawtooth (0=none, 1=full). Sine: Feedback (0=clean). FM2: Ratio A.",
    },
    "osc1_param2": {
        "osc_path": "/param/a/osc/1/param2",
        "value_type": "float_norm",
        "description": "Classic: Pulse (0=none, 1=full square). Sine: FM routing (0=off). FM2: Ratio B.",
    },
    "osc1_param3": {
        "osc_path": "/param/a/osc/1/param3",
        "value_type": "float_norm",
        "description": "Classic: Triangle (0=none, 1=full). Sine: Internal filter (0=off). FM2: M1 depth.",
    },
    "osc1_param4": {
        "osc_path": "/param/a/osc/1/param4",
        "value_type": "float_norm",
        "description": "Classic: Pulse width (0.5=50% duty). FM2: M2 depth.",
    },
    "osc1_param5": {
        "osc_path": "/param/a/osc/1/param5",
        "value_type": "float_norm",
        "description": "Classic: Hard sync (0=off). FM2: Feedback.",
    },
    "osc1_unison_detune": {
        "osc_path": "/param/a/osc/1/param6",
        "value_type": "float_norm",
        "description": "Unison detune spread in cents. 0=no detune.",
    },
    "osc1_unison_voices": {
        "osc_path": "/param/a/osc/1/param7",
        "value_type": "float_norm",
        "description": "Unison voice count. 0=1 voice, 1=16 voices.",
    },
    "osc1_level": {
        "osc_path": "/param/a/mixer/osc1/volume",
        "value_type": "float_norm",
        "description": "Osc 1 volume in mixer. 0.89≈0dB. Keep ≥0.85 for audible output.",
    },
    "osc1_mute": {
        "osc_path": "/param/a/mixer/osc1/mute",
        "value_type": "bool",
        "description": "Osc 1 mute. 0=unmuted (audible), 1=muted (silent). ALWAYS set 0 unless intentional.",
    },
    "osc1_solo": {
        "osc_path": "/param/a/mixer/osc1/solo",
        "value_type": "bool",
        "description": "Osc 1 solo. 0=normal, 1=solo (mutes other oscs).",
    },
    "osc1_route": {
        "osc_path": "/param/a/mixer/osc1/route",
        "value_type": "int",
        "description": "Osc 1 filter routing. INT: 0=Filter1, 1=Both, 2=Filter2.",
    },
    "osc1_keytrack": {
        "osc_path": "/param/a/osc/1/keytrack",
        "value_type": "bool",
        "description": "Pitch follows keyboard. 1=on (normal), 0=off (drone at fixed pitch).",
    },
    "osc1_retrigger": {
        "osc_path": "/param/a/osc/1/retrigger",
        "value_type": "bool",
        "description": "Retrigger oscillator phase on each note. 0=free-running, 1=retrigger.",
    },
}

OSC2 = {
    "osc2_type": {
        "osc_path": "/param/a/osc/2/type",
        "value_type": "int",
        "values": OSC_TYPES,
        "description": "Osc 2 type. Same values as osc1_type. 0=Classic, 1=Sine, 6=FM2.",
    },
    "osc2_octave": {
        "osc_path": "/param/a/osc/2/octave",
        "value_type": "int",
        "range": (-3, 3),
        "description": "Osc 2 octave offset. INT: -3 to +3.",
    },
    "osc2_pitch": {
        "osc_path": "/param/a/osc/2/pitch",
        "value_type": "float_norm",
        "description": "Osc 2 pitch fine offset. 0.5=center. Detune slightly for thickness.",
    },
    "osc2_param1": {
        "osc_path": "/param/a/osc/2/param1",
        "value_type": "float_norm",
        "description": "Osc 2 param 1 (same meaning as osc1 for matching type).",
    },
    "osc2_param2": {
        "osc_path": "/param/a/osc/2/param2",
        "value_type": "float_norm",
        "description": "Osc 2 param 2.",
    },
    "osc2_param3": {
        "osc_path": "/param/a/osc/2/param3",
        "value_type": "float_norm",
        "description": "Osc 2 param 3.",
    },
    "osc2_param4": {
        "osc_path": "/param/a/osc/2/param4",
        "value_type": "float_norm",
        "description": "Osc 2 param 4.",
    },
    "osc2_param5": {
        "osc_path": "/param/a/osc/2/param5",
        "value_type": "float_norm",
        "description": "Osc 2 param 5.",
    },
    "osc2_unison_detune": {
        "osc_path": "/param/a/osc/2/param6",
        "value_type": "float_norm",
        "description": "Osc 2 unison detune.",
    },
    "osc2_unison_voices": {
        "osc_path": "/param/a/osc/2/param7",
        "value_type": "float_norm",
        "description": "Osc 2 unison voices.",
    },
    "osc2_level": {
        "osc_path": "/param/a/mixer/osc2/volume",
        "value_type": "float_norm",
        "description": "Osc 2 volume. 0=silent (off by default). Set >0 to blend in.",
    },
    "osc2_mute": {
        "osc_path": "/param/a/mixer/osc2/mute",
        "value_type": "bool",
        "description": "Osc 2 mute. 0=unmuted, 1=muted.",
    },
    "osc2_solo": {
        "osc_path": "/param/a/mixer/osc2/solo",
        "value_type": "bool",
        "description": "Osc 2 solo.",
    },
    "osc2_route": {
        "osc_path": "/param/a/mixer/osc2/route",
        "value_type": "int",
        "description": "Osc 2 filter routing. INT: 0=Filter1, 1=Both, 2=Filter2.",
    },
    "osc2_keytrack": {
        "osc_path": "/param/a/osc/2/keytrack",
        "value_type": "bool",
        "description": "Osc 2 pitch follows keyboard. 1=on.",
    },
    "osc2_retrigger": {
        "osc_path": "/param/a/osc/2/retrigger",
        "value_type": "bool",
        "description": "Osc 2 retrigger phase on note.",
    },
}

OSC3 = {
    "osc3_type": {
        "osc_path": "/param/a/osc/3/type",
        "value_type": "int",
        "values": OSC_TYPES,
        "description": "Osc 3 type.",
    },
    "osc3_octave": {
        "osc_path": "/param/a/osc/3/octave",
        "value_type": "int",
        "range": (-3, 3),
        "description": "Osc 3 octave offset.",
    },
    "osc3_pitch": {
        "osc_path": "/param/a/osc/3/pitch",
        "value_type": "float_norm",
        "description": "Osc 3 pitch fine offset.",
    },
    "osc3_param1": {
        "osc_path": "/param/a/osc/3/param1",
        "value_type": "float_norm",
        "description": "Osc 3 param 1.",
    },
    "osc3_param2": {
        "osc_path": "/param/a/osc/3/param2",
        "value_type": "float_norm",
        "description": "Osc 3 param 2.",
    },
    "osc3_param3": {
        "osc_path": "/param/a/osc/3/param3",
        "value_type": "float_norm",
        "description": "Osc 3 param 3.",
    },
    "osc3_param4": {
        "osc_path": "/param/a/osc/3/param4",
        "value_type": "float_norm",
        "description": "Osc 3 param 4.",
    },
    "osc3_param5": {
        "osc_path": "/param/a/osc/3/param5",
        "value_type": "float_norm",
        "description": "Osc 3 param 5.",
    },
    "osc3_unison_detune": {
        "osc_path": "/param/a/osc/3/param6",
        "value_type": "float_norm",
        "description": "Osc 3 unison detune.",
    },
    "osc3_unison_voices": {
        "osc_path": "/param/a/osc/3/param7",
        "value_type": "float_norm",
        "description": "Osc 3 unison voices.",
    },
    "osc3_level": {
        "osc_path": "/param/a/mixer/osc3/volume",
        "value_type": "float_norm",
        "description": "Osc 3 volume. 0=silent.",
    },
    "osc3_mute": {
        "osc_path": "/param/a/mixer/osc3/mute",
        "value_type": "bool",
        "description": "Osc 3 mute. 0=unmuted, 1=muted.",
    },
    "osc3_solo": {
        "osc_path": "/param/a/mixer/osc3/solo",
        "value_type": "bool",
        "description": "Osc 3 solo.",
    },
    "osc3_route": {
        "osc_path": "/param/a/mixer/osc3/route",
        "value_type": "int",
        "description": "Osc 3 filter routing. INT: 0=Filter1, 1=Both, 2=Filter2.",
    },
    "osc3_keytrack": {
        "osc_path": "/param/a/osc/3/keytrack",
        "value_type": "bool",
        "description": "Osc 3 pitch follows keyboard.",
    },
    "osc3_retrigger": {
        "osc_path": "/param/a/osc/3/retrigger",
        "value_type": "bool",
        "description": "Osc 3 retrigger phase on note.",
    },
}

# ─── MIXER ────────────────────────────────────────────────────────────────────
MIXER = {
    "noise_level": {
        "osc_path": "/param/a/mixer/noise/volume",
        "value_type": "float_norm",
        "description": "Noise volume. 0=off. Add for texture/breath.",
    },
    "noise_color": {
        "osc_path": "/param/a/mixer/noise/color",
        "value_type": "float_norm",
        "description": "Noise color. 0=white, 1=pink/colored.",
    },
    "noise_mute": {
        "osc_path": "/param/a/mixer/noise/mute",
        "value_type": "bool",
        "description": "Noise mute. 0=unmuted, 1=muted.",
    },
    "noise_route": {
        "osc_path": "/param/a/mixer/noise/route",
        "value_type": "int",
        "description": "Noise filter routing. INT: 0=Filter1, 1=Both, 2=Filter2.",
    },
    "ring_mod_1x2": {
        "osc_path": "/param/a/mixer/rm1x2/volume",
        "value_type": "float_norm",
        "description": "Ring mod osc1×osc2 volume. 0=off. Metallic/bell tones.",
    },
    "rm1x2_mute": {
        "osc_path": "/param/a/mixer/rm1x2/mute",
        "value_type": "bool",
        "description": "Ring mod 1×2 mute.",
    },
    "rm1x2_route": {
        "osc_path": "/param/a/mixer/rm1x2/route",
        "value_type": "int",
        "description": "Ring mod 1×2 routing. INT: 0=Filter1, 1=Both, 2=Filter2.",
    },
    "ring_mod_2x3": {
        "osc_path": "/param/a/mixer/rm2x3/volume",
        "value_type": "float_norm",
        "description": "Ring mod osc2×osc3 volume. 0=off.",
    },
    "rm2x3_mute": {
        "osc_path": "/param/a/mixer/rm2x3/mute",
        "value_type": "bool",
        "description": "Ring mod 2×3 mute.",
    },
    "rm2x3_route": {
        "osc_path": "/param/a/mixer/rm2x3/route",
        "value_type": "int",
        "description": "Ring mod 2×3 routing. INT: 0=Filter1, 1=Both, 2=Filter2.",
    },
    "prefilter_gain": {
        "osc_path": "/param/a/mixer/prefilter_gain",
        "value_type": "float_norm",
        "description": "Gain before filters. 0.5=neutral. Higher=more drive/saturation.",
    },
}

# ─── FILTER ──────────────────────────────────────────────────────────────────
# Filter types (raw int as float, source-confirmed):
# 0=LP12  1=LP24  2=LP Moog  7=HP12  8=HP24  11=BP12  12=BP24  13=Notch

FILTER_TYPES = {
    "LP12": 0, "LP24": 1, "LP_Moog": 2,
    "HP12": 7, "HP24": 8,
    "BP12": 11, "BP24": 12,
    "Notch": 13,
}

FILTER = {
    "filter1_type": {
        "osc_path": "/param/a/filter/1/type",
        "value_type": "int",
        "values": FILTER_TYPES,
        "description": "Filter 1 type. INT: 0=LP12, 1=LP24, 2=Moog, 7=HP12, 8=HP24, 11=BP12, 13=Notch.",
    },
    "filter1_subtype": {
        "osc_path": "/param/a/filter/1/subtype",
        "value_type": "int",
        "description": "Filter 1 subtype. Changes character within the type (e.g. Clean/Driven/Smooth).",
    },
    "filter1_cutoff": {
        "osc_path": "/param/a/filter/1/cutoff",
        "value_type": "float_norm",
        "description": "Filter 1 cutoff. 0=closed/dark, 1=wide open/bright.",
    },
    "filter1_resonance": {
        "osc_path": "/param/a/filter/1/resonance",
        "value_type": "float_norm",
        "description": "Filter 1 resonance. 0=flat, 0.7=vocal peak, >0.9=self-oscillation.",
    },
    "filter1_feg_amount": {
        "osc_path": "/param/a/filter/1/feg_amount",
        "value_type": "float_norm",
        "description": "Filter 1 envelope amount. 0.5=neutral, >0.5=opens, <0.5=closes.",
    },
    "filter1_keytrack": {
        "osc_path": "/param/a/filter/1/keytrack",
        "value_type": "float_norm",
        "description": "Filter 1 pitch tracking. 0=none, 0.5=half, 1.0=full (cutoff tracks note pitch).",
    },
    "filter2_type": {
        "osc_path": "/param/a/filter/2/type",
        "value_type": "int",
        "values": FILTER_TYPES,
        "description": "Filter 2 type.",
    },
    "filter2_subtype": {
        "osc_path": "/param/a/filter/2/subtype",
        "value_type": "int",
        "description": "Filter 2 subtype.",
    },
    "filter2_cutoff": {
        "osc_path": "/param/a/filter/2/cutoff",
        "value_type": "float_norm",
        "description": "Filter 2 cutoff.",
    },
    "filter2_resonance": {
        "osc_path": "/param/a/filter/2/resonance",
        "value_type": "float_norm",
        "description": "Filter 2 resonance.",
    },
    "filter2_feg_amount": {
        "osc_path": "/param/a/filter/2/feg_amount",
        "value_type": "float_norm",
        "description": "Filter 2 envelope amount.",
    },
    "filter2_keytrack": {
        "osc_path": "/param/a/filter/2/keytrack",
        "value_type": "float_norm",
        "description": "Filter 2 pitch tracking. 0=none, 1.0=full.",
    },
    "filter2_offset_mode": {
        "osc_path": "/param/a/filter/2/offset",
        "value_type": "bool",
        "description": "Filter 2 offset mode. 1=filter 2 cutoff is offset relative to filter 1.",
    },
    "filter2_link_resonance": {
        "osc_path": "/param/a/filter/2/link_resonance",
        "value_type": "bool",
        "description": "Filter 2 link resonance to filter 1. 1=both resonances move together.",
    },
    "filter_balance": {
        "osc_path": "/param/a/filter/balance",
        "value_type": "float_norm",
        "description": "Filter 1/2 mix balance. 0=only Filter1, 0.5=equal, 1=only Filter2.",
    },
    "filter_keytrack_root": {
        "osc_path": "/param/a/filter/keytrack_root",
        "value_type": "int",
        "description": "MIDI note where keytrack is neutral. INT: 60=middle C (default).",
    },
    "filter_config": {
        "osc_path": "/param/a/filter/config",
        "value_type": "int",
        "description": "Filter routing. INT: 0=Serial1, 1=Serial2, 2=Serial3, 3=Dual1, 4=Dual2, 5=Stereo, 6=Ring.",
    },
    "filter_feedback": {
        "osc_path": "/param/a/filter/feedback",
        "value_type": "float_norm",
        "description": "Filter feedback. 0=off.",
    },
    "highpass": {
        "osc_path": "/param/a/highpass",
        "value_type": "float_norm",
        "description": "Scene high-pass. 0=off (pass all). Removes low rumble.",
    },
}

# ─── WAVESHAPER ───────────────────────────────────────────────────────────────
WAVESHAPER = {
    "waveshaper_drive": {
        "osc_path": "/param/a/waveshaper/drive",
        "value_type": "float_norm",
        "description": "Waveshaper drive. 0=bypassed, 0.5=moderate saturation, 1=heavy.",
    },
    "waveshaper_type": {
        "osc_path": "/param/a/waveshaper/type",
        "value_type": "int",
        "description": "Waveshaper curve. INT: 0=Soft, 1=Hard, 2=Asymmetric, 3=Sine, 4=Digital.",
    },
}

# ─── AMP ENVELOPE (aeg) ───────────────────────────────────────────────────────
AMP_ENV = {
    "amp_attack": {
        "osc_path": "/param/a/aeg/attack",
        "value_type": "float_norm",
        "description": "Amp attack. 0=instant. 0.25=~30ms. 0.5=~300ms. 1.0=very slow.",
    },
    "amp_decay": {
        "osc_path": "/param/a/aeg/decay",
        "value_type": "float_norm",
        "description": "Amp decay. 0=instant. 0.5=~200ms.",
    },
    "amp_sustain": {
        "osc_path": "/param/a/aeg/sustain",
        "value_type": "float_norm",
        "description": "Amp sustain level. 0=silent after decay. 1.0=full.",
    },
    "amp_release": {
        "osc_path": "/param/a/aeg/release",
        "value_type": "float_norm",
        "description": "Amp release. 0=cut off. 0.3=~80ms. 0.7=~2s.",
    },
    "amp_attack_shape": {
        "osc_path": "/param/a/aeg/attack_shape",
        "value_type": "int",
        "description": "Amp attack curve. INT: 0=Linear, 1=Quadratic, 2=Cubic.",
    },
    "amp_decay_shape": {
        "osc_path": "/param/a/aeg/decay_shape",
        "value_type": "int",
        "description": "Amp decay curve. INT: 0=Linear, 1=Quadratic, 2=Cubic.",
    },
    "amp_release_shape": {
        "osc_path": "/param/a/aeg/release_shape",
        "value_type": "int",
        "description": "Amp release curve. INT: 0=Linear, 1=Quadratic, 2=Cubic.",
    },
    "amp_mode": {
        "osc_path": "/param/a/aeg/mode",
        "value_type": "bool",
        "description": "Amp envelope mode. 0=Digital (precise), 1=Analog (warmer, slight quirks).",
    },
}

# ─── FILTER ENVELOPE (feg) ────────────────────────────────────────────────────
FILTER_ENV = {
    "filter_env_attack": {
        "osc_path": "/param/a/feg/attack",
        "value_type": "float_norm",
        "description": "Filter envelope attack.",
    },
    "filter_env_decay": {
        "osc_path": "/param/a/feg/decay",
        "value_type": "float_norm",
        "description": "Filter envelope decay.",
    },
    "filter_env_sustain": {
        "osc_path": "/param/a/feg/sustain",
        "value_type": "float_norm",
        "description": "Filter envelope sustain.",
    },
    "filter_env_release": {
        "osc_path": "/param/a/feg/release",
        "value_type": "float_norm",
        "description": "Filter envelope release.",
    },
    "filter_env_mode": {
        "osc_path": "/param/a/feg/mode",
        "value_type": "bool",
        "description": "Filter envelope mode. 0=Digital, 1=Analog.",
    },
}

# ─── LFO ─────────────────────────────────────────────────────────────────────
LFO = {
    "lfo1_type": {
        "osc_path": "/param/a/vlfo/1/type",
        "value_type": "int",
        "description": "LFO 1 waveform. INT: 0=Sine, 1=Triangle, 2=Saw, 4=Square, 5=S&H.",
    },
    "lfo1_rate": {
        "osc_path": "/param/a/vlfo/1/rate",
        "value_type": "float_norm",
        "description": "LFO 1 rate. 0=very slow, 0.46=~1.3Hz, 1.0=fast.",
    },
    "lfo1_depth": {
        "osc_path": "/param/a/vlfo/1/amplitude",
        "value_type": "float_norm",
        "description": "LFO 1 depth. 0=no modulation, 1=maximum.",
    },
    "lfo1_deform": {
        "osc_path": "/param/a/vlfo/1/deform",
        "value_type": "float_norm",
        "description": "LFO 1 waveform shape deformation.",
    },
    "lfo1_phase": {
        "osc_path": "/param/a/vlfo/1/phase",
        "value_type": "float_norm",
        "description": "LFO 1 start phase.",
    },
    "lfo1_trigger_mode": {
        "osc_path": "/param/a/vlfo/1/triggermode",
        "value_type": "int",
        "description": "LFO 1 trigger mode. INT: 0=Freerun, 1=Keytrigger, 2=Random.",
    },
    "lfo1_unipolar": {
        "osc_path": "/param/a/vlfo/1/unipolar",
        "value_type": "bool",
        "description": "LFO 1 unipolar. 0=bipolar (-1 to +1), 1=unipolar (0 to 1).",
    },
    "lfo1_eg_delay": {
        "osc_path": "/param/a/vlfo/1/eg/delay",
        "value_type": "float_norm",
        "description": "LFO 1 envelope delay before fade-in starts.",
    },
    "lfo1_eg_attack": {
        "osc_path": "/param/a/vlfo/1/eg/attack",
        "value_type": "float_norm",
        "description": "LFO 1 fade-in time. Delays LFO from reaching full depth — great for vibrato.",
    },
    "lfo1_eg_hold": {
        "osc_path": "/param/a/vlfo/1/eg/hold",
        "value_type": "float_norm",
        "description": "LFO 1 hold time at full depth.",
    },
    "lfo1_eg_decay": {
        "osc_path": "/param/a/vlfo/1/eg/decay",
        "value_type": "float_norm",
        "description": "LFO 1 modulation decay.",
    },
    "lfo1_eg_sustain": {
        "osc_path": "/param/a/vlfo/1/eg/sustain",
        "value_type": "float_norm",
        "description": "LFO 1 modulation sustain.",
    },
    "lfo1_eg_release": {
        "osc_path": "/param/a/vlfo/1/eg/release",
        "value_type": "float_norm",
        "description": "LFO 1 modulation release.",
    },
}

# LFOs 2–6 (voice LFOs — same params as LFO1)
def _make_lfo(n):
    return {
        f"lfo{n}_type": {
            "osc_path": f"/param/a/vlfo/{n}/type",
            "value_type": "int",
            "description": f"LFO {n} waveform. INT: 0=Sine, 1=Triangle, 2=Saw, 4=Square, 5=S&H.",
        },
        f"lfo{n}_rate": {
            "osc_path": f"/param/a/vlfo/{n}/rate",
            "value_type": "float_norm",
            "description": f"LFO {n} rate.",
        },
        f"lfo{n}_depth": {
            "osc_path": f"/param/a/vlfo/{n}/amplitude",
            "value_type": "float_norm",
            "description": f"LFO {n} depth. 0=off.",
        },
        f"lfo{n}_deform": {
            "osc_path": f"/param/a/vlfo/{n}/deform",
            "value_type": "float_norm",
            "description": f"LFO {n} shape deform.",
        },
        f"lfo{n}_phase": {
            "osc_path": f"/param/a/vlfo/{n}/phase",
            "value_type": "float_norm",
            "description": f"LFO {n} start phase.",
        },
        f"lfo{n}_trigger_mode": {
            "osc_path": f"/param/a/vlfo/{n}/triggermode",
            "value_type": "int",
            "description": f"LFO {n} trigger mode. INT: 0=Freerun, 1=Keytrigger, 2=Random.",
        },
        f"lfo{n}_eg_attack": {
            "osc_path": f"/param/a/vlfo/{n}/eg/attack",
            "value_type": "float_norm",
            "description": f"LFO {n} fade-in time.",
        },
        f"lfo{n}_eg_decay": {
            "osc_path": f"/param/a/vlfo/{n}/eg/decay",
            "value_type": "float_norm",
            "description": f"LFO {n} decay.",
        },
        f"lfo{n}_eg_sustain": {
            "osc_path": f"/param/a/vlfo/{n}/eg/sustain",
            "value_type": "float_norm",
            "description": f"LFO {n} sustain.",
        },
        f"lfo{n}_eg_release": {
            "osc_path": f"/param/a/vlfo/{n}/eg/release",
            "value_type": "float_norm",
            "description": f"LFO {n} release.",
        },
    }

LFO2 = _make_lfo(2)
LFO3 = _make_lfo(3)
LFO4 = _make_lfo(4)
LFO5 = _make_lfo(5)
LFO6 = _make_lfo(6)

# Scene LFOs 1–6 (slfo — not voice-tracked, used for scene-level modulation)
def _make_slfo(n):
    return {
        f"slfo{n}_type": {
            "osc_path": f"/param/a/slfo/{n}/type",
            "value_type": "int",
            "description": f"Scene LFO {n} waveform. INT: 0=Sine, 1=Triangle, 2=Saw, 4=Square, 5=S&H.",
        },
        f"slfo{n}_rate": {
            "osc_path": f"/param/a/slfo/{n}/rate",
            "value_type": "float_norm",
            "description": f"Scene LFO {n} rate.",
        },
        f"slfo{n}_depth": {
            "osc_path": f"/param/a/slfo/{n}/amplitude",
            "value_type": "float_norm",
            "description": f"Scene LFO {n} depth. 0=off.",
        },
    }

SLFO1 = _make_slfo(1)
SLFO2 = _make_slfo(2)
SLFO3 = _make_slfo(3)

# ─── AMP EXTRAS ───────────────────────────────────────────────────────────────
AMP_EXTRAS = {
    "amp_width": {
        "osc_path": "/param/a/amp/width",
        "value_type": "float_norm",
        "description": "Stereo width. 0=mono, 0.5=normal stereo, 1=extra wide.",
    },
    "amp_vel_to_gain": {
        "osc_path": "/param/a/amp/veltogain",
        "value_type": "float_norm",
        "description": "Velocity sensitivity. 0=no velocity response (all notes same volume), 1=full dynamics.",
    },
}

# ─── MACRO CONTROLLERS ────────────────────────────────────────────────────────
MACROS = {
    "macro1": {"osc_path": "/param/macro/1", "value_type": "float_norm", "description": "Macro controller 1 (assignable). 0–1."},
    "macro2": {"osc_path": "/param/macro/2", "value_type": "float_norm", "description": "Macro controller 2."},
    "macro3": {"osc_path": "/param/macro/3", "value_type": "float_norm", "description": "Macro controller 3."},
    "macro4": {"osc_path": "/param/macro/4", "value_type": "float_norm", "description": "Macro controller 4."},
    "macro5": {"osc_path": "/param/macro/5", "value_type": "float_norm", "description": "Macro controller 5."},
    "macro6": {"osc_path": "/param/macro/6", "value_type": "float_norm", "description": "Macro controller 6."},
    "macro7": {"osc_path": "/param/macro/7", "value_type": "float_norm", "description": "Macro controller 7."},
    "macro8": {"osc_path": "/param/macro/8", "value_type": "float_norm", "description": "Macro controller 8."},
}

# ─── SCENE / GLOBAL ──────────────────────────────────────────────────────────
SCENE = {
    "scene_pitch": {
        "osc_path": "/param/a/pitch",
        "value_type": "float_norm",
        "description": "Scene pitch offset. 0.5=center (no shift).",
    },
    "scene_octave": {
        "osc_path": "/param/a/octave",
        "value_type": "int",
        "range": (-3, 3),
        "description": "Scene octave offset. INT: -3 to +3. 0=no shift.",
    },
    "portamento": {
        "osc_path": "/param/a/portamento",
        "value_type": "float_norm",
        "description": "Portamento/glide time. 0=off.",
    },
    "fm_depth": {
        "osc_path": "/param/a/osc/fm_depth",
        "value_type": "float_norm",
        "description": "FM depth from osc routing. 0=off.",
    },
    "fm_routing": {
        "osc_path": "/param/a/osc/fm_routing",
        "value_type": "int",
        "description": "FM routing config. INT: 0=Off, 1=2→1, 2=3→2→1, 3=2+3→1, 4=3→1+2, 5=Custom.",
    },
    "osc_drift": {
        "osc_path": "/param/a/osc/drift",
        "value_type": "float_norm",
        "description": "Analog pitch drift across oscillators. 0=perfect tuning, 0.05–0.15=warm.",
    },
    "amp_volume": {
        "osc_path": "/param/a/amp/volume",
        "value_type": "float_norm",
        "description": "Scene output volume. Keep ≥0.95.",
    },
    "amp_pan": {
        "osc_path": "/param/a/amp/pan",
        "value_type": "float_norm",
        "description": "Pan. 0=hard left, 0.5=center, 1=hard right.",
    },
    "global_volume": {
        "osc_path": "/param/global/volume",
        "value_type": "float_norm",
        "description": "Master output volume.",
    },
    "global_character": {
        "osc_path": "/param/global/character",
        "value_type": "float_norm",
        "description": "Global character filter. 0=warm/darker, 0.5=neutral, 1=bright/harsher.",
    },
    "play_mode": {
        "osc_path": "/param/a/play_mode",
        "value_type": "int",
        "description": "Polyphony. INT: 0=Poly, 1=Mono, 3=Mono+Portamento. DEFAULT: 0.",
    },
    "pitchbend_up": {
        "osc_path": "/param/a/pitchbend_up",
        "value_type": "int",
        "range": (0, 24),
        "description": "Pitch bend wheel up range in semitones. Default=2. NEVER set to 0.",
    },
    "pitchbend_down": {
        "osc_path": "/param/a/pitchbend_down",
        "value_type": "int",
        "range": (0, 24),
        "description": "Pitch bend wheel down range in semitones. Default=2. NEVER set to 0.",
    },
}

# ─── FULL SCHEMA ─────────────────────────────────────────────────────────────
ALL_PARAMS = {}
ALL_PARAMS.update(OSC1)
ALL_PARAMS.update(OSC2)
ALL_PARAMS.update(OSC3)
ALL_PARAMS.update(MIXER)
ALL_PARAMS.update(FILTER)
ALL_PARAMS.update(WAVESHAPER)
ALL_PARAMS.update(AMP_ENV)
ALL_PARAMS.update(FILTER_ENV)
ALL_PARAMS.update(LFO)
ALL_PARAMS.update(LFO2)
ALL_PARAMS.update(LFO3)
ALL_PARAMS.update(LFO4)
ALL_PARAMS.update(LFO5)
ALL_PARAMS.update(LFO6)
ALL_PARAMS.update(SLFO1)
ALL_PARAMS.update(SLFO2)
ALL_PARAMS.update(SLFO3)
ALL_PARAMS.update(AMP_EXTRAS)
ALL_PARAMS.update(MACROS)
ALL_PARAMS.update(SCENE)

# ─── DEFAULT PRESET — pure sine wave baseline ─────────────────────────────────
DEFAULT_PRESET = {
    # Osc 1 — Sine oscillator, clean, single voice
    "osc1_type":          1,      # Sine (source-confirmed: ot_sine=1)
    "osc1_octave":        0,
    "osc1_pitch":         0.5,
    "osc1_param1":        0.0,    # No feedback (Sine: 0=clean)
    "osc1_param2":        0.0,    # Sine: FM routing off
    "osc1_param3":        0.0,    # Sine: internal filter off
    "osc1_param4":        0.5,
    "osc1_param5":        0.0,
    "osc1_unison_detune": 0.0,
    "osc1_unison_voices": 0.0,    # 1 voice
    "osc1_level":         0.95,
    "osc1_mute":          0,      # UNMUTED — critical, always 0
    "osc1_solo":          0,
    "osc1_route":         0,      # Filter 1
    "osc1_keytrack":      1,
    "osc1_retrigger":     0,
    # Osc 2 — off
    "osc2_type":          1,
    "osc2_octave":        0,
    "osc2_pitch":         0.5,
    "osc2_param1":        0.0,
    "osc2_param2":        0.0,
    "osc2_param3":        0.0,
    "osc2_param4":        0.5,
    "osc2_param5":        0.0,
    "osc2_unison_detune": 0.0,
    "osc2_unison_voices": 0.0,
    "osc2_level":         0.0,
    "osc2_mute":          0,
    "osc2_solo":          0,
    "osc2_route":         0,
    "osc2_keytrack":      1,
    "osc2_retrigger":     0,
    # Osc 3 — off
    "osc3_type":          1,
    "osc3_octave":        0,
    "osc3_pitch":         0.5,
    "osc3_param1":        0.0,
    "osc3_param2":        0.0,
    "osc3_param3":        0.0,
    "osc3_param4":        0.5,
    "osc3_param5":        0.0,
    "osc3_unison_detune": 0.0,
    "osc3_unison_voices": 0.0,
    "osc3_level":         0.0,
    "osc3_mute":          0,
    "osc3_solo":          0,
    "osc3_route":         0,
    "osc3_keytrack":      1,
    "osc3_retrigger":     0,
    # Mixer
    "noise_level":        0.0,
    "noise_color":        0.5,
    "noise_mute":         0,
    "noise_route":        0,
    "ring_mod_1x2":       0.0,
    "rm1x2_mute":         0,
    "rm1x2_route":        0,
    "ring_mod_2x3":       0.0,
    "rm2x3_mute":         0,
    "rm2x3_route":        0,
    "prefilter_gain":     0.5,
    # Filters — fully open
    "filter1_type":       1,      # LP24
    "filter1_subtype":    0,
    "filter1_cutoff":     1.0,
    "filter1_resonance":  0.0,
    "filter1_feg_amount": 0.5,    # Neutral
    "filter1_keytrack":   0.0,
    "filter2_type":       1,
    "filter2_subtype":    0,
    "filter2_cutoff":     1.0,
    "filter2_resonance":  0.0,
    "filter2_feg_amount": 0.5,
    "filter2_keytrack":   0.0,
    "filter2_offset_mode":     0,
    "filter2_link_resonance":  0,
    "filter_balance":     0.5,
    "filter_keytrack_root": 60,   # Middle C
    "filter_config":      0,      # Serial 1
    "filter_feedback":    0.0,
    "highpass":           0.0,
    # Waveshaper — bypassed
    "waveshaper_drive":   0.0,
    "waveshaper_type":    0,
    # Amp envelope
    "amp_attack":         0.0,
    "amp_decay":          0.3,
    "amp_sustain":        1.0,
    "amp_release":        0.3,
    "amp_attack_shape":   0,
    "amp_decay_shape":    0,
    "amp_release_shape":  0,
    "amp_mode":           0,      # Digital
    # Filter envelope — neutral
    "filter_env_attack":  0.0,
    "filter_env_decay":   0.5,
    "filter_env_sustain": 0.5,
    "filter_env_release": 0.3,
    "filter_env_mode":    0,
    # LFO 1 — off
    "lfo1_type":          0,
    "lfo1_rate":          0.46,
    "lfo1_depth":         0.0,
    "lfo1_deform":        0.5,
    "lfo1_phase":         0.0,
    "lfo1_trigger_mode":  0,
    "lfo1_unipolar":      0,
    "lfo1_eg_delay":      0.0,
    "lfo1_eg_attack":     0.0,
    "lfo1_eg_hold":       0.0,
    "lfo1_eg_decay":      0.5,
    "lfo1_eg_sustain":    1.0,
    "lfo1_eg_release":    0.5,
    # LFOs 2–6 — off
    "lfo2_type": 0, "lfo2_rate": 0.46, "lfo2_depth": 0.0, "lfo2_deform": 0.5, "lfo2_phase": 0.0,
    "lfo2_trigger_mode": 0, "lfo2_eg_attack": 0.0, "lfo2_eg_decay": 0.5, "lfo2_eg_sustain": 1.0, "lfo2_eg_release": 0.5,
    "lfo3_type": 0, "lfo3_rate": 0.46, "lfo3_depth": 0.0, "lfo3_deform": 0.5, "lfo3_phase": 0.0,
    "lfo3_trigger_mode": 0, "lfo3_eg_attack": 0.0, "lfo3_eg_decay": 0.5, "lfo3_eg_sustain": 1.0, "lfo3_eg_release": 0.5,
    "lfo4_type": 0, "lfo4_rate": 0.46, "lfo4_depth": 0.0, "lfo4_deform": 0.5, "lfo4_phase": 0.0,
    "lfo4_trigger_mode": 0, "lfo4_eg_attack": 0.0, "lfo4_eg_decay": 0.5, "lfo4_eg_sustain": 1.0, "lfo4_eg_release": 0.5,
    "lfo5_type": 0, "lfo5_rate": 0.46, "lfo5_depth": 0.0, "lfo5_deform": 0.5, "lfo5_phase": 0.0,
    "lfo5_trigger_mode": 0, "lfo5_eg_attack": 0.0, "lfo5_eg_decay": 0.5, "lfo5_eg_sustain": 1.0, "lfo5_eg_release": 0.5,
    "lfo6_type": 0, "lfo6_rate": 0.46, "lfo6_depth": 0.0, "lfo6_deform": 0.5, "lfo6_phase": 0.0,
    "lfo6_trigger_mode": 0, "lfo6_eg_attack": 0.0, "lfo6_eg_decay": 0.5, "lfo6_eg_sustain": 1.0, "lfo6_eg_release": 0.5,
    # Scene LFOs — off
    "slfo1_type": 0, "slfo1_rate": 0.46, "slfo1_depth": 0.0,
    "slfo2_type": 0, "slfo2_rate": 0.46, "slfo2_depth": 0.0,
    "slfo3_type": 0, "slfo3_rate": 0.46, "slfo3_depth": 0.0,
    # Amp extras
    "amp_width":          0.5,    # Normal stereo
    "amp_vel_to_gain":    0.5,    # Moderate velocity sensitivity
    # Macros — neutral (not assigned by default)
    "macro1": 0.5, "macro2": 0.5, "macro3": 0.5, "macro4": 0.5,
    "macro5": 0.5, "macro6": 0.5, "macro7": 0.5, "macro8": 0.5,
    # Scene
    "scene_pitch":        0.5,
    "scene_octave":       0,
    "portamento":         0.0,
    "fm_depth":           0.0,
    "fm_routing":         0,      # Off
    "osc_drift":          0.0,
    "amp_volume":         0.97,
    "amp_pan":            0.5,
    "global_volume":      0.91,
    "global_character":   0.5,    # Neutral
    "play_mode":          0,      # Poly
    "pitchbend_up":       2,
    "pitchbend_down":     2,
}


def schema_for_prompt() -> str:
    """Returns a human-readable parameter list for injection into Claude's system prompt."""
    lines = []
    lines.append("PARAMETER NAME          | VALUE TYPE | OSC PATH                              | DESCRIPTION")
    lines.append("-" * 120)
    for name, p in ALL_PARAMS.items():
        vtype = p.get("value_type", "float_norm")
        desc = p["description"][:70]
        lines.append(f"{name:<23} | {vtype:<10} | {p['osc_path']:<38} | {desc}")
    return "\n".join(lines)
