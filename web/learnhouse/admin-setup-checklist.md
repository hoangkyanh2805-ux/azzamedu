# LearnHouse Admin Setup Checklist

Run once after `deploy-guide.md` completes. Owner: **Admin Ops**.

**Fast path (local):** run `scripts/seed-course.ps1` — uploads 8 modules / 35 lessons via API.

---

## 1. Organization

- [ ] Log in at `https://learn.[domain].com` as admin
- [ ] Organization name: **Alpha Elite**
- [ ] Logo uploaded (dark/gold mark if available)
- [ ] Default language: **English**
- [ ] Footer / about: link to `hoa-homes.com` risk disclaimer

---

## 2. User groups

Create groups (Settings → Users / Groups — exact menu may vary by LH version):

| Group slug | Display name | Purpose |
|------------|--------------|---------|
| `apprentice-students` | Apprentice Students | AE-APP-001 |
| `vip-members` | VIP Members | AE-VIP-MON / AE-VIP-YR |
| `quant-desk` | Quant Desk | AE-QNT-001 (phase 2) |

- [ ] All three groups created
- [ ] Test user can be assigned to one group

---

## 3. Course — Apprentice Operating Course

| Field | Value |
|-------|-------|
| Title | Apprentice Operating Course |
| Slug | `apprentice-operating-course` |
| Visibility | Private / enrolled only |
| Language | English |

### Modules (create in order)

| # | Module title | Lessons |
|---|--------------|---------|
| M1 | Operating Mindset | 3 |
| M2 | The 2% Rule in Practice | 4 |
| M3 | Daily & Weekly SOPs | 3 |
| M4 | Automation Support Literacy | 2 |
| M5 | Path to VIP | 2 |

- [ ] Course shell created
- [ ] 5 modules created
- [ ] 14 lesson placeholders created (titles from `content/course-manifest.md`)

### Per-lesson paste workflow

For each lesson in `content/apprentice-operating-course/m0X-*.md`:

1. Copy **Objective** → lesson description
2. Paste **Key points** → lesson body (markdown)
3. Add **Compliance note** at bottom of body
4. Embed **YouTube unlisted** URL (when video ready)
5. Attach worksheet PDF from `content/worksheets/` (when exported)

- [ ] M1–M3 lessons fully pasted (MVP minimum)
- [ ] M4–M5 pasted or scheduled for week 2

---

## 4. Course — VIP Resource Library

| Field | Value |
|-------|-------|
| Title | VIP Resource Library |
| Slug | `vip-resource-library` |
| Access | vip-members group only |

Sections (from `content/vip-resource-library/README.md`):

- [ ] SOP Archive
- [ ] Structured Trade Idea Format
- [ ] Automation Support Docs
- [ ] Office Hours / Recordings (optional at launch)

---

## 5. Enrollment rules (MVP — manual)

LearnHouse MVP uses **manual enroll** per `playbook/ops/learnhouse-provision-sop.md`:

| SKU | Enroll in |
|-----|-----------|
| AE-APP-001 | Apprentice only |
| AE-VIP-MON/YR | Apprentice + VIP Library |
| AE-QNT-001 | All (when Quant live) |

- [ ] Admin can: Users → Add → assign group → enroll courses
- [ ] Spot-check: apprentice test user sees M1 only
- [ ] Spot-check: VIP test user sees both courses

---

## 6. YouTube video naming

| Rule | Example |
|------|---------|
| Unlisted only | — |
| Neutral title | `AE Apprentice M2L1` |
| No money thumbnails | Text or chart only |
| Description | LearnHouse link + education disclaimer |

- [ ] Video naming SOP shared with editor
- [ ] At least M1L1–M1L3 videos uploaded (or placeholders noted)

---

## 7. Test accounts

| Account | Group | Verify |
|---------|-------|--------|
| `test-apprentice@...` | apprentice-students | M1–M5 visible, VIP lib hidden |
| `test-vip@...` | vip-members | Both courses visible |

- [ ] Mobile: complete M1L1 on phone
- [ ] Worksheet download works
- [ ] Progress bar updates

---

## 8. Go-live sign-off

- [ ] `qg-lms-checklist.md` completed
- [ ] Provision SOP dry-run with test WooCommerce order
- [ ] Brevo `access_ready` template includes LH URL
- [ ] Bot `LEARNHOUSE_URL` updated

**Signed:** _______________ **Date:** _______________
