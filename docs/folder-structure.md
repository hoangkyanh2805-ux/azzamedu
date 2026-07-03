# Folder Structure — Alpha Elite (Kickstart)

> **Kickstart artifact #7** · Where every artifact lives. Do not move production WP/LMS into `.ai/`.

```text
webkhoahoc/
│
├── README.md                         # Project entry + kickstart index
│
├── docs/                             # ★ Project truth (read first)
│   ├── project-mission.md            # #1 Mission
│   ├── stack-architecture.md         # #2 Stack
│   ├── offer_stack.md                # #3 Offers + SKUs
│   ├── user-journey.md               # #4 Journeys
│   ├── sprint-roadmap.md             # #5 Sprints
│   ├── backlog.md                    # #6 Task board
│   ├── folder-structure.md           # #7 This file
│   ├── human-approval-gates.md       # #8 Approvals
│   ├── mvp-launch-checklist.md       # #9 Launch
│   ├── risk-compliance-checklist.md  # #10 Risk/compliance
│   │
│   ├── project_brief.md              # Extended brief
│   ├── mvp-system-map.md             # End-to-end flows
│   ├── requirements.md               # First-principles reqs (optional expand)
│   ├── architecture.md               # Short arch (mirror)
│   ├── mvp-build-map.md              # Phase map
│   ├── first-sprint.md               # Week 1–2 detail
│   ├── sop-ops-runbook.md            # Daily/weekly ops
│   │
│   ├── lead_magnet_blueprint.md
│   ├── landing_page_cro_framework.md
│   ├── funnelkit_checkout_map.md
│   ├── learnhouse_lms_map.md
│   ├── brevo_email_sequence.md
│   ├── compliance_guardrails.md
│   ├── telegram-access-bot-operating-model.md
│   ├── web_quality_checklist.md
│   ├── launch_checklist.md           # Extended launch (duplicate depth OK)
│   │
│   ├── agent-loop-operating-model.md
│   ├── permission-matrix.md
│   ├── qa-gates.md
│   └── ai-project-folder-structure.md
│
├── .ai/                              # Agent operating system
│   ├── agents/                       # 10 agent contracts
│   ├── rules/                        # compliance, permissions, stops
│   ├── commands/                     # pre-launch, audit-funnel, provision
│   ├── references/                   # skills-index
│   └── audit/                        # compliance, web-quality, approvals
│
├── knowledge/                        # Distilled knowledge (factory)
│   ├── distilled/principles/
│   ├── distilled/frameworks/
│   └── project-maps/alpha-elite/
│       └── telegram-access-bot/   # Bot / Mini App knowledge (11 assets)
│
├── playbook/ops/                     # Human SOPs
│   ├── learnhouse-provision-sop.md
│   └── telegram-onboarding-sop.md
│
├── sales/assets/                     # Copy drafts, PDFs, email HTML
│   ├── gameplan/
│   ├── landing-copy.md
│   └── brevo/
│
├── config/                           # GA4 events, env templates (no secrets)
│   └── analytics-events.md
│
├── telegram-bot/                     # Telegram Access Bot (Python)
│   ├── README.md
│   ├── bot/
│   └── docs/
│
└── web/                              # Implementation notes (not live WP)
    ├── wordpress/
    │   └── wireframes/
    └── learnhouse/
        └── content/
```

---

## External systems (not in repo)

| System | Notes path |
|--------|------------|
| WordPress live site | Hosting panel |
| LearnHouse Docker | VPS `learn.domain.com` |
| Brevo | app.brevo.com |
| PayPal | WooCommerce gateway |
| Telegram | Mobile app + group admin |

---

## File naming rules

- Kickstart artifacts: `kebab-case.md` in `docs/`  
- Agent contracts: `.ai/agents/{name}.md`  
- Audit logs: `.ai/audit/{type}/YYYY-MM-DD-{slug}.md`  
- Never commit: `.env`, API keys, customer PII exports  

---

## New file decision tree

| I'm creating… | Put it in… |
|---------------|------------|
| Mission/strategy | `docs/` |
| Customer copy draft | `sales/assets/` |
| Agent behavior | `.ai/agents/` or `.ai/rules/` |
| Human procedure | `playbook/ops/` |
| Telegram bot OS | `docs/telegram-access-bot-operating-model.md` |
| Launch evidence | `.ai/audit/` |
| Distilled framework | `knowledge/distilled/` |

---

## Acceptance

- [ ] Every kickstart artifact #1–10 exists in `docs/`
- [ ] `backlog.md` task board updated weekly
- [ ] No secrets in repo
