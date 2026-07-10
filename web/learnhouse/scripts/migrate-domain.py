#!/usr/bin/env python3
"""Migrate the LearnHouse production domain on the VPS over SSH.

Reads VPS credentials + target domain from `scripts/deploy-production.env`
(same file used by deploy-vps.py). Never commit that file.

Usage:
    python migrate-domain.py --inspect   # read-only: show how/where the domain is stored
    python migrate-domain.py             # apply: backup, replace old->new domain, restart, doctor

Old domain defaults to `learn.hoa-homes.com`; new domain = LEARNHOUSE_DOMAIN
from the env file (currently `learn.azzamedu.com`). Override either with env vars
OLD_DOMAIN / LEARNHOUSE_DOMAIN.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ENV_FILE = SCRIPT_DIR / "deploy-production.env"
MIGRATE_SH = SCRIPT_DIR / "migrate-domain.sh"
OLD_DOMAIN_DEFAULT = "learn.hoa-homes.com"


def load_env() -> dict[str, str]:
    env = {
        "VPS_HOST": "162.4.176.43",
        "VPS_PORT": "24700",
        "VPS_USER": "root",
        "VPS_PASSWORD": "",
        "LEARNHOUSE_DOMAIN": "learn.azzamedu.com",
        "LEARNHOUSE_INSTALL_DIR": "/opt/learnhouse",
        "OLD_DOMAIN": OLD_DOMAIN_DEFAULT,
    }
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    for k in list(env):
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env


def connect(env: dict[str, str]):
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
    return client


def run(client, cmd: str) -> int:
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True)
    for line in iter(stdout.readline, ""):
        print(line, end="")
    err = stderr.read().decode()
    if err:
        print(err, file=sys.stderr)
    return stdout.channel.recv_exit_status()


def do_inspect(client, env: dict[str, str]) -> int:
    d = env["LEARNHOUSE_INSTALL_DIR"]
    old = env["OLD_DOMAIN"]
    # Redact values of keys that look like secrets so credentials don't leak into logs.
    redact = (
        r"sed -E 's/(\"[^\"]*(password|secret|key|token)[^\"]*\"[[:space:]]*:[[:space:]]*\")[^\"]*\"/\1***\"/gI; "
        r"s/((PASSWORD|SECRET|KEY|TOKEN)[A-Z_]*=).*/\1***/I'"
    )
    cmd = (
        f"set +e; "
        f"echo '=== ls {d} ==='; ls -la {d}; "
        f"echo; echo '=== learnhouse.config.json (secrets redacted) ==='; "
        f"cat {d}/learnhouse.config.json 2>/dev/null | {redact} || echo '(missing)'; "
        f"echo; echo '=== .env (secrets redacted) ==='; cat {d}/.env 2>/dev/null | {redact} || echo '(no .env)'; "
        f"echo; echo '=== docker-compose files ==='; ls {d}/docker-compose* 2>/dev/null || echo '(none)'; "
        f"echo; echo '=== files referencing {old} ==='; "
        f"grep -rIl --exclude-dir=node_modules --exclude-dir=.git -- {old} {d} 2>/dev/null || echo '(none)'; "
        f"echo; echo '=== containers ==='; docker ps || true"
    )
    return run(client, cmd)


def do_apply(client, env: dict[str, str]) -> int:
    old = env["OLD_DOMAIN"]
    new = env["LEARNHOUSE_DOMAIN"]
    install = env["LEARNHOUSE_INSTALL_DIR"]
    if old == new:
        print(f"OLD_DOMAIN == NEW_DOMAIN ({old}) — nothing to do.")
        return 1

    script = MIGRATE_SH.read_text(encoding="utf-8")
    sftp = client.open_sftp()
    remote = "/tmp/migrate-domain.sh"
    with sftp.file(remote, "w") as f:
        f.write(script)
    sftp.close()

    print(f"Migrating {old} -> {new} on {env['VPS_HOST']} ...")
    cmd = (
        f"export OLD_DOMAIN={old} NEW_DOMAIN={new} LEARNHOUSE_INSTALL_DIR={install} && "
        f"chmod +x {remote} && bash {remote}"
    )
    return run(client, cmd)


def main() -> int:
    inspect = "--inspect" in sys.argv
    env = load_env()

    if not env.get("VPS_PASSWORD"):
        print("VPS_PASSWORD is empty. Fill scripts/deploy-production.env first:")
        print("  Copy-Item deploy-production.env.example deploy-production.env")
        print("  # then set VPS_PASSWORD=<from iNET email / OneDash reset>")
        return 1

    try:
        import paramiko  # noqa: F401
    except ImportError:
        print("pip install paramiko requests")
        return 1

    print(f"=== {'INSPECT' if inspect else 'MIGRATE'} LearnHouse domain ===")
    print(f"host: {env['VPS_USER']}@{env['VPS_HOST']}:{env['VPS_PORT']}")
    print(f"{env['OLD_DOMAIN']} -> {env['LEARNHOUSE_DOMAIN']}")

    client = connect(env)
    try:
        if inspect:
            return do_inspect(client, env)
        return do_apply(client, env)
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
