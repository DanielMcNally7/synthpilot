"""
Surge XT Parameter Schema — verified from SurgePatch.cpp source + live OSC discovery.

KEY INSIGHT: Some parameters use raw integer/float values, NOT normalized 0-1.
These are marked with value_type = "int" or "float_raw".
Most continuous params (cutoff, resonance, ADSR) use normalized 0.0-1.0.

OSC paths confirmed from source: fmt::format("{:c}/osc/{}/type", 'a'+sc, osc+1)
"""

# ─── OSCILLATOR TYPES (send as raw integer) ──────────────────────────────────
OSC_TYPES = {
    "Classic":    0,   # Bandlimited saw/square/triangle mix — default, often buzzy
    "Modern":     1,   # Extended classic with more waveform options
    "Wavetable":  2,   # Wavetable-based oscillator
    "Window":     3,   # Window-based wavetable
    "Sine":       4,   # Pure sine oscillator — use this for clean sine sounds
    "FM2":        5,   # 2-operator FM
    "FM3":        6,   # 3-operator FM
    "String":     7,   # Physical modeling string
    "Twist":      8,   # Mutable Instruments Plaits-based
    "Alias":      9,   # Aliasing/bitcrushed oscillator
    "SH_Noise":   10,  # Sample & hold noise
}

# ─── CLASSIC OSCILLATOR (type=0) param meanings ──────────────────────────────
# param1 = Sawtooth amount     (0=none, 0.5=50%, 1.0=full)  → set to 0 for no saw
# param2 = Pulse amount        (0=none, 1.0=full square)     → set to 0 for no pulse
# param3 = Triangle/Sine mix   (0=none, 1.0=full triangle)   → set to 0 for no tri
# param4 = Pulse width         (0=thin, 0.5=50% square)
# param5 = Hard sync amount    (semitones, 0.0=off)
# param6 = Unison detune (cents) ✓ confirmed
# param7 = Unison voices        ✓ confirmed (raw int 1-16 mapped to 0-1 normalized)

# ─── SINE OSCILLATOR (type=4) param meanings ─────────────────────────────────
# param1 = Feedback            (0=clean sine, higher=adds harmonics/distortion)
# param2 = FM from osc routing
# param3 = Internal low/highpass
# param6 = Unison detune (cents)
# param7 = Unison voices

# ─── FM2 OSCILLATOR (type=5) param meanings ──────────────────────────────────
# param1 = Ratio A (modulator frequency ratio)
# param2 = Ratio B
# param3 = M1 Amount (modulation depth 1)
# param4 = M2 Amount (modulation depth 2)
# param5 = Feedback

# ─── OSCILLATORS ─────────────────────────────────────────────────────────────
OSC1 = {
    "osc1_type": {
        "osc_path": "/param/a/osc/1/type",           # ✓ source confirmed
        "value_type": "int",
        "values": OSC_TYPES,
        "description": "Oscillator type. INTEGER: 0=Classic, 4=Sine, 5=FM2, 7=String. Use 4 for pure sine.",
    },
    "osc1_octave": {
        "osc_path": "/param/a/osc/1/octave",         # ✓ source confirmed
        "value_type": "int",
        "range": (-3, 3),
        "description": "Octave offset. INTEGER: -3 to +3. 0 = no shift.",
    },
    "osc1_pitch": {
        "osc_path": "/param/a/osc/1/pitch",          # ✓ confirmed
        "value_type": "float_norm",
        "description": "Pitch offset in semitones. 0.5=center (no shift). 0.0=-7st, 1.0=+7st.",
    },
    "osc1_param1": {
        "osc_path": "/param/a/osc/1/param1",         # ✓ confirmed
        "value_type": "float_norm",
        "description": "Classic: Sawtooth amount (0=none, 1=full). Sine: Feedback (0=clean). FM2: Ratio A.",
    },
    "osc1_param2": {
        "osc_path": "/param/a/osc/1/param2",         # ✓ confirmed
        "value_type": "float_norm",
        "description": "Classic: Pulse amount (0=none, 1=full square). FM2: Ratio B.",
    },
    "osc1_param3": {
        "osc_path": "/param/a/osc/1/param3",         # ✓ confirmed
        "value_type": "float_norm",
        "description": "Classic: Triangle/Sine mix (0=none, 1=full triangle). FM2: M1 depth.",
    },
    "osc1_param4": {
        "osc_path": "/param/a/osc/1/param4",         # ✓ confirmed
        "value_type": "float_norm",
        "description": "Classic: Pulse width (0=thin, 0.5=square). FM2: M2 depth.",
    },
    "osc1_param5": {
        "osc_path": "/param/a/osc/1/param5",         # ✓ confirmed
        "value_type": "float_norm",
        "description": "Classic: Hard sync in semitones (0=off). FM2: Feedback.",
    },
    "osc1_unison_detune": {
        "osc_path": "/param/a/osc/1/param6",         # ✓ confirmed = cents detune
        "value_type": "float_norm",
        "description": "Unison detune spread in cents. 0=no detune, 1=maximum spread.",
    },
    "osc1_unison_voices": {
        "osc_path": "/param/a/osc/1/param7",         # ✓ confirmed = voice count
        "value_type": "float_norm",
        "description": "Unison voice count. Normalized: 0.0=1 voice, 1.0=16 voices.",
    },
    "osc1_level": {
        "osc_path": "/param/a/mixer/osc1/volume",    # ✓ confirmed
        "value_type": "float_norm",
        "description": "Oscillator 1 volume in mixer. 0.89 ≈ 0dB. 0=silent.",
    },
    "osc1_keytrack": {
        "osc_path": "/param/a/osc/1/keytrack",       # ✓ source confirmed
        "value_type": "bool",
        "description": "Pitch follows keyboard. 1=on (normal), 0=off (drone).",
    },
}

