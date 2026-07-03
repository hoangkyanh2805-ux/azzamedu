# Access Control Model

## Tiers (`access_tier`)

| Tier | User label | Description |
|------|------------|-------------|
| `free` | Free | Gameplan lead |
| `apprentice` | Apprentice | Course buyer |
| `vip` | VIP | Private desk member |
| `quant` | Quant | Quant Desk |
| `inner_circle` | Inner Circle | Invite-only (P2) |

## Status (`member_status`)

| Status | User sees | Next step |
|--------|-----------|-----------|
| `lead` | Free member | Browse / checkout |
| `pending_payment` | Awaiting payment | Pay or submit proof |
| `payment_review` | Under review | Wait for admin |
| `payment_confirmed` | Payment confirmed | G4 in progress |
| `provisioning` | Setting up | G4 |
| `lh_active_apprentice` | LearnHouse ready | Log in |
| `lh_active_vip` | LearnHouse ready | VIP steps |
| `tg_pending` | VIP pending approval | Submit @username |
| `access_active_vip` | VIP active | Desk rules |
| `access_active_quant` | Quant active | Priority channel |
| `suspended` | Access paused | Contact support |
| `revoked` | Access ended | — |

## Auth model (MVP)

- **Identity:** `telegram_id` (unique)
- **Email:** optional until payment proof or webhook
- **No RBAC in bot** — admin = config allowlist of Telegram IDs
- **Entitlements:** derived from `tier` + `status`, not separate permissions table

## What each tier can do in bot

| Action | free | apprentice | vip | quant |
|--------|------|------------|-----|-------|
| View offers | ✅ | ✅ | ✅ | ✅ |
| See LH URL | ❌ | ✅* | ✅* | ✅* |
| VIP status line | ❌ | ❌ | ✅ | ✅ |
| Submit payment proof | ✅ | ✅ | ✅ | ✅ |

\*After `lh_active_*` or `access_active_*`

## VIP Telegram access

- **Never** auto-granted at MVP
- Requires `tg_pending` → admin G5 → `access_active_vip`
- Bot sends invite **message** only; human sends actual Telegram invite link

## Schema

See `database/schema_supabase.sql` — tables `members`, `provision_queue`, `audit_log`.

## Future (P2)

- WooCommerce order meta → auto-set `tier` + `wc_order_id`
- LearnHouse API → auto-enroll on webhook
- Mini App read-only dashboard signed by Telegram `initData`
