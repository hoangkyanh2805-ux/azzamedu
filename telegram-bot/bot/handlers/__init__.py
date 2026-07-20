"""Register all bot handlers."""

import logging
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

logger = logging.getLogger(__name__)

from bot.handlers.admin import admin_confirm, admin_provisioned, admin_queue, admin_tgdone
from bot.handlers.common import menu_router
from bot.handlers.status import status_handler
from bot.handlers.offers import (
    offer_back_callback,
    offer_category_callback,
    offer_dwy_callback,
    offers_handler,
)
from bot.handlers.pay import (
    ASK_EMAIL,
    ASK_PROOF,
    pay_cancel,
    pay_email,
    pay_handler,
    pay_proof,
    pay_sku_callback,
)
from bot.handlers.start import start_handler
from bot.handlers.support import ASK_SUPPORT, support_cancel, support_handler, support_message


def register_handlers(app: Application) -> None:
    pay_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(pay_sku_callback, pattern=r"^pay:")],
        states={
            ASK_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, pay_email)],
            ASK_PROOF: [MessageHandler(filters.TEXT & ~filters.COMMAND, pay_proof)],
        },
        fallbacks=[CommandHandler("cancel", pay_cancel)],
        name="pay_flow",
        persistent=False,
    )

    support_conv = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex(r"^💬 Support$"), support_handler)],
        states={
            ASK_SUPPORT: [MessageHandler(filters.TEXT & ~filters.COMMAND, support_message)],
        },
        fallbacks=[CommandHandler("cancel", support_cancel)],
        name="support_flow",
        persistent=False,
    )

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("menu", offers_handler))
    app.add_handler(CommandHandler("offers", offers_handler))
    app.add_handler(CommandHandler("shop", offers_handler))
    app.add_handler(CommandHandler("status", status_handler))
    app.add_handler(CommandHandler("queue", admin_queue))
    app.add_handler(CommandHandler("confirm", admin_confirm))
    app.add_handler(CommandHandler("provisioned", admin_provisioned))
    app.add_handler(CommandHandler("tgdone", admin_tgdone))

    app.add_handler(pay_conv)
    app.add_handler(support_conv)
    app.add_handler(CallbackQueryHandler(offer_dwy_callback, pattern=r"^offer:dwy$"))
    app.add_handler(CallbackQueryHandler(offer_back_callback, pattern=r"^offer:back$"))
    app.add_handler(CallbackQueryHandler(offer_category_callback, pattern=r"^offer:cat:"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_router))
