from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.menus import MAIN_MENU
from bot.templates.loader import load_template


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    from bot.services.db import store

    user = update.effective_user
    if not user or not update.message:
        return

    store.upsert_member(user.id, user.username)
    text = load_template("welcome")
    await update.message.reply_text(text, reply_markup=MAIN_MENU)
