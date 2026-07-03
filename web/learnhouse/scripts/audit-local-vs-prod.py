#!/usr/bin/env python3
"""Detailed audit: local vs production — every section, every lesson."""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass, field

import requests

LOCAL = os.environ.get("LEARNHOUSE_LOCAL_API", "http://localhost:8080/api/v1")
PROD = os.environ.get("LEARNHOUSE_API", "http://learn.hoa-homes.com/api/v1")
EMAIL = os.environ.get("LEARNHOUSE_ADMIN_EMAIL", "admin@hoa-homes.com")
LOCAL_PWD = os.environ.get("LEARNHOUSE_LOCAL_PASSWORD", "AlphaElite-Local-2026!")
PROD_PWD = os.environ.get("LEARNHOUSE_ADMIN_PASSWORD", "AlphaElite-Prod-Learn-2026!")
COURSE_NAME = "Advanced trading course : The complete Smart Money Concepts"


@dataclass
class LessonInfo:
    title: str
    blocks: int = 0
    has_video: bool = False
    text_len: int = 0
  # first 80 chars of plain text
    preview: str = ""


@dataclass
class SectionInfo:
    name: str
    local_lessons: list[LessonInfo] = field(default_factory=list)
    prod_lessons: list[LessonInfo] = field(default_factory=list)


def login(session: requests.Session, base: str, password: str) -> str:
    r = session.post(f"{base}/auth/login", data={"username": EMAIL, "password": password}, timeout=30)
    r.raise_for_status()
    return r.json()["tokens"]["access_token"]


def plain_text(content: dict | None) -> str:
    if not isinstance(content, dict):
        return ""
    parts: list[str] = []

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "text":
                parts.append(node.get("text", ""))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for x in node:
                walk(x)

    walk(content.get("content", []))
    return " ".join(parts).strip()


def lesson_info(act: dict) -> LessonInfo:
    content = act.get("content") or {}
    blocks = content.get("content", []) if isinstance(content, dict) else []
    has_video = any(b.get("type") == "blockEmbed" for b in blocks)
    text = plain_text(content)
    return LessonInfo(
        title=act.get("name", ""),
        blocks=len(blocks),
        has_video=has_video,
        text_len=len(text),
        preview=text[:100].replace("\n", " "),
    )


def fetch(session: requests.Session, base: str, token: str) -> tuple[dict, list]:
    h = {"Authorization": f"Bearer {token}"}
    courses = session.get(f"{base}/courses/org_slug/alpha-elite/page/1/limit/50", headers=h, timeout=30).json()
    course = next(c for c in courses if c.get("name") == COURSE_NAME)
    chapters = session.get(
        f"{base}/chapters/course/{course['id']}/page/1/limit/50", headers=h, timeout=30
    ).json()
    return course, chapters


