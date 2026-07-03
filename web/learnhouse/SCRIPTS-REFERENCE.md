# LearnHouse Scripts Reference

Every script in `web/learnhouse/scripts/`. Grouped by task.

---

## Local dev

| Script | Purpose |
|--------|---------|
| `local-setup.ps1` | First-time: Docker Desktop check → `npx learnhouse setup --ci` at `http://localhost:8080` |
| `local-start.ps1` | `npx learnhouse start` for local instance |

---

## Seed / sync course (bodies from `.md`)

| Script | Purpose | Destructive? |
|--------|---------|--------------|
| `seed-udemy-clone.py` | Delete old course + recreate 20 sections × 71 lessons from `udemy-clone-curriculum.json` + `udemy-original/*.md` | **YES** — wipes course |
| `seed-udemy-clone.ps1` | PowerShell wrapper (`pip install requests` + run) | — |
| `sync-udemy-clone.py` | Update body of existing lessons (match by title). Adds nothing, deletes nothing. | No |
| `sync-udemy-clone.ps1` | PowerShell wrapper | — |
| `seed-course.py` / `seed-course.ps1` | **Legacy** — old 8-module (`apprentice-operating-course`) seed. Not used for Udemy clone. | — |
| `sync-course.py` / `sync-course.ps1` | **Legacy** — sync 8-module bodies. | — |
| `course_api.py` | Shared helpers: login, auth headers, activity create, markdown→TipTap conversion. **Do not run directly**. | — |

**Env vars** (all scripts):

- `LEARNHOUSE_API` (default `http://localhost:8080/api/v1`)
- `LEARNHOUSE_ADMIN_EMAIL`, `LEARNHOUSE_ADMIN_PASSWORD`
- `LEARNHOUSE_ORG_SLUG` (default `alpha-elite`)

---

## VPS bootstrap (production)

| Script | Purpose |
|--------|---------|
| `deploy-production.env.example` | Template for `deploy-production.env` (VPS creds + admin pw). Copy + fill. |
| `deploy-production.env` | **Gitignored** — real secrets. |
| `deploy-production.ps1` | Wrapper — auto-creates env from template, `pip install paramiko`, runs `deploy-vps.py`. Flag `-SeedOnly` skips VPS bootstrap. |
| `deploy-vps.py` | SSH into VPS → upload + run `vps-bootstrap.sh` → wait for site up → run `seed-udemy-clone.py` against prod API. |
| `vps-bootstrap.sh` | Runs **on VPS**: apt update, install Docker + Node 20, ufw ports, `npx learnhouse setup --ci`, `start`, `doctor`. Uses `DEBIAN_FRONTEND=noninteractive` + `--force-confold` to avoid apt prompts. |
| `print-vps-paste.py` | Emit base64-encoded one-liner to paste into OneDash SSH terminal when SSH auto fails. |
| `fix-and-bootstrap.py` | Recovery: kills hung apt/dpkg locks, runs `dpkg --configure -a`, retries bootstrap. |
| `resume-vps.py` | Similar recovery for older stuck states. |

Typical run:

```powershell
cd web\learnhouse\scripts
Copy-Item deploy-production.env.example deploy-production.env
notepad deploy-production.env
.\deploy-production.ps1
```

---

## Local → Production sync

| Script | Purpose |
|--------|---------|
| `sync-local-to-prod.py` | Read every activity from local, push to prod when local has more blocks or has a `blockEmbed` (video) that prod lacks. Preserves prod-only content that's already richer. |
| `sync-ab-fixes.py` | Targeted fixes: **A** merge S16 by index (local `S16 -` chapter has 4 videos with `001…` titles; prod `S16:` has 6 Udemy titles) · **B** force-overwrite quiz lessons S14/S15/S17 (local has real questions, prod defaults to Udemy template). |
| `compare-local-prod.py` | Quick check: metadata, L1 block count, video type presence. |
| `audit-local-vs-prod.py` | **Full section-by-section diff**. Writes `audit-local-vs-prod.json`. Flags: `TITLE`, `NO_VIDEO_PROD`, `TEXT_DIFF(nvsm)`, `BLOCKS(nvsm)`, `EMPTY_PROD`. |

**Env** for these:

- `LEARNHOUSE_LOCAL_API`, `LEARNHOUSE_LOCAL_PASSWORD` (local instance)
- `LEARNHOUSE_API`, `LEARNHOUSE_ADMIN_PASSWORD` (prod)

Or use `deploy-production.env` (auto-loaded by wrappers).

---

## Content-source layout

```
content/
├── udemy-clone-curriculum.json   # 20 chapters × 71 lessons — SEED SOURCE
├── udemy-original/
│   ├── s01-introduction.md       # 9 lessons
│   ├── s02-definitions.md        # 7 lessons
│   ├── ...
│   └── s20-thank-you.md          # 4 lessons
├── LESSON-TEMPLATE-FULL.md       # Style guide for full-length lessons
└── apprentice-operating-course/  # Legacy 8-module content (not deployed)
```

Each `sNN-*.md` file has one `## Lesson title` per lesson. Title must match `udemy-clone-curriculum.json` exactly (case-insensitive).

---

## Runbooks

| Scenario | Script order |
|----------|--------------|
| **Cold VPS install** | `deploy-production.ps1` (does everything) |
| **Rebuild course from scratch on prod** | `deploy-production.ps1 -SeedOnly` |
| **Text-only edit → prod** | edit `.md` → `sync-udemy-clone.py` (local) → `sync-local-to-prod.py` (prod) |
| **Video edit → prod** | UI on local → `sync-local-to-prod.py` |
| **S16 or quiz repair after re-seed** | `sync-ab-fixes.py` |
| **What's different?** | `audit-local-vs-prod.py` |
| **Emergency: VPS apt locked** | `fix-and-bootstrap.py` or paste unlock block from `PRODUCTION-DEPLOY-RUNBOOK.md` |

---

## Debug tips

**Login failure (401):**
- Check `LEARNHOUSE_ADMIN_PASSWORD` env var vs actual instance
- Local default: `AlphaElite-Local-2026!`
- Prod default: `AlphaElite-Prod-Learn-2026!`

**Lesson body empty in UI:**
- Ensure TipTap doc is `{type:"doc", content:[...]}` at root (handled by `markdown_to_tiptap_doc()` in `course_api.py`)

**`sync` says `MISSING` for a lesson:**
- Title in `.md` doesn't match title in `udemy-clone-curriculum.json` OR the activity was renamed in UI
- Check with `audit-local-vs-prod.py` output

**Seed hangs 8+ minutes:**
- Old `####` heading not handled — already fixed; run latest `course_api.py`
