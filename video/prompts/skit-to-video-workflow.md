# Dancing Skit → Seedance Video Workflow

Bridge the **dancing-skit** script skill with **Seedance 2.0** video generation.

## Pipeline

```
Topic/vibe
    ↓
/dancing-skit  →  production .md script (acts, dialogue, named moves)
    ↓
/video-creator  →  shot table + production brief
    ↓
Extract choreography cues + scene descriptions per act
    ↓
seedance/SKILL.md  →  Seedance 2.0 prompts with @ references
    ↓
Jimeng Seedance 2.0  →  4–15s clips per act/scene
    ↓
Voxtral TTS  →  dialogue/narration from script lines (not in Seedance prompt)
    ↓
FFmpeg concat + mux  →  final montage with voice + music
```

For the full pipeline (Grok Imagine path, Voxtral STT on reference clips, FFmpeg ducking), see `video-creator/SKILL.md`.

## Step 1: Generate the skit script

Ask Grok:

```
/dancing-skit medieval peasants during a plague outbreak
```

Output: a full `.md` script with named moves like **THE HUMOURAL FLUTTER** and **THE PLAGUE DOCTOR WORM**.

## Step 2: Map script beats to Seedance prompts

For each act, extract:

| From script | Into Seedance prompt |
|-------------|---------------------|
| Scene description | `Scene references [setting]` |
| Named move | Action description in timed segments |
| `📹 VIDEO NOTE` | Camera movement terms (push in, orbit, track) |
| `🎵 MUSIC CUE` | Audio direction at end of prompt |
| Cast appearance | `@Image1's character as the subject` |

## Step 3: Example conversion

**From skit (Act 1 excerpt):**

> *GREGOR executes **THE PLAGUE DOCTOR WORM** — floor contact achieved through compliance, not joy.*

**To Seedance prompt:**

```
@Image1's character as the subject. Scene references a muddy medieval village
square with thatched roofs and confused chickens.

0–5s: Full shot. Character in plague doctor aesthetic performs a committed
worm dance across mud, believing it wards off disease. Camera tracks at
ground level.
5–10s: Villagers watch without intervening. Character rises and executes
THE HUMOURAL FLUTTER — wrist circles with medical conviction.
10–13s: Wide shot. Character bows to a well. Music cuts to silence.

🎵 Gregorian chant with accidental disco bass. 9:16. 13 seconds.
```

## Step 4: Generate and assemble

1. Upload character reference as @Image1
2. Generate one clip per act (or per scene within long acts)
3. Concat with FFmpeg (`-c copy` for no quality loss)

## Tips

- Seedance handles **literal motion** better than abstract comedy — write moves as physical actions, not jokes
- Keep each clip to **one clear dance sequence** — busy multi-action prompts fail
- Use **time-segmented prompts** (0–3s, 3–6s…) for clips over 8 seconds
- The skit's **mundane dialogue** → **Voxtral TTS** in post (see `video-creator/references/voxtral-voice-pipeline.md`), not in Seedance prompts
- Use personality voice guides (Scottish, chieftain, festival, etc.) for TTS `Text` and `Voice` direction blocks