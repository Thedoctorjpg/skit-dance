# skit-dance

Grok / agent skill for generating absurdist humorous dancing skit scripts — Monty Python meets TikTok at 3am.

## Install

Copy the skill directory to your Grok skills folder:

```bash
git clone https://github.com/Thedoctorjpg/skit-dance.git
cp -r skit-dance ~/.grok/skills/dancing-skit
```

On Windows (PowerShell):

```powershell
git clone https://github.com/Thedoctorjpg/skit-dance.git
Copy-Item -Recurse skit-dance "$env:USERPROFILE\.grok\skills\dancing-skit"
```

## Usage

- Slash command: `/dancing-skit`
- Or ask: *"Write a dancing skit about medieval peasants"*

## Files

| File | Description |
|------|-------------|
| `SKILL.md` | Main skill — tone, process, quality checks |
| `references/format-guide.md` | Production-ready `.md` script format + example |
| `references/move-names.md` | Seed list of absurdist dance move names |