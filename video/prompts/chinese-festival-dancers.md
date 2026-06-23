# Seedance Prompts — Chinese Festival Dancers

9:16 vertical. Fictional Jade Lantern Troupe — red/gold festival costumes, fans/ribbons/lion head, synchronized drum-led formations. Comedy from wrong-place setting. Dance only — no violence.

---

## Template (per clip, 5–13s)

```
@Image1 festival dance troupe leader in red and gold Chinese-inspired performance costume
9:16 vertical, [LOCATION], cinematic lighting

0-2s: Captain Wei raises drum stick — troupe freezes in line, fans closed
2-5s: THE DRUM GATE — entry on third beat, synchronized step
5-8s: THE [MOVE NAME] — [fan wall / ribbon typhoon / lion head nod]
8-13s: Captain nod of approval; troupe holds final pose; wrong-place gag ([elevator buttons / IKEA aisle / scanner beep])

Style: celebratory festival dance pageantry, vibrant red and gold, sharp formation, meme energy
Audio suggestion: Chinese festival drum + [wrong genre]
```

---

## Example — Airport Security

```
@Image1 Captain Wei, Chinese festival dance troupe leader, red gold performance regalia
9:16 vertical, airport security lane, fluorescent lights

0-2s: Dancer places lion head in plastic tray; Captain watches like opening ceremony
2-5s: THE AIRPORT SECURITY LINE — proud walk through arch
5-8s: THE LION HEAD NOD on "clear" — alarm flashes, perfect stance held
8-10s: Captain single nod; lion head reclaimed; DOUBLE FAN SALUTE

Celebratory dance energy, synchronized troupe background, meme loop ending
```

---

## Pipeline

1. Generate meme pack via `/chinese-festival-dancers [vibe]`
2. One Seedance prompt per meme beat
3. `video/assets/character-reference.jpg` as @Image1 for captain look consistency
4. FFmpeg concat per `skit-to-video-workflow.md`