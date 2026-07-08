---
name: learnhouse-production-sync
description: Deploy LearnHouse to a fresh iNET VPS and keep the local dev instance in sync with production. Use when the user wants to (1) bootstrap a new LearnHouse server on Ubuntu via SSH, (2) push course content from local `:8080` to `learn.azzamedu.com`, (3) audit differences between local and prod, or (4) recover from stuck apt/dpkg during VPS setup. Covers the Udemy SMC clone (20 sections, 71 lessons) but the pattern works for any LearnHouse course.
---

# LearnHouse — Local → Production Sync Skill

## When to use

The user is working in `web/learnhouse/` and asks about:

- Deploying LearnHouse to a VPS (iNET or similar Ubuntu box)
- Pushing course content from local to production
- Comparing local vs prod (audit)
- Fixing a broken deploy (dpkg lock, apt hang, seed failure)
- Adding videos or lessons and getting them live

## Ground rules

1. **Two DBs, one source of truth.** Local `:8080` and prod `learn.azzamedu.com` are independent LearnHouse instances. Content lives in the DB, not just in `.md` files. UI edits (videos, thumbnails) do **not** appear in `.md` — they must be synced via API.

2. **Never commit `deploy-production.env`.** It contains VPS root password. `.gitignore` covers it.

3. **Course name must match exactly:** `Advanced trading course : The complete Smart Money Concepts`. Lesson matching is by exact title (case-insensitive fallback).

4. **Re-seed only when acceptable to lose UI edits.** `seed-udemy-clone.py` deletes the course. Prefer `sync-udemy-clone.py` / `sync-local-to-prod.py` for updates.

## Deploy phases (cold VPS)

| Phase | Action | Script |
|-------|--------|--------|
| 0 | Confirm DNS `learn.<domain>` → VPS IP (verify with `ping`) | manual |
| 1 | Fill `deploy-production.env` (host, port, root password, admin creds) | edit |
| 2 | Auto SSH bootstrap → Docker + Node + `learnhouse setup --ci` | `deploy-vps.py` |
| 3 | Wait for HTTP 200 on the domain | built into `deploy-vps.py` |
| 4 | Seed 71 lessons over API | `seed-udemy-clone.py` (auto) |
| 5 | Sync local UI edits (videos, richer bodies) up | `sync-local-to-prod.py` |
| 6 | Targeted fixes (S16 index merge, quiz overwrite) | `sync-ab-fixes.py` |
| 7 | Audit | `audit-local-vs-prod.py` |

Full command sequence:

```powershell
cd web\learnhouse\scripts
Copy-Item deploy-production.env.example deploy-production.env
notepad deploy-production.env
.\deploy-production.ps1
```

## Ongoing sync workflow

Once VPS is live, day-to-day flow is:

```text
Edit .md              ──► sync-udemy-clone.py  ──► LOCAL DB
Add video in UI       ──► LOCAL DB
                          │
                          ▼
                      sync-local-to-prod.py    ──► PROD DB
```

`sync-local-to-prod.py` pushes any lesson where local has more blocks or a `blockEmbed` prod lacks. Idempotent — safe to re-run.

## Known VPS gotchas

1. **cloud-init prompt hangs apt.** Use `DEBIAN_FRONTEND=noninteractive UCF_FORCE_CONFFOLD=1` **and** `debconf-set-selections` for `cloud-init/cloud.cfg multiselect keep`. Already baked into `vps-bootstrap.sh`.

2. **dpkg lock after Ctrl+C.** Kill hung processes, remove locks, `dpkg --configure -a`:
   ```bash
   pkill -9 -f 'apt-get'; pkill -9 -f dpkg; sleep 2
   rm -f /var/lib/dpkg/lock-frontend /var/lib/dpkg/lock /var/cache/apt/archives/lock
   dpkg --configure -a
   ```
   Or run `fix-and-bootstrap.py`.

3. **OneDash SSH `Permission denied`.** User is `root`, not the Google email. Password from iNET activation email or OnePortal reset.

4. **Prod on port 80 (no HTTPS by default).** Users hit `http://learn.azzamedu.com`. To enable Let's Encrypt, rerun `learnhouse setup` with `--port 443`.

## S16 duplicate quirk (project-specific)

Local has a chapter `S16 - (New update) Trading tips - experience` with 4 lessons named `001 …`, `002 …`, etc. (each with a YouTube embed).

Prod (after re-seed) has `S16: (New update) Trading tips - experience` with 6 lessons named per Udemy JSON.

