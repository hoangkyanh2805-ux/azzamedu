#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

import paramiko

HERE = Path(__file__).resolve().parent
ENV_FILE = HERE / "deploy-alex-mentor.env"
SCRIPT = HERE / "fix-alex-mentor-ssl.sh"


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


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
    remote = "/tmp/fix-alex-mentor-ssl.sh"
    sftp = client.open_sftp()
    with sftp.file(remote, "w") as f:
        f.write(SCRIPT.read_text(encoding="utf-8"))
    sftp.close()
    cmd = f"chmod +x {remote} && LEARNHOUSE_DOMAIN=learn.alex-mentor.com bash {remote}"
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True, timeout=900)
    data = stdout.read().decode("utf-8", errors="replace")
    sys.stdout.buffer.write(data.encode("utf-8", errors="replace"))
    sys.stdout.flush()
    rc = stdout.channel.recv_exit_status()
    print(f"\nexit={rc}", flush=True)
    client.close()
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
