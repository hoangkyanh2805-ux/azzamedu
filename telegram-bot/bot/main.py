"""Alpha Elite Telegram Access Bot — entry point."""

import logging
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
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


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

    logger.info("Alpha Elite Access Bot starting (%s)", config.bot.mode)
    app.run_polling(allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    main()
