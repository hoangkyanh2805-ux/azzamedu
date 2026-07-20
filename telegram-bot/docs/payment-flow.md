# Payment Flow

## Channels (MVP priority)

| Channel | Role | Automation |
|---------|------|------------|
| WooCommerce / FunnelKit | Primary card checkout (Alpha Elite stack) | P2 webhook |
| PayPal (manual) | Off-card / international | Bot instructions + proof |
| Crypto USDT | Alternative | Bot instructions + proof |
| **@Azzam_Storebot** | **Payment bot cho 4 khóa NCI/Azzam live trên LearnHouse** | Sale gửi deep-link → khách tự thanh toán |

> **Brand split:** @Azzam_Storebot phục vụ 4 khóa NCI/Azzam (learn.azzamedu.com).
> Các channel Woo/PayPal/USDT phục vụ stack Alpha Elite (Apprentice/VIP).
> Hai brand tách biệt — KHÔNG trộn SKU giữa 2 hệ.

### @Azzam_Storebot — handoff flow (sale-driven)
1. Sale tư vấn xong → gửi deep-link Storebot theo khóa (tham khảo `sales/assets/nci-course-sales-support.md` §9).
2. Khách thanh toán trong Storebot → nhận order ID / receipt.
3. Xác nhận đơn → cấp access LearnHouse (manual ≤24h hoặc auto nếu Storebot có webhook).
4. Chưa có webhook Storebot → sale/admin enroll thủ công theo `playbook/ops/learnhouse-provision-sop.md`.

> TODO (khi bot live): bổ sung product ID thật vào deep-link, xác nhận có webhook callback hay không để automate provision.

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
