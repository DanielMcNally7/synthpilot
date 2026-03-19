"""
Surge XT Parameter Schema for SynthPilot

Each parameter includes:
- osc_path: The OSC address used to control it in Surge XT
- range: (min, max) — the actual value range for human-readable use
- normalized: whether Surge XT expects 0.0–1.0 (True) or raw value (False)
- description: what it does in plain English

OSC default port: Surge XT listens on 53280
Enable in Surge XT: Main Menu → OSC → Enable OSC
"""

# ─── OSCILLATOR 1 ───────────────────────────────────────────────────────────
OSC1 = {
    "osc1_type": {
        "osc_path": "/param/a/osc/1/type",
        "range": (0, 7),
        "normalized": True,
        "description": "Oscillator waveform. 0=Sine, 0.14=Triangle, 0.28=Sawtooth, 0.42=Square, 0.57=Noise, 0.71=S&H Noise, 0.85=Window, 1.0=Wavetable",
        "type": "enum",
        "options": {
            "sine":      0.0,
            "triangle":  0.14,
            "sawtooth":  0.28,
            "square":    0.42,
            "noise":     0.57,
        }
    },
    "osc1_pitch": {
        "osc_path": "/param/a/osc/1/pitch",
        "range": (-48, 48),
        "normalized": True,
        "description": "Pitch offset in semitones. 0.5 = center (no shift).",
    },
    "osc1_octave": {
        "osc_path": "/param/a/osc/1/octave",
        "range": (-3, 3),
        "normalized": True,
        "description": "Octave shift. 0.5 = center.",
    },
    "osc1_level": {
        "osc_path": "/param/a/osc/1/level",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Volume of oscillator 1 in the mix.",
    },
    "osc1_unison_voices": {
        "osc_path": "/param/a/osc/1/unison_voices",
        "range": (1, 16),
        "normalized": True,
        "description": "Number of unison voices. More voices = thicker/wider sound. 0.0 = 1 voice.",
    },
    "osc1_unison_detune": {
        "osc_path": "/param/a/osc/1/unison_detune",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Detuning spread across unison voices. 0 = no detune, 1.0 = max detune.",
    },
}

# ─── OSCILLATOR 2 ───────────────────────────────────────────────────────────
OSC2 = {
    "osc2_type": {
        "osc_path": "/param/a/osc/2/type",
        "range": (0, 7),
        "normalized": True,
        "description": "Oscillator 2 waveform. Same options as osc1.",
        "type": "enum",
        "options": {
            "sine":      0.0,
            "triangle":  0.14,
            "sawtooth":  0.28,
            "square":    0.42,
            "noise":     0.57,
        }
    },
    "osc2_pitch": {
        "osc_path": "/param/a/osc/2/pitch",
        "range": (-48, 48),
        "normalized": True,
        "description": "Pitch offset for osc 2 in semitones.",
    },
    "osc2_level": {
        "osc_path": "/param/a/osc/2/level",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Volume of oscillator 2 in the mix.",
    },
}

# ─── FILTER ─────────────────────────────────────────────────────────────────
FILTER = {
    "filter1_type": {
        "osc_path": "/param/a/filter/1/type",
        "range": (0, 1),
        "normalized": True,
        "description": "Filter type. 0=LP12, 0.2=LP24, 0.4=HP12, 0.6=BP, 0.8=Notch, 1.0=Off",
        "type": "enum",
        "options": {
            "lowpass_12":  0.0,
            "lowpass_24":  0.2,
            "highpass_12": 0.4,
            "bandpass":    0.6,
            "notch":       0.8,
            "off":         1.0,
        }
    },
    "filter1_cutoff": {
        "osc_path": "/param/a/filter/1/cutoff",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Filter cutoff frequency. 0=low/dark, 1=high/bright.",
    },
    "filter1_resonance": {
        "osc_path": "/param/a/filter/1/resonance",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Filter resonance. 0=smooth, high values=peaky/screaming.",
    },
}

# ─── AMP ENVELOPE (controls volume shape over time) ─────────────────────────
AMP_ENV = {
    "amp_attack": {
        "osc_path": "/param/a/amp_env/attack",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "How long it takes the sound to reach full volume. 0=instant, 1=very slow fade in.",
    },
    "amp_decay": {
        "osc_path": "/param/a/amp_env/decay",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "How fast volume drops from peak to sustain level.",
    },
    "amp_sustain": {
        "osc_path": "/param/a/amp_env/sustain",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Volume level held while key is down. 0=silent, 1=full.",
    },
    "amp_release": {
        "osc_path": "/param/a/amp_env/release",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "How long sound fades out after key is released. 0=cut off, 1=long fade.",
    },
}

