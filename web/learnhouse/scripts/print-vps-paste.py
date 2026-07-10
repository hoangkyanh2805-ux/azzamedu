#!/usr/bin/env python3
"""Print one block to paste into OneDash SSH Terminal."""
import base64
from pathlib import Path

p = Path(__file__).resolve().parent / "vps-bootstrap.sh"
b = base64.b64encode(p.read_bytes()).decode()
print("=== COPY ALL BELOW INTO OneDash SSH Terminal ===")
print(f"echo '{b}' | base64 -d > /tmp/vps-bootstrap.sh")
print("chmod +x /tmp/vps-bootstrap.sh")
print(
    "export LEARNHOUSE_DOMAIN=learn.azzamedu.com "
    "LEARNHOUSE_ADMIN_EMAIL=admin@hoa-homes.com "
    "LEARNHOUSE_ADMIN_PASSWORD='AlphaElite-Prod-Learn-2026!' "
    "LEARNHOUSE_ORG_SLUG=alpha-elite"
)
print("bash /tmp/vps-bootstrap.sh")
print("=== END ===")
