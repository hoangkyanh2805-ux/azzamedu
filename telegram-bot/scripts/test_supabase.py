"""Test Supabase connection and basic CRUD for the Telegram bot.

Usage:
  cd telegram-bot
  python scripts/test_supabase.py
  python scripts/test_supabase.py --cleanup   # remove test rows after success
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

load_dotenv(ROOT / ".env")

from bot.config import load_config  # noqa: E402
from bot.services.db import SupabaseStore, init_store, store  # noqa: E402


TEST_TELEGRAM_ID = 999999999
TEST_USERNAME = "supabase_test_user"


def _fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def _ok(message: str) -> None:
    print(f"OK  : {message}")


def test_raw_connection(supabase_url: str, service_key: str) -> SupabaseStore | None:
    print("\n=== 1) Raw API connection ===")
    try:
        backend = SupabaseStore(supabase_url=supabase_url, service_key=service_key)
        rows = backend._request("GET", "/offers?select=sku,name&limit=3").json()
        _ok(f"Connected. offers table readable ({len(rows)} sample rows).")
        for row in rows:
            print(f"    - {row.get('sku')}: {row.get('name')}")
        return backend
    except Exception as exc:
        _fail(f"Cannot reach Supabase REST API — {exc}")
        return None


def test_member_flow(backend: SupabaseStore, cleanup: bool) -> int:
    print("\n=== 2) Member upsert ===")
    try:
        member = backend.upsert_member(TEST_TELEGRAM_ID, TEST_USERNAME)
        _ok(f"Member upserted tg:{member.telegram_id} status={member.status} tier={member.tier}")
    except Exception as exc:
        return _fail(f"Member upsert failed — {exc}")

    print("\n=== 3) Email link ===")
    try:
        member = backend.link_email(TEST_TELEGRAM_ID, "test@alpha-elite.local")
        _ok(f"Email linked: {member.email}")
    except Exception as exc:
        return _fail(f"Email link failed — {exc}")

    print("\n=== 4) Queue insert ===")
    try:
        item = backend.add_queue(
            telegram_id=TEST_TELEGRAM_ID,
            request_type="connection_test",
            sku="AE-APP-001",
            email="test@alpha-elite.local",
            proof="supabase_connection_test",
        )
        _ok(f"Queue created: {item.queue_code}")
    except Exception as exc:
        return _fail(f"Queue insert failed — {exc}")

    print("\n=== 5) Queue status update ===")
    try:
        updated = backend.set_queue_status(item.queue_code, "payment_confirmed")
        if not updated:
            return _fail("Queue status update returned None")
        _ok(f"Queue status -> {updated.status}")
    except Exception as exc:
        return _fail(f"Queue status update failed — {exc}")

    print("\n=== 6) Pending queue read ===")
    try:
        pending = backend.pending_queue()
        _ok(f"Pending queue count: {len(pending)}")
    except Exception as exc:
        return _fail(f"Pending queue read failed — {exc}")

    if cleanup:
        print("\n=== 7) Cleanup test rows ===")
        try:
            backend._request(
                "DELETE",
                f"/provision_queue?telegram_id=eq.{TEST_TELEGRAM_ID}",
            )
            backend._request(
                "DELETE",
                f"/members?telegram_id=eq.{TEST_TELEGRAM_ID}",
            )
            _ok("Test rows removed.")
        except Exception as exc:
            return _fail(f"Cleanup failed — {exc}")
    else:
        print("\n=== 7) Cleanup skipped ===")
        print("    Run with --cleanup to delete test member/queue rows.")

    return 0


def test_bot_store_init(config) -> int:
    print("\n=== 8) Bot store init (same path as bot.main) ===")
    init_store(
        provider=config.database_provider,
        database_url=config.database_url,
        supabase_service_key=config.supabase_service_key,
    )
    backend_name = type(store.backend).__name__
    if backend_name != "SupabaseStore":
        return _fail(
            f"Expected SupabaseStore but got {backend_name}. "
            "Set database.provider=supabase in config.yaml and env keys in .env"
        )
    _ok(f"init_store() selected {backend_name}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Test Supabase wiring for Alpha Elite bot")
    parser.add_argument("--cleanup", action="store_true", help="Delete test rows after success")
    args = parser.parse_args()

    config = load_config()

    print("Alpha Elite — Supabase connection test")
    print(f"provider: {config.database_provider}")
    print(f"url set : {'yes' if config.database_url else 'no'}")
    print(f"key set : {'yes' if config.supabase_service_key else 'no'}")

    if not config.database_url:
        return _fail("DATABASE_URL missing in .env (use https://<project>.supabase.co)")
    if not config.supabase_service_key:
        return _fail("SUPABASE_SERVICE_KEY missing in .env (service_role key)")

    if not config.database_url.startswith("https://") or "supabase.co" not in config.database_url:
        return _fail(
            "DATABASE_URL must be Supabase project URL, e.g. https://abcd1234.supabase.co "
            "(not postgresql:// connection string)"
        )

    backend = test_raw_connection(config.database_url, config.supabase_service_key)
    if not backend:
        return 1

    code = test_member_flow(backend, cleanup=args.cleanup)
    if code != 0:
        return code

    code = test_bot_store_init(config)
    if code != 0:
        return code

    print("\nALL TESTS PASSED")
    print("Next: set database.provider: supabase in config.yaml and restart bot.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
