#!/usr/bin/env python3
"""Create LearnHouse users via the public API and verify each can log in.

Usage:
    python create-users.py                       # creates the default sample users
    python create-users.py user:email:pass ...   # create specific users

Login in LearnHouse is by EMAIL. Env overrides:
    LEARNHOUSE_API (default https://learn.azzamedu.com/api/v1)
    LEARNHOUSE_ADMIN_EMAIL / LEARNHOUSE_ADMIN_PASSWORD
"""

from __future__ import annotations

import os
import sys

import requests

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = os.environ.get("LEARNHOUSE_API", "https://learn.azzamedu.com/api/v1")
ADMIN_EMAIL = os.environ.get("LEARNHOUSE_ADMIN_EMAIL", "admin@hoa-homes.com")
ADMIN_PASSWORD = os.environ.get("LEARNHOUSE_ADMIN_PASSWORD", "AlphaElite-Prod-Learn-2026!")

DEFAULT_USERS = [
    ("azzam123", "azzam123@azzamedu.com", "azzam123"),
    ("azzam124", "azzam124@azzamedu.com", "azzam123"),
    ("azzam125", "azzam125@azzamedu.com", "azzam123"),
]


def parse_args() -> list[tuple[str, str, str]]:
    if len(sys.argv) > 1:
        out = []
        for a in sys.argv[1:]:
            parts = a.split(":")
            if len(parts) != 3:
                print(f"skip malformed '{a}' (want username:email:password)")
                continue
            out.append((parts[0], parts[1], parts[2]))
        return out
    return DEFAULT_USERS


def main() -> int:
    s = requests.Session()
    tok = s.post(
        f"{BASE}/auth/login",
        data={"username": ADMIN_EMAIL, "password": ADMIN_PASSWORD},
        timeout=30,
    ).json()["tokens"]["access_token"]
    H = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}

    users = parse_args()
    print(f"API: {BASE}")
    print(f"Creating {len(users)} user(s)\n")

    for username, email, pwd in users:
        r = s.post(
            f"{BASE}/users/",
            headers=H,
            json={"username": username, "email": email, "password": pwd},
            timeout=30,
        )
        ok = r.status_code in (200, 201)
        note = "created" if ok else f"FAILED ({r.status_code})"
        print(f"[{note}] {username}  <{email}>")
        if not ok:
            print("   ->", r.text[:300])
            continue
        # verify login with a clean session
        vs = requests.Session()
        lr = vs.post(f"{BASE}/auth/login", data={"username": email, "password": pwd}, timeout=30)
        print(f"   login check ({email}) -> {lr.status_code} {'OK' if lr.status_code == 200 else lr.text[:200]}")

    print("\nDONE. Login page: https://learn.azzamedu.com/login  (đăng nhập bằng EMAIL)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
