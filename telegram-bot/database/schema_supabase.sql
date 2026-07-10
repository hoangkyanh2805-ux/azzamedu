-- Alpha Elite Telegram Access Bot — Supabase schema
-- Run in Supabase SQL Editor. Service role used by bot backend only.

-- Enums
CREATE TYPE access_tier AS ENUM (
  'free',
  'apprentice',
  'vip',
  'quant',
  'inner_circle'
);

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

CREATE TYPE payment_method AS ENUM ('paypal', 'crypto', 'card', 'unknown');

-- Members (auth = telegram_id)
CREATE TABLE members (
  id                        UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  telegram_id               BIGINT UNIQUE NOT NULL,
  telegram_username         TEXT,
  email                     TEXT,
  tier                      access_tier NOT NULL DEFAULT 'free',
  status                    member_status NOT NULL DEFAULT 'lead',
  sku_last                  TEXT,
  wc_order_id               TEXT,
  payment_method            payment_method,
  vip_username              TEXT,
  learnhouse_url            TEXT DEFAULT 'https://learn.yourdomain.com',
  learnhouse_provisioned_at TIMESTAMPTZ,
  telegram_added_at         TIMESTAMPTZ,
  created_at                TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at                TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_members_email ON members (email);
CREATE INDEX idx_members_status ON members (status);
CREATE INDEX idx_members_wc_order ON members (wc_order_id);

-- Provision queue
CREATE TABLE provision_queue (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  queue_code        TEXT UNIQUE NOT NULL,
  member_id         UUID REFERENCES members(id) ON DELETE SET NULL,
  telegram_id       BIGINT NOT NULL,
  email             TEXT,
  sku               TEXT,
  request_type      TEXT NOT NULL,
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
CREATE INDEX idx_queue_telegram ON provision_queue (telegram_id);

-- Support tickets
CREATE TABLE support_tickets (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  ticket_code   TEXT UNIQUE NOT NULL,
  member_id     UUID REFERENCES members(id) ON DELETE SET NULL,
  telegram_id   BIGINT NOT NULL,
  message       TEXT NOT NULL,
  status        TEXT NOT NULL DEFAULT 'open',
  admin_reply   TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at     TIMESTAMPTZ
);

CREATE INDEX idx_tickets_status ON support_tickets (status);

-- Audit log
CREATE TABLE audit_log (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  actor         TEXT NOT NULL,
  action        TEXT NOT NULL,
  entity_type   TEXT NOT NULL,
  entity_id     UUID,
  payload       JSONB,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Offer catalog (optional — can use config.yaml shop section instead)
CREATE TABLE offers (
  sku           TEXT PRIMARY KEY,
  name          TEXT NOT NULL,
  tier          access_tier NOT NULL,
  category      TEXT DEFAULT 'general',
  price_usd     NUMERIC(10,2),
  checkout_path TEXT NOT NULL,
  active        BOOLEAN DEFAULT true
);

-- Seed offers (G0 draft prices — update after owner sign-off)
INSERT INTO offers (sku, name, tier, category, price_usd, checkout_path) VALUES
  ('AE-APP-001', 'Apprentice Operating Course', 'apprentice', 'khoa_hoc', 297, '/checkout/?add-to-cart=AE-APP-001'),
  ('AE-VIP-MON', 'VIP Private Desk — Monthly', 'vip', 'membership', 149, '/checkout/?add-to-cart=AE-VIP-MON'),
  ('AE-VIP-YR', 'VIP Private Desk — Annual', 'vip', 'membership', 1290, '/checkout/?add-to-cart=AE-VIP-YR'),
  ('AE-QNT-001', 'Quant Desk', 'quant', 'membership', NULL, '/quant-desk'),
  ('AE-DWY-001', 'DWY Bot & Broker Setup', 'vip', 'services', 497, '/checkout/?add-to-cart=AE-DWY-001')
ON CONFLICT (sku) DO NOTHING;

-- updated_at trigger
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER members_updated_at
  BEFORE UPDATE ON members
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER queue_updated_at
  BEFORE UPDATE ON provision_queue
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

-- RLS: enable but deny anon; bot uses service_role key server-side only
ALTER TABLE members ENABLE ROW LEVEL SECURITY;
ALTER TABLE provision_queue ENABLE ROW LEVEL SECURITY;
ALTER TABLE support_tickets ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_log ENABLE ROW LEVEL SECURITY;
ALTER TABLE offers ENABLE ROW LEVEL SECURITY;
