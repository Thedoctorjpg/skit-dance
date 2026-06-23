# skit-dance

Agent skills, example scripts, and video prompts for absurdist comedy — dancing skits, Swedish Chef cook-offs, and Seedance 2.0 video.

## What's in here

| Path | Skill | Description |
|------|-------|-------------|
| `andy-warhol-director/` | **andy-warhol-director** | **Master director** — Factory persona routing all skills ([Master index](andy-warhol-director/Andy-Warhol-Director-Master.md)) |
| `dr-seuss-script-writer/` | **dr-seuss-script-writer** | Ted Rhymewell — rhyming Seuss-style scripts; Warhol prompt handoff partner |
| `stephen-spielberg-producer/` | **stephen-spielberg-producer** | Steve Reelwright — blockbuster producer; Warhol & Seuss triple handoff |
| `le-corbusier-set-designer/` | **le-corbusier-set-designer** | Le Corbu Modulier — modernist set designer; Warhol, Spielberg & Seuss quartet handoff |
| `eddie-vedder-musician/` | **eddie-vedder-musician** | Eddie Stonevoice — grunge-folk soundtrack; master ensemble handoff with all masters |
| `video-creator/` | **video-creator** | End-to-end video: Fugu orchestration + Imagine/Seedance + Voxtral + FFmpeg |
| `video-creator/pipelines/` | — | Sakana Fugu ready-made pipeline prompts (P1–P6) |
| `SKILL.md` + `references/` | **dancing-skit** | Monty Python-style dance skit scripts |
| `swedish-chef-cookoff/` | **swedish-chef-cookoff** | Muppets Swedish Chef cook-off challenges |
| `aussie-bogan-personality/` | **aussie-bogan-personality** | Dazza — loveable Aussie bogan larrikin persona |
| `british-football-hooligan-personality/` | **british-football-hooligan-personality** | Gaz Hollis — terrace banter & match-day lad chaos |
| `american-gameshow-announcer/` | **american-gameshow-announcer** | Chip Lexington — classic TV game show announcer |
| `kiwi-cricket-announcer-personality/` | **kiwi-cricket-announcer-personality** | Murray "Muzz" Clegg — NZ cricket commentary & good areas |
| `canadian-southpark-animator/` | **canadian-southpark-animator** | Gord McKenzie — construction-paper satire animator |
| `scottish-haggis-kilt-dance/` | **scottish-haggis-kilt-dance** | Kilted haggis dance memes — strong Scots accent |
| `devout-irish-catholic-personality/` | **devout-irish-catholic-personality** | Declan O'Sullivan — warm parish faith & sure look it |
| `muslim-artist-personality/` | **muslim-artist-personality** | Yusuf Rahman — geometry, calligraphy & faith-informed craft |
| `african-chieftain-dance-fighters/` | **african-chieftain-dance-fighters** | Chief Jabari — ceremonial guard dance/fighter memes |
| `chinese-festival-dancers/` | **chinese-festival-dancers** | Captain Wei — Jade Lantern Troupe fan/lion/ribbon memes |
| `french-mistress-personality/` | **french-mistress-personality** | Colette Duval — dramatic French mistress camp |
| `italian-shoe-shiner-personality/` | **italian-shoe-shiner-personality** | Giuseppe "Beppe" Rossini — sciuscià craftsman pride |
| `russian-hairdresser-personality/` | **russian-hairdresser-personality** | Svetlana "Sveta" Volkova — salon bluntness & layers |
| `german-frau-personality/` | **german-frau-personality** | Ingrid Hofmeister — stern German Frau, Ordnung & warmth |
| `dutch-cheese-enthusiast-personality/` | **dutch-cheese-enthusiast-personality** | Pieter van der Berg — gezellig kaas devotion |
| `swiss-banker-personality/` | **swiss-banker-personality** | Klaus Meier — Zürich precision, discretion & ledger calm |
| `korean-gangnam-girl-personality/` | **korean-gangnam-girl-personality** | Park Min-ju — Gangnam K-beauty & cafe influencer chic |
| `pacific-islander-bro-personality/` | **pacific-islander-bro-personality** | Sione "Sio" Tuala — Pasifika cuz energy & aiga warmth |
| `japanese-tourist-personality/` | **japanese-tourist-personality** | Yuki Nakamura — enthusiastic tourist wonder & polite chaos |
| `thai-international-student-vlogger-personality/` | **thai-international-student-vlogger-personality** | Natt Srisuk — study-abroad vlog diary & sabai chaos |
| `filipina-tiktok-personality/` | **filipina-tiktok-personality** | Beatrice "Bea" Dela Cruz — Taglish TikTok storytime & slay |
| `icelandic-beauty-personality/` | **icelandic-beauty-personality** | Elín Jónsdóttir — Nordic minimal beauty & þetta reddast |
| `south-american-padel-enthusiast-personality/` | **south-american-padel-enthusiast-personality** | Diego Morales — pádel passion, dale & volea metaphors |
| `singaporean-ladies-man-personality/` | **singaporean-ladies-man-personality** | Marcus "MJ" Tan — Singlish smooth charm & steady lah |
| `seedance/` | **seedance-prompt-en/zh** | Seedance 2.0 video prompt writing ([dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill)) |
| `skits/` | — | Example production-ready dancing skit scripts |
| `memes/` | — | Short dance meme caption packs (Scottish, chieftain guard, Chinese festival) |
| `video/assets/` | — | Character reference image for @Image1 |
| `video/prompts/` | — | Seedance prompts + skit→video workflow |

