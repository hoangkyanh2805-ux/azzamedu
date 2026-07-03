# 8 — Sprint Roadmap

> **Horizon:** ~6 weeks to MVP bot live (parallel with website G3)

---

## S0 — Foundation (Week 1)

| Task | Output | Done when |
|------|--------|-----------|
| Kickstart pack reviewed | This folder | Team aligned |
| BotFather bot created | Token in vault | Test `/start` locally |
| Pick Supabase vs Sheets | Decision log | DB connection works |
| Schema applied | Tables/sheets | CRUD smoke test |
| Config template | `config.yaml` | URLs + SKUs filled |
| Compliance templates draft | `bot/templates/` | Disclaimer on start |

**Exit:** Polling bot echoes `/start` + disclaimer.

---

## S1 — Core user flows (Week 2)

| Task | Output | Done when |
|------|--------|-----------|
| `/offers` all 5 products | Inline URLs | Links open |
| `/status` | Tier display | Test users see correct tier |
| `/pay` + proof FSM | Queue row | Admin notified |
| `/support` | Tickets | Admin notified |
| `/link` email | Member update | Email stored |
| Main menu keyboard | UX | All buttons work |

**Exit:** Manual test script A–D in `04-user-journey.md` passes.

---

## S2 — Admin + provision (Week 3)

| Task | Output | Done when |
|------|--------|-----------|
| `/admin pending/confirm/...` | Commands | State transitions work |
| LH + VIP message templates | templates | Compliance review |
| Notify admin chat | `notify.py` | <5s delivery |
| Dry run with `.ai/commands/telegram-provision.md` | Audit log | G4+G5 simulated |
| Deploy staging VPS | systemd | 24h uptime test |

**Exit:** One test member provisioned end-to-end on staging.

---

## S3 — Hardening + launch (Week 4)

| Task | Output | Done when |
|------|--------|-----------|
| Compliance PASS all templates | audit file | G1-bot |
| Production deploy | webhook mode | BotFather commands set |
| TY page bot link | WordPress | ?start= deep link |
| Ops sheet/runbook training | Admin | Queue cleared <24h |
| `10-mvp-launch-checklist.md` | All boxes | Owner sign-off |

**Exit:** Live bot with real paid test (sandbox or low-tier).

---

## S4 — Mini App + webhook prep (Week 5–6, optional)

| Task | Output | Done when |
|------|--------|-----------|
| Mini App status UI | `miniapp/` | Opens in Telegram |
| Webhook receiver stub | FastAPI route | Test payload logged |
| Supabase migration from Sheets | If needed | No data loss |

**Exit:** P2 ready per `12-future-webhook-plan.md`.

---

## Critical path

```text
S0 schema → S1 /pay + /status → S2 admin confirm → G4 human → S3 launch
```

**Blocked if:** G0 pricing unset, G3 checkout not live, Compliance FAIL.

---

## Defer

| Item | Sprint |
|------|--------|
| Inner Circle automation | Post-S4 |
| Brevo bi-sync | S4+ |
| LearnHouse API | S4+ |
| Auto VIP invite | Policy decision |

---

## Milestones

| Milestone | Target |
|-----------|--------|
| M1 — Dev bot working | End S1 |
| M2 — Provision dry run | End S2 |
| M3 — Production G1-bot | End S3 |
| M4 — Webhook beta | End S4 |
