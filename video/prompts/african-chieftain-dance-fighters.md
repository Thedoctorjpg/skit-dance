# Seedance Prompts — African Chieftain Dance Fighters

9:16 vertical. Fictional Royal Umoja Ceremonial Guard — regal beaded capes, ceremonial spears/shields, synchronized stomps/jumps. Comedy from wrong-place setting. No graphic violence.

---

## Template (per clip, 5–13s)

```
@Image1 chieftain leader in ornate African-inspired ceremonial regalia, beaded cape, gold accents
9:16 vertical, [LOCATION], cinematic lighting

0-2s: Chief Jabari raises hand — guards freeze in line, ceremonial spears vertical
2-5s: THE UMoja STOMP — synchronized foot strikes, dust motes, drum beat visual
5-8s: THE [MOVE NAME] — [spear salute / sky-high jump / shield wall shuffle]
8-13s: Chief nod of approval; guards hold final pose; optional wrong-place gag ([elevator buttons / IKEA aisle / scanner beep])

Style: celebratory warrior dance pageantry, vibrant colors, sharp formation, meme energy, not combat violence
Audio suggestion: djembe rhythm + [wrong genre]
```

---

## Example — Airport Security

```
@Image1 Chief Jabari Okoro, African ceremonial chieftain regalia, beaded cape, dignified bearing
9:16 vertical, airport security lane, fluorescent lights

0-2s: Guard places ceremonial spear in plastic tray; Chief watches like state ceremony
2-5s: THE AIRPORT SECURITY LINE — slow proud walk through arch
5-8s: THE SKY-HIGH JUMP on "clear" — alarm flashes, guard lands perfect stance
8-10s: Chief single nod; guard thumbs up; spear reclaimed with spear salute

Celebratory dance energy, synchronized guards in background, meme loop ending
```

---

## Pipeline

1. Generate meme pack via `/african-chieftain-dance-fighters [vibe]`
2. One Seedance prompt per meme beat
3. `video/assets/character-reference.jpg` as @Image1 for chief look consistency
4. FFmpeg concat per `skit-to-video-workflow.md`