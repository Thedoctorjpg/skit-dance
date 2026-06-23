param(
    [Parameter(Mandatory = $true)]
    [string]$Token,

    [string]$EnvPath = (Join-Path $PSScriptRoot "..\.env")
)

$ErrorActionPreference = "Stop"
$EnvPath = Resolve-Path (Split-Path $EnvPath -Parent) -ErrorAction SilentlyContinue
if (-not $EnvPath) {
    $EnvPath = Join-Path $PSScriptRoot ".."
}
$envFile = Join-Path $EnvPath ".env"

if ($Token -match '^your_' -or $Token.Length -lt 20) {
    Write-Error "Token looks like a placeholder. Use a real OAuth 2.0 user access token from developer.x.com"
}

Write-Host "Verifying token against X API..."
$resp = curl -s -w "`n%{http_code}" "https://api.x.com/2/users/me" -H "Authorization: Bearer $Token"
$lines = $resp -split "`n"
$code = $lines[-1]
$body = ($lines[0..($lines.Length - 2)] -join "`n")

if ($code -ne "200") {
    Write-Error "Token verification failed (HTTP $code): $body"
}

$user = $body | ConvertFrom-Json
$username = $user.data.username
Write-Host "OK: authenticated as @$username"

if ($username -ne "ADHDloganberry") {
    Write-Warning "Expected @ADHDloganberry but got @$username — continuing anyway."
}

$content = @"
# @ADHDloganberry X API credentials — LOCAL ONLY, never commit
# Setup: adhdloganberry-feed/references/x-api-setup.md

X_USER_ACCESS_TOKEN=$Token

X_API_BASE=https://api.x.com
FEED_DRY_RUN=0
"@

Set-Content -Path $envFile -Value $content -Encoding UTF8 -NoNewline
Write-Host "Wrote token to $envFile (gitignored — will NOT be pushed)"

# Mirror to user skills copy if present
$skillsEnv = Join-Path $env:USERPROFILE ".grok\skills\adhdloganberry-feed\.env"
if (Test-Path (Split-Path $skillsEnv -Parent)) {
    Set-Content -Path $skillsEnv -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Mirrored to $skillsEnv"
}