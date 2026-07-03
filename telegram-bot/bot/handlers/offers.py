from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.menus import offers_keyboard
from bot.templates.loader import load_template


async def offers_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    config = context.bot_data["config"]
    text = load_template("offers")
    markup = offers_keyboard(config)

    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text, reply_markup=markup)
        return

    if update.message:
        await update.message.reply_text(text, reply_markup=markup)


async def offer_dwy_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.callback_query:
        return
    await update.callback_query.answer()
    text = load_template("offer_dwy")
    await update.callback_query.message.reply_text(text)