## Install

```powershell
git clone https://github.com/Thedoctorjpg/skit-dance.git
cd skit-dance

# Andy Warhol Director — master router (install first)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\andy-warhol-director" | Out-Null
Copy-Item -Recurse andy-warhol-director\* "$env:USERPROFILE\.grok\skills\andy-warhol-director\"

# Dr. Seuss script writer — rhyming Factory writer (pairs with Warhol)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\dr-seuss-script-writer" | Out-Null
Copy-Item -Recurse dr-seuss-script-writer\* "$env:USERPROFILE\.grok\skills\dr-seuss-script-writer\"

# Stephen Spielberg producer — blockbuster greenlight (pairs with Warhol & Seuss)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\stephen-spielberg-producer" | Out-Null
Copy-Item -Recurse stephen-spielberg-producer\* "$env:USERPROFILE\.grok\skills\stephen-spielberg-producer\"

# Le Corbusier set designer — Modulor volumes (pairs with Warhol, Spielberg & Seuss)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\le-corbusier-set-designer" | Out-Null
Copy-Item -Recurse le-corbusier-set-designer\* "$env:USERPROFILE\.grok\skills\le-corbusier-set-designer\"

# Eddie Vedder musician — soundtrack & vocals (master ensemble)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\eddie-vedder-musician" | Out-Null
Copy-Item -Recurse eddie-vedder-musician\* "$env:USERPROFILE\.grok\skills\eddie-vedder-musician\"

# Video creator skill (Imagine + Seedance + Voxtral + FFmpeg)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\video-creator" | Out-Null
Copy-Item -Recurse video-creator\* "$env:USERPROFILE\.grok\skills\video-creator\"

# Dancing skit script skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\dancing-skit" | Out-Null
Copy-Item SKILL.md "$env:USERPROFILE\.grok\skills\dancing-skit\SKILL.md"
Copy-Item -Recurse references "$env:USERPROFILE\.grok\skills\dancing-skit\references"

# Swedish Chef cook-off skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\swedish-chef-cookoff" | Out-Null
Copy-Item -Recurse swedish-chef-cookoff\* "$env:USERPROFILE\.grok\skills\swedish-chef-cookoff\"

# Aussie bogan personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\aussie-bogan-personality" | Out-Null
Copy-Item aussie-bogan-personality\SKILL.md "$env:USERPROFILE\.grok\skills\aussie-bogan-personality\SKILL.md"

# British football hooligan personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\british-football-hooligan-personality" | Out-Null
Copy-Item british-football-hooligan-personality\SKILL.md "$env:USERPROFILE\.grok\skills\british-football-hooligan-personality\SKILL.md"

# American game show announcer skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\american-gameshow-announcer" | Out-Null
Copy-Item american-gameshow-announcer\SKILL.md "$env:USERPROFILE\.grok\skills\american-gameshow-announcer\SKILL.md"

# Kiwi cricket announcer personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\kiwi-cricket-announcer-personality" | Out-Null
Copy-Item kiwi-cricket-announcer-personality\SKILL.md "$env:USERPROFILE\.grok\skills\kiwi-cricket-announcer-personality\SKILL.md"

# Canadian South Park style animator skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\canadian-southpark-animator" | Out-Null
Copy-Item canadian-southpark-animator\SKILL.md "$env:USERPROFILE\.grok\skills\canadian-southpark-animator\SKILL.md"

# Scottish haggis kilt dance memes skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\scottish-haggis-kilt-dance" | Out-Null
Copy-Item -Recurse scottish-haggis-kilt-dance\* "$env:USERPROFILE\.grok\skills\scottish-haggis-kilt-dance\"

# African chieftain dance fighters skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\african-chieftain-dance-fighters" | Out-Null
Copy-Item -Recurse african-chieftain-dance-fighters\* "$env:USERPROFILE\.grok\skills\african-chieftain-dance-fighters\"

# Chinese festival dancers skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\chinese-festival-dancers" | Out-Null
Copy-Item -Recurse chinese-festival-dancers\* "$env:USERPROFILE\.grok\skills\chinese-festival-dancers\"

# French mistress personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\french-mistress-personality" | Out-Null
Copy-Item french-mistress-personality\SKILL.md "$env:USERPROFILE\.grok\skills\french-mistress-personality\SKILL.md"

# Italian shoe shiner personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\italian-shoe-shiner-personality" | Out-Null
Copy-Item italian-shoe-shiner-personality\SKILL.md "$env:USERPROFILE\.grok\skills\italian-shoe-shiner-personality\SKILL.md"

# Russian hairdresser personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\russian-hairdresser-personality" | Out-Null
Copy-Item russian-hairdresser-personality\SKILL.md "$env:USERPROFILE\.grok\skills\russian-hairdresser-personality\SKILL.md"

# German frau personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\german-frau-personality" | Out-Null
Copy-Item german-frau-personality\SKILL.md "$env:USERPROFILE\.grok\skills\german-frau-personality\SKILL.md"

# Dutch cheese enthusiast personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\dutch-cheese-enthusiast-personality" | Out-Null
Copy-Item dutch-cheese-enthusiast-personality\SKILL.md "$env:USERPROFILE\.grok\skills\dutch-cheese-enthusiast-personality\SKILL.md"

# Swiss banker personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\swiss-banker-personality" | Out-Null
Copy-Item swiss-banker-personality\SKILL.md "$env:USERPROFILE\.grok\skills\swiss-banker-personality\SKILL.md"

# Korean Gangnam girl personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\korean-gangnam-girl-personality" | Out-Null
Copy-Item korean-gangnam-girl-personality\SKILL.md "$env:USERPROFILE\.grok\skills\korean-gangnam-girl-personality\SKILL.md"

# Pacific Islander bro personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\pacific-islander-bro-personality" | Out-Null
Copy-Item pacific-islander-bro-personality\SKILL.md "$env:USERPROFILE\.grok\skills\pacific-islander-bro-personality\SKILL.md"

# Japanese tourist personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\japanese-tourist-personality" | Out-Null
Copy-Item japanese-tourist-personality\SKILL.md "$env:USERPROFILE\.grok\skills\japanese-tourist-personality\SKILL.md"

# Thai international student vlogger personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\thai-international-student-vlogger-personality" | Out-Null
Copy-Item thai-international-student-vlogger-personality\SKILL.md "$env:USERPROFILE\.grok\skills\thai-international-student-vlogger-personality\SKILL.md"

# Singaporean ladies man personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\singaporean-ladies-man-personality" | Out-Null
Copy-Item singaporean-ladies-man-personality\SKILL.md "$env:USERPROFILE\.grok\skills\singaporean-ladies-man-personality\SKILL.md"

# Devout Irish Catholic personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\devout-irish-catholic-personality" | Out-Null
Copy-Item devout-irish-catholic-personality\SKILL.md "$env:USERPROFILE\.grok\skills\devout-irish-catholic-personality\SKILL.md"

# Muslim artist personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\muslim-artist-personality" | Out-Null
Copy-Item muslim-artist-personality\SKILL.md "$env:USERPROFILE\.grok\skills\muslim-artist-personality\SKILL.md"

# Filipina TikTok personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\filipina-tiktok-personality" | Out-Null
Copy-Item filipina-tiktok-personality\SKILL.md "$env:USERPROFILE\.grok\skills\filipina-tiktok-personality\SKILL.md"

# Icelandic beauty personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\icelandic-beauty-personality" | Out-Null
Copy-Item icelandic-beauty-personality\SKILL.md "$env:USERPROFILE\.grok\skills\icelandic-beauty-personality\SKILL.md"

# South American padel enthusiast personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\south-american-padel-enthusiast-personality" | Out-Null
Copy-Item south-american-padel-enthusiast-personality\SKILL.md "$env:USERPROFILE\.grok\skills\south-american-padel-enthusiast-personality\SKILL.md"

# Seedance prompt skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\seedance-prompt-en" | Out-Null
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\seedance-prompt-zh" | Out-Null
Copy-Item seedance\SKILL.md "$env:USERPROFILE\.grok\skills\seedance-prompt-en\SKILL.md"
Copy-Item seedance\zh\SKILL.md "$env:USERPROFILE\.grok\skills\seedance-prompt-zh\SKILL.md"
```

