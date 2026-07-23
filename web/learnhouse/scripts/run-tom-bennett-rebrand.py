#!/usr/bin/env python3
"""SSH: rebrand LearnHouse clone alex-mentor -> tom-edu (skill learnhouse-vps-clone-rebrand)."""
from __future__ import annotations

import sys
from pathlib import Path

import paramiko

HERE = Path(__file__).resolve().parent
ENV_FILE = HERE / "deploy-tom-bennett.env"
FIX_SH = HERE / "fix-alex-mentor-clone.sh"
SSL_SH = HERE / "fix-alex-mentor-ssl.sh"


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def run(client: paramiko.SSHClient, cmd: str, timeout: int = 900) -> int:
    print(f"\n>>> {cmd[:100]}...", flush=True)
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True, timeout=timeout)
    data = stdout.read().decode("utf-8", errors="replace")
    sys.stdout.buffer.write(data.encode("utf-8", errors="replace"))
    sys.stdout.flush()
    return stdout.channel.recv_exit_status()


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

    sftp = client.open_sftp()
    for local, remote in (
        (FIX_SH, "/tmp/fix-clone-rebrand.sh"),
        (SSL_SH, "/tmp/fix-ssl-rebrand.sh"),
    ):
        with sftp.file(remote, "w") as f:
            f.write(local.read_text(encoding="utf-8"))
    sftp.close()

    old = env.get("OLD_DOMAIN", "learn.alex-mentor.com")
    new = env.get("LEARNHOUSE_DOMAIN", "learn.tom-edu.com")
    old_top = env.get("OLD_TOP", "alex-mentor.com")
    new_top = env.get("NEW_TOP", "tom-edu.com")
    install = env.get("LEARNHOUSE_INSTALL_DIR", "/root/.learnhouse/default")

    rc1 = run(
        client,
        f"export OLD_DOMAIN={old} NEW_DOMAIN={new} OLD_TOP={old_top} NEW_TOP={new_top} "
        f"LEARNHOUSE_INSTALL_DIR={install} && chmod +x /tmp/fix-clone-rebrand.sh && "
        f"bash /tmp/fix-clone-rebrand.sh",
    )
    print(f"clone_fix_exit={rc1}", flush=True)

    rc2 = run(
        client,
        f"export LEARNHOUSE_DOMAIN={new} ACME_EMAIL=admin@tom-edu.com && "
        f"chmod +x /tmp/fix-ssl-rebrand.sh && bash /tmp/fix-ssl-rebrand.sh",
    )
    print(f"ssl_fix_exit={rc2}", flush=True)

    run(
        client,
        f"""
set +e
echo '=== verify ==='
curl -sI http://{new}/ | sed -n '1,12p'
curl -skI https://{new}/ | sed -n '1,12p'
curl -skL https://{new}/ 2>/dev/null | grep -oE 'https?://[^" ]+' | grep -E 'alex-mentor|azzamedu|tom-edu|content|og:image|favicon' | sort -u | head -30
docker exec learnhouse-app-9f55066e sh -c 'env | grep -Ei "DOMAIN|NEXTAUTH_URL|BACKEND|COOKIE|TOP" | sort' || true
""",
    )
    client.close()
    return 0 if rc1 == 0 and rc2 == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
