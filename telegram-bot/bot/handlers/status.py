from telegram import Update
from telegram.ext import ContextTypes

from bot.constants import STATUS_LABELS, TIER_LABELS
from bot.services.db import store


async def status_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not update.message:
        return

    m = store.upsert_member(user.id, user.username)
    tier = TIER_LABELS.get(m.tier, m.tier)
    status = STATUS_LABELS.get(m.status, m.status)

    lines = [
        f"<b>Your access</b>",
        f"Tier: {tier}",
        f"Status: {status}",
    ]
    if m.email:
        lines.append(f"Email: {m.email}")
    if m.status in ("lh_active_apprentice", "lh_active_vip", "access_active_vip"):
        config = context.bot_data["config"]
        lines.append(f"\nLearnHouse: {config.site.learnhouse_url}")
    if m.status == "tg_pending":
        lines.append("\nVIP Telegram access is pending admin approval.")
    if m.status == "access_active_vip":
        lines.append("\nCheck Telegram for your VIP group invite.")

    await update.message.reply_text("\n".join(lines), parse_mode="HTML")
