# Grok Imagine Shot Planning

Visual generation path for the video-creator skill. Complements Seedance 2.0.

---

## Shot Design Rules

1. **One shot = one beat** — 6s default, 10s max
2. **One subject motion** — e.g. spin OR walk, not both
3. **One camera move** — push-in, track, or orbit; not all three
4. **Simple frame animates better** — plain background, clear silhouette
5. **Reuse reference** — same character image across shots via `image_edit`

---

## Shot Table Template

| # | Dur | First frame prompt | Motion prompt | AR |
|---|-----|-------------------|---------------|-----|
| 1 | 6s | Character in supermarket aisle, full body, fluorescent | Camera tracks sideways; character does silly shuffle | 9:16 |
| 2 | 6s | Same character, rainy neon street, night | Slow orbit; umbrella twirl | 9:16 |

---

## Tool Sequence Per Shot

```
image_gen(prompt, aspect_ratio="9:16")
  → save frame-01.png

image_to_video(
  image="frame-01.png",
  prompt="Camera tracks sideways. Character shuffles with confident arm flaps. Smooth 6s.",
  duration=6
)
  → save shot-01.mp4
```

### reference_to_video

Only when user provides reference images and asks for character consistency without composing manually:

```
reference_to_video(
  prompt="Character from reference does silly dance in supermarket",
  reference_images=["character-reference.jpg"],
  duration=6,
  aspect_ratio="9:16"
)
```

Prefer `image_edit` + `image_to_video` when you control the first frame.

---

## xAI API (Headless / No TUI Tools)

```bash
# Text-to-video (no first frame control)
curl -X POST https://api.x.ai/v1/videos/generations \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{"model":"grok-imagine-video","prompt":"...","duration":6,"aspect_ratio":"9:16"}'

# Image-to-video
curl -X POST https://api.x.ai/v1/videos/generations \
  -d '{"model":"grok-imagine-video","prompt":"...","image":{"url":"..."},"duration":6}'

# Reference-to-video
curl -X POST https://api.x.ai/v1/videos/generations \
  -d '{"model":"grok-imagine-video","prompt":"...","reference_images":[{"url":"..."}],"duration":6}'
```

Poll `GET /v1/videos/{request_id}` until `status: done`.

---

## Grok TUI Fallback

If agent session lacks video tools:

```
/imagine-video [shot motion prompt] — use character from attached reference, 9:16, 6 seconds
```

User attaches `video/assets/character-reference.jpg`.

---

## Camera Vocabulary

| Term | Use when |
|------|----------|
| Slow push-in | Emotional beat, reveal |
| Track / follow | Character moving through space |
| Orbit | Hero moment, 180–360° |
| Static + subject motion | Busy background; only character moves |
| Low angle | Triumph, absurd confidence |
| Wide establishing | New location intro |

---

## Matching Skit 📹 VIDEO NOTEs

| Skit note | Imagine prompt fragment |
|-----------|------------------------|
| "Smash cut on stapler" | Generate stapler frame; hard cut in edit, not in-gen |
| "Dutch angle" | `image_gen` with tilted composition |
| "Freeze frame" | Post-production; export last frame |
| "Post-credits sting" | Extra 3s shot, separate file |