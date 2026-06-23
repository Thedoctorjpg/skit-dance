# Master Ensemble Handoff Protocol

Five-persona prompt channel for the **skit-dance master personalities**:

| Skill | Persona | Role |
|-------|---------|------|
| `andy-warhol-director` | Andy Warhol Director | Screen tests, cast, repetition grid, routing |
| `dr-seuss-script-writer` | Ted Rhymewell | Rhyming scripts, moral, dance beats in verse |
| `stephen-spielberg-producer` | Steven Reelwright | Blockbuster treatment, set pieces, greenlight |
| `le-corbusier-set-designer` | Charles-Édouard Modulier | Modulor sets, zones, spatial grid |
| `eddie-vedder-musician` | Edward Stonevoice | Soundtrack, vocals, cue map, Voxtral blocks |

Sub-protocols: Warhol↔Seuss · triple (Spielberg) · quadruple (Corbu) — see paths at bottom.

---

## Full Stack Order (All Five)

```
User idea
    ↓
1. Steve  — SPIELBERG PRODUCER OUT (+ SPIELBERG RHYME BRIEF if rhyming)
2. Corbu  — CORBU SET DESIGN OUT (+ CORBU RHYME GEOGRAPHY)
3. Eddie  — VEDDER SOUNDTRACK OUT (scores zones + set pieces + grid)
4. Andy   — WARHOL PROMPT IN (embeds all refs)
5. Ted    — SEUSS PROMPT OUT (may weave Eddie's hook meter)
6. Andy   — SEUSS PROMPT ACK + Factory brief
7. Steve  — SPIELBERG GREENLIGHT ACK
8. Corbu  — CORBU SET SIGNOFF
9. Eddie  — VEDDER SESSION SIGNOFF
10. video-creator P2/P6 + Voxtral from Eddie's blocks
```

---

## Message: VEDDER SOUNDTRACK OUT

Eddie sends:

```markdown
## VEDDER SOUNDTRACK OUT
**From:** Edward Stonevoice · Rain Session Studio
**Session #:** 12
**Linked:** Picture #12 · Screen Test #12 · Set Study #12
**Title:** *Ribbon Light Hymn*
**Tempo / key:** 88 BPM · Em
**Vocal direction:** baritone earnest; growl on chase; ukulele on moral
**Original hook (chorus):**
  Under the ribbon where the cold air sings
  We shuffle holy past the frozen things
**Cue map:**
  | Cue | Grid | Zone / set piece | Music |
  | 1 | A | Pilotis wide | fingerpick verse |
  | 2 | B | Ribbon chase | full band drop |
  | 3 | C | Free-plan button | strip to voice + uke |
  | 4 | D | Airport wrong-room | same chords, PA wash |
**Hand to Andy / Steve / Corbu / Ted:** [one line each]
**Ready for:** video-creator · Voxtral TTS
— Eddie Stonevoice
```

---

## Inbound to Eddie

### WARHOL MUSIC IN (Andy → Eddie)

```markdown
## WARHOL MUSIC IN
**From:** Andy Warhol Director
**Screen Test #:** 12
**Repetition grid:** A supermarket / B neon / C B&W / D airport
**Cast VO:** rhyming narrator + optional Superstar accents
**Needs:** sonic palette per grid variant · hook that repeats 4×
```

### SPIELBERG MUSIC IN (Steve → Eddie)

```markdown
## SPIELBERG MUSIC IN
**From:** Steven Reelwright
**Picture #:** 12
**Set pieces:** wide mist / cart chase / silhouette button
**Emotional spine:** discovery
**Steve's music cue:** piano wonder → brass chase → strings moral
**Needs:** Eddie score translating Steve's arc — original lyrics
```

### CORBU MUSIC IN (Corbu → Eddie)

```markdown
## CORBU MUSIC IN
**From:** Charles-Édouard Modulier
**Set Study #:** 12
**Zones:** Pilotis Promenade · Ribbon of Nine · Free-Plan Floor · Roof Garden Button
**Needs:** tempo per zone · dancer count-in · clearance bars
```

### SEUSS MUSIC IN (Ted → Eddie)

```markdown
## SEUSS MUSIC IN
**From:** Ted Rhymewell
**Rhyme title:** *Oh, the Freezer Light at Quarter to Nine*
**Meter:** anapestic tetrameter · 4 stanzas
**Moral couplet:** [text]
**Needs:** singable phrase lengths · optional chorus rhyme with hook
```

Eddie returns **VEDDER SOUNDTRACK OUT** with **verse seeds** matching stanza syllables.

---

## Cross-Persona Quick Reference

| From | To | Block |
|------|-----|-------|
| Steve | Andy, Ted, Corbu, Eddie | SPIELBERG PRODUCER OUT |
| Corbu | All | CORBU SET DESIGN OUT |
| Eddie | All | VEDDER SOUNDTRACK OUT |
| Andy | Ted | WARHOL PROMPT IN |
| Ted | Andy | SEUSS PROMPT OUT |
| Andy | All | SEUSS PROMPT ACK |
| Steve | All | SPIELBERG GREENLIGHT ACK |
| Corbu | All | CORBU SET SIGNOFF |
| Eddie | All | VEDDER SESSION SIGNOFF |

---

## Combined Invocation (User)

```
/eddie-vedder-musician + /le-corbusier-set-designer + /stephen-spielberg-producer + /andy-warhol-director + /dr-seuss-script-writer
Session: original grunge score for rhyming brutalist supermarket dance
```

Shorthand: *"master ensemble"*, *"all five"*, *"full stack"*

---

## Grok Single-Session

| Loaded | Behaviour |
|--------|-----------|
| `eddie-vedder-musician` only | Session brief + VEDDER SOUNDTRACK OUT + hand-to-master stubs |
| Quartet + music | Add Eddie after CORBU SET DESIGN OUT |
| `andy-warhol-director` + score | WARHOL MUSIC IN → `/eddie-vedder-musician` |
| All five | Full stack order above |

---

## File Naming

| Persona | Output path |
|---------|-------------|
| Eddie | `skits/[kebab-title]-soundtrack.md` |
| Corbu | `skits/[kebab-title]-set-study.md` |
| Spielberg | `skits/[kebab-title]-treatment.md` |
| Seuss | `skits/[kebab-rhyme-title].md` |
| Warhol | `skits/[kebab-title]-factory-brief.md` |

---

## Recipe IDs (registry)

| ID | Combo |
|----|-------|
| ME-01 | Full five → video-creator P2 + Voxtral |
| ME-02 | Eddie score only → Andy grid → video-creator P1 |
| ME-03 | Ted rhyme → Eddie meter → Andy → video-creator |
| ME-04 | Steve + Eddie music arc → Corbu → Andy |
| ME-05 | Quartet (no Eddie) — LC-01 |
| ME-06 | All five → Fugu P6 (all prompt blocks in input) |

---

## Sub-Protocols

| Scope | File |
|-------|------|
| Warhol ↔ Seuss | `dr-seuss-script-writer/references/warhol-handoff-protocol.md` |
| + Spielberg | `stephen-spielberg-producer/references/triple-handoff-protocol.md` |
| + Corbu | `le-corbusier-set-designer/references/quadruple-handoff-protocol.md` |
| + Eddie (this file) | `eddie-vedder-musician/references/master-ensemble-handoff-protocol.md` |