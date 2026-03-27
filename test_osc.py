#!/usr/bin/env python3
"""
SynthPilot — OSC connection test
Sends confirmed parameter changes to Surge XT.
Watch the knobs move in real time.
"""
import time
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 53280)

def sweep(path, label, low=0.0, high=1.0, steps=8, delay=0.3):
    print(f"\n  {label} ({path})")
    for i in range(steps + 1):
        val = low + (high - low) * (i / steps)
        client.send_message(path, val)
        bar = "█" * i + "░" * (steps - i)
        print(f"  [{bar}] {val:.2f}", end="\r")
        time.sleep(delay)
    print()

print("\n  SynthPilot OSC Test")
print("  Watch these knobs move in Surge XT...\n")

# Test confirmed paths
sweep("/param/a/filter/2/cutoff",  "Filter 2 Cutoff  — should sweep dark → bright")
sweep("/param/a/aeg/attack",       "Amp Attack        — should sweep instant → slow")
sweep("/param/a/aeg/release",      "Amp Release       — should sweep short → long")
sweep("/param/a/vlfo/1/rate",      "LFO 1 Rate        — should sweep slow → fast")
sweep("/param/a/mixer/osc1/volume","Osc 1 Volume      — should sweep silent → full")

print("\n  Did the knobs move? y/n: ", end="")
result = input().strip().lower()
if result == "y":
    print("  ✓ OSC is working. Run python3 main.py to start.\n")
else:
    print("  ✗ Something's wrong. Check Surge XT has OSC enabled (Main Menu → OSC → Enable OSC)\n")

# ─── Pitch bend range test ────────────────────────────────────────────────────
print("\n  ── Pitch Bend Range Test ─────────────────────────────")
print("  Setting pitch bend range to 0 semitones (both wheels should go dead)...")
client.send_message("/param/a/pitchbend_up",   float(0))
client.send_message("/param/a/pitchbend_down", float(0))
time.sleep(1.0)
print("  Try your pitch wheel now — it should do NOTHING.")
input("  Press Enter to continue...")

print("\n  Setting pitch bend range to 12 semitones (one full octave)...")
client.send_message("/param/a/pitchbend_up",   float(12))
client.send_message("/param/a/pitchbend_down", float(12))
time.sleep(1.0)
print("  Try your pitch wheel now — it should bend a full octave.")
input("  Press Enter to continue...")

print("\n  Restoring pitch bend range to 2 semitones (default)...")
client.send_message("/param/a/pitchbend_up",   float(2))
client.send_message("/param/a/pitchbend_down", float(2))
print("  ✓ Done. Pitch bend range restored to ±2 semitones.\n")