# ─── FILTER ENVELOPE (modulates filter cutoff over time) ────────────────────
FILTER_ENV = {
    "filter_env_attack": {
        "osc_path": "/param/a/filter_env/attack",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Attack of the filter envelope.",
    },
    "filter_env_decay": {
        "osc_path": "/param/a/filter_env/decay",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Decay of the filter envelope.",
    },
    "filter_env_sustain": {
        "osc_path": "/param/a/filter_env/sustain",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Sustain of the filter envelope.",
    },
    "filter_env_release": {
        "osc_path": "/param/a/filter_env/release",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Release of the filter envelope.",
    },
    "filter_env_amount": {
        "osc_path": "/param/a/filter/1/env_amount",
        "range": (-1.0, 1.0),
        "normalized": True,
        "description": "How much the filter envelope modulates cutoff. 0.5=none, >0.5=opens, <0.5=closes.",
    },
}

# ─── LFO (Low Frequency Oscillator — creates movement/modulation) ────────────
LFO = {
    "lfo1_shape": {
        "osc_path": "/param/a/lfo/1/shape",
        "range": (0, 1),
        "normalized": True,
        "description": "LFO waveform. 0=Sine, 0.2=Triangle, 0.4=Sawtooth, 0.6=Square, 0.8=S&H, 1.0=Envelope",
        "type": "enum",
        "options": {
            "sine":      0.0,
            "triangle":  0.2,
            "sawtooth":  0.4,
            "square":    0.6,
            "random":    0.8,
        }
    },
    "lfo1_rate": {
        "osc_path": "/param/a/lfo/1/rate",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "LFO speed. 0=very slow, 1=very fast.",
    },
    "lfo1_depth": {
        "osc_path": "/param/a/lfo/1/magnitude",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "LFO intensity — how much it modulates the target.",
    },
}

# ─── GLOBAL ──────────────────────────────────────────────────────────────────
GLOBAL = {
    "master_volume": {
        "osc_path": "/param/a/volume",
        "range": (0.0, 1.0),
        "normalized": True,
        "description": "Scene A master volume.",
    },
    "scene_pitch": {
        "osc_path": "/param/a/pitch",
        "range": (-24, 24),
        "normalized": True,
        "description": "Global pitch offset for the scene.",
    },
}

# ─── FULL SCHEMA ─────────────────────────────────────────────────────────────
ALL_PARAMS = {}
ALL_PARAMS.update(OSC1)
ALL_PARAMS.update(OSC2)
ALL_PARAMS.update(FILTER)
ALL_PARAMS.update(AMP_ENV)
ALL_PARAMS.update(FILTER_ENV)
ALL_PARAMS.update(LFO)
ALL_PARAMS.update(GLOBAL)

# ─── DEFAULT PRESET (sine wave baseline) ─────────────────────────────────────
DEFAULT_PRESET = {
    "osc1_type":          0.0,   # sine
    "osc1_pitch":         0.5,   # center
    "osc1_octave":        0.5,   # center
    "osc1_level":         1.0,   # full
    "osc1_unison_voices": 0.0,   # 1 voice
    "osc1_unison_detune": 0.0,   # no detune
    "osc2_type":          0.0,
    "osc2_pitch":         0.5,
    "osc2_level":         0.0,   # silent
    "filter1_type":       0.0,   # LP12
    "filter1_cutoff":     0.8,   # mostly open
    "filter1_resonance":  0.0,   # no resonance
    "amp_attack":         0.0,   # instant
    "amp_decay":          0.3,
    "amp_sustain":        0.8,
    "amp_release":        0.3,
    "filter_env_attack":  0.0,
    "filter_env_decay":   0.3,
    "filter_env_sustain": 0.5,
    "filter_env_release": 0.3,
    "filter_env_amount":  0.5,   # neutral
    "lfo1_shape":         0.0,   # sine
    "lfo1_rate":          0.3,
    "lfo1_depth":         0.0,   # off
    "master_volume":      0.8,
    "scene_pitch":        0.5,   # center
}


def schema_for_prompt() -> str:
    """Returns a compact parameter description string for injection into Claude's system prompt."""
    lines = ["PARAMETER NAME | OSC PATH | RANGE 0-1 | DESCRIPTION"]
    lines.append("-" * 80)
    for name, p in ALL_PARAMS.items():
        desc = p["description"][:80]
        lines.append(f"{name:<30} | {p['osc_path']:<35} | {desc}")
    return "\n".join(lines)
