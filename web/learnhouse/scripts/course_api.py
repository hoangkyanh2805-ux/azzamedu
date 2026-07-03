"""Shared LearnHouse course API helpers for seed + sync scripts."""

from __future__ import annotations

import os
import re
from pathlib import Path

import requests

BASE_URL = os.environ.get("LEARNHOUSE_API", "http://localhost:8080/api/v1")
ADMIN_EMAIL = os.environ.get("LEARNHOUSE_ADMIN_EMAIL", "admin@hoa-homes.com")
ADMIN_PASSWORD = os.environ.get("LEARNHOUSE_ADMIN_PASSWORD", "AlphaElite-Local-2026!")
ORG_ID = int(os.environ.get("LEARNHOUSE_ORG_ID", "1"))
ORG_SLUG = os.environ.get("LEARNHOUSE_ORG_SLUG", "alpha-elite")

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "apprentice-operating-course"

MODULE_FILES = [
    "m01-operating-mindset.md",
    "m02-market-structure-foundations.md",
    "m03-poi-setup-framework.md",
    "m04-risk-sizing-protocol.md",
    "m05-session-sops-journal.md",
    "m06-case-walkthroughs.md",
    "m07-confirmation-mtf.md",
    "m08-tools-path-vip.md",
]

COURSE_NAME = "Apprentice Operating Course"
COURSE_DESCRIPTION = (
    "Install a repeatable XAUUSD operating desk: market structure literacy, "
    "2% risk protocol, session SOPs, and journal discipline. Education only — not a signal group."
)
COURSE_ABOUT = """Alpha Elite Apprentice is a private **operating system** for serious traders.

**21 sections · full SMC education path**

You will learn liquidity, fair value gap (IMB), manipulation phases, BOS/CHoCH, double order-block POI, trend follow vs structure break, session reviews, journal discipline, quizzes, and final exam — inside a documented framework, not an alert feed.

**Compliance:** Trading involves substantial risk. No profit guarantees. Not investment advice.
"""
COURSE_LEARNINGS = """- Course path, operator mindset, and VIP onboarding (education)
- Market structure definitions — liquidity, IMB/FVG, BOS, CHoCH, POI
- Double order block with POI and BOS bounce frameworks
- Trend follow vs structure break — theory and cases
- Educational walkthroughs on XAUUSD, US30, EURCAD, USDCHF
- Session review days and scalping framework documentation
- Trading journal and process-only experience sharing
- Basic + advanced quiz banks and final examination
- 2026 structure rules, tools, lot size, and next steps
"""


