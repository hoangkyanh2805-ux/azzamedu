#!/usr/bin/env python3
"""Deploy LearnHouse to VPS + seed Udemy clone course."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
BOOTSTRAP = SCRIPT_DIR / "vps-bootstrap.sh"
ENV_FILE = SCRIPT_DIR / "deploy-production.env"


def load_env() -> dict[str, str]:
    env = {
        "VPS_HOST": "162.4.176.43",
        "VPS_PORT": "24700",
        "VPS_USER": "root",
        "VPS_PASSWORD": "",
        "LEARNHOUSE_DOMAIN": "learn.hoa-homes.com",
        "LEARNHOUSE_ADMIN_EMAIL": "admin@hoa-homes.com",
        "LEARNHOUSE_ADMIN_PASSWORD": "AlphaElite-Prod-Learn-2026!",
        "LEARNHOUSE_ORG_SLUG": "alpha-elite",
        "LEARNHOUSE_ORG_ID": "1",
    }
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    for k in env:
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env


def ssh_bootstrap(env: dict[str, str]) -> bool:
    password = env.get("VPS_PASSWORD", "")
    if not password:
        return False
    try:
        import paramiko
    except ImportError:
        print("pip install paramiko")
        return False

    host = env["VPS_HOST"]
    port = int(env["VPS_PORT"])
    user = env["VPS_USER"]
    script = BOOTSTRAP.read_text(encoding="utf-8")

    print(f"SSH {user}@{host}:{port} - uploading bootstrap...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=user, password=password, timeout=30)

    sftp = client.open_sftp()
    remote = "/tmp/vps-bootstrap.sh"
    with sftp.file(remote, "w") as f:
        f.write(script)
    sftp.close()

    remote_env = (
        f"export LEARNHOUSE_DOMAIN={env['LEARNHOUSE_DOMAIN']} "
        f"LEARNHOUSE_ADMIN_EMAIL={env['LEARNHOUSE_ADMIN_EMAIL']} "
        f"LEARNHOUSE_ADMIN_PASSWORD='{env['LEARNHOUSE_ADMIN_PASSWORD']}' "
        f"LEARNHOUSE_ORG_SLUG={env['LEARNHOUSE_ORG_SLUG']}"
    )
    cmd = f"{remote_env} && chmod +x {remote} && bash {remote}"
    print("Running bootstrap on VPS (5–15 min)...")
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True)
    for line in iter(stdout.readline, ""):
        print(line, end="")
    err = stderr.read().decode()
    if err:
        print(err, file=sys.stderr)
    code = stdout.channel.recv_exit_status()
    client.close()
    if code != 0:
        print(f"Bootstrap exit code {code}", file=sys.stderr)
        return False
    print("VPS bootstrap OK")
    return True


def wait_for_site(domain: str, max_minutes: int = 25) -> bool:
    import requests

    targets = [
        f"https://{domain}",
        f"https://{domain}/api/v1/health",
        f"http://{domain}",
    ]
    deadline = time.time() + max_minutes * 60
    n = 0
    while time.time() < deadline:
        n += 1
        for t in targets:
            try:
                r = requests.get(t, timeout=12, allow_redirects=True)
                if r.status_code < 500:
                    print(f"Site up: {t} ({r.status_code})")
                    return True
            except requests.RequestException:
                pass
        print(f"Waiting for https://{domain} ... ({n})")
        time.sleep(20)
    return False


def seed_course(env: dict[str, str]) -> int:
    domain = env["LEARNHOUSE_DOMAIN"]
    os.environ["LEARNHOUSE_API"] = f"https://{domain}/api/v1"
    os.environ["LEARNHOUSE_ADMIN_EMAIL"] = env["LEARNHOUSE_ADMIN_EMAIL"]
    os.environ["LEARNHOUSE_ADMIN_PASSWORD"] = env["LEARNHOUSE_ADMIN_PASSWORD"]
    os.environ["LEARNHOUSE_ORG_SLUG"] = env["LEARNHOUSE_ORG_SLUG"]
    os.environ["LEARNHOUSE_ORG_ID"] = env["LEARNHOUSE_ORG_ID"]

    seed = SCRIPT_DIR / "seed-udemy-clone.py"
    print(f"\nSeeding course to https://{domain} ...")
    r = subprocess.run([sys.executable, "-u", str(seed)], cwd=str(SCRIPT_DIR))
    return r.returncode


def print_paste_instructions(env: dict[str, str]) -> None:
    domain = env["LEARNHOUSE_DOMAIN"]
    print("\n" + "=" * 60)
    print("PASTE VAO OneDash SSH Terminal (neu chua co VPS_PASSWORD):")
    print("=" * 60)
    print(
        f"curl -fsSL -o /tmp/bootstrap.sh && "
        f"Or: copy file scripts/vps-bootstrap.sh len VPS\n"
    )
    print("Hoac chay truc tiep:")
    print(
        f"export LEARNHOUSE_DOMAIN={domain} "
        f"LEARNHOUSE_ADMIN_EMAIL={env['LEARNHOUSE_ADMIN_EMAIL']} "
        f"LEARNHOUSE_ADMIN_PASSWORD='{env['LEARNHOUSE_ADMIN_PASSWORD']}' "
        f"LEARNHOUSE_ORG_SLUG={env['LEARNHOUSE_ORG_SLUG']}"
    )
    print(f"bash /tmp/vps-bootstrap.sh")
    print("=" * 60)


def main() -> int:
    seed_only = "--seed-only" in sys.argv
    env = load_env()
    domain = env["LEARNHOUSE_DOMAIN"]

    print(f"=== Deploy LearnHouse -> https://{domain} ===")
    print(f"DNS target: {env['VPS_HOST']}")

    if not seed_only:
        if not ssh_bootstrap(env):
            print("\nSSH auto failed (can VPS_PASSWORD trong deploy-production.env)")
            print_paste_instructions(env)
            if not wait_for_site(domain):
                print("Timeout - chua thay site. Chay bootstrap tren VPS truoc.")
                return 1
        else:
            if not wait_for_site(domain, max_minutes=10):
                print("Bootstrap xong nhung site chua len - doi them hoac xem logs: npx learnhouse logs")
                return 1

    if seed_course(env) != 0:
        return 1
    print(f"\n=== XONG ===\nhttps://{domain}\nLogin: {env['LEARNHOUSE_ADMIN_EMAIL']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
