# Feed Workflow — skit-dance → @ADHDloganberry

End-to-end path from Grok production to X post.

---

## Pipeline

```
User topic / Warhol screen test
    ↓
video-creator (P1 meme | P2 full skit | P4 personality wall)
    ↓
FFmpeg assembly → raw-final.mp4
    ↓
export-for-x.ps1 → final-x.mp4
    ↓
caption.txt + post-meta.json → queue/
    ↓
post-to-x.py → https://x.com/ADHDloganberry
```

---

## Step-by-step (agent)

1. **Produce** — Run `video-creator` or `/andy-warhol-director` + cast; deliver `production-brief.md`
2. **Assemble** — FFmpeg per `video-creator/references/audio-mux-ffmpeg.md`
3. **Export** — `scripts/export-for-x.ps1 -Input raw-final.mp4 -PostId [kebab-id]`
4. **Caption** — Write `caption.txt` per `feed-config.md` rules (≤280 chars)
5. **Queue** — Write `queue/[post-id].json` with paths + caption
6. **Publish** — `python scripts/post-to-x.py --post-id [post-id]` OR dry-run first

---

## Grok slash command

```
/adhdloganberry-feed wacky dance at Auckland supermarket — post to X
```

```
/adhdloganberry-feed dry-run Muzz narrates chieftain dancers at Countdown
```

---

## Handoff block (FEED POST OUT)

```markdown
## FEED POST OUT
**To:** @ADHDloganberry
**Post ID:** supermarket-shuffle-001
**Video:** adhdloganberry-feed/output/supermarket-shuffle-001/final-x.mp4
**Caption:** POV: hyperfocus aisle 4. The shuffle is mandatory. Screen test #7.
**Duration:** 32s
**Pipeline:** video-creator P1
**Cast:** CAST-04 Muzz VO
**Publish:** python scripts/post-to-x.py --post-id supermarket-shuffle-001
```

---

## Integration with master ensemble

Optional full stack before export:

1. Warhol screen test → cast
2. video-creator P2
3. `export-for-x.ps1`
4. `post-to-x.py`

Recipe **FEED-02** in `feed-config.md`.