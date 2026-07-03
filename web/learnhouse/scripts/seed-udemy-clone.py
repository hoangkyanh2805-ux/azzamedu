#!/usr/bin/env python3
"""Seed LearnHouse with verbatim Udemy SMC clone — original titles, no compliance rewrite."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import requests

from course_api import (
    BASE_URL,
    ORG_ID,
    activity_payload,
    auth_headers,
    create_chapter,
    delete_course,
    login,
    publish_course,
    udemy_lesson_page_content,
    list_courses,
)

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / "content" / "udemy-clone-curriculum.json"
SECTIONS_DIR = ROOT / "content" / "udemy-original"

COURSE_ABOUT_UDEMY = """**What you'll learn**

Step by Step : How to trade with Smart Money Concepts with 3 section : Definition - Main Strategy - Extra Knowledge

Lesson's form : What it is ? - How to define or apply it ? - Example

Definitions : Liquidity - smart money

Definitions : Imbalance

Definitions : Manipulation

Definitions : BOS / CTS

Definitions : Pullback and Break out

Definitions : Premium and Discount

Definitions : Orderblock / POI

Main Strategy : Trading follow trend - Theory & Example

Main Strategy : Trading break trend - Theory & Example

Extra Knowledge : The simple Wyckoff and Elliot

Extra Knowledge : Define MOMENTUM of the waves

Extra Knowledge : Mistake and Successful system

Created by Jayce PHAM | TOP England funds Trader | TOP FTMO leaderboard trader
"""

COURSE_DESCRIPTION_UDEMY = (
    "Level 2. Understand market's Liquidity, Fair value gap (IMB), "
    "manipulation stories to trade better - 2026 update"
)

COURSE_LEARNINGS_HTML = """<ul>
<li>Learn smart money concepts, including liquidity, imbalance, manipulation, and order-blocks</li>
<li>Apply the main strategy to trade trends or breakouts using premium and discount zones</li>
<li>Extra Knowledge: Wyckoff and Elliot, wave momentum, mistakes and successful systems</li>
<li>Live trading sessions, trading journal, quizzes, final exam, NCI indicators</li>
</ul>"""

OLD_COURSE_NAMES = {
    "Apprentice Operating Course",
    "Advanced trading course : The complete Smart Money Concepts",
}


def load_section_bodies(section_num: int) -> dict[str, str]:
    """Load lesson bodies from content/udemy-original/s{nn}-*.md if present."""
    pattern = f"s{section_num:02d}-*.md"
    matches = sorted(SECTIONS_DIR.glob(pattern))
    if not matches:
        return {}

    text = matches[0].read_text(encoding="utf-8")
    bodies: dict[str, str] = {}
    parts = re.split(r"^## (.+?)\r?\n", text, flags=re.MULTILINE)
    # parts[0] is file header; then pairs of (title, body)
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""
        body = re.split(r"\n---\s*\n", body)[0].strip()
        body = re.split(r"\n## Module |\n## Section ", body)[0].strip()
        if body:
            bodies[title.lower()] = body
    return bodies


def generate_lesson_body(section: str, title: str, lesson_type: str, duration: str = "") -> str:
    dur = f" ({duration})" if duration else ""
    if lesson_type == "quiz":
        return f"""### Quiz — {title}

Complete all questions from the downloadable quiz PDF in this section.

**Instructions**
- Review the matching video lectures in this section first
- Answer from your course notes and chart markup practice
- Retake until you score 100% on definitions

### Question bank
See `content/quizzes/quiz-bank.md` and Udemy practice test for this section.

### Video
`[PENDING: attach Udemy quiz or import questions]` · Section: `{section}`
"""
    return f"""### Objective
Master **{title}** using Jayce Pham's lesson form: definition → application → chart example.

### What it is?
{title} is a core piece of the Smart Money Concepts (SMC) map taught in this course. Smart Money refers to institutional participation that leaves a **footprint** on the chart — liquidity engineering, imbalance (FVG), manipulation phases, and POI zones where the next impulse may begin.

This lesson belongs to section **{section}**{dur}. The course teaches step-by-step: **What it is? → How to define or apply it? → Example** — not random entries.

#### Smart Money phases (course map)
- **Phase 0 — Test liquidity:** institutions probe whether momentum is weak after a long trend
- **Phase 1 — Absorbing:** aggressive move creates **IMBALANCE (FVG)** — first confirmation smart money participated
- **Phase 2 — Lack of liquidity / manipulation:** price pushes to collect sell-side liquidity before the real move
- **Phase 3 — POI / discount zone:** price reaches the institutional buy zone — plan the second leg
- **Phase 4 — Retail + institutions together:** structure is obvious; trend continuation or reversal is documented with BOS/CHoCH

