# Production Deploy Runbook — LearnHouse on iNET VPS

> **Real deploy log** from 2026-07-03. Followed by anyone repeating this stack.
> Course: `Advanced trading course : The complete Smart Money Concepts` (20 sections, 71 lessons).
>
> **Domain migration 2026-07-04:** production domain switched from the original `learn.hoa-homes.com`
> to **`learn.azzamedu.com`**. All operational steps below use the new domain. The dated deploy log
> at the bottom keeps the original hostname for history. See `scripts/migrate-domain.py` for the switch.

---

## Stack

| Layer | Value |
|-------|-------|
| Domain | `learn.azzamedu.com` |
| VPS | iNET Cloud (Ubuntu 22.04) · `162.4.176.43:24700` |
| Panel | OneDash — https://one.inet.vn |
| LMS | LearnHouse (Docker: nginx + app + redis + postgres) |
| Admin | `admin@hoa-homes.com` |
| Org slug | `alpha-elite` |

WordPress stays on hosting **WP-H1** at `hoa-homes.com` — LMS is a **separate subdomain on a separate VPS**.

---

## Phase 0 — Prerequisites

- iNET domain `hoa-homes.com` (active)
- iNET Cloud VPS 2 vCPU / 4 GB / Ubuntu 22.04 — SSH via OneDash
- Python 3.11+ on Windows (for deploy scripts)
- Course content ready in `web/learnhouse/content/udemy-original/*.md`

---

## Phase 1 — DNS

**OnePortal → Tên miền → hoa-homes.com → Bản ghi DNS:**

| Type | Host | Value | TTL |
|------|------|-------|-----|
| A | `learn` | `<VPS_IP>` | 5 min |

Verify from Windows:

```powershell
ping learn.azzamedu.com
```

Must return the VPS IP. Wait 5–30 min after saving.

---

## Phase 2 — Configure deploy env (local)

Copy the template:

```powershell
cd "web\learnhouse\scripts"
Copy-Item deploy-production.env.example deploy-production.env
notepad deploy-production.env
```

Fill:

```env
VPS_HOST=162.4.176.43
VPS_PORT=24700
VPS_USER=root
VPS_PASSWORD=<from iNET email or OneDash reset>

LEARNHOUSE_DOMAIN=learn.azzamedu.com
LEARNHOUSE_ADMIN_EMAIL=admin@hoa-homes.com
LEARNHOUSE_ADMIN_PASSWORD=<strong password — save in vault>
LEARNHOUSE_ORG_SLUG=alpha-elite
```

`deploy-production.env` is **gitignored** — never commit.

---

## Phase 3 — Automated VPS bootstrap

```powershell
python -m pip install paramiko requests -q
python -u deploy-vps.py
```

Script does (over SSH from Windows):

1. `apt update && apt upgrade` (non-interactive)
2. Install Docker + Node 20
3. Open ports 22, 80, 443
4. `npx learnhouse@latest setup --ci` → domain, admin, org
5. `npx learnhouse start && npx learnhouse doctor`
6. Wait for `https://learn.azzamedu.com` to answer
7. Auto-run seed script if site is up

Total time: **10–15 min**.

### Known interactive prompt

Ubuntu upgrade may pause on `/etc/cloud/cloud.cfg` conf prompt. Two ways to unblock:

**A. Fully non-interactive (already in `vps-bootstrap.sh`):**
```bash
export DEBIAN_FRONTEND=noninteractive UCF_FORCE_CONFFOLD=1
echo 'cloud-init cloud-init/cloud.cfg multiselect keep' | debconf-set-selections
apt-get -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold -y upgrade
```

**B. If deploy hangs — SSH via OneDash terminal, type `N` + Enter until it continues.**

Then re-run `deploy-vps.py`.

### If dpkg is locked from an earlier interrupt

```bash
pkill -9 -f 'apt-get'; pkill -9 -f dpkg; sleep 2
rm -f /var/lib/dpkg/lock-frontend /var/lib/dpkg/lock /var/cache/apt/archives/lock
dpkg --configure -a
```

---

## Phase 4 — Manual paste fallback

If SSH auto fails, open **OneDash → server card → SSH Terminal** → login `root` + VPS password → paste this block (see `print-vps-paste.py` to regenerate):

