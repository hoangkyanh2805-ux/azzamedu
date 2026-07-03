# Payment Flow

## Channels (MVP priority)

| Channel | Role | Automation |
|---------|------|------------|
| WooCommerce / FunnelKit | Primary card checkout | P2 webhook |
| PayPal (manual) | Off-card / international | Bot instructions + proof |
| Crypto USDT | Alternative | Bot instructions + proof |

## User flow (manual)

1. User opens **💳 Payment** in bot
2. Sees PayPal email + crypto wallet from `config.yaml`
3. Pays externally with note: `@username` + SKU
4. Taps **Submit payment proof**
5. Enters checkout email
6. Sends TX ID or screenshot description
7. Bot creates `provision_queue` row (`AE-YYYY-NNNN`)
8. Admins notified via Telegram

## Admin verification

| Check | Source |
|-------|--------|
| Amount matches SKU | PayPal / chain explorer |
| Email matches | WooCommerce order or PayPal |
| SKU entitlement | Queue row |
| Duplicate | Same TX ID / order |

On pass: `/confirm <code>` → G4 → `/provisioned` → (VIP) `/tgdone`

## Config example

```yaml
payment:
  paypal_email: hello@yourdomain.com
  crypto:
    network: USDT TRC20
    wallet: TYourWalletAddress

pricing_usd:  # G0 draft
  AE-APP-001: 297
  AE-VIP-MON: 149
  AE-VIP-YR: 1290
  AE-DWY-001: 497
```

## Database fields

- `members.payment_method`: `paypal` | `crypto` | `card` | `unknown`
- `members.sku_last`, `members.wc_order_id`
- `provision_queue.payment_proof_ref`, `provision_queue.wc_order_id`

## Compliance

- Payment messages must not promise returns
- State clearly: access granted only after admin review
- No "instant VIP" language

## P2 — WooCommerce

When `order.completed` webhook fires:

1. Match email → `telegram_id` (user linked bot first) or queue by email
2. Set `payment_confirmed` automatically
3. Still require human G4/G5 for LH and VIP

See `docs/future-webhook-plan.md`.