### How to define or apply it?
1. Open the execution chart (forex, XAUUSD, crypto, or indices — SMC works on all).
2. Mark the concept from **{title}** on a **historical** chart first (replay mode).
3. Write your **if/then** plan: entry POI, invalidation, target liquidity, and RR before any live click.
4. Confirm with **higher timeframe** bias — course uses multiple timeframe theory (Level 0 in NCI school).
5. Backtest 1–3 months on demo before sizing real risk (course requirement).

**Double Order Block cornerstones (later sections)**
- First order block = cornerstone to explain the **power** of the second order block
- Combine with **market structure**, **market cycle**, and **BOS bounce** for confirmation
- Use **first POI** vs **second POI** to optimize stop placement and RR

### Example
Walk through one historical case where **{title}** appears:

1. **Context:** trend direction on H4/D1 — follow trend or break trend?
2. **Structure:** mark BOS/CHoCH, premium/discount, and liquidity pools
3. **POI:** mark order block / imbalance confluence
4. **Execution:** limit order at POI vs wait for confirmation (covered in Signal Power section)
5. **Management:** partials, break-even, or hold to opposing liquidity — journal every decision

Grade the **quality of your markup** (A–F). The course Q&A: Jayce replies within 4–12 hours on Udemy.

### Practice exercise
- Mark **2 charts** in replay where {title} is visible
- Screenshot before/after with labels: liquidity, IMB, POI, BOS
- Post question in Udemy Q&A if any step is unclear

### Video
`[PENDING: YouTube unlisted]` · `{section} — {title}`{dur}

### Key points
- Lesson form: **What it is? → How to apply? → Example**
- SMC = definitions + main strategy (double OB/POI, trend/break) + extra knowledge
- Backtest 1–3 months before live trading
- Join Discord/Telegram NCI communities for discussion — **not** a signal feed

### Downloads
Check Udemy **Resources** tab for PDFs, indicators, and quiz files for this section.

### Worksheet
Use downloadable materials from the course (setup journal, quiz PDFs).
"""


def resolve_body(
    section_num: int,
    section_title: str,
    lesson: dict,
    section_bodies: dict[str, str],
) -> str:
    if lesson.get("body"):
        return lesson["body"]
    title = lesson["title"]
    key = title.lower()
    if key in section_bodies:
        return section_bodies[key]
    # fuzzy: strip punctuation for match
    for k, v in section_bodies.items():
        if k.replace("_", " ") in key or key in k:
            return v
    return generate_lesson_body(
        section_title,
        title,
        lesson.get("type", "video"),
        lesson.get("duration", ""),
    )


def create_lesson(
    session, token: str, chapter_id: int, section_num: int, section_title: str, lesson: dict
) -> dict:
    title = lesson["title"]
    section_bodies = load_section_bodies(section_num)
    body = resolve_body(section_num, section_title, lesson, section_bodies)
    page = udemy_lesson_page_content(body)
    payload = activity_payload(title, chapter_id, page)
    r = session.post(f"{BASE_URL}/activities/", headers=auth_headers(token), json=payload, timeout=30)
    r.raise_for_status()
    return r.json()


def main() -> int:
    data = json.loads(CURRICULUM.read_text(encoding="utf-8"))
    course_name = data.get("course_title_original", "Advanced trading course : The complete Smart Money Concepts")
    session = requests.Session()
    print("Logging in...")
    token = login(session)

    for c in list_courses(session, token):
        if c.get("name") in OLD_COURSE_NAMES:
            print(f"Removing: {c['name']} ({c['course_uuid']})")
            delete_course(session, token, c["course_uuid"])

    form = {
        "name": course_name,
        "description": COURSE_DESCRIPTION_UDEMY,
        "public": "false",
        "about": COURSE_ABOUT_UDEMY,
        "learnings": COURSE_LEARNINGS_HTML,
        "tags": "smc,smart-money-concepts,jayce-pham,forex,xauusd,udemy-clone",
        "thumbnail_type": "image",
    }
    r = session.post(
        f"{BASE_URL}/courses/?org_id={ORG_ID}",
        data=form,
        headers={"Authorization": f"Bearer {token}"},
        timeout=60,
    )
    r.raise_for_status()
    course = r.json()
    course_id = course["id"]
    course_uuid = course["course_uuid"]
    print(f"Created course {course_uuid}")

    total = 0
    for ch in data["chapters"]:
        section_num = ch["number"]
        section_title = ch["title"]
        name = f"S{section_num:02d}: {section_title}"
        print(f"\n{name} ({len(ch['lessons'])} lessons)")
        chapter = create_chapter(session, token, course_id, name, section_title)
        for lesson in ch["lessons"]:
            act = create_lesson(session, token, chapter["id"], section_num, section_title, lesson)
            total += 1
            print(f"  + {act['name'][:70]}")

    publish_course(session, token, course_uuid)
    print(f"\n=== Udemy ORIGINAL clone seeded: {len(data['chapters'])} sections, {total} lessons ===")
    print("URL: http://localhost:8080")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"API error: {exc}", file=sys.stderr)
        if exc.response is not None:
            print(exc.response.text[:500], file=sys.stderr)
        raise SystemExit(1)
