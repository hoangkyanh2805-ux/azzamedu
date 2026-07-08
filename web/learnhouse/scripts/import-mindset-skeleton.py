#!/usr/bin/env python3
"""Create the as-is Udemy Mindset course skeleton in an existing LearnHouse course.

Direct Web Import into Existing Course mode.

Source Udemy:
https://www.udemy.com/course/the-mindset-must-know-before-learning-trading-and-investing/

Target LearnHouse:
https://learn.azzamedu.com/course/b2acf623-7983-4fe4-bb7f-5b2447faa998

Rules:
- targets one existing course UUID only
- creates missing chapters/activities only
- does not create/delete courses
- does not rewrite lesson titles or add custom lesson copy
- does not import videos/resources; attach those to matching lessons afterwards
- requires verified logged-in Udemy/export curriculum before skeleton import
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
    "TARGET_COURSE_UUID", "course_b2acf623-7983-4fe4-bb7f-5b2447faa998"
)
if not TARGET_COURSE_UUID.startswith("course_"):
    TARGET_COURSE_UUID = f"course_{TARGET_COURSE_UUID}"

# Fill this only from logged-in Udemy curriculum or exported course package.
# Do not guess section/lecture titles from public metadata.
CURRICULUM: list[tuple[str, list[str]]] = []
EXPECTED_SECTIONS = 0
EXPECTED_LESSONS = 0


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def login(session: requests.Session) -> str:
    if not ADMIN_PASSWORD:
        raise RuntimeError("LEARNHOUSE_ADMIN_PASSWORD is required")
    r = session.post(
        f"{BASE_URL}/auth/login",
        data={"username": ADMIN_EMAIL, "password": ADMIN_PASSWORD},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["tokens"]["access_token"]


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


def validate_curriculum() -> None:
    if not CURRICULUM:
        raise RuntimeError(
            "Mindset CURRICULUM is empty. Fill it from logged-in Udemy/export before running."
        )
    lesson_count = sum(len(lessons) for _section, lessons in CURRICULUM)
    if EXPECTED_SECTIONS and len(CURRICULUM) != EXPECTED_SECTIONS:
        raise RuntimeError(
            f"Expected {EXPECTED_SECTIONS} sections, got {len(CURRICULUM)}"
        )
    if EXPECTED_LESSONS and lesson_count != EXPECTED_LESSONS:
        raise RuntimeError(f"Expected {EXPECTED_LESSONS} lessons, got {lesson_count}")


def main() -> int:
    validate_curriculum()
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

    expected_lessons = sum(len(lessons) for _section, lessons in CURRICULUM)
    print("\nDONE")
    print(f"Created chapters: {created_chapters}")
    print(f"Created lessons: {created_activities}")
    print(f"Skipped existing lessons: {skipped_activities}")
    print(f"Expected skeleton: {len(CURRICULUM)} sections, {expected_lessons} lessons")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
