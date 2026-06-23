# Scottish Kilt & Haggis Dance — Seedance 2.0 Prompts

9:16 vertical meme clips. Kilted dancers, haggis props, Highland fling energy in wrong locations.

## Assets

| Asset | File | Role |
|-------|------|------|
| @Image1 | `../assets/character-reference.jpg` | Base character (edit to kilt/tartan in prompt) |

Add to every prompt: *kilted Scottish dancer, tartan pattern, sporran, holding or tossing haggis*

---

## Scene 1: Highland Car Park Tornado (13s)

```
@Image1's character as a kilted Scottish dancer with tartan kilt and sporran,
holding a haggis. Scene references an empty outdoor car park under grey sky.

0–4s: Wide shot. Dancer executes a vigorous Highland fling spin — THE TARTAN
TORNADO — kilt flares, haggis held high with both hands.
4–9s: Medium shot. Faster footwork, wee jumps, arms precise, face deadly serious.
9–13s: Hero pose; kilt slightly crooked; haggis intact. Wind blows tartan.

🎵 Bagpipes with accidental disco kick drum. 9:16 vertical. 13 seconds.
Smooth motion, no stutter.
```

---

## Scene 2: Supermarket Aisle Fling (10s)

```
@Image1's character as kilted dancer in bright supermarket aisle. Haggis in
shopping trolley and in hands.

0–3s: Track shot. Dancer performs silly Highland steps between shelves — THE
SUPERMARKET SPORRAN SLIDE — trolley moves with footwork.
3–7s: Spin near cereal boxes; products wobble but do not fall; shoppers unfazed.
7–10s: Bow to haggis on pedestal of stacked oatcakes. Triumphant.

🎵 Celtic folk EDM mashup. 9:16. 10 seconds.
```

---

## Scene 3: Elevator Kilt Helicopter (8s)

```
@Image1's character as kilted dancer cramped in modern elevator with two
confused passengers. Haggis clutched to chest.

0–2s: Close-up — "och" expression. Dancer begins THE KILT HELICOPTER spin.
2–6s: Full spin in tight space; sporran swings; passengers pressed to walls.
6–8s: Ding — doors open; dancer exits mid-pose; haggis salute.

🎵 Elevator muzak with bagpipe stab. 9:16. 8 seconds.
```

---

## Scene 4: Airport Security Shuffle (7s)

```
@Image1's character as kilted dancer at airport security arch. Haggis on tray.

0–3s: THE AIRPORT SECURITY SHUFFLE — wee steps forward, arms raised, kilt sway.
3–5s: Alarm lights flash; dancer proud thumbs-up.
5–7s: Security guard slow clap. Haggis elevated like trophy.

🎵 Airport PA voice energy, drum roll. 9:16. 7 seconds.
```

---

## Scene 5: Library Silent Fling (10s)

```
@Image1's character as kilted dancer in silent library. Readers at tables.

0–5s: Wide. Maximum-intensity Highland fling with minimal floor sound — visual
exaggeration only. THE HAGGIS HIGHLAND FLING.
5–8s: Librarian stands, finger to lips. Dancer nods, continues.
8–10s: Freeze on SHHH sign. Haggis still aloft.

🎵 Silence then single bagpipe note. 9:16. 10 seconds.
```

---

## Caption Overlay Suggestions

Pair clips with phonetic Scots from `memes/scottish-haggis-kilt-dance-memes.md`:

- "Och, ye cannae fling in a lift? Watch me."
- "Th' haggis set off th' alarm. Richt proud."
- "Pure dead brilliant. Haggis intact."

---

## Montage

```bash
ffmpeg -f concat -safe 0 -i scottish-memes.txt -c copy kilt-meme-montage.mp4
```

```
file 'car-park-tornado.mp4'
file 'supermarket-fling.mp4'
file 'elevator-helicopter.mp4'
```