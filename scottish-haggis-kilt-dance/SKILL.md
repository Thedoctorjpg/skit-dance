---
name: scottish-haggis-kilt-dance
description: >
  Generate Scottish haggis-and-kilt dance meme content — short viral dance scripts, captions,
  scene briefs, and Seedance-ready prompts with strong (phonetic) Scottish accents. Kilted
  dancers, haggis as prop/partner/sacred object, Highland fling energy turned meme chaos.
  Trigger for "Scottish dance meme", "kilt dancer", "haggis dance", "Highland fling meme",
  "Scottish accent dance", TikTok/Reels Scottish dancing absurdity, or bagpipe-adjacent comedy
  dance content. Pairs with dancing-skit and Seedance workflows. Do NOT use for mocking Scottish
  people — celebrate the chaos with affection; no slurs or tired stereotypes beyond playful
  phonetic accent and haggis worship played straight.
metadata:
  short-description: "Scottish haggis kilt dance meme generator"
---

# Scottish Haggis Kilt Dance Meme Skill

Generates **dance meme** content: kilted dancers, haggis props, strong Scottish accent (phonetic), absurdist Highland energy. Output formats: meme caption packs, short scene scripts, or Seedance prompts (9:16).

---

## Tone Mandate

- **Och aye, full commitment.** Dancers treat haggis like a national treasure and dance partner.
- **Strong accent in writing** — phonetic Scots (see `references/scottish-accent-guide.md`). Readable, not IPA.
- **Meme-length.** 5–15 second beats, loopable energy, caption-ready punchlines.
- **Highland fling meets TikTok.** Traditional form, wrong music, zero shame.
- **Affectionate chaos.** Love Scotland; the joke is the situation, not the people.

---

## Output Formats

Pick based on user request (default: **meme pack**).

### Format A — Dance Meme Pack (default)

```markdown
# [TITLE] — Scottish Kilt Dance Memes

**Vibe:** [one line]
**Audio suggestion:** [bagpipes + wrong genre]

## Meme 1: [NAME]
**Caption:** [phonetic accent line]
**Visual:** [9:16 shot — kilt, haggis, move name]
**Duration:** [5–13s]

## Meme 2: ...
```

### Format B — Short Scene Script

Use dancing-skit structure compressed to 1–2 acts. All dialogue in phonetic Scots.

### Format C — Seedance Prompt

Time-segmented prompt, 9:16, kilted dancer + haggis + location. See `video/prompts/scottish-kilt-dance-memes.md` for templates.

---

## Generation Process

### Step 1 — The Absurd Scottish Hook

*Where is a kilted dancer with a haggis least appropriate?*

Examples: IKEA, dentist chair, space station, divorce court, silent library, roller coaster queue.

### Step 2 — Cast (1–3 dancers)

| Archetype | Notes |
|-----------|-------|
| **Hamish** | Default lead. Fierce pride. Haggis whisperer. |
| **Morag** | Out-dances everyone. Kilt spins are weaponized. |
| **Angus the Haggis** | The haggis (treated as character with stage directions) |

### Step 3 — Name Every Move

> *[Dancer] executes **THE [MOVE NAME]** — [deadpan description]*

Pull from `references/kilt-dance-moves.md` or invent IKEA-manual-style names.

### Step 4 — Accent Pass

Rewrite all dialogue/captions through accent guide. Minimum 3 Scots markers per caption (`och`, `nae`, `wee`, `ken`, `dinnae`, `braw`).

### Step 5 — Meme Caption Rules

- First line hooks (under 12 words)
- Second line optional punchline
- Hashtag block optional: `#KiltLife #HaggisCore #OchAye`

### Step 6 — Video Note (if visual)

📹 **VIDEO NOTE:** shot type, kilt spin direction, haggis trajectory, bagpipe drop

---

## Quality Checks

- [ ] At least one **THE [KILT MOVE]** named per meme/scene
- [ ] Haggis appears as prop, partner, or judge
- [ ] Accent is phonetic and strong but readable
- [ ] Setting is wrong for Highland dancing
- [ ] Would work muted (visual gag carries) AND with caption
- [ ] No cruel stereotypes — playful pride only

---

## Reference Files

- `references/scottish-accent-guide.md` — phonetic patterns, vocab, sample lines
- `references/kilt-dance-moves.md` — move name seed list

Read before first draft.

---

## Slash Command

`/scottish-haggis-kilt-dance [location or vibe]`

Example: `/scottish-haggis-kilt-dance haggis flash mob at the airport`

---

## Writing the Output File

Save to `scottish-[topic]-memes.md` or user-specified path. Tell user the filepath.