def main() -> int:
    ls, ps = requests.Session(), requests.Session()
    lt, pt = login(ls, LOCAL, LOCAL_PWD), login(ps, PROD, PROD_PWD)
    lc, lch = fetch(ls, LOCAL, lt)
    pc, pch = fetch(ps, PROD, pt)

    print("=" * 70)
    print("COURSE METADATA")
    print("=" * 70)
    for label, c in [("LOCAL", lc), ("PROD", pc)]:
        print(f"{label}: thumbnail={bool(c.get('thumbnail_image'))} | about={len(c.get('about') or '')} chars")

    # Index by chapter name (normalize S01 prefix)
    def ch_map(chapters: list) -> dict[str, list[LessonInfo]]:
        m: dict[str, list[LessonInfo]] = {}
        for ch in chapters:
            name = ch.get("name", "")
            m[name] = [lesson_info(a) for a in ch.get("activities") or []]
        return m

    local_ch = ch_map(lch)
    prod_ch = ch_map(pch)

    all_chapters = sorted(set(local_ch) | set(prod_ch))

    issues: list[str] = []
    stats = {
        "sections_ok": 0,
        "lesson_title_mismatch": 0,
        "prod_missing_lesson": 0,
        "local_missing_lesson": 0,
        "video_local_only": 0,
        "video_both": 0,
        "video_neither": 0,
        "text_diff": 0,
        "blocks_diff": 0,
        "prod_no_content": 0,
    }

    report_lines: list[str] = []

    for ch_name in all_chapters:
        ll = local_ch.get(ch_name, [])
        pl = prod_ch.get(ch_name, [])
        report_lines.append(f"\n{'='*70}")
        report_lines.append(f"{ch_name}")
        report_lines.append(f"  Local: {len(ll)} lessons | Prod: {len(pl)} lessons")

        if ch_name not in local_ch:
            stats["local_missing_lesson"] += len(pl)
            report_lines.append("  !! Section MISSING on LOCAL")
            issues.append(f"Section only on PROD: {ch_name}")
            continue
        if ch_name not in prod_ch:
            stats["prod_missing_lesson"] += len(ll)
            report_lines.append("  !! Section MISSING on PROD")
            issues.append(f"Section only on LOCAL: {ch_name}")
            continue

        if len(ll) != len(pl):
            issues.append(f"Count mismatch {ch_name}: local={len(ll)} prod={len(pl)}")

        # Match by index (order should match curriculum)
        max_n = max(len(ll), len(pl))
        section_ok = True
        for i in range(max_n):
            if i >= len(ll):
                stats["prod_missing_lesson"] += 0
                report_lines.append(f"  L{i+1} PROD ONLY: {pl[i].title[:60]}")
                issues.append(f"Extra on prod [{ch_name}] L{i+1}: {pl[i].title}")
                section_ok = False
                continue
            if i >= len(pl):
                stats["local_missing_lesson"] += 1
                report_lines.append(f"  L{i+1} LOCAL ONLY: {ll[i].title[:60]}")
                issues.append(f"Missing on prod [{ch_name}] L{i+1}: {ll[i].title}")
                section_ok = False
                continue

            l, p = ll[i], pl[i]
            flags: list[str] = []

            if l.title != p.title:
                flags.append("TITLE")
                stats["lesson_title_mismatch"] += 1
                issues.append(f"Title [{ch_name}] L{i+1}: local='{l.title}' prod='{p.title}'")

            if l.has_video and p.has_video:
                stats["video_both"] += 1
            elif l.has_video and not p.has_video:
                flags.append("NO_VIDEO_PROD")
                stats["video_local_only"] += 1
                issues.append(f"No video on prod [{ch_name}] L{i+1}: {l.title}")
            elif not l.has_video and p.has_video:
                flags.append("VIDEO_PROD_ONLY")
            else:
                stats["video_neither"] += 1
                if "[PENDING]" not in l.preview:
                    flags.append("NO_VIDEO_BOTH")

            if p.text_len == 0:
                flags.append("EMPTY_PROD")
                stats["prod_no_content"] += 1
                issues.append(f"Empty prod [{ch_name}] L{i+1}: {p.title}")

            if abs(l.text_len - p.text_len) > 50 and l.title == p.title:
                flags.append(f"TEXT_DIFF({l.text_len}vs{p.text_len})")
                stats["text_diff"] += 1

            if l.blocks != p.blocks:
                flags.append(f"BLOCKS({l.blocks}vs{p.blocks})")
                stats["blocks_diff"] += 1

            status = "OK" if not flags else " | ".join(flags)
            vid_l = "V" if l.has_video else "-"
            vid_p = "V" if p.has_video else "-"
            report_lines.append(
                f"  L{i+1:02d} [{status}] vid {vid_l}/{vid_p} blk {l.blocks}/{p.blocks} | {l.title[:55]}"
            )
            if flags and "TEXT_DIFF" in str(flags):
                report_lines.append(f"       local: {l.preview[:80]}...")
                report_lines.append(f"       prod:  {p.preview[:80]}...")

        if section_ok and len(ll) == len(pl):
            stats["sections_ok"] += 1

    print("\n".join(report_lines))

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Sections compared: {len(all_chapters)}")
    print(f"Sections fully matched (count+order): {stats['sections_ok']}")
    print(f"Title mismatches: {stats['lesson_title_mismatch']}")
    print(f"Lessons missing on PROD: {stats['local_missing_lesson']}")
    print(f"Lessons only on PROD: extra rows above")
    print(f"Video on LOCAL only (not synced): {stats['video_local_only']}")
    print(f"Video on BOTH: {stats['video_both']}")
    print(f"No video on either: {stats['video_neither']}")
    print(f"Text length diff >50 chars: {stats['text_diff']}")
    print(f"Block count diff: {stats['blocks_diff']}")
    print(f"Empty content on PROD: {stats['prod_no_content']}")
    print(f"Total issues logged: {len(issues)}")

    out = Path(__file__).parent / "audit-local-vs-prod.json"
    out.write_text(
        json.dumps({"stats": stats, "issues": issues}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nFull issue list: {out}")
    return 0


from pathlib import Path

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"API error: {exc}", file=sys.stderr)
        raise SystemExit(1)
