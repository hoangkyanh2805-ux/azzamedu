#!/usr/bin/env python3
"""Build Elementor page JSON from an HTML source (single HTML widget)."""

from __future__ import annotations

import argparse
import json
import re
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_HTML = ROOT / "html" / "homepage-dark-gold.html"
DEFAULT_OUT = Path(__file__).resolve().parent.parent / "elementor-alpha-elite-homepage.json"


def _id() -> str:
    return uuid.uuid4().hex[:7]


def extract_main_html(raw: str) -> str:
    """Extract header + main + footer body content for HTML widget."""
    # Drop <script> blocks (VSL — add via Elementor video widget later)
    raw = re.sub(r"<script\b[^>]*>.*?</script>", "", raw, flags=re.DOTALL | re.IGNORECASE)
    # Take from header through footer (full page chrome in one widget)
    start = raw.find("<header")
    end = raw.find("</html>")
    if start == -1 or end == -1:
        raise ValueError("Could not find header/html end in homepage HTML")
    chunk = raw[start:end]
    # WP link placeholders — user replaces in Elementor or via find-replace after import
    replacements = {
        'href="gameplan-preview.html"': 'href="/gameplan"',
        'href="apprentice-preview.html"': 'href="/apprentice"',
        'href="vip-preview.html"': 'href="/vip"',
        'href="quant-desk-preview.html"': 'href="/quant-desk"',
        'href="gameplan-thank-you.html"': 'href="/gameplan-thank-you"',
        'action="gameplan-thank-you.html"': 'action="/gameplan-thank-you"',
        'href="homepage-dark-gold.html"': 'href="/"',
        'href="alpha-elite-tokens.css"': 'href="#" data-ae-tokens="1"',
    }
    for old, new in replacements.items():
        chunk = chunk.replace(old, new)
    return chunk.strip()


def build_elementor_json(html_content: str, title: str) -> dict:
    section_id = _id()
    col_id = _id()
    widget_id = _id()
    return {
        "title": title,
        "type": "page",
        "version": "0.4",
        "page_settings": {
            "hide_title": "yes",
            "template": "elementor_canvas",
        },
        "content": [
            {
                "id": section_id,
                "elType": "section",
                "isInner": False,
                "settings": {
                    "layout": "full_width",
                    "gap": "no",
                    "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
                },
                "elements": [
                    {
                        "id": col_id,
                        "elType": "column",
                        "isInner": False,
                        "settings": {"_column_size": 100},
                        "elements": [
                            {
                                "id": widget_id,
                                "elType": "widget",
                                "widgetType": "html",
                                "settings": {"html": html_content},
                                "elements": [],
                            }
                        ],
                    }
                ],
            }
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Elementor JSON from HTML file")
    parser.add_argument("--input", type=Path, default=DEFAULT_HTML, help="Source HTML path")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT, help="Output JSON path")
    parser.add_argument("--title", type=str, default="Alpha Elite Homepage", help="Elementor template title")
    args = parser.parse_args()

    raw = args.input.read_text(encoding="utf-8")
    html_content = extract_main_html(raw)
    data = build_elementor_json(html_content, args.title)
    args.output.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.output} ({len(html_content)} chars)")


if __name__ == "__main__":
    main()
