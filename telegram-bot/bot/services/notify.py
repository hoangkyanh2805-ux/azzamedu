"""Admin notifications."""

from telegram import Bot

from bot.config import Config


async def notify_admins(bot: Bot, config: Config, text: str) -> None:
    for admin_id in config.admin_ids:
        try:
            await bot.send_message(chat_id=admin_id, text=text, parse_mode="HTML")
        except Exception:
            pass  # log in production
