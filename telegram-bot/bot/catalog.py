"""Shop catalog — Supabase (primary) or config.yaml (fallback)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot.config import Config


@dataclass(frozen=True)
class ShopCategory:
    id: str
    label: str


@dataclass(frozen=True)
class ShopOffer:
    sku: str
    category_id: str
    name: str
    emoji: str = ""
    kind: str = "checkout"  # checkout | gameplan | apply | callback
    callback_data: str = ""
    apply_path: str = ""
    price_usd: float | None = None
    checkout_path: str = ""


DEFAULT_CATEGORIES: list[ShopCategory] = [
    ShopCategory("khoa_hoc", "📚 Khóa học"),
    ShopCategory("membership", "🏛 Membership"),
    ShopCategory("free", "🎁 Free"),
    ShopCategory("services", "🔧 Services"),
]

DEFAULT_OFFERS: list[ShopOffer] = [
    ShopOffer("AE-APP-001", "khoa_hoc", "Apprentice Operating Course", "📘"),
    ShopOffer("AE-VIP-MON", "membership", "VIP Private Desk — Monthly", "🏛"),
    ShopOffer("AE-VIP-YR", "membership", "VIP Private Desk — Annual", "🏛"),
    ShopOffer("AE-QNT-001", "membership", "Quant Desk", "📊", kind="apply", apply_path="/quant-desk"),
    ShopOffer("AE-GP-000", "free", "2% Rule Gameplan", "🎁", kind="gameplan", checkout_path="/gameplan"),
    ShopOffer(
        "AE-DWY-001",
        "services",
        "DWY Bot & Broker Setup",
        "🔧",
        kind="callback",
        callback_data="offer:dwy",
    ),
]


def _use_supabase_catalog(config: Config) -> bool:
    if config.catalog_source != "supabase":
        return False
    from bot.services.db import store

    return type(store.backend).__name__ == "SupabaseStore"


def _row_to_offer(row: dict) -> ShopOffer:
    name = row.get("display_name") or row.get("name") or row["sku"]
    price = row.get("price_usd")
    return ShopOffer(
        sku=row["sku"],
        category_id=row.get("category") or "general",
        name=name,
        emoji=row.get("emoji") or "",
        kind=row.get("kind") or "checkout",
        callback_data=row.get("callback_data") or "",
        apply_path=row.get("apply_path") or "",
        price_usd=float(price) if price is not None else None,
        checkout_path=row.get("checkout_path") or "",
    )


def load_categories(config: Config) -> list[ShopCategory]:
    if _use_supabase_catalog(config):
        from bot.services.db import store

        try:
            rows = store.list_shop_categories()
            if rows:
                return [ShopCategory(id=r["id"], label=r["label"]) for r in rows]
        except Exception:
            pass

    raw = config.shop.get("categories") or []
    if raw:
        return [ShopCategory(id=c["id"], label=c["label"]) for c in raw]
    return list(DEFAULT_CATEGORIES)


def load_offers(config: Config) -> list[ShopOffer]:
    if _use_supabase_catalog(config):
        from bot.services.db import store

        try:
            rows = store.list_shop_offers(active_only=True)
            if rows:
                return [_row_to_offer(r) for r in rows]
        except Exception:
            pass

    raw = config.shop.get("offers") or []
    if raw:
        offers: list[ShopOffer] = []
        for o in raw:
            price = config.pricing_usd.get(o["sku"])
            offers.append(
                ShopOffer(
                    sku=o["sku"],
                    category_id=o["category"],
                    name=o["name"],
                    emoji=o.get("emoji", ""),
                    kind=o.get("kind", "checkout"),
                    callback_data=o.get("callback_data", ""),
                    apply_path=o.get("apply_path", ""),
                    price_usd=float(price) if price is not None else None,
                    checkout_path=config.checkout.get(o["sku"], ""),
                )
            )
        return offers

    offers = []
    for o in DEFAULT_OFFERS:
        price = config.pricing_usd.get(o.sku)
        offers.append(
            ShopOffer(
                sku=o.sku,
                category_id=o.category_id,
                name=o.name,
                emoji=o.emoji,
                kind=o.kind,
                callback_data=o.callback_data,
                apply_path=o.apply_path,
                price_usd=float(price) if price is not None else o.price_usd,
                checkout_path=config.checkout.get(o.sku, o.checkout_path),
            )
        )
    return offers


def offers_in_category(offers: list[ShopOffer], category_id: str) -> list[ShopOffer]:
    return [o for o in offers if o.category_id == category_id]


def category_by_id(categories: list[ShopCategory], category_id: str) -> ShopCategory | None:
    return next((c for c in categories if c.id == category_id), None)


def paid_course_skus(offers: list[ShopOffer]) -> list[str]:
    ids = {"khoa_hoc", "membership"}
    return [o.sku for o in offers if o.category_id in ids and o.kind == "checkout"]
