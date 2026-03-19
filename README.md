# 🎛 SynthPilot

> Describe the sound you want. Claude sets the knobs.

SynthPilot is a CLI tool that connects Claude (Anthropic) to Surge XT via OSC. Type a plain-English description of a sound, get 5 synthesizer presets back, pick one, hear it, and keep iterating.

---

## How It Works

```
You type a prompt → Claude generates 5 presets (JSON params) → 
SynthPilot sends them to Surge XT via OSC → You hear the sound
```

Always starts from a sine wave. Each iteration builds on the last selected preset.

---

## Setup

### 1. Install Surge XT
Download free from [surge-synthesizer.github.io](https://surge-synthesizer.github.io)

Enable OSC in Surge XT:
```
Main Menu (hamburger icon) → OSC → Enable OSC
```
Default port: **53280** — leave it as-is.

### 2. Clone this repo
```bash
git clone https://github.com/DanielMcNally7/synthpilot.git
cd synthpilot
```

### 3. Install Python dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Add your Anthropic API key
```bash
cp .env.example .env
# Open .env and paste your API key from console.anthropic.com
```

### 5. Run it
```bash
python3 main.py
```

---

## Usage

```
🎛  Describe the sound you want: buzzy synth with detuning that slowly fades off

  Generating 5 presets... ✓

  1.  Dirty Unison Lead
      Heavy detuned saws with a mid filter and punchy envelope

  2.  Soft Buzz Pad
      Slight detune on a square, longer release, warm low-pass

  3.  Aggressive Buzz
      Square + saw mix, resonant filter, fast decay with tail

  4.  Chorus Detune
      6-voice unison, gentle chorus movement, slow fade

  5.  FM Buzz
      Sine with light FM, envelope-controlled timbre shift

  Pick one (1–5) or [s]kip: 1

  → Dirty Unison Lead
  Sending to Surge XT... ✓

  ✦  Iterate (describe changes) or [n]ew / [q]uit: make it brighter and add more attack
```

### Commands
| Input | Action |
|-------|--------|
| Text | Generate presets from description |
| `1`–`5` | Select a preset and send to Surge XT |
| `n` | Start fresh (resets to sine wave) |
| `r` | Reset Surge XT to sine wave |
| `q` | Quit |

### CLI flags
```bash
python3 main.py --ping      # Test Surge XT OSC connection
python3 main.py --reset     # Reset to defaults
python3 main.py --port 53280  # Custom OSC port
```

---

## Troubleshooting

**"Surge XT not responding"**
- Open Surge XT standalone or in Logic
- Go to Main Menu → OSC → Enable OSC
- Make sure port is 53280

**"Parameter not found" warnings**
- Surge XT's OSC parameter paths can vary by version
- Right-click any knob in Surge XT to see its exact OSC address
- Update `parameter_schema.py` with the correct path

**Logic Pro X setup**
- Load Surge XT as an AU instrument on a software instrument track
- Enable OSC in Surge XT's menu (same as standalone)
- SynthPilot talks to Surge XT directly regardless of Logic

---

## Project Structure

```
synthpilot/
├── main.py              — CLI loop and UI
├── synth_agent.py       — Claude API integration
├── osc_controller.py    — Surge XT OSC interface  
├── parameter_schema.py  — All parameter definitions + OSC paths
├── requirements.txt
└── .env.example
```

---

## Roadmap

- [ ] Verify all OSC parameter paths against Surge XT 1.3+
- [ ] Parameter discovery mode (dump all active params from Surge XT)
- [ ] Save/load named presets to JSON
- [ ] Web UI (replace CLI with a browser interface)
- [ ] Custom JUCE plugin (standalone, no Surge XT dependency)
