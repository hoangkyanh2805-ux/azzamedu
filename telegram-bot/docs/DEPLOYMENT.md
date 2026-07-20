# Deployment — Telegram Access Bot

> **Human gate G1** required before production token serves real users.

---

## Prerequisites

- Python 3.11+
- Telegram bot token ([@BotFather](https://t.me/BotFather))
- VPS (same region as users) or PaaS with always-on process
- Supabase project **or** Google Service Account for Sheets
- Domain for Mini App (P1): HTTPS required by Telegram

---

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `TELEGRAM_BOT_TOKEN` | Yes | Bot API token |
| `ADMIN_TELEGRAM_IDS` | Yes | Comma-separated admin user IDs |
| `DATABASE_URL` | Yes* | Supabase Postgres connection string |
| `SITE_BASE_URL` | Yes | `https://yourdomain.com` |
| `LEARNHOUSE_URL` | Yes | `https://learn.yourdomain.com` |
| `PAYPAL_EMAIL` | G6 | Shown in `/pay` |
| `CRYPTO_WALLET` | G6 | USDT address |
| `WEBHOOK_URL` | P2 | WooCommerce receiver |
| `WEBHOOK_SECRET` | P2 | HMAC verify |

\* Or Sheets: `GOOGLE_SHEETS_ID` + credentials JSON path

---

## Local development

```bash
cd telegram-bot
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy config.example.yaml config.yaml
# Edit config.yaml — do not commit
python -m bot.main
```

Use polling mode for local dev (`BOT_MODE=polling`).
Use webhook mode for production if you have HTTPS and a public endpoint (`BOT_MODE=webhook`, `BOT_WEBHOOK_URL=https://bot.yourdomain.com/webhook/secret-path-here`).

---

## Production: systemd (Linux VPS)

```ini
# /etc/systemd/system/alpha-elite-telegram-bot.service
[Unit]
Description=Alpha Elite Telegram Access Bot
After=network.target

[Service]
Type=simple
User=deploy
WorkingDirectory=/opt/webkhoahoc/telegram-bot
EnvironmentFile=/opt/webkhoahoc/telegram-bot/.env
ExecStart=/opt/webkhoahoc/telegram-bot/.venv/bin/python -m bot.main
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable alpha-elite-telegram-bot
sudo systemctl start alpha-elite-telegram-bot
sudo journalctl -u alpha-elite-telegram-bot -f
```

---

## Production: webhook mode (recommended)

Telegram webhook → `https://bot.yourdomain.com/webhook/{secret_path}`

Benefits: lower latency, no polling loop.

1. Nginx reverse proxy → bot process (FastAPI/aiohttp webhook server)
2. Set webhook via Bot API `setWebhook`
3. Keep TLS certificate valid (Let's Encrypt)

**Mini App (P1):** static files or small FastAPI route on same host.

---

## Docker (optional)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY bot ./bot
ENV PYTHONUNBUFFERED=1
CMD ["python", "-m", "bot.main"]
```

```bash
docker build -t alpha-elite-telegram-bot .
docker run -d --env-file .env --name ae-bot alpha-elite-telegram-bot
```

---

## BotFather setup

1. `/newbot` → name + username  
2. Set description: education & member access (no signal promises)  
3. `/setcommands`:

```text
start - Main menu and disclaimer
offers - View offers and checkout links
status - Your access status
pay - Payment instructions
onboard - Onboarding checklist
support - Contact support
legal - Risk disclaimer
```

4. Mini App (P1): Bot Settings → Menu Button → Web App URL

---

## WooCommerce webhook (P2)

Separate service or route in bot app:

```text
POST /hooks/woocommerce/order
Header: X-WC-Webhook-Signature
→ verify → upsert members + provision_queue → notify admin
```

Spec: `knowledge/project-maps/alpha-elite/telegram-access-bot/11-future-webhook-plan.md`

Deploy webhook on same VPS or Cloudflare Worker — **not** on shared WordPress host if possible.

---

## Security checklist

- [ ] `config.yaml` and `.env` in `.gitignore`
- [ ] Admin commands restricted to `ADMIN_TELEGRAM_IDS`
- [ ] No customer PII in application logs
- [ ] Webhook secret rotated if leaked
- [ ] Bot description reviewed by Compliance (G1)

---

## Rollback

1. `systemctl stop alpha-elite-telegram-bot`
2. Revert to previous release tag
3. Notify admins — manual provision via WooCommerce + SOP until bot restored

---

## Post-deploy verification

- [ ] `/start` shows disclaimer
- [ ] `/offers` links resolve
- [ ] Test payment proof → admin notification
- [ ] `/admin confirm` dry run on test row
- [ ] G4/G5 human steps complete for test user
- [ ] Log in `.ai/audit/approvals/YYYY-MM-DD-telegram-bot-launch.md`
