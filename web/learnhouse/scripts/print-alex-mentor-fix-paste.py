#!/usr/bin/env python3
"""Emit OneDash paste block for alex-mentor clone fix."""
from __future__ import annotations

import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
script = (HERE / "fix-alex-mentor-clone.sh").read_bytes()
b64 = base64.b64encode(script).decode()
out = HERE / "onedash-fix-alex-mentor.txt"
body = "\n".join(
    [
        "=== PASTE ALL INTO OneDash SSH Terminal (VPS2 162.4.176.68) ===",
        f"echo '{b64}' | base64 -d > /tmp/fix-alex-mentor-clone.sh",
        "chmod +x /tmp/fix-alex-mentor-clone.sh",
        "export OLD_DOMAIN=learn.azzamedu.com NEW_DOMAIN=learn.alex-mentor.com LEARNHOUSE_INSTALL_DIR=/opt/learnhouse",
        "bash /tmp/fix-alex-mentor-clone.sh",
        "=== END ===",
        "",
    ]
)
out.write_text(body, encoding="utf-8")
print(out)
print("b64_len", len(b64))
