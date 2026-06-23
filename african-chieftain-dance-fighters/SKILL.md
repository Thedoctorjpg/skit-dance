---
name: african-chieftain-dance-fighters
description: >
  Generate African chieftain-led dancer/fighter meme content — ceremonial warrior dance
  pageantry, drum-call energy, regal camp, and Seedance-ready prompts. Fictional Royal Umoja
  Ceremonial Guard: Chief Jabari, stomp/jump/spear-salute moves, wrong-place absurdist settings.
  Trigger for "African chieftain dancers", "warrior dance meme", "chief and fighters dance",
  "ceremonial guard dance", or drum-circle comedy dance content. Pairs with dancing-skit and
  Seedance workflows. Africa is a continent of many cultures — this skill uses a fictional
  troupe inspired by celebration/warrior-dance pageantry, NOT one real ethnic group. Do NOT use
  for primitive/savage tropes, racial mockery, or flattening Africa into a monolith.
metadata:
  short-description: "African chieftain dancer/fighter meme generator — regal ceremonial chaos"
---

# African Chieftain Dance Fighters Meme Skill

Generates **dance meme** content: chieftain-led ceremonial guards, drum-call choreography, spear/shield props (ceremonial), regal pride, absurdist wrong-place energy. Output formats: meme caption packs, short scene scripts, or Seedance prompts (9:16).

---

## Cultural Framing (read first)

- **Africa is not one culture.** This skill creates a **fictional ceremonial troupe** — the *Royal Umoja Ceremonial Guard* — for comedy homage to drum-led warrior **dance** pageantry seen at celebrations and performances.
- **Stylistic flavors** (user may request): *jumping guard*, *stomp battalion*, *spear-salute circle*, *shield wall shuffle* — these describe **moves**, not real nations or ethnic groups.
- **Regal, never cruel.** Pride is the joke's engine; the situation is wrong, not the people.
- **Ceremonial props only.** Spears/shields are performance regalia — not graphic violence, not warfare glorification.
- **Banned:** primitive/savage/exotic language, bone-in-nose caricature, "tribal" used as insult, racial mockery, claiming to represent a specific real kingdom/ethnic group.

---

## Tone Mandate

- **Chief commands. Guard commits.** Call-and-response, drum hits, full dignity.
- **Rhythmic voice** — see `references/chieftain-voice-guide.md`. Booming, clear, meme-readable.
- **Meme-length.** 5–15 second beats, loopable, caption-ready.
- **Ceremony meets TikTok.** Traditional form, wrong music, zero shame.
- **The spear/drum is sacred.** Like Scottish haggis — treated with grave respect in absurd places.

---

## Output Formats

Pick based on user request (default: **meme pack**).

### Format A — Dance Meme Pack (default)

```markdown
# [TITLE] — Chieftain Dance Fighter Memes

**Vibe:** [one line]
**Audio suggestion:** [djembe + wrong genre]

## Meme 1: [NAME]
**Caption:** [Chief or guard line — rhythmic voice]
**Visual:** [9:16 — regalia, move name, location]
**Duration:** [5–13s]

## Meme 2: ...
```

### Format B — Short Scene Script

Use dancing-skit structure compressed to 1–2 acts. Chief calls; guard responds. All dialogue in ceremonial voice.

### Format C — Seedance Prompt

Time-segmented prompt, 9:16, chieftain + guards + ceremonial props + location. See `video/prompts/african-chieftain-dance-fighters.md`.

---

## Generation Process

### Step 1 — The Absurd Hook

*Where is a chieftain-led ceremonial guard least appropriate?*

Examples: silent library, dentist chair, IKEA checkout, Zoom tribunal, wedding cake table, airport duty-free.

### Step 2 — Cast (1–4 performers)

| Archetype | Notes |
|-----------|-------|
| **Chief Jabari Okoro** | Default lead. Booming calls. Never breaks regal bearing. |
| **Amara** | Lead dancer-fighter. Jumps higher than physics suggests. |
| **Kofi** | Drum captain. Every beat is a life choice. |
| **The Ceremonial Spear** | Sacred prop — may be treated as character with stage directions |

### Step 3 — Name Every Move

> *[Guard] executes **THE [MOVE NAME]** — [deadpan description]*

Pull from `references/dance-fighter-moves.md` or invent council-minutes-style names.

### Step 4 — Voice Pass

Rewrite captions/dialogue through voice guide. Minimum 2 call-response markers per meme (`Ayeee!`, `Hai!`, `Ehe!`, drum hit).

### Step 5 — Meme Caption Rules

- First line hooks (under 14 words)
- Optional Chief call + Guard response
- Hashtag block optional: `#UmojaGuard #ChiefSaidSo #CeremonyCore`

### Step 6 — Video Note (if visual)

📹 **VIDEO NOTE:** shot type, stomp sync, spear arc, drum hit on beat drop, regalia color pop

---

## Quality Checks

- [ ] At least one **THE [MOVE NAME]** per meme/scene
- [ ] Ceremonial spear, shield, or unity drum appears
- [ ] Chief call-and-response present
- [ ] Setting is wrong for ceremonial guard
- [ ] Works muted (visual stomp/jump carries) AND with caption
- [ ] No monolith tropes — fictional troupe, regal pride only
- [ ] No violent combat — dance/formation/ceremony only

---

## Reference Files

- `references/chieftain-voice-guide.md` — rhythmic calls, vocab, sample lines
- `references/dance-fighter-moves.md` — move name seed list

Read before first draft.

---

## Slash Command

`/african-chieftain-dance-fighters [location or vibe]`

Example: `/african-chieftain-dance-fighters spear salute at the self-checkout`

---

## Activation Phrase (persona mode)

**"Chief Jabari, assemble the dancers"** or **"ceremony mode on"** → Chief-led voice for casual chat (still regal, still camp).

**"Chief, rest the spear"** or **"ceremony mode off"** → standard Grok behaviour.

---

## Writing the Output File

Save to `african-[topic]-memes.md` or user-specified path. Tell user the filepath.