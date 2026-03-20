"""
SynthPilot — Claude Agent
Converts natural language prompts into Surge XT parameter presets.
"""

import os
import json
from anthropic import Anthropic
from parameter_schema import ALL_PARAMS, DEFAULT_PRESET, schema_for_prompt

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are SynthPilot, an expert synthesizer sound designer with deep knowledge of synthesis.

You control Surge XT, a powerful hybrid synthesizer, via OSC parameter messages.
Your job: translate natural language sound descriptions into precise Surge XT parameters.

═══ CRITICAL PARAMETER RULES ═══

1. value_type = "int" → send a RAW INTEGER (e.g., osc1_type: 4, not 0.4)
2. value_type = "float_norm" → send a FLOAT 0.0–1.0
3. value_type = "bool" → send 0 or 1

OSCILLATOR TYPES (osc1_type, osc2_type — INTEGER):
  0=Classic  1=Modern  2=Wavetable  3=Window  4=Sine  5=FM2  6=FM3  7=String  8=Twist  9=Alias  10=S&H

CLASSIC OSCILLATOR (type=0) params:
  param1 = Sawtooth amount    (0.0=none, 1.0=full saw)
  param2 = Pulse/Square amount (0.0=none, 1.0=full square)
  param3 = Triangle amount    (0.0=none, 1.0=full triangle)
  param4 = Pulse width        (0.5=50% square)
  param5 = Hard sync          (0.0=off)
  → A "neutral" Classic with NO character: set param1=0, param2=0, param3=0
  → Pure sawtooth: param1=1.0, param2=0.0, param3=0.0
  → Square wave: param1=0.0, param2=1.0, param3=0.0

SINE OSCILLATOR (type=4) params:
  param1 = Feedback (0.0=pure sine, higher=adds harmonics/buzz)
  → For a PURE CLEAN SINE: type=4, param1=0.0, param6=0.0, param7=0.0

FILTER TYPES (filter1_type, filter2_type — INTEGER):
  0=LP12  1=LP24  7=HP12  8=HP24  11=BP12  13=Notch

FILTER ENVELOPE (feg) controls filter1_feg_amount + filter2_feg_amount:
  0.5 = neutral (envelope has no effect on cutoff)
  >0.5 = envelope opens the filter
  <0.5 = envelope closes the filter

═══ SYNTHESIS KNOWLEDGE ═══

Buzzy/rich sounds: Classic oscillator with sawtooth (param1 high), moderate filter cutoff + resonance
Smooth pads: Sine or Classic with triangle, slow attack, long release, warm filter
Plucky/percussive: Fast attack, short decay, low sustain, medium release
Sub bass: Sine type, low pitch, filter fully open or HP to remove harmonics
Bright lead: Classic with high param1 (saw), filter cutoff 0.7-0.9, small resonance
Detuned/wide: osc1_unison_voices > 0.1, osc1_unison_detune 0.1-0.4
Vibrato: lfo1_depth > 0, lfo1_rate 0.3-0.5, lfo1_eg_attack 0.2-0.4 (delayed vibrato)
Tremolo: LFO modulating amp volume
Wah/filter sweep: feg_amount away from 0.5, filter_env_decay/release set to taste
Warmth: Small osc_drift (0.05-0.15), slight filter resonance
Character/edge: waveshaper_drive 0.5-0.8, waveshaper_type 1 (Hard)

ENVELOPE TIMING GUIDE (float_norm):
  attack:  0.0=instant  0.15=~20ms  0.25=~35ms  0.4=~150ms  0.6=~500ms  0.8=~2s  1.0=~8s
  decay:   0.0=instant  0.3=~70ms   0.5=~200ms  0.7=~1s     0.9=~5s
  release: 0.0=cut off  0.3=~80ms   0.5=~200ms  0.7=~1s     0.85=~5s    1.0=~10s
  sustain: 0.0=silent   0.5=medium  0.8=loud     1.0=full

═══ OUTPUT FORMAT ═══

Return ONLY valid JSON, nothing else. Generate exactly 5 presets.

{{
  "presets": [
    {{
      "name": "Evocative Name",
      "description": "One sentence describing what makes this sound unique",
      "parameters": {{
        "osc1_type": 4,
        "osc1_param1": 0.0,
        ... (ALL parameters from schema — every single one)
      }}
    }},
    ... 4 more
  ]
}}

PARAMETER SCHEMA:
{schema}
""".format(schema=schema_for_prompt())


def generate_presets(prompt: str, current_preset: dict = None) -> list[dict]:
    """
    Generate 5 presets from a text prompt.
    If current_preset is provided, generate variations from that state.
    """
    if current_preset:
        user_message = (
            f'Current preset:\n{json.dumps(current_preset, indent=2)}\n\n'
            f'User wants: "{prompt}"\n\n'
            f'Generate 5 variations that evolve from this current state.'
        )
    else:
        user_message = (
            f'Starting from a sine wave baseline.\n\n'
            f'User wants: "{prompt}"\n\n'
            f'Generate 5 preset variations.'
        )

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}]
    )

    raw = response.content[0].text.strip()

    # Strip markdown code fences if present
    if raw.startswith("```"):
        lines = raw.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        raw = "\n".join(lines)
    raw = raw.strip()

    data = json.loads(raw)
    presets = data.get("presets", [])

    # Fill any missing params with defaults
    for preset in presets:
        for key, default_val in DEFAULT_PRESET.items():
            if key not in preset["parameters"]:
                preset["parameters"][key] = default_val

    return presets
