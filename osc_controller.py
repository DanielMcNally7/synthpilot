"""
SynthPilot — Surge XT OSC Controller
Sends parameter values to Surge XT via Open Sound Control.

Setup in Surge XT:
  Main Menu (hamburger) → OSC → Enable OSC
  Default port: 53280

SOURCE-CONFIRMED RULE (OpenSoundControl.cpp):
  Surge XT checks isFloat32() on every incoming message and discards
  non-floats with an error. ALL arguments must be OSC float32.

  - float_norm params → send normalized float 0.0–1.0
  - int params        → send raw integer cast to float (e.g. float(4) for Sine)
                        Surge internally converts via intScaledToFloat()
  - bool params       → send 0.0 (false) or 1.0 (true)
"""

import time
from pythonosc import udp_client
from parameter_schema import ALL_PARAMS, DEFAULT_PRESET

SURGE_HOST = "127.0.0.1"
SURGE_PORT = 53280


class SurgeOSCController:
    def __init__(self, host: str = SURGE_HOST, port: int = SURGE_PORT):
        self.host = host
        self.port = port
        self.client = udp_client.SimpleUDPClient(host, port)
        print(f"  OSC → Surge XT at {host}:{port}")

    def send_param(self, param_name: str, value):
        """Send a single parameter value to Surge XT."""
        if param_name not in ALL_PARAMS:
            print(f"  ⚠️  Unknown param: {param_name}")
            return

        schema = ALL_PARAMS[param_name]
        osc_path = schema["osc_path"]
        value_type = schema.get("value_type", "float_norm")

        if value_type in ("int", "bool"):
            # Must be float32 — Surge rejects OSC int type entirely.
            # int/bool: send raw integer value cast to float.
            # Surge's processBlockOSC calls intScaledToFloat() internally.
            self.client.send_message(osc_path, float(int(value)))
        else:
            # float_norm — clamp to 0.0–1.0
            self.client.send_message(osc_path, max(0.0, min(1.0, float(value))))

    def apply_preset(self, parameters: dict, delay_ms: int = 10):
        """
        Send all parameters in a preset to Surge XT.
        Small delay between messages to avoid overwhelming the OSC receiver.
        """
        sent = 0
        for param_name, value in parameters.items():
            self.send_param(param_name, value)
            sent += 1
            if delay_ms > 0:
                time.sleep(delay_ms / 1000.0)

        print(f"  ✓ Sent {sent} parameters to Surge XT")

    def reset_to_default(self):
        """Reset Surge XT to the default sine wave baseline."""
        print("  Resetting to default sine wave...")
        self.apply_preset(DEFAULT_PRESET)

    def test_connection(self) -> bool:
        """
        Send a test message to verify Surge XT is listening.
        Returns True if the message was sent without error (UDP — no ack).
        """
        try:
            self.client.send_message("/param/a/amp/volume", 0.8)
            return True
        except Exception as e:
            print(f"  ✗ OSC connection failed: {e}")
            return False

    def ping(self):
        """Quick connection check — prints status."""
        print(f"\n  Testing connection to Surge XT at {self.host}:{self.port}...")
        ok = self.test_connection()
        if ok:
            print("  ✓ Connected (message sent — check Surge XT responded)")
        else:
            print("  ✗ Failed — is Surge XT running with OSC enabled?")
        return ok