## Usage

### Andy Warhol Director (master)

```
/andy-warhol-director cast Muzz narrating Chinese festival dancers at IKEA — silver wall 4×
```

Or: *"Factory mode"*, *"screen test"*, *"Warhol director"*

**Full cast assembly (all 30 personality skills):**

```
/andy-warhol-director cast all — Factory wall, everyone dances the same beat 4×
```

Roster: [`andy-warhol-director/references/full-cast-assembly.md`](andy-warhol-director/references/full-cast-assembly.md)

Master index linking every skill: [`andy-warhol-director/Andy-Warhol-Director-Master.md`](andy-warhol-director/Andy-Warhol-Director-Master.md)

### Eddie Vedder musician + master ensemble (all five)

```
/eddie-vedder-musician + /le-corbusier-set-designer + /stephen-spielberg-producer + /andy-warhol-director + /dr-seuss-script-writer
Session: grunge-folk score for rhyming brutalist supermarket dance — full master ensemble
```

Or: *"Eddie Vedder musician"*, *"Eddie Vetter"* (common misspelling), *"Vedder soundtrack"*, *"master ensemble"*, *"all five"*

Master ensemble handoff: [`eddie-vedder-musician/references/master-ensemble-handoff-protocol.md`](eddie-vedder-musician/references/master-ensemble-handoff-protocol.md)

