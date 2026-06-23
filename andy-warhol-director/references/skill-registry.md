# Skill Registry — Machine Routing Table

Quick lookup for `andy-warhol-director`. Full prose index: `../Andy-Warhol-Director-Master.md`.

---

## Production Skills

| ID | skill name | invoke |
|----|------------|--------|
| PROD-01 | dancing-skit | `/dancing-skit` · `SKILL.md` |
| PROD-02 | video-creator | `/video-creator` · `video-creator/SKILL.md` |
| PROD-03 | seedance-en | `seedance/SKILL.md` |
| PROD-04 | seedance-zh | `seedance/zh/SKILL.md` |
| PROD-05 | swedish-chef-cookoff | `/swedish-chef-cookoff` |
| PROD-06 | dr-seuss-script-writer | `/dr-seuss-script-writer` · `dr-seuss-script-writer/SKILL.md` |
| PROD-07 | stephen-spielberg-producer | `/stephen-spielberg-producer` · `stephen-spielberg-producer/SKILL.md` |
| PROD-08 | le-corbusier-set-designer | `/le-corbusier-set-designer` · `le-corbusier-set-designer/SKILL.md` |
| PROD-09 | eddie-vedder-musician | `/eddie-vedder-musician` · `eddie-vedder-musician/SKILL.md` |
| PROD-10 | adhdloganberry-feed | `/adhdloganberry-feed` · `adhdloganberry-feed/SKILL.md` |

## Fugu Pipelines (via PROD-02)

| ID | file |
|----|------|
| FUGU-P1 | `video-creator/pipelines/p1-dance-meme.md` |
| FUGU-P2 | `video-creator/pipelines/p2-full-skit-video.md` |
| FUGU-P3 | `video-creator/pipelines/p3-reference-dance.md` |
| FUGU-P6 | `video-creator/pipelines/p6-autonomous.md` |

---

## Cast Registry

| ID | skill name | path | voice ref |
|----|------------|------|-----------|
| CAST-01 | aussie-bogan-personality | `aussie-bogan-personality/SKILL.md` | — |
| CAST-02 | british-football-hooligan-personality | `british-football-hooligan-personality/SKILL.md` | — |
| CAST-03 | american-gameshow-announcer | `american-gameshow-announcer/SKILL.md` | — |
| CAST-04 | kiwi-cricket-announcer-personality | `kiwi-cricket-announcer-personality/SKILL.md` | — |
| CAST-05 | canadian-southpark-animator | `canadian-southpark-animator/SKILL.md` | — |
| CAST-06 | scottish-haggis-kilt-dance | `scottish-haggis-kilt-dance/` | `scottish-accent-guide.md` |
| CAST-07 | african-chieftain-dance-fighters | `african-chieftain-dance-fighters/` | `chieftain-voice-guide.md` |
| CAST-08 | chinese-festival-dancers | `chinese-festival-dancers/` | `festival-voice-guide.md` |
| CAST-09 | devout-irish-catholic-personality | `devout-irish-catholic-personality/SKILL.md` | — |
| CAST-10 | muslim-artist-personality | `muslim-artist-personality/SKILL.md` | — |
| CAST-11 | french-mistress-personality | `french-mistress-personality/SKILL.md` | — |
| CAST-12 | italian-shoe-shiner-personality | `italian-shoe-shiner-personality/SKILL.md` | — |
| CAST-13 | russian-hairdresser-personality | `russian-hairdresser-personality/SKILL.md` | — |
| CAST-14 | german-frau-personality | `german-frau-personality/SKILL.md` | — |
| CAST-15 | dutch-cheese-enthusiast-personality | `dutch-cheese-enthusiast-personality/SKILL.md` | — |
| CAST-16 | swiss-banker-personality | `swiss-banker-personality/SKILL.md` | — |
| CAST-17 | korean-gangnam-girl-personality | `korean-gangnam-girl-personality/SKILL.md` | — |
| CAST-18 | pacific-islander-bro-personality | `pacific-islander-bro-personality/SKILL.md` | — |
| CAST-19 | japanese-tourist-personality | `japanese-tourist-personality/SKILL.md` | — |
| CAST-20 | thai-international-student-vlogger-personality | `thai-international-student-vlogger-personality/SKILL.md` | — |
| CAST-21 | filipina-tiktok-personality | `filipina-tiktok-personality/SKILL.md` | — |
| CAST-22 | icelandic-beauty-personality | `icelandic-beauty-personality/SKILL.md` | — |
| CAST-23 | south-american-padel-enthusiast-personality | `south-american-padel-enthusiast-personality/SKILL.md` | — |
| CAST-24 | singaporean-ladies-man-personality | `singaporean-ladies-man-personality/SKILL.md` | — |
| CAST-25 | swedish-chef-cookoff | `swedish-chef-cookoff/SKILL.md` | `references/chef-vocabulary.md` |
| CAST-26 | portuguese-barista-personality | `portuguese-barista-personality/SKILL.md` | — |

