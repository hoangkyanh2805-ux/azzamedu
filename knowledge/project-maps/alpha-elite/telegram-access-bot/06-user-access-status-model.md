# 6 — User Access Status Model

## State machine

```text
                    ┌──────────────┐
                    │  anonymous   │
                    └──────┬───────┘
                           │ /start, optional lead tag
                           ▼
                    ┌──────────────┐
         ┌─────────│    lead      │─────────┐
         │         └──────┬───────┘         │
         │                │ payment intent   │
         │                ▼                  │
         │         ┌──────────────┐          │
         │         │pending_payment│         │
         │         └──────┬───────┘         │
         │                │ proof submitted │
         │                ▼                  │
         │         ┌──────────────┐          │
         │         │payment_review│◄── WC webhook (P2)
         │         └──────┬───────┘         │
         │                │ admin confirm   │
         │                ▼                  │
         │         ┌──────────────┐          │
         │         │payment_confirmed│       │
         │         └──────┬───────┘         │
         │                │ ops picks up    │
         │                ▼                  │
         │         ┌──────────────┐          │
         │         │provisioning  │          │
         │         └──────┬───────┘         │
         │         ┌────────┴────────┐       │
         │         ▼                 ▼       │
         │  ┌─────────────┐   ┌─────────────┐ │
         │  │lh_active    │   │tg_pending   │ │ (VIP only)
         │  │apprentice   │   │(await @user)│ │
         │  └──────┬──────┘   └──────┬──────┘ │
         │         │                 │ admin add
         │         │                 ▼
         │         │          ┌─────────────┐
         │         └─────────►│access_active│
         │                    │_vip         │
         │                    └──────┬──────┘
         │                           │
         │              suspend / refund / chargeback
         │                           ▼
         │                    ┌─────────────┐
         └────────────────────►│revoked      │
                              └─────────────┘
```

---

## Status definitions

| Status | User-visible label | Meaning |
|--------|-------------------|---------|
| `anonymous` | — | Telegram ID only, no email |
| `lead` | Free member | Gameplan path; no paid entitlements |
| `pending_payment` | Awaiting payment | Chose offer; not paid |
| `payment_review` | Payment received — reviewing | Proof or WC order pending admin |
| `payment_confirmed` | Payment confirmed | Paid; queue for provision |
| `provisioning` | Setting up your access | Ops working (≤24h) |
| `lh_active_apprentice` | Course ready | LearnHouse enrolled |
| `tg_pending` | VIP — username needed | Waiting @username or admin add |
| `access_active_vip` | VIP active | LH + Telegram complete |
| `suspended` | Access paused | Payment dispute / policy |
| `revoked` | Access ended | Refund or subscription lapsed |

---

## Database fields (member record)

| Field | Type | Notes |
|-------|------|-------|
| `telegram_id` | bigint | PK |
| `telegram_username` | string | optional |
| `email` | string | match WC billing |
| `status` | enum | above |
| `tier` | enum | `lead` \| `apprentice` \| `vip` \| `quant` |
| `sku` | string | last purchased SKU |
| `wc_order_id` | string | optional until webhook |
| `payment_method` | enum | `paypal` \| `crypto` \| `card` |
| `payment_proof_url` | string | Telegram file ref |
| `vip_username_requested` | string | @handle for VIP |
| `learnhouse_provisioned_at` | datetime | |
| `telegram_added_at` | datetime | |
| `notes` | text | admin |

---

## User-facing `/status` response template

```text
Access status: {status_label}
Tier: {tier}
Email: {email_masked}

LearnHouse: {ready | provisioning | not included}
VIP Desk: {active | pending username | not included}

Questions? /support
Education only — not investment advice. Trading involves risk.
```

---

## Brevo tag alignment (optional sync)

| Status | Suggested Brevo tag |
|--------|---------------------|
| `lead` | `lead_gameplan` |
| `payment_confirmed` | `purchased_{sku}` |
| `lh_active_*` | `access_ready` |
| `access_active_vip` | `telegram_added` |
| `revoked` | remove access tags |

---

## Acceptance

- [ ] Every status has user-facing copy (no internal jargon)
- [ ] VIP cannot reach `access_active_vip` without `payment_confirmed`
- [ ] Refund path documented → `revoked`
