#!/usr/bin/env python3
"""Create the as-is Udemy Market Structure course skeleton in an existing LearnHouse course.

Direct Web Import into Existing Course mode.

Source Udemy:
https://www.udemy.com/course/market-structure-in-trading-from-zero-to-hero-18-hours/

Target LearnHouse:
https://learn.azzamedu.com/course/2b8dad9d-39e8-43bc-bebe-46add8baad04

Rules:
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
    "TARGET_COURSE_UUID", "course_2b8dad9d-39e8-43bc-bebe-46add8baad04"
)
if not TARGET_COURSE_UUID.startswith("course_"):
    TARGET_COURSE_UUID = f"course_{TARGET_COURSE_UUID}"

# Captured from Udemy public curriculum after expanding all sections in Chrome.
CURRICULUM: list[tuple[str, list[str]]] = [
    [
        "Jayce's INTRODUCTION - Get your TRUST - Learn more Serious - Get the real result",
        [
            "What You'll Get in This Course",
            "Effective Study Schedule for the serious traders",
            "How to download PDF documents"
        ]
    ],
    [
        "Market structure - the key element to make different in trading",
        [
            "What is market structure and market cycle ?",
            "The waves of market structure",
            "Internal Structure - A common mistake",
            "How to define TREND with Market structure",
            "When market is changed the trend"
        ]
    ],
    [
        "Market structure and Trading strategy",
        [
            "Why market structure and KEY LEVEL can define the TREND - Market liquidity",
            "The best strategies you can combine with market structure",
            "Apply Market structure and strategy on Bitcoin trading"
        ]
    ],
    [
        "SINGLE CANDLE Full knowledge",
        [
            "Three types of CANDLEs MUST and JUST need to know",
            "Marubozu candle - High pressure candle",
            "Pinbar candle - High fluctuation candle",
            "Doji candle - No power candle",
            "Normal candle - Unclearly power candle",
            "Speical marubozu candle - Advanced knowledge for top traders"
        ]
    ],
    [
        "How to define a VALID PULLBACK - Full standard - Advanced level",
        [
            "Pullback mindset and stories",
            "Two Maru candle STANDARD in Pullback",
            "BIG maru and one small candle - Same color case",
            "BIG Maru and one small candle - Different color case",
            "Price action in Pullback - Advanced level (PAC Standard)"
        ]
    ],
    [
        "How to define a VALID BREAK OUT - Full standard - Advanced level",
        [
            "Two Maru STANDARD in Break Out",
            "Big Maru and one small candle - same color case",
            "Big Maru and one small candle - Different color case",
            "Price action confirmation in BREAK OUT (PAC standard)",
            "ADVANCED _ Speical break out and pullback cases must KNOW"
        ]
    ],
    [
        "How to define a RANGE - full standard",
        [
            "Range by Marubozu candle",
            "Range by Pinbar and Doji candles",
            "Range by an INVALID PULLBACK",
            "Range by a FAKE BREAK OUT",
            "What you should do with a RANGE _ Trading or Skip it",
            "RANGE before and after a valid pullback",
            "Low liquidity RANGE"
        ]
    ],
    [
        "10 MARKET STRUCTURE assginments - Medium level",
        [
            "Assigment #1 - XAUUSD Market structure - detail explanation",
            "Assigment #2 - NZDUSD - Market structure - detail explanation",
            "How to analyze market structure QUICKER",
            "Assigment #3 - EURAUD - Start to analyze chart quicker",
            "Assigment #4 - EURAUD - A note for price action confirmation",
            "Assigment #5 - Bitcoin chart - A speical case of PRICE ACTION confirmation",
            "Assigment #6 - Bitcoin - A noise chart with gap",
            "Assigment #7 - USDCAD - A difficult chart of price action confirmation",
            "Assigment #8 - USDJPY - Noise and hard market with price action",
            "Assigment #9 - GBPAUD - A speical point of big maru and one small candle",
            "Assigment #10 - BNBUSD - Analyze pullback to find Risky zone"
        ]
    ],
    [
        "10 MARKET STRUCTURE assginments - Pro level",
        [
            "Assigment #11 - S&P 500 Index - Analyze with GAP on M1 chart",
            "Assigment #12 - NZDUSD - Price action confirmation at sensitive place",
            "Assigment #13 - GBPUSD - When and where will we start analyze a chart",
            "Assigment #14 - SOLANA- Always follow Market flow during analyze",
            "Assigment #15 - USDCHF- Boom and Crash case - Market structure with big NEWS",
            "Assigment #16 - USDCHF- How to understand a NOISE market structure",
            "Assigment #17 - CADJPY - How smart money work with market structure",
            "Assigment #18 - US30 - How to analyze a STRAIGHT WAVE - No pullback",
            "Assigment #19 - Emini Nasdaq 100 Futures - Scaling on M1 timeframe ?",
            "Assigment #20 - Bank of America - Scalping mindset"
        ]
    ],
    [
        "How to analyze market structure with GAPS",
        [
            "How GAP appears on chart",
            "When GAP appears on chart",
            "How to TRADE with GAP market",
            "Example with India Stock - Bank of Baroda (BoB)"
        ]
    ],
    [
        "Multiple timeframe theories - Start to Establish your Trading System",
        [
            "BASE timeframe - the key of multiple timefram effectively",
            "Function of Satellite timeframes - the remain market pictures",
            "How to Combine Multiple timeframe with market example - having example",
            "JUDGE market condition on HIGH timeframe to reduce RISK",
            "Detail EXAMPLE about Trading with Multiple timeframe"
        ]
    ],
    [
        "MARKET CYCLE Theories - The Beginning and ending of a trend/wave",
        [
            "Market cycle you must know before start trading",
            "Avoid losing trade with Market CYCLE",
            "Market CYCLE works perfectly with smart money concepts on Bitcoint chart"
        ]
    ],
    [
        "COMBINE Market structure - Market cycle - Multiple timeframe",
        [
            "How to analyze the Market structrure from D1 to M1 on GBPUSD - Part 1",
            "How to analyze the Market structrure from D1 to M1 on GBPUSD - Part 2",
            "When to STOP analyzing on Lower timeframe ? XAUUSD from H1 to M1",
            "The best market condition to TRADE on lower timeframe"
        ]
    ],
    [
        "TF/2 - A high level of market structure for Pro trader",
        [
            "TF2 standard - Advanced level of market structure for Pro trader",
            "Trading plan with T and TF2 standard on GOLD H4",
            "Six cases must know to use TF2 smoothly"
        ]
    ],
    [
        "SOP - PDCA process - A professional learning, practicing process in trading",
        [
            "SOP definition to Work consistency",
            "SOP assignments - How to give out trading plan from a clean chart",
            "SOP-PDCA process to practice after the course",
            "How to know your MARKET STRUCTURE is correctly - market verification"
        ]
    ],
    [
        "Thank you",
        [
            "Thank you and Trading mindset to the serious traders",
            "Tip 2025 : Where should you start analyzing on a clean chart ?",
            "Bonus Section : Start learning & practicing from Zero to Profitable level",
            "Practicing after the course carefully - The key mindset to make changes"
        ]
    ],
    [
        "More knowledges with Advanced cases (After course section)",
        [
            "Reading PRICE ACTION - Don't read candle by candle - Explain again lecture 59",
            "Economic NEWs & Polistic News"
        ]
    ],
    [
        "Extra : The mindset of successful traders",
        [
            "The Missing Piece Most Struggling Traders Don't Know About",
            "ZONE is Tested - Power is absorbed"
        ]
    ]
]
EXPECTED_SECTIONS = 18
EXPECTED_LESSONS = 86


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


def create_chapter(session: requests.Session, token: str, course_id: int, name: str, description: str = "") -> dict:
    payload = {"course_id": course_id, "name": name, "description": description, "org_id": ORG_ID}
    r = session.post(f"{BASE_URL}/chapters/", headers=auth_headers(token), json=payload, timeout=30)
    r.raise_for_status()
    return r.json()


def list_courses(session: requests.Session, token: str) -> list[dict]:
    r = session.get(f"{BASE_URL}/courses/org_slug/{ORG_SLUG}/page/1/limit/100", headers=auth_headers(token), timeout=30)
    r.raise_for_status()
    return r.json()


def get_course(session: requests.Session, token: str) -> dict:
    for course in list_courses(session, token):
        if course.get("course_uuid") == TARGET_COURSE_UUID:
            return course
    raise RuntimeError(f"Target course not found: {TARGET_COURSE_UUID}")


def get_chapters(session: requests.Session, token: str, course_id: int) -> list[dict]:
    r = session.get(f"{BASE_URL}/chapters/course/{course_id}/page/1/limit/100", headers=auth_headers(token), timeout=30)
    r.raise_for_status()
    return r.json()


def blank_doc() -> dict:
    return {"type": "doc", "content": [{"type": "paragraph", "content": [{"type": "text", "text": " "}]}]}


def create_activity(session: requests.Session, token: str, chapter_id: int, title: str) -> dict:
    payload = {
        "name": title,
        "chapter_id": chapter_id,
        "activity_type": "TYPE_DYNAMIC",
        "activity_sub_type": "SUBTYPE_DYNAMIC_PAGE",
        "published": True,
        "content": blank_doc(),
    }
    r = session.post(f"{BASE_URL}/activities/", headers=auth_headers(token), json=payload, timeout=30)
    r.raise_for_status()
    return r.json()


def validate_curriculum() -> None:
    lesson_count = sum(len(lessons) for _section, lessons in CURRICULUM)
    if len(CURRICULUM) != EXPECTED_SECTIONS:
        raise RuntimeError(f"Expected {EXPECTED_SECTIONS} sections, got {len(CURRICULUM)}")
    if lesson_count != EXPECTED_LESSONS:
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
