#!/usr/bin/env python3
"""Resume VPS deploy after interactive apt hang."""
import paramiko
from pathlib import Path

ENV = {}
for line in Path(__file__).parent.joinpath("deploy-production.env").read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, v = line.split("=", 1)
        ENV[k.strip()] = v.strip()

host, port = ENV["VPS_HOST"], int(ENV["VPS_PORT"])
user, password = ENV["VPS_USER"], ENV["VPS_PASSWORD"]
script = Path(__file__).parent.joinpath("vps-bootstrap.sh").read_text(encoding="utf-8").replace("\r\n", "\n")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=password, timeout=30)

# Kill stuck apt/dpkg if any
cmds = [
    "pkill -f 'apt-get upgrade' || true",
    "dpkg --configure -a",
    f"export DEBIAN_FRONTEND=noninteractive LEARNHOUSE_DOMAIN={ENV['LEARNHOUSE_DOMAIN']} "
    f"LEARNHOUSE_ADMIN_EMAIL={ENV['LEARNHOUSE_ADMIN_EMAIL']} "
    f"LEARNHOUSE_ADMIN_PASSWORD='{ENV['LEARNHOUSE_ADMIN_PASSWORD']}' "
    f"LEARNHOUSE_ORG_SLUG={ENV['LEARNHOUSE_ORG_SLUG']}",
]
stdin, stdout, stderr = client.exec_command(" && ".join(cmds), get_pty=True)
stdout.channel.recv_exit_status()

sftp = client.open_sftp()
with sftp.file("/tmp/vps-bootstrap.sh", "w") as f:
    f.write(script)
sftp.close()

remote_env = (
    f"export LEARNHOUSE_DOMAIN={ENV['LEARNHOUSE_DOMAIN']} "
    f"LEARNHOUSE_ADMIN_EMAIL={ENV['LEARNHOUSE_ADMIN_EMAIL']} "
    f"LEARNHOUSE_ADMIN_PASSWORD='{ENV['LEARNHOUSE_ADMIN_PASSWORD']}' "
    f"LEARNHOUSE_ORG_SLUG={ENV['LEARNHOUSE_ORG_SLUG']}"
)
print("Re-running bootstrap...")
stdin, stdout, stderr = client.exec_command(
    f"{remote_env} && chmod +x /tmp/vps-bootstrap.sh && bash /tmp/vps-bootstrap.sh",
    get_pty=True,
)
for line in iter(stdout.readline, ""):
    print(line, end="")
code = stdout.channel.recv_exit_status()
client.close()
print("exit", code)
raise SystemExit(code)
