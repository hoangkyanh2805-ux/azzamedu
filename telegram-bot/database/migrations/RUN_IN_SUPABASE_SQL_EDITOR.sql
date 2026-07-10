-- RUN IN SUPABASE SQL EDITOR (one paste)
-- Project: alpha-elite-bot (updklrkzxxqqyddyxjcd)
-- After run: python scripts/seed-shop-catalog.py && restart bot

-- === 002 shop catalog ===
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

-- Map existing offers
UPDATE offers SET category = 'khoa_hoc', emoji = '📘', kind = 'checkout', sort_order = 1, display_name = name
  WHERE sku = 'AE-APP-001';
UPDATE offers SET category = 'membership', emoji = '🏛', kind = 'checkout', sort_order = 2, display_name = name
  WHERE sku = 'AE-VIP-MON';
UPDATE offers SET category = 'membership', emoji = '🏛', kind = 'checkout', sort_order = 3, display_name = name
  WHERE sku = 'AE-VIP-YR';
UPDATE offers SET category = 'membership', emoji = '📊', kind = 'apply', apply_path = '/quant-desk', sort_order = 4, display_name = name
  WHERE sku = 'AE-QNT-001';
UPDATE offers SET category = 'services', emoji = '🔧', kind = 'callback', callback_data = 'offer:dwy', sort_order = 5, display_name = name
  WHERE sku = 'AE-DWY-001';

INSERT INTO offers (sku, name, tier, category, price_usd, checkout_path, emoji, kind, sort_order, active, active_on_bot, display_name)
VALUES ('AE-GP-000', '2% Rule Gameplan', 'free', 'free', NULL, '/gameplan', '🎁', 'gameplan', 1, true, true, '2% Rule Gameplan')
ON CONFLICT (sku) DO UPDATE SET
  category = EXCLUDED.category,
  emoji = EXCLUDED.emoji,
  kind = EXCLUDED.kind,
  checkout_path = EXCLUDED.checkout_path,
  active_on_bot = true;

-- === 003 miniapp public read ===
DROP POLICY IF EXISTS miniapp_read_shop_categories ON shop_categories;
CREATE POLICY miniapp_read_shop_categories ON shop_categories
  FOR SELECT TO anon
  USING (active = true);

DROP POLICY IF EXISTS miniapp_read_offers ON offers;
CREATE POLICY miniapp_read_offers ON offers
  FOR SELECT TO anon
  USING (active = true AND COALESCE(active_on_bot, true) = true);
