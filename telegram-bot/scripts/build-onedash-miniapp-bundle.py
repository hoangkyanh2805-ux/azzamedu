#!/usr/bin/env python3
"""Build scripts/onedash-install-miniapp.sh — paste & run on iNET OneDash terminal.

Usage:
  cd telegram-bot
  python scripts/build-onedash-miniapp-bundle.py
"""

from __future__ import annotations

import base64
import io
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MINIAPP = ROOT / "miniapp"
OUT = Path(__file__).resolve().parent / "onedash-install-miniapp.sh"

INCLUDE = [
    "index.html",
    "css/shop.css",
    "js/catalog.js",
    "js/app.js",
    "js/config.js",
    "js/config.example.js",
]


def _tar_b64() -> str:
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for rel in INCLUDE:
            path = MINIAPP / rel
            if not path.exists():
                raise FileNotFoundError(path)
            tar.add(path, arcname=f"miniapp/{rel}")
    return base64.b64encode(buf.getvalue()).decode("ascii")


def main() -> None:
    payload = _tar_b64()
    script = f"""#!/bin/bash
# Alpha Elite Telegram Mini App — install on LearnHouse VPS (OneDash terminal)
set -euo pipefail
REMOTE_ROOT="/var/www/alpha-elite-miniapp"
TMP="/tmp/ae-miniapp.tgz.b64"

echo "=== Alpha Elite Mini App install ==="
mkdir -p "$REMOTE_ROOT"
cat > "$TMP" << 'B64_EOF'
{payload}
B64_EOF

base64 -d "$TMP" | tar -xzf - -C /tmp
rm -f "$TMP"
cp -a /tmp/miniapp/. "$REMOTE_ROOT/"
rm -rf /tmp/miniapp
echo "Files installed to $REMOTE_ROOT"

NGINX_CT=$(docker ps --format '{{{{.Names}}}}' | grep -i nginx | head -1 || true)
COMPOSE_DIR=""
if [ -n "$NGINX_CT" ]; then
  COMPOSE_DIR=$(docker inspect "$NGINX_CT" --format '{{{{index .Config.Labels "com.docker.compose.project.working_dir"}}}}' 2>/dev/null || true)
fi
if [ -z "$COMPOSE_DIR" ] || [ ! -f "$COMPOSE_DIR/docker-compose.yml" ]; then
  COMPOSE_DIR=$(find /root /opt /home -maxdepth 5 -name docker-compose.yml 2>/dev/null | head -1 | xargs dirname 2>/dev/null || true)
fi
echo "nginx: $NGINX_CT"
echo "compose: $COMPOSE_DIR"

if [ -z "$COMPOSE_DIR" ] || [ ! -f "$COMPOSE_DIR/extra/nginx.prod.conf" ]; then
  echo "WARN: nginx.prod.conf not found — add location /miniapp/ manually"
  exit 0
fi

CONF="$COMPOSE_DIR/extra/nginx.prod.conf"
if ! grep -q 'location /miniapp/' "$CONF"; then
  cp "$CONF" "$CONF.bak-miniapp-$(date +%s)"
  cat >> "$CONF" << 'NGINX_EOF'

    location /miniapp/ {{
        alias /var/www/alpha-elite-miniapp/;
        index index.html;
    }}
NGINX_EOF
  echo "Patched $CONF"
fi

if ! grep -q '/var/www/alpha-elite-miniapp' "$COMPOSE_DIR/docker-compose.yml" 2>/dev/null; then
  sed -i 's|./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro|./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro\\n      - /var/www/alpha-elite-miniapp:/var/www/alpha-elite-miniapp:ro|' \\
    "$COMPOSE_DIR/docker-compose.yml" || true
fi

cd "$COMPOSE_DIR"
docker compose up -d --force-recreate nginx
docker exec "$NGINX_CT" nginx -t
echo ""
echo "DONE: https://learn.azzamedu.com/miniapp/"
echo "Test: curl -sI https://learn.azzamedu.com/miniapp/ | head -5"
"""
    OUT.write_text(script, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
    print("OneDash: paste entire file contents and run: bash onedash-install-miniapp.sh")


if __name__ == "__main__":
    main()
