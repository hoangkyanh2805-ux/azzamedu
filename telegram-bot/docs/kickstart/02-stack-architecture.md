# 2 — Stack Architecture

## System context

```text
                         ┌─────────────────────────────────────┐
                         │           END USERS                  │
                         │  Telegram app · Mini App (P1)        │
                         └──────────────────┬──────────────────┘
                                            │
                         ┌──────────────────▼──────────────────┐
                         │   Alpha Elite Telegram Access Bot    │
                         │   Python · Bot API · webhook/poll    │
                         └──────────────────┬──────────────────┘
              ┌────────────────────────────┼────────────────────────────┐
              │                            │                            │
              ▼                            ▼                            ▼
     ┌────────────────┐          ┌────────────────┐          ┌────────────────┐
     │ Supabase       │          │ Admin Telegram │          │ Config / URLs  │
     │ or Google      │          │ notify chat    │          │ site, LH, SKU  │
     │ Sheets         │          │ /admin cmds    │          │ checkout paths │
     └────────────────┘          └────────────────┘          └────────────────┘

EXTERNAL (not in bot process)
     ┌────────────────┐          ┌────────────────┐          ┌────────────────┐
     │ WordPress      │          │ LearnHouse     │          │ Brevo          │
     │ WooCommerce    │          │ (manual G4)  │          │ (parallel)     │
     │ FunnelKit      │          │                │          │                │
     └────────────────┘          └────────────────┘          └────────────────┘
              │
              ▼ P2
     ┌────────────────┐
     │ WC Webhook     │
     │ receiver       │
     └────────────────┘
```

---

## Component table

| Component | Technology | Role |
|-----------|------------|------|
| **Bot runtime** | Python 3.11+ | Handlers, business logic |
| **Bot framework** | `python-telegram-bot` ≥21 | Updates, keyboards, files |
| **Auth** | Telegram `user.id` | Primary identity — no separate login |
| **MVP database** | Supabase (Postgres) **or** Google Sheets | Members, queue, tickets |
| **Admin channel** | Telegram group/chat | Notifications + commands |
| **Payments (MVP)** | PayPal + crypto manual | Instructions in `/pay`; verify by admin |
| **Payments (web)** | WooCommerce + FunnelKit | Primary card/PayPal checkout |
| **LMS** | LearnHouse | Manual enroll; bot sends URL |
| **Email** | Brevo | Parallel nurture — not replaced by bot |
| **Mini App** | HTTPS static/SPA (P1) | Status dashboard in Telegram |
| **Secrets** | `.env` / VPS env | `TELEGRAM_BOT_TOKEN`, `DATABASE_URL` |

---

## Repository layout (this subproject)

```text
telegram-bot/
├── README.md
├── requirements.txt
├── config.example.yaml
├── bot/
│   ├── main.py
│   ├── config.py
│   ├── handlers/          # start, offers, status, pay, support, admin
│   ├── keyboards/
│   ├── templates/         # compliance-reviewed copy
│   └── services/
│       ├── db.py
│       └── notify.py
├── docs/
│   ├── DATABASE.md
│   ├── DEPLOYMENT.md
│   └── kickstart/         # this pack
└── miniapp/               # P1
```

---

## Integration boundaries

| System | Bot reads | Bot writes | Human only |
|--------|-----------|------------|------------|
| Telegram | user id, messages, files | messages to user/admin | VIP group add |
| Supabase/Sheets | member, queue | member, queue, tickets | — |
| LearnHouse | — | — | create user, enroll |
| WooCommerce | — (P2 webhook) | — | order verify |
| Website | — | — | checkout, content |

---

## Deployment (MVP)

| Mode | Use |
|------|-----|
| **Polling** | Local dev |
| **Webhook** | Production VPS + TLS |
| **systemd** | Process supervision |

Details: `../DEPLOYMENT.md`

---

## Security

- Admin commands gated by `ADMIN_TELEGRAM_IDS`  
- No bot token or DB credentials in git  
- PII minimized in logs  
- Webhook path secret (P2)  

---

## Defer list

| Item | Phase |
|------|-------|
| WooCommerce webhook | P2 — `12-future-webhook-plan.md` |
| LearnHouse API auto-enroll | P2b |
| Mini App | P1 |
| Telegram Payments API | Not planned (compliance + WC primary) |
| Inner Circle automation | P3 |
