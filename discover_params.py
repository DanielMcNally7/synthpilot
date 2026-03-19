#!/usr/bin/env python3
"""
SynthPilot — OSC Parameter Discovery
Listens for OSC messages from Surge XT so we can capture the exact parameter paths.

Usage:
    python3 discover_params.py

Then in Surge XT: wiggle any knob (filter cutoff, attack, etc.)
You'll see the exact OSC address printed here — that's what we need.

Surge XT sends OSC output on port 53280 by default.
"""

from pythonosc import dispatcher, osc_server
import argparse

LISTEN_PORT = 53280

def catch_all(address, *args):
    print(f"  {address}  →  {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=LISTEN_PORT)
    args = parser.parse_args()

    d = dispatcher.Dispatcher()
    d.set_default_handler(catch_all)

    server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", args.port), d)
    print(f"\n  Listening for Surge XT OSC on port {args.port}...")
    print("  Wiggle knobs in Surge XT — addresses will print here.")
    print("  Ctrl+C to stop.\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Done.")
