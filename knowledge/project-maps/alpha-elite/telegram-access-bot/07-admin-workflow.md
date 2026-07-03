# 7 — Admin Workflow

> **Owner:** Admin Ops · **SLA:** ≤24h provision (`playbook/ops/learnhouse-provision-sop.md`)

---

## Admin surfaces (MVP)

| Surface | Purpose |
|---------|---------|
| **Admin Telegram chat** | Real-time notifications + `/admin` commands |
| **Google Sheets / Supabase** | Provision queue — source of truth |
| **WooCommerce orders** | Payment verification (primary when checkout used) |
| **LearnHouse admin** | Enroll users |
| **Telegram group admin** | VIP add/remove |

---

## Notification triggers (bot → admin)

| Event | Admin message |
|-------|---------------|
| Payment proof uploaded | `NEW PAYMENT REVIEW · {email} · {sku}` |
| VIP @username submitted | `VIP USERNAME · {email} · @{username}` |
| Support ticket | `SUPPORT #{id} · {telegram_id}` |
| Status stuck >24h | Daily digest (cron) |

---

## Daily ops loop

```text
1. Open admin queue (sheet or /admin pending)
2. For each payment_review:
   a. Match WooCommerce order OR verify PayPal/crypto proof
   b. /admin confirm {id} → payment_confirmed
3. For each payment_confirmed:
   a. Run LearnHouse SOP → provisioning → lh_active
   b. If VIP SKU: request @username if missing
   c. Approve Telegram add → access_active_vip
4. /admin provisioned {id} → notify user via bot
5. Log WooCommerce order note + sheet row
```

---

## Admin commands (bot)

| Command | Action |
|---------|--------|
| `/admin pending` | List rows where status ∈ `payment_review`, `payment_confirmed`, `provisioning`, `tg_pending` |
| `/admin confirm <id>` | `payment_review` → `payment_confirmed` |
| `/admin reject <id> <reason>` | Back to `pending_payment` + notify user |
| `/admin provisioned <id>` | Mark LH done; set `lh_active_*` |
| `/admin tgdone <id>` | Mark Telegram added; `access_active_vip` |
| `/admin revoke <id>` | `revoked` + run revoke SOP |

**Security:** Restrict commands to `ADMIN_TELEGRAM_IDS` in config.

---

## Sheet columns (MVP queue)

| Column | Example |
|--------|---------|
| id | `AE-2026-0042` |
| created_at | ISO datetime |
| telegram_id | 123456789 |
| email | user@example.com |
| sku | AE-VIP-MON |
| status | payment_review |
| wc_order_id | 1847 |
| vip_username | @trader_ops |
| assigned_to | admin name |
| provisioned_at | |
| notes | |

---

## VIP Telegram approval gate

**Never auto-add on bot payment claim alone.**

Checklist before `/admin tgdone`:

- [ ] WooCommerce order paid OR manual payment verified
- [ ] SKU is VIP (MON/YR) or Quant
- [ ] @username matches customer confirmation
- [ ] User acknowledged pinned rules (bot onboarding step)
- [ ] Not on refund/chargeback list

See `playbook/ops/telegram-onboarding-sop.md`.

---

## Escalation

| Case | Action |
|------|--------|
| Payment unclear | Hold status; message user via `/support` thread |
| Duplicate enroll | Check email + order ID |
| Compliance concern in support | Escalate to owner; no trading advice in reply |
| Chargeback | `revoked` + LH + TG remove |

---

## Acceptance

- [ ] Admin can clear queue without leaving Telegram (or with sheet open)
- [ ] Every confirm action logs actor + timestamp
- [ ] Revoke path tested once in dry run
