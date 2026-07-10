-- Migration 003: Public read-only catalog for Telegram Mini App (anon key)
-- Run after 002_shop_catalog.sql
-- Mini App uses SUPABASE_ANON_KEY in browser — NOT service_role.

CREATE POLICY miniapp_read_shop_categories ON shop_categories
  FOR SELECT TO anon
  USING (active = true);

CREATE POLICY miniapp_read_offers ON offers
  FOR SELECT TO anon
  USING (active = true AND COALESCE(active_on_bot, true) = true);