OSC2 = {
    "osc2_type": {
        "osc_path": "/param/a/osc/2/type",           # ✓ source confirmed
        "value_type": "int",
        "values": OSC_TYPES,
        "description": "Oscillator 2 type. Same values as osc1_type.",
    },
    "osc2_pitch": {
        "osc_path": "/param/a/osc/2/pitch",
        "value_type": "float_norm",
        "description": "Oscillator 2 pitch offset. 0.5=center. Good for detuned layers.",
    },
    "osc2_param1": {
        "osc_path": "/param/a/osc/2/param1",
        "value_type": "float_norm",
        "description": "Osc 2 param 1. Same meaning as osc1 depending on type.",
    },
    "osc2_param2": {
        "osc_path": "/param/a/osc/2/param2",
        "value_type": "float_norm",
        "description": "Osc 2 param 2.",
    },
    "osc2_param6": {
        "osc_path": "/param/a/osc/2/param6",
        "value_type": "float_norm",
        "description": "Osc 2 unison detune.",
    },
    "osc2_param7": {
        "osc_path": "/param/a/osc/2/param7",
        "value_type": "float_norm",
        "description": "Osc 2 unison voices.",
    },
    "osc2_level": {
        "osc_path": "/param/a/mixer/osc2/volume",    # ✓ confirmed
        "value_type": "float_norm",
        "description": "Oscillator 2 volume. 0=silent (off by default).",
    },
}

OSC3 = {
    "osc3_type": {
        "osc_path": "/param/a/osc/3/type",
        "value_type": "int",
        "values": OSC_TYPES,
        "description": "Oscillator 3 type.",
    },
    "osc3_level": {
        "osc_path": "/param/a/mixer/osc3/volume",    # ✓ confirmed
        "value_type": "float_norm",
        "description": "Oscillator 3 volume. 0=silent.",
    },
}

# ─── NOISE & MIXER ────────────────────────────────────────────────────────────
MIXER = {
    "noise_level": {
        "osc_path": "/param/a/mixer/noise/volume",   # ✓ confirmed
        "value_type": "float_norm",
        "description": "Noise oscillator volume. 0=off. Add for texture/breathiness.",
    },
    "noise_color": {
        "osc_path": "/param/a/mixer/noise/color",    # ✓ confirmed
        "value_type": "float_norm",
        "description": "Noise color. 0=white noise, 1=colored/pink noise.",
    },
    "ring_mod_1x2": {
        "osc_path": "/param/a/mixer/rm1x2/volume",   # ✓ confirmed
        "value_type": "float_norm",
        "description": "Ring modulation of osc 1 × osc 2. 0=off. Adds metallic/bell tones.",
    },
    "prefilter_gain": {
        "osc_path": "/param/a/mixer/prefilter_gain", # ✓ confirmed
        "value_type": "float_norm",
        "description": "Gain before filters. Boost for overdrive/saturation.",
    },
}

