from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from bot.config import Config

MAIN_MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📋 Offers"), KeyboardButton("🔑 My Access")],
        [KeyboardButton("💳 Payment"), KeyboardButton("🧭 Onboarding")],
        [KeyboardButton("💬 Support"), KeyboardButton("⚠️ Disclaimer")],
    ],
    resize_keyboard=True,
)


def offers_keyboard(config: Config) -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton("🎁 Free Gameplan", url=config.gameplan_url())],
        [
            InlineKeyboardButton(
                "📘 Apprentice",
                url=config.checkout_url("AE-APP-001"),
            )
        ],
        [
            InlineKeyboardButton(
                "🏛 VIP Monthly",
                url=config.checkout_url("AE-VIP-MON"),
            ),
            InlineKeyboardButton(
                "🏛 VIP Annual",
                url=config.checkout_url("AE-VIP-YR"),
            ),
        ],
        [
            InlineKeyboardButton(
                "📊 Quant Desk",
                url=f"{config.site.base_url.rstrip('/')}/quant-desk",
            )
        ],
        [
            InlineKeyboardButton(
                "🔧 DWY Setup (VIP bump)",
                callback_data="offer:dwy",
            )
        ],
    ]
    return InlineKeyboardMarkup(rows)


def pay_sku_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Apprentice — AE-APP-001", callback_data="pay:AE-APP-001")],
            [InlineKeyboardButton("VIP Monthly — AE-VIP-MON", callback_data="pay:AE-VIP-MON")],
            [InlineKeyboardButton("VIP Annual — AE-VIP-YR", callback_data="pay:AE-VIP-YR")],
            [InlineKeyboardButton("Submit payment proof", callback_data="pay:submit")],
        ]
    )
