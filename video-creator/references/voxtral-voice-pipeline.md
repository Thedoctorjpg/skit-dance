# Voxtral Voice Pipeline

Voice layer for the video-creator skill. Based on [Mistral Voxtral](https://mistral.ai/news/voxtral/) and [Julia Turc's technical overview](https://x.com/juliarturc/status/2069096367155507257).

---

## Why Voxtral (Not Handwritten Rules)

Traditional voice assistants:

```
if "play music" → play_music()
elif "stop" → stop()
else → "I didn't understand"
```

LLM + Voxtral stack:

```
audio → Voxtral STT → text + semantics → LLM reasoning → Voxtral TTS → audio
```

For **pre-rendered skit video**, we use the TTS/STT pieces without a realtime loop.

---

## Models (2025–2026)

| Model | Size | Use in video-creator |
|-------|------|----------------------|
| Voxtral Small | 24B | Production STT + audio understanding |
| Voxtral Mini | 3B | Local/edge STT, fast transcription |
| Voxtral Mini Transcribe | — | Cost-efficient transcription |
| Voxtral Realtime | — | Low-latency streaming (live assistants) |
| Voxtral TTS | — | Narration + character dialogue |
| Voxtral Codec | — | Audio tokenization (underlying tech) |

Apache 2.0 — [Hugging Face](https://huggingface.co/mistralai/).

---

## TTS Workflow for Skit Video

### 1. Extract lines from script

From dancing-skit or personality meme output:

| Field | Source |
|-------|--------|
| Character | `**CHARACTER NAME**` blocks |
| Line | Dialogue under character |
| Acting note | Parentheticals → TTS emotion |
| Timing | Shot table act/beat |

### 2. Build TTS direction block

```markdown
### LINE 3 — DEREK (Act 2, shot 2, t=12.0s)

Voice: Male, 40s, corporate-calm baritone, fully sincere
Pace: Measured, as if quarterly results depend on this dance
Emotion: Mild disappointment recalling 1987
Text: "Does anyone need more water?"

Output: line-03-derek.wav
```

### 3. Personality accent overlay

If `scottish-accent-guide.md` active, **Text** uses phonetic spelling:

```
Text: "Och, that's nae a haggis — that's ma lunch!"
Voice: Warm Highland brogue, festive not cruel, clear enunciation
```

### 4. Generate audio

**Mistral API** (verify endpoint in current docs):

```python
# Pseudocode — check https://docs.mistral.ai/capabilities/audio/
response = client.audio.speech.create(
    model="voxtral-tts",
    input="Does anyone need more water?",
    voice="alloy",  # or voice preset matching persona
)
response.stream_to_file("line-03-derek.wav")
```

**Local** (Hugging Face):

```bash
# Requires GPU; model card: mistralai/Voxtral-4B-TTS-2603
python -m voxtral_tts --text "..." --out line-03-derek.wav
```

### 5. Silence gag lines

When skit specifies music stop + mundane line:

- Generate TTS with **room tone** or **slight reverb**
- No background music on that clip
- Resume music on next shot — cut music bed in FFmpeg, not in TTS

---

## STT Workflow for Reference Video

When user supplies a dance reference (@Video1):

### 1. Extract audio

```bash
ffmpeg -i reference.mp4 -vn -acodec pcm_s16le -ar 16000 reference.wav
```

### 2. Transcribe + understand

```bash
curl -X POST https://api.mistral.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -F file="@reference.wav" \
  -F model="voxtral-mini-transcribe" \
  -F response_format="verbose_json"
```

### 3. Beat-sync mapping

From verbose JSON timestamps:

| Time | Event | Edit action |
|------|-------|-------------|
| 0.0s | Music start | Shot 1 in |
| 4.2s | Beat drop | Cut to shot 2 |
| 8.7s | Vocal "hey" | Caption overlay optional |

Feed into Seedance `reference @Video1's rhythm` prompts or manual FFmpeg cut list.

### 4. Semantic Q&A (optional)

```
Audio: reference.wav
Question: "Describe the energy shifts and where the tempo changes."
→ Use answer to structure montage pacing
```

---

## Realtime Pattern (Live / Explainer Mode)

For narrated explainers (not pre-baked skit):

```
Mic → Voxtral Realtime STT → streaming tokens
     → LLM (script facts + personality skill)
     → Voxtral TTS → speaker
```

Delayed Streams Modeling (DSM) enables low-latency without cutting off mid-sentence — see Julia Turc video §6:07.

Not required for meme/skit output; document for user if they ask for "live narrator."

---

## API Keys

| Service | Env var | Console |
|---------|---------|---------|
| Mistral Voxtral | `MISTRAL_API_KEY` | [console.mistral.ai](https://console.mistral.ai/) |
| xAI Grok Imagine | `XAI_API_KEY` | [console.x.ai](https://console.x.ai/) |

Pricing: Voxtral transcription from ~$0.001/min (per Mistral announcement).

---

## Failure Modes

| Issue | Fix |
|-------|-----|
| No MISTRAL_API_KEY | Output TTS blocks; user generates in Le Chat |
| TTS wrong accent | Strengthen phonetic Text; add Voice adjectives |
| STT poor on music-heavy ref | Separate stems with `demucs` first, transcribe vocal stem |
| Lip sync needed | Seedance does not lip-sync dialogue — add VO in post, not in-gen |