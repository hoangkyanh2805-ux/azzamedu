from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.keyboards.menus import pay_sku_keyboard
from bot.services.db import store
from bot.services.notify import notify_admins
from bot.templates.loader import load_template

ASK_EMAIL, ASK_PROOF = range(2)


def _payment_text(config) -> str:
    payment = config.payment
    crypto = payment.get("crypto", {})
    return load_template("payment_instructions").format(
        paypal_email=payment.get("paypal_email", "hello@yourdomain.com"),
        crypto_network=crypto.get("network", "USDT TRC20"),
        crypto_wallet=crypto.get("wallet", "TYourWalletAddress"),
    )


async def pay_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        config = context.bot_data["config"]
        await update.message.reply_text(
            _payment_text(config),
            reply_markup=pay_sku_keyboard(config),
        )


async def pay_sku_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    if not query or not query.data:
        return ConversationHandler.END

    await query.answer()
    data = query.data
    if data == "pay:submit":
        await query.message.reply_text(
            "Reply with your <b>checkout email</b> (same as WooCommerce or PayPal).",
            parse_mode="HTML",
        )
        return ASK_EMAIL

    sku = data.split(":", 1)[1]
    context.user_data["pay_sku"] = sku
    config = context.bot_data["config"]
    price = config.pricing_usd.get(sku, "—")
    await query.message.reply_text(
        f"Selected: <b>{sku}</b> (${price} draft).\n"
        "Complete payment via PayPal or crypto (see Payment menu), then tap "
        "<b>Submit payment proof</b>.",
        parse_mode="HTML",
    )
    return ConversationHandler.END


async def pay_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if not update.message or not update.message.text:
        return ASK_EMAIL

    email = update.message.text.strip()
    if "@" not in email:
        await update.message.reply_text("Please send a valid email.")
        return ASK_EMAIL

    context.user_data["pay_email"] = email
    store.link_email(update.effective_user.id, email)
    await update.message.reply_text(
        "Now send your <b>payment proof</b> — screenshot, transaction ID, or short note.",
        parse_mode="HTML",
    )
    return ASK_PROOF


async def pay_proof(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    if not user or not update.message:
        return ConversationHandler.END

    proof = update.message.text or "(attachment)"
    sku = context.user_data.get("pay_sku")
    email = context.user_data.get("pay_email")

    item = store.add_queue(
        telegram_id=user.id,
        request_type="payment_proof",
        sku=sku,
        email=email,
        proof=proof[:500],
    )

    await update.message.reply_text(load_template("payment_submitted").format(code=item.queue_code))

    admin_text = (
        f"<b>New payment review</b>\n"
        f"Code: {item.queue_code}\n"
        f"User: @{user.username or user.id} ({user.id})\n"
        f"SKU: {sku or '—'}\n"
        f"Email: {email or '—'}\n"
        f"Proof: {proof[:200]}"
    )
    await notify_admins(context.bot, context.bot_data["config"], admin_text)
    context.user_data.clear()
    return ConversationHandler.END


async def pay_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.clear()
    if update.message:
        await update.message.reply_text("Payment submission cancelled.")
    return ConversationHandler.END
