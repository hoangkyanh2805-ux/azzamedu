# LearnHouse - Azzam Gold LMS

Self-hosted course delivery for SMC course access, VIP packages, deposit bundles, and future course libraries.

| System | Role |
|---|---|
| WooCommerce / manual payment | Payment + order truth |
| LearnHouse | Course delivery, progress, user access |
| UserGroups | Access tiers and package control |
| YouTube Unlisted | Video hosting (embed only) |
| Brevo / Gmail / Zalo | Customer login delivery |
| Admin | Manual provision within 24h |

Production LMS: `https://learn.azzamedu.com`
Clones: `https://learn.alex-mentor.com/` · `https://learn.tom-edu.com/`
Next clone: **Eddric** (pending domain + VPS) — skill `.ai/skills/learnhouse-vps-clone-rebrand/SKILL.md`

## Current Status

Updated 2026-07-23:

| Area | Status |
|---|---|
| Azzam LearnHouse dashboard | Live: `https://learn.azzamedu.com/dash/courses` |
| Alex Mentor LearnHouse | Live: `https://learn.alex-mentor.com/` |
| Tom Bennett LearnHouse | Live: `https://learn.tom-edu.com/` |
| Eddric LearnHouse | Pending next clone |
| Course library | 4 courses live (per instance) |
| Provisioning | Manual user creation/enroll remains the supported MVP workflow |
| Next ops focus | Eddric VPS clone + QA learner access / checkout handoff |

---

## Key Docs

| Doc | When to read |
|---|---|
| `PRODUCTION-DEPLOY-RUNBOOK.md` | Cold VPS install -> live site |
| `admin-setup-checklist.md` | Dashboard setup, groups, SMTP, test users |
| `../../playbook/ops/learnhouse-provision-sop.md` | Daily user creation and access SOP |
| `SCRIPTS-REFERENCE.md` | What each script in `scripts/` does |
| `docs/EDITING-GUIDE.md` | Day-to-day content edits and sync workflow |
| `local-test-guide.md` | Local instance on Windows + Docker Desktop |

---

## Access Model

Use LearnHouse **UserGroups** as the source of truth. Add users to the right group, then enroll the user/group into the matching courses.

| Access case | Dashboard group / slug | Courses / access |
|---|---|---|
| Course 1 only | `smc-cours` | Advanced SMC Course |
| Course library | course-specific group(s) | 4 live LearnHouse courses |
| VIP $1000 | `vip-1000` | VIP access + 1-2 bonus courses |
| Deposit $3k-$5k | `deposit-3k-5k` | Mid-tier course bundle |
| Deposit >$5k-$10k | `full-access` | Full course library |

Example user provision:

```text
Email: hoangvu.linhan2805@gmail.com
Username: hoangvulinhan2805
Group: smc-cours
Course: Advanced trading course : The complete Smart Money Concepts
```

Standard flow:

```text
Verify payment/access -> create user via /signup -> test login -> assign UserGroup -> enroll course -> spot-check -> send login -> record ops log
```

---

## Quick Start: Manual Provision

1. Open incognito: `https://learn.azzamedu.com/signup`
2. Create account with customer email and vault-saved password.
3. Test login: `https://learn.azzamedu.com/login`
4. Go to **Users -> UserGroups -> Manage Users**.
5. Add the user to the correct group.
6. Go to **Courses** and enroll the user/course if group access is not automatic.
7. Login as the user and confirm course visibility.
8. Send login via Brevo/Gmail/Zalo.
9. Log the action in Woo/order sheet/CRM.

Manual signup remains the fallback until SMTP invite flow is tested.

---

## SMTP Quick Note

For LearnHouse **Invite Members**, configure SMTP with Brevo if the dashboard exposes email settings.

```text
Host: smtp-relay.brevo.com
Port: 587
Encryption: STARTTLS / TLS
Username: Brevo SMTP login
Password: Brevo SMTP key
From email: verified sender email
From name: Azzam Gold
```

Test one internal inbox before inviting real customers.

---

## Repo Layout

```text
web/learnhouse/
├── PRODUCTION-DEPLOY-RUNBOOK.md
├── SCRIPTS-REFERENCE.md
├── admin-setup-checklist.md
├── docs/EDITING-GUIDE.md
├── local-test-guide.md
├── content/
│   ├── udemy-clone-curriculum.json
│   ├── udemy-original/
│   ├── apprentice-operating-course/
│   ├── worksheets/
│   └── vip-resource-library/
└── scripts/
    ├── deploy-production.ps1
    ├── deploy-vps.py / vps-bootstrap.sh
    ├── seed-udemy-clone.py
    ├── sync-udemy-clone.py
    ├── sync-local-to-prod.py
    ├── audit-local-vs-prod.py
    └── create-users.py
```

---

## MVP Acceptance

- [x] `npx learnhouse doctor` passes on VPS
- [x] HTTPS live at `https://learn.azzamedu.com`
- [x] HTTPS live at `https://learn.alex-mentor.com/`
- [x] 4 LearnHouse courses live
- [x] Primary course published and visible to `smc-cours` users
- [ ] Test learner can complete first lesson on mobile
- [ ] Manual provision dry-run completed under 24h SLA
- [ ] SMTP invite tested, or manual signup fallback documented
- [ ] `qg-lms-checklist.md` signed off

---

## Direct Udemy Import

For a new Udemy course that should go straight into an existing production LearnHouse course, use the direct import SOP:

`docs/DIRECT-UDEMY-IMPORT-GUIDE.md`

Standard naming:

```text
Skill: learnhouse-production-sync
Workflow: Direct Udemy -> Existing Course Import
Operator/agent: Course Import Operator
```

Use this when the user provides both a Udemy source URL and a target `https://learn.azzamedu.com/course/<uuid>` URL. Confirm the API UUID first, create only missing chapters/lessons, copy metadata as-is, then attach videos/resources to the matching lessons. Do not use the old SMC seed script for this path.

MTF case script:

```text
scripts/import-mtf-skeleton.py
```
