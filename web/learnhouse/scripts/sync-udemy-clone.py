#!/usr/bin/env python3
"""Sync all Udemy-original markdown bodies into existing LearnHouse course (no re-seed)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import requests

from course_api import (
    BASE_URL,
    auth_headers,
    build_activity_map,
    get_chapters,
    login,
    udemy_lesson_page_content,
)

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / "content" / "udemy-clone-curriculum.json"
SECTIONS_DIR = ROOT / "content" / "udemy-original"

COURSE_NAME = "Advanced trading course : The complete Smart Money Concepts"


def load_section_bodies(section_num: int) -> dict[str, str]:
    matches = sorted(SECTIONS_DIR.glob(f"s{section_num:02d}-*.md"))
    if not matches:
        return {}
    text = matches[0].read_text(encoding="utf-8")
    bodies: dict[str, str] = {}
    parts = re.split(r"^## (.+?)\r?\n", text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""
        body = re.split(r"\n---\s*\n", body)[0].strip()
        if body:
            bodies[title.lower()] = body
    return bodies


def find_body(section_bodies: dict[str, str], title: str) -> str | None:
    key = title.lower()
    if key in section_bodies:
        return section_bodies[key]
    for k, v in section_bodies.items():
        if k == key or k.replace("_", " ") in key or key in k:
            return v
    return None


def find_course(session, token: str) -> dict | None:
    r = session.get(
        f"{BASE_URL}/courses/org_slug/alpha-elite/page/1/limit/50",
        headers=auth_headers(token),
        timeout=30,
    )
    r.raise_for_status()
    for c in r.json():
        if c.get("name") == COURSE_NAME:
            return c
    return None


def update_activity(session, token: str, activity_uuid: str, title: str, page: dict) -> None:
    payload = {
        "name": title,
        "activity_type": "TYPE_DYNAMIC",
        "activity_sub_type": "SUBTYPE_DYNAMIC_PAGE",
        "content": page,
        "published": True,
    }
    r = session.put(
        f"{BASE_URL}/activities/{activity_uuid}",
        headers=auth_headers(token),
        json=payload,
        timeout=60,
    )
    r.raise_for_status()


def main() -> int:
    data = json.loads(CURRICULUM.read_text(encoding="utf-8"))
    session = requests.Session()
    print("Logging in...")
    token = login(session)

    course = find_course(session, token)
    if not course:
        print(f"Course not found: {COURSE_NAME}. Run seed-udemy-clone.ps1 first.")
        return 1

    chapters = get_chapters(session, token, course["id"])
    by_name: dict[str, dict] = {}
    for ch in chapters:
        for act in ch.get("activities") or []:
            by_name[act.get("name", "").lower()] = act

    updated = 0
    missing = 0
    for ch in data["chapters"]:
        section_num = ch["number"]
        bodies = load_section_bodies(section_num)
        print(f"\nS{section_num:02d}: {len(bodies)} md lessons, {len(ch['lessons'])} json lessons")
        for lesson in ch["lessons"]:
            title = lesson["title"]
            act = by_name.get(title.lower())
            if not act:
                print(f"  MISSING activity: {title[:60]}")
                missing += 1
                continue
            body = lesson.get("body") or find_body(bodies, title)
            if not body:
                print(f"  MISSING body: {title[:60]}")
                missing += 1
                continue
            page = udemy_lesson_page_content(body)
            update_activity(session, token, act["activity_uuid"], title, page)
            updated += 1
            blocks = len(page.get("content", []))
            print(f"  ok {title[:50]} ({blocks} blocks)")

    print(f"\n=== Synced {updated} lessons, {missing} missing ===")
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"API error: {exc}", file=sys.stderr)
        if exc.response is not None:
            print(exc.response.text[:500], file=sys.stderr)
        raise SystemExit(1)
