# 12 — Future Webhook Plan (WooCommerce)

> **Phase:** P2 — after MVP manual flow stable (30+ provisions, zero P0 incidents)  
> **Extended spec:** `knowledge/project-maps/alpha-elite/telegram-access-bot/11-future-webhook-plan.md`

---

## Objective

Automatically sync WooCommerce orders to bot `members` + `provision_queue`, notify admin, and let users link Telegram via deep link — **without** removing human G4/G5 for LearnHouse and VIP Telegram.

---

## Architecture

```text
WooCommerce (order.completed)
        │
        ▼ POST /hooks/woocommerce/order
┌───────────────────┐
│ Webhook service   │  Python FastAPI (same VPS or worker)
│ HMAC verify       │
└─────────┬─────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
 Supabase    Admin Telegram
 update      "WC ORDER {id}"
```

---

## Events to handle

| WC event | Bot action |
|----------|------------|
| `order.processing` | Log; optional `payment_review` if user linked |
| `order.completed` | `payment_confirmed` if telegram_id linked |
| `order.refunded` | `revoked` + admin alert |
| Subscription renewal | Extend VIP status |
| Subscription cancel | Schedule revoke at period end |

---

## User linking (required for auto-status)

```text
Thank-you page CTA:
  https://t.me/YourBot?start=order_{woocommerce_order_id}

/start order_1847
  → bot associates telegram_id ↔ wc_order_id
  → when webhook arrives, match completes
```

---

## Payload mapping

| WC field | DB field |
|----------|----------|
| `billing.email` | `members.email` |
| `id` | `wc_order_id` |
| `line_items[0].sku` | `sku_last` |
| `total` | verify against G0 price |
| `meta.telegram_username` | `vip_username` (if TY form writes meta) |

---

## What stays manual (MVP+ policy)

| Step | Auto? | Gate |
|------|-------|------|
| Payment detect | ✓ webhook | — |
| Admin notify | ✓ | — |
| LearnHouse enroll | Optional API | **G4** until API trusted |
| VIP Telegram add | ✗ MVP+ | **G5** |
| Bot user message | ✓ after provisioned/tgdone | — |

---

## Security

- [ ] `WC_WEBHOOK_SECRET` HMAC validation  
- [ ] Idempotency: `order_id + status`  
- [ ] No email in admin chat — mask `u***@domain.com`  
- [ ] Rate limit endpoint  

---

## Rollout phases

| Phase | Scope |
|-------|-------|
| **P2a** | Webhook logs + admin notify only |
| **P2b** | Auto `payment_confirmed` when telegram linked |
| **P2c** | LearnHouse API enroll (if available) |
| **P2d** | Brevo tag sync |
| **P3** | Auto VIP invite (policy decision only) |

---

## Implementation tasks (backlog)

| ID | Task |
|----|------|
| TB-L02 | FastAPI webhook route |
| TB-L02a | WC webhook registration in WP |
| TB-L02b | Deep link on all TY pages |
| TB-L02c | Idempotency + tests |
| TB-L02d | Refund → revoke automation |

---

## Rollback

1. Disable WC webhook in WooCommerce admin  
2. Bot falls back to manual `/pay` + admin confirm  
3. Queue processed from sheet only  

---

## Acceptance (P2)

- [ ] Test order per SKU updates linked member  
- [ ] Refund test triggers revoke workflow  
- [ ] Unlinked orders still work via manual queue  
- [ ] Compliance review on any new automated user messages