# ─── FILTER ──────────────────────────────────────────────────────────────────
# Filter types (send as raw integer):
# 0=LP12, 1=LP24, 2=LP Moog24, 3=LP6, 4=LP OD, 5=LP BP, 6=LP BP2
# 7=HP12, 8=HP24, 9=HP6, 10=HP Butter
# 11=BP12, 12=BP24, 13=Notch12, 14=Notch24
# 15=Comb+, 16=S&H

FILTER_TYPES = {
    "LP12":   0,   "LP24":   1,   "LP_Moog": 2,
    "HP12":   7,   "HP24":   8,
    "BP12":   11,  "BP24":   12,
    "Notch":  13,
    "OFF":    -1,
}

FILTER = {
    "filter1_type": {
        "osc_path": "/param/a/filter/1/type",        # ✓ source confirmed
        "value_type": "int",
        "values": FILTER_TYPES,
        "description": "Filter 1 type. INT: 0=LP12, 1=LP24, 7=HP12, 11=BP12, 13=Notch.",
    },
    "filter1_cutoff": {
        "osc_path": "/param/a/filter/1/cutoff",      # ✓ source confirmed
        "value_type": "float_norm",
        "description": "Filter 1 cutoff. 0=very dark/closed, 1=wide open/bright.",
    },
    "filter1_resonance": {
        "osc_path": "/param/a/filter/1/resonance",   # ✓ source confirmed
        "value_type": "float_norm",
        "description": "Filter 1 resonance. 0=flat, 0.7=vocal peak, >0.9=self-oscillation.",
    },
    "filter1_feg_amount": {
        "osc_path": "/param/a/filter/1/feg_amount",  # ✓ confirmed
        "value_type": "float_norm",
        "description": "Filter envelope amount on filter 1. 0.5=neutral, >0.5=opens, <0.5=closes.",
    },
    "filter2_type": {
        "osc_path": "/param/a/filter/2/type",        # ✓ source confirmed
        "value_type": "int",
        "values": FILTER_TYPES,
        "description": "Filter 2 type.",
    },
    "filter2_cutoff": {
        "osc_path": "/param/a/filter/2/cutoff",      # ✓ confirmed
        "value_type": "float_norm",
        "description": "Filter 2 cutoff.",
    },
    "filter2_resonance": {
        "osc_path": "/param/a/filter/2/resonance",
        "value_type": "float_norm",
        "description": "Filter 2 resonance.",
    },
    "filter2_feg_amount": {
        "osc_path": "/param/a/filter/2/feg_amount",  # ✓ confirmed
        "value_type": "float_norm",
        "description": "Filter envelope amount on filter 2.",
    },
    "filter_config": {
        "osc_path": "/param/a/filter/config",        # ✓ confirmed
        "value_type": "int",
        "description": "Filter routing. INT: 0=Serial1, 1=Serial2, 2=Serial3, 3=Dual1, 4=Dual2, 5=Stereo, 6=Ring.",
    },
    "filter_feedback": {
        "osc_path": "/param/a/filter/feedback",      # ✓ confirmed
        "value_type": "float_norm",
        "description": "Filter feedback. 0=off. Adds resonant character and self-oscillation tendency.",
    },
    "highpass": {
        "osc_path": "/param/a/highpass",             # ✓ confirmed
        "value_type": "float_norm",
        "description": "Scene high-pass filter. 0=off (passes all). Removes rumble/sub.",
    },
}

# ─── WAVESHAPER ───────────────────────────────────────────────────────────────
WAVESHAPER = {
    "waveshaper_drive": {
        "osc_path": "/param/a/waveshaper/drive",     # ✓ confirmed
        "value_type": "float_norm",
        "description": "Waveshaper drive. Adds harmonic saturation. 0=off, 0.5=moderate, 1.0=heavy.",
    },
    "waveshaper_type": {
        "osc_path": "/param/a/waveshaper/type",      # ✓ confirmed
        "value_type": "int",
        "description": "Waveshaper curve. INT: 0=Soft, 1=Hard, 2=Asymmetric, 3=Sine, 4=Digital.",
    },
}

