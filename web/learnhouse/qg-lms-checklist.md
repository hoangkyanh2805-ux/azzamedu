# QG-LMS Quality Gate — LearnHouse

Run before soft launch. Owner: **Compliance + Ops**.

Reference: `.ai/agents/learnhouse-agent.md` acceptance criteria.

---

## Infrastructure

- [ ] `npx learnhouse doctor` passes on production VPS
- [ ] HTTPS valid at `https://learn.[domain].com`
- [ ] Admin credentials in secure vault (not in repo)
- [ ] Weekly backup cron configured

---

## Course structure

- [ ] Apprentice Operating Course live with 5 modules
- [ ] ≥ 3 modules (M1–M3) have full lesson body + compliance note
- [ ] VIP Resource Library shell exists (VIP group only)
- [ ] User groups: `apprentice-students`, `vip-members`

---

## Compliance (every lesson)

- [ ] Video intro script (15s) present or recorded on every video
- [ ] No guaranteed profit / passive income / signal-group language
- [ ] Compliance note at bottom of every lesson:
  > *Education only. Trading involves substantial risk. Nothing here guarantees profit or constitutes investment advice.*
- [ ] YouTube titles neutral (`AE Apprentice M#L#`)
- [ ] Thumbnails: no money imagery

---

## Content quality

- [ ] Each lesson has: objective, key points, worksheet link (where applicable)
- [ ] Worksheets downloadable (PDF or LH attachment)
- [ ] M1 completion path clear for new student
- [ ] M5 does not promise VIP results — upgrade framing only

---

## Access matrix

- [ ] AE-APP-001 → Apprentice only (tested)
- [ ] AE-VIP-MON/YR → Apprentice + VIP Library (tested)
- [ ] AE-DWY-001 → no LMS enrollment change (documented)

---

## Ops integration

- [ ] `playbook/ops/learnhouse-provision-sop.md` dry-run complete
- [ ] Brevo `access_ready` email sends correct LH URL
- [ ] Telegram bot `LEARNHOUSE_URL` matches production
- [ ] Provision SLA test: sandbox order → login < 24h

---

## UX

- [ ] Test student completes M1 on mobile
- [ ] Video embed plays on mobile
- [ ] Progress tracking updates after lesson complete

---

## Sign-off

| Role | Name | Date | PASS/FAIL |
|------|------|------|-----------|
| Content | | | |
| Compliance | | | |
| Ops | | | |

**FAIL items block paid traffic to Apprentice checkout.**
