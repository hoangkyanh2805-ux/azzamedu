"""Validate production config before go-live."""

from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from bot.config import load_config  # noqa: E402

PLACEHOLDERS = {
    "yourdomain.com",
    "your-paypal@email.com",
    "TYourWalletAddressHere",
    "TYourWalletAddress",
    "hello@yourdomain.com",
}


def main() -> int:
    config = load_config()
    issues: list[str] = []

    if "yourdomain" in config.site.base_url:
        issues.append("SITE_BASE_URL still placeholder")
    if "yourdomain" in config.site.learnhouse_url:
        issues.append("LEARNHOUSE_URL still placeholder")

    paypal = config.payment.get("paypal_email", "")
    if not paypal or paypal in PLACEHOLDERS:
        issues.append("PAYPAL_EMAIL not set")

    wallet = (config.payment.get("crypto") or {}).get("wallet", "")
    if not wallet or wallet in PLACEHOLDERS:
        issues.append("CRYPTO_WALLET not set")

    print("Alpha Elite — config check\n")
    print(f"site.base_url     : {config.site.base_url}")
    print(f"site.learnhouse   : {config.site.learnhouse_url}")
    print(f"payment.paypal    : {paypal or '(empty)'}")
    print(f"payment.crypto    : {(config.payment.get('crypto') or {}).get('network')} / {wallet or '(empty)'}")
    print(f"database.provider : {config.database_provider}")

    if issues:
        print("\nWARN: fix before go-live:")
        for item in issues:
            print(f"  - {item}")
        return 1

    print("\nOK: production config looks ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