# ─── AMP ENVELOPE (aeg) — CONFIRMED from live discovery ──────────────────────
AMP_ENV = {
    "amp_attack": {
        "osc_path": "/param/a/aeg/attack",           # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "Volume attack. 0=instant on. 0.25=~30ms. 0.5=~300ms. 1.0=very slow.",
    },
    "amp_decay": {
        "osc_path": "/param/a/aeg/decay",            # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "Volume decay after attack peak. 0=instant. 0.5=~200ms. 1.0=very long.",
    },
    "amp_sustain": {
        "osc_path": "/param/a/aeg/sustain",          # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "Volume level while key held. 0=silent after decay. 1.0=full (no decay effect).",
    },
    "amp_release": {
        "osc_path": "/param/a/aeg/release",          # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "Volume fade after key released. 0=cut off. 0.3=~80ms. 0.7=~2s. 1.0=very long.",
    },
}

# ─── FILTER ENVELOPE (feg) — CONFIRMED from live discovery ───────────────────
FILTER_ENV = {
    "filter_env_attack": {
        "osc_path": "/param/a/feg/attack",           # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "Filter envelope attack. Controls how fast cutoff sweeps open.",
    },
    "filter_env_decay": {
        "osc_path": "/param/a/feg/decay",            # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "Filter envelope decay. How fast cutoff returns to sustain level.",
    },
    "filter_env_sustain": {
        "osc_path": "/param/a/feg/sustain",          # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "Filter envelope sustain level.",
    },
    "filter_env_release": {
        "osc_path": "/param/a/feg/release",          # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "Filter envelope release time.",
    },
}

# ─── LFO (vlfo) — CONFIRMED from live discovery ──────────────────────────────
LFO_TYPES = {
    "Sine": 0.0, "Triangle": 1.0, "Sawtooth": 2.0,
    "Sawtooth_Rev": 3.0, "Square": 4.0, "Random_SH": 5.0,
}

LFO = {
    "lfo1_type": {
        "osc_path": "/param/a/vlfo/1/type",          # ✓ confirmed
        "value_type": "int",
        "description": "LFO waveform. INT: 0=Sine, 1=Triangle, 2=Saw, 4=Square, 5=S&H.",
    },
    "lfo1_rate": {
        "osc_path": "/param/a/vlfo/1/rate",          # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "LFO speed. 0=very slow (0.008Hz), 0.46=~1.3Hz, 1.0=very fast.",
    },
    "lfo1_depth": {
        "osc_path": "/param/a/vlfo/1/amplitude",     # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "LFO depth/intensity. 0=no modulation. 1.0=maximum modulation.",
    },
    "lfo1_deform": {
        "osc_path": "/param/a/vlfo/1/deform",        # ✓ confirmed
        "value_type": "float_norm",
        "description": "LFO waveform deformation/shape morph.",
    },
    "lfo1_phase": {
        "osc_path": "/param/a/vlfo/1/phase",         # ✓ confirmed
        "value_type": "float_norm",
        "description": "LFO start phase offset.",
    },
    "lfo1_eg_attack": {
        "osc_path": "/param/a/vlfo/1/eg/attack",     # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "LFO fade-in time. How long before LFO reaches full depth. Great for slow vibrato.",
    },
    "lfo1_eg_hold": {
        "osc_path": "/param/a/vlfo/1/eg/hold",       # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "How long LFO stays at full depth before decaying.",
    },
    "lfo1_eg_decay": {
        "osc_path": "/param/a/vlfo/1/eg/decay",      # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "LFO modulation decay after hold.",
    },
    "lfo1_eg_sustain": {
        "osc_path": "/param/a/vlfo/1/eg/sustain",    # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "LFO modulation sustain level while key held.",
    },
    "lfo1_eg_release": {
        "osc_path": "/param/a/vlfo/1/eg/release",    # ✓ CONFIRMED
        "value_type": "float_norm",
        "description": "LFO modulation release after key up.",
    },
}

