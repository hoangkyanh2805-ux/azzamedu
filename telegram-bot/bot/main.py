"""Alpha Elite Telegram Access Bot — entry point."""

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from telegram.ext import Application

from bot.config import load_config
from bot.services.db import init_store, store

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
from bot.handlers import register_handlers
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,  # DEBUG to see all updates
)
logger = logging.getLogger(__name__)
logging.getLogger("telegram.ext.Application").setLevel(logging.INFO)  # Less verbose Application logs


def main() -> None:
    config = load_config()
    if not config.bot.token:
        logger.error("TELEGRAM_BOT_TOKEN not set. Copy config.example.yaml → config.yaml")
        sys.exit(1)

    init_store(
        provider=config.database_provider,
        database_url=config.database_url,
        supabase_service_key=config.supabase_service_key,
    )
    logger.info("Database backend: %s", type(store.backend).__name__)

    app = (
        Application.builder()
        .token(config.bot.token)
        .build()
    )
    app.bot_data["config"] = config
    register_handlers(app)

    logger.info(
        "Alpha Elite Access Bot starting (%s) — shop catalog v2, source=%s",
        config.bot.mode,
        config.catalog_source,
    )

    if config.bot.mode == "webhook":
        webhook_url = config.bot.webhook_url
        if not webhook_url:
            logger.error(
                "Webhook mode requires BOT_WEBHOOK_URL or bot.webhook_url in config.yaml"
            )
            sys.exit(1)
        port = int(os.environ.get("BOT_PORT", os.environ.get("PORT", "8443")))
        listen = os.environ.get("BOT_LISTEN", "0.0.0.0")
        logger.info(
            "Starting webhook listener on %s:%s %s",
            listen,
            port,
            config.bot.webhook_path,
        )
        app.run_webhook(
            listen=listen,
            port=port,
            url_path=config.bot.webhook_path,
            webhook_url=webhook_url,
            allowed_updates=["message", "callback_query"],
        )
    else:
        app.run_polling(allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    main()
