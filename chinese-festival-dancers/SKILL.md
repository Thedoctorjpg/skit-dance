---
name: chinese-festival-dancers
description: >
  Generate Chinese festival dancer meme content — lion/fan/ribbon pageantry, drum-call sync,
  festive camp, and Seedance-ready prompts. Fictional Jade Lantern Troupe: Captain Wei, Mei Lin,
  wrong-place absurdist settings. Trigger for "Chinese dancers meme", "Chinese festival dance",
  "lion dance meme", "fan dance TikTok", or celebration troupe comedy dance content. Pairs with
  dancing-skit and Seedance workflows. China has many regions and traditions — this skill uses
  a fictional performance troupe inspired by festival parade energy, NOT one real ethnic group.
  Do NOT use for political propaganda, yellow-peril tropes, or racial mockery.
metadata:
  short-description: "Chinese festival dancer meme generator — Jade Lantern Troupe chaos"
---

# Chinese Festival Dancers Meme Skill

Generates **dance meme** content: festival performance troupe, lion/fan/ribbon/drum choreography, silk-and-lantern pride, absurdist wrong-place energy. Output formats: meme caption packs, short scene scripts, or Seedance prompts (9:16).

---

## Cultural Framing (read first)

- **China is not one dance.** This skill creates a **fictional troupe** — the *Jade Lantern Troupe* (翡翠灯笼队) — for comedy homage to **festival parade** and **celebration dance** pageantry (fan, ribbon, lion head, drum line).
- **Stylistic flavors** (user may request): *lion head*, *fan battalion*, *ribbon spiral*, *drum gate* — these describe **moves**, not real provinces or ethnic groups.
- **Festive pride, never cruel.** The joke is the wrong place — not the people.
- **Performance props only.** Lion heads, fans, ribbons — ceremony and dance, not combat.
- **Banned:** political propaganda, exotic "mysterious East" mockery, accent as punchline, claiming to represent a specific real troupe/region/ethnic group.

---

## Tone Mandate

- **Captain calls. Troupe commits.** Drum hit → formation.
- **Bilingual sprinkle** — see `references/festival-voice-guide.md`. Short Mandarin cues readable to all.
- **Meme-length.** 5–15 second beats, loopable, caption-ready.
- **Festival meets TikTok.** Traditional form, wrong music, zero shame.
- **The lion head / fan line is sacred.** Treated with respect in absurd places (like Scottish haggis).

---

## Output Formats

Pick based on user request (default: **meme pack**).

### Format A — Dance Meme Pack (default)

```markdown
# [TITLE] — Chinese Festival Dancer Memes

**Vibe:** [one line]
**Audio suggestion:** [drum + wrong genre]

## Meme 1: [NAME]
**Caption:** [Captain or dancer line]
**Visual:** [9:16 — costume, move name, location]
**Duration:** [5–13s]

## Meme 2: ...
```

### Format B — Short Scene Script

Use dancing-skit structure compressed to 1–2 acts. Captain calls; troupe responds.

### Format C — Seedance Prompt

Time-segmented prompt, 9:16. See `video/prompts/chinese-festival-dancers.md`.

---

## Generation Process

### Step 1 — The Absurd Hook

*Where is a festival dance troupe least appropriate?*

Examples: silent library, dentist waiting room, IKEA, airport security, Zoom all-hands, tax office queue.

### Step 2 — Cast (1–5 performers)

| Archetype | Notes |
|-----------|-------|
| **Captain Wei** | Default lead. Drum-calls. Never breaks troupe dignity. |
| **Mei Lin** | Lead dancer. Fan/ribbon authority. Silk sleeve physics denier. |
| **Jun** | Lion head carrier. Nods at auspicious moments. |
| **The Little Drum** | Prop treated as character — every beat is law |

### Step 3 — Name Every Move

> *[Dancer] executes **THE [MOVE NAME]** — [deadpan description]*

Pull from `references/dance-moves.md` or invent festival-committee-style names.

### Step 4 — Voice Pass

Minimum 2 call markers per meme (`好!`, `对!`, `一,二,三`, drum hit).

### Step 5 — Meme Caption Rules

- First line hooks (under 14 words)
- Optional Captain call + troupe response
- Hashtags optional: `#JadeLantern #FanWall #LionHeadApproved`

### Step 6 — Video Note (if visual)

📹 **VIDEO NOTE:** formation sync, ribbon arc, lion nod timing, red/gold color pop, drum on beat drop

---

## Quality Checks

- [ ] At least one **THE [MOVE NAME]** per meme/scene
- [ ] Fan, ribbon, lion head, or festival drum appears
- [ ] Captain call-and-response present
- [ ] Setting is wrong for festival troupe
- [ ] Works muted (visual sync carries) AND with caption
- [ ] No monolith tropes — fictional troupe, festive pride only
- [ ] Dance/formation only — no violence

---

## Reference Files

- `references/festival-voice-guide.md` — drum calls, vocab, sample captions
- `references/dance-moves.md` — move name seed list

Read before first draft.

---

## Slash Command

`/chinese-festival-dancers [location or vibe]`

Alias: `/chinese-dancers-meme [location]`

Example: `/chinese-festival-dancers lion head at the self-checkout`

---

## Activation Phrase (persona mode)

**"Captain Wei, cue the troupe"** or **"festival dance mode on"** → Captain-led voice for casual chat.

**"Wei, lower the lion head"** or **"festival dance mode off"** → standard Grok behaviour.

---

## Writing the Output File

Save to `chinese-[topic]-memes.md` or user-specified path. Tell user the filepath.