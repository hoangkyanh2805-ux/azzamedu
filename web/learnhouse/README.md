# LearnHouse — Alpha Elite LMS

Self-hosted course delivery for **Apprentice Operating Course** and **VIP Resource Library**.

| System | Role |
|--------|------|
| WooCommerce | Payment + order truth |
| LearnHouse | Course delivery, progress |
| YouTube Unlisted | Video hosting (embed only) |
| Brevo | `access_ready` email |
| Admin | Manual enroll ≤ 24h (MVP) |

**Customer-facing language:** English (Canada + EU market standard per `docs/offer_stack.md`).

---

## Key docs (start here)

| Doc | When to read |
|-----|--------------|
| `PRODUCTION-DEPLOY-RUNBOOK.md` | Cold VPS install → live site (this is the current source of truth) |
| `SCRIPTS-REFERENCE.md` | What each script in `scripts/` does |
| `docs/EDITING-GUIDE.md` | Day-to-day content edits, sync workflow |
| `local-test-guide.md` | Set up local instance on Windows + Docker Desktop |
| `admin-setup-checklist.md` | Org / groups / permissions in LearnHouse UI |
| `deploy-guide.md` | Original generic deploy notes (superseded by RUNBOOK) |

## Repo layout

```text
web/learnhouse/
├── PRODUCTION-DEPLOY-RUNBOOK.md  # ← START HERE for prod deploy
├── SCRIPTS-REFERENCE.md
├── docs/EDITING-GUIDE.md
├── deploy-guide.md               # legacy generic notes
├── local-test-guide.md
├── admin-setup-checklist.md
├── qg-lms-checklist.md
├── content/
│   ├── udemy-clone-curriculum.json    # 20 chapters × 71 lessons (seed source)
│   ├── udemy-original/                # sNN-*.md lesson bodies
│   ├── apprentice-operating-course/   # legacy 8-module content
│   ├── worksheets/
│   └── vip-resource-library/
└── scripts/
    ├── deploy-production.ps1          # cold VPS install + seed
    ├── deploy-vps.py / vps-bootstrap.sh
    ├── seed-udemy-clone.py            # destructive: recreate course
    ├── sync-udemy-clone.py            # safe: update bodies from .md
    ├── sync-local-to-prod.py          # copy local edits + videos to prod
    ├── sync-ab-fixes.py               # targeted S16 + quiz repair
    ├── audit-local-vs-prod.py         # diff report
    └── course_api.py                  # shared helpers
```

## Environments

| Env | URL | Login |
|-----|-----|-------|
| Local | http://localhost:8080 | `admin@hoa-homes.com` / `AlphaElite-Local-2026!` |
| Production | http://learn.hoa-homes.com | `admin@hoa-homes.com` / `AlphaElite-Prod-Learn-2026!` |

---

## Quick start (ops)

### Local test (Windows — no VPS yet)

1. **One-time:** Docker Desktop + WSL2 → see `local-test-guide.md`
2. Run `.\scripts\local-setup.ps1` from `web/learnhouse/`
3. Open http://localhost:8080

### Production VPS

1. **Deploy** — follow `deploy-guide.md` → `learn.hoa-homes.com` (or your subdomain)
2. **Admin** — follow `admin-setup-checklist.md` (org, groups, courses)
3. **Content** — paste lessons from `content/` into LearnHouse lesson editor
4. **Videos** — upload unlisted YouTube, embed per lesson
5. **Test** — create test student, complete M1 on mobile
6. **Provision** — `playbook/ops/learnhouse-provision-sop.md`

---

## SKU → access

| SKU | Group | Courses |
|-----|-------|---------|
| AE-APP-001 | apprentice-students | Apprentice Operating Course |
| AE-VIP-MON/YR | vip-members | Apprentice + VIP Resource Library |
| AE-QNT-001 | quant-desk | All + Quant (phase 2) |
| AE-DWY-001 | — | No LMS change (setup session only) |

---

## Related docs

- `docs/learnhouse_lms_map.md` — course map (project truth)
- `playbook/ops/learnhouse-provision-sop.md` — human provision SOP
- `telegram-bot/docs/learnhouse-delivery-flow.md` — bot delivery after G4
- `web/wordpress/course-curriculum-copy.md` — landing curriculum copy source

---

## MVP acceptance

- [ ] `npx learnhouse doctor` passes on VPS
- [ ] HTTPS live at `https://learn.[domain].com`
- [ ] M1–M3 lessons published with unlisted embeds
- [ ] Test student completes M1 on mobile
- [ ] Manual provision dry-run < 24h SLA
- [ ] `qg-lms-checklist.md` signed off
