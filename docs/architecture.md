# Architecture — Alpha Elite Stack

> System architecture cho funnel + LMS MVP.

---

## High-level diagram

```text
                    ┌─────────────┐
                    │   Traffic   │
                    │ organic/ads │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  WordPress  │
                    │  Elementor  │
                    │  Landing    │
                    └──────┬──────┘
                           │ opt-in
                    ┌──────▼──────┐
                    │    Brevo    │◄──── WooCommerce sync
                    │   Email     │
                    └──────┬──────┘
                           │ CTA
                    ┌──────▼──────┐
                    │ WooCommerce │
                    │  + FunnelKit│
                    │  Checkout   │
                    └──────┬──────┘
                           │ PayPal
                    ┌──────▼──────┐
              ┌─────┤ Admin Ops   ├─────┐
              │     │  (manual)   │     │
       ┌──────▼──┐  └─────────────┘  ┌──▼───────┐
       │LearnHouse│                   │ Telegram │
       │   LMS    │                   │   VIP    │
       └──────┬───┘                   └──────────┘
              │
       ┌──────▼──────┐
       │  YouTube    │
       │  Unlisted   │
       └─────────────┘
```

---

## Component responsibilities

| Layer | Tech | Responsibility |
|-------|------|----------------|
| CMS | WordPress | Pages, blog, legal |
| Page builder | Elementor | Landing, sales pages |
| Commerce | WooCommerce | Products, orders, subscriptions |
| Funnel | FunnelKit | Checkout UX, bump, upsell, TY |
| Payment | PayPal | Primary gateway MVP |
| Email | Brevo | Lists, automation, transactional |
| LMS | LearnHouse (Docker) | Courses, progress, discussions |
| Video | YouTube Unlisted | Hosting only |
| Community | Telegram | VIP group, support |
| Analytics | GA4 | Events, conversion |

---

## Data flow — order to access

```text
1. User pays → WooCommerce order (source of truth)
2. Webhook/plugin → Brevo tags
3. Admin notified → manual checklist
4. Admin → LearnHouse create user + enroll
5. Admin → Brevo send access_ready (or automation)
6. If VIP → collect @telegram → manual add
7. Order note → provisioned timestamp
```

---

## Domains (đề xuất)

| Subdomain | Service |
|------------|---------|
| `www.domain.com` | WordPress |
| `learn.domain.com` | LearnHouse |
| `hello@domain.com` | Brevo sender |

---

## Security

- WordPress: limit login attempts, 2FA admin
- LearnHouse: HTTPS, strong admin password, backups
- Brevo: API key in env not repo
- Telegram: private invite-only groups
- No API keys in git

---

## Phase 2 integrations

```text
WooCommerce webhook → Make/Zapier → LearnHouse API → auto enroll
Refund webhook → revoke LearnHouse access
```

---

## Hosting

| Service | Host |
|---------|------|
| WordPress | Existing shared/VPS |
| LearnHouse | Separate VPS $10–15/mo |
| DNS | Cloudflare recommended |

---

*Infrastructure changes require update to `docs/sop-ops-runbook.md`.*