```bash
export DEBIAN_FRONTEND=noninteractive UCF_FORCE_CONFFOLD=1
echo 'cloud-init cloud-init/cloud.cfg multiselect keep' | debconf-set-selections
apt-get update -qq
apt-get install -y curl git ca-certificates
command -v docker >/dev/null || curl -fsSL https://get.docker.com | sh
command -v node >/dev/null || (curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && apt-get install -y nodejs)
ufw allow 80,443/tcp 2>/dev/null; ufw --force enable 2>/dev/null
mkdir -p /opt/learnhouse && cd /opt/learnhouse
npx learnhouse@latest setup --ci \
  --install-dir /opt/learnhouse \
  --domain learn.azzamedu.com --port 80 \
  --admin-email admin@hoa-homes.com \
  --admin-password 'CHANGE-ME' \
  --org-name "Alpha Elite" --org-slug alpha-elite
npx learnhouse@latest start && sleep 20 && npx learnhouse@latest doctor
echo '=== DONE ==='
```

Wait for `LearnHouse is ready!` + doctor pass.

---

## Phase 5 — Seed course content

From Windows, either automatic (as part of `deploy-vps.py`) or standalone:

```powershell
.\deploy-production.ps1 -SeedOnly
```

Under the hood: sets env vars → runs `seed-udemy-clone.py` against prod API. Creates course, 20 chapters, 71 activities.

Expected output tail:

```
=== Udemy ORIGINAL clone seeded: 20 sections, 71 lessons ===
```

---

## Phase 6 — Sync full content from local (with videos)

Text-only seed misses two things that live in the **local LearnHouse database**, not in `.md` files:

- YouTube embed blocks (`blockEmbed`) added via UI
- Rich lesson bodies edited in the TipTap editor

Run:

```powershell
python -u sync-local-to-prod.py
```

Requires local instance at `http://localhost:8080`. Copies any lesson where local has more blocks or an embed. Matched by lesson title.

For per-section fixes (e.g. S16 title mismatch, quiz overwrite):

```powershell
python -u sync-ab-fixes.py
```

---

## Phase 7 — Audit local vs production

```powershell
python -u audit-local-vs-prod.py
```

Prints per-section table (blocks, video flag, text length) and writes `audit-local-vs-prod.json`. Use to find:

- Lessons empty on prod
- Sections with title mismatch
- Video-on-local-only cases
- Text-length divergence

---

## Phase 8 — Post-deploy tasks

| Task | Where |
|------|-------|
| Upload course thumbnail (banner SMC) | LearnHouse UI → Course settings |
| Enable HTTPS via Let's Encrypt | Re-run `npx learnhouse setup` with `--port 443` or configure nginx |
| WordPress thank-you page → link `http://learn.azzamedu.com` | Elementor edit `/gameplan-thank-you` |
| Brevo `access_ready` template → same URL | Brevo dashboard |
| Rotate VPS root password (was shared for setup) | OnePortal → VPS → Reset password |
| Set weekly backup cron on VPS | `crontab -e` → `0 3 * * 0 cd /opt/learnhouse && npx learnhouse backup` |

---

## Phase 9 — Update workflow (after go-live)

**Change lesson text (uses .md files):**

```powershell
# Edit content/udemy-original/sNN-*.md
python -u sync-udemy-clone.py    # dev instance
python -u sync-local-to-prod.py  # push to VPS
```

**Add video to a lesson (fastest via UI):**

1. Open `http://learn.azzamedu.com` → lesson → Edit
2. Paste YouTube URL → embed block
3. Save

Or edit local, then push:

```powershell
python -u sync-local-to-prod.py
```

**Restructure sections (rare):**

Edit `content/udemy-clone-curriculum.json` → run `seed-udemy-clone.py` (**wipes course**). Only for full rebuild.

---

## Phase 10 — Change production domain (migration)

Switch the live LMS to a new subdomain (e.g. `learn.hoa-homes.com` → `learn.azzamedu.com`)
without losing content. Order matters — **DNS first**, then config.

1. **DNS (iNET OnePortal → Tên miền → azzamedu.com → Bản ghi DNS):**

   | Type | Host | Value | TTL |
   |------|------|-------|-----|
   | A | `learn` | `162.4.176.43` | 5 min |

   Remove/override any existing `learn` record (and any wildcard `*`) that points elsewhere.
   Verify from Windows: `ping learn.azzamedu.com` must return `162.4.176.43`.