## Master Ensemble (production masters)

| ID | skill name | path | role |
|----|------------|------|------|
| MASTER-01 | andy-warhol-director | `andy-warhol-director/SKILL.md` | director · router |
| MASTER-02 | dr-seuss-script-writer | `dr-seuss-script-writer/SKILL.md` | writer |
| MASTER-03 | stephen-spielberg-producer | `stephen-spielberg-producer/SKILL.md` | producer |
| MASTER-04 | le-corbusier-set-designer | `le-corbusier-set-designer/SKILL.md` | set designer |
| MASTER-05 | eddie-vedder-musician | `eddie-vedder-musician/SKILL.md` | musician |

**Full cast assembly (31 + masters):** `references/full-cast-assembly.md`

---

## Asset Paths

| Asset | path |
|-------|------|
| Character @Image1 | `video/assets/character-reference.jpg` |
| Skit→video | `video/prompts/skit-to-video-workflow.md` |
| Wacky scenes | `video/prompts/wacky-dance-scenes.md` |
| Move names | `references/move-names.md` (dancing-skit) |
| Format guide | `references/format-guide.md` (dancing-skit) |

---

## Combo Recipes

| Recipe | Skills |
|--------|--------|
| **Silver Dance Wall** | andy-warhol-director + video-creator P1 + CAST-06/07/08 + seedance-en |
| **Announced Spectacle** | CAST-03 or CAST-04 + dancing-skit + video-creator P2 |
| **Kitchen Screen Test** | swedish-chef-cookoff + canadian-southpark-animator (storyboard) |
| **Global Ensemble** | andy-warhol-director + 4 CAST-* + video-creator P4 |
| **Full Factory** | andy-warhol-director + video-creator P6 + Andy-Warhol-Director-Master.md as context |
| **WS-01 Rhyming skit** | andy-warhol-director → dr-seuss-script-writer → video-creator P2 |
| **WS-02 Rhyme meme wall** | dr-seuss-script-writer (quatrain) → andy-warhol-director → video-creator P1 |
| **WS-03 Rhyme + cast VO** | dr-seuss-script-writer + CAST-* → andy-warhol-director → video-creator P4 |
| **WS-04 Rhyme autonomous** | dr-seuss-script-writer + andy-warhol-director → video-creator P6 (both prompt blocks) |
| **SWS-01 Blockbuster rhyme skit** | stephen-spielberg-producer → andy-warhol-director → dr-seuss-script-writer → video-creator P2 |
| **SWS-02 Wonder meme wall** | stephen-spielberg-producer → dr-seuss-script-writer → andy-warhol-director → video-creator P1 |
| **SWS-03 Warhol → Steve polish** | andy-warhol-director → stephen-spielberg-producer → full stack |
| **SWS-04 Seuss → Steve spectacle** | dr-seuss-script-writer → stephen-spielberg-producer → andy-warhol-director |
| **SWS-05 Triple autonomous** | all three → video-creator P6 (SPIELBERG PRODUCER OUT + SEUSS PROMPT OUT) |
| **LC-01 Full quartet** | le-corbusier-set-designer + stephen-spielberg-producer + andy-warhol-director + dr-seuss-script-writer → video-creator P2 |
| **LC-02 Modulor grid** | le-corbusier-set-designer → andy-warhol-director → seedance-en zone shots |
| **LC-03 Steve → Corbu → Ted** | stephen-spielberg-producer → le-corbusier-set-designer → dr-seuss-script-writer → andy-warhol-director |
| **LC-04 Ted zones → Corbu plan** | dr-seuss-script-writer → le-corbusier-set-designer → stephen-spielberg-producer → andy-warhol-director |
| **LC-05 Quartet autonomous** | all four → video-creator P6 (CORBU SET DESIGN OUT + SPIELBERG PRODUCER OUT + SEUSS PROMPT OUT) |
| **ME-01 Full master ensemble** | all five PROD-06–09 + andy-warhol-director → video-creator P2 + Voxtral |
| **ME-02 Vedder score wall** | eddie-vedder-musician → andy-warhol-director → video-creator P1 |
| **ME-03 Rhyme + score** | dr-seuss-script-writer → eddie-vedder-musician → andy-warhol-director |
| **ME-04 Steve music arc** | stephen-spielberg-producer → eddie-vedder-musician → le-corbusier-set-designer → andy-warhol-director |
| **ME-06 Ensemble autonomous** | all five → video-creator P6 (all master prompt blocks) |
| **CA-01 Full Factory Wall** | all CAST-01–26 → video-creator P4 personality montage |
| **CA-02 Master + 4 Superstars** | MASTER-* + 4 CAST-* → video-creator P2 |
| **CA-03 Global regional grid** | CAST-01–24 rotate on repetition grid → P1 |
| **CA-04 Troupe triple + announcer** | CAST-06/07/08 + CAST-03 or 04 → P2 |
| **CA-05 Full cast + master ensemble** | CA-01 + ME-01 → video-creator P6 |

