#!/usr/bin/env python3
"""Run an arbitrary command on the VPS over SSH. Reads scripts/deploy-production.env.

Usage:
    python vps-run.py "whoami && free -h"

Uses VPS_HOST / VPS_PORT / VPS_USER / VPS_PASSWORD from deploy-production.env.
For ad-hoc ops (discovery, swap, certbot, etc.) during a maintenance session.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SCRIPT_DIR = Path(__file__).resolve().parent
ENV_FILE = SCRIPT_DIR / "deploy-production.env"


def load_env() -> dict[str, str]:
    env = {"VPS_HOST": "162.4.176.43", "VPS_PORT": "24700", "VPS_USER": "root", "VPS_PASSWORD": ""}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def main() -> int:
    if len(sys.argv) < 2:
        print('usage: python vps-run.py "<command>"')
        print('       python vps-run.py --script <local_file.sh>')
        return 2

    env = load_env()
    if not env.get("VPS_PASSWORD"):
        print("VPS_PASSWORD missing in deploy-production.env")
        return 1

    import paramiko

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        env["VPS_HOST"],
        port=int(env["VPS_PORT"]),
        username=env["VPS_USER"],
        password=env["VPS_PASSWORD"],
        timeout=30,
    )
    try:
        if sys.argv[1] == "--script":
            local = Path(sys.argv[2])
            script = local.read_text(encoding="utf-8")
            sftp = client.open_sftp()
            remote = "/tmp/" + local.name
            with sftp.file(remote, "w") as f:
                f.write(script)
            sftp.close()
            command = f"chmod +x {remote} && bash {remote}"
        else:
            command = sys.argv[1]

        stdin, stdout, stderr = client.exec_command(command, get_pty=True, timeout=900)
        for line in iter(stdout.readline, ""):
            print(line, end="")
        err = stderr.read().decode()
        if err:
            print(err, file=sys.stderr)
        return stdout.channel.recv_exit_status()
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
