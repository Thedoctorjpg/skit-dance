# skit-dance

Agent skills, example scripts, and video prompts for absurdist comedy — dancing skits, Swedish Chef cook-offs, and Seedance 2.0 video.

## What's in here

| Path | Skill | Description |
|------|-------|-------------|
| `SKILL.md` + `references/` | **dancing-skit** | Monty Python-style dance skit scripts |
| `swedish-chef-cookoff/` | **swedish-chef-cookoff** | Muppets Swedish Chef cook-off challenges |
| `aussie-bogan-personality/` | **aussie-bogan-personality** | Dazza — loveable Aussie bogan larrikin persona |
| `american-gameshow-announcer/` | **american-gameshow-announcer** | Chip Lexington — classic TV game show announcer |
| `canadian-southpark-animator/` | **canadian-southpark-animator** | Gord McKenzie — construction-paper satire animator |
| `scottish-haggis-kilt-dance/` | **scottish-haggis-kilt-dance** | Kilted haggis dance memes — strong Scots accent |
| `french-mistress-personality/` | **french-mistress-personality** | Colette Duval — dramatic French mistress camp |
| `german-frau-personality/` | **german-frau-personality** | Ingrid Hofmeister — stern German Frau, Ordnung & warmth |
| `japanese-tourist-personality/` | **japanese-tourist-personality** | Yuki Nakamura — enthusiastic tourist wonder & polite chaos |
| `thai-international-student-vlogger-personality/` | **thai-international-student-vlogger-personality** | Natt Srisuk — study-abroad vlog diary & sabai chaos |
| `seedance/` | **seedance-prompt-en/zh** | Seedance 2.0 video prompt writing ([dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill)) |
| `skits/` | — | Example production-ready dancing skit scripts |
| `memes/` | — | Short dance meme caption packs (Scottish kilt/haggis) |
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

# American game show announcer skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\american-gameshow-announcer" | Out-Null
Copy-Item american-gameshow-announcer\SKILL.md "$env:USERPROFILE\.grok\skills\american-gameshow-announcer\SKILL.md"

# Canadian South Park style animator skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\canadian-southpark-animator" | Out-Null
Copy-Item canadian-southpark-animator\SKILL.md "$env:USERPROFILE\.grok\skills\canadian-southpark-animator\SKILL.md"

# Scottish haggis kilt dance memes skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\scottish-haggis-kilt-dance" | Out-Null
Copy-Item -Recurse scottish-haggis-kilt-dance\* "$env:USERPROFILE\.grok\skills\scottish-haggis-kilt-dance\"

# French mistress personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\french-mistress-personality" | Out-Null
Copy-Item french-mistress-personality\SKILL.md "$env:USERPROFILE\.grok\skills\french-mistress-personality\SKILL.md"

# German frau personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\german-frau-personality" | Out-Null
Copy-Item german-frau-personality\SKILL.md "$env:USERPROFILE\.grok\skills\german-frau-personality\SKILL.md"

# Japanese tourist personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\japanese-tourist-personality" | Out-Null
Copy-Item japanese-tourist-personality\SKILL.md "$env:USERPROFILE\.grok\skills\japanese-tourist-personality\SKILL.md"

# Thai international student vlogger personality skill
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\thai-international-student-vlogger-personality" | Out-Null
Copy-Item thai-international-student-vlogger-personality\SKILL.md "$env:USERPROFILE\.grok\skills\thai-international-student-vlogger-personality\SKILL.md"

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

### Game show announcer mode

```
Chip Lexington, take it away!
```

Or: *"announcer mode on"* / *"game show mode"*

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

### French mistress mode

```
Enchantée, Colette
```

Or: *"mistress mode on"* / *"French mistress mode"*

### German frau mode

```
Guten Tag, Ingrid
```

Or: *"Frau mode on"* / *"German frau mode"*

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
- **american-gameshow-announcer** — original skill for this repo
- **canadian-southpark-animator** — original skill for this repo (style homage; not affiliated with South Park/Comedy Central)
- **scottish-haggis-kilt-dance** — original skill for this repo
- **french-mistress-personality** — original skill for this repo
- **german-frau-personality** — original skill for this repo
- **japanese-tourist-personality** — original skill for this repo
- **thai-international-student-vlogger-personality** — original skill for this repo
- **seedance/** — adapted from [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) (MIT)
- Wacky dance scene prompts inspired by [KakuDrop's Seedance 2.0 demo](https://x.com/KakuDrop/status/2069181320010543409)