"""WooCommerce webhook scaffold (P2)."""

from __future__ import annotations

import hashlib
import hmac
from typing import Any

from bot.services.db import store
from bot.services.notify import notify_admins


def verify_woocommerce_signature(raw_body: bytes, signature: str, secret: str) -> bool:
    digest = hmac.new(secret.encode("utf-8"), raw_body, hashlib.sha256).digest()
    expected = digest.hex()
    return hmac.compare_digest(expected, signature or "")


async def handle_completed_order(payload: dict[str, Any], bot, config) -> str:
    """Create queue item from WooCommerce order.completed payload."""
    order_id = str(payload.get("id", ""))
    billing = payload.get("billing", {}) or {}
    email = (billing.get("email") or "").strip().lower()

    line_items = payload.get("line_items", []) or []
    sku = None
    if line_items:
        sku = line_items[0].get("sku")

    # telegram id must be attached by thank-you deep link flow in next phase
    telegram_id = 0
    for meta in payload.get("meta_data", []) or []:
        if str(meta.get("key")) == "_ae_telegram_id":
            try:
                telegram_id = int(meta.get("value"))
            except (TypeError, ValueError):
                telegram_id = 0
            break

    if not telegram_id:
        return "missing_telegram_id"

    store.upsert_member(telegram_id=telegram_id)
    item = store.add_queue(
        telegram_id=telegram_id,
        request_type="wc_order",
        sku=sku,
        email=email,
        proof=f"wc_order_id:{order_id}",
    )
    store.set_queue_status(item.queue_code, "payment_confirmed")

    admin_text = (
        "<b>WooCommerce payment confirmed</b>\n"
        f"Code: {item.queue_code}\n"
        f"Order: {order_id}\n"
        f"Telegram: {telegram_id}\n"
        f"SKU: {sku or '—'}\n"
        f"Email: {email or '—'}"
    )
    await notify_admins(bot, config, admin_text)
    return item.queue_code
