# Sprint Roadmap — Alpha Elite MVP

> **Kickstart artifact #5** · 3-sprint path to launch (~6 weeks). Adjust dates when team assigns owners.

---

## Binding constraint

**Value is blocked until Path A works:** opt-in → Gameplan email → at least one paid Apprentice test with manual LearnHouse access.

---

## Overview

| Sprint | Weeks | Goal | Exit criteria |
|--------|-------|------|---------------|
| **S0** | 0 | Ground truth + accounts | Docs signed, Brevo/PayPal ready |
| **S1** | 1–2 | Capture + nurture | Live opt-in, 7-day Brevo, Gameplan PDF |
| **S2** | 2–4 | Convert + deliver | Apprentice checkout + LearnHouse M1–3 |
| **S3** | 4–6 | VIP + launch | VIP flow, Telegram SOP, pre-launch gates |

---

## Sprint 0 — Ground truth (Week 0)

**Goal:** Accounts, domain, pricing decisions, compliance briefing.

| Deliverable | Verification |
|-------------|--------------|
| Pricing filled in `offer_stack.md` | No `[FILL]` for launch SKUs |
| Brevo domain authenticated | SPF/DKIM green |
| PayPal business connected | Sandbox works |
| LearnHouse VPS provisioned | `learnhouse doctor` OK |
| Compliance briefing | Team read `risk-compliance-checklist.md` |

---

## Sprint 1 — Capture + nurture (Weeks 1–2)

**Goal:** Lead magnet live.

| Deliverable | Verification |
|-------------|--------------|
| Alpha Elite Gameplan PDF v1 | Compliance PASS |
| Homepage + opt-in form | Test submit → Brevo |
| Email 0 + Days 1–7 automations | Walkthrough contact |
| Thank-you page | Redirect works |
| Legal pages stub | Footer links work |
| Landing CRO + web quality | Mobile ≥70, disclaimer present |

**Demo:** Stranger opts in, gets PDF in <5 min.

---

## Sprint 2 — Convert + deliver (Weeks 2–4)

**Goal:** Paid Apprentice with manual LMS access.

| Deliverable | Verification |
|-------------|--------------|
| `/apprentice` sales page | CTA → checkout |
| WooCommerce `AE-APP-001` | Add to cart |
| FunnelKit checkout + bump | Sandbox purchase |
| TY page + Brevo purchase tags | Tags fire |
| LearnHouse modules 1–3 + videos | Mobile playback |
| Provision SOP dry run | <24h on test order |

**Demo:** Sandbox buy → admin provision → student completes M1.

---

## Sprint 3 — VIP + launch (Weeks 4–6)

**Goal:** Full funnel + soft launch.

| Deliverable | Verification |
|-------------|--------------|
| VIP products + checkout | `AE-VIP-MON/YR` |
| VIP upsell post-Apprentice | Accept/decline paths |
| Telegram VIP + pinned rules | Compliance PASS pin |
| VIP onboarding emails | QG-EMAIL |
| Quant Desk page stub | CTA only OK for MVP |
| `mvp-launch-checklist.md` complete | G1 approval logged |
| Soft launch 10–20 warm leads | Metrics baseline |

**Demo:** Full journey test script (`user-journey.md`).

---

## Critical path

```text
1. Gameplan PDF + Brevo Email 0
2. Landing opt-in live
3. Apprentice checkout (PayPal)
4. LearnHouse Module 1 + provision SOP
5. Compliance + web quality gates
6. Soft launch
```

---

## Delete / defer

| Item | Decision | Reason |
|------|----------|--------|
| LearnHouse API auto-enroll | Defer | Manual OK at volume |
| Inner Circle cohort | Defer | Capacity |
| Crypto auto-gateway | Defer | Manual invoice MVP |
| Paid ads | Defer | Need baseline organic first |
| Affiliate program | Delete from MVP | Scope |

---

## Risks

| Risk | Mitigation | Stop if |
|------|------------|---------|
| Compliance copy slip | Compliance Agent + checklist | P0 before launch |
| Provision delay | Daily ops + alerts | SLA >48h repeated |
| LearnHouse downtime | Weekly backup | Extended outage |
| Signal-group perception | Positioning in every touchpoint | User research says “still signals” |

---

## Post-launch (Later sprints)

- Abandoned cart (FunnelKit)  
- LearnHouse webhook automation  
- Inner Circle application flow  
- Quant Desk full content  
- Crypto gateway (G6)  

Task detail: `backlog.md`
