# 6 — Database Schema

> **Full DDL:** `../DATABASE.md`  
> **MVP pick:** Supabase (recommended) or Google Sheets (fastest)

---

## Entity relationship

```text
members (1) ──< (N) provision_queue
members (1) ──< (N) support_tickets
members (1) ──< (N) audit_log (via actor ref)

offers (config) — referenced by SKU
```

---

## Enums

### `access_tier` (user-facing tier)

| Value | Label |
|-------|-------|
| `free` | Free |
| `apprentice` | Apprentice |
| `vip` | VIP |
| `quant` | Quant |
| `inner_circle` | Inner Circle |

### `member_status` (pipeline)

`anonymous` → `lead` → `pending_payment` → `payment_review` → `payment_confirmed` → `provisioning` → `lh_active_*` → `tg_pending` → `access_active_vip` → (`revoked`)

See `knowledge/.../06-user-access-status-model.md` for full definitions.

---

## Core tables (summary)

| Table | PK | Purpose |
|-------|-----|---------|
| `members` | `id` / `telegram_id` unique | User identity + tier + status |
| `provision_queue` | `queue_code` | Payment proofs, upgrades, VIP username |
| `support_tickets` | `ticket_code` | Support threads |
| `audit_log` | `id` | Admin actions |
| `offers` | `sku` | Catalog cache (optional) |

---

## `members` key fields

| Column | Notes |
|--------|-------|
| `telegram_id` | BIGINT UNIQUE — auth |
| `email` | Link to WC billing |
| `tier` | access_tier |
| `status` | member_status |
| `sku_last` | Last purchase |
| `wc_order_id` | P2 webhook |
| `vip_username` | @handle for G5 |
| `learnhouse_provisioned_at` | G4 timestamp |
| `telegram_added_at` | G5 timestamp |

---

## `provision_queue` key fields

| Column | Notes |
|--------|-------|
| `queue_code` | `AE-2026-0042` human-friendly |
| `request_type` | `payment_proof` \| `upgrade` \| `vip_username` |
| `payment_proof_ref` | Telegram file id or txn text |
| `status` | mirrors pipeline |

---

## Google Sheets MVP layout

| Sheet | Key columns |
|-------|-------------|
| `members` | telegram_id, email, tier, status, sku, vip_username, updated_at |
| `queue` | queue_code, telegram_id, email, sku, status, notes, created_at |
| `tickets` | ticket_code, telegram_id, message, status, created_at |

**Trade-off:** Sheets OK for <50 members/month; migrate to Supabase before webhooks.

---

## Seed data (`offers`)

| sku | tier | checkout_path |
|-----|------|---------------|
| AE-APP-001 | apprentice | `/checkout/?add-to-cart=AE-APP-001` |
| AE-VIP-MON | vip | `/checkout/?add-to-cart=AE-VIP-MON` |
| AE-VIP-YR | vip | `/checkout/?add-to-cart=AE-VIP-YR` |
| AE-QNT-001 | quant | `/quant-desk` |
| AE-DWY-001 | vip | VIP bump |

---

## Migrations

1. Run SQL in `../DATABASE.md` on Supabase  
2. Enable RLS — service role only from bot backend  
3. No anon read of `email`  

---

## Acceptance

- [ ] `telegram_id` unique constraint  
- [ ] Queue links to member  
- [ ] Schema supports all 5 tier labels + MVP statuses
