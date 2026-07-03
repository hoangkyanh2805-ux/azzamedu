#!/usr/bin/env python3
"""Build native Elementor JSON (multi-section, drag-drop editable) for Homepage v2."""

from __future__ import annotations

import json
import uuid
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "elementor-alpha-elite-homepage-v2-native.json"


def _id() -> str:
    return uuid.uuid4().hex[:7]


def heading(text: str, size: str = "xl") -> dict:
    return {"id": _id(), "elType": "widget", "widgetType": "heading", "settings": {"title": text, "size": size}, "elements": []}


def text_editor(text: str) -> dict:
    return {"id": _id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": text}, "elements": []}


def button(text: str, link: str = "#", style: str = "default") -> dict:
    return {
        "id": _id(),
        "elType": "widget",
        "widgetType": "button",
        "settings": {"text": text, "button_type": style, "link": {"url": link}},
        "elements": [],
    }


def divider() -> dict:
    return {"id": _id(), "elType": "widget", "widgetType": "divider", "settings": {}, "elements": []}


def icon_box(title: str, desc: str) -> dict:
    return {
        "id": _id(),
        "elType": "widget",
        "widgetType": "icon-box",
        "settings": {"title_text": title, "description_text": desc},
        "elements": [],
    }


def accordion(items: list[tuple[str, str]]) -> dict:
    entries = []
    for i, (q, a) in enumerate(items, 1):
        entries.append({"_id": _id(), "tab_title": q, "tab_content": a})
    return {
        "id": _id(),
        "elType": "widget",
        "widgetType": "accordion",
        "settings": {"accordion": entries},
        "elements": [],
    }


def section_single(section_id: str, widgets: list[dict]) -> dict:
    return {
        "id": _id(),
        "elType": "section",
        "isInner": False,
        "settings": {"css_id": section_id},
        "elements": [
            {"id": _id(), "elType": "column", "isInner": False, "settings": {"_column_size": 100}, "elements": widgets}
        ],
    }


def section_columns(section_id: str, columns: list[tuple[int, list[dict]]]) -> dict:
    cols = []
    for size, widgets in columns:
        cols.append(
            {"id": _id(), "elType": "column", "isInner": False, "settings": {"_column_size": size}, "elements": widgets}
        )
    return {"id": _id(), "elType": "section", "isInner": False, "settings": {"css_id": section_id}, "elements": cols}


def build() -> dict:
    content = []

    # Hero 2-column
    content.append(
        section_columns(
            "hero-main",
            [
                (
                    58,
                    [
                        text_editor("PRIVATE XAUUSD OPERATING SYSTEM"),
                        heading("You don't need another signal. You need a system that stops emotional trading."),
                        text_editor("Education, structured trade process, and accountability around a 2% risk framework."),
                        button("Get The 2% Rule Gameplan", "#get-gameplan", "info"),
                        text_editor("Trading involves risk. Educational content only."),
                    ],
                ),
                (
                    42,
                    [
                        heading("Desk Preview", "medium"),
                        text_editor("Use an image/video widget here for dashboard preview."),
                    ],
                ),
            ],
        )
    )

    # Not signal group
    content.append(
        section_columns(
            "not-signal-group",
            [
                (
                    100,
                    [
                        heading("Not a signal feed. An operating standard."),
                        text_editor("Most traders fail from no process, not from missing alerts."),
                    ],
                ),
                (
                    50,
                    [heading("What We Are Not", "medium"), text_editor("Random alerts<br>FOMO entries<br>Profit-claim marketing")],
                ),
                (
                    50,
                    [heading("What We Are", "medium"), text_editor("2% risk framework<br>Daily/weekly SOPs<br>Education-first desk rhythm")],
                ),
            ],
        )
    )

    # Video
    content.append(
        section_single(
            "video-demo",
            [
                heading("See the desk before you join"),
                text_editor("Drop Elementor Video widget here (YouTube unlisted)."),
                button("Get The 2% Rule Gameplan", "#get-gameplan", "info"),
            ],
        )
    )

    # What you learn
    content.append(
        section_columns(
            "what-you-learn",
            [
                (100, [heading("What you actually build"), text_editor("Core capabilities, not hype.")]),
                (33, [icon_box("Risk Framework", "Define size before entry and protect downside.")]),
                (33, [icon_box("Execution SOP", "Pre-trade and post-trade checklists for consistency.")]),
                (34, [icon_box("Review Loop", "Weekly review and journal-driven adjustments.")]),
            ],
        )
    )

    # How it works
    content.append(
        section_columns(
            "how-it-works",
            [
                (100, [heading("How the system works")]),
                (25, [icon_box("Step 1", "Get the 2% Rule Gameplan")]),
                (25, [icon_box("Step 2", "Install Apprentice SOPs")]),
                (25, [icon_box("Step 3", "Operate in VIP desk cadence")]),
                (25, [icon_box("Step 4", "Apply to Quant / 1:1")]),
            ],
        )
    )

    # Offers
    content.append(
        section_columns(
            "offers",
            [
                (100, [heading("Choose your next step")]),
                (
                    33,
                    [
                        heading("Apprentice Operating Course", "medium"),
                        text_editor("$297 one-time"),
                        button("Start Apprentice Course", "/checkout-apprentice/", "info"),
                    ],
                ),
                (
                    33,
                    [
                        heading("VIP Private Desk Monthly", "medium"),
                        text_editor("$149 / month"),
                        button("Start VIP Private Desk", "/checkout-vip-monthly/", "success"),
                    ],
                ),
                (
                    34,
                    [
                        heading("VIP Private Desk Annual", "medium"),
                        text_editor("$1,290 / year"),
                        button("Start VIP Private Desk", "/checkout-vip-annual/", "success"),
                    ],
                ),
            ],
        )
    )

    # Form section placeholder
    content.append(
        section_single(
            "get-gameplan",
            [
                heading("Get The 2% Rule Gameplan"),
                text_editor("Add Elementor Form widget here: Email, First Name, Experience."),
                text_editor("Button label: Send Me The Gameplan"),
                text_editor("Trading involves risk. Educational content only."),
            ],
        )
    )

    # FAQ
    content.append(
        section_single(
            "faq",
            [
                heading("Frequently asked"),
                accordion(
                    [
                        ("Is this a signal group?", "No. Alpha Elite is an education-first operating system."),
                        ("Do you guarantee profits?", "No. Trading involves risk and outcomes vary."),
                        ("Is this investment advice?", "No. Educational support only."),
                        ("How do I start?", "Begin with the free Gameplan, then Apprentice."),
                    ]
                ),
            ],
        )
    )

    # Final CTA
    content.append(
        section_single(
            "final-cta",
            [
                heading("Build your trading process before your next trade"),
                button("Get The 2% Rule Gameplan", "#get-gameplan", "info"),
            ],
        )
    )

    # Risk footer
    content.append(
        section_single(
            "risk",
            [
                divider(),
                text_editor(
                    "RISK WARNING: Trading forex, crypto, and leveraged products involves substantial risk of loss. Educational content only. Not investment advice."
                ),
            ],
        )
    )

    return {
        "title": "Alpha Elite Homepage V2 Native",
        "type": "page",
        "version": "0.4",
        "page_settings": {"hide_title": "yes", "template": "elementor_canvas"},
        "content": content,
    }


def main() -> None:
    data = build()
    OUT.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()

