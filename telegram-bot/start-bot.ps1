param(
    [ValidateSet('polling', 'webhook')]
    [string]$Mode = 'polling'
)

Set-Location $PSScriptRoot

if (-not (Test-Path '.env')) {
    Write-Error 'Missing .env. Copy .env.example to .env and set TELEGRAM_BOT_TOKEN.'
    exit 1
}

$env:BOT_MODE = $Mode

if ($Mode -eq 'webhook') {
    if (-not $env:BOT_WEBHOOK_URL) {
        Write-Host 'Webhook mode requires BOT_WEBHOOK_URL in environment or .env.'
        Write-Host 'Set BOT_WEBHOOK_URL=https://bot.yourdomain.com/webhook/secret-path-here'
        exit 1
    }
}

Write-Host "Starting Alpha Elite Telegram bot in $Mode mode..."
python -m bot.main
