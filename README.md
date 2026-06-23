# skit-dance

Agent skills, example scripts, and video prompts for absurdist comedy — dancing skits, Swedish Chef cook-offs, and Seedance 2.0 video.

## What's in here

| Path | Skill | Description |
|------|-------|-------------|
| `SKILL.md` + `references/` | **dancing-skit** | Monty Python-style dance skit scripts |
| `swedish-chef-cookoff/` | **swedish-chef-cookoff** | Muppets Swedish Chef cook-off challenges |
| `aussie-bogan-personality/` | **aussie-bogan-personality** | Dazza — loveable Aussie bogan larrikin persona |
| `british-football-hooligan-personality/` | **british-football-hooligan-personality** | Gaz Hollis — terrace banter & match-day lad chaos |
| `american-gameshow-announcer/` | **american-gameshow-announcer** | Chip Lexington — classic TV game show announcer |
| `kiwi-cricket-announcer-personality/` | **kiwi-cricket-announcer-personality** | Murray "Muzz" Clegg — NZ cricket commentary & good areas |
| `canadian-southpark-animator/` | **canadian-southpark-animator** | Gord McKenzie — construction-paper satire animator |
| `scottish-haggis-kilt-dance/` | **scottish-haggis-kilt-dance** | Kilted haggis dance memes — strong Scots accent |
| `devout-irish-catholic-personality/` | **devout-irish-catholic-personality** | Declan O'Sullivan — warm parish faith & sure look it |
| `african-chieftain-dance-fighters/` | **african-chieftain-dance-fighters** | Chief Jabari — ceremonial guard dance/fighter memes |
| `french-mistress-personality/` | **french-mistress-personality** | Colette Duval — dramatic French mistress camp |
| `italian-shoe-shiner-personality/` | **italian-shoe-shiner-personality** | Giuseppe "Beppe" Rossini — sciuscià craftsman pride |
| `russian-hairdresser-personality/` | **russian-hairdresser-personality** | Svetlana "Sveta" Volkova — salon bluntness & layers |
| `german-frau-personality/` | **german-frau-personality** | Ingrid Hofmeister — stern German Frau, Ordnung & warmth |
| `dutch-cheese-enthusiast-personality/` | **dutch-cheese-enthusiast-personality** | Pieter van der Berg — gezellig kaas devotion |
| `korean-gangnam-girl-personality/` | **korean-gangnam-girl-personality** | Park Min-ju — Gangnam K-beauty & cafe influencer chic |
| `pacific-islander-bro-personality/` | **pacific-islander-bro-personality** | Sione "Sio" Tuala — Pasifika cuz energy & aiga warmth |
| `japanese-tourist-personality/` | **japanese-tourist-personality** | Yuki Nakamura — enthusiastic tourist wonder & polite chaos |
| `thai-international-student-vlogger-personality/` | **thai-international-student-vlogger-personality** | Natt Srisuk — study-abroad vlog diary & sabai chaos |
| `singaporean-ladies-man-personality/` | **singaporean-ladies-man-personality** | Marcus "MJ" Tan — Singlish smooth charm & steady lah |
| `seedance/` | **seedance-prompt-en/zh** | Seedance 2.0 video prompt writing ([dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill)) |
| `skits/` | — | Example production-ready dancing skit scripts |
| `memes/` | — | Short dance meme caption packs (Scottish kilt/haggis, chieftain guard) |
| `video/assets/` | — | Character reference image for @Image1 |
| `video/prompts/` | — | Seedance prompts + skit→video workflow |

## Install

```powershell
git clone https://github.com/Thedoctorjpg/skit-dance.git
cd skit-dance

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

# Seedance prompt skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\seedance-prompt-en" | Out-Null
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\seedance-prompt-zh" | Out-Null
Copy-Item seedance\SKILL.md "$env:USERPROFILE\.grok\skills\seedance-prompt-en\SKILL.md"
Copy-Item seedance\zh\SKILL.md "$env:USERPROFILE\.grok\skills\seedance-prompt-zh\SKILL.md"
```

## Usage

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

### Seedance video prompts

Use [`video/prompts/wacky-dance-scenes.md`](video/prompts/wacky-dance-scenes.md), or [`video/prompts/skit-to-video-workflow.md`](video/prompts/skit-to-video-workflow.md) to convert a skit into Seedance clips.

### Full dance pipeline

1. `/dancing-skit` → production `.md` script
2. Map acts to Seedance prompts (workflow doc)
3. Upload `video/assets/character-reference.jpg` as @Image1 in [Jimeng Seedance 2.0](https://jimeng.jianying.com/)
4. Generate clips → FFmpeg concat

## Credits

- **dancing-skit** — original skill for this repo
- **swedish-chef-cookoff** — original skill for this repo (Muppet Show parody; not affiliated with Disney/Muppets)
- **aussie-bogan-personality** — original skill for this repo
- **british-football-hooligan-personality** — original skill for this repo (comedy persona; not glorifying real violence)
- **american-gameshow-announcer** — original skill for this repo
- **kiwi-cricket-announcer-personality** — original skill for this repo
- **canadian-southpark-animator** — original skill for this repo (style homage; not affiliated with South Park/Comedy Central)
- **scottish-haggis-kilt-dance** — original skill for this repo
- **african-chieftain-dance-fighters** — original skill for this repo (fictional ceremonial troupe; not affiliated with any real kingdom or ethnic group)
- **french-mistress-personality** — original skill for this repo
- **italian-shoe-shiner-personality** — original skill for this repo
- **russian-hairdresser-personality** — original skill for this repo
- **german-frau-personality** — original skill for this repo
- **dutch-cheese-enthusiast-personality** — original skill for this repo
- **korean-gangnam-girl-personality** — original skill for this repo
- **pacific-islander-bro-personality** — original skill for this repo
- **japanese-tourist-personality** — original skill for this repo
- **thai-international-student-vlogger-personality** — original skill for this repo
- **singaporean-ladies-man-personality** — original skill for this repo
- **devout-irish-catholic-personality** — original skill for this repo
- **seedance/** — adapted from [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) (MIT)
- Wacky dance scene prompts inspired by [KakuDrop's Seedance 2.0 demo](https://x.com/KakuDrop/status/2069181320010543409)