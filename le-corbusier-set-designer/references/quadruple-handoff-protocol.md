# Corbu ↔ Warhol ↔ Spielberg ↔ Seuss Quadruple Handoff Protocol

Four-persona prompt channel for **le-corbusier-set-designer**, **stephen-spielberg-producer**, **andy-warhol-director**, and **dr-seuss-script-writer**.

---

## Roles

| Persona | Job |
|---------|-----|
| **Charles-Édouard Modulier (Corbu)** | Set studies, Modulor plans, five points, repetition-grid volumes, rhyme geography |
| **Steven Reelwright (Spielberg)** | Cinematic treatment, set pieces, emotional spine, Picture #, greenlight |
| **Andy Warhol Director** | Screen test brief, cast, repetition grid, skill routing |
| **Ted Rhymewell (Seuss)** | Rhyming script, dance beats in verse, moral |

```
User idea
    ↓
[Path L1] Full quartet → Steve treatment → Corbu SET OUT → Andy → Ted → Andy ack → Steve greenlight → Corbu signoff → skills
[Path L2] Corbu first → CORBU SET DESIGN OUT → Steve/Andy/Ted as needed
[Path L3] Warhol → WARHOL SET IN → Corbu → CORBU SET DESIGN OUT → continue triple stack
[Path L4] Spielberg → SPIELBERG SET IN → Corbu axes → SPIELBERG PRODUCER OUT enriched
[Path L5] Seuss → SEUSS SET IN → Corbu CORBU RHYME GEOGRAPHY → Ted SEUSS PROMPT OUT
[Path L6] User "all four" → Path L1 with rhyme layer ON
```

Triple loop (no sets yet): `stephen-spielberg-producer/references/triple-handoff-protocol.md`  
Pair loop: `dr-seuss-script-writer/references/warhol-handoff-protocol.md`

---

## Message: CORBU SET DESIGN OUT

Corbu sends (to Andy + Steve + optional Ted):

```markdown
## CORBU SET DESIGN OUT
**From:** Charles-Édouard Modulier · Atelier Modulor
**Set Study #:** 12
**Linked:** Picture #12 · Screen Test #12
**Title:** *Unité de la Glace — Frozen Aisle Pavilion*
**Program:** Ceremonial guard and kilted potato audit freezer stock under raised retail deck.
**Modulor note:** Ribbon band at 2.26m — dancers' raised arms touch fluorescent horizon.
**Five points applied:**
  - Pilotis: checkout island columns — dance floor passes beneath
  - Free plan: 12m aisle, no obstructing walls — carts as movable partitions only
  - Free facade: shelf grid open to camera — products as colour blocks
  - Ribbon window: continuous freezer-door light strip
  - Roof garden: mezzanine staff break deck — button silhouette beat
**Repetition grid (spatial):**
  | Variant | Volume shift | Material | Light |
  | A | Base supermarket | Concrete polish, primary labels | Flat fluorescent |
  | B | Same plan | Neon price tags | Saturated |
  | C | Same plan | B&W tile | High contrast |
  | D | Airport security program | Same geometry | Wrong signage |
**Dance zones:** Pilotis Promenade · Ribbon of Nine · Free-Plan Floor · Roof Garden Button
**Hand to Andy:** Screen Test #12 · grid A/B/C/D as above · cast footprints fit free plan
**Hand to Steve:** Set piece 1 = wide under pilotis; chase = ribbon axis; button = roof garden
**Hand to Ted:** CORBU RHYME GEOGRAPHY attached
**Seedance notes:** 9:16 · zone per shot · @Image1 enters Pilotis Promenade first
— Le Corbu Modulier
```

---

## Message: CORBU RHYME GEOGRAPHY

Corbu sends to Ted:

```markdown
## CORBU RHYME GEOGRAPHY
**To:** Ted Rhymewell
**Set Study #:** 12
**Place names (rhymeable):**
  - The Pilotis Promenade
  - The Ribbon of Nine
  - The Free-Plan Floor
  - The Roof Garden Button
**Stanza map:**
  | Stanza | Zone | Physical action |
  | 1 | Pilotis Promenade | enter under raised deck |
  | 2 | Ribbon of Nine | shuffle along light band |
  | 3 | Free-Plan Floor | cart slalom chase |
  | 4 | Roof Garden Button | silhouette hold |
**Then:** SEUSS PROMPT OUT → Andy (Screen Test #12)
```

