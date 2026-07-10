#!/usr/bin/env python3
"""Seed shop_categories + enrich offers from sync-rules.yaml (no Woo required).

Run after apply-supabase-migrations.py.

Usage:
  cd telegram-bot
  python scripts/seed-shop-catalog.py
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

load_dotenv(ROOT / ".env")

from bot.config import load_config  # noqa: E402
from bot.services.db import SupabaseStore  # noqa: E402


def main() -> int:
    config = load_config()
    rules_path = ROOT / "sync-rules.yaml"
    rules = yaml.safe_load(rules_path.read_text(encoding="utf-8")) or {}

    if not config.database_url or not config.supabase_service_key:
        print("FAIL: DATABASE_URL and SUPABASE_SERVICE_KEY required")
        return 1

    store = SupabaseStore(config.database_url, config.supabase_service_key)

    print("=== shop_categories ===")
    for cat in rules.get("categories", []):
        store.upsert_shop_category(cat)
        print(f"  {cat['id']}: {cat['label']}")

    sku_rules = rules.get("sku_rules", {})
    now = datetime.now(timezone.utc).isoformat()

    print("\n=== enrich offers from sku_rules ===")
    rows = store.list_shop_offers(active_only=False)
    for row in rows:
        sku = row["sku"]
        rule = sku_rules.get(sku, {})
        payload = {
            "sku": sku,
            "name": row.get("name") or sku,
            "tier": row.get("tier") or rule.get("tier", "free"),
            "checkout_path": row.get("checkout_path") or "/",
            "category": rule.get("category") or row.get("category") or "general",
            "display_name": row.get("display_name") or row.get("name"),
            "emoji": rule.get("emoji", row.get("emoji") or ""),
            "kind": rule.get("kind", row.get("kind") or "checkout"),
            "callback_data": rule.get("callback_data"),
            "apply_path": rule.get("apply_path"),
            "sort_order": rule.get("sort_order", row.get("sort_order") or 0),
            "active": row.get("active", True),
            "active_on_bot": row.get("active_on_bot", True),
            "price_usd": row.get("price_usd"),
            "synced_at": now,
        }
        store.upsert_offer(payload)
        print(f"  {sku} → {payload['category']} | {payload.get('kind')}")

    print("\n=== static offers ===")
    for static in rules.get("static_offers", []):
        payload = {
            "sku": static["sku"],
            "name": static["name"],
            "display_name": static.get("display_name") or static["name"],
            "tier": static.get("tier", "free"),
            "category": static["category"],
            "emoji": static.get("emoji", ""),
            "kind": static.get("kind", "checkout"),
            "callback_data": static.get("callback_data"),
            "apply_path": static.get("apply_path"),
            "checkout_path": static.get("checkout_path", "/"),
            "price_usd": static.get("price_usd"),
            "sort_order": static.get("sort_order", 0),
            "active": static.get("active", True),
            "active_on_bot": static.get("active_on_bot", True),
            "synced_at": now,
        }
        store.upsert_offer(payload)
        print(f"  {static['sku']}: static")

    print("\nDONE — restart bot; Mini App can read catalog with anon key")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
