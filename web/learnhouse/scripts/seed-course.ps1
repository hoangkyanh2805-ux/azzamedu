# Run after local-setup.ps1
# Requires: pip install requests (or python -m pip install requests)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

python -m pip install requests -q 2>$null
python .\seed-course.py
