# Audio Mux & FFmpeg Assembly

Final assembly for video-creator pipeline.

---

## Prerequisites

All video clips must share:

- Same resolution (e.g. 720×1280 for 9:16)
- Same frame rate (e.g. 24 or 30 fps)
- Same codec (H.264 from generators)

Re-encode mismatched clips before concat:

```bash
ffmpeg -i shot-01.mp4 -vf scale=720:1280 -r 30 -c:v libx264 shot-01-norm.mp4
```

---

## Step 1: Concat Video (Stream Copy)

`scenes.txt`:

```
file 'shot-01-norm.mp4'
file 'shot-02-norm.mp4'
file 'shot-03-norm.mp4'
file 'shot-04-norm.mp4'
```

```bash
ffmpeg -f concat -safe 0 -i scenes.txt -c copy video-only.mp4
```

---

## Step 2: Build Voice Track

### Option A — Concat WAVs with gaps

Create a silent base matching video duration:

```bash
ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 52 -c:a pcm_s16le silence.wav
```

Overlay each TTS line at timestamp (from shot table):

```bash
ffmpeg -i silence.wav -i line-01.wav -i line-02.wav \
  -filter_complex \
  "[0:a][1:a]adelay=0|0[a1]; \
   [a1][2:a]adelay=12000|12000[a2]" \
  -map "[a2]" voice-track.wav
```

`adelay` values in milliseconds (= shot table `t=` × 1000).

### Option B — Per-shot mux then concat

Mux voice onto each shot before video concat (simpler timing):

```bash
ffmpeg -i shot-01-norm.mp4 -i line-01.wav \
  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest shot-01-vo.mp4
```

Update `scenes.txt` to use `shot-01-vo.mp4` etc.

---

## Step 3: Music Bed

```bash
# Loop or trim music to video length
ffmpeg -i music-bed.mp3 -t 52 -af "volume=0.25" music-low.wav

# Duck music under voice (sidechaincompress)
ffmpeg -i video-only.mp4 -i voice-track.wav -i music-low.wav \
  -filter_complex \
  "[2:a][1:a]sidechaincompress=threshold=0.02:ratio=6:attack=200:release=1000[ducked]; \
   [1:a][ducked]amix=inputs=2:duration=first:dropout_transition=0[aout]" \
  -map 0:v:0 -map "[aout]" -c:v copy -c:a aac final.mp4
```

### Silence gag (skit music stop)

Split video at gag timestamp; middle segment gets **voice only**:

```bash
# 0–18s with music, 18–21s silence+VO, 21–52s music returns
ffmpeg -i part-a.mp4 -i part-b-voice-only.mp4 -i part-c.mp4 \
  -f concat -safe 0 -i parts.txt -c copy final.mp4
```

---

## Step 4: Optional Captions

Burn in from script (not from Voxtral STT unless syncing ref):

```bash
ffmpeg -i final.mp4 -vf "drawtext=text='Does anyone need more water?':fontsize=24:fontcolor=white:x=(w-text_w)/2:y=h-80:enable='between(t,18,21)'" final-captioned.mp4
```

Or export `.srt` for platform upload:

```srt
1
00:00:12,000 --> 00:00:15,000
Troupe — formation!

2
00:00:18,000 --> 00:00:21,000
Does anyone need more water?
```

---

## Output Checklist

- [ ] Video plays start-to-finish without glitches at concat points
- [ ] Voice aligned ±200ms to visual beats
- [ ] Music ducks under dialogue, not competing
- [ ] Silence gag has no bed music
- [ ] Final file: `final.mp4` + `production-brief.md` + raw assets folder