# ─── SCENE / GLOBAL ──────────────────────────────────────────────────────────
SCENE = {
    "scene_pitch": {
        "osc_path": "/param/a/pitch",                # ✓ source confirmed
        "value_type": "float_norm",
        "description": "Scene pitch offset in semitones. 0.5=center.",
    },
    "scene_octave": {
        "osc_path": "/param/a/octave",               # ✓ source confirmed
        "value_type": "int",
        "description": "Scene octave offset. INT: -3 to +3.",
    },
    "portamento": {
        "osc_path": "/param/a/portamento",           # ✓ source confirmed
        "value_type": "float_norm",
        "description": "Portamento/glide time. 0=off (instant pitch change). Higher=slower glide.",
    },
    "fm_depth": {
        "osc_path": "/param/a/osc/fm_depth",         # ✓ source confirmed
        "value_type": "float_norm",
        "description": "FM modulation depth from oscillator routing.",
    },
    "osc_drift": {
        "osc_path": "/param/a/osc/drift",            # ✓ confirmed
        "value_type": "float_norm",
        "description": "Pitch instability across oscillators. 0=perfect tuning. Higher=analog drift.",
    },
    "amp_volume": {
        "osc_path": "/param/a/amp/volume",           # ✓ confirmed
        "value_type": "float_norm",
        "description": "Scene output volume. 0.97 ≈ -0.7dB. Keep this high.",
    },
    "amp_pan": {
        "osc_path": "/param/a/amp/pan",              # ✓ confirmed
        "value_type": "float_norm",
        "description": "Pan position. 0=hard left, 0.5=center, 1=hard right.",
    },
    "global_volume": {
        "osc_path": "/param/global/volume",          # ✓ confirmed
        "value_type": "float_norm",
        "description": "Master output volume.",
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
ALL_PARAMS.update(SCENE)

# ─── DEFAULT PRESET — pure sine wave baseline ─────────────────────────────────
DEFAULT_PRESET = {
    # Osc 1 — Sine oscillator, single voice, centered
    "osc1_type":          4,      # Sine oscillator (INTEGER)
    "osc1_octave":        0,      # No octave shift (INTEGER)
    "osc1_pitch":         0.5,    # Center
    "osc1_param1":        0.0,    # No feedback
    "osc1_param2":        0.5,
    "osc1_param3":        0.5,
    "osc1_param4":        0.5,
    "osc1_param5":        0.0,
    "osc1_unison_detune": 0.0,    # No detune
    "osc1_unison_voices": 0.0,    # 1 voice
    "osc1_level":         0.89,   # ~0dB
    "osc1_keytrack":      1,      # Follows keyboard (INTEGER)
    # Osc 2 — off
    "osc2_type":          4,
    "osc2_pitch":         0.5,
    "osc2_param1":        0.0,
    "osc2_param2":        0.5,
    "osc2_param6":        0.0,
    "osc2_param7":        0.0,
    "osc2_level":         0.0,    # Silent
    # Osc 3 — off
    "osc3_type":          4,
    "osc3_level":         0.0,    # Silent
    # Mixer
    "noise_level":        0.0,
    "noise_color":        0.5,
    "ring_mod_1x2":       0.0,
    "prefilter_gain":     0.5,
    # Filters — wide open (not filtering the sine)
    "filter1_type":       1,      # LP24 (INTEGER)
    "filter1_cutoff":     1.0,    # Fully open
    "filter1_resonance":  0.0,
    "filter1_feg_amount": 0.5,    # Neutral
    "filter2_type":       1,      # LP24 (INTEGER)
    "filter2_cutoff":     1.0,
    "filter2_resonance":  0.0,
    "filter2_feg_amount": 0.5,
    "filter_config":      0,      # Serial 1 (INTEGER)
    "filter_feedback":    0.0,
    "highpass":           0.0,
    # Waveshaper — neutral
    "waveshaper_drive":   0.44,
    "waveshaper_type":    0,      # Soft (INTEGER)
    # Amp envelope — sustain-heavy, short release
    "amp_attack":         0.0,
    "amp_decay":          0.3,
    "amp_sustain":        1.0,
    "amp_release":        0.3,
    # Filter envelope — neutral
    "filter_env_attack":  0.0,
    "filter_env_decay":   0.5,
    "filter_env_sustain": 0.5,
    "filter_env_release": 0.3,
    # LFO — off
    "lfo1_type":          0,      # Sine (INTEGER)
    "lfo1_rate":          0.46,
    "lfo1_depth":         0.0,    # Off
    "lfo1_deform":        0.5,
    "lfo1_phase":         0.0,
    "lfo1_eg_attack":     0.0,
    "lfo1_eg_hold":       0.0,
    "lfo1_eg_decay":      0.5,
    "lfo1_eg_sustain":    1.0,
    "lfo1_eg_release":    0.5,
    # Scene
    "scene_pitch":        0.5,
    "scene_octave":       0,      # No shift (INTEGER)
    "portamento":         0.0,
    "fm_depth":           0.5,
    "osc_drift":          0.0,
    "amp_volume":         0.97,
    "amp_pan":            0.5,
    "global_volume":      0.91,
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
