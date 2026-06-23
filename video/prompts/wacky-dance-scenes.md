# Wacky Dance Scenes — Seedance 2.0 Prompts

Production-ready Seedance 2.0 prompts for the "same character, silly dances in wrong places" format (inspired by [KakuDrop's Seedance 2.0 Omni reference demo](https://x.com/KakuDrop/status/2069181320010543409)).

## Assets

| Asset | File | Role |
|-------|------|------|
| @Image1 | `../assets/character-reference.jpg` | Character appearance reference |

Upload `character-reference.jpg` as @Image1 in Jimeng Seedance 2.0. Optionally upload a dance reference clip as @Video1 for motion replication.

---

## Scene 1: Supermarket (13s)

```
@Image1's character as the subject. Scene references a bright fluorescent
supermarket aisle with cereal boxes and shopping carts.

0–4s: Full shot. The character executes an exaggerated silly shuffle between
shelves, arms flapping with complete professional confidence. Camera tracks
sideways at waist height.
4–9s: Medium shot. Character spins once near the dairy section, nearly
knocking nothing over. Other shoppers visible but unfazed.
9–13s: Close-up on character's delighted face, then pull back to wide shot
as they strike a triumphant pose by the checkout lane.

🎵 Triumphant 80s synth grocery-store energy. Smooth motion, no stuttering.
Aspect ratio 9:16. Duration 13 seconds.
```

---

## Scene 2: Rainy Neon Street (13s)

```
@Image1's character as the subject. Scene references a rainy city street at
night with neon signs reflecting on wet pavement.

0–3s: Wide establishing shot. Character enters frame doing THE BUREAUCRATIC
SHUFFLE — small committed steps through puddles without acknowledging rain.
3–8s: Track shot following character. They perform an interpretive umbrella
twirl. Neon colors cast pink and blue on their outfit.
8–13s: Low-angle hero shot. Character freezes mid-dance as a bus passes,
then immediately resumes with renewed enthusiasm.

🎵 Lo-fi rain beats with unexpected disco breakdown at 8s. 9:16 vertical.
Duration 13 seconds.
```

---

## Scene 3: Office Cubicle (10s)

```
@Image1's character as the subject. Scene references a generic open-plan
office with cubicles, fluorescent lights, and one sad plant.

0–3s: Medium shot. Character sits at desk, then stands and executes THE
SYNERGY SLIDE across linoleum without moving their feet.
3–7s: Coworkers in background continue typing, completely unbothered.
Character performs THE STRATEGIC PIVOT — slow 270° turn maintaining eye
contact with a printer.
7–10s: Character bows formally to the water cooler. Music stops. Silence.

🎵 Corporate muzak that implies a spa inside a bank vault. 9:16. 10 seconds.
```

---

## Scene 4: Beach Sunset (13s)

```
@Image1's character as the subject. Scene references a golden-hour beach
with gentle waves and warm orange sky.

0–5s: Wide shot. Character does a hula-inspired silly dance at the
waterline, waves lapping at their feet. Camera slowly pushes in.
5–10s: Orbit shot around character as they add increasingly unnecessary
arm movements with full sincerity.
10–13s: Silhouette against sunset. Character holds final pose. Seagull
crosses frame. Nobody explains why.

🎵 Tropical ukulele that takes itself too seriously. Smooth, fluid motion.
9:16 vertical. 13 seconds.
```

---

## Dance Replication Template (with reference video)

If you have a dance reference clip, use @Video1:

```
Have the character in @Image1 replicate the dance moves and beat-synced
music from @Video1. Scene references [LOCATION]. Generate a 13-second video.
Movements should be smooth with no stuttering or freezing. The character
treats the dance as completely routine for this setting.
```

---

## Montage Assembly

Generate each scene separately (4–13s each), then concatenate with FFmpeg:

```bash
ffmpeg -f concat -safe 0 -i scenes.txt -c copy wacky-dance-montage.mp4
```

`scenes.txt` example:

```
file 'scene1-supermarket.mp4'
file 'scene2-rainy-street.mp4'
file 'scene3-office.mp4'
file 'scene4-beach.mp4'
```

Keep all clips at the same resolution and frame rate for stream copy to work.