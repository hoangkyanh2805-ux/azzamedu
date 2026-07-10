#!/usr/bin/env python3
"""Deploy telegram-bot/miniapp to LearnHouse VPS (static files + nginx).

Reads web/learnhouse/scripts/deploy-production.env for SSH credentials.

Usage:
  cd telegram-bot
  python scripts/deploy-miniapp-vps.py
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MINIAPP_DIR = SCRIPT_DIR.parent / "miniapp"
ENV_FILE = SCRIPT_DIR.parent.parent / "web" / "learnhouse" / "scripts" / "deploy-production.env"
REMOTE_ROOT = "/var/www/alpha-elite-miniapp"


def load_env() -> dict[str, str]:
    env = {
        "VPS_HOST": "162.4.176.43",
        "VPS_PORT": "24700",
        "VPS_USER": "root",
        "VPS_PASSWORD": "",
        "LEARNHOUSE_DOMAIN": "learn.azzamedu.com",
    }
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def upload_tree(sftp, local: Path, remote: str) -> None:
    try:
        sftp.stat(remote)
    except OSError:
        sftp.mkdir(remote)

    for item in local.iterdir():
        if item.name in {".git", "config.js"}:
            continue
        rpath = f"{remote}/{item.name}"
        if item.is_dir():
            upload_tree(sftp, item, rpath)
        else:
            sftp.put(str(item), rpath)


def main() -> int:
    if not MINIAPP_DIR.exists():
        print(f"FAIL: {MINIAPP_DIR} not found")
        return 1

    env = load_env()
    password = env.get("VPS_PASSWORD", "")
    if not password:
        print(f"FAIL: VPS_PASSWORD missing in {ENV_FILE}")
        return 1

    try:
        import paramiko
    except ImportError:
        print("pip install paramiko")
        return 1

    domain = env["LEARNHOUSE_DOMAIN"]
    host, port, user = env["VPS_HOST"], int(env["VPS_PORT"]), env["VPS_USER"]

    print(f"SSH {user}@{host}:{port}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=user, password=password, timeout=90)

    try:
        sftp = client.open_sftp()
        print(f"Upload → {REMOTE_ROOT}")
        upload_tree(sftp, MINIAPP_DIR, REMOTE_ROOT)
        remote_config = f"{REMOTE_ROOT}/js/config.js"
        try:
            sftp.stat(remote_config)
        except OSError:
            sftp.put(str(MINIAPP_DIR / "js" / "config.example.js"), remote_config)
            print("Created js/config.js from example — set supabase anon key on VPS")
        sftp.close()

        setup_sh = f"""#!/bin/bash
set -e
REMOTE_ROOT="{REMOTE_ROOT}"
NGINX_CT=$(docker ps --format '{{{{.Names}}}}' | grep -i nginx | head -1 || true)
COMPOSE_DIR=""
if [ -n "$NGINX_CT" ]; then
  COMPOSE_DIR=$(docker inspect "$NGINX_CT" --format '{{{{index .Config.Labels "com.docker.compose.project.working_dir"}}}}' 2>/dev/null || true)
fi
if [ -z "$COMPOSE_DIR" ] || [ ! -f "$COMPOSE_DIR/docker-compose.yml" ]; then
  COMPOSE_DIR=$(find /root /opt /home -maxdepth 5 -name docker-compose.yml 2>/dev/null | head -1 | xargs dirname 2>/dev/null || true)
fi
echo "nginx container: $NGINX_CT"
echo "compose dir: $COMPOSE_DIR"
if [ -z "$COMPOSE_DIR" ] || [ ! -f "$COMPOSE_DIR/extra/nginx.prod.conf" ]; then
  echo "WARN: nginx.prod.conf not found — static files at $REMOTE_ROOT"
  exit 0
fi
CONF="$COMPOSE_DIR/extra/nginx.prod.conf"
if ! grep -q 'location /miniapp/' "$CONF"; then
  cp "$CONF" "$CONF.bak-miniapp-$(date +%s)"
  cat >> "$CONF" << 'NGINX_EOF'

    location /miniapp/ {{
        alias {REMOTE_ROOT}/;
        index index.html;
    }}
NGINX_EOF
  echo "Patched $CONF"
fi
if ! grep -q '{REMOTE_ROOT}' "$COMPOSE_DIR/docker-compose.yml" 2>/dev/null; then
  sed -i 's|./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro|./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro\\n      - {REMOTE_ROOT}:{REMOTE_ROOT}:ro|' "$COMPOSE_DIR/docker-compose.yml" || true
fi
cd "$COMPOSE_DIR" && docker compose up -d --force-recreate nginx
docker exec "$NGINX_CT" nginx -t
echo "OK https://{domain}/miniapp/"
"""
        sftp = client.open_sftp()
        remote_sh = "/tmp/deploy-miniapp.sh"
        with sftp.file(remote_sh, "w") as f:
            f.write(setup_sh)
        sftp.close()

        stdin, stdout, stderr = client.exec_command(f"chmod +x {remote_sh} && bash {remote_sh}", timeout=300)
        for line in iter(stdout.readline, ""):
            print(line, end="")
        err = stderr.read().decode()
        if err:
            print(err, file=sys.stderr)
        code = stdout.channel.recv_exit_status()
        print(f"\nMini App: https://{domain}/miniapp/")
        return code
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
