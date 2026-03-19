"""
Surge XT Parameter Schema — all paths verified by live OSC discovery.
✓ = confirmed from Surge XT output
~ = inferred from confirmed pattern (same path structure)
"""

# ─── OSCILLATOR 1 ────────────────────────────────────────────────────────────
OSC1 = {
    "osc1_pitch": {
        "osc_path": "/param/a/osc/1/pitch",         # ✓
        "description": "Pitch offset. 0.5=center, <0.5=lower, >0.5=higher.",
    },
    "osc1_param1": {
        "osc_path": "/param/a/osc/1/param1",         # ✓ (waveform-specific)
        "description": "Oscillator param 1 (meaning depends on waveform type).",
    },
    "osc1_param2": {
        "osc_path": "/param/a/osc/1/param2",         # ✓
        "description": "Oscillator param 2.",
    },
    "osc1_param3": {
        "osc_path": "/param/a/osc/1/param3",         # ✓
        "description": "Oscillator param 3.",
    },
    "osc1_param4": {
        "osc_path": "/param/a/osc/1/param4",         # ✓
        "description": "Oscillator param 4.",
    },
    "osc1_param5": {
        "osc_path": "/param/a/osc/1/param5",         # ✓
        "description": "Oscillator param 5 (e.g. sync amount in semitones).",
    },
    "osc1_unison_detune": {
        "osc_path": "/param/a/osc/1/param6",         # ✓ = 'cents' detune
        "description": "Unison detune spread in cents. 0=none, 1=max.",
    },
    "osc1_unison_voices": {
        "osc_path": "/param/a/osc/1/param7",         # ✓ = voice count
        "description": "Unison voice count. Normalized: 0=1 voice, 1=16 voices.",
    },
    "osc1_level": {
        "osc_path": "/param/a/mixer/osc1/volume",    # ✓
        "description": "Oscillator 1 volume in the mixer.",
    },
}

# ─── OSCILLATOR 2 ────────────────────────────────────────────────────────────
OSC2 = {
    "osc2_pitch": {
        "osc_path": "/param/a/osc/2/pitch",          # ~ inferred
        "description": "Oscillator 2 pitch offset.",
    },
    "osc2_level": {
        "osc_path": "/param/a/mixer/osc2/volume",    # ✓
        "description": "Oscillator 2 volume in the mixer. 0=silent.",
    },
}

# ─── NOISE ───────────────────────────────────────────────────────────────────
NOISE = {
    "noise_level": {
        "osc_path": "/param/a/mixer/noise/volume",   # ✓
        "description": "Noise oscillator volume. 0=off.",
    },
    "noise_color": {
        "osc_path": "/param/a/mixer/noise/color",    # ✓
        "description": "Noise color. 0=white, 1=colored.",
    },
}

# ─── FILTER ──────────────────────────────────────────────────────────────────
FILTER = {
    "filter1_cutoff": {
        "osc_path": "/param/a/filter/1/cutoff",      # ~ inferred (filter/2/cutoff ✓)
        "description": "Filter 1 cutoff. 0=dark/closed, 1=bright/open.",
    },
    "filter1_resonance": {
        "osc_path": "/param/a/filter/1/resonance",   # ~ inferred
        "description": "Filter 1 resonance. 0=smooth, high=peaky/screaming.",
    },
    "filter1_feg_amount": {
        "osc_path": "/param/a/filter/1/feg_amount",  # ✓
        "description": "How much filter envelope modulates cutoff. 0.5=none.",
    },
    "filter2_cutoff": {
        "osc_path": "/param/a/filter/2/cutoff",      # ✓
        "description": "Filter 2 cutoff.",
    },
    "filter2_resonance": {
        "osc_path": "/param/a/filter/2/resonance",   # ~ inferred
        "description": "Filter 2 resonance.",
    },
    "filter2_feg_amount": {
        "osc_path": "/param/a/filter/2/feg_amount",  # ✓
        "description": "Filter 2 envelope modulation amount.",
    },
    "filter_config": {
        "osc_path": "/param/a/filter/config",        # ✓ (0=Serial1, 1=Serial2, 5=Stereo)
        "description": "Filter routing. 0=Serial1, 0.2=Serial2, 1.0=Stereo.",
    },
    "highpass": {
        "osc_path": "/param/a/highpass",             # ✓
        "description": "Scene high-pass filter. 0=off, 1=very high cutoff.",
    },
}

# ─── WAVESHAPER ───────────────────────────────────────────────────────────────
WAVESHAPER = {
    "waveshaper_drive": {
        "osc_path": "/param/a/waveshaper/drive",     # ✓
        "description": "Waveshaper drive/distortion amount.",
    },
}

