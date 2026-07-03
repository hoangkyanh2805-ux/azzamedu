# 11 — Future Webhook Plan (WooCommerce → Bot → LearnHouse)

> **Phase:** P2 — after manual MVP stable 30+ provisions without errors.

---

## Goals

1. Auto-create / update member record on WooCommerce order
2. Reduce manual payment proof for card/PayPal checkout
3. Optionally trigger LearnHouse enrollment API (when available)
4. Keep **Telegram VIP add as admin-approved** until trust + mod capacity proven

---

## Target architecture

```text
WooCommerce order completed
        │
        ▼
┌───────────────────┐
│ Webhook receiver  │  Python FastAPI on VPS / Cloudflare Worker
│ (HMAC verify)     │
└─────────┬─────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
┌────────┐  ┌─────────────┐
│Supabase│  │ Telegram    │
│ members│  │ admin notify│
└────┬───┘  └─────────────┘
     │
     ▼
┌────────────────┐      ┌──────────────┐
│ Status:        │      │ Brevo API    │
│ payment_confirmed     │ tag purchased│
└────────┬───────┘      └──────────────┘
         │
         ▼ (optional API)
┌────────────────┐
│ LearnHouse API │  P2b — if documented
│ auto-enroll    │
└────────────────┘
```

---

## WooCommerce webhook events

| Event | Action |
|-------|--------|
| `order.created` | Log pending if status `on-hold` |
| `order.processing` | `payment_confirmed` + notify admin |
| `order.completed` | Same + start provision timer |
| `order.refunded` | `revoked` + revoke SOP |
| `subscription.renewal` | VIP extend `access_active_vip` |
| `subscription.cancelled` | Schedule `revoked` at period end |

**Plugin:** WooCommerce webhooks or FunnelKit-compatible hook — verify payload schema in staging.

---

## Payload mapping

| WC field | Member field |
|----------|--------------|
| `billing.email` | `email` |
| `id` | `wc_order_id` |
| `line_items[0].sku` | `sku` |
| `total` | verify amount |
| `meta.telegram_username` | `vip_username_requested` (if TY form writes meta) |

**Gap:** Link `telegram_id` — user must `/link {order_id}` in bot once, or TY Mini App passes `start_param`.

---

## Bot linking flow (recommended)

```text
Thank-you page: "Open Telegram bot" with ?start=order_1847
Bot /start order_1847 → associates telegram_id + wc_order_id
Webhook arrives → finds member by order id → updates status
```

---

## Security

- [ ] Verify WooCommerce webhook signature secret
- [ ] Idempotency key = order_id + status
- [ ] No PII in admin Telegram beyond email mask
- [ ] Rate limit webhook endpoint

---

## LearnHouse automation (P2b)

| Step | Manual MVP | Webhook phase |
|------|------------|---------------|
| Create user | Admin UI | API POST `/users` (if available) |
| Enroll course | Admin UI | API enroll endpoint |
| Notify | Brevo + bot | Same, triggered by job queue |

**Fallback:** Webhook only updates status; human still enrolls until API tested.

---

## Brevo sync (optional)

| Webhook event | Brevo action |
|---------------|--------------|
| `order.completed` | Add tag `purchased_{sku}` |
| `access provisioned` | Tag `access_ready` |
| `revoked` | Remove purchase tags |

---

## Migration from Sheets

1. Export sheet → Supabase `members` + `provision_queue`
2. Dual-write period: webhook + manual admin commands
3. Deprecate sheet when 2 weeks zero discrepancies

---

## Rollout phases

| Phase | Scope |
|-------|-------|
| **P2a** | WC webhook → Supabase + admin Telegram only |
| **P2b** | User `/status` auto-updates from WC |
| **P2c** | LearnHouse API enroll |
| **P2d** | Brevo bi-directional tags |
| **P3** | Auto VIP invite link (only if policy allows) |

---

## Acceptance

- [ ] Staging webhook tested with test order per SKU
- [ ] Refund test revokes access end-to-end
- [ ] Compliance review on any new automated user messages
- [ ] Rollback plan: disable webhook, revert to manual queue

---

## Related docs

- `docs/funnelkit_checkout_map.md`
- `docs/mvp-system-map.md` (deferred items)
- `knowledge/project-maps/alpha-elite/README.md`