def learnings_html() -> str:
    items = [
        line.strip().lstrip("-").strip()
        for line in COURSE_LEARNINGS.strip().splitlines()
        if line.strip()
    ]
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def login(session: requests.Session) -> str:
    r = session.post(
        f"{BASE_URL}/auth/login",
        data={"username": ADMIN_EMAIL, "password": ADMIN_PASSWORD},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["tokens"]["access_token"]


def auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def list_courses(session: requests.Session, token: str) -> list:
    r = session.get(
        f"{BASE_URL}/courses/org_slug/{ORG_SLUG}/page/1/limit/50",
        headers=auth_headers(token),
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def find_course(session: requests.Session, token: str) -> dict | None:
    for course in list_courses(session, token):
        if course.get("name") == COURSE_NAME:
            return course
    return None


def get_chapters(session: requests.Session, token: str, course_id: int) -> list:
    r = session.get(
        f"{BASE_URL}/chapters/course/{course_id}/page/1/limit/50",
        headers=auth_headers(token),
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def parse_module(path: Path) -> tuple[str, str, list[tuple[str, str]]]:
    text = path.read_text(encoding="utf-8")
    header = re.match(r"# (M\d+) — (.+?)\r?\n", text)
    if not header:
        raise ValueError(f"Invalid module header: {path}")
    module_id, module_title = header.group(1), header.group(2).strip()

    lessons: list[tuple[str, str]] = []
    pattern = re.compile(r"^## (M\d+L\d+ — .+?)\r?\n", re.MULTILINE)
    matches = list(pattern.finditer(text))
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        body = re.split(r"\n## Module \d+ completion", body)[0].strip()
        lessons.append((title, body))
    return module_id, module_title, lessons


def lesson_markdown(title: str, body: str) -> str:
    if "### Compliance note" in body:
        return f"# {title}\n\n{body}"
    disclaimer = (
        "\n\n---\n\n*Education only. Trading involves substantial risk. "
        "Nothing here guarantees profit or constitutes investment advice.*\n"
    )
    return f"# {title}\n\n{body}{disclaimer}"


def _inline_nodes(text: str) -> list[dict]:
    """Parse **bold** and *italic* into TipTap text nodes."""
    nodes: list[dict] = []
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|[^*]+)")
    for part in pattern.findall(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            nodes.append({"type": "text", "text": part[2:-2], "marks": [{"type": "bold"}]})
        elif part.startswith("*") and part.endswith("*"):
            nodes.append({"type": "text", "text": part[1:-1], "marks": [{"type": "italic"}]})
        else:
            nodes.append({"type": "text", "text": part})
    return nodes or [{"type": "text", "text": text}]


def _paragraph(text: str) -> dict:
    return {"type": "paragraph", "content": _inline_nodes(text.strip())}


def _heading(level: int, text: str) -> dict:
    return {
        "type": "heading",
        "attrs": {"level": level},
        "content": [{"type": "text", "text": text.strip()}],
    }


def markdown_to_tiptap_doc(markdown: str) -> dict:
    """TipTap document for LearnHouse activity.content (root must be type: doc)."""
    lines = markdown.splitlines()
    blocks: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped or stripped == "---":
            i += 1
            continue

        if stripped.startswith("#### "):
            blocks.append(_heading(4, stripped[5:]))
            i += 1
            continue
        if stripped.startswith("### "):
            blocks.append(_heading(3, stripped[4:]))
            i += 1
            continue
        if stripped.startswith("## "):
            blocks.append(_heading(2, stripped[3:]))
            i += 1
            continue
        if stripped.startswith("# "):
            blocks.append(_heading(1, stripped[2:]))
            i += 1
            continue

        if stripped.startswith("|") and "|" in stripped[1:]:
            table_rows: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = lines[i].strip()
                if not re.match(r"^\|[-: |]+\|$", row):
                    table_rows.append(row)
                i += 1
            for row in table_rows:
                cells = [c.strip() for c in row.strip("|").split("|")]
                blocks.append(_paragraph(" | ".join(cells)))
            continue

        if stripped.startswith("- "):
            items: list[dict] = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(
                    {
                        "type": "listItem",
                        "content": [_paragraph(lines[i].strip()[2:])],
                    }
                )
                i += 1
            blocks.append({"type": "bulletList", "content": items})
            continue

        if stripped[0].isdigit() and ". " in stripped[:4]:
            items: list[dict] = []
            while i < len(lines):
                s = lines[i].strip()
                if not (s and s[0].isdigit() and ". " in s[:4]):
                    break
                text = s.split(". ", 1)[1] if ". " in s else s
                items.append({"type": "listItem", "content": [_paragraph(text)]})
                i += 1
            blocks.append({"type": "orderedList", "content": items})
            continue

        para_parts: list[str] = []
        while i < len(lines):
            s = lines[i].strip()
            if not s or s == "---" or s.startswith("#") or s.startswith("- ") or (
                s.startswith("|") and "|" in s[1:]
            ) or (s[0].isdigit() and ". " in s[:4]):
                break
            para_parts.append(s)
            i += 1
        if para_parts:
            blocks.append(_paragraph(" ".join(para_parts)))
        else:
            i += 1

    if not blocks:
        blocks.append(_paragraph(" "))
    return {"type": "doc", "content": blocks}


def markdown_to_page_content(markdown: str) -> dict:
    """Legacy wrapper — returns {body: doc} for older sync scripts."""
    return {"body": markdown_to_tiptap_doc(markdown)}


def udemy_lesson_page_content(body: str) -> dict:
    """Verbatim Udemy clone — TipTap doc as activity.content (no title wrapper)."""
    return markdown_to_tiptap_doc(body.strip())


def lesson_page_content(title: str, body: str) -> dict:
    return markdown_to_tiptap_doc(lesson_markdown(title, body))


def activity_payload(title: str, chapter_id: int, page_content: dict) -> dict:
    return {
        "name": title,
        "chapter_id": chapter_id,
        "activity_type": "TYPE_DYNAMIC",
        "activity_sub_type": "SUBTYPE_DYNAMIC_PAGE",
        "published": True,
        "content": page_content,
    }


def normalize_lesson_key(title: str) -> str:
    m = re.match(r"(M\d+L\d+)", title)
    return m.group(1) if m else title.strip().lower()


def build_activity_map(chapters: list) -> dict[str, dict]:
    mapping: dict[str, dict] = {}
    for chapter in chapters:
        for activity in chapter.get("activities") or []:
            mapping[normalize_lesson_key(activity.get("name", ""))] = activity
    return mapping


def delete_course(session: requests.Session, token: str, course_uuid: str) -> None:
    r = session.delete(
        f"{BASE_URL}/courses/{course_uuid}",
        headers=auth_headers(token),
        timeout=30,
    )
    if r.status_code not in (200, 204, 404):
        r.raise_for_status()


def create_course(session: requests.Session, token: str) -> dict:
    form = {
        "name": COURSE_NAME,
        "description": COURSE_DESCRIPTION,
        "public": "false",
        "about": COURSE_ABOUT,
        "learnings": learnings_html(),
        "tags": "apprentice,operating-course,xauusd",
        "thumbnail_type": "image",
    }
    r = session.post(
        f"{BASE_URL}/courses/?org_id={ORG_ID}",
        data=form,
        headers={"Authorization": f"Bearer {token}"},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def publish_course(session: requests.Session, token: str, course_uuid: str) -> None:
    r = session.put(
        f"{BASE_URL}/courses/{course_uuid}",
        headers=auth_headers(token),
        json={"published": True, "public": False},
        timeout=30,
    )
    r.raise_for_status()


def create_chapter(
    session: requests.Session, token: str, course_id: int, name: str, description: str
) -> dict:
    payload = {
        "name": name,
        "description": description,
        "org_id": ORG_ID,
        "course_id": course_id,
    }
    r = session.post(
        f"{BASE_URL}/chapters/",
        headers=auth_headers(token),
        json=payload,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def create_lesson(
    session: requests.Session, token: str, chapter_id: int, title: str, body: str
) -> dict:
    page = lesson_page_content(title, body)
    payload = activity_payload(title, chapter_id, page)
    r = session.post(
        f"{BASE_URL}/activities/",
        headers=auth_headers(token),
        json=payload,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()
