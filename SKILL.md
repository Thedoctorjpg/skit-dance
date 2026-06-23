---
name: dancing-skit
description: >
  Generate a humorous dancing skit script from a single topic or vibe prompt, formatted as a
  production-ready .md file with full stage directions, dialogue, choreography cues, and video
  notes. Tone is absurdist chaos — think Monty Python meets TikTok at 3am. Trigger this skill
  whenever the user asks for a dancing skit, comedy dance script, video skit script, funny
  choreography scene, or any request combining "dance" with "comedy", "script", "video", "skit",
  "scene", or "sketch". Also trigger when the user gives a topic/prompt and wants it turned into
  a funny dance-based performance. Do NOT use for serious choreography, professional dance
  notation, or non-humorous video production.
---

# Dancing Skit Skill

Generates a complete, absurdist humorous dancing skit script from a single topic or vibe prompt.
Output is a `.md` file formatted for video production use — ready to hand to performers, a
director, or paste into a video editing brief.

---

## Tone & Style Mandate

**Monty Python energy. Always.**

- Logic is optional. Commitment is mandatory.
- Characters believe completely in what they're doing, no matter how ridiculous.
- Dance moves should have names. Absurd names. ("The Bureaucratic Shuffle", "The Confused Flamingo")
- At least one character should have no idea what is happening and enthusiastically participate anyway.
- There must be at least one moment where the music stops and someone says something devastatingly mundane.
- The ending should resolve nothing, or resolve everything incorrectly.
- Physical comedy beats should be written with the same gravity as Shakespearean stage directions.

---

## Output Format

Generate a `.md` file with the following structure. Every section is required.

```
# [SKIT TITLE] — A Dancing Skit in [N] Acts

**PRODUCTION NOTES**
**CAST**
**PROPS & STAGING**
**MUSIC CUES**

---

## ACT [N]: [ACT TITLE]

[SCENE DESCRIPTION]

[STAGE DIRECTIONS / CHOREOGRAPHY CUES]
[DIALOGUE]
[VIDEO NOTES]

---

## EPILOGUE / POST-CREDITS
```

See `references/format-guide.md` for full formatting spec and examples.

---

## Generation Process

When a user provides a topic/vibe prompt:

### Step 1 — Extract the Absurdist Premise
Take the topic and ask: *What is the single most unexpected thing that could happen involving dancing here?* That is your skit's spine. The dance should not be metaphorical — it should be literal and inappropriate to the setting.

Examples:
- "Tax returns" → IRS auditors break into a tango mid-audit
- "Medieval peasants" → plague doctors doing the worm to ward off disease
- "Job interview" → candidate performs interpretive dance CV instead of speaking

### Step 2 — Build the Cast
- **2–4 characters** minimum
- At least one character is a reluctant dancer who becomes the best dancer
- At least one character is extremely confident but technically terrible
- Optional: one silent character who only communicates through interpretive movement

### Step 3 — Structure the Acts
Skits should have **2–3 acts** plus an epilogue:

| Act | Purpose |
|-----|---------|
| Act 1 | Establish normalcy. Immediately destroy it with dancing. |
| Act 2 | Escalate. Someone joins who shouldn't. The stakes become inexplicably high. |
| Act 3 | Climax — the most chaotic dance sequence. At least one prop is misused. |
| Epilogue | Post-credits scene. Undercut everything. |

### Step 4 — Choreography Naming
Every distinct dance move must be named. Use the format:

> *[Character] executes THE [MOVE NAME] — [1-sentence deadpan description]*

Move names should sound like they belong in a government manual or a Victorian medical textbook.

### Step 5 — Video Production Notes
After each major scene, include a `📹 VIDEO NOTE:` block with:
- Suggested camera angle/shot type
- Any visual effects or editing gag
- Costume or prop callout

### Step 6 — Music Cues
Include a `🎵 MUSIC CUE:` indicator whenever the music changes. Describe the track style (not a real song — describe it: "triumphant 80s synth that implies the protagonist is about to fix the photocopier").

---

## Dialogue Style Rules

- **Stage directions** in *italics*, written with Shakespearean gravitas
- **Character names** in `CAPS` before their line
- Parenthetical acting notes like `(as if recalling a mild disappointment from 1987)`
- No character should ever directly acknowledge that what they are doing is strange
- Non-sequiturs are encouraged. Plant one early. Pay it off incorrectly at the end.

---

## Quality Checks Before Output

Before writing the final script, verify:

- [ ] The central dance makes NO logical sense in context — but the characters treat it as routine
- [ ] There is at least one move with a bureaucratic/Victorian/clinical name
- [ ] The music stops at least once at an inopportune moment
- [ ] At least one line of dialogue could appear on a motivational poster without modification
- [ ] The ending does not explain what just happened

---

## Reference Files

- `references/format-guide.md` — Full formatting spec with annotated example skit
- `references/move-names.md` — Seed list of absurdist dance move names to remix or draw inspiration from

Read these before generating your first draft if you want maximum chaos consistency.

---

## Writing the Output File

1. Read `references/format-guide.md` and `references/move-names.md` before drafting.
2. Write the complete script to a `.md` file in the user's working directory (or a path they specify).
3. Use a filename derived from the skit title in kebab-case (e.g. `the-bureaucratic-shuffle.md`).
4. Tell the user where the file was saved.