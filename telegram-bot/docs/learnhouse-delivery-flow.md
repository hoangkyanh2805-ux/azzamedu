# LearnHouse Delivery Flow

## Principle

LearnHouse accounts are **created manually** at MVP (gate G4). The bot **delivers instructions**, not credentials, after admin confirms provision.

## Flow

```text
payment_confirmed
    ↓
Admin: create LH user (email = checkout email)
    ↓
Admin: assign course per SKU
    ↓
Admin: /provisioned AE-YYYY-NNNN
    ↓
Bot sends learnhouse_ready.md template
    ↓
members.status → lh_active_apprentice (or lh_active_vip)
```

## SKU → LearnHouse bundles

| SKU | LH content |
|-----|------------|
| AE-APP-001 | Apprentice Operating Course (5 modules) |
| AE-VIP-MON/YR | Apprentice + VIP resource library |
| AE-QNT-001 | Above + Quant modules |
| AE-DWY-001 | No LH change — setup session only |

## Bot template (`learnhouse_ready.md`)

- LearnHouse URL from config
- "Use your checkout email"
- Complete Module 1 before VIP desk
- Education disclaimer

## SOP reference

`playbook/ops/learnhouse-provision-sop.md` (repo root)

## SLA

≤ 24 business hours from `/confirm` to `/provisioned`

## Troubleshooting (support)

| Issue | Resolution |
|-------|------------|
| No invite email | Resend from LH admin; check spam |
| Wrong email | Admin updates LH user; note in queue |
| Wrong course | Admin fixes enrollment |

## Future (P2)

- LearnHouse API / SSO if available
- Auto-enroll on WooCommerce webhook + provisioned flag
- Mini App deep link to LH with signed token

## Security

- Bot never stores LH passwords
- Do not paste credentials in Telegram chat
- Service role DB access only server-side
