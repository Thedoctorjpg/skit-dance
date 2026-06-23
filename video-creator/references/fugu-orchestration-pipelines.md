# Sakana Fugu Orchestration Pipelines

Multi-agent orchestration for video-creator via [Sakana Fugu](https://sakana.ai/fugu/) — one OpenAI-compatible API that dynamically routes script, visual, voice, and assembly steps across a pool of frontier models.

**Source:** [sakana.ai/fugu](https://sakana.ai/fugu) · [Get started](https://console.sakana.ai/get-started) · [GitHub](https://github.com/SakanaAI/fugu)

---

## Why Fugu in video-creator

Handwritten pipeline:

```
if step == "script" → call LLM A
if step == "visual" → call API B
if step == "voice" → call API C
```

Fugu orchestration (TRINITY / Conductor):

```
one request → Fugu assigns Thinker / Worker / Verifier roles
           → routes to best model per subtask
           → synthesizes production brief + assets list
```

Fugu excels at **long, multi-step, messy workflows** — exactly what video production is.

---

## API Setup

| Setting | Value |
|---------|-------|
| Base URL | `https://api.sakana.ai/v1` |
| Env var | `SAKANA_API_KEY` |
| Models | `fugu` (balanced latency) · `fugu-ultra` (max quality) |
| Reasoning | `reasoning.effort`: `high` or `xhigh` (alias `max`) |
| Endpoints | Chat Completions · Responses API (preferred) |

```bash
export SAKANA_API_KEY=your_key

curl -X POST https://api.sakana.ai/v1/chat/completions \
  -H "Authorization: Bearer $SAKANA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"fugu","messages":[{"role":"user","content":"ping"}]}'
```

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.sakana.ai/v1",
    api_key="YOUR_SAKANA_API_KEY",
)

response = client.responses.create(
    model="fugu-ultra",
    input=PIPELINE_PROMPT,
    timeout=600.0,  # video pipelines are long-running
    extra_body={"reasoning": {"effort": "high"}},
)
print(response.output_text)
```

**Compliance:** Opt out providers in [console.sakana.ai](https://console.sakana.ai) API key settings (Fugu only; Ultra pool is fixed). Not available in EU/EEA yet.

---

## TRINITY Roles in Video Pipelines

Map Fugu's internal coordination to video-creator steps:

| TRINITY Role | Video pipeline duty |
|--------------|---------------------|
| **Thinker** | Intake, shot plan, personality/voice guide selection, pipeline pick |
| **Worker** | Generate script, Seedance prompts, TTS blocks, FFmpeg commands |
| **Verifier** | Quality checks — one motion per shot, silence gag preserved, voice matches guide |

Ask Fugu explicitly to use this structure in complex prompts.

---

## Pipeline Catalog

### P1 — Dance Meme (fast)

**Model:** `fugu` · **Effort:** `high` · **~2–5 min**

```
Topic + optional personality skill name
  → meme captions (3–5)
  → Seedance @Image1 prompts per scene
  → optional Voxtral TTS for captain call-and-response
  → FFmpeg concat command
```

**Trigger:** short dance meme, single character, multiple wrong-place scenes.

### P2 — Full Dancing Skit Video

**Model:** `fugu-ultra` · **Effort:** `xhigh` · **~10–30 min**

```
Topic
  → full dancing-skit .md script (acts, named moves, silence gag)
  → shot table (duration, visual, voice, music per shot)
  → Seedance OR Grok Imagine prompts per act
  → Voxtral TTS block per dialogue line
  → FFmpeg concat + mux + ducking commands
  → production-brief.md
```

**Trigger:** absurdist comedy skit with narration and multi-act structure.

### P3 — Reference Dance Replication

**Model:** `fugu` · **Effort:** `high`

```
@Image1 character ref + @Video1 dance ref
  → Voxtral STT on reference audio (beat timestamps)
  → Seedance prompt: replicate moves from @Video1
  → cut list aligned to beats
  → concat command
```

**Trigger:** KakuDrop-style same character, copy dance from reference clip.

### P4 — Personality VO Montage

**Model:** `fugu` · **Effort:** `high`

```
Personality skill (e.g. scottish-haggis-kilt-dance)
  → load voice guide
  → meme captions in persona voice
  → Seedance visual prompts (costume/prop from skill)
  → Voxtral TTS with phonetic/accent Text fields
  → per-line Voice direction from guide
```

**Trigger:** cultural/persona-driven dance content with accented VO.

### P5 — Narrated Explainer (Voxtral + visuals)

**Model:** `fugu-ultra` · **Effort:** `xhigh`

```
Topic (technical/educational)
  → script with timed segments
  → Grok Imagine shot prompts OR static slides
  → Voxtral TTS narration per segment
  → optional STT QA on draft VO
  → mux timeline
```

**Trigger:** Julia Turc-style explainers with voice + visuals (not comedy skit).

### P6 — Autonomous End-to-End

**Model:** `fugu-ultra` · **Effort:** `xhigh` · **single mega-prompt**

One prompt instructs Fugu to run P2 end-to-end, outputting only deliverables. Use when user says *"make the whole video"* and has API keys for sub-services.

---

## Ready-Made Fugu Prompts

Copy into `client.responses.create(input=...)` or Grok with SAKANA routing.

### P1 — Dance Meme

```markdown
You are the video-creator orchestrator. Run Pipeline P1 (Dance Meme).

Topic: {TOPIC}
Character reference: video/assets/character-reference.jpg as Seedance @Image1
Aspect ratio: 9:16

Deliver:
1. Five meme captions (short, deadpan, one named dance move each)
2. Five Seedance 2.0 prompts (6–13s each, time-segmented, @Image1 subject)
3. Optional captain call-and-response lines + Voxtral TTS direction blocks
4. scenes.txt + ffmpeg concat command
5. Quality check: one motion per shot, no lip-sync in Seedance prompts

Use dancing-skit move-naming style. Do not use handwritten if/else — plan then execute.
```

### P2 — Full Skit Video

```markdown
You are the video-creator orchestrator. Run Pipeline P2 (Full Dancing Skit Video).

Topic: {TOPIC}
Personality overlay: {PERSONALITY_SKILL or "none"}
Visual backend: {seedance | grok-imagine}
Voice: Voxtral TTS for all dialogue (not embedded in visual prompts)

TRINITY structure:
- Thinker: intake, act structure, shot table
- Worker: script .md, visual prompts, TTS blocks, FFmpeg commands
- Verifier: silence gag present, mundane line after music stop, persona voice match

Deliver production-brief.md with:
## Summary
## Shot Table
## Script (or path to skit .md)
## Visual Prompts
## Voxtral TTS Blocks
## FFmpeg Commands

Reference: video-creator/references/voxtral-voice-pipeline.md, seedance/SKILL.md
```

### P3 — Reference Dance Replication

```markdown
You are the video-creator orchestrator. Run Pipeline P3 (Reference Dance Replication).

@Image1: {character image path or URL}
@Video1: {dance reference path or URL}
Locations: {list of 3–4 scenes}

Steps:
1. Outline Voxtral STT commands to extract beat timestamps from @Video1
2. Write Seedance prompt per location: character from @Image1 replicates @Video1 choreography
3. Map beat timestamps to shot boundaries
4. FFmpeg concat with stream copy

Duration per clip: 10–13s. 9:16. Smooth motion, no stuttering.
```

### P6 — Autonomous

```markdown
You are the video-creator orchestrator. Run Pipeline P6 (Autonomous End-to-End).

User request: {FULL_USER_REQUEST}

Available skills in repo: dancing-skit, seedance-prompt-en, video-creator, personality skills.
Available APIs (user may or may not have keys): SAKANA_API_KEY, XAI_API_KEY, MISTRAL_API_KEY.

Produce a complete production package without asking clarifying questions unless topic is empty.
Default: 4-shot 9:16 dance meme with Voxtral VO if personality named, else silent.

Output: single production-brief.md ready for human execution of API calls and FFmpeg.
Model yourself as fugu-ultra: Thinker plans, Worker drafts all assets, Verifier checks quality list.
```

---

## Model Selection Guide

| Task | Model | Effort |
|------|-------|--------|
| Quick meme captions + 3 prompts | `fugu` | `high` |
| Full skit script + 6+ shots + TTS | `fugu-ultra` | `xhigh` |
| Beat-sync from reference video | `fugu` | `high` |
| Personality voice + 5 scenes | `fugu` | `high` |
| Entire pipeline one shot | `fugu-ultra` | `xhigh` |
| Interactive iteration in Grok TUI | `fugu` | `high` |

**Timeouts:** Set client timeout ≥ 120s for `fugu`, ≥ 600s for `fugu-ultra` multi-step.

---

## Integration with Grok

Grok agents can call Fugu via shell:

```bash
grok -p "$(cat video-creator/pipelines/p2-full-skit.txt)" \
  -m fugu-ultra  # if Grok supports custom model routing
```

Or use OpenAI SDK from a script in the repo. Fugu does **not** generate video pixels directly — it orchestrates prompts and commands for XAI/Seedance/Voxtral/FFmpeg.

---

## Pipeline vs Direct Skill

| Approach | When |
|----------|------|
| **Fugu pipeline** | Multi-step, 4+ shots, personality + voice + visuals, user has SAKANA_API_KEY |
| **Direct video-creator skill** | Grok session without Sakana; agent runs steps manually |
| **Hybrid** | Fugu plans → Grok executes image_to_video / file writes |

Default: try Fugu P1/P2 if `SAKANA_API_KEY` is set; else fall back to direct skill steps.

---

## External Links

- [Sakana Fugu product](https://sakana.ai/fugu)
- [Console / API keys](https://console.sakana.ai)
- [TRINITY paper](https://arxiv.org/abs/2512.04695)
- [Conductor paper](https://arxiv.org/abs/2512.04388)
- [Technical report](https://arxiv.org/abs/2606.21228)
- [Mario Zechner recommends Julia Turc on voice models](https://x.com/badlogicgames/status/2069156188902559751) — complementary Voxtral layer in these pipelines