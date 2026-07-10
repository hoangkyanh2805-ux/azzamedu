#!/usr/bin/env python3
"""Apply shop catalog SQL migrations to Supabase (002 + 003).

Requires in .env:
  DATABASE_URL=https://<project>.supabase.co
  SUPABASE_DB_PASSWORD=<database password from project creation>

Usage:
  cd telegram-bot
  python scripts/apply-supabase-migrations.py
  python scripts/apply-supabase-migrations.py --dry-run
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
MIGRATIONS = [
    ROOT / "database/migrations/002_shop_catalog.sql",
    ROOT / "database/migrations/003_miniapp_public_read.sql",
]


def _project_ref(database_url: str) -> str:
    m = re.search(r"https://([^.]+)\.supabase\.co", database_url.strip())
    if not m:
        raise ValueError("DATABASE_URL must be https://<ref>.supabase.co")
    return m.group(1)


def _connect(database_url: str, password: str):
    import psycopg2

    ref = _project_ref(database_url)
    hosts = [
        f"db.{ref}.supabase.co",
        "aws-0-ap-southeast-1.pooler.supabase.com",
        "aws-0-ap-northeast-1.pooler.supabase.com",
    ]
    last_err: Exception | None = None
    for host in hosts:
        if host.startswith("db."):
            conninfo = (
                f"host={host} port=5432 dbname=postgres user=postgres "
                f"password={password} sslmode=require connect_timeout=15"
            )
        else:
            conninfo = (
                f"host={host} port=6543 dbname=postgres user=postgres.{ref} "
                f"password={password} sslmode=require connect_timeout=15"
            )
        try:
            return psycopg2.connect(conninfo)
        except Exception as exc:
            last_err = exc
    raise last_err or RuntimeError("Could not connect to Supabase Postgres")


def _run_sql(conn, sql: str) -> None:
    import psycopg2

    statements = [s.strip() for s in sql.split(";") if s.strip() and not s.strip().startswith("--")]
    with conn.cursor() as cur:
        for stmt in statements:
            try:
                cur.execute(stmt)
            except psycopg2.Error as exc:
                msg = str(exc).lower()
                if "already exists" in msg or "duplicate" in msg:
                    conn.rollback()
                    continue
                raise
    conn.commit()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    database_url = os.environ.get("DATABASE_URL", "").strip()
    password = os.environ.get("SUPABASE_DB_PASSWORD", "").strip()

    if not database_url:
        print("FAIL: DATABASE_URL missing in .env")
        return 1
    if not password:
        print("FAIL: SUPABASE_DB_PASSWORD missing in .env")
        print("  Supabase Dashboard -> Project Settings -> Database -> Database password")
        print("  Add to .env: SUPABASE_DB_PASSWORD=your_db_password")
        print("  Or paste database/migrations/RUN_IN_SUPABASE_SQL_EDITOR.sql in SQL Editor")
        return 1

    sql_parts = []
    for path in MIGRATIONS:
        if not path.exists():
            print(f"FAIL: missing {path}")
            return 1
        sql_parts.append(path.read_text(encoding="utf-8"))
    combined = "\n\n".join(sql_parts)

    if args.dry_run:
        print("DRY RUN — would apply:")
        for path in MIGRATIONS:
            print(f"  - {path.name}")
        return 0

    print(f"Connecting to Supabase project {_project_ref(database_url)}...")
    conn = _connect(database_url, password)
    try:
        for path in MIGRATIONS:
            print(f"Applying {path.name}...")
            _run_sql(conn, path.read_text(encoding="utf-8"))
        print("OK: migrations applied")
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
