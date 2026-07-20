# Hermes Agent — Telegram Access Bot

**Part of:** Alpha Elite 12-Agent Orchestration Model  
**Agent role:** Telegram Access Agent + Admin Ops (member access, payment verification, delivery)  
**Bot handle:** `@Course7979_bot`

Member access, onboarding, and support layer for Alpha Elite trading education. **Not a signal bot.**

## What it does (MVP)

| Feature | Status |
|---------|--------|
| Telegram ID authentication | ✅ `/start` upserts member |
| Offer menu (category shop + khóa học) | ✅ `/menu` `/shop` + 🛒 Shop |
| Access tiers (Free → Inner Circle) | ✅ `/status` |
| Payment instructions (PayPal / crypto) | ✅ |
| Payment proof → admin queue | ✅ |
| Admin commands (`/queue`, `/confirm`, `/provisioned`, `/tgdone`) | ✅ |
| LearnHouse + VIP onboarding messages | ✅ templates |
| Support tickets | ✅ |
| Supabase schema | ✅ `database/schema_supabase.sql` |
| WooCommerce webhook scaffold | ✅ `bot/webhooks/woocommerce.py` |
| **Woo → Supabase catalog sync** | ✅ `scripts/sync-woo-catalog.py` |
| **Mini App shop (HTML + Supabase)** | ✅ `miniapp/` |

## MVP access rule

```
Payment or apply → admin review → admin creates LearnHouse user (G4)
→ admin approves VIP Telegram (G5) → bot sends onboarding
```

## Quick start

```bash
cd telegram-bot
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy config.example.yaml config.yaml
copy .env.example .env
# Set TELEGRAM_BOT_TOKEN in .env and admin telegram_ids in config.yaml
python -m bot.main
```

Default database is **in-memory** (`database.provider: memory`).

## Run the bot (connect Hermes / Telegram)

The Telegram bot must be running continuously for Hermes desktop or any Telegram client to connect.

- Local/polling mode (best for Windows / dev):
  - `.	elegram-bot\start-bot.ps1`
  - or set `BOT_MODE=polling` and run `python -m bot.main`
- Webhook mode (production / public HTTPS):
  - set `BOT_MODE=webhook`
  - set `BOT_WEBHOOK_URL=https://bot.yourdomain.com/webhook/secret-path-here`
  - set `BOT_WEBHOOK_PATH=/webhook/secret-path-here`
  - then run `python -m bot.main`

If the bot is not running, Hermes desktop cannot deliver messages through Telegram.

For Supabase (detailed guide: `docs/supabase-setup.md`):
1. Run `database/schema_supabase.sql` in Supabase SQL Editor
2. Run `database/migrations/002_shop_catalog.sql`
3. Run `database/migrations/003_miniapp_public_read.sql` (for Mini App anon read)
4. Set in `.env`: `DATABASE_URL`, `SUPABASE_SERVICE_KEY`, Woo API keys
5. `python scripts/sync-woo-catalog.py`
6. Set `catalog.source: supabase` in `config.yaml` and restart bot

**Mini App:** see `miniapp/README.md` — copy `js/config.js`, deploy HTTPS, set `site.miniapp_shop_url`.

## Project layout

```
telegram-bot/
├── README.md
├── config.example.yaml
├── database/schema_supabase.sql
├── docs/                    # mission, flows, shop-catalog.md
├── miniapp/                 # Telegram WebApp shop (Supabase catalog)
└── bot/
    ├── catalog.py           # shop categories + offers
    ├── main.py
    ├── config.py
    ├── handlers/            # start, offers, pay, admin, …
    ├── keyboards/
    ├── services/            # db (memory), notify
    └── templates/           # compliance-safe copy (.md)
```

## Admin commands

| Command | Action |
|---------|--------|
| `/queue` | List open provision queue |
| `/confirm AE-2026-0001` | Mark payment confirmed |
| `/provisioned AE-2026-0001` | Send LearnHouse instructions |
| `/tgdone AE-2026-0001` | Mark VIP active, send invite message |

Human SOPs: `playbook/ops/learnhouse-provision-sop.md`, `playbook/ops/telegram-onboarding-sop.md`

## Related docs

- `docs/project-mission.md` — scope and non-goals
- `docs/bot-flow.md` — commands and state machine
- `knowledge/project-maps/alpha-elite/telegram-access-bot/` — knowledge pack
- `docs/telegram-access-bot-operating-model.md` — agent OS (repo root)

## Compliance

All bot copy must pass `docs/compliance-checklist.md`. No profit guarantees, no financial advice claims, no signal-group positioning.

## Deployment

See `docs/DEPLOYMENT.md` (polling MVP) or run behind nginx + webhook for production.
