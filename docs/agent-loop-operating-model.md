# Agent Loop Operating Model — Alpha Elite

> **Core loop:** Goal → Observe → Plan → Act → Check → Stop → Human Approval  
> Designed via `agent-os-designer` for course + lead magnet + CRO + checkout funnel coordination.

---

## System objective

Coordinate **10 specialist agents** to build and maintain the Alpha Elite funnel:

```text
Skills → Offer → Lead Magnet → Landing Copy → CRO → Compliance → FunnelKit → LearnHouse → Brevo → Web Quality → Human Launch
```

**Positioning law (all agents):** Education, trade ideas, automation support, SOPs, community support — **not** signal group, guaranteed profit, risk-free, or passive-income bot.

**Source of truth:** `docs/project_brief.md` · `docs/compliance_guardrails.md`

---

## Agent roster

| # | Agent | Contract | Primary deliverable |
|---|-------|----------|-------------------|
| 1 | Repo Skill Librarian | `.ai/agents/repo-skill-librarian.md` | Skill index, install map, routing |
| 2 | Offer Architect | `.ai/agents/offer-architect.md` | Offer stack, SKUs, ladder |
| 3 | Lead Magnet | `.ai/agents/lead-magnet-agent.md` | 2% Rule Gameplan blueprint + copy |
| 4 | Landing Copy | `.ai/agents/landing-copy-agent.md` | Hero, sections, FAQ copy |
| 5 | CRO | `.ai/agents/cro-agent.md` | Page structure, forms, conversion |
| 6 | FunnelKit | `.ai/agents/funnelkit-agent.md` | Checkout, bump, upsell, TY |
| 7 | LearnHouse | `.ai/agents/learnhouse-agent.md` | Course map, lessons, provision SOP |
| 8 | Brevo Email | `.ai/agents/brevo-email-agent.md` | 7-day nurture + onboarding |
| 9 | Compliance | `.ai/agents/compliance-agent.md` | PASS/FAIL review gate |
| 10 | Web Quality | `.ai/agents/web-quality-agent.md` | Lighthouse, a11y, SEO gate |
| 11 | Telegram Access | `.ai/agents/telegram-access-agent.md` | Bot/Mini App, commands, deploy |
| 12 | Telegram Admin Ops | `.ai/agents/telegram-admin-ops-agent.md` | Provision queue, admin notify |

**Orchestration index:** `.ai/agents/README.md`  
**Telegram OS:** `docs/telegram-access-bot-operating-model.md`

---

## Multi-agent workflow (build funnel)

```text
Phase A — Foundation
  Repo Skill Librarian → Offer Architect
       ↓
Phase B — Attract
  Lead Magnet Agent → Landing Copy Agent → CRO Agent
       ↓
Phase C — Gate (mandatory)
  Compliance Agent → [FAIL: return to producer] → [PASS: continue]
       ↓
Phase D — Convert & Deliver
  FunnelKit Agent ∥ LearnHouse Agent ∥ Brevo Email Agent
       ↓
Phase E — Launch gate
  Web Quality Agent → Compliance Agent (re-check public URLs)
       ↓
Phase F — Human
  G1 Publish approval → deploy

Phase G — Telegram access layer (after G3 checkout live)
  Offer Architect → Telegram Access Agent + Telegram Admin Ops Agent
       ↓
  Compliance Agent → bot/templates PASS
       ↓
  Human G1-bot + G6 (payment text) → deploy telegram-bot/
       ↓
  Dry run: .ai/commands/telegram-provision.md (G4 + G5)
```

---

## Standard review loop (every customer-facing artifact)

