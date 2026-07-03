# Alpha Elite — Telegram Access Bot

Member access, onboarding, and support layer for Alpha Elite trading education. **Not a signal bot.**

## What it does (MVP)

| Feature | Status |
|---------|--------|
| Telegram ID authentication | ✅ `/start` upserts member |
| Offer menu (Gameplan, Apprentice, VIP, Quant, DWY) | ✅ `/offers` + keyboard |
| Access tiers (Free → Inner Circle) | ✅ `/status` |
| Payment instructions (PayPal / crypto) | ✅ |
| Payment proof → admin queue | ✅ |
| Admin commands (`/queue`, `/confirm`, `/provisioned`, `/tgdone`) | ✅ |
| LearnHouse + VIP onboarding messages | ✅ templates |
| Support tickets | ✅ |
| Supabase schema | ✅ `database/schema_supabase.sql` |
| WooCommerce webhook scaffold | ✅ `bot/webhooks/woocommerce.py` |

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

For Supabase (detailed guide: `docs/supabase-setup.md`):
1. Run `database/schema_supabase.sql` in Supabase SQL Editor
2. Set in `.env`: `DATABASE_URL=https://<project>.supabase.co` and `SUPABASE_SERVICE_KEY=<service_role>`
3. Test: `python scripts/test_supabase.py --cleanup`
4. Set `database.provider: supabase` in `config.yaml` and restart bot

## Project layout

```
telegram-bot/
├── README.md
├── config.example.yaml
├── database/schema_supabase.sql
├── docs/                    # mission, flows, compliance
└── bot/
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
