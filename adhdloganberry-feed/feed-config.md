# @ADHDloganberry — Video Output Feed Config

| Field | Value |
|-------|--------|
| **Handle** | [@ADHDloganberry](https://x.com/ADHDloganberry) |
| **Name** | David Logan |
| **Location** | Auckland, New Zealand |
| **Feed status** | Greenfield (no posts yet — first video sets tone) |

---

## Feed identity

- **Vibe:** ADHD-forward absurdist comedy — dance in wrong places, hyperfocus montages, wholesome chaos
- **Visual default:** `9:16` (720×1280) — mobile X timeline
- **Length default:** 15–45s per post; hard cap **140s** (X non-Premium limit)
- **Audio:** Voxtral VO + optional Eddie Vedder-style bed (original only)
- **Production stack:** skit-dance → `video-creator` P1/P2 → `export-for-x` → `post-to-x`

---

## Content pillars

| Pillar | Source skills | Example |
|--------|---------------|---------|
| **Wacky dance** | `dancing-skit` + `video-creator` P1 | Supermarket shuffle, airport fling |
| **Personality wall** | CAST-* + P4 | Muzz narrates Chief Jabari at IKEA |
| **Factory screen test** | `andy-warhol-director` + repetition grid | Same dance 4× colour variants |
| **Rhyme chaos** | `dr-seuss-script-writer` + P2 | Ted rhymes a freezer audit |
| **ADHD hyperfocus bit** | Any CAST + deadpan VO | 30s on one mundane object, then dance drop |

---

## Default post package

Every feed item produces:

```
adhdloganberry-feed/output/[post-id]/
  final-x.mp4          # X-ready encode
  caption.txt          # Tweet text ≤ 280 chars
  post-meta.json       # ids, timestamps, pipeline refs
  production-brief.md  # copy from video-creator (optional)
```

Queue before publish:

```
adhdloganberry-feed/queue/[post-id].json
```

---

## Caption rules

- Lead with the bit — no "new video drop" filler unless ironic
- Max **280** characters (X post text)
- 0–2 hashtags default: `#ADHD` optional, skit-specific tags welcome
- No @mentions unless casting a collab
- Auckland / NZ sprinkles OK — dry, not touristy

**Templates:**

```
[one deadpan line about the dance location]

[optional CAST name] energy. Screen test #[N].
```

```
POV: hyperfocus aisle #[N]. Same shuffle. Different fluorescent crime.
```

---

## Environment variables

Copy `.env.example` → `.env` (never commit `.env`).

| Variable | Required | Purpose |
|----------|----------|---------|
| `X_USER_ACCESS_TOKEN` | Yes (to post) | OAuth 2.0 user token for @ADHDloganberry |
| `X_API_BASE` | No | Default `https://api.x.com` |
| `FEED_DRY_RUN` | No | `1` = export only, skip API post |

---

## Recipes

| ID | Flow |
|----|------|
| **FEED-01** | Topic → `video-creator` P1 → `export-for-x.ps1` → queue → `post-to-x.py` |
| **FEED-02** | `andy-warhol-director` brief → P2 → export → post |
| **FEED-03** | Batch: 4 grid variants → pick best → single post |
| **FEED-04** | `FEED_DRY_RUN=1` — render + caption, manual post from X app |