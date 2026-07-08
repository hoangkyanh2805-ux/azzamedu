#!/usr/bin/env python3
"""Create the as-is Udemy MTF course skeleton in an existing LearnHouse course.

This script is intentionally narrow:
- targets one existing course UUID only
- creates missing chapters/activities only
- does not create/delete courses
- does not rewrite lesson titles or add custom lesson copy
- does not import videos/resources; attach those to matching lessons afterwards
"""

from __future__ import annotations

import os
import sys

import requests

BASE_URL = os.environ.get("LEARNHOUSE_API", "https://learn.azzamedu.com/api/v1")
ORG_SLUG = os.environ.get("LEARNHOUSE_ORG_SLUG", "alpha-elite")
ORG_ID = int(os.environ.get("LEARNHOUSE_ORG_ID", "1"))
ADMIN_EMAIL = os.environ.get("LEARNHOUSE_ADMIN_EMAIL", "admin@hoa-homes.com")
ADMIN_PASSWORD = os.environ.get("LEARNHOUSE_ADMIN_PASSWORD", "")
TARGET_COURSE_UUID = os.environ.get(
    "TARGET_COURSE_UUID", "course_f0b9e0d8-240b-47b5-8c39-1a713dccdc0a"
)
if not TARGET_COURSE_UUID.startswith("course_"):
    TARGET_COURSE_UUID = f"course_{TARGET_COURSE_UUID}"

CURRICULUM = [
    (
        "Introduction",
        [
            "Introduction",
            "Share to you my Motivation when I just started this career",
            "Trader Yusuf withdrawn 1669$ after learning 3 months only",
            "Jayce Interview by England funds _ How did I come to top 1% in competitions?",
            "How to start your trading career and get freedom financial",
            "Quick recap about NCI trading system from level 0 - 5",
            "Discord community - NCI Trading",
            "Telegram community - NCI Trading",
            "TOP 7 Trader on FTMO real account Leaderboard 06/2024",
            "PLease becareful with spammers",
        ],
    ),
    (
        "Trading journal for you to gain the real experience - NEW UPDATE this year",
        [
            "Reading all my strategy by my only one day trading examples + 5%/day scalp 2700$",
            "My day trading journal - Sep 27th 2022",
            "My day trading journal - Sep 28th 2022",
        ],
    ),
    (
        "Quick recap about NCI trading system from level 0 - 5 and BONUS",
        ["Quick recap about NCI trading system from level 0 - 5 and BONUS"],
    ),
    (
        "Trading examples - Multiple timeframe with Key level and Smart Money Concepts",
        [
            "How did I get 8000$ with Gold trading using Key level and Smart Money strategy",
            "Three types of candles you must know on this career",
        ],
    ),
    (
        "Basic about Multiple Time-Frame",
        [
            "Benefit of using Multiple-Timeframe?",
            "How many timeframe we should use",
        ],
    ),
    (
        "How to choose number of Time-Frame suitable",
        [
            "Choosing number of timeframe based on trading styles",
            "Choosing number of timeframe based on your logical",
        ],
    ),
    (
        "How to Select your trading method with Multiple Timeframe",
        [
            "Top-down & Dow top analyzation",
            "How to use Top down - Down top",
            "When we need to use TOP DOWN and DOWN TOP",
        ],
    ),
    (
        "How to analyze with Multiple Timeframe",
        [
            "Market cycle Theory and Standard to Entry by TOP DOWN",
            "Standard to Entry by DOWN TOP",
        ],
    ),
    ("Conclusion", ["Checking what did you get"]),
]


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def login(session: requests.Session) -> str:
    if not ADMIN_PASSWORD:
        raise RuntimeError("LEARNHOUSE_ADMIN_PASSWORD is required")
    r = session.post(
        f"{BASE_URL}/auth/login",
        json={"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["access_token"]


def create_chapter(
    session: requests.Session,
    token: str,
    course_id: int,
    name: str,
    description: str = "",
) -> dict:
    payload = {
        "course_id": course_id,
        "name": name,
        "description": description,
        "org_id": ORG_ID,
    }
    r = session.post(
        f"{BASE_URL}/chapters/",
        headers=auth_headers(token),
        json=payload,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def list_courses(session: requests.Session, token: str) -> list[dict]:
    r = session.get(
        f"{BASE_URL}/courses/org_slug/{ORG_SLUG}/page/1/limit/100",
        headers=auth_headers(token),
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def get_course(session: requests.Session, token: str) -> dict:
    for course in list_courses(session, token):
        if course.get("course_uuid") == TARGET_COURSE_UUID:
            return course
    raise RuntimeError(f"Target course not found: {TARGET_COURSE_UUID}")


def get_chapters(session: requests.Session, token: str, course_id: int) -> list[dict]:
    r = session.get(
        f"{BASE_URL}/chapters/course/{course_id}/page/1/limit/100",
        headers=auth_headers(token),
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def blank_doc() -> dict:
    return {
        "type": "doc",
        "content": [
            {
                "type": "paragraph",
                "content": [{"type": "text", "text": " "}],
            }
        ],
    }


def create_activity(
    session: requests.Session, token: str, chapter_id: int, title: str
) -> dict:
    payload = {
        "name": title,
        "chapter_id": chapter_id,
        "activity_type": "TYPE_DYNAMIC",
        "activity_sub_type": "SUBTYPE_DYNAMIC_PAGE",
        "published": True,
        "content": blank_doc(),
    }
    r = session.post(
        f"{BASE_URL}/activities/",
        headers=auth_headers(token),
        json=payload,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def main() -> int:
    session = requests.Session()
    print(f"API: {BASE_URL}")
    print(f"Target course UUID: {TARGET_COURSE_UUID}")
    token = login(session)
    course = get_course(session, token)
    print(f"Target course: {course.get('name')} (id={course['id']})")

    chapters = get_chapters(session, token, course["id"])
    by_chapter_name = {c.get("name", ""): c for c in chapters}

    created_chapters = 0
    created_activities = 0
    skipped_activities = 0

    for section_title, lessons in CURRICULUM:
        chapter = by_chapter_name.get(section_title)
        if not chapter:
            chapter = create_chapter(session, token, course["id"], section_title, section_title)
            by_chapter_name[section_title] = chapter
            created_chapters += 1
            print(f"+ chapter: {section_title}")
        else:
            print(f"= chapter: {section_title}")

        existing_titles = {a.get("name", "") for a in (chapter.get("activities") or [])}
        for lesson_title in lessons:
            if lesson_title in existing_titles:
                skipped_activities += 1
                print(f"  = lesson: {lesson_title}")
                continue
            create_activity(session, token, chapter["id"], lesson_title)
            created_activities += 1
            print(f"  + lesson: {lesson_title}")

    print("\nDONE")
    print(f"Created chapters: {created_chapters}")
    print(f"Created lessons: {created_activities}")
    print(f"Skipped existing lessons: {skipped_activities}")
    print(f"Expected skeleton: {len(CURRICULUM)} sections, 26 lessons")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
