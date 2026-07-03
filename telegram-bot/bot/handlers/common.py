from telegram import Update
from telegram.ext import ContextTypes

from bot.services.db import store
from bot.templates.loader import load_template


async def onboard_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(load_template("onboarding"))


async def disclaimer_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(load_template("disclaimer"))


async def menu_router(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Route reply-keyboard labels to handlers."""
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()
    routes = {
        "📋 Offers": "offers",
        "🔑 My Access": "status",
        "💳 Payment": "pay",
        "🧭 Onboarding": "onboard",
        "💬 Support": "support",
        "⚠️ Disclaimer": "disclaimer",
    }
    action = routes.get(text)
    if action == "offers":
        from bot.handlers.offers import offers_handler

        await offers_handler(update, context)
    elif action == "status":
        from bot.handlers.status import status_handler

        await status_handler(update, context)
    elif action == "pay":
        from bot.handlers.pay import pay_handler

        await pay_handler(update, context)
    elif action == "onboard":
        await onboard_handler(update, context)
    elif action == "disclaimer":
        await disclaimer_handler(update, context)
