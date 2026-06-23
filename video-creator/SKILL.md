---
name: video-creator
description: >
  End-to-end video production skill: plan shots, generate visuals (Grok Imagine or Seedance 2.0),
  synthesize voice/narration with Voxtral TTS, transcribe reference audio with Voxtral STT, mux
  audio with FFmpeg, and deliver a production brief. Trigger when the user asks for video creator,
  imagine-video, make a video, video production pipeline, voice-over for video, narrated skit video,
  Voxtral voice, or combines script + dance + narration into a finished clip. Also trigger for
  /video-creator and /imagine-video requests. Do NOT use for static images only or professional
  broadcast mastering.
---

# Video Creator Skill

Orchestrates the full pipeline from idea → script → visuals → voice → assembled video.

**Philosophy (Julia Turc / Voxtral):** Plug LLMs into voice workflows instead of handwritten rules. Use Voxtral for speech understanding and TTS; use agent skills for creative structure — not brittle if/else voice trees.

---

## Pipeline Overview

```
Topic / vibe / reference link
    ↓
[Optional] personality or dancing-skit skill → script .md
    ↓
Shot plan (6–10s beats)
    ↓
Visual generation ──┬── Grok Imagine (image_gen → image_to_video)
                      └── Seedance 2.0 (@ references, timed prompts)
    ↓
Voice layer (Voxtral) ──┬── TTS: dialogue, narration, captions-as-VO
                        └── STT: transcribe @Video1 dance/audio references
    ↓
FFmpeg: concat clips → mux voice + music → final .mp4
    ↓
Production brief .md delivered to user
```

See `references/voxtral-voice-pipeline.md`, `references/grok-imagine-shots.md`, and `references/audio-mux-ffmpeg.md`.

---

## Step 0: Verify Tools

Before generating, check what's available:

| Tool | Use | Fallback if missing |
|------|-----|---------------------|
| `image_gen` / `image_edit` | Source frames | Tell user to use Grok TUI `/imagine` or xAI API |
| `image_to_video` / `reference_to_video` | Animate shots | Grok TUI `/imagine-video` or xAI `grok-imagine-video` API |
| Voxtral API / local model | TTS + STT | Mistral API, Hugging Face `mistralai/Voxtral-*`, or manual VO |
| FFmpeg | Concat + mux | Provide commands for user to run |

Never invent tool results. If video tools are absent in the current session, output the full production brief and prompts so the user can run them in Grok TUI or API.

---

## Step 1: Intake

Ask or infer:

1. **Format** — dance meme, absurdist skit, narrated explainer, personality-driven clip?
2. **Visual backend** — Grok Imagine (image-to-video) or Seedance 2.0 (multimodal @ refs)?
3. **Voice** — narration only, character dialogue, both, or silent?
4. **Personality** — any skit-dance personality skill active? (Use its voice guide for TTS prompts.)
5. **Duration** — target length; default 30–60s montage of 4–6 shots.
6. **Aspect ratio** — default `9:16` for social; `16:9` for landscape.

---

## Step 2: Script & Shot Plan

| Source | When |
|--------|------|
| `/dancing-skit` | Absurdist comedy with acts + named moves |
| Personality skill + meme pack | Short dance meme captions |
| User topic only | Draft a minimal shot list (no full skit) |

Output an internal **shot table** before generating:

| Shot | Duration | Visual prompt | Voice line | Music |
|------|----------|---------------|------------|-------|
| 1 | 6s | … | … | … |

Named dance moves from skits map to **literal physical actions** in visual prompts (not jokes).

---

## Step 3: Visual Generation

### Grok Imagine path

1. `image_gen` or `image_edit` per shot — consistent character via reference image reuse
2. `image_to_video` per shot — one motion, one camera move, 6s preferred
3. `reference_to_video` only when user supplies multiple refs or asks explicitly

Load imagine skill principles: simple frames animate better; busy scenes → camera-only motion.

### Seedance 2.0 path

1. Load `seedance/SKILL.md` @ reference syntax
2. Upload `video/assets/character-reference.jpg` as @Image1 (or user asset)
3. Time-segmented prompts per shot (0–3s, 3–6s…)
4. Dialogue goes to **Voxtral TTS**, not embedded in Seedance prompt (Seedance auto-SFX only)

---

## Step 4: Voxtral Voice Layer

**Do not use handwritten rule trees for voice.** Generate natural speech from script lines + personality voice guides.

