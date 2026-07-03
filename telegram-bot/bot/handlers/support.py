from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.services.db import store
from bot.services.notify import notify_admins
from bot.templates.loader import load_template

ASK_SUPPORT = 0


async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message:
        await update.message.reply_text(load_template("support_prompt"))
    return ASK_SUPPORT


async def support_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    if not user or not update.message or not update.message.text:
        return ASK_SUPPORT

    ticket = store.add_ticket(user.id, update.message.text.strip())
    await update.message.reply_text(
        f"Ticket <b>{ticket.ticket_code}</b> received. We reply within 24–48h (business days).",
        parse_mode="HTML",
    )

    await notify_admins(
        context.bot,
        context.bot_data["config"],
        f"<b>Support {ticket.ticket_code}</b>\n@{user.username or user.id}: {update.message.text[:300]}",
    )
    return ConversationHandler.END


async def support_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message:
        await update.message.reply_text("Support request cancelled.")
    return ConversationHandler.END
