# MVP Build Map — Alpha Elite

> Phases, critical path, defer/delete decisions. Orchestrated by project-kickstart-os.

---

## Critical path

```text
Compliance docs → Lead magnet → Landing opt-in → Brevo nurture
    → WooCommerce products → FunnelKit checkout
    → LearnHouse course (min 3 modules) → Manual provision SOP
    → Telegram VIP SOP → End-to-end test → Soft launch
```

**Bottleneck dự kiến:** LearnHouse content + manual ops SLA.

---

## Phase map

| Phase | Tuần | Deliverable | Acceptance |
|-------|------|-------------|------------|
| P0 Docs | 0 | All `docs/*.md` | Stakeholder sign-off |
| P1 Lead + Landing | 1 | Gameplan PDF + opt-in live | Test opt-in works |
| P2 Checkout | 2 | Apprentice + VIP purchasable | Sandbox payment PASS |
| P3 LMS | 2 | LearnHouse 3 modules | Test user completes M1 |
| P4 Email | 2 | Brevo sequences 1–3 | Automation walkthrough |
| P5 Ops | 2–3 | Provision + Telegram SOP | <24h SLA test |
| P6 QA + Launch | 3 | Full funnel test | `launch_checklist.md` 80%+ |

---

## Build vs buy vs defer

| Item | Decision | Lý do |
|------|----------|-------|
| Landing WP/Elementor | **Build** on existing | Team familiarity |
| LMS LearnHouse | **Self-host** | No platform fees, ownership |
| Email Brevo | **Buy** SaaS | Fast automation |
| Checkout FunnelKit | **Buy** plugin | Bump/upsell native |
| LearnHouse auto-enroll | **Defer** | Manual OK for MVP volume |
| Crypto payments | **Defer** manual | Complexity |
| Inner Circle | **Defer** | Capacity |
| SSO | **Delete** from MVP | Unnecessary early |

---

## Deletion / defer list

**Không làm trong MVP:**
- Affiliate program
- Multi-language EN site
- Mobile app
- Public signal channel
- Automated Telegram bot onboarding
- LearnHouse payments module (enterprise)
- Complex analytics warehouse

---

## Resource estimate

| Role | Hours (MVP) |
|------|-------------|
| Content (Gameplan + course) | 40–60h |
| WP/Elementor dev | 20–30h |
| FunnelKit setup | 8–12h |
| LearnHouse setup + content | 16–24h |
| Brevo automations | 8–12h |
| Ops SOP + testing | 8h |

---

## Risk register

| Risk | Impact | Mitigation |
|------|--------|------------|
| Compliance copy slip | High | Review gate + agent rules |
| Provision delay >24h | Medium | SOP + admin alerts |
| Low opt-in rate | Medium | CRO framework A/B |
| LearnHouse downtime | Medium | Weekly backup, monitoring |
| PayPal dispute | Medium | Clear refund policy |

---

## Definition of done (MVP)

MVP **done** khi một người lạ có thể:
1. Tìm landing từ link
2. Opt-in và nhận Gameplan
3. Mua Apprentice qua PayPal
4. Nhận LearnHouse access trong 24h
5. Hoàn thành Module 1
6. (Optional VIP path) Được add Telegram

---

*Xem chi tiết sprint: `docs/first-sprint.md`*
