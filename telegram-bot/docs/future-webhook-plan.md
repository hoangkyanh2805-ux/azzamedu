# Future Webhook Plan — WooCommerce → Bot

## Goal

Close the loop between WordPress checkout and Telegram member record without manual payment proof for card orders.

## Phase P2 scope

1. WooCommerce `order.completed` (or FunnelKit equivalent) → HTTPS webhook
2. Verify HMAC signature / shared secret
3. Upsert `members` by billing email + optional `telegram_id` meta
4. Insert `provision_queue` with `request_type: wc_order`
5. Notify admins (same as manual proof)
6. Optionally auto `/confirm` for trusted payment methods

## Endpoint (planned)

```text
POST /webhooks/woocommerce/order
Headers: X-WC-Webhook-Signature
Body: order JSON (id, billing.email, line_items[].sku, meta_data)
```

## Order meta (recommended)

| Meta key | Purpose |
|----------|---------|
| `_ae_telegram_id` | Link bot user from thank-you page |
| `_ae_sku` | Primary SKU |
| `_ae_queue_code` | Idempotency |

## Thank-you page integration

1. User pays on site
2. Thank-you: "Connect Telegram" button with `?start=order_<id>` deep link
3. Bot `/start` payload parses order id → prompts email confirm → links `wc_order_id`

## Idempotency

- Unique index on `provision_queue.wc_order_id`
- Ignore duplicate webhooks for same order id

## Still human at MVP+1

| Step | Auto? |
|------|-------|
| Payment confirmed (card) | ✅ webhook |
| LearnHouse create | ❌ G4 manual |
| VIP Telegram add | ❌ G5 manual |

## Security

- Webhook secret in env only
- Validate SKU against `offers` table
- Rate limit endpoint
- No PII in application logs

## Implementation sketch

```python
# bot/webhooks/woocommerce.py (P2)
async def handle_order(payload: dict) -> None:
    order_id = str(payload["id"])
    email = payload["billing"]["email"]
    skus = [li["sku"] for li in payload["line_items"]]
    telegram_id = meta.get("_ae_telegram_id")
    # upsert member, create queue, notify_admins()
```

## Rollout

1. Staging WooCommerce → staging bot
2. Test orders AE-APP-001, AE-VIP-MON
3. Compliance review of auto-confirm copy
4. Production with manual G4/G5 unchanged
