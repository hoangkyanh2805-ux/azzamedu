# Start / stop LearnHouse local (after first setup)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $ScriptDir
$InstanceDir = Join-Path $Root "instance"

$env:Path = "C:\Program Files\Docker\Docker\resources\bin;" + $env:Path

if (-not (Test-Path (Join-Path $InstanceDir "learnhouse.config.json"))) {
    Write-Host "No install found. Run .\scripts\local-setup.ps1 first." -ForegroundColor Red
    exit 1
}

docker info 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Start Docker Desktop first." -ForegroundColor Red
    exit 1
}

Set-Location $InstanceDir
npx learnhouse@latest start
npx learnhouse@latest status
Write-Host ""
Write-Host "http://localhost:8080" -ForegroundColor Green
Write-Host "admin@hoa-homes.com / AlphaElite-Local-2026!"
