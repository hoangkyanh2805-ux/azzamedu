# SOP Ops Runbook — Alpha Elite

> Daily / weekly / monthly ops cadence.

---

## Roles

| Role | Trách nhiệm |
|------|-------------|
| **Admin Ops** | Order provision, Telegram, support tickets |
| **Content** | Course updates, newsletter, Gameplan versions |
| **Tech** | WP, LearnHouse, integrations |

---

## Daily (mỗi ngày làm việc)

| Time | Task | Input | Output |
|------|------|-------|--------|
| AM | Check WooCommerce new orders | Orders dashboard | Provision started |
| AM | Process pending provisions | Orders < 24h old | LearnHouse + email sent |
| AM | VIP Telegram adds | Username form submissions | Members added |
| PM | Support inbox / Telegram mod | User questions | Responses < 12h |
| PM | Log metrics | GA4, Brevo | Sheet update |

**SLA:** Payment → access email ≤ 24h.

---

## Weekly

| Day | Task |
|-----|------|
| Mon | Review funnel metrics (opt-in, sales, provision SLA) |
| Tue | Send weekly newsletter (Brevo) |
| Wed | LearnHouse content progress / student drop-off |
| Thu | Compliance spot-check new copy |
| Fri | `learnhouse backup` + order reconciliation |
| Fri | Sprint ops retro notes |

---

## Monthly

- [ ] LearnHouse update (staging first)
- [ ] Review `compliance_guardrails.md` effectiveness
- [ ] VIP member audit (active vs churned)
- [ ] Refund/chargeback review
- [ ] Backup restore test (LearnHouse)
- [ ] SSL cert check
- [ ] Gameplan / course content updates

---

## Provision SOP (summary)

Chi tiết: `playbook/ops/learnhouse-provision-sop.md`

1. Verify order paid
2. Create LearnHouse user
3. Enroll course by SKU
4. Send Brevo access email
5. VIP: add Telegram
6. Note order + timestamp

---

## Escalation

| Issue | Escalate to | SLA |
|-------|-------------|-----|
| Payment dispute | Project owner | 4h |
| LearnHouse down | Tech | 1h |
| Compliance complaint | Project owner + legal | 2h |
| Data breach suspect | Project owner | Immediate |

---

## Monitoring

| System | Check |
|--------|-------|
| WordPress | UptimeRobot |
| LearnHouse | `learnhouse doctor` weekly |
| Brevo | Deliverability dashboard |
| PayPal | Dispute notifications |

---

## Incident log

Ghi vào `.ai/audit/incidents/YYYY-MM-DD-[slug].md`:
- What happened
- Customer impact
- Root cause
- Fix
- Prevention

---

## Backup

| Asset | Method | Frequency |
|-------|--------|-----------|
| LearnHouse DB | `learnhouse backup` | Weekly |
| WordPress | Hosting backup / UpdraftPlus | Daily |
| Brevo | Export contacts | Monthly |
| Gameplan PDF | Git / drive version | On change |
