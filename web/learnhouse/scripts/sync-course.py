#!/usr/bin/env python3
"""Sync lesson markdown from repo into existing LearnHouse course."""

from __future__ import annotations

import sys

import requests

from course_api import (
    BASE_URL,
    CONTENT,
    COURSE_ABOUT,
    COURSE_DESCRIPTION,
    COURSE_NAME,
    MODULE_FILES,
    auth_headers,
    build_activity_map,
    find_course,
    get_chapters,
    learnings_html,
    lesson_page_content,
    login,
    normalize_lesson_key,
    parse_module,
)


def update_activity(session, token: str, activity_uuid: str, title: str, page_content: dict) -> None:
    payload = {
        "name": title,
        "activity_type": "TYPE_DYNAMIC",
        "activity_sub_type": "SUBTYPE_DYNAMIC_PAGE",
        "content": page_content,
        "published": True,
    }
    r = session.put(
        f"{BASE_URL}/activities/{activity_uuid}",
        headers=auth_headers(token),
        json=payload,
        timeout=30,
    )
    r.raise_for_status()


def update_course_meta(session, token: str, course_uuid: str) -> None:
    r = session.put(
        f"{BASE_URL}/courses/{course_uuid}",
        headers=auth_headers(token),
        json={
            "description": COURSE_DESCRIPTION,
            "about": COURSE_ABOUT,
            "learnings": learnings_html(),
            "published": True,
        },
        timeout=30,
    )
    r.raise_for_status()


def main() -> int:
    session = requests.Session()
    print("Logging in...")
    token = login(session)

    course = find_course(session, token)
    if not course:
        print(f"Course '{COURSE_NAME}' not found. Run seed-course.ps1 first.")
        return 1

    course_id = course["id"]
    course_uuid = course["course_uuid"]
    print(f"Syncing {course_uuid} (id={course_id})")

    chapters = get_chapters(session, token, course_id)
    act_map = build_activity_map(chapters)

    updated = 0
    missing = 0
    for filename in MODULE_FILES:
        path = CONTENT / filename
        if not path.exists():
            continue
        _mod_id, _mod_title, lessons = parse_module(path)
        for title, body in lessons:
            key = normalize_lesson_key(title)
            activity = act_map.get(key)
            if not activity:
                print(f"  MISSING: {title}")
                missing += 1
                continue
            page = lesson_page_content(title, body)
            update_activity(session, token, activity["activity_uuid"], title, page)
            updated += 1
            print(f"  updated {key}")

    print("Updating course About / What you will learn...")
    update_course_meta(session, token, course_uuid)

    print(f"\nDone: {updated} lessons synced, {missing} missing.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"API error: {exc}", file=sys.stderr)
        if exc.response is not None:
            print(exc.response.text[:500], file=sys.stderr)
        raise SystemExit(1)
