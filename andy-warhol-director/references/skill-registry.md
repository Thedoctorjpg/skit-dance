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

Handoff protocol: `dr-seuss-script-writer/references/warhol-handoff-protocol.md`

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