# LearnHouse LMS Course Map — Alpha Elite

## Purpose
Self-hosted course structure for Apprentice Operating Course and VIP resource delivery. Commerce stays on WooCommerce; learning stays on LearnHouse.

---

## Role in stack

| System | Job |
|--------|-----|
| WooCommerce | Payment + order truth |
| LearnHouse | Course delivery, progress |
| YouTube Unlisted | Video hosting (embed only) |
| Brevo | Access-ready email |
| Admin | Manual enroll ≤ 24h (MVP) |

```text
Payment → Admin creates user → Enroll by SKU → access_ready email → (VIP) Telegram
```

---

## Infrastructure

```bash
npx learnhouse@latest setup
npx learnhouse start
npx learnhouse doctor
npx learnhouse backup   # weekly
```

**Host:** `learn.[domain].com` · VPS 2 vCPU / 4GB · Docker

---

## Organization

```text
Alpha Elite (org)
├── Apprentice Operating Course
├── VIP Resource Library
└── User groups:
    ├── apprentice-students
    ├── vip-members
    └── quant-desk (phase 2)
```

---

## Course — Apprentice Operating Course

| Field | Value |
|-------|-------|
| Slug | `apprentice-operating-course` |
| Language | **English** (Canada + EU customer standard) |
| Access | Paid — manual enroll |
| Tone | System-first, no hype intros |
| Content repo | `web/learnhouse/content/` |

### Module map (v2 — SMC rebuild 2026-07-02)

| Module | Title | Lessons | Outcome |
|--------|-------|---------|---------|
| M1 | Operating Mindset & Desk Setup | 3 | Emotional vs structured execution |
| M2 | Market Structure Foundations | 7 | Liquidity, FVG, BOS, POI literacy |
| M3 | POI & Setup Framework | 5 | Trend/break + double POI documentation |
| M4 | Risk & Sizing Protocol | 4 | 2% framework + lot calc + risk gate |
| M5 | Session SOPs & Journal | 4 | Daily/weekly + process journal |
| M6 | Educational Case Walkthroughs | 5 | XAUUSD / loss review / session scorecard |
| M7 | Confirmation & Multi-TF Rules | 3 | Wait vs confirm; conflicting setups |
| M8 | Tools, Extension & VIP Path | 4 | Indicators literacy, Wyckoff intro, VIP |

**Total:** 35 lessons · ~7–10h video · worksheets + quizzes

Blueprint: `web/learnhouse/COURSE-REBUILD-MASTER.md`  
Source map: `web/learnhouse/content/source-analysis/purchased-smc-course-map.md`

Lesson drafts: `web/learnhouse/content/apprentice-operating-course/`  
Manifest + worksheet index: `web/learnhouse/content/course-manifest.md`

---

## Lesson template (every lesson)

1. **Objective** — one sentence  
2. **Video** — YouTube unlisted embed  
3. **Key points** — bullet summary  
4. **Worksheet** — downloadable  
5. **Compliance note** — "Education only. Trading involves risk."  

### Video intro script (15s, every video)
> This lesson is for education only. Trading involves substantial risk. Nothing here guarantees profit or constitutes investment advice.

---

## YouTube Unlisted policy

| Rule | Implementation |
|------|----------------|
| Visibility | Unlisted |
| Titles | Neutral: `AE Apprentice M2L1` |
| Thumbnails | No money imagery |
| Description | LearnHouse link + disclaimer |

---

## SKU → access matrix

| SKU | Group | Courses |
|-----|-------|---------|
| AE-APP-001 | apprentice-students | Apprentice |
| AE-VIP-MON/YR | vip-members | Apprentice + VIP Library |
| AE-QNT-001 | quant-desk | All + Quant (phase 2) |
| Gameplan free | — | No LMS |

---

## Manual provision SOP (summary)

| Step | Action | SLA |
|------|--------|-----|
| 1 | Verify paid order | < 4h |
| 2 | Create LearnHouse user | < 24h |
| 3 | Assign group + enroll | < 24h |
| 4 | Send Brevo `access_ready` | < 24h |
| 5 | VIP: Telegram add | < 24h |
| 6 | Order note: provisioned date | — |

Full SOP: `playbook/ops/learnhouse-provision-sop.md`

---

## VIP Resource Library (structure)

| Section | Content type |
|---------|--------------|
| SOP Archive | PDFs, checklists |
| Automation docs | Setup guides (education) |
| Trade idea format | How to read structured ideas — not alerts |
| Office hours | Links/recordings if applicable |

**Compliance:** No "copy this trade for guaranteed win" framing.

Detail: `web/learnhouse/content/vip-resource-library/README.md`

---

## Metrics

| Metric | Target |
|--------|--------|
| Provision SLA | < 24h |
| Module 1 completion (7d) | ≥ 60% |
| Full course (30d) | ≥ 40% |

---

## Phase 2

- LearnHouse API auto-enroll from WooCommerce webhook  
- Completion certificates  
- Quant Desk course module  

---

## Acceptance criteria

- [ ] ≥ 3 modules live with unlisted video  
- [ ] Test student completes M1 on mobile  
- [ ] Manual provision tested end-to-end  
- [ ] All scripts pass compliance swap table  
