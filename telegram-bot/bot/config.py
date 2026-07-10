"""Load configuration from config.yaml and environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class BotConfig:
    token: str
    mode: str = "polling"
    webhook_path: str = "/webhook/secret"


@dataclass
class SiteConfig:
    base_url: str = "https://yourdomain.com"
    learnhouse_url: str = "https://learn.yourdomain.com"
    gameplan_path: str = "/gameplan"
    miniapp_shop_url: str = ""


@dataclass
class Config:
    bot: BotConfig
    admin_ids: list[int] = field(default_factory=list)
    site: SiteConfig = field(default_factory=SiteConfig)
    checkout: dict[str, str] = field(default_factory=dict)
    pricing_usd: dict[str, float] = field(default_factory=dict)
    payment: dict[str, Any] = field(default_factory=dict)
    shop: dict[str, Any] = field(default_factory=dict)
    catalog_source: str = "yaml"  # yaml | supabase
    database_provider: str = "memory"
    database_url: str = ""
    supabase_service_key: str = ""
    disclaimer_short: str = ""

    def checkout_url(self, sku: str) -> str:
        path = self.checkout.get(sku, "/")
        if path.startswith("http"):
            return path
        return f"{self.site.base_url.rstrip('/')}{path}"

    def gameplan_url(self) -> str:
        p = self.site.gameplan_path
        if p.startswith("http"):
            return p
        return f"{self.site.base_url.rstrip('/')}{p}"


def _expand_env(value: Any) -> Any:
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        return os.environ.get(value[2:-1], "")
    if isinstance(value, dict):
        return {k: _expand_env(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_env(v) for v in value]
    return value


def load_config(path: Path | None = None) -> Config:
    path = path or ROOT / "config.yaml"
    data: dict[str, Any] = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    data = _expand_env(data)

    token = os.environ.get("TELEGRAM_BOT_TOKEN") or data.get("bot", {}).get("token", "")
    admin_raw = data.get("admin", {}).get("telegram_ids", [])
    admin_ids = [int(x) for x in admin_raw]

    site_raw = data.get("site", {})
    payment_raw = data.get("payment", {}) or {}
    crypto_raw = payment_raw.get("crypto", {}) or {}

    site = SiteConfig(
        base_url=os.environ.get("SITE_BASE_URL") or site_raw.get("base_url", SiteConfig.base_url),
        learnhouse_url=os.environ.get("LEARNHOUSE_URL") or site_raw.get("learnhouse_url", SiteConfig.learnhouse_url),
        gameplan_path=site_raw.get("gameplan_url", "/gameplan"),
        miniapp_shop_url=os.environ.get("MINIAPP_SHOP_URL") or site_raw.get("miniapp_shop_url", ""),
    )

    payment = {
        "paypal_email": os.environ.get("PAYPAL_EMAIL") or payment_raw.get("paypal_email", ""),
        "crypto": {
            "network": os.environ.get("CRYPTO_NETWORK") or crypto_raw.get("network", "USDT TRC20"),
            "wallet": os.environ.get("CRYPTO_WALLET") or crypto_raw.get("wallet", ""),
        },
    }

    return Config(
        bot=BotConfig(
            token=token,
            mode=data.get("bot", {}).get("mode", "polling"),
            webhook_path=data.get("bot", {}).get("webhook_path", "/webhook/secret"),
        ),
        admin_ids=admin_ids,
        site=site,
        checkout=data.get("checkout", {}),
        pricing_usd={k: float(v) for k, v in data.get("pricing_usd", {}).items()},
        payment=payment,
        shop=data.get("shop", {}) or {},
        catalog_source=(data.get("catalog") or {}).get("source", "yaml"),
        database_provider=data.get("database", {}).get("provider", "memory"),
        database_url=os.environ.get("DATABASE_URL") or data.get("database", {}).get("url", ""),
        supabase_service_key=os.environ.get("SUPABASE_SERVICE_KEY", ""),
        disclaimer_short=(data.get("compliance", {}).get("disclaimer_short") or "").strip(),
    )
