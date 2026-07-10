#!/usr/bin/env python3
"""Sync WooCommerce products → Supabase offers (Model B).

Usage:
  cd telegram-bot
  python scripts/sync-woo-catalog.py
  python scripts/sync-woo-catalog.py --dry-run
  python scripts/sync-woo-catalog.py --write-yaml   # optional dev snapshot

Requires .env:
  DATABASE_URL, SUPABASE_SERVICE_KEY
  WC_API_URL, WC_CONSUMER_KEY, WC_CONSUMER_SECRET
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

load_dotenv(ROOT / ".env")

from bot.config import load_config  # noqa: E402
from bot.services.db import SupabaseStore  # noqa: E402


def _load_rules() -> dict[str, Any]:
    path = ROOT / "sync-rules.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _woo_get_all_products(api_url: str, key: str, secret: str, sku_prefix: str) -> list[dict]:
    base = api_url.rstrip("/")
    products: list[dict] = []
    page = 1
    while True:
        resp = httpx.get(
            f"{base}/products",
            auth=(key, secret),
            params={"per_page": 100, "page": page, "status": "any"},
            timeout=30,
        )
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        for p in batch:
            sku = (p.get("sku") or "").strip()
            if sku and sku.startswith(sku_prefix):
                products.append(p)
        if len(batch) < 100:
            break
        page += 1
    return products


def _cart_path(rules: dict, sku: str) -> str:
    tpl = rules.get("woo", {}).get("cart_path_template", "/checkout/?add-to-cart={sku}")
    return tpl.format(sku=sku)


def _build_woo_offer(product: dict, rules: dict, existing: dict | None) -> dict:
    sku = product["sku"].strip()
    rule = rules.get("sku_rules", {}).get(sku, {})
    price = product.get("regular_price") or product.get("price") or ""
    price_usd = float(price) if price not in ("", None) else None
    published = product.get("status") == "publish"

    row = {
        "sku": sku,
        "name": product.get("name") or sku,
        "display_name": (existing or {}).get("display_name"),
        "wc_product_id": product.get("id"),
        "price_usd": price_usd,
        "checkout_path": _cart_path(rules, sku),
        "tier": rule.get("tier", (existing or {}).get("tier", "apprentice")),
        "category": rule.get("category", (existing or {}).get("category", "general")),
        "emoji": rule.get("emoji", (existing or {}).get("emoji") or ""),
        "kind": rule.get("kind", (existing or {}).get("kind") or "checkout"),
        "callback_data": rule.get("callback_data", (existing or {}).get("callback_data")),
        "apply_path": rule.get("apply_path", (existing or {}).get("apply_path")),
        "sort_order": rule.get("sort_order", (existing or {}).get("sort_order") or 0),
        "active": published,
        "active_on_bot": (existing or {}).get("active_on_bot", True),
        "synced_at": datetime.now(timezone.utc).isoformat(),
    }
    return row


def _build_static_offer(static: dict) -> dict:
    return {
        "sku": static["sku"],
        "name": static["name"],
        "display_name": static.get("display_name"),
        "wc_product_id": None,
        "price_usd": static.get("price_usd"),
        "checkout_path": static.get("checkout_path", "/"),
        "tier": static.get("tier", "free"),
        "category": static["category"],
        "emoji": static.get("emoji", ""),
        "kind": static.get("kind", "checkout"),
        "callback_data": static.get("callback_data"),
        "apply_path": static.get("apply_path"),
        "sort_order": static.get("sort_order", 0),
        "active": static.get("active", True),
        "active_on_bot": static.get("active_on_bot", True),
        "synced_at": datetime.now(timezone.utc).isoformat(),
    }


def _optional_yaml_snapshot(offers: list[dict], categories: list[dict]) -> None:
    out = ROOT / "config.catalog.snapshot.yaml"
    payload = {
        "shop": {
            "categories": [{"id": c["id"], "label": c["label"]} for c in categories],
            "offers": [
                {
                    "sku": o["sku"],
                    "category": o["category"],
                    "name": o.get("display_name") or o["name"],
                    "emoji": o.get("emoji") or "",
                    "kind": o.get("kind") or "checkout",
                }
                for o in offers
                if o.get("active_on_bot", True)
            ],
        },
        "pricing_usd": {
            o["sku"]: o["price_usd"]
            for o in offers
            if o.get("price_usd") is not None
        },
    }
    with open(out, "w", encoding="utf-8") as f:
        yaml.safe_dump(payload, f, allow_unicode=True, sort_keys=False)
    print(f"Wrote snapshot: {out}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync WooCommerce catalog to Supabase")
    parser.add_argument("--dry-run", action="store_true", help="Print changes only")
    parser.add_argument("--write-yaml", action="store_true", help="Write config.catalog.snapshot.yaml")
    args = parser.parse_args()

    import os

    config = load_config()
    rules = _load_rules()
    sku_prefix = rules.get("woo", {}).get("sku_prefix", "AE-")

    db_url = config.database_url or os.environ.get("DATABASE_URL", "")
    service_key = config.supabase_service_key or os.environ.get("SUPABASE_SERVICE_KEY", "")
    wc_url = os.environ.get("WC_API_URL", "").strip()
    wc_key = os.environ.get("WC_CONSUMER_KEY", "").strip()
    wc_secret = os.environ.get("WC_CONSUMER_SECRET", "").strip()

    if not db_url or not service_key:
        print("FAIL: DATABASE_URL and SUPABASE_SERVICE_KEY required")
        return 1
    if not wc_url or not wc_key or not wc_secret:
        print("FAIL: WC_API_URL, WC_CONSUMER_KEY, WC_CONSUMER_SECRET required in .env")
        return 1

    store = SupabaseStore(supabase_url=db_url, service_key=service_key)

    print("=== Sync shop_categories ===")
    categories = rules.get("categories", [])
    for cat in categories:
        print(f"  {cat['id']}: {cat['label']}")
        if not args.dry_run:
            store.upsert_shop_category(cat)

    print("\n=== Fetch WooCommerce products ===")
    try:
        wc_products = _woo_get_all_products(wc_url, wc_key, wc_secret, sku_prefix)
    except httpx.HTTPError as exc:
        print(f"FAIL: Woo API — {exc}")
        return 1
    print(f"  Found {len(wc_products)} products with SKU prefix {sku_prefix!r}")

    existing_rows = {r["sku"]: r for r in store.list_shop_offers(active_only=False)}
    merged: list[dict] = []

    print("\n=== Merge Woo → offers ===")
    for product in wc_products:
        sku = product.get("sku", "").strip()
        if not sku:
            continue
        row = _build_woo_offer(product, rules, existing_rows.get(sku))
        merged.append(row)
        print(f"  {sku}: ${row.get('price_usd')} | {row['name'][:40]} | active={row['active']}")

    for static in rules.get("static_offers", []):
        row = _build_static_offer(static)
        merged.append(row)
        print(f"  {row['sku']}: static | {row['name']}")

    if args.dry_run:
        print("\nDRY RUN — no writes")
        return 0

    print("\n=== Upsert Supabase offers ===")
    for row in merged:
        store.upsert_offer(row)

    if args.write_yaml:
        _optional_yaml_snapshot(merged, categories)

    print("\nDONE — restart bot or wait for next /menu (reads Supabase)")
    print("Set catalog_source: supabase in config.yaml if not already.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
