---
name: swedish-chef-cookoff
description: >
  Generate absurdist Muppets-style Swedish Chef cook-off challenge content — full challenge
  briefs, round scripts, sabotage events, bork-bork dialogue, judging rubrics, and video notes.
  Tone is chaotic variety-show cooking: ingredients fly, logic optional, commitment mandatory.
  Trigger whenever the user asks for a Swedish Chef cook-off, Muppets cooking challenge,
  bork bork cook battle, chef showdown, mystery basket chaos, or competitive cooking skit in
  Swedish Chef voice. Also trigger for "cook off challenge", "muppet chef", or requests to
  write/run/host a ridiculous cooking competition. Do NOT use for real recipes, serious culinary
  instruction, or food safety advice — unless explicitly requested as comedy.
metadata:
  short-description: "Muppets Swedish Chef cook-off challenge generator"
---

# Swedish Chef Cook-Off Challenge Skill

Generates complete, production-ready cook-off challenge content in **Muppet Show Swedish Chef** energy — competitive cooking as variety-show chaos.

Output is a `.md` file ready for performers, a director, a game host, or a video brief.

---

## Tone & Style Mandate

**The Muppet Show kitchen. Always.**

- Everything is a cook-off. Even when it shouldn't be.
- Chefs believe they are making haute cuisine. They are not.
- Ingredients have opinions. Pots have agency. At least one animal appears uninvited.
- Dialogue is **Swedish Chef speak** — see `references/chef-vocabulary.md`.
- Sabotage is encouraged but never acknowledged as sabotage.
- Judges score on criteria that make no culinary sense.
- The winner is wrong. The loser is also wrong. Everyone celebrates anyway.

---

## Swedish Chef Voice Rules

Apply to all chef dialogue:

1. **Mangle English** with pseudo-Scandinavian phonetics: *de*, *yer*, *bork*, *flörgen*, *mörgen*
2. **Food words get extra syllables**: chicken → *chicky-bicky*, spaghetti → *spaghetty-flörgetty*
3. **Verbs end in -en or -a**: *choppen*, *flippa-de-floppa*, *smashina*
4. **Exclamations**: BORK! MÖRK! FLOORK! YUMP YUMP YUMP!
5. **Never break character** to explain the joke — chefs are deadly serious
6. **Subtitles optional** — if provided, the subtitle should disagree with what the chef said

See `references/chef-vocabulary.md` for word bank and dialogue patterns.

---

## Output Format

Generate a `.md` file with this structure. Every section is required.

```
# [CHALLENGE TITLE] — A Swedish Chef Cook-Off in [N] Rounds

**CHALLENGE BRIEF**
**CONTESTANTS**
**MYSTERY BASKET**
**JUDGES & SCORING**
**CHAOS EVENTS SCHEDULE**

---

## ROUND [N]: [ROUND TITLE]

[SCENE DESCRIPTION]
[COOKING ACTION / STAGE DIRECTIONS]
[CHEF DIALOGUE in Swedish Chef speak]
[SABOTAGE BEAT]
[📹 VIDEO NOTE]

---

## JUDGING & VERDICT

---

## EPILOGUE
```

See `references/format-guide.md` for full spec and annotated example.

---

## Generation Process

When a user provides a topic, ingredient, vibe, or challenge theme:

### Step 1 — Pick the Absurd Hook

Ask: *What is the most inappropriate dish to cook competitively in this setting?*

Examples:
- "Tax audit" → Cook-off to determine who owes the most meatballs
- "Space station" → Zero-gravity flörgen stew; spoons revolt
- "Funeral" → Competitive consommé; widow judges on "respectfulness of garnish"

### Step 2 — Build Contestants (2–4 chefs)

| Archetype | Role |
|-----------|------|
| **The Purist** | Insists on tradition. Tradition is invented 30 seconds ago. |
| **The Innovator** | Adds one wrong ingredient with total confidence |
| **The Saboteur** | "Accidentally" helpful. Never caught. |
| **The Guest Celebrity** | Appears mid-round. Is a lobster. |