```
/eddie-vedder-musician original baritone hook for a Factory screen test dance skit
```

### Le Corbusier set designer + Warhol + Spielberg + Seuss (full quartet)

```
/le-corbusier-set-designer + /stephen-spielberg-producer + /andy-warhol-director + /dr-seuss-script-writer
Set study: brutalist supermarket pilotis — Chief Jabari rhymes under the ribbon light, blockbuster wonder
```

Or: *"Le Corbusier set designer"*, *"Corbu sets"*, *"modulor stage"*, *"all four personas"*

Quadruple handoff: [`le-corbusier-set-designer/references/quadruple-handoff-protocol.md`](le-corbusier-set-designer/references/quadruple-handoff-protocol.md)

```
/le-corbusier-set-designer Modulor floor plan for a dance skit in a fluorescent aisle
```

### Stephen Spielberg producer + Warhol + Seuss (triple stack)

```
/stephen-spielberg-producer + /andy-warhol-director + /dr-seuss-script-writer
Picture: Chief Jabari chases a glowing haggis through aisle 7 — rhyming blockbuster wonder
```

Or: *"Spielberg producer"*, *"Speilburg producer"*, *"blockbuster wonder"*, *"all three personas"*

Triple handoff: [`stephen-spielberg-producer/references/triple-handoff-protocol.md`](stephen-spielberg-producer/references/triple-handoff-protocol.md)

```
/stephen-spielberg-producer cinematic treatment for padel chase in a cheese shop
```

### Dr. Seuss script writer + Warhol combo

```
/andy-warhol-director + /dr-seuss-script-writer
Screen test: Kiwi announcer rhymes about padel dancers in a cheese shop
```

Or: *"write it in rhyme"*, *"Seuss-style skit"*, *"Warhol and Seuss"*

Handoff protocol: [`dr-seuss-script-writer/references/warhol-handoff-protocol.md`](dr-seuss-script-writer/references/warhol-handoff-protocol.md)

```
/dr-seuss-script-writer rhyming dance skit about haggis at airport security
```

### Dancing skit

```
/dancing-skit job interview where the candidate dances their CV
```

Example: [`skits/the-supermarket-shuffle.md`](skits/the-supermarket-shuffle.md)

### Swedish Chef cook-off

```
/swedish-chef-cookoff submarine mystery basket with rubber chicken and flörgen
```

### Aussie bogan mode

```
G'day Dazza
```

Or: *"bogan mode on"* / *"talk like an Aussie bogan"*

### British football hooligan mode

```
Oi oi, Gaz
```

Or: *"hooligan mode on"* / *"football hooligan mode"*

### Game show announcer mode

```
Chip Lexington, take it away!
```

Or: *"announcer mode on"* / *"game show mode"*