```text
┌─────────────┐
│  Producer   │  Lead Magnet / Landing Copy / Brevo / etc.
│   Agent     │
└──────┬──────┘
       │ draft artifact
       ▼
┌─────────────┐
│ Compliance  │  Mandatory. No bypass.
│   Agent     │─── FAIL ──→ Producer revises (max 3 loops)
└──────┬──────┘
       │ PASS
       ▼
┌─────────────┐     (if web artifact)
│ Web Quality │─── FAIL ──→ CRO or Landing Copy fixes
│   Agent     │
└──────┬──────┘
       │ PASS
       ▼
┌─────────────┐
│ Human G1    │  Owner + compliance sign-off → publish
└─────────────┘
```

**Max revision loops:** 3 per artifact. After 3 FAILs → escalate to human with evidence.

---

## Global stop conditions

| # | Condition | Action |
|---|-----------|--------|
| S1 | Missing `compliance_guardrails.md` context | STOP — load rules first |
| S2 | User requests prohibited claims | STOP — escalate Compliance |
| S3 | Production write (WP, Woo, LearnHouse, Brevo live) | STOP — human gate |
| S4 | Pricing empty in `offer_stack.md` for checkout work | STOP — Offer Architect first |
| S5 | 3 consecutive Compliance FAILs | STOP — human review |
| S6 | Conflicting docs (offer vs funnel map) | STOP — Offer Architect reconciles |
| S7 | Missing credentials for external system | STOP — report safe options |

**Escalation format:** See `.ai/rules/stop-conditions.md`

---

## QA gates summary

| Gate | Owner agent | Blocks |
|------|-------------|--------|
| QG-COMP | Compliance | All publish |
| QG-WEB | Web Quality | Landing/checkout go-live |
| QG-OFFER | Offer Architect | FunnelKit SKU wiring |
| QG-FUNNEL | FunnelKit | Payment test |
| QG-LMS | LearnHouse | Course launch |
| QG-EMAIL | Brevo Email | Live automation send |

Full checklist: `docs/qa-gates.md`

---

## Human approval points

| Gate | Trigger | Approver |
|------|---------|----------|
| **G0** | Offer/pricing/SKU changes | Project owner |
| **G1** | Publish any public copy or page | Owner + Compliance |
| **G2** | Live Brevo campaign / automation | Owner + Compliance |
| **G3** | WooCommerce/FunnelKit live config | Tech + Owner |
| **G4** | LearnHouse user create / enroll | Admin ops |
| **G5** | Telegram VIP add | Admin ops |
| **G6** | Payment gateway / crypto process | Owner |
| **G7** | Compliance incident | Owner immediately |

Details: `docs/human-approval-gates.md`

---

## Permission principle

| Autonomous OK | Human required |
|---------------|----------------|
| Read docs, draft copy, audit, checklists | Publish, deploy, send live email |
| Skill mapping, wireframes in markdown | WooCommerce/LearnHouse/Brevo writes |
| Compliance scan (advisory) | Override Compliance FAIL |
| Test recommendations | Money, access, refunds |

Full matrix: `docs/permission-matrix.md`

---

## Logging & audit

| Event | Log path |
|-------|----------|
| Compliance PASS/FAIL | `.ai/audit/compliance/YYYY-MM-DD-<artifact>.md` |
| Web quality audit | `.ai/audit/web-quality/YYYY-MM-DD-<url>.md` |
| Human G1 approval | `.ai/audit/approvals/YYYY-MM-DD-<artifact>.md` |
| Agent stop/escalation | `.ai/audit/escalations/` |

---

## Superseded agents (v1 → v2)

| Old | Replaced by |
|-----|-------------|
| `funnel-builder.md` | FunnelKit Agent + CRO Agent |
| `landing-qa.md` | Web Quality Agent + CRO Agent |
| `compliance-reviewer.md` | Compliance Agent |
| `ops-provisioner.md` | LearnHouse Agent (human SOP section) |

---

## Acceptance criteria

- [ ] All 10 agent contracts exist with full template fields
- [ ] Every customer-facing path goes through Compliance Agent
- [ ] Web pages go through Web Quality Agent before G1
- [ ] No agent autonomously publishes or provisions customers (MVP)
- [ ] `docs/qa-gates.md` and permission matrix complete
