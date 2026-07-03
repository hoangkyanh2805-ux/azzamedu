# Stack Architecture — Alpha Elite

> **Kickstart artifact #2** · How each tool fits the MVP.

---

## Architecture diagram

```text
                         TRAFFIC
                            │
              ┌─────────────▼─────────────┐
              │   WordPress + Elementor    │  ← Landing, sales, legal
              │   (Marketing front door)   │
              └─────────────┬─────────────┘
                            │
         ┌──────────────────┼──────────────────┐
         │ opt-in           │ purchase          │
         ▼                  ▼                   │
┌─────────────────┐  ┌──────────────────────┐ │
│     Brevo       │  │ WooCommerce          │ │
│ · Gameplan send │  │ + FunnelKit          │ │
│ · 7-day nurture │  │ · checkout           │ │
│ · onboarding    │  │ · bump / upsell / TY │ │
└────────┬────────┘  └──────────┬───────────┘ │
         │                      │             │
         │            ┌─────────▼─────────┐   │
         │            │ PayPal + Crypto   │   │
         │            │ (manual crypto)   │   │
         │            └─────────┬─────────┘   │
         │                      │             │
         │            ┌─────────▼─────────┐   │
         │            │   Admin Ops       │   │
         │            │  MANUAL MVP       │   │
         │            └─────────┬─────────┘   │
         │         ┌────────────┼────────────┐ │
         │         ▼            ▼            ▼ │
         │   ┌──────────┐ ┌─────────┐ ┌──────────┐
         │   │LearnHouse│ │ Brevo   │ │ Telegram │
         │   │  (LMS)   │ │ access  │ │ VIP desk │
         │   └────┬─────┘ └─────────┘ └──────────┘
         │        │
         │        ▼
         │   ┌──────────┐
         └──►│ YouTube  │
             │ Unlisted │  ← Video embed only
             └──────────┘
```

---

## Component matrix

| Layer | Technology | Responsibility | Owner (MVP) |
|-------|------------|----------------|-------------|
| **Marketing** | WordPress | CMS, URLs, media | Tech |
| **Pages** | Elementor | Landing, `/apprentice`, `/vip`, legal | Tech + Copy |
| **Commerce** | WooCommerce | Products, orders, subscriptions | Tech |
| **Funnel UX** | FunnelKit | Checkout, order bump, upsell, thank-you | Tech |
| **Payments** | PayPal | Primary gateway | Owner (G6) |
| **Payments** | Crypto | Manual invoice MVP | Owner (G6) |
| **Email** | Brevo | Lists, automation, transactional | Ops |
| **LMS** | LearnHouse (self-host) | Courses, progress, VIP library | Tech + Ops |
| **Video** | YouTube Unlisted | Lesson hosting (embed) | Content |
| **Community** | Telegram | VIP accountability desk | Ops |
| **Analytics** | GA4 | Events, conversion | Tech |

---

## Integration points

| From | To | Mechanism (MVP) |
|------|-----|-----------------|
| Elementor form | Brevo | Plugin / API → list `gameplan-leads` |
| WooCommerce order | Brevo | Official integration → tags |
| WooCommerce order | Admin | Email / Slack notification |
| Admin | LearnHouse | Manual UI create user + enroll |
| Admin | Brevo | Send `access_ready` template |
| Admin | Telegram | Manual add by @username |
| LearnHouse | YouTube | Unlisted embed in lessons |

**Phase 2:** WooCommerce webhook → LearnHouse API auto-enroll.

---

## Data sources of truth

| Data | Source of truth |
|------|-----------------|
| Paid / entitled | WooCommerce order status |
| Email list membership | Brevo |
| Course access | LearnHouse enrollment |
| VIP community | Telegram membership (manual log) |

---

## Domains & hosting

| Host | URL | Spec |
|------|-----|------|
| WordPress | `www.[domain].com` | Existing host/VPS |
| LearnHouse | `learn.[domain].com` | VPS 2 vCPU / 4GB · Docker |
| Email sender | `hello@[domain].com` | Brevo verified domain |

---

## Security baseline

- HTTPS everywhere  
- WP admin 2FA  
- API keys in env (never in git)  
- Telegram private invite-only  
- Weekly `learnhouse backup`  

---

## Stack doc index

| Topic | File |
|-------|------|
| End-to-end flows | `mvp-system-map.md` |
| FunnelKit flows | `funnelkit_checkout_map.md` |
| LearnHouse | `learnhouse_lms_map.md` |
| Ops | `sop-ops-runbook.md` |

Also mirrored in `architecture.md` (legacy short form).