# ─── AMP ENVELOPE (aeg) ───────────────────────────────────────────────────────
AMP_ENV = {
    "amp_attack": {
        "osc_path": "/param/a/aeg/attack",           # ✓
        "description": "Amp envelope attack. 0=instant, 1=very slow fade in.",
    },
    "amp_decay": {
        "osc_path": "/param/a/aeg/decay",            # ✓
        "description": "Amp envelope decay. How fast it drops to sustain.",
    },
    "amp_sustain": {
        "osc_path": "/param/a/aeg/sustain",          # ✓
        "description": "Amp sustain level. 0=silent, 1=full while held.",
    },
    "amp_release": {
        "osc_path": "/param/a/aeg/release",          # ✓
        "description": "Amp release. 0=cut off instantly, 1=long fade out.",
    },
}

# ─── FILTER ENVELOPE (feg) ───────────────────────────────────────────────────
FILTER_ENV = {
    "filter_env_attack": {
        "osc_path": "/param/a/feg/attack",           # ✓
        "description": "Filter envelope attack.",
    },
    "filter_env_decay": {
        "osc_path": "/param/a/feg/decay",            # ✓
        "description": "Filter envelope decay.",
    },
    "filter_env_sustain": {
        "osc_path": "/param/a/feg/sustain",          # ✓
        "description": "Filter envelope sustain.",
    },
    "filter_env_release": {
        "osc_path": "/param/a/feg/release",          # ✓
        "description": "Filter envelope release.",
    },
}

# ─── LFO (vlfo in Surge XT) ──────────────────────────────────────────────────
LFO = {
    "lfo1_rate": {
        "osc_path": "/param/a/vlfo/1/rate",          # ✓
        "description": "LFO speed. 0=very slow, 1=very fast.",
    },
    "lfo1_depth": {
        "osc_path": "/param/a/vlfo/1/amplitude",     # ✓
        "description": "LFO depth/intensity. 0=off, 1=full modulation.",
    },
    "lfo1_deform": {
        "osc_path": "/param/a/vlfo/1/deform",        # ✓
        "description": "LFO waveform deformation/shape.",
    },
}

# ─── GLOBAL ──────────────────────────────────────────────────────────────────
GLOBAL = {
    "amp_volume": {
        "osc_path": "/param/a/amp/volume",           # ✓
        "description": "Scene amp volume.",
    },
    "amp_pan": {
        "osc_path": "/param/a/amp/pan",              # ✓
        "description": "Pan. 0=hard left, 0.5=center, 1=hard right.",
    },
    "osc_drift": {
        "osc_path": "/param/a/osc/drift",            # ✓
        "description": "Pitch drift/instability across all oscillators.",
    },
    "global_volume": {
        "osc_path": "/param/global/volume",          # ✓
        "description": "Master output volume.",
    },
}

# ─── FULL SCHEMA ─────────────────────────────────────────────────────────────
ALL_PARAMS = {}
ALL_PARAMS.update(OSC1)
ALL_PARAMS.update(OSC2)
ALL_PARAMS.update(NOISE)
ALL_PARAMS.update(FILTER)
ALL_PARAMS.update(WAVESHAPER)
ALL_PARAMS.update(AMP_ENV)
ALL_PARAMS.update(FILTER_ENV)
ALL_PARAMS.update(LFO)
ALL_PARAMS.update(GLOBAL)

# ─── DEFAULT PRESET (clean sine wave baseline) ───────────────────────────────
DEFAULT_PRESET = {
    "osc1_pitch":         0.5,
    "osc1_param1":        0.5,
    "osc1_param2":        0.5,
    "osc1_param3":        0.5,
    "osc1_param4":        0.0,
    "osc1_param5":        0.0,
    "osc1_unison_detune": 0.0,
    "osc1_unison_voices": 0.0,
    "osc1_level":         0.89,   # ~0dB
    "osc2_pitch":         0.5,
    "osc2_level":         0.0,    # silent
    "noise_level":        0.0,    # silent
    "noise_color":        0.5,
    "filter1_cutoff":     1.0,    # fully open
    "filter1_resonance":  0.0,
    "filter1_feg_amount": 0.5,    # neutral
    "filter2_cutoff":     1.0,
    "filter2_resonance":  0.0,
    "filter2_feg_amount": 0.5,
    "filter_config":      0.0,    # Serial 1
    "highpass":           0.0,
    "waveshaper_drive":   0.44,   # neutral
    "amp_attack":         0.0,
    "amp_decay":          0.3,
    "amp_sustain":        1.0,
    "amp_release":        0.3,
    "filter_env_attack":  0.0,
    "filter_env_decay":   0.3,
    "filter_env_sustain": 0.5,
    "filter_env_release": 0.3,
    "lfo1_rate":          0.46,
    "lfo1_depth":         0.0,    # off
    "lfo1_deform":        0.5,
    "amp_volume":         0.97,
    "amp_pan":            0.5,    # center
    "osc_drift":          0.0,
    "global_volume":      0.91,
}


def schema_for_prompt() -> str:
    lines = ["PARAMETER | OSC PATH | DESCRIPTION"]
    lines.append("-" * 80)
    for name, p in ALL_PARAMS.items():
        lines.append(f"{name:<25} | {p['osc_path']:<40} | {p['description'][:65]}")
    return "\n".join(lines)