`sync-local-to-prod.py` uses title match → misses the S16 videos. Solution: **`sync-ab-fixes.py`** merges by **index** (local L1→prod L1, L2→L2, up to `min(len_local, len_prod)`).

## Quiz vs template quirk

`.md` files for S14, S15, S17 L1 contain "What it is / How to define" template — this is what `seed` puts on prod. Local has real quiz questions (pasted in UI).

`sync-ab-fixes.py` force-overwrites these 3 lessons from local — always run after a fresh seed.

## Audit workflow

```powershell
python -u audit-local-vs-prod.py
```

Reads both APIs, prints per-section table, writes `audit-local-vs-prod.json`. Flag meanings:

- `NO_VIDEO_PROD` — local has embed, prod doesn't → run `sync-local-to-prod.py`
- `TEXT_DIFF(a vs b)` — significant body divergence
- `BLOCKS(a vs b)` — block count differs
- `EMPTY_PROD` — prod lesson has no content
- `TITLE` — titles differ (rare after fixes)

Green result: `Sections fully matched: 19+`, `Video on BOTH: 34+`, `Empty content on PROD: 0`.

## Files to inspect if debugging

1. `web/learnhouse/scripts/course_api.py` — API helpers, TipTap conversion
2. `web/learnhouse/scripts/vps-bootstrap.sh` — the actual VPS install script
3. `web/learnhouse/content/udemy-clone-curriculum.json` — canonical lesson structure
4. `web/learnhouse/content/udemy-original/*.md` — canonical lesson bodies

## What NOT to do

- Do **not** run `seed-udemy-clone.py` against prod once videos are attached — it wipes them
- Do **not** commit `deploy-production.env`
- Do **not** paste VPS password in chat / screenshots (rotate immediately if exposed)
- Do **not** copy WordPress and LearnHouse to the same host — separate VPS by design

## Reference docs

- `web/learnhouse/PRODUCTION-DEPLOY-RUNBOOK.md` — full step-by-step with deploy log
- `web/learnhouse/SCRIPTS-REFERENCE.md` — every script explained
- `web/learnhouse/docs/EDITING-GUIDE.md` — content edit workflows

## Direct Udemy -> existing LearnHouse course workflow

Use this mode when the user gives:

- a Udemy source URL, and
- an existing LearnHouse target course URL on `https://learn.azzamedu.com/course/<uuid>`.

This workflow is different from the old local -> prod SMC workflow. It goes directly to the production LearnHouse course and does not use local LearnHouse as a staging database.

### Names

| Layer | Name |
|-------|------|
| Skill | `learnhouse-production-sync` |
| Workflow | Direct Udemy -> Existing Course Import |
| Operator / agent | Course Import Operator |
| Helper roles | Source Mapper, LearnHouse Course Operator, Video/Resource Import Operator, QA Reviewer |

### Ground rules for direct import

1. Convert the target URL UUID to API UUID by adding `course_` when needed.
2. Confirm the target course by API before writing anything.
3. Create missing chapters/lessons only; do not delete or recreate the course.
4. Copy Udemy metadata as-is: title, subtitle/description, about, and learning bullets.
5. Do not rewrite, translate, summarize, or customize lesson content unless requested.
6. Do not run `seed-udemy-clone.py` for this mode. That script is for the Advanced SMC clone and can wipe/recreate content.
7. Do not run `sync-local-to-prod.py` unless local LearnHouse is intentionally the source of truth.
8. Public Udemy pages are enough for first-pass metadata/curriculum. Logged-in Udemy access or exports are required for videos/resources.
9. If the target course already has value, export/backup first.

### MTF case script

For the course `Master Multiple timeframe theory in trading within 1 hour`, use:

```powershell
cd web\learnhouse\scripts
$env:LEARNHOUSE_API='https://learn.azzamedu.com/api/v1'
$env:LEARNHOUSE_ADMIN_EMAIL='admin@hoa-homes.com'
$env:LEARNHOUSE_ADMIN_PASSWORD='<set locally, never commit>'
$env:TARGET_COURSE_UUID='course_f0b9e0d8-240b-47b5-8c39-1a713dccdc0a'
python .\import-mtf-skeleton.py
```

Expected skeleton: 9 sections, 26 lessons. The script is idempotent and skips existing lessons on rerun.

Full SOP: `web/learnhouse/docs/DIRECT-UDEMY-IMPORT-GUIDE.md`.
