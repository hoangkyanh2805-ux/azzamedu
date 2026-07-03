#!/usr/bin/env python3
"""Seed Alpha Elite Apprentice course into local LearnHouse via REST API."""

from __future__ import annotations

import sys

import requests

from course_api import (
    ADMIN_EMAIL,
    CONTENT,
    COURSE_NAME,
    MODULE_FILES,
    create_chapter,
    create_course,
    create_lesson,
    delete_course,
    list_courses,
    login,
    parse_module,
    publish_course,
)


def main() -> int:
    session = requests.Session()
    print("Logging in...")
    token = login(session)

    for course in list_courses(session, token):
        if course.get("name") in (COURSE_NAME, "Test Course"):
            print(f"Removing existing course: {course['name']} ({course['course_uuid']})")
            delete_course(session, token, course["course_uuid"])

    print("Creating course...")
    course = create_course(session, token)
    course_id = course["id"]
    course_uuid = course["course_uuid"]
    print(f"  course_uuid={course_uuid}")

    total_lessons = 0
    for filename in MODULE_FILES:
        path = CONTENT / filename
        if not path.exists():
            print(f"SKIP missing {filename}")
            continue
        module_id, module_title, lessons = parse_module(path)
        chapter_name = f"{module_id}: {module_title}"
        print(f"Chapter {chapter_name} ({len(lessons)} lessons)")
        chapter = create_chapter(session, token, course_id, chapter_name, module_title)
        for title, body in lessons:
            act = create_lesson(session, token, chapter["id"], title, body)
            total_lessons += 1
            print(f"  + {title} -> {act['activity_uuid']}")

    print("Publishing course...")
    publish_course(session, token, course_uuid)

    print("")
    print("=== Seed complete ===")
    print("URL:      http://localhost:8080")
    print(f"Course:   {COURSE_NAME}")
    print(f"UUID:     {course_uuid}")
    print(f"Lessons:  {total_lessons}")
    print(f"Admin:    {ADMIN_EMAIL}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"API error: {exc}", file=sys.stderr)
        if exc.response is not None:
            print(exc.response.text[:500], file=sys.stderr)
        raise SystemExit(1)
