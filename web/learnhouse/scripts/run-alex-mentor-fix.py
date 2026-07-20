#!/usr/bin/env python3
"""Upload and run fix-alex-mentor-clone.sh on VPS2."""
from __future__ import annotations

import sys
from pathlib import Path

import paramiko

HERE = Path(__file__).resolve().parent
ENV_FILE = HERE / "deploy-alex-mentor.env"
FIX_SH = HERE / "fix-alex-mentor-clone.sh"


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

    remote = "/tmp/fix-alex-mentor-clone.sh"
    sftp = client.open_sftp()
    with sftp.file(remote, "w") as f:
        f.write(FIX_SH.read_text(encoding="utf-8"))
    sftp.close()

    cmd = (
        "export OLD_DOMAIN=learn.azzamedu.com NEW_DOMAIN=learn.alex-mentor.com "
        "OLD_TOP=azzamedu.com NEW_TOP=alex-mentor.com "
        "LEARNHOUSE_INSTALL_DIR=/root/.learnhouse/default && "
        f"chmod +x {remote} && bash {remote}"
    )
    print("Running fix...", flush=True)
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True, timeout=900)
    while True:
        line = stdout.readline()
        if not line:
            break
        sys.stdout.buffer.write(line.encode("utf-8", errors="replace") if isinstance(line, str) else line)
        # readline returns str with get_pty
        if isinstance(line, str):
            sys.stdout.buffer.write(line.encode("utf-8", errors="replace"))
        sys.stdout.flush()
    # Actually stdout.readline with get_pty returns str - simplify
    client.close()
    # Re-run cleaner
    return 0


if __name__ == "__main__":
    # cleaner streaming
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
    remote = "/tmp/fix-alex-mentor-clone.sh"
    sftp = client.open_sftp()
    with sftp.file(remote, "w") as f:
        f.write(FIX_SH.read_text(encoding="utf-8"))
    sftp.close()
    cmd = (
        "export OLD_DOMAIN=learn.azzamedu.com NEW_DOMAIN=learn.alex-mentor.com "
        "OLD_TOP=azzamedu.com NEW_TOP=alex-mentor.com "
        "LEARNHOUSE_INSTALL_DIR=/root/.learnhouse/default && "
        f"chmod +x {remote} && bash {remote}"
    )
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True, timeout=900)
    data = stdout.read().decode("utf-8", errors="replace")
    sys.stdout.buffer.write(data.encode("utf-8", errors="replace"))
    sys.stdout.flush()
    rc = stdout.channel.recv_exit_status()
    print(f"\nexit={rc}", flush=True)
    client.close()
    raise SystemExit(rc)