### Kiwi cricket announcer mode

```
Kia ora, Muzz
```

Or: *"cricket announcer mode on"* / *"Kiwi cricket mode"*

### Canadian animator mode

```
Gord, roll the cardboard
```

Or: *"south park style on"* / *"animator mode on"*

### Scottish kilt & haggis dance memes

```
/scottish-haggis-kilt-dance airport security Highland fling
```

Memes: [`memes/scottish-haggis-kilt-dance-memes.md`](memes/scottish-haggis-kilt-dance-memes.md)  
Skit: [`skits/the-haggis-highland-fling.md`](skits/the-haggis-highland-fling.md)  
Seedance: [`video/prompts/scottish-kilt-dance-memes.md`](video/prompts/scottish-kilt-dance-memes.md)

### African chieftain dance fighters

```
/african-chieftain-dance-fighters spear salute at the self-checkout
```

Or: *"Chief Jabari, assemble the dancers"* / *"ceremony mode on"*

Memes: [`memes/african-chieftain-dance-fighters-memes.md`](memes/african-chieftain-dance-fighters-memes.md)  
Seedance: [`video/prompts/african-chieftain-dance-fighters.md`](video/prompts/african-chieftain-dance-fighters.md)

### Chinese festival dancers

```
/chinese-festival-dancers lion head at the self-checkout
```

Or: *"Captain Wei, cue the troupe"* / *"festival dance mode on"*

Memes: [`memes/chinese-festival-dancers-memes.md`](memes/chinese-festival-dancers-memes.md)  
Seedance: [`video/prompts/chinese-festival-dancers.md`](video/prompts/chinese-festival-dancers.md)

### French mistress mode

```
Enchantée, Colette
```

Or: *"mistress mode on"* / *"French mistress mode"*

### Italian shoe shiner mode

```
Buongiorno, Beppe
```

Or: *"shoe shiner mode on"* / *"Italian shoe shiner mode"*

### Russian hairdresser mode

```
Zdravstvuyte, Sveta
```

Or: *"hairdresser mode on"* / *"Russian hairdresser mode"*

### German frau mode

```
Guten Tag, Ingrid
```

Or: *"Frau mode on"* / *"German frau mode"*

### Dutch cheese enthusiast mode

```
Goedemorgen, Pieter
```

Or: *"cheese mode on"* / *"Dutch cheese mode"*

### Swiss banker mode

```
Grüezi, Klaus
```

Or: *"Swiss banker mode on"* / *"banker mode — Klaus"*

### Korean Gangnam girl mode

```
Annyeong, Min-ju
```

Or: *"Gangnam mode on"* / *"Gangnam girl mode"* (also *"ganganam girl"*)

### Pacific Islander bro mode

```
Talofa, Sio
```

Or: *"island bro mode on"* / *"Pacific bro mode"*

### Japanese tourist mode

```
Konnichiwa, Yuki
```

Or: *"tourist mode on"* / *"Japanese tourist mode"*

### Thai international student vlogger mode

```
Sawasdee krub, Natt
```

Or: *"vlogger mode on"* / *"Thai student vlogger mode"*

### Singaporean ladies man mode

```
Eh Marcus, steady lah
```

Or: *"ladies man mode on"* / *"Singaporean ladies man mode"*

### Devout Irish Catholic mode

```
Dia duit, Declan
```

Or: *"Irish Catholic mode on"* / *"devout Irish Catholic mode"*

### Muslim artist mode

```
As-salamu alaykum, Yusuf
```

Or: *"Muslim artist mode on"* / *"artist mode — Yusuf"*

### Filipina TikTok mode

```
Kumusta, Bea
```

Or: *"TikTok mode on"* / *"Filipina TikTok mode"*

### Icelandic beauty mode

```
Góðan daginn, Elín
```

Or: *"Icelandic beauty mode on"* / *"Icelandlic beauty mode"*

### South American padel enthusiast mode

```
Qué tal, Diego
```

Or: *"padel mode on"* / *"South American padel mode"*

### Seedance video prompts

Use [`video/prompts/wacky-dance-scenes.md`](video/prompts/wacky-dance-scenes.md), or [`video/prompts/skit-to-video-workflow.md`](video/prompts/skit-to-video-workflow.md) to convert a skit into Seedance clips.

### Video creator (full pipeline)

```
/video-creator wacky dance montage with Scottish narrator
```

Or: `/imagine-video`, *"make a narrated skit video"*, *"Voxtral voice-over"*, *"Fugu pipeline P3"*

