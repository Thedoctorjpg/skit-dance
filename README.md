# skit-dance

Agent skills and video prompts for absurdist dancing comedy — from script to Seedance 2.0 video.

## What's in here

| Path | Description |
|------|-------------|
| `SKILL.md` | **dancing-skit** — generate Monty Python-style dance skit scripts |
| `references/` | Script format guide + absurdist move name seed list |
| `seedance/` | **Seedance 2.0** prompt writing skill ([dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill)) |
| `video/assets/` | Character reference image for @Image1 |
| `video/prompts/` | Ready-to-use Seedance prompts + skit→video workflow |
| `skits/` | Example production-ready dancing skit scripts |

## Install

```powershell
git clone https://github.com/Thedoctorjpg/skit-dance.git
cd skit-dance

# Dancing skit script skill
Copy-Item -Recurse . "$env:USERPROFILE\.grok\skills\dancing-skit"

# Seedance prompt skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\seedance-prompt-en" | Out-Null
New-Item -ItemType Directory -Force "$env:USERPROFILE\.grok\skills\seedance-prompt-zh" | Out-Null
Copy-Item seedance\SKILL.md "$env:USERPROFILE\.grok\skills\seedance-prompt-en\SKILL.md"
Copy-Item seedance\zh\SKILL.md "$env:USERPROFILE\.grok\skills\seedance-prompt-zh\SKILL.md"
```

## Usage

### Write a skit script

```
/dancing-skit job interview where the candidate dances their CV
```

Example output: [`skits/the-supermarket-shuffle.md`](skits/the-supermarket-shuffle.md)

### Generate Seedance video prompts

Use prompts in `video/prompts/wacky-dance-scenes.md`, or follow `video/prompts/skit-to-video-workflow.md` to convert a skit script into Seedance clips.

### Full pipeline

1. `/dancing-skit` → production `.md` script
2. Map acts to Seedance prompts (see workflow doc)
3. Upload `video/assets/character-reference.jpg` as @Image1 in [Jimeng Seedance 2.0](https://jimeng.jianying.com/)
4. Generate clips → FFmpeg concat

## Credits

- **dancing-skit** — original skill for this repo
- **seedance/** — adapted from [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) (MIT)
- Wacky dance scene prompts inspired by [KakuDrop's Seedance 2.0 demo](https://x.com/KakuDrop/status/2069181320010543409)