param(
    [Parameter(Mandatory = $true)]
    [string]$Input,

    [Parameter(Mandatory = $true)]
    [string]$PostId,

    [string]$OutputRoot = (Join-Path $PSScriptRoot "..\output"),

    [int]$Width = 720,
    [int]$Height = 1280,
    [int]$MaxSeconds = 140
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    Write-Error "ffmpeg not found in PATH. Install ffmpeg and retry."
}

$outDir = Join-Path $OutputRoot $PostId
New-Item -ItemType Directory -Force $outDir | Out-Null

$inputPath = Resolve-Path $Input
$outputPath = Join-Path $outDir "final-x.mp4"

$vf = "scale=${Width}:${Height}:force_original_aspect_ratio=decrease,pad=${Width}:${Height}:(ow-iw)/2:(oh-ih)/2,setsar=1"

$ffmpegArgs = @(
    "-y",
    "-i", $inputPath,
    "-vf", $vf,
    "-r", "30",
    "-c:v", "libx264",
    "-profile:v", "high",
    "-pix_fmt", "yuv420p",
    "-crf", "23",
    "-maxrate", "4M",
    "-bufsize", "8M",
    "-c:a", "aac",
    "-b:a", "128k",
    "-ar", "44100",
    "-ac", "2",
    "-movflags", "+faststart",
    "-t", $MaxSeconds,
    $outputPath
)

Write-Host "Encoding X-ready video for @ADHDloganberry..."
& ffmpeg @ffmpegArgs

if ($LASTEXITCODE -ne 0) {
    Write-Error "ffmpeg failed with exit code $LASTEXITCODE"
}

$meta = @{
    post_id    = $PostId
    account    = "ADHDloganberry"
    account_url = "https://x.com/ADHDloganberry"
    video      = $outputPath
    encoded_at = (Get-Date).ToUniversalTime().ToString("o")
    spec       = "720x1280 H.264 AAC faststart max ${MaxSeconds}s"
}
$metaPath = Join-Path $outDir "post-meta.json"
$meta | ConvertTo-Json -Depth 4 | Set-Content -Path $metaPath -Encoding UTF8

Write-Host "Done: $outputPath"
Write-Host "Meta: $metaPath"
Write-Host "Next: add caption.txt then run post-to-x.py --post-id $PostId"