# Backlog & Task Board — Alpha Elite

> **Kickstart artifact #6** · Kanban: **Now · Next · Later · Blocked · Done**  
> Update status as work moves. Owner = assign when ready.

---

## How to use

- **Now** — actively in progress this week  
- **Next** — queued after current Now items  
- **Later** — post-MVP / phase 2  
- **Blocked** — waiting on decision, access, or dependency  
- **Done** — completed (keep for reference; move old items quarterly)

---

## Now

| ID | Task | Owner | Output | Depends on |
|----|------|-------|--------|------------|
| N-01 | Fill pricing in `offer_stack.md` (Apprentice, VIP) | — | Prices in doc | G0 approval |
| N-02 | Write Alpha Elite Gameplan PDF v1 | — | `sales/assets/gameplan/` | Compliance review |
| N-03 | Set up Brevo: domain auth + list `gameplan-leads` | — | SPF/DKIM green | Domain access |
| N-04 | Build homepage hero + opt-in (Elementor) | — | `/` live | N-02, N-03, wireframes |
| N-05 | Brevo Email 0 + 7-day automation | — | QG-EMAIL ready | N-03, N-02 |

---

## Next

| ID | Task | Owner | Output | Depends on |
|----|------|-------|--------|------------|
| X-01 | Thank-you page `/gameplan-thank-you` | — | Page live | N-04 |
| X-02 | Legal pages (privacy, terms, risk, refund) | — | Footer links | Compliance |
| X-03 | `/apprentice` sales page copy + layout | — | Page live | N-01 |
| X-04 | WooCommerce SKU `AE-APP-001` + FunnelKit checkout | — | Sandbox buy | N-01, G3 |
| X-05 | LearnHouse VPS + `learnhouse setup` | — | HTTPS subdomain | VPS budget |
| X-06 | Apprentice modules 1–3 + YouTube unlisted | — | QG-LMS | X-05 |
| X-07 | Provision SOP dry run | — | Audit log | X-04, X-06 |
| X-08 | Landing web quality audit | — | `.ai/audit/web-quality/` | N-04 |

---

## Later

| ID | Task | Notes |
|----|------|-------|
| L-01 | VIP checkout `AE-VIP-MON/YR` + upsell | Sprint 3 |
| L-02 | Telegram VIP group + pinned rules | Sprint 3 |
| L-02b | **Telegram Access Bot** (full MVP) | `telegram-bot/docs/kickstart/` |
| L-03 | Quant Desk product + page stub | Post soft launch |
| L-04 | Inner Circle application flow | Phase 2 |
| L-05 | LearnHouse auto-enroll webhook | Phase 2 |
| L-06 | FunnelKit abandoned cart | Phase 2 |
| L-07 | Crypto gateway (NOWPayments etc.) | G6 |
| L-08 | Paid ads + UTM campaigns | After baseline metrics |
| L-09 | DWY service delivery playbook | After VIP live |
| L-10 | A/B headline tests | Post traffic |

---

## Blocked

| ID | Task | Blocker | Unblock |
|----|------|---------|---------|
| B-01 | Live PayPal checkout | Need G6 + business account verify | Owner completes PayPal |
| B-02 | Production domain DNS | Domain not finalized | Choose domain |
| B-03 | Final VIP monthly price | G0 pricing decision | Owner sets price |
| B-04 | Legal entity for disclaimer | Jurisdiction TBD | Legal counsel / owner |
| B-05 | Crypto payment SOP | Gateway not chosen | Pick provider |

---

## Done

| ID | Task | Completed |
|----|------|-----------|
| D-01 | Project mission doc | `docs/project-mission.md` |
| D-02 | Stack architecture doc | `docs/stack-architecture.md` |
| D-03 | Offer stack framework (6 tiers) | `docs/offer_stack.md` |
| D-04 | User journey map | `docs/user-journey.md` |
| D-05 | Sprint roadmap | `docs/sprint-roadmap.md` |
| D-06 | Kickstart folder structure | `docs/folder-structure.md` |
| D-07 | Human approval gates | `docs/human-approval-gates.md` |
| D-08 | MVP launch checklist | `docs/mvp-launch-checklist.md` |
| D-09 | Risk/compliance checklist | `docs/risk-compliance-checklist.md` |
| D-10 | Agent OS (10 agents) | `.ai/agents/` |
| D-11 | Lead magnet blueprint | `docs/lead_magnet_blueprint.md` |
| D-12 | Brevo 7-day sequence spec | `docs/brevo_email_sequence.md` |
| D-13 | FunnelKit checkout map | `docs/funnelkit_checkout_map.md` |
| D-14 | LearnHouse LMS map | `docs/learnhouse_lms_map.md` |
| D-15 | Landing CRO framework | `docs/landing_page_cro_framework.md` |
| D-16 | Compliance guardrails | `docs/compliance_guardrails.md` |
| D-17 | Web quality checklist | `docs/web_quality_checklist.md` |
| D-18 | MVP system map | `docs/mvp-system-map.md` |
| D-22 | Elementor gameplan thank-you spec | `web/wordpress/elementor-spec-gameplan-thank-you.md` |
| D-21 | Elementor hero + opt-in spec | `web/wordpress/elementor-spec-homepage-hero-optin.md` |
| D-20 | Landing page CRO design + wireframes | `web/wordpress/landing-page-cro-design.md` |
| D-23 | Telegram Access Bot kickstart pack | `telegram-bot/docs/kickstart/` |
| D-24 | Telegram bot Agent OS + contracts | `docs/telegram-access-bot-operating-model.md` |

---

## Telegram Access Bot (subproject)

**Task board:** `telegram-bot/docs/kickstart/09-backlog.md`  
**Sprint:** `telegram-bot/docs/first-sprint.md`  
**Launch:** `telegram-bot/docs/kickstart/10-mvp-launch-checklist.md`

## Weekly ritual

**Monday:** Move cards Now → Done; pull from Next → Now  
**Friday:** Update Blocked; log metrics; sync `sprint-roadmap.md`
