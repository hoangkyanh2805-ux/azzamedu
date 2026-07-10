-- Migration 002: Woo → Supabase shop catalog (Model B)
-- Run in Supabase SQL Editor after schema_supabase.sql

CREATE TABLE IF NOT EXISTS shop_categories (
  id          TEXT PRIMARY KEY,
  label       TEXT NOT NULL,
  sort_order  INT NOT NULL DEFAULT 0,
  active      BOOLEAN NOT NULL DEFAULT true
);

INSERT INTO shop_categories (id, label, sort_order) VALUES
  ('khoa_hoc', '📚 Khóa học', 1),
  ('membership', '🏛 Membership', 2),
  ('free', '🎁 Free', 3),
  ('services', '🔧 Services', 4)
ON CONFLICT (id) DO NOTHING;

ALTER TABLE offers ADD COLUMN IF NOT EXISTS wc_product_id BIGINT;
ALTER TABLE offers ADD COLUMN IF NOT EXISTS category TEXT DEFAULT 'general';
ALTER TABLE offers ADD COLUMN IF NOT EXISTS display_name TEXT;
ALTER TABLE offers ADD COLUMN IF NOT EXISTS emoji TEXT;
ALTER TABLE offers ADD COLUMN IF NOT EXISTS kind TEXT DEFAULT 'checkout';
ALTER TABLE offers ADD COLUMN IF NOT EXISTS callback_data TEXT;
ALTER TABLE offers ADD COLUMN IF NOT EXISTS apply_path TEXT;
ALTER TABLE offers ADD COLUMN IF NOT EXISTS sort_order INT DEFAULT 0;
ALTER TABLE offers ADD COLUMN IF NOT EXISTS active_on_bot BOOLEAN DEFAULT true;
ALTER TABLE offers ADD COLUMN IF NOT EXISTS synced_at TIMESTAMPTZ;

CREATE INDEX IF NOT EXISTS idx_offers_category ON offers (category);
CREATE INDEX IF NOT EXISTS idx_offers_active_bot ON offers (active, active_on_bot);

ALTER TABLE shop_categories ENABLE ROW LEVEL SECURITY;
