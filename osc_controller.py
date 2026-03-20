"""
SynthPilot — Surge XT OSC Controller
Sends parameter values to Surge XT via Open Sound Control.

Setup in Surge XT:
  Main Menu (hamburger) → OSC → Enable OSC
  Default port: 53280

Parameter paths are verified against Surge XT 1.3+ OSC implementation.
If a parameter doesn't respond, right-click it in Surge XT and look at
the OSC address shown in the context menu to get the exact path.
"""

import time
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder
from parameter_schema import ALL_PARAMS

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

        if value_type == "int" or value_type == "bool":
            # Send as raw integer — Surge XT expects this for type selectors
            self.client.send_message(osc_path, int(value))
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
        from parameter_schema import DEFAULT_PRESET
        print("  Resetting to default sine wave...")
        self.apply_preset(DEFAULT_PRESET)

    def test_connection(self) -> bool:
        """
        Send a test message to verify Surge XT is listening.
        Sends master volume to a safe value and back.
        """
        try:
            self.client.send_message("/param/a/volume", 0.8)
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
