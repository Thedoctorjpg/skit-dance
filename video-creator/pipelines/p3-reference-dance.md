# Pipeline P3 — Reference Dance Replication

**Fugu model:** `fugu` · **Effort:** `high` · **Timeout:** 180s

Inspired by [KakuDrop Seedance 2.0 Omni](https://x.com/KakuDrop/status/2069181320010543409).

## Variables

`{IMAGE1_PATH}` `{VIDEO1_PATH}` `{LOCATIONS}` (comma-separated)

## Prompt

You are the video-creator orchestrator running **Pipeline P3 — Reference Dance Replication**.

**@Image1:** {IMAGE1_PATH} — character appearance (consistent across all shots)
**@Video1:** {VIDEO1_PATH} — dance choreography + beat reference
**Locations:** {LOCATIONS}

### Steps

1. **STT** — Voxtral commands to transcribe @Video1 audio; extract beat timestamps for editing.
2. **Seedance** — One prompt per location: character from @Image1 replicates dance moves and rhythm from @Video1. 10–13s, 9:16, smooth motion.
3. **Edit map** — Table: shot | location | start beat | duration
4. **FFmpeg** — `scenes.txt` + concat -c copy

### Seedance template per location

```
Have the character in @Image1 replicate the dance moves and beat-synced
music from @Video1. Scene references {LOCATION}. Generate a 13-second video.
Movements smooth, no stuttering. Character treats dance as routine for setting.
```

### Deliverables

Production brief with STT commands, all Seedance prompts, beat-sync table, FFmpeg commands.