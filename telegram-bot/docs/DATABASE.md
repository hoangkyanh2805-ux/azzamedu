# Database schema — Telegram Access Bot

> **MVP:** Supabase (Postgres) recommended · Google Sheets acceptable for queue-only MVP  
> **Maps to:** `06-user-access-status-model.md`

---

## Enums

### `access_tier`

```sql
CREATE TYPE access_tier AS ENUM (
  'free',           -- Gameplan lead
  'apprentice',
  'vip',
  'quant',
  'inner_circle'
);
```

### `member_status`

```sql
CREATE TYPE member_status AS ENUM (
  'anonymous',
  'lead',
  'pending_payment',
  'payment_review',
  'payment_confirmed',
  'provisioning',
  'lh_active_apprentice',
  'lh_active_vip',
  'tg_pending',
  'access_active_vip',
  'access_active_quant',
  'suspended',
  'revoked'
);
```

### `payment_method`

```sql
CREATE TYPE payment_method AS ENUM ('paypal', 'crypto', 'card', 'unknown');
```

---

## Table: `members`

Primary identity = **Telegram ID**.

```sql
CREATE TABLE members (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  telegram_id       BIGINT UNIQUE NOT NULL,
  telegram_username TEXT,
  email             TEXT,
  tier              access_tier NOT NULL DEFAULT 'free',
  status            member_status NOT NULL DEFAULT 'lead',
  sku_last          TEXT,
  wc_order_id       TEXT,
  payment_method    payment_method,
  vip_username      TEXT,
  learnhouse_url    TEXT DEFAULT 'https://learn.yourdomain.com',
  learnhouse_provisioned_at TIMESTAMPTZ,
  telegram_added_at TIMESTAMPTZ,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_members_email ON members (email);
CREATE INDEX idx_members_status ON members (status);
CREATE INDEX idx_members_wc_order ON members (wc_order_id);
```

---

## Table: `provision_queue`

One row per payment claim, upgrade request, or VIP username submission.

```sql
CREATE TABLE provision_queue (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  queue_code        TEXT UNIQUE NOT NULL,  -- e.g. AE-2026-0042
  member_id         UUID REFERENCES members(id),
  telegram_id       BIGINT NOT NULL,
  email             TEXT,
  sku               TEXT,
  request_type      TEXT NOT NULL,  -- payment_proof | upgrade | vip_username | wc_order
  status            member_status NOT NULL DEFAULT 'payment_review',
  payment_proof_ref TEXT,
  wc_order_id       TEXT,
  admin_notes       TEXT,
  assigned_to       TEXT,
  confirmed_at      TIMESTAMPTZ,
  provisioned_at    TIMESTAMPTZ,
  tg_done_at        TIMESTAMPTZ,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_queue_status ON provision_queue (status);
CREATE INDEX idx_queue_created ON provision_queue (created_at DESC);
```

---

## Table: `support_tickets`

```sql
CREATE TABLE support_tickets (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  ticket_code   TEXT UNIQUE NOT NULL,  -- SUP-0042
  member_id     UUID REFERENCES members(id),
  telegram_id   BIGINT NOT NULL,
  message       TEXT NOT NULL,
  status        TEXT NOT NULL DEFAULT 'open',  -- open | replied | closed
  admin_reply   TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at     TIMESTAMPTZ
);
```

---

## Table: `audit_log`

```sql
CREATE TABLE audit_log (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  actor         TEXT NOT NULL,  -- telegram_id or admin name
  action        TEXT NOT NULL,  -- confirm | provisioned | tgdone | revoke
  entity_type   TEXT NOT NULL,
  entity_id     UUID,
  payload       JSONB,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

---

## Table: `offers` (config cache)

Optional — can also live in `config.yaml`.

```sql
CREATE TABLE offers (
  sku           TEXT PRIMARY KEY,
  name          TEXT NOT NULL,
  tier          access_tier NOT NULL,
  price_usd     NUMERIC(10,2),
  checkout_path TEXT NOT NULL,
  active        BOOLEAN DEFAULT true
);
```

Seed from `docs/offer_stack.md`:

| sku | tier |
|-----|------|
| AE-APP-001 | apprentice |
| AE-VIP-MON | vip |
| AE-VIP-YR | vip |
| AE-QNT-001 | quant |
| AE-DWY-001 | vip (bump) |

---

## Google Sheets MVP (alternative)

| Sheet | Columns |
|-------|---------|
| `members` | telegram_id, email, tier, status, sku, wc_order_id, vip_username, updated_at |
| `queue` | queue_code, telegram_id, email, sku, status, notes, created_at |
| `tickets` | ticket_code, telegram_id, message, status, created_at |

---

## Tier vs status (user dashboard)

| User label (`/status`) | `tier` | Typical `status` |
|------------------------|--------|------------------|
| Free | free | lead |
| Apprentice | apprentice | lh_active_apprentice |
| VIP | vip | access_active_vip |
| Quant | quant | access_active_quant |
| Inner Circle | inner_circle | tg_pending / manual |

---

## RLS (Supabase)

- Bot service role: full access via backend only  
- No anon client exposure of `members.email`  
- Mini App (P1): read-only view for own `telegram_id` via signed token

---

## Migration

1. Run SQL in Supabase SQL editor  
2. Set `DATABASE_URL` in bot env  
3. Seed `offers` from `offer_stack.md` after G0
