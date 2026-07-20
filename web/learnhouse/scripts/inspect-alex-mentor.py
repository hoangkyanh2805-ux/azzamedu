#!/usr/bin/env python3
"""Locate LearnHouse install + azzamedu refs on alex-mentor VPS."""
from __future__ import annotations

import sys
from pathlib import Path

import paramiko

HERE = Path(__file__).resolve().parent
ENV_FILE = HERE / "deploy-alex-mentor.env"


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def run(client: paramiko.SSHClient, cmd: str) -> str:
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True, timeout=180)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    # Avoid Windows console UnicodeEncodeError
    sys.stdout.buffer.write((out + (err or "")).encode("utf-8", errors="replace"))
    sys.stdout.buffer.write(b"\n")
    return out


def main() -> int:
    env = load_env()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        env["VPS_HOST"],
        port=int(env["VPS_PORT"]),
        username=env["VPS_USER"],
        password=env["VPS_PASSWORD"],
        timeout=30,
    )
    print("SSH OK", flush=True)

    cmds = [
        "docker inspect learnhouse-app-9f55066e --format '{{json .Mounts}}' | python3 -m json.tool 2>/dev/null || docker inspect learnhouse-app-9f55066e --format '{{json .Mounts}}'",
        "docker inspect learnhouse-app-9f55066e --format '{{range .Config.Env}}{{println .}}{{end}}' | grep -Ei 'DOMAIN|URL|MEDIA|CONTENT|NEXTAUTH|HOST' || true",
        "docker inspect learnhouse-nginx-9f55066e --format '{{json .Mounts}}'",
        "docker volume ls",
        "find /root /opt /var/lib/docker/volumes /home -maxdepth 4 \\( -name '.env' -o -name 'learnhouse.config.json' -o -name 'docker-compose*.yml' \\) 2>/dev/null | head -80",
        "grep -rIl --exclude-dir=proc --exclude-dir=sys --exclude-dir=node_modules -- 'learn.azzamedu.com' /root /opt /etc 2>/dev/null | head -50",
        "docker exec learnhouse-app-9f55066e sh -c 'env | grep -Ei \"DOMAIN|URL|MEDIA|CONTENT|NEXTAUTH\" | sort' 2>/dev/null || true",
        "docker exec learnhouse-app-9f55066e sh -c 'ls -la / | head -40; ls -la /app 2>/dev/null | head; ls -la /content 2>/dev/null | head; ls -la /data 2>/dev/null | head; find / -maxdepth 3 -type d \\( -iname \"*media*\" -o -iname \"*upload*\" -o -iname \"*content*\" \\) 2>/dev/null | head -40'",
    ]
    for c in cmds:
        print("\n====", c[:90], flush=True)
        run(client, "set +e; " + c)

    client.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
