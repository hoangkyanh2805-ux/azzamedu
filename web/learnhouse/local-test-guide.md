# LearnHouse Local Test — Alpha Elite

Run LearnHouse on **Windows** before VPS deploy. Uses Docker Desktop + LearnHouse CLI.

---

## ⚠️ First-time on this machine

If you just installed Docker/WSL via the setup script:

1. **Reboot Windows** (WSL install requires it)
2. Open **Docker Desktop** → wait for **Engine running**
3. Run `.\scripts\local-setup.ps1`

Shortcut: read `START-HERE-AFTER-REBOOT.md`

---

## Prerequisites (one-time)

1. **Node.js** ≥ 18 — already installed
2. **Docker Desktop** — install via:
   ```powershell
   winget install -e --id Docker.DockerDesktop --source winget
   ```
3. Open **Docker Desktop** → wait until status is **Running** (whale icon steady)
4. First launch may require WSL2 — accept prompts and reboot if asked

---

## Quick start (automated)

From repo root in PowerShell:

```powershell
cd "g:\Other computers\My Computer\Project\webkhoahoc\web\learnhouse"
.\scripts\local-setup.ps1      # first time only
.\scripts\seed-course.ps1        # upload 8 modules / 35 lessons via API
```

Or manual:

```powershell
cd "g:\Other computers\My Computer\Project\webkhoahoc\web\learnhouse\instance"

npx learnhouse@latest setup --ci `
  --install-dir . `
  --domain localhost `
  --port 8080 `
  --admin-email admin@hoa-homes.com `
  --admin-password "AlphaElite-Local-2026!" `
  --org-name "Alpha Elite" `
  --org-slug alpha-elite

npx learnhouse@latest start
npx learnhouse@latest doctor
```

**Open:** http://localhost:8080

| Field | Local test value |
|-------|------------------|
| URL | http://localhost:8080 |
| Admin email | admin@hoa-homes.com |
| Admin password | `AlphaElite-Local-2026!` (change after first login) |

> Password is for **local dev only** — never use on production VPS.

---

## After login — paste course content

1. Follow `admin-setup-checklist.md` (groups, courses)
2. Copy lessons from `content/apprentice-operating-course/m0X-*.md`
3. Attach worksheets from `content/worksheets/` (export to PDF optional)
4. Use any YouTube embed for video test (unlisted when recording real content)

---

## Daily commands

```powershell
cd "g:\Other computers\My Computer\Project\webkhoahoc\web\learnhouse\instance"
npx learnhouse@latest start    # start
npx learnhouse@latest stop     # stop
npx learnhouse@latest logs     # debug
npx learnhouse@latest doctor   # health
npx learnhouse@latest status   # containers
```

---

## Connect Telegram bot (optional local)

In `telegram-bot/.env`:

```
LEARNHOUSE_URL=http://localhost:8080
```

Only for local bot testing — production uses `https://learn.azzamedu.com`.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `docker` not recognized | Open Docker Desktop; restart terminal |
| WSL required | Settings → enable WSL2; reboot |
| Port 8080 in use | Change `--port 8081` in setup |
| `doctor` fails | `npx learnhouse logs` — wait 60s after first start |
| Path with spaces | Use quoted paths as in scripts |

---

## Migrate to VPS later

When VPS is ready:

1. `npx learnhouse backup` on local instance
2. Deploy per `deploy-guide.md` on VPS
3. Restore or re-paste content (MVP: re-paste is fine)
4. Update DNS + bot `LEARNHOUSE_URL`

---

## Git ignore

`web/learnhouse/instance/` is gitignored (Docker volumes, `.env`, credentials).
