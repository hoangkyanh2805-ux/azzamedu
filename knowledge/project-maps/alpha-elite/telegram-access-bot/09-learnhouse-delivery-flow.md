# 9 — LearnHouse Delivery Flow

> **SLA:** ≤24h from payment confirmed · **SOP:** `playbook/ops/learnhouse-provision-sop.md`

---

## Trigger

| Source | Trigger |
|--------|---------|
| WooCommerce | Order `Processing` or `Completed` |
| Bot manual | Admin `/admin confirm` → `payment_confirmed` |
| Brevo | Parallel `access_ready` email (not replaced by bot) |

---

## SKU → LearnHouse mapping

| SKU | User group | Courses |
|-----|------------|---------|
| `AE-APP-001` | `apprentice-students` | Apprentice Operating Course |
| `AE-VIP-MON` | `vip-members` | Apprentice + VIP Resource Library |
| `AE-VIP-YR` | `vip-members` | Apprentice + VIP Resource Library |
| `AE-QNT-001` | `quant-desk` | Above + Quant (when live) |

---

## End-to-end flow

```text
payment_confirmed
       │
       ▼
┌──────────────────┐
│ status:          │
│ provisioning     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐     ┌─────────────────┐
│ LearnHouse admin │────►│ Create user     │
│ (human G4)       │     │ email = billing │
└────────┬─────────┘     └────────┬────────┘
         │                          │
         ▼                          ▼
┌──────────────────┐     ┌─────────────────┐
│ Enroll courses   │     │ Password reset  │
│ per SKU table    │     │ email to user   │
└────────┬─────────┘     └────────┬────────┘
         │                          │
         └──────────┬───────────────┘
                    ▼
         ┌──────────────────┐
         │ status:          │
         │ lh_active_*      │
         └────────┬─────────┘
                  │
      ┌───────────┴───────────┐
      ▼                         ▼
 Bot notifies user      Brevo access_ready
 "Course is ready"       template (parallel)
 LH URL button
```

---

## Bot messages (templates)

### Provisioning (immediate after confirm)

```text
Payment confirmed — we're setting up your LearnHouse access.

Usually within 24 hours you'll receive login instructions at {email}.
Status: /status

Education only. Trading involves risk.
```

### Access ready

```text
Your Apprentice course is ready on LearnHouse.

Login: {learnhouse_url}
Use "Forgot password" with {email} if needed.

Start with Module 1 — Operating Mindset.
Need help? /support
```

### VIP add-on (after LH, before TG)

```text
Course access is active. For VIP Private Desk, submit your Telegram username:
Tap below and send @yourusername (admin approval required).
```

---

## Bot ↔ LearnHouse boundary (MVP)

| Bot does | LearnHouse does |
|----------|-----------------|
| Show link + status | Host videos, worksheets, progress |
| Remind Module 1 | Track completion |
| Escalate login issues | Auth + enrollment |

**No** course video delivery inside Telegram (compliance + UX).

---

## Failure modes

| Problem | Bot response | Ops action |
|---------|--------------|------------|
| >24h no access | Apologize + /support | Priority queue |
| Wrong email | Ask user to confirm | Fix in LH + WC |
| Can't login | Link to reset | Verify enrollment |
| Refund | Status `revoked` | Remove enrollment |

---

## Mini App (P1) display

Timeline step: **LearnHouse** — ✅ Ready | ⏳ Provisioning | — Not included

Button: **Open LearnHouse** (enabled when `lh_active_*`)

---

## Acceptance

- [ ] Bot never claims course guarantees trading results
- [ ] Login URL from config, not hardcoded in code without env
- [ ] VIP SKU still triggers Telegram flow after LH step
