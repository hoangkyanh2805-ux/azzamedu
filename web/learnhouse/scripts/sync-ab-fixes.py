#!/usr/bin/env python3
"""Fix A: S16 merge by index. Fix B: force-sync quiz lessons from local to prod."""

from __future__ import annotations

import os
import sys

import requests

LOCAL = os.environ.get("LEARNHOUSE_LOCAL_API", "http://localhost:8080/api/v1")
PROD = os.environ.get("LEARNHOUSE_API", "http://learn.hoa-homes.com/api/v1")
EMAIL = os.environ.get("LEARNHOUSE_ADMIN_EMAIL", "admin@hoa-homes.com")
LOCAL_PWD = os.environ.get("LEARNHOUSE_LOCAL_PASSWORD", "AlphaElite-Local-2026!")
PROD_PWD = os.environ.get("LEARNHOUSE_ADMIN_PASSWORD", "AlphaElite-Prod-Learn-2026!")
COURSE_NAME = "Advanced trading course : The complete Smart Money Concepts"

# B: force overwrite these lesson titles (local quiz content wins)
FORCE_SYNC_TITLES = {
    "15 Bonus Basic Quiz",
    "15 Bonus Advanced Quiz",
    "Practice carefully after course - Mindset is key to create change",
}


def login(session: requests.Session, base: str, password: str) -> str:
    r = session.post(f"{base}/auth/login", data={"username": EMAIL, "password": password}, timeout=30)
    r.raise_for_status()
    return r.json()["tokens"]["access_token"]


def get_chapters(session: requests.Session, base: str, token: str) -> list:
    h = {"Authorization": f"Bearer {token}"}
    courses = session.get(f"{base}/courses/org_slug/alpha-elite/page/1/limit/50", headers=h, timeout=30).json()
    course = next(c for c in courses if c.get("name") == COURSE_NAME)
    return session.get(
        f"{base}/chapters/course/{course['id']}/page/1/limit/50", headers=h, timeout=30
    ).json()


def find_s16(chapters: list, prefer_dash: bool) -> dict | None:
    for ch in chapters:
        name = ch.get("name", "")
        if "S16" not in name or "Trading tips" not in name:
            continue
        if prefer_dash and "S16 -" in name:
            return ch
        if not prefer_dash and name.startswith("S16:"):
            return ch
    # fallback: any S16 tips
    for ch in chapters:
        if "S16" in ch.get("name", "") and "Trading tips" in ch.get("name", ""):
            return ch
    return None


def push_lesson(ps: requests.Session, prod_base: str, ph: dict, prod_act: dict, local_act: dict, label: str) -> bool:
    content = local_act.get("content")
    if not content:
        print(f"  skip (no content): {label}")
        return False
    r = ps.put(
        f"{prod_base}/activities/{prod_act['activity_uuid']}",
        headers=ph,
        json={
            "name": prod_act["name"],
            "activity_type": prod_act.get("activity_type", "TYPE_DYNAMIC"),
            "activity_sub_type": prod_act.get("activity_sub_type", "SUBTYPE_DYNAMIC_PAGE"),
            "content": content,
            "published": True,
        },
        timeout=30,
    )
    if r.status_code == 200:
        blocks = len(content.get("content", []))
        has_vid = any(b.get("type") == "blockEmbed" for b in content.get("content", []))
        print(f"  ok [{ 'video' if has_vid else 'text' }] {prod_act['name'][:58]} ({blocks} blocks)")
        return True
    print(f"  FAIL {prod_act['name'][:40]}: {r.status_code} {r.text[:100]}")
    return False


def main() -> int:
    ls, ps = requests.Session(), requests.Session()
    lt, pt = login(ls, LOCAL, LOCAL_PWD), login(ps, PROD, PROD_PWD)
    lh, ph = {"Authorization": f"Bearer {lt}"}, {"Authorization": f"Bearer {pt}"}

    lch, pch = get_chapters(ls, LOCAL, lt), get_chapters(ps, PROD, pt)
    local_s16 = find_s16(lch, prefer_dash=True)
    prod_s16 = find_s16(pch, prefer_dash=False)

    print("=== A: S16 merge by index ===")
    if not local_s16 or not prod_s16:
        print("  ERROR: S16 chapter not found")
        print(f"  local: {local_s16['name'] if local_s16 else 'MISSING'}")
        print(f"  prod:  {prod_s16['name'] if prod_s16 else 'MISSING'}")
    else:
        print(f"  Local: {local_s16['name']} ({len(local_s16.get('activities', []))} lessons)")
        print(f"  Prod:  {prod_s16['name']} ({len(prod_s16.get('activities', []))} lessons)")
        local_acts = local_s16.get("activities") or []
        prod_acts = prod_s16.get("activities") or []
        n = min(len(local_acts), len(prod_acts))
        a_ok = 0
        for i in range(n):
            print(f"  [{i+1}/{n}] local: {local_acts[i]['name'][:50]}")
            print(f"       -> prod: {prod_acts[i]['name'][:50]}")
            if push_lesson(ps, PROD, ph, prod_acts[i], local_acts[i], f"S16-{i+1}"):
                a_ok += 1
        if len(local_acts) > len(prod_acts):
            for a in local_acts[len(prod_acts) :]:
                print(f"  !! local-only (no prod slot): {a['name'][:60]}")
        print(f"  S16 merged: {a_ok}/{n}")

    print("\n=== B: Quiz force-sync ===")
    prod_by_title = {}
    for ch in pch:
        for a in ch.get("activities") or []:
            prod_by_title[a["name"]] = a

    local_by_title = {}
    for ch in lch:
        for a in ch.get("activities") or []:
            local_by_title[a["name"]] = a

    b_ok = 0
    for title in FORCE_SYNC_TITLES:
        la = local_by_title.get(title)
        pa = prod_by_title.get(title)
        if not la:
            print(f"  MISSING local: {title}")
            continue
        if not pa:
            print(f"  MISSING prod: {title}")
            continue
        print(f"  {title[:55]}")
        if push_lesson(ps, PROD, ph, pa, la, title):
            b_ok += 1
    print(f"  Quiz synced: {b_ok}/{len(FORCE_SYNC_TITLES)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"API error: {exc}", file=sys.stderr)
        raise SystemExit(1)