At least one contestant is clearly the Swedish Chef. Others may be regional variants (Norwegian Nils, Danish Dorte) or Muppet archetypes (Statler & Waldorf as judges only — they never cook, only insult).

### Step 3 — Mystery Basket

Generate 5–7 ingredients. Rules:
- At least 2 should not belong together
- At least 1 is alive or sentient
- At least 1 is a metaphor made literal ("a cup of ambition" = actual cup)
- One ingredient is always **flörgen** (undefined; never explain what it is)

### Step 4 — Structure Rounds

| Round | Duration | Purpose |
|-------|----------|---------|
| Round 1 | 10 min | Panic prep. Establish chaos. First bork. |
| Round 2 | 15 min | Escalation. Sabotage. Animal entrance. |
| Round 3 (if 3 rounds) | 5 min | "Plating" — nothing is plated correctly |
| Judging | — | Scores announced incorrectly |
| Epilogue | — | Kitchen on fire. Everyone wins. Or loses. Same thing. |

### Step 5 — Name Every Technique

Format:

> *[Chef] performs **THE [TECHNIQUE NAME]** — [deadpan one-sentence description]*

Technique names sound like IKEA assembly instructions or medieval medical procedures.

Examples: **THE FLÖRDEN FLIPPA**, **THE MEATBALL MANEUVER**, **THE PANICKEN WHISKEN**

### Step 6 — Chaos Events

Schedule 2–4 chaos events across the challenge. Pick from or remix:

- Flying utensils (no CGI — clearly puppet strings acceptable)
- Ingredient achieves consciousness
- Judge eats contestant's spoon by mistake
- Timer counts up instead of down; nobody notices
- Swedish Chef argues with his own reflection; reflection wins
- "Commercial break" mid-cooking; resumes in different kitchen

### Step 7 — Judging Rubric

Score on 4 categories (1–10 each). Categories must be absurd:

| Category | What it measures |
|----------|------------------|
| **Bork Factor** | Intensity of bork-bork delivery |
| **Flörgen Integrity** | How much flörgen was respected (undefined) |
| **Chaos Commitment** | Did anyone acknowledge the fire? (Points deducted if yes) |
| **Meatball Symmetry** | Even if no meatballs are present |

### Step 8 — Video Notes

After each round, include `📹 VIDEO NOTE:` with shot type, puppet-wire gag, prop callout, and suggested sound effect (always include at least one *BOING* or *SPLORK*).

---

## Dialogue Style Rules

- **Chef lines** in Swedish Chef speak with optional `[subtitle: actual meaning]`
- **Stage directions** in *italics*, written like a nature documentary about apex predators
- **Judge lines** are grumpy, food-critic serious, completely wrong about what they ate
- **Narrator/host** speaks BBC documentary calm while describing catastrophe
- No chef acknowledges that their dish failed — it is always "a interesting experiment"

---

## Quality Checks Before Output

- [ ] At least 3 distinct **THE [TECHNIQUE NAME]** moves named
- [ ] Mystery basket contains flörgen (unexplained)
- [ ] At least one chaos event involves an uninvited animal or Muppet
- [ ] Music or timer stops at the worst moment; someone says something mundane
- [ ] Judging criteria include at least one category unrelated to food
- [ ] Ending does not resolve who won — or declares everyone Grand Champion incorrectly
- [ ] At least 5 uses of BORK/MÖRK/FLOORK across the script

---

## Reference Files

- `references/format-guide.md` — Full challenge format + annotated mini-example
- `references/chef-vocabulary.md` — Swedish Chef word bank, dialogue patterns, ingredient mangling

Read both before generating the first draft.

---

## Writing the Output File

1. Read reference files before drafting.
2. Write the complete challenge to a `.md` file in the user's working directory (or path they specify).
3. Filename: kebab-case from challenge title (e.g. `the-meatball-trials.md`).
4. Tell the user where the file was saved.

---

## Slash Command

`/swedish-chef-cookoff [theme or ingredients]`

Example: `/swedish-chef-cookoff underwater basket with rubber chicken and dignity`