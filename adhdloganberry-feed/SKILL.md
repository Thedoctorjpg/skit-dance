---
name: adhdloganberry-feed
description: >
  Twitter/X video output feed for @ADHDloganberry (David Logan, Auckland). Produces X-ready
  encodes from skit-dance video-creator pipeline and posts via X API v2 chunked upload.
  Triggers include "ADHDloganberry feed", "post to X", "Twitter video feed", "loganberry feed",
  "tweet the video", "X output feed", or user links https://x.com/ADHDloganberry. Also
  /adhdloganberry-feed. Requires X_USER_ACCESS_TOKEN in adhdloganberry-feed/.env for live posts.
  Use FEED_DRY_RUN=1 to export without posting.
metadata:
  short-description: "@ADHDloganberry X video feed — export & post"
---

# @ADHDloganberry Video Output Feed

Publish skit-dance videos to **[@ADHDloganberry](https://x.com/ADHDloganberry)** — David Logan, Auckland. ADHD-forward absurdist dance comedy.

Read `feed-config.md` for account defaults. Read `references/feed-workflow.md` for the full pipeline.

---

## Quick Start

```powershell
cd skit-dance\adhdloganberry-feed
copy .env.example .env
# Fill X_USER_ACCESS_TOKEN — see references/x-api-setup.md

pip install requests python-dotenv

# After video-creator delivers raw-final.mp4:
.\scripts\export-for-x.ps1 -Input ..\path\to\raw-final.mp4 -PostId supermarket-shuffle-001
Set-Content output\supermarket-shuffle-001\caption.txt "POV: hyperfocus aisle 4. The shuffle is mandatory."

$env:FEED_DRY_RUN="1"   # remove for live post
python scripts\post-to-x.py --post-id supermarket-shuffle-001
```

---

## Agent Workflow

1. **Produce** — `video-creator` P1/P2 or `/andy-warhol-director` + cast → assembled `.mp4`
2. **Export** — `scripts/export-for-x.ps1` → `output/[post-id]/final-x.mp4`
3. **Caption** — `caption.txt` ≤280 chars per `feed-config.md`
4. **Emit FEED POST OUT** — see `references/feed-workflow.md`
5. **Publish** — `python scripts/post-to-x.py --post-id [id]` (or dry-run first)

---

## Feed defaults

| Setting | Value |
|---------|-------|
| Account | https://x.com/ADHDloganberry |
| Aspect | 9:16 · 720×1280 |
| Max length | 140s (target 15–45s) |
| Codec | H.264 + AAC faststart |

---

## Skill pairings

| Make… | Use… |
|-------|------|
| Quick dance meme post | `video-creator` P1 → FEED-01 |
| Full skit post | `video-creator` P2 → FEED-01 |
| Factory screen test | `andy-warhol-director` → FEED-02 |
| Personality montage | CAST-* + P4 → export → post |
| Render only | `FEED_DRY_RUN=1` → FEED-04 |

---

## Quality checks

- [ ] `final-x.mp4` passes `references/x-video-spec.md`
- [ ] Caption ≤280 characters
- [ ] `X_USER_ACCESS_TOKEN` set (or dry-run acknowledged)
- [ ] FEED POST OUT block includes post-id and publish command

---

## Reference files

- `feed-config.md` — account identity, pillars, captions
- `references/x-api-setup.md` — OAuth + token setup
- `references/x-video-spec.md` — encode limits
- `references/feed-workflow.md` — FEED POST OUT + recipes
- `scripts/export-for-x.ps1` — FFmpeg X encode
- `scripts/post-to-x.py` — chunked upload + tweet create