# LearnHouse Editing Guide

**Course:** `Advanced trading course : The complete Smart Money Concepts` (verbatim Udemy clone)
**Structure:** 20 sections · 71 lessons

| Environment | URL | Login |
|-------------|-----|-------|
| **Local** | http://localhost:8080 | `admin@hoa-homes.com` / `AlphaElite-Local-2026!` |
| **Production** | http://learn.azzamedu.com | `admin@hoa-homes.com` / `AlphaElite-Prod-Learn-2026!` |

For **first-time deploy** or full re-provision, follow `PRODUCTION-DEPLOY-RUNBOOK.md`.

---

## Decision matrix — how to edit

| I want to… | Method | File / Tool |
|------------|--------|-------------|
| Fix a typo in one lesson | UI on the target env | LearnHouse editor |
| Add a YouTube video to a lesson | UI (embed block) | LearnHouse editor |
| Rewrite body of many lessons | Edit `.md` + sync | `content/udemy-original/*.md` |
| Change lesson title | Edit JSON + rename in UI | `content/udemy-clone-curriculum.json` |
| Add/remove a section | Edit JSON + full re-seed | ⚠️ wipes course |
| Push a local edit up to prod | Sync script | `sync-local-to-prod.py` |
| Course description / About / thumbnail | UI (Course settings) | On each env |

---

## Fast edit in LearnHouse UI (1 lesson at a time)

1. Login → **Courses** → **Advanced trading course : The complete Smart Money Concepts**
2. Sidebar → choose section → click lesson name
3. **Edit** (pencil icon) → change content → **Save**
4. Refresh

Edits made in the **local** UI stay on local. Push to prod with:

```powershell
cd web\learnhouse\scripts
python -u sync-local-to-prod.py
```

---

## Edit lesson bodies via markdown files

Files: `content/udemy-original/s01-introduction.md` … `s20-thank-you.md`

Each lesson is an `## Heading` block inside the section file. Structure:

```markdown
## Lesson title (must match curriculum JSON exactly)

Intro paragraph.

### What it is?
...

### How to define or apply it?
- bullet
- bullet

### Example
...

### Video
`[PENDING]` · Duration: 2:33
```

After edit:

```powershell
python -u sync-udemy-clone.py    # → local (dev preview)
python -u sync-local-to-prod.py  # → production
```

Lesson matched by **exact title** (case-insensitive fallback).

---

## Add YouTube video

**Option A — UI (recommended):** paste YouTube URL in lesson editor → embed block appears.

**Option B — programmatic:** UI-created embeds live in the DB, not `.md`. `sync-local-to-prod.py` copies them from local. So workflow:

1. Add video on local via UI
2. Run `python sync-local-to-prod.py`

Video URL format that works: `https://youtu.be/XXXXXXXX` or full YouTube link.

---

## Change section titles / add lessons

Edit `content/udemy-clone-curriculum.json`:

```json
{
  "number": 2,
  "title": "Definitions about Smart Money Concepts",
  "lessons": [
    {"title": "Liquidity - smart money", "type": "video", "duration": "3:22"},
    {"title": "New lesson here", "type": "video"}
  ]
}
```

Then **either**:

- Add matching `## New lesson here` to `content/udemy-original/s02-definitions.md` and run `sync-udemy-clone.py` — safe, no data loss
- **OR** run `seed-udemy-clone.py` — wipes and recreates course

Only re-seed when the course is broken or you're OK losing UI edits (videos, thumbnails).

---

## Sync direction summary

```text
.md files ──seed/sync──► LOCAL DB ──sync-local-to-prod──► PROD DB
     ▲                       ▲
     │                       │
  edit .md            edit in UI
```

- `seed-udemy-clone.py` — full rebuild (delete + create) against `LEARNHOUSE_API`
- `sync-udemy-clone.py` — safe update of bodies against `LEARNHOUSE_API`
- `sync-local-to-prod.py` — copy from `LEARNHOUSE_LOCAL_API` to `LEARNHOUSE_API`

Env vars used by all scripts (see `course_api.py`):

| Var | Default |
|-----|---------|
| `LEARNHOUSE_API` | `http://localhost:8080/api/v1` |
| `LEARNHOUSE_LOCAL_API` | `http://localhost:8080/api/v1` |
| `LEARNHOUSE_ADMIN_EMAIL` | `admin@hoa-homes.com` |
| `LEARNHOUSE_ADMIN_PASSWORD` | `AlphaElite-Local-2026!` |
| `LEARNHOUSE_LOCAL_PASSWORD` | `AlphaElite-Local-2026!` |
| `LEARNHOUSE_ORG_SLUG` | `alpha-elite` |

For prod sync, set `LEARNHOUSE_API=http://learn.azzamedu.com/api/v1` and `LEARNHOUSE_ADMIN_PASSWORD=<prod pw>` — or use `deploy-production.env`.

---

## Common commands (Windows PowerShell)

```powershell
cd "web\learnhouse\scripts"

# Local dev
.\local-start.ps1              # start Docker + LearnHouse local
python -u sync-udemy-clone.py  # push .md changes to local

# Production
.\deploy-production.ps1 -SeedOnly   # push course to prod (uses env file)
python -u sync-local-to-prod.py     # push local UI edits (videos etc.) to prod
python -u audit-local-vs-prod.py    # diff report
```

---

## Section map (verbatim Udemy)

| # | Section title |
|---|---------------|
| S01 | Jayce's INTRODUCTION - Get your TRUST - Learn more Serious - Get the real result |
| S02 | Definitions about Smart Money Concepts |
| S03 | Main : Double Order-Block with POI - POI to optimize RR |
| S04 | Main : Double Order Block with BOS bounce |
| S05 | Extra Knowledge |
| S06 | Trading EXAMPLES - All the cases with SMC |
| S07 | How to define the power of Smart Money Signal - New update |
| S08–S11 | Live sessions Sep 26–29 |
| S12 | Trading journal |
| S13 | Bonus Section : Zero to Profitable |
| S14 | 15 Bonus Basic Quiz |
| S15 | 15 Bonus Advanced Quiz |
| S16 | Trading tips - experience |
| S17 | Final examination - 18 Questions |
| S18 | 2024 UPDATE for Smart Money Concepts |
| S19 | UPDATE _ NCI indicators for REAL TRADING |
| S20 | Thank you |

Full lesson list: `content/udemy-clone-curriculum.json`.

---

## Related docs

- `PRODUCTION-DEPLOY-RUNBOOK.md` — VPS setup from zero
- `SCRIPTS-REFERENCE.md` — every script explained
- `local-test-guide.md` — Docker Desktop setup on Windows
- `admin-setup-checklist.md` — org / groups / permissions in LH UI
