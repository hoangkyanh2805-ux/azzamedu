# Project Brief — Alpha Elite Course + Funnel

## Mission

Build an **MVP web system** that:

1. **Captures leads** via WordPress/Elementor landing  
2. **Delivers** the free **Alpha Elite Gameplan** (2% Rule operating framework)  
3. **Sells** the **Apprentice Operating Course** (LearnHouse + WooCommerce)  
4. **Upgrades** users into **VIP Private System** (membership + Telegram)  
5. **Routes** serious users into **Quant Desk** / **Inner Circle**  
6. **Offers** **Done-With-You Bot & Broker Setup** as implementation ascension  

**Positioning:** Private financial operating system — education, trade ideas, automation support, SOPs, community support. **Not** a signal group.

---

## One-line objective

Launch a compliant, premium funnel that moves traffic → Gameplan → Apprentice → VIP → Quant / Inner Circle with manual LMS + Telegram provision ≤ 24h.

---

## Core offer stack

| # | Offer | Role in MVP |
|---|-------|-------------|
| 1 | **Free Alpha Elite Gameplan** | Lead magnet (2% Rule framework) |
| 2 | **Apprentice Operating Course** | First paid product |
| 3 | **VIP Private System** | Core membership |
| 4 | **Quant Desk** | Ascension tier |
| 5 | **Inner Circle** | High-touch (defer full launch) |
| 6 | **DWY Bot & Broker Setup** | Service / order bump |

Detail: `docs/offer_stack.md`

---

## Core stack

| Layer | Tool | MVP job |
|-------|------|---------|
| Landing | **WordPress / Elementor** | Capture leads, sell offers |
| Commerce | **WooCommerce** | Products, orders, subscriptions |
| Funnel | **FunnelKit** | Checkout, bump, upsell, thank-you |
| LMS | **LearnHouse** (self-host) | Apprentice + VIP course delivery |
| Email | **Brevo** | Gameplan delivery, 7-day nurture, onboarding |
| Video | **YouTube Unlisted** | Lesson hosting (embed in LearnHouse) |
| Pay | **PayPal** + **Crypto** (manual MVP) | Revenue |
| Community | **Telegram** | VIP private desk |

Architecture: `docs/mvp-system-map.md` · `docs/architecture.md`

---

## Primary funnel

```text
Traffic
  → Landing opt-in (Alpha Elite Gameplan)
  → Brevo instant PDF + 7-day nurture
  → Apprentice Operating Course (FunnelKit checkout)
  → Upsell: VIP Private System
  → Ascension: Quant Desk / Inner Circle
  → DWY Bot & Broker Setup (bump / service)
  → Telegram onboarding (VIP+)
```

---

## Problem

Retail traders execute on emotion, confuse signal groups with systems, and churn without SOPs, nurture, or accountability. Alpha Elite sells **structure** — not alerts or guaranteed returns.

---

## Positioning (non-negotiable)

| IS | IS NOT |
|----|--------|
| Private financial operating system | Signal group |
| Education, trade ideas, SOPs, automation support | Guaranteed profit |
| 2% risk discipline | Risk-free trading |
| Premium, system-first | Hype, passive-income bot |

---

## Target user

| Persona | Entry | Ascension |
|---------|-------|-----------|
| Curious Operator | Alpha Elite Gameplan → Apprentice | VIP |
| Serious Operator | Apprentice → VIP | Quant Desk |
| Capital Allocator | VIP | Quant / Inner Circle / DWY |

---

## MVP success metrics (30 days)

| Metric | Target |
|--------|--------|
| VIP paid conversions / week | ≥ 3 |
| Lead → Email #1 open (48h) | ≥ 45% |
| Apprentice Module 1 done (7d) | ≥ 60% |
| Payment → access email | < 24h |
| Refund / chargeback rate | < 3% |

---

## In scope

- Full stack listed above
- Manual LearnHouse user + Telegram provision
- Compliance + web quality gates (Agent OS)
- ≥ 3 LearnHouse modules for Apprentice

## Out of scope (defer)

- LearnHouse auto-enroll API
- Inner Circle full cohort
- SSO, affiliate, paid ads scale
- Guaranteed-return or signal-group positioning

---

## Constraints

- **Compliance:** No profit guarantees, risk-free claims, passive bot income. Always include trading risk disclaimer.  
- **Access:** Manual provision ≤ 24h post-payment  
- **Voice:** Premium, anti-hype — `knowledge/distilled/principles/anti-hype-qualification.md`

---

## Agent OS

10 agents coordinate build + review: `.ai/agents/README.md`  
Orchestration: `docs/agent-loop-operating-model.md`

---

## Related docs

| Doc | Purpose |
|-----|---------|
| `docs/mvp-system-map.md` | End-to-end MVP system |
| `docs/offer_stack.md` | Tiers, SKUs, pricing |
| `docs/launch_checklist.md` | Go-live |
| `docs/compliance_guardrails.md` | Copy rules |

---

## Acceptance criteria

- [ ] Mission funnel testable end-to-end (opt-in → pay → access)
- [ ] All six offers documented with compliant promises
- [ ] Stack wired per `mvp-system-map.md`