2. **Inspect the VPS first (read-only):**

   ```powershell
   cd "web\learnhouse\scripts"
   Copy-Item deploy-production.env.example deploy-production.env   # if not present
   notepad deploy-production.env                                   # set VPS_PASSWORD
   python -u migrate-domain.py --inspect
   ```

   Shows `learnhouse.config.json`, `.env`, compose files, and which files hold the old domain.

3. **Apply the switch:**

   ```powershell
   python -u migrate-domain.py
   ```

   Backs up each config file, replaces old→new domain, restarts LearnHouse, runs doctor.
   If the browser still calls the old domain, the frontend image was built with a baked-in
   `NEXT_PUBLIC_LEARNHOUSE_DOMAIN` → re-run `npx learnhouse setup --ci --domain <new> ...` on the VPS.

4. **Enable HTTPS** for the new domain (Phase 8) once DNS resolves + ports 80/443 open.

5. **Update downstream:** WordPress thank-you link, Brevo `access_ready` template, Telegram bot
   `LEARNHOUSE_URL`. (Repo defaults already point to the new domain.)

> Admin login email stays `admin@hoa-homes.com` (it is a DB user, independent of the domain).
> Change it separately in the LearnHouse UI only if you want to rebrand the account.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ping learn.azzamedu.com` returns wrong IP | Wait 30 min; check OnePortal DNS record |
| `learn.azzamedu.com` refused connect | SSH into VPS → `cd /opt/learnhouse && npx learnhouse start && npx learnhouse doctor` |
| SSH `Permission denied` | Reset VPS root password in OnePortal, update `deploy-production.env` |
| `Kết nối thất bại` in OneDash | Wrong username (use `root`) or password |
| `apt-get` hangs on conf prompt | See Phase 3 known-prompt fix or paste `N` in OneDash SSH |
| Seed returns 401 | Wrong admin password → run `learnhouse setup` again OR reset user in DB |
| Sync says `MISSING on prod` for a lesson | Title differs between local and JSON — check section 16 for renames |
| HTTPS fails Let's Encrypt | DNS not propagated; ports 80/443 blocked; wait then retry |

---

## Files touched during deploy

```
web/learnhouse/scripts/
├── deploy-production.env          # secrets — gitignored
├── deploy-production.env.example  # template
├── deploy-production.ps1          # wrapper: pip + python deploy-vps.py
├── deploy-vps.py                  # SSH bootstrap + wait + seed
├── vps-bootstrap.sh               # runs on VPS: apt, docker, node, learnhouse setup
├── fix-and-bootstrap.py           # recovery: dpkg unlock + rerun bootstrap
├── resume-vps.py                  # after apt hang: kill locks + continue
├── print-vps-paste.py             # emit base64 one-liner for manual paste
├── migrate-domain.py              # SSH: switch prod domain (inspect + apply)
├── migrate-domain.sh              # runs on VPS: backup config + replace domain + restart
├── seed-udemy-clone.py            # create course + 20 sections + 71 lessons
├── sync-udemy-clone.py            # update bodies (no course wipe)
├── sync-local-to-prod.py          # copy local content → prod, incl. videos
├── sync-ab-fixes.py               # targeted: S16 merge + quiz sync
├── audit-local-vs-prod.py         # diff report + JSON dump
└── compare-local-prod.py          # quick metadata check
```

Content:

```
web/learnhouse/content/
├── udemy-clone-curriculum.json    # 20 chapters × 71 lessons — SEED SOURCE
└── udemy-original/                # sNN-*.md — SYNC SOURCE for bodies
```

---

## Deploy log 2026-07-03 (reference)

- 15:30 — DNS `learn` → `162.4.176.43` (iNET OnePortal)
- 16:53 — SSH root login OK
- 16:55 — First `apt upgrade` hung on `cloud.cfg` prompt (manual N)
- 18:46 — Second run with non-interactive flags: OK
- 19:00 — `npx learnhouse setup --ci` OK, 4 containers up
- 19:01 — Course seed 20 sections / 71 lessons OK
- 19:14 — `sync-local-to-prod.py`: 34 videos + 2 long texts pushed
- 19:25 — `sync-ab-fixes.py`: S16 (4 lessons) + quizzes (3 lessons) pushed
- 20:55 — Initial git push to GitHub azzamedu

Result (2026-07-03): `http://learn.hoa-homes.com` live · 4 containers healthy · course fully populated.
Migrated to `learn.azzamedu.com` on 2026-07-04 (see top note + `scripts/migrate-domain.py`).
