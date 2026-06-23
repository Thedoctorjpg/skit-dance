# Spielberg ↔ Warhol ↔ Seuss Triple Handoff Protocol

Three-persona prompt channel for **stephen-spielberg-producer**, **andy-warhol-director**, and **dr-seuss-script-writer**.

---

## Roles

| Persona | Job |
|---------|-----|
| **Steven Reelwright (Spielberg)** | Cinematic treatment, set pieces, emotional spine, Picture #, greenlight |
| **Andy Warhol Director** | Screen test brief, cast, repetition grid, skill routing |
| **Ted Rhymewell (Seuss)** | Rhyming script, dance beats in verse, moral |

```
User idea
    ↓
[Path S1] Spielberg → SPIELBERG PRODUCER OUT → Warhol → (optional) Seuss → Warhol → Steve greenlight → skills
[Path S2] Spielberg → SPIELBERG RHYME BRIEF → Seuss → SEUSS PROMPT OUT → Warhol → Steve greenlight
[Path S3] Warhol → WARHOL PRODUCER IN → Spielberg → SPIELBERG PRODUCER OUT → Warhol → …
[Path S4] Seuss → SEUSS PRODUCER IN → Spielberg → set pieces → back to Warhol/Seuss
[Path S5] User "all three" → S1 full stack with rhyme layer ON
```

Pair loop (Warhol ↔ Seuss only): `dr-seuss-script-writer/references/warhol-handoff-protocol.md`

---

## Message: SPIELBERG PRODUCER OUT

Steve sends (to Andy + optional Ted):

```markdown
## SPIELBERG PRODUCER OUT
**From:** Steven Reelwright · Picture Division
**Picture #:** 12
**Title:** *The Aisle That Time Forgot*
**Log line:** A ceremonial guard and a kilted potato chase the last glowing freezer light before closing.
**Why audiences care:** Everyone has run through a store at 9:58 PM. This makes that sacred.
**Set pieces:**
  1. Wide — fluorescent aisle, mist rolls, dancers freeze mid-shuffle
  2. Chase — cart slalom between endcaps, Muzz VO under rhyming narrator
  3. Button — silhouette high-five through freezer door; music holds
**Emotional spine:** discovery
**Rhyme layer:** yes
**Hand to Andy:**
  Screen Test #12 · cast: african-chieftain-dance-fighters + scottish-haggis-kilt-dance
  Grid: A supermarket / B neon night market / C B&W / D airport security
  Pipeline: video-creator P2 · 9:16 · ~45s
**Hand to Ted:** SPIELBERG RHYME BRIEF attached below
**Music cue:** Piano wonder theme → brass on chase drop → strings on moral
**Ready for:** andy-warhol-director · dr-seuss-script-writer
— Steve Reelwright
```

---

## Message: SPIELBERG RHYME BRIEF

Steve sends to Ted (embedded in PRODUCER OUT or standalone):

```markdown
## SPIELBERG RHYME BRIEF
**To:** Ted Rhymewell
**From:** Steve Reelwright
**Picture #:** 12
**Rhyme title seed:** *Oh, the Freezer Light at Quarter to Nine*
**Stanza map:**
  - Stanza 1: wonder — mist, wide aisle
  - Stanza 2: chase — cart slalom (grid A/B)
  - Stanza 3: discovery — glowing object
  - Stanza 4: button — reunion dance (grid C/D)
**Dance beats in verse:** must name Shuffle-of-Forms, Fluffle-Stuffle Flap equivalents
**Moral direction:** warm, sideways — "late nights can be holy"
**Then:** SEUSS PROMPT OUT → Andy (Screen Test #12)
```

Ted responds with **SEUSS PROMPT OUT** (see warhol-handoff-protocol.md).

---

## Message: WARHOL PRODUCER IN

Andy requests spectacle polish:

```markdown
## WARHOL PRODUCER IN
**From:** Andy Warhol Director
**Screen Test #:** 12
**Flat log line:** Dancers audit a frozen aisle at closing.
**Cast shortlist:** CAST-06 + CAST-07
**Needs:** set pieces · emotional spine · working title for Picture #
```

Steve responds with **SPIELBERG PRODUCER OUT**.

---

## Message: SEUSS PRODUCER IN

Ted requests blockbuster framing:

```markdown
## SEUSS PRODUCER IN
**From:** Ted Rhymewell
**Rhyme title:** *Oh, the Aisles You'll Flap Upon a Spud*
**Stanzas summary:**
  - Opening wonder in verse
  - Chase couplets
  - Moral on late-night holiness
**Needs:** set-piece shot list · music cues · Picture # greenlight for Andy
```

Steve responds with set-piece table + **SPIELBERG GREENLIGHT ACK** stub.

---

## Warhol Bridge (unchanged)

After Steve's handoff, Andy emits **WARHOL PROMPT IN** → Ted **SEUSS PROMPT OUT** → Andy **SEUSS PROMPT ACK** + Factory brief.

Andy may prefix WARHOL PROMPT IN with:

```markdown
**Producer treatment:** Picture #12 · SPIELBERG PRODUCER OUT attached
```

---

## Message: SPIELBERG GREENLIGHT ACK

Steve closes development:

```markdown
## SPIELBERG GREENLIGHT ACK
Picture #12 — we're making this picture.

**Set pieces locked** — mist wide / cart chase / freezer silhouette button
**Emotional button** — hold on joined hands through glass; strings 3s
**Hand to Andy** — shoot the grid four times; Ted's rhyme is canon VO
**Hand to video-creator** — P2 with SEUSS PROMPT OUT + Factory brief

That's a wrap on development.

— Steve Reelwright
```

---

## Combined Invocation (User)

```
/stephen-spielberg-producer + /andy-warhol-director + /dr-seuss-script-writer
Picture: Filipino TikTok narrator rhymes a padel chase through a cheese shop — blockbuster wonder
```

**Execution order:**
1. Steve — SPIELBERG PRODUCER OUT + SPIELBERG RHYME BRIEF
2. Andy — WARHOL PROMPT IN (references Picture #)
3. Ted — full rhyme + SEUSS PROMPT OUT
4. Andy — SEUSS PROMPT ACK + Factory brief
5. Steve — SPIELBERG GREENLIGHT ACK
6. video-creator P2/P6 per brief

---

## Grok Single-Session

| Only loaded | Behaviour |
|-------------|-----------|
| `stephen-spielberg-producer` | Treatment + SPIELBERG PRODUCER OUT + *"Hand to Andy and Ted"* stubs |
| `andy-warhol-director` + blockbuster ask | WARHOL PRODUCER IN → invoke `/stephen-spielberg-producer` |
| `dr-seuss-script-writer` + spectacle ask | SEUSS PRODUCER IN → invoke `/stephen-spielberg-producer` |
| All three | Path S5 automatic |

---

## File Naming

| Persona | Output path |
|---------|-------------|
| Spielberg | `skits/[kebab-title]-treatment.md` |
| Seuss | `skits/[kebab-rhyme-title].md` |
| Warhol | `skits/[kebab-title]-factory-brief.md` |

---

## Recipe IDs (registry)

| ID | Combo |
|----|-------|
| SWS-01 | Spielberg treatment → Warhol → Seuss → Warhol → video-creator P2 |
| SWS-02 | Spielberg → rhyme brief → Seuss quatrain → Warhol P1 silver wall |
| SWS-03 | Warhol intake → Spielberg set pieces → Seuss → full stack |
| SWS-04 | Seuss script → Spielberg spectacle polish → Warhol production |
| SWS-05 | All three → Fugu P6 with SPIELBERG PRODUCER OUT + SEUSS PROMPT OUT in input |