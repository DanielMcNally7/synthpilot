"""
Surge XT Parameter Schema for SynthPilot

OSC paths verified against Surge XT 1.3+ by live discovery.
Confirmed paths marked with ✓
Paths marked with ~ are pattern-inferred and may need tuning.

Enable OSC in Surge XT: Main Menu → OSC → Enable OSC
In: 53280 | Out: 53281
"""

# ─── OSCILLATOR 1 ───────────────────────────────────────────────────────────
OSC1 = {
    "osc1_pitch": {
        "osc_path": "/param/a/osc/1/pitch",   # ✓ confirmed
        "description": "Pitch offset in semitones. 0.5 = center (no shift).",
    },
    "osc1_octave": {
        "osc_path": "/param/a/osc/1/octave",  # ~ inferred
        "description": "Octave shift. 0.5 = center.",
    },
    "osc1_unison_detune": {
        "osc_path": "/param/a/osc/1/param6",  # ✓ confirmed (21.07 cents)
        "description": "Detuning spread across unison voices. 0=none, 1=max.",
    },
    "osc1_unison_voices": {
        "osc_path": "/param/a/osc/1/param7",  # ✓ confirmed (voice count)
        "description": "Number of unison voices. 0=1 voice, 1=16 voices.",
    },
    "osc1_level": {
        "osc_path": "/param/a/osc/1/level",   # ~ inferred from pattern
        "description": "Volume of oscillator 1 in the mix.",
    },
}

# ─── OSCILLATOR 2 ───────────────────────────────────────────────────────────
OSC2 = {
    "osc2_pitch": {
        "osc_path": "/param/a/osc/2/pitch",   # ~ inferred
        "description": "Pitch offset for oscillator 2 in semitones.",
    },
    "osc2_level": {
        "osc_path": "/param/a/osc/2/level",   # ~ inferred
        "description": "Volume of oscillator 2 in the mix. 0=silent.",
    },
}

# ─── FILTER ─────────────────────────────────────────────────────────────────
FILTER = {
    "filter1_cutoff": {
        "osc_path": "/param/a/filter/1/cutoff",    # ~ inferred (filter/2/cutoff confirmed)
        "description": "Filter cutoff frequency. 0=dark/closed, 1=bright/open.",
    },
    "filter1_resonance": {
        "osc_path": "/param/a/filter/1/resonance", # ~ inferred
        "description": "Filter resonance. 0=smooth, high=peaky.",
    },
    "filter2_cutoff": {
        "osc_path": "/param/a/filter/2/cutoff",    # ✓ confirmed
        "description": "Filter 2 cutoff frequency.",
    },
    "filter2_resonance": {
        "osc_path": "/param/a/filter/2/resonance", # ~ inferred
        "description": "Filter 2 resonance.",
    },
}

# ─── AMP ENVELOPE ────────────────────────────────────────────────────────────
AMP_ENV = {
    "amp_attack": {
        "osc_path": "/param/a/amp_eg/attack",  # ~ inferred
        "description": "How long to reach full volume. 0=instant, 1=very slow.",
    },
    "amp_decay": {
        "osc_path": "/param/a/amp_eg/decay",
        "description": "How fast volume drops to sustain level.",
    },
    "amp_sustain": {
        "osc_path": "/param/a/amp_eg/sustain",
        "description": "Volume held while key is down. 0=silent, 1=full.",
    },
    "amp_release": {
        "osc_path": "/param/a/amp_eg/release",
        "description": "Fade out time after key release. 0=cut off, 1=long tail.",
    },
}

# ─── FILTER ENVELOPE ─────────────────────────────────────────────────────────
FILTER_ENV = {
    "filter_env_attack": {
        "osc_path": "/param/a/filter_eg/attack",
        "description": "Attack of the filter envelope.",
    },
    "filter_env_decay": {
        "osc_path": "/param/a/filter_eg/decay",
        "description": "Decay of the filter envelope.",
    },
    "filter_env_sustain": {
        "osc_path": "/param/a/filter_eg/sustain",
        "description": "Sustain of the filter envelope.",
    },
    "filter_env_release": {
        "osc_path": "/param/a/filter_eg/release",
        "description": "Release of the filter envelope.",
    },
}

# ─── LFO ─────────────────────────────────────────────────────────────────────
LFO = {
    "lfo1_rate": {
        "osc_path": "/param/a/lfo/1/rate",
        "description": "LFO speed. 0=very slow, 1=very fast.",
    },
    "lfo1_depth": {
        "osc_path": "/param/a/lfo/1/magnitude",
        "description": "LFO intensity.",
    },
}

# ─── FULL SCHEMA ──────────────────────────────────────────────────────────────
ALL_PARAMS = {}
ALL_PARAMS.update(OSC1)
ALL_PARAMS.update(OSC2)
ALL_PARAMS.update(FILTER)
ALL_PARAMS.update(AMP_ENV)
ALL_PARAMS.update(FILTER_ENV)
ALL_PARAMS.update(LFO)

# ─── DEFAULT PRESET (sine wave baseline) ─────────────────────────────────────
DEFAULT_PRESET = {
    "osc1_pitch":         0.5,
    "osc1_octave":        0.5,
    "osc1_unison_detune": 0.0,
    "osc1_unison_voices": 0.0,
    "osc1_level":         1.0,
    "osc2_pitch":         0.5,
    "osc2_level":         0.0,
    "filter1_cutoff":     0.8,
    "filter1_resonance":  0.0,
    "filter2_cutoff":     0.8,
    "filter2_resonance":  0.0,
    "amp_attack":         0.0,
    "amp_decay":          0.3,
    "amp_sustain":        0.8,
    "amp_release":        0.3,
    "filter_env_attack":  0.0,
    "filter_env_decay":   0.3,
    "filter_env_sustain": 0.5,
    "filter_env_release": 0.3,
    "lfo1_rate":          0.3,
    "lfo1_depth":         0.0,
}


def schema_for_prompt() -> str:
    lines = ["PARAMETER | OSC PATH | DESCRIPTION"]
    lines.append("-" * 80)
    for name, p in ALL_PARAMS.items():
        lines.append(f"{name:<25} | {p['osc_path']:<40} | {p['description'][:60]}")
    return "\n".join(lines)
