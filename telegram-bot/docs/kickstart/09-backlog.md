# 9 — Backlog & Task Board

> **Project:** Alpha Elite Telegram Access Bot  
> **Update:** Weekly · move cards Now → Done

---

## Now (active)

| ID | Task | Owner | Output | Depends |
|----|------|-------|--------|---------|
| TB-N01 | Create BotFather bot + store token | — | Bot exists | — |
| TB-N02 | Choose Supabase vs Sheets | — | Decision in README | — |
| TB-N03 | Apply schema (`06-database-schema.md`) | — | Tables live | TB-N02 |
| TB-N04 | Implement `handlers/start.py` + disclaimer | — | `/start` works | TB-N01 |
| TB-N05 | Implement `handlers/offers.py` (5 offers) | — | Catalog | G0 URLs |
| TB-N06 | Draft `bot/templates/*.md` | — | All messages | Compliance |
| TB-N07 | Compliance review templates | — | PASS log | TB-N06 |

---

## Next

| ID | Task | Owner | Output | Depends |
|----|------|-------|--------|---------|
| TB-X01 | `/status` + tier labels | — | Status view | TB-N03 |
| TB-X02 | `/pay` + proof FSM | — | Queue + notify | TB-N03 |
| TB-X03 | `/support` tickets | — | Ticket + notify | TB-N03 |
| TB-X04 | Admin commands suite | — | `/admin *` | TB-X02 |
| TB-X05 | LH + VIP notify templates | — | Post-G4/G5 msgs | Compliance |
| TB-X06 | `notify.py` admin chat | — | Reliable push | TB-N01 |
| TB-X07 | Staging deploy (`DEPLOYMENT.md`) | — | systemd | TB-X04 |
| TB-X08 | WordPress TY bot deep link | — | `?start=order_` | Web TY live |

---

## Later

| ID | Task | Notes |
|----|------|-------|
| TB-L01 | Mini App dashboard | P1 |
| TB-L02 | WooCommerce webhook receiver | P2 — `12-future-webhook-plan.md` |
| TB-L03 | LearnHouse API enroll | P2b |
| TB-L04 | Brevo tag sync | Optional |
| TB-L05 | VI message locale | Post-MVP |
| TB-L06 | Inner Circle waitlist flow | P3 |

---

## Blocked

| ID | Task | Blocker | Unblock |
|----|------|---------|---------|
| TB-B01 | Live `/pay` amounts | G0 pricing | Owner sign `pricing-draft-g0.md` |
| TB-B02 | PayPal/crypto text live | G6 | Owner payment accounts |
| TB-B03 | Production bot G1-bot | Compliance + staging | TB-N07, TB-X07 |
| TB-B04 | WC order auto-link | P2 webhook | TB-L02 |

---

## Done

| ID | Task | Completed |
|----|------|-----------|
| TB-D01 | Knowledge pack (11 assets) | 2026-07-01 |
| TB-D02 | Agent OS operating model | 2026-07-01 |
| TB-D03 | Agent contracts T1/T2 | 2026-07-01 |
| TB-D04 | Kickstart pack (this folder) | 2026-07-01 |
| TB-D05 | Scaffold `telegram-bot/` + deploy docs | 2026-07-01 |

---

## Definition of done (per task)

- Code: handler tested locally + logged  
- Copy: Compliance PASS  
- Ops: documented in admin journey  
- Deploy: noted in CHANGELOG or audit log
