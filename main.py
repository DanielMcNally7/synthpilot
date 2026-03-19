#!/usr/bin/env python3
"""
SynthPilot — AI-powered Surge XT synthesizer control
Describe a sound in plain English. Claude sets the knobs.

Usage:
    python main.py              — start interactive session
    python main.py --ping       — test Surge XT OSC connection
    python main.py --reset      — reset Surge XT to sine wave default
"""

import os
import sys
import json
import argparse
from dotenv import load_dotenv

load_dotenv()

from synth_agent import generate_presets
from osc_controller import SurgeOSCController
from parameter_schema import DEFAULT_PRESET

# ─── DISPLAY ─────────────────────────────────────────────────────────────────

BANNER = """
╔═══════════════════════════════════════════════╗
║           🎛  S Y N T H P I L O T            ║
║    Describe sounds. Claude sets the knobs.    ║
╚═══════════════════════════════════════════════╝
"""

def print_presets(presets: list[dict]):
    print()
    for i, preset in enumerate(presets, 1):
        name = preset.get("name", f"Preset {i}")
        desc = preset.get("description", "")
        print(f"  {i}.  {name}")
        print(f"      {desc}")
    print()

def print_params(parameters: dict):
    """Show the key parameters of the selected preset."""
    highlights = {
        "osc1_type": "Osc 1 type",
        "osc1_unison_voices": "Unison voices",
        "osc1_unison_detune": "Detune",
        "filter1_type": "Filter type",
        "filter1_cutoff": "Filter cutoff",
        "filter1_resonance": "Resonance",
        "amp_attack": "Attack",
        "amp_decay": "Decay",
        "amp_sustain": "Sustain",
        "amp_release": "Release",
    }
    print("\n  ── Parameters ──────────────────────────")
    for key, label in highlights.items():
        val = parameters.get(key, 0.0)
        bar = "█" * int(val * 20) + "░" * (20 - int(val * 20))
        print(f"  {label:<20} {bar}  {val:.2f}")
    print()


# ─── MAIN LOOP ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="SynthPilot — AI synth control")
    parser.add_argument("--ping", action="store_true", help="Test Surge XT connection")
    parser.add_argument("--reset", action="store_true", help="Reset Surge XT to defaults")
    parser.add_argument("--host", default="127.0.0.1", help="Surge XT OSC host")
    parser.add_argument("--port", type=int, default=53280, help="Surge XT OSC port")
    args = parser.parse_args()

    # Check API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("✗ ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key.")
        sys.exit(1)

    osc = SurgeOSCController(host=args.host, port=args.port)

    if args.ping:
        osc.ping()
        return

    if args.reset:
        osc.reset_to_default()
        print("  ✓ Reset to sine wave default.")
        return

    print(BANNER)
    print("  Make sure Surge XT is open with OSC enabled:")
    print("  Main Menu → OSC → Enable OSC (port 53280)\n")

    current_preset = None   # tracks the currently applied preset for iteration
    current_params = dict(DEFAULT_PRESET)

    while True:
        try:
            if current_preset:
                prompt = input("  ✦  Iterate (describe changes) or [n]ew / [q]uit: ").strip()
            else:
                prompt = input("  🎛  Describe the sound you want: ").strip()

            if not prompt:
                continue

            if prompt.lower() in ("q", "quit", "exit"):
                print("\n  Later.\n")
                break

            if prompt.lower() in ("n", "new"):
                current_preset = None
                current_params = dict(DEFAULT_PRESET)
                osc.reset_to_default()
                print("  ✓ Reset to sine wave. Start fresh.\n")
                continue

            if prompt.lower() in ("r", "reset"):
                osc.reset_to_default()
                current_params = dict(DEFAULT_PRESET)
                current_preset = None
                print("  ✓ Reset.\n")
                continue

            # Generate presets
            print(f"\n  Generating 5 presets", end="", flush=True)
            if current_preset:
                print(f" (iterating from '{current_preset['name']}')", end="", flush=True)
            print("...", end="", flush=True)

            try:
                presets = generate_presets(
                    prompt=prompt,
                    current_preset=current_params if current_preset else None
                )
            except Exception as e:
                print(f"\n  ✗ Claude error: {e}")
                continue

            print(" ✓\n")
            print_presets(presets)

            # User picks one
            while True:
                choice = input("  Pick one (1–5) or [s]kip: ").strip().lower()
                if choice == "s":
                    break
                if choice.isdigit() and 1 <= int(choice) <= 5:
                    idx = int(choice) - 1
                    selected = presets[idx]
                    current_preset = selected
                    current_params = selected["parameters"]

                    print(f"\n  → {selected['name']}")
                    print_params(current_params)
                    print("  Sending to Surge XT...")
                    osc.apply_preset(current_params)
                    print()
                    break
                else:
                    print("  Enter 1–5 or 's' to skip.")

        except KeyboardInterrupt:
            print("\n\n  Later.\n")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
