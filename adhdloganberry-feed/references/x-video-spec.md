# X Video Spec — @ADHDloganberry Feed

Encode targets for `scripts/export-for-x.ps1`.

---

## Limits (standard X video post)

| Constraint | Value |
|------------|-------|
| Max duration | **140 seconds** (2:20) |
| Max file size | **512 MB** |
| Min resolution | 32×32 |
| Max resolution | 1920×1200 (landscape) / 1200×1920 (portrait) |
| Frame rate | ≤ 60 fps |
| Video codec | H.264 (recommended) |
| Audio codec | AAC LC stereo |

---

## Feed defaults (@ADHDloganberry)

| Setting | Value |
|---------|-------|
| Aspect | **9:16** portrait |
| Resolution | **720×1280** |
| FPS | **30** |
| Video bitrate | ~4 Mbps CRF equivalent (`-crf 23`) |
| Audio | AAC 128k stereo 44.1kHz |
| Max duration target | 15–45s (under 140s cap) |

---

## FFmpeg one-liner (manual)

Portrait skit-dance clip → X-ready:

```bash
ffmpeg -i input.mp4 -vf "scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2" -r 30 -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 23 -maxrate 4M -bufsize 8M -c:a aac -b:a 128k -ar 44100 -ac 2 -movflags +faststart -t 140 final-x.mp4
```

`-movflags +faststart` — moov atom at front (required for streaming playback on X).

---

## Pre-flight checklist

- [ ] Duration ≤ 140s
- [ ] File size ≤ 512 MB
- [ ] H.264 + AAC
- [ ] `yuv420p` pixel format
- [ ] faststart enabled
- [ ] No letterbox errors on 9:16 phone preview