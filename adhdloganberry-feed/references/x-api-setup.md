# X API Setup — @ADHDloganberry

Post videos programmatically via [X API v2](https://docs.x.com/x-api/introduction).

---

## 1. Developer account

1. Go to [developer.x.com](https://developer.x.com)
2. Create a project + app tied to **@ADHDloganberry** (user context)
3. Enable **OAuth 2.0** with scopes:
   - `tweet.read`
   - `tweet.write`
   - `users.read`
   - `media.write` (required for video upload)

---

## 2. User access token

Generate an **OAuth 2.0 User Access Token** for the @ADHDloganberry account (not app-only bearer for posting).

Store in `.env` (never commit — `.gitignore` blocks it):

```
X_USER_ACCESS_TOKEN=...
```

Or run the setup script (verifies token, writes `.env` locally only):

```powershell
cd adhdloganberry-feed
.\scripts\setup-token.ps1 -Token "YOUR_OAUTH2_USER_ACCESS_TOKEN"
```

---

## 3. Verify token

```powershell
$token = (Get-Content .env | Where-Object { $_ -match '^X_USER_ACCESS_TOKEN=' }) -replace 'X_USER_ACCESS_TOKEN=',''
curl -s "https://api.x.com/2/users/me" -H "Authorization: Bearer $token"
```

Expect `username: ADHDloganberry`.

---

## 4. Post a test video

```powershell
cd adhdloganberry-feed
pip install requests python-dotenv
python scripts/post-to-x.py --video output/test/final-x.mp4 --caption "hello from the feed setup"
```

Dry run (no API call):

```powershell
$env:FEED_DRY_RUN="1"
python scripts/post-to-x.py --video path\to\final-x.mp4 --caption "test"
```

---

## 5. Rate limits

- Media upload: chunked — see [media upload quickstart](https://docs.x.com/x-api/media/quickstart/media-upload-chunked)
- Post creation: plan-dependent — queue posts in `queue/` if batching

---

## 6. Troubleshooting

| Error | Fix |
|-------|-----|
| 403 on upload | Add `media.write` scope; regenerate token |
| Processing failed | Re-encode with `export-for-x.ps1` — H.264 + AAC |
| 401 | Token expired — refresh OAuth token |
| File too large | Max 512 MB; shorten video or lower bitrate |