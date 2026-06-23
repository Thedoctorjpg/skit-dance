#!/usr/bin/env python3
"""Post video to @ADHDloganberry via X API v2 chunked media upload."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("Install dependencies: pip install requests python-dotenv", file=sys.stderr)
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None  # type: ignore

FEED_ROOT = Path(__file__).resolve().parent.parent
CHUNK_SIZE = 1024 * 1024  # 1 MB


def load_env() -> None:
    env_path = FEED_ROOT / ".env"
    if load_dotenv and env_path.exists():
        load_dotenv(env_path)
    elif env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def api_base() -> str:
    return os.environ.get("X_API_BASE", "https://api.x.com").rstrip("/")


def token() -> str:
    t = os.environ.get("X_USER_ACCESS_TOKEN", "").strip()
    if not t or t.startswith("your_") or t == "your_oauth2_user_access_token_here":
        return ""
    return t


def is_dry_run() -> bool:
    if os.environ.get("FEED_DRY_RUN", "0") == "1":
        return True
    return not token()


def headers() -> dict[str, str]:
    t = token()
    if not t:
        raise RuntimeError("No X_USER_ACCESS_TOKEN configured")
    return {"Authorization": f"Bearer {t}"}


def init_upload(video_path: Path, session: requests.Session) -> str:
    total = video_path.stat().st_size
    url = f"{api_base()}/2/media/upload"
    resp = session.post(
        url,
        headers=headers(),
        data={
            "command": "INIT",
            "media_type": "video/mp4",
            "total_bytes": str(total),
            "media_category": "tweet_video",
        },
    )
    resp.raise_for_status()
    media_id = resp.json()["data"]["id"]
    print(f"INIT media_id={media_id} ({total} bytes)")
    return media_id


def append_chunks(video_path: Path, media_id: str, session: requests.Session) -> None:
    url = f"{api_base()}/2/media/upload"
    with video_path.open("rb") as f:
        index = 0
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            resp = session.post(
                url,
                headers=headers(),
                data={
                    "command": "APPEND",
                    "media_id": media_id,
                    "segment_index": str(index),
                },
                files={"media": (f"chunk{index}.mp4", chunk, "application/octet-stream")},
            )
            resp.raise_for_status()
            print(f"APPEND segment {index}")
            index += 1


def finalize_upload(media_id: str, session: requests.Session) -> dict:
    url = f"{api_base()}/2/media/upload"
    resp = session.post(
        url,
        headers=headers(),
        data={"command": "FINALIZE", "media_id": media_id},
    )
    resp.raise_for_status()
    return resp.json().get("data", {})


def wait_for_processing(media_id: str, session: requests.Session) -> None:
    url = f"{api_base()}/2/media/upload"
    while True:
        resp = session.get(
            url,
            headers=headers(),
            params={"command": "STATUS", "media_id": media_id},
        )
        resp.raise_for_status()
        data = resp.json().get("data", {})
        info = data.get("processing_info") or {}
        state = info.get("state", "succeeded")
        if state == "succeeded":
            print("Media processing succeeded")
            return
        if state == "failed":
            raise RuntimeError(f"Media processing failed: {data}")
        wait = int(info.get("check_after_secs", 2))
        print(f"Processing state={state}, wait {wait}s")
        time.sleep(wait)


def create_post(caption: str, media_id: str, session: requests.Session) -> dict:
    url = f"{api_base()}/2/tweets"
    payload = {"text": caption, "media": {"media_ids": [media_id]}}
    resp = session.post(
        url,
        headers={**headers(), "Content-Type": "application/json"},
        json=payload,
    )
    resp.raise_for_status()
    return resp.json()


def resolve_post(post_id: str | None, video: str | None, caption: str | None) -> tuple[Path, str, Path]:
    if post_id:
        out_dir = FEED_ROOT / "output" / post_id
        video_path = out_dir / "final-x.mp4"
        caption_path = out_dir / "caption.txt"
        if not video_path.exists():
            print(f"Missing video: {video_path}", file=sys.stderr)
            sys.exit(1)
        text = caption or (caption_path.read_text(encoding="utf-8").strip() if caption_path.exists() else "")
        if not text:
            print(f"Missing caption: pass --caption or create {caption_path}", file=sys.stderr)
            sys.exit(1)
        if len(text) > 280:
            print(f"Warning: caption is {len(text)} chars (X limit 280)", file=sys.stderr)
        return video_path, text, out_dir

    if not video or not caption:
        print("Provide --post-id OR both --video and --caption", file=sys.stderr)
        sys.exit(1)
    return Path(video).resolve(), caption, Path(video).resolve().parent


def write_queue_entry(out_dir: Path, post_id: str, tweet_id: str, caption: str, video: Path) -> None:
    queue_dir = FEED_ROOT / "queue"
    queue_dir.mkdir(parents=True, exist_ok=True)
    entry = {
        "post_id": post_id,
        "tweet_id": tweet_id,
        "account": "ADHDloganberry",
        "account_url": "https://x.com/ADHDloganberry",
        "caption": caption,
        "video": str(video),
        "posted_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "tweet_url": f"https://x.com/ADHDloganberry/status/{tweet_id}",
    }
    qpath = queue_dir / f"{post_id}.posted.json"
    qpath.write_text(json.dumps(entry, indent=2), encoding="utf-8")
    meta_path = out_dir / "post-meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta.update(entry)
        meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Post video to @ADHDloganberry")
    parser.add_argument("--post-id", help="Post folder under output/")
    parser.add_argument("--video", help="Path to final-x.mp4")
    parser.add_argument("--caption", help="Tweet text (max 280 recommended)")
    args = parser.parse_args()

    load_env()
    video_path, caption, out_dir = resolve_post(args.post_id, args.video, args.caption)
    post_id = args.post_id or out_dir.name

    if not video_path.suffix.lower() == ".mp4":
        print(f"Expected .mp4 video, got: {video_path}", file=sys.stderr)
        sys.exit(1)

    if is_dry_run():
        reason = "FEED_DRY_RUN=1" if os.environ.get("FEED_DRY_RUN") == "1" else "no valid X_USER_ACCESS_TOKEN"
        print(f"DRY RUN ({reason}) — would post:")
        print(f"  account: https://x.com/ADHDloganberry")
        print(f"  video:   {video_path}")
        print(f"  caption: {caption}")
        return

    with requests.Session() as session:
        media_id = init_upload(video_path, session)
        append_chunks(video_path, media_id, session)
        data = finalize_upload(media_id, session)
        if data.get("processing_info"):
            wait_for_processing(media_id, session)
        result = create_post(caption, media_id, session)

    tweet_id = result.get("data", {}).get("id", "")
    print(f"Posted: https://x.com/ADHDloganberry/status/{tweet_id}")
    write_queue_entry(out_dir, post_id, tweet_id, caption, video_path)


if __name__ == "__main__":
    main()