### TTS (Voxtral Text-to-Speech)

For each voice line in the shot table:

1. Pull accent/rhythm from active personality `references/*-voice-guide.md` if applicable
2. Write a **TTS direction block** per line:

```
Voice: [persona — e.g. "regal ceremonial baritone, unhurried"]
Text: "[exact line from script]"
Pace: [slow / brisk / deadpan]
Emotion: [committed / mundane / escalating — never "ironic"]
```

3. Generate via Mistral Voxtral TTS API (`grok-imagine-video` is visual only — use Voxtral for audio):

```bash
# Mistral API — check current Voxtral TTS endpoint in docs
curl -X POST https://api.mistral.ai/v1/audio/speech \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "voxtral-tts", "input": "...", "voice": "..."}'
```

If API unavailable, output TTS direction blocks for the user to generate in [Le Chat voice mode](https://chat.mistral.ai) or Hugging Face.

### STT (Voxtral Speech-to-Text)

When user provides a **dance or audio reference** (@Video1):

1. Transcribe with Voxtral STT to capture beat markers and any spoken cues
2. Map timestamps to shot cuts for beat-synced editing
3. Use semantic understanding for Q&A: *"Where does the chorus drop?"* → cut point

```bash
curl -X POST https://api.mistral.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -F file="@reference.mp4" \
  -F model="voxtral-mini-transcribe"
```

### Voice assistant pattern (advanced)

For interactive/narrated explainers (Julia Turc style):

- **Old way:** trigger words → fixed responses
- **Voxtral way:** stream audio → LLM reasons → Voxtral TTS responds

For pre-rendered skit video, pre-generate all lines — no realtime loop needed.

---

## Step 5: Audio Mix & Assembly

1. **Concat video** — `ffmpeg -f concat -safe 0 -i scenes.txt -c copy video-only.mp4`
2. **Mux voice** — align each TTS clip to shot start timestamps
3. **Bed music** — lower under VO (-12 to -18 dB); duck on dialogue
4. **Silence gag** — skit scripts often cut music for mundane lines; preserve this in the mix

See `references/audio-mux-ffmpeg.md` for exact commands.

---

## Step 6: Deliverables

Write a production brief `.md` to the user's working directory:

```
# [TITLE] — Video Production Brief

## Summary
## Shot Table
## Visual Prompts (per shot)
## Voxtral TTS Blocks (per line)
## Seedance @ References (if applicable)
## FFmpeg Commands
## Output Files
```

Filename: kebab-case from title (e.g. `supermarket-shuffle-video-brief.md`).

---

## Personality Voice Integration

When a personality skill is active, cross-reference its voice guide for TTS direction:

| Skill | Voice guide |
|-------|-------------|
| scottish-haggis-kilt-dance | `references/scottish-accent-guide.md` |
| african-chieftain-dance-fighters | `references/chieftain-voice-guide.md` |
| chinese-festival-dancers | `references/festival-voice-guide.md` |
| kiwi-cricket-announcer-personality | SKILL.md voice section |
| american-gameshow-announcer | SKILL.md voice section |

TTS `Text` field uses phonetic/dialogue from the guide; `Voice` field describes timbre and pace.

---

## Quality Checks

- [ ] Every shot has one clear motion (not multi-action chaos)
- [ ] Voice lines match script — not paraphrased unless intentional
- [ ] Music stops at least once if source skit specifies a silence gag
- [ ] TTS persona matches active personality guide
- [ ] FFmpeg concat uses same resolution/FPS across clips
- [ ] User told which steps require TUI/API if tools unavailable in session

---

## Reference Files

- `references/voxtral-voice-pipeline.md` — Voxtral STT/TTS/realtime patterns
- `references/grok-imagine-shots.md` — Shot planning + Imagine tool usage
- `references/audio-mux-ffmpeg.md` — Concat, mux, ducking commands
- `../video/prompts/skit-to-video-workflow.md` — Skit → Seedance conversion
- `../seedance/SKILL.md` — Seedance @ reference syntax

## External References

- [Voxtral announcement](https://mistral.ai/news/voxtral/) — models, pricing, capabilities
- [Julia Turc Voxtral deep-dive](https://x.com/juliarturc/status/2069096367155507257) — LLM + voice vs handwritten rules
- [Grok Imagine video API](https://docs.x.ai/developers/model-capabilities/video/generation)
- [KakuDrop Seedance dance demo](https://x.com/KakuDrop/status/2069181320010543409)