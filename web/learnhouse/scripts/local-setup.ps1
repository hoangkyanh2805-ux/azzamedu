# Alpha Elite - LearnHouse local setup (Windows)
# Requires Docker Desktop running before execute.

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $ScriptDir
$InstanceDir = Join-Path $Root "instance"
$AdminEmail = "admin@hoa-homes.com"
$AdminPassword = "AlphaElite-Local-2026!"
$Port = 8080

$env:Path = "C:\Program Files\Docker\Docker\resources\bin;" + $env:Path

Write-Host "=== Alpha Elite LearnHouse Local Setup ===" -ForegroundColor Cyan
Write-Host "Instance dir: $InstanceDir"

$maxWait = 36
$dockerReady = $false
for ($i = 1; $i -le $maxWait; $i++) {
    docker info 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) {
        $dockerReady = $true
        Write-Host "Docker is ready." -ForegroundColor Green
        break
    }
    Write-Host "Waiting for Docker Desktop... ($i/$maxWait)"
    Start-Sleep -Seconds 5
}

if (-not $dockerReady) {
    Write-Host ""
    Write-Host "ERROR: Docker is not running." -ForegroundColor Red
    Write-Host "1. Open Docker Desktop from Start menu"
    Write-Host "2. Wait until status shows Running"
    Write-Host "3. Re-run: .\scripts\local-setup.ps1"
    exit 1
}

New-Item -ItemType Directory -Force -Path $InstanceDir | Out-Null
Set-Location $InstanceDir

$configFile = Join-Path $InstanceDir "learnhouse.config.json"
if (Test-Path $configFile) {
    Write-Host "Existing install found - starting services..." -ForegroundColor Yellow
    npx learnhouse@latest start
} else {
    Write-Host "Running first-time setup (CI mode)..." -ForegroundColor Cyan
    npx learnhouse@latest setup --ci `
        --install-dir $InstanceDir `
        --domain localhost `
        --port $Port `
        --admin-email $AdminEmail `
        --admin-password $AdminPassword `
        --org-name "Alpha Elite" `
        --org-slug alpha-elite
}

Write-Host "Running doctor..." -ForegroundColor Cyan
npx learnhouse@latest doctor

Write-Host ""
Write-Host "=== LearnHouse local ready ===" -ForegroundColor Green
Write-Host "URL:      http://localhost:$Port"
Write-Host "Email:    $AdminEmail"
Write-Host "Password: $AdminPassword"
Write-Host ""
Write-Host 'Next: see admin-setup-checklist.md and paste from content folder'
