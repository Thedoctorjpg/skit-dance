# Warhol ↔ Seuss Handoff Protocol

Bidirectional prompt channel between **andy-warhol-director** and **dr-seuss-script-writer**.

---

## Roles

| Persona | Job |
|---------|-----|
| **Andy Warhol Director** | Flat brief, cast, repetition grid, skill routing, screen test # |
| **Ted Rhymewell (Seuss)** | Rhyming script, dance beats in verse, moral, SEUSS PROMPT OUT |

```
User idea
    ↓
[Path A] Warhol first → WARHOL PROMPT IN → Seuss → SEUSS PROMPT OUT → Warhol → skills
[Path B] Seuss first → SEUSS PROMPT OUT → Warhol → Factory brief → skills
[Path C] User says "both" → Warhol intake (1 stanza) → Seuss full script → Warhol production
```

---

## Message: WARHOL PROMPT IN

Warhol (or user acting as Factory) sends:

```markdown
## WARHOL PROMPT IN
**From:** Andy Warhol Director · Screen Test Division
**Screen Test #:** 47
**Log line:** A kilted potato audits the frozen aisle.
**Cast:** scottish-haggis-kilt-dance (+ optional kiwi-cricket-announcer for intro)
**Repetition grid:**
  A — fluorescent supermarket
  B — neon night market
  C — black and white
  D — airport security
**Pipeline:** video-creator P2
**Duration:** ~45s montage
**Aspect:** 9:16
**Constraints:** Voxtral VO from rhyming narrator lines; no trademark characters
```

Seuss must echo the screen test # and honor cast + grid in verse.

---

## Message: SEUSS PROMPT OUT

Seuss sends back:

```markdown
## SEUSS PROMPT OUT
**To:** Andy Warhol Director
**Screen Test #:** 47
**Title:** *Oh, the Aisles You'll Flap Upon a Spud*

### Rhyme script
[stanzas + directions]

### Dance beats (maps to grid)
| Variant | Stanza | Move in verse |
|---------|--------|---------------|
| A | 2 | Shuffle-of-Forms |
| B | 3 | Flam-Flamingo Stand |
| C | 4 | Pivotal Spin of Note |
| D | 5 | Fluffle-Stuffle Flap |

### Moral
[couplet]

### Cast assignment
- Stanzas 1–2: Scottish troupe voice guide
- Stanza 0 intro: Muzz (optional)

**Ready for:** video-creator P2 · seedance @Image1 · Voxtral TTS from stanzas 1,3,5

— Ted Rhymewell, for the Factory
```

---

## Warhol Response (SEUSS PROMPT ACK)

After receiving SEUSS PROMPT OUT, Warhol outputs:

```markdown
## SEUSS PROMPT ACK
That's very good. We'll shoot it four times.

**Factory brief follows** — [full SCREEN TEST brief with skill invocations]

**/dr-seuss-script-writer** — archived script: `skits/[kebab-title].md`
**/video-creator** — P2 with SEUSS PROMPT OUT attached
```

---

## Combined Invocation (User)

Single command for both personas:

```
/andy-warhol-director + /dr-seuss-script-writer
Screen test: Filipino TikTok narrator rhymes about padel dancers in a cheese shop
```

**Execution order:**
1. Warhol — WARHOL PROMPT IN (short)
2. Seuss — full rhyme script + SEUSS PROMPT OUT
3. Warhol — SEUSS PROMPT ACK + Factory brief + skill slashes

---

## Grok Single-Session (no slash)

If only `dr-seuss-script-writer` loaded:

1. Write script + SEUSS PROMPT OUT
2. End with: *"Collaborator, hand this to Andy."* + paste-ready WARHOL PROMPT IN stub for user to continue with `/andy-warhol-director`

If only `andy-warhol-director` loaded and user wants rhyme:

1. Warhol emits WARHOL PROMPT IN
2. Says: *"The room needs Ted."* → invoke `/dr-seuss-script-writer` with that block

---

## File Naming

| Writer | Output path |
|--------|-------------|
| Seuss | `skits/[kebab-rhyme-title].md` |
| Warhol | `skits/[kebab-title]-factory-brief.md` or production-brief from video-creator |

---

## Recipe IDs (registry)

| ID | Combo |
|----|-------|
| WS-01 | Warhol intake → Seuss script → video-creator P2 |
| WS-02 | Seuss meme quatrain → Warhol P1 silver wall |
| WS-03 | Seuss + Superstar cast → Warhol P4 personality VO |
| WS-04 | Seuss rhyme → Fugu P6 with both prompt blocks in input |