**Orchestration:** [Sakana Fugu](https://sakana.ai/fugu) pipelines P1–P6 via `SAKANA_API_KEY` → [`video-creator/references/fugu-orchestration-pipelines.md`](video-creator/references/fugu-orchestration-pipelines.md)

**Direct (no Fugu):** script → shot plan → Imagine/Seedance → Voxtral → FFmpeg. See [`video-creator/SKILL.md`](video-creator/SKILL.md).

| Pipeline | Prompt file |
|----------|-------------|
| P1 Dance meme | [`pipelines/p1-dance-meme.md`](video-creator/pipelines/p1-dance-meme.md) |
| P2 Full skit | [`pipelines/p2-full-skit-video.md`](video-creator/pipelines/p2-full-skit-video.md) |
| P3 Reference dance | [`pipelines/p3-reference-dance.md`](video-creator/pipelines/p3-reference-dance.md) |
| P6 Autonomous | [`pipelines/p6-autonomous.md`](video-creator/pipelines/p6-autonomous.md) |

### Full dance pipeline

1. `/dancing-skit` → production `.md` script
2. `/video-creator` → shot table + Voxtral TTS blocks + FFmpeg commands
3. Map acts to Seedance prompts (workflow doc)
4. Upload `video/assets/character-reference.jpg` as @Image1 in [Jimeng Seedance 2.0](https://jimeng.jianying.com/)
5. Generate clips → Voxtral voice → FFmpeg concat + mux

## Credits

- **andy-warhol-director** — master router persona; Factory homage (not affiliated with AWF/estate)
- **dr-seuss-script-writer** — Ted Rhymewell rhyming writer; Seuss-style homage (not affiliated with Seuss Enterprises)
- **stephen-spielberg-producer** — Steve Reelwright blockbuster producer; Spielberg-style homage (not affiliated with Amblin/estate)
- **le-corbusier-set-designer** — Charles-Édouard Modulier set designer; Le Corbusier-style homage (1887–1965, Switzerland/France; not affiliated with Fondation Le Corbusier)
- **eddie-vedder-musician** — Edward Stonevoice musician; Vedder-style homage (not affiliated with Pearl Jam/estate; original lyrics only)
- **video-creator** — original skill; [Sakana Fugu](https://sakana.ai/fugu) orchestration; Voxtral via [Julia Turc](https://x.com/juliarturc/status/2069096367155507257) / [Mistral](https://mistral.ai/news/voxtral/)
- **dancing-skit** — original skill for this repo
- **swedish-chef-cookoff** — original skill for this repo (Muppet Show parody; not affiliated with Disney/Muppets)
- **aussie-bogan-personality** — original skill for this repo
- **british-football-hooligan-personality** — original skill for this repo (comedy persona; not glorifying real violence)
- **american-gameshow-announcer** — original skill for this repo
- **kiwi-cricket-announcer-personality** — original skill for this repo
- **canadian-southpark-animator** — original skill for this repo (style homage; not affiliated with South Park/Comedy Central)
- **scottish-haggis-kilt-dance** — original skill for this repo
- **african-chieftain-dance-fighters** — original skill for this repo (fictional ceremonial troupe; not affiliated with any real kingdom or ethnic group)
- **chinese-festival-dancers** — original skill for this repo (fictional Jade Lantern Troupe; not affiliated with any real performance group or ethnic tradition)
- **french-mistress-personality** — original skill for this repo
- **italian-shoe-shiner-personality** — original skill for this repo
- **russian-hairdresser-personality** — original skill for this repo
- **german-frau-personality** — original skill for this repo
- **dutch-cheese-enthusiast-personality** — original skill for this repo
- **swiss-banker-personality** — original skill for this repo
- **korean-gangnam-girl-personality** — original skill for this repo
- **pacific-islander-bro-personality** — original skill for this repo
- **japanese-tourist-personality** — original skill for this repo
- **thai-international-student-vlogger-personality** — original skill for this repo
- **singaporean-ladies-man-personality** — original skill for this repo
- **devout-irish-catholic-personality** — original skill for this repo
- **muslim-artist-personality** — original skill for this repo
- **filipina-tiktok-personality** — original skill for this repo
- **icelandic-beauty-personality** — original skill for this repo
- **south-american-padel-enthusiast-personality** — original skill for this repo
- **seedance/** — adapted from [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) (MIT)
- Wacky dance scene prompts inspired by [KakuDrop's Seedance 2.0 demo](https://x.com/KakuDrop/status/2069181320010543409)