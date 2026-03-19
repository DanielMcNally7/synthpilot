"""
SynthPilot — Claude Agent
Converts natural language prompts into Surge XT parameter presets.
"""

import os
import json
from anthropic import Anthropic
from parameter_schema import ALL_PARAMS, DEFAULT_PRESET, schema_for_prompt

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are SynthPilot, an expert synthesizer sound designer.
Your job is to translate natural language descriptions of sounds into precise synthesizer parameters for Surge XT.

You always start from a sine wave foundation and build up from there.
You have deep knowledge of synthesis: oscillators, filters, envelopes, LFOs, and how they interact to create timbre.

When given a sound description, you generate EXACTLY 5 preset variations.
Each preset interprets the description slightly differently — different oscillator choices, filter settings, envelope shapes.
This gives the musician real creative options, not 5 copies of the same thing.

When given a current preset + an iteration request, you generate 5 variations that evolve from the current state.

PARAMETER SCHEMA (all values normalized 0.0–1.0 unless noted):
{schema}

RULES:
1. Always return valid JSON — nothing else, no explanation outside the JSON.
2. Generate exactly 5 presets.
3. Each preset must include ALL parameters from the schema.
4. Parameter values must be floats between 0.0 and 1.0.
5. Name each preset something evocative (2-4 words).
6. Write a 1-sentence description of what makes each one unique.
7. Think like a musician: attack/release shape matters, filter openness affects brightness, detune adds width.

RESPONSE FORMAT:
{{
  "presets": [
    {{
      "name": "Dirty Unison Lead",
      "description": "Heavy detuned saws with a mid filter and punchy envelope",
      "parameters": {{
        "osc1_type": 0.28,
        "osc1_pitch": 0.5,
        ... (all params)
      }}
    }},
    ... (4 more)
  ]
}}
""".format(schema=schema_for_prompt())


def generate_presets(prompt: str, current_preset: dict = None) -> list[dict]:
    """
    Given a text prompt (and optionally a current preset for iteration),
    return a list of 5 preset dicts from Claude.
    """
    if current_preset:
        user_message = f"""Current preset state:
{json.dumps(current_preset, indent=2)}

User request: "{prompt}"

Generate 5 variations that evolve from this current state based on the request."""
    else:
        user_message = f"""Starting from a basic sine wave.

User request: "{prompt}"

Generate 5 preset variations that match this description."""

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    raw = response.content[0].text.strip()

    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    data = json.loads(raw)
    presets = data.get("presets", [])

    # Ensure every preset has all params (fill missing with defaults)
    for preset in presets:
        for key, default_val in DEFAULT_PRESET.items():
            if key not in preset["parameters"]:
                preset["parameters"][key] = default_val

    return presets


def explain_preset(preset: dict) -> str:
    """Ask Claude to explain what a preset does in plain English for a musician."""
    params = preset["parameters"]
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"""Explain this synthesizer preset to a musician in plain English.
Focus on: what the oscillator/filter/envelope settings will sound like.
Keep it to 2-3 sentences, no jargon.

Preset name: {preset['name']}
Parameters: {json.dumps(params, indent=2)}"""
        }]
    )
    return response.content[0].text.strip()
