from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

from bot.catalog import (
    ShopOffer,
    category_by_id,
    load_categories,
    load_offers,
    offers_in_category,
    paid_course_skus,
)
from bot.config import Config

MAIN_MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🛒 Shop"), KeyboardButton("🔑 My Access")],
        [KeyboardButton("💳 Payment"), KeyboardButton("🧭 Onboarding")],
        [KeyboardButton("💬 Support"), KeyboardButton("⚠️ Disclaimer")],
    ],
    resize_keyboard=True,
)


def _offer_price(config: Config, offer: ShopOffer) -> float | None:
    if offer.price_usd is not None:
        return offer.price_usd
    return config.pricing_usd.get(offer.sku)


def _checkout_url(config: Config, offer: ShopOffer) -> str:
    path = offer.checkout_path or config.checkout.get(offer.sku, "/")
    if path.startswith("http"):
        return path
    return f"{config.site.base_url.rstrip('/')}{path}"


def _price_label(config: Config, offer: ShopOffer) -> str:
    price = _offer_price(config, offer)
    base = f"{offer.emoji} {offer.name}".strip()
    if offer.kind == "gameplan":
        return f"{base} · Free"
    if offer.kind == "apply":
        return f"{base} · Apply"
    if price is not None:
        if offer.sku.endswith("-MON"):
            return f"{base} · ${price:.0f}/mo"
        if offer.sku.endswith("-YR"):
            return f"{base} · ${price:.0f}/yr"
        return f"{base} · ${price:.0f}"
    return base


def _offer_button(config: Config, offer: ShopOffer) -> InlineKeyboardButton:
    label = _price_label(config, offer)
    if offer.kind == "gameplan":
        return InlineKeyboardButton(label, url=config.gameplan_url())
    if offer.kind == "apply":
        path = offer.apply_path or "/"
        if path.startswith("http"):
            url = path
        else:
            url = f"{config.site.base_url.rstrip('/')}{path}"
        return InlineKeyboardButton(label, url=url)
    if offer.kind == "callback":
        return InlineKeyboardButton(label, callback_data=offer.callback_data or "offer:dwy")
    return InlineKeyboardButton(label, url=_checkout_url(config, offer))


def shop_categories_keyboard(config: Config) -> InlineKeyboardMarkup:
    categories = load_categories(config)
    rows = [
        [InlineKeyboardButton(cat.label, callback_data=f"offer:cat:{cat.id}")]
        for cat in categories
    ]
    webapp_row = _shop_webapp_row(config)
    if webapp_row:
        rows.insert(0, webapp_row)
    return InlineKeyboardMarkup(rows)


def _shop_webapp_row(config: Config) -> list[InlineKeyboardButton] | None:
    url = (getattr(config.site, "miniapp_shop_url", None) or "").strip()
    if not url:
        return None
    return [InlineKeyboardButton("📱 Mở Shop App", web_app=WebAppInfo(url=url))]


def shop_webapp_keyboard(config: Config) -> InlineKeyboardMarkup | None:
    """Single-row WebApp launcher when site.miniapp_shop_url is set."""
    row = _shop_webapp_row(config)
    return InlineKeyboardMarkup([row]) if row else None


def shop_category_keyboard(config: Config, category_id: str) -> InlineKeyboardMarkup:
    offers = offers_in_category(load_offers(config), category_id)
    rows = [[_offer_button(config, o)] for o in offers]
    rows.append([InlineKeyboardButton("« Danh mục", callback_data="offer:back")])
    return InlineKeyboardMarkup(rows)


def category_header(category) -> str:
    if not category:
        return "🛒 Sản phẩm"
    return category.label


def offers_keyboard(config: Config) -> InlineKeyboardMarkup:
    return shop_categories_keyboard(config)


def pay_sku_keyboard(config: Config | None = None) -> InlineKeyboardMarkup:
    skus = (
        paid_course_skus(load_offers(config))
        if config
        else ["AE-APP-001", "AE-VIP-MON", "AE-VIP-YR"]
    )
    rows = [[InlineKeyboardButton(sku, callback_data=f"pay:{sku}")] for sku in skus]
    rows.append([InlineKeyboardButton("Submit payment proof", callback_data="pay:submit")])
    return InlineKeyboardMarkup(rows)
