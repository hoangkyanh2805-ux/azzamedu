"""Load message templates from bot/templates/*.md"""

from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent


def load_template(name: str) -> str:
    path = TEMPLATES_DIR / f"{name}.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()