Handoff protocols: `dr-seuss-script-writer/references/warhol-handoff-protocol.md` · `stephen-spielberg-producer/references/triple-handoff-protocol.md` · `le-corbusier-set-designer/references/quadruple-handoff-protocol.md` · `eddie-vedder-musician/references/master-ensemble-handoff-protocol.md`

---

## Trigger → Skill (auto-route)

| User says | Route to |
|-----------|----------|
| warhol / factory / screen test | andy-warhol-director (this) |
| skit / acts / choreography script | PROD-01 |
| video / imagine / seedance / fugu | PROD-02 |
| chef / cook-off / muppet | PROD-05 |
| [personality name] | matching CAST-* |
| list skills / cast | Andy-Warhol-Director-Master.md |
| rhyme / seuss / write in verse | PROD-06 (+ andy-warhol-director for Factory) |
| warhol + seuss / both | andy-warhol-director + PROD-06 (handoff protocol) |
| spielberg / speilburg / blockbuster producer | PROD-07 (+ andy-warhol-director + PROD-06 for triple stack) |
| all three / wonder + rhyme + factory | PROD-07 + andy-warhol-director + PROD-06 (triple handoff) |
| corbu / le corbusier / modulor / set design | PROD-08 (+ PROD-07 + PROD-06 for full quartet) |
| all four / brutalist + wonder + rhyme | PROD-08 + PROD-07 + andy-warhol-director + PROD-06 (quadruple handoff) |
| vedder / vetter / eddie / soundtrack / score | PROD-09 (+ other masters for ME-01) |
| master ensemble / all five / full stack | PROD-06–09 + andy-warhol-director (master-ensemble handoff) |
| ADHDloganberry / post to X / twitter feed | PROD-10 (+ PROD-02 video-creator) |
| cast all / full cast / assemble cast / factory wall everyone | `references/full-cast-assembly.md` → CA-01 |