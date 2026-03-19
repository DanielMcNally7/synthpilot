#!/usr/bin/env python3
"""
Quick OSC test — sends one obvious parameter change to Surge XT.
Watch the filter cutoff knob in Surge XT while running this.
If it moves, OSC is working.
"""
import time
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 53280)

print("Sending filter cutoff sweep to Surge XT...")
print("Watch the filter 2 cutoff knob — it should sweep low → high\n")

for i in range(11):
    val = i / 10.0
    client.send_message("/param/a/filter/2/cutoff", val)
    print(f"  /param/a/filter/2/cutoff → {val:.1f}")
    time.sleep(0.4)

print("\nDone. Did the knob move?")
