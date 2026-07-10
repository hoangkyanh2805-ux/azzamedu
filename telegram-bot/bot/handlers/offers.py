from telegram import Update
from telegram.ext import ContextTypes

from bot.catalog import category_by_id, load_categories, load_offers
from bot.keyboards.menus import (
    category_header,
    shop_categories_keyboard,
    shop_category_keyboard,
)
from bot.templates.loader import load_template


async def _send_shop_root(update: Update, config, *, edit: bool) -> None:
    text = load_template("shop")
    markup = shop_categories_keyboard(config)
    if edit and update.callback_query and update.callback_query.message:
        await update.callback_query.edit_message_text(text, reply_markup=markup)
    elif update.message:
        await update.message.reply_text(text, reply_markup=markup)
    elif update.callback_query and update.callback_query.message:
        await update.callback_query.message.reply_text(text, reply_markup=markup)


async def offers_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    config = context.bot_data["config"]
    if update.callback_query:
        await update.callback_query.answer()
    await _send_shop_root(update, config, edit=bool(update.callback_query))


async def offer_category_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if not query or not query.data:
        return
    await query.answer()

    config = context.bot_data["config"]
    category_id = query.data.removeprefix("offer:cat:")
    categories = load_categories(config)
    category = category_by_id(categories, category_id)
    if not category:
        await _send_shop_root(update, config, edit=True)
        return

    offers = load_offers(config)
    count = sum(1 for o in offers if o.category_id == category_id)
    header = category_header(category)
    text = load_template("shop_category").format(category=header, count=count)
    await query.edit_message_text(text, reply_markup=shop_category_keyboard(config, category_id))


async def offer_back_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if not query:
        return
    await query.answer()
    config = context.bot_data["config"]
    text = load_template("shop")
    await query.edit_message_text(text, reply_markup=shop_categories_keyboard(config))


async def offer_dwy_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.callback_query:
        return
    await update.callback_query.answer()
    text = load_template("offer_dwy")
    await update.callback_query.message.reply_text(text)
