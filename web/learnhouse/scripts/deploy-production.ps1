# Deploy LearnHouse to VPS + seed Udemy clone
# 1. Copy deploy-production.env.example → deploy-production.env
# 2. Dien VPS_PASSWORD (email iNET)
# 3. Chay: .\deploy-production.ps1

param(
    [switch]$SeedOnly
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path "deploy-production.env")) {
    Copy-Item "deploy-production.env.example" "deploy-production.env"
    Write-Host "Da tao deploy-production.env — DIEN VPS_PASSWORD roi chay lai!" -ForegroundColor Yellow
    Write-Host "Hoac paste vps-bootstrap.sh vao OneDash SSH Terminal." -ForegroundColor Yellow
    notepad deploy-production.env
    exit 1
}

python -m pip install paramiko requests -q 2>$null

$args = @("-u", "deploy-vps.py")
if ($SeedOnly) { $args += "--seed-only" }
python @args
