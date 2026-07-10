#!/usr/bin/env python3
"""Copy full lesson content (incl. video embeds) from local LearnHouse to production."""

from __future__ import annotations

import os
import sys

import requests

LOCAL = os.environ.get("LEARNHOUSE_LOCAL_API", "http://localhost:8080/api/v1")
PROD = os.environ.get("LEARNHOUSE_API", "http://learn.azzamedu.com/api/v1")
EMAIL = os.environ.get("LEARNHOUSE_ADMIN_EMAIL", "admin@hoa-homes.com")
LOCAL_PWD = os.environ.get("LEARNHOUSE_LOCAL_PASSWORD", "AlphaElite-Local-2026!")
PROD_PWD = os.environ.get("LEARNHOUSE_ADMIN_PASSWORD", "AlphaElite-Prod-Learn-2026!")
COURSE_NAME = "Advanced trading course : The complete Smart Money Concepts"


def login(session: requests.Session, base: str, password: str) -> str:
    r = session.post(f"{base}/auth/login", data={"username": EMAIL, "password": password}, timeout=30)
    r.raise_for_status()
    return r.json()["tokens"]["access_token"]


def get_course_data(session: requests.Session, base: str, token: str) -> tuple[dict, list]:
    h = {"Authorization": f"Bearer {token}"}
    courses = session.get(f"{base}/courses/org_slug/alpha-elite/page/1/limit/50", headers=h, timeout=30).json()
    course = next(c for c in courses if c.get("name") == COURSE_NAME)
    chapters = session.get(
        f"{base}/chapters/course/{course['id']}/page/1/limit/50", headers=h, timeout=30
    ).json()
    return course, chapters


def activity_map(chapters: list) -> dict[str, dict]:
    m: dict[str, dict] = {}
    for ch in chapters:
        for a in ch.get("activities") or []:
            m[a["name"]] = a
    return m


def has_embed(content: dict | None) -> bool:
    if not isinstance(content, dict):
        return False
    return any(b.get("type") == "blockEmbed" for b in content.get("content", []))


def main() -> int:
    ls = requests.Session()
    ps = requests.Session()
    print("Login local + prod...")
    lt = login(ls, LOCAL, LOCAL_PWD)
    pt = login(ps, PROD, PROD_PWD)
    lh = {"Authorization": f"Bearer {lt}"}
    ph = {"Authorization": f"Bearer {pt}"}

    lc, lch = get_course_data(ls, LOCAL, lt)
    pc, pch = get_course_data(ps, PROD, pt)
    local_acts = activity_map(lch)
    prod_acts = activity_map(pch)

    # Course thumbnail + metadata if local has thumbnail
    if lc.get("thumbnail_image") and not pc.get("thumbnail_image"):
        form = {
            "name": pc["name"],
            "description": lc.get("description") or pc.get("description") or "",
            "about": lc.get("about") or pc.get("about") or "",
            "learnings": lc.get("learnings") or pc.get("learnings") or "",
            "tags": lc.get("tags") or pc.get("tags") or "",
            "thumbnail_type": "image",
        }
        r = ps.put(
            f"{PROD}/courses/{pc['course_uuid']}",
            data=form,
            headers=ph,
            timeout=60,
        )
        print(f"Course thumbnail sync: {r.status_code}")

    synced = skipped = missing = updated = 0
    for title, la in local_acts.items():
        pa = prod_acts.get(title)
        if not pa:
            print(f"  MISSING on prod: {title[:60]}")
            missing += 1
            continue
        lcontent = la.get("content")
        if not lcontent:
            skipped += 1
            continue
        # Sync if local has more content (video, longer text, or more blocks)
        pcontent = pa.get("content") or {}
        lblocks = lcontent.get("content", []) if isinstance(lcontent, dict) else []
        pblocks = pcontent.get("content", []) if isinstance(pcontent, dict) else []
        if len(lblocks) <= len(pblocks) and not has_embed(lcontent):
            skipped += 1
            continue
        r = ps.put(
            f"{PROD}/activities/{pa['activity_uuid']}",
            headers=ph,
            json={
                "name": title,
                "activity_type": pa.get("activity_type", "TYPE_DYNAMIC"),
                "activity_sub_type": pa.get("activity_sub_type", "SUBTYPE_DYNAMIC_PAGE"),
                "content": lcontent,
                "published": True,
            },
            timeout=30,
        )
        if r.status_code == 200:
            synced += 1
            tag = "video" if has_embed(lcontent) else "text"
            print(f"  ok [{tag}] {title[:55]}")
        else:
            print(f"  FAIL {title[:40]}: {r.status_code} {r.text[:120]}")

    print(f"\n=== Synced {synced} lessons, skipped {skipped} (prod already same), missing {missing} ===")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"API error: {exc}", file=sys.stderr)
        raise SystemExit(1)
