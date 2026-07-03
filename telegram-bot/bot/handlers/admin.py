from telegram import Update
from telegram.ext import ContextTypes

from bot.services.db import store
from bot.templates.loader import load_template


def _is_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    user = update.effective_user
    if not user:
        return False
    return user.id in context.bot_data["config"].admin_ids


async def admin_queue(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_admin(update, context) or not update.message:
        return

    pending = store.pending_queue()
    if not pending:
        await update.message.reply_text("No open queue items.")
        return

    lines = ["<b>Open queue</b>"]
    for q in pending[:20]:
        lines.append(f"{q.queue_code} — tg:{q.telegram_id} — {q.status} — {q.sku or '—'}")
    await update.message.reply_text("\n".join(lines), parse_mode="HTML")


async def admin_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_admin(update, context) or not update.message:
        return

    args = context.args or []
    if not args:
        await update.message.reply_text("Usage: /confirm AE-2026-0001")
        return

    code = args[0].upper()
    item = store.set_queue_status(code, "payment_confirmed")
    if not item:
        await update.message.reply_text("Queue code not found.")
        return
    await context.bot.send_message(
        chat_id=item.telegram_id,
        text=load_template("payment_confirmed"),
    )
    await update.message.reply_text(f"{code} → payment_confirmed. Create LearnHouse user (G4).")


async def admin_provisioned(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_admin(update, context) or not update.message:
        return

    args = context.args or []
    if not args:
        await update.message.reply_text("Usage: /provisioned AE-2026-0001")
        return

    code = args[0].upper()
    item = store.get_queue(code)
    if not item:
        await update.message.reply_text("Queue code not found.")
        return

    store.set_queue_status(code, "lh_active_apprentice")
    if item.sku and item.sku.startswith("AE-VIP"):
        store.set_queue_status(code, "tg_pending")

    config = context.bot_data["config"]
    msg = load_template("learnhouse_ready").format(learnhouse_url=config.site.learnhouse_url)
    await context.bot.send_message(chat_id=item.telegram_id, text=msg)
    await update.message.reply_text(f"{code} → LearnHouse instructions sent.")


async def admin_tgdone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_admin(update, context) or not update.message:
        return

    args = context.args or []
    if not args:
        await update.message.reply_text("Usage: /tgdone AE-2026-0001")
        return

    code = args[0].upper()
    item = store.get_queue(code)
    if not item:
        await update.message.reply_text("Queue code not found.")
        return

    store.set_queue_status(code, "access_active_vip")
    msg = load_template("vip_invite")
    await context.bot.send_message(chat_id=item.telegram_id, text=msg)
    await update.message.reply_text(f"{code} → VIP onboarding sent.")