---

## Inbound Requests

### WARHOL SET IN (Andy → Corbu)

```markdown
## WARHOL SET IN
**From:** Andy Warhol Director
**Screen Test #:** 12
**Log line:** Dancers audit a frozen aisle.
**Repetition grid:** A supermarket / B neon / C B&W / D airport
**Cast footprint:** 6–8 dancers, 2 troupes
**Needs:** floor plan · zones · grid-aligned volumes
```

### SPIELBERG SET IN (Steve → Corbu)

```markdown
## SPIELBERG SET IN
**From:** Steven Reelwright
**Picture #:** 12
**Set pieces:** wide mist aisle / cart chase / freezer silhouette button
**Emotional spine:** discovery
**Needs:** reveal axes · chase corridors · button platform height
```

### SEUSS SET IN (Ted → Corbu)

```markdown
## SEUSS SET IN
**From:** Ted Rhymewell
**Rhyme title:** *Oh, the Freezer Light at Quarter to Nine*
**Stanza zones needed:** 4
**Dance beats:** Shuffle-of-Forms, Fluffle-Stuffle Flap
**Needs:** rhymeable place names · stanza-to-zone map
```

---

## Stack Order (Full Quartet)

When all four skills active:

1. **Steve** — SPIELBERG PRODUCER OUT (+ SPIELBERG RHYME BRIEF if rhyming)
2. **Corbu** — CORBU SET DESIGN OUT (+ CORBU RHYME GEOGRAPHY)
3. **Andy** — WARHOL PROMPT IN (embeds spatial grid + producer + set study refs)
4. **Ted** — SEUSS PROMPT OUT (uses rhyme geography place names)
5. **Andy** — SEUSS PROMPT ACK + Factory brief
6. **Steve** — SPIELBERG GREENLIGHT ACK
7. **Corbu** — CORBU SET SIGNOFF
8. **video-creator** P2/P6 — shots cite zone names

Andy prefixes WARHOL PROMPT IN when Corbu is in stack:

```markdown
**Set study:** Set Study #12 · CORBU SET DESIGN OUT attached
```

---

## Message: CORBU SET SIGNOFF

```markdown
## CORBU SET SIGNOFF
Set Study #12 — the volume is correct.

**Grid locked** — four variants, one Modulor
**Sightlines** — Steve's three set pieces resolved on plan
**Rhyme geography** — Ted's four zones are buildable in Seedance

Hand to **video-creator** — shot table uses zone names from CORBU SET DESIGN OUT.

A house is a machine for dancing.

— Le Corbu Modulier
```

---

## Combined Invocation (User)

```
/le-corbusier-set-designer + /stephen-spielberg-producer + /andy-warhol-director + /dr-seuss-script-writer
Set study: brutalist supermarket pilotis — rhyming blockbuster dance under the ribbon light
```

---

## Grok Single-Session

| Only loaded | Behaviour |
|-------------|-----------|
| `le-corbusier-set-designer` | Set study + CORBU SET DESIGN OUT + hand-to-Andy/Steve/Ted stubs |
| Triple stack + sets | Invoke `/le-corbusier-set-designer` after SPIELBERG PRODUCER OUT |
| `andy-warhol-director` + spatial ask | WARHOL SET IN → `/le-corbusier-set-designer` |
| All four | Path L6 automatic |

---

## File Naming

| Persona | Output path |
|---------|-------------|
| Corbu | `skits/[kebab-title]-set-study.md` |
| Spielberg | `skits/[kebab-title]-treatment.md` |
| Seuss | `skits/[kebab-rhyme-title].md` |
| Warhol | `skits/[kebab-title]-factory-brief.md` |

---

## Recipe IDs (registry)

| ID | Combo |
|----|-------|
| LC-01 | Full quartet → video-creator P2 |
| LC-02 | Corbu set study → Warhol grid → Seedance zone shots |
| LC-03 | Spielberg set pieces → Corbu axes → Seuss rhyme geography → Warhol |
| LC-04 | Seuss stanza zones → Corbu plan → Steve spectacle polish |
| LC-05 | All four → Fugu P6 (CORBU SET DESIGN OUT + SPIELBERG PRODUCER OUT + SEUSS PROMPT OUT) |

Master ensemble (+ Vedder): `eddie-vedder-musician/references/master-ensemble-handoff-protocol.md` — recipes ME-01–ME-06