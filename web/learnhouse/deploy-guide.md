# LearnHouse Deploy Guide — Alpha Elite

**Target:** `https://learn.azzamedu.com` (subdomain separate from WordPress on `hoa-homes.com`)

**Local test first:** `local-test-guide.md` (Windows + Docker Desktop)

**Recommended VPS:** 2 vCPU · 4 GB RAM · 40 GB SSD · Ubuntu 22.04+

> WordPress stays on iNET hosting. LearnHouse runs on a **separate VPS** so LMS traffic does not compete with Elementor/WooCommerce.

---

## Prerequisites

| Requirement | Notes |
|-------------|-------|
| Node.js ≥ 18 | On VPS or local machine running CLI |
| Docker Engine 20.10+ | With Compose v2 |
| DNS | A record `learn` → VPS IP |
| Ports | 80, 443 open |

---

## Step 1 — DNS

In domain panel (iNET / registrar):

| Type | Host | Value |
|------|------|-------|
| A | `learn` | `<VPS_IP>` |

Wait for propagation (5–60 min). Verify: `ping learn.azzamedu.com`

---

## Step 2 — VPS bootstrap

```bash
# SSH into VPS
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git

# Install Docker (official script)
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# Log out and back in for group to apply

# Install Node 20 (for CLI)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
node -v   # should be >= 18
```

---

## Step 3 — LearnHouse CLI setup

```bash
mkdir -p /opt/learnhouse && cd /opt/learnhouse

npx learnhouse@latest setup
```

**Wizard answers (recommended):**

| Prompt | Value |
|--------|-------|
| Install directory | `/opt/learnhouse` |
| Domain | `learn.azzamedu.com` |
| HTTPS | **Yes** (Let's Encrypt) |
| Database | Local Docker (PostgreSQL) |
| Redis | Local Docker |
| Organization name | `Alpha Elite` |
| Admin email | ops@yourdomain.com |
| Admin password | Strong — store in password manager |

```bash
npx learnhouse start
npx learnhouse doctor
```

Open `https://learn.azzamedu.com` → log in with admin credentials.

---

## Step 4 — Post-install hardening

- [ ] Change default admin password if auto-generated
- [ ] Enable firewall: `sudo ufw allow 22,80,443/tcp && sudo ufw enable`
- [ ] Set weekly backup cron:

```bash
# Add to crontab (crontab -e)
0 3 * * 0 cd /opt/learnhouse && npx learnhouse backup >> /var/log/learnhouse-backup.log 2>&1
```

- [ ] Document admin URL + credentials in secure ops vault (not in git)

---

## Step 5 — Connect to Alpha Elite stack

| Integration | MVP action |
|-------------|------------|
| WooCommerce | Manual provision per order (no API) |
| Brevo | `access_ready` email with LH login URL |
| Telegram bot | Set `LEARNHOUSE_URL=https://learn.azzamedu.com` in bot `.env` |
| YouTube | Unlisted embeds per lesson — no LH video upload |

**Bot config** (`telegram-bot/config.yaml`):

```yaml
site:
  learnhouse_url: https://learn.azzamedu.com
```

---

## Common CLI commands

```bash
cd /opt/learnhouse
npx learnhouse start      # Start services
npx learnhouse stop       # Stop services
npx learnhouse logs       # Stream logs
npx learnhouse doctor     # Health check
npx learnhouse backup     # Manual backup
npx learnhouse update     # Update LH version (test staging first)
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| SSL fails | Confirm DNS A record points to VPS; port 443 open |
| `doctor` fails DB | `npx learnhouse logs` → restart postgres container |
| Can't reach from browser | Check `ufw`, cloud provider security group |
| Embed blocked | YouTube embed domain whitelist not needed for unlisted |
| Slow on 2GB VPS | Upgrade to 4GB or move LH to dedicated VPS |

---

## Phase 2 (defer)

- LearnHouse API auto-enroll from WooCommerce webhook
- SSO / OAuth if needed at scale
- S3 for worksheet storage (optional — PDFs in LH attachments OK for MVP)
