$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $MyInvocation.MyCommand.Path)
python -m pip install requests -q 2>$null
python -u .\sync-udemy-clone.py
