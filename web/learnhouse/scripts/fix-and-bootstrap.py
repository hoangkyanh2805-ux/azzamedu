#!/usr/bin/env python3
import time
import paramiko
from pathlib import Path

ENV = {}
for line in Path(__file__).parent.joinpath("deploy-production.env").read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, v = line.split("=", 1)
        ENV[k.strip()] = v.strip()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ENV["VPS_HOST"], int(ENV["VPS_PORT"]), ENV["VPS_USER"], ENV["VPS_PASSWORD"], timeout=30)

def run(cmd, timeout=3600):
    print(f">>> {cmd[:120]}")
    stdin, stdout, stderr = client.exec_command(cmd, get_pty=True, timeout=timeout)
    out = []
    for line in iter(stdout.readline, ""):
        print(line, end="")
        out.append(line)
    code = stdout.channel.recv_exit_status()
    return code, "".join(out)

# Kill hung apt/dpkg from earlier attempt
run("kill -9 34647 2>/dev/null; pkill -9 -f 'apt-get upgrade' 2>/dev/null; pkill -9 -f 'dpkg --configure' 2>/dev/null; sleep 3; rm -f /var/lib/dpkg/lock-frontend /var/lib/dpkg/lock /var/cache/apt/archives/lock")

fix = r"""
export DEBIAN_FRONTEND=noninteractive
export UCF_FORCE_CONFFOLD=1
echo 'cloud-init cloud-init/cloud.cfg multiselect keep' | debconf-set-selections
dpkg --configure -a
apt-get -f install -y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold
"""
run(fix)

script = Path(__file__).parent.joinpath("vps-bootstrap.sh").read_text(encoding="utf-8").replace("\r\n", "\n")
sftp = client.open_sftp()
with sftp.file("/tmp/vps-bootstrap.sh", "w") as f:
    f.write(script)
sftp.close()

env = (
    f"export LEARNHOUSE_DOMAIN={ENV['LEARNHOUSE_DOMAIN']} "
    f"LEARNHOUSE_ADMIN_EMAIL={ENV['LEARNHOUSE_ADMIN_EMAIL']} "
    f"LEARNHOUSE_ADMIN_PASSWORD='{ENV['LEARNHOUSE_ADMIN_PASSWORD']}' "
    f"LEARNHOUSE_ORG_SLUG={ENV['LEARNHOUSE_ORG_SLUG']}"
)
code, _ = run(f"{env} && bash /tmp/vps-bootstrap.sh", timeout=3600)
client.close()
raise SystemExit(code)
