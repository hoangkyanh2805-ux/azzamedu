# AI Project Folder Structure — Alpha Elite

> Agent OS layer mapped to repo. Do not move production WP/LearnHouse files into `.ai/` — document paths only.

---

## Structure

```text
webkhoahoc/
├── README.md                          # Human + agent entrypoint
├── docs/                              # Project truth (agents read first)
│   ├── project_brief.md
│   ├── offer_stack.md
│   ├── compliance_guardrails.md
│   ├── lead_magnet_blueprint.md
│   ├── landing_page_cro_framework.md
│   ├── funnelkit_checkout_map.md
│   ├── learnhouse_lms_map.md
│   ├── brevo_email_sequence.md
│   ├── web_quality_checklist.md
│   ├── agent-loop-operating-model.md  # Orchestration
│   ├── permission-matrix.md
│   ├── human-approval-gates.md
│   └── qa-gates.md
│
├── .ai/                               # Agent operating system
│   ├── agents/                        # 10 agent contracts
│   │   ├── README.md                  # Roster + routing
│   │   ├── repo-skill-librarian.md
│   │   ├── offer-architect.md
│   │   ├── lead-magnet-agent.md
│   │   ├── landing-copy-agent.md
│   │   ├── cro-agent.md
│   │   ├── funnelkit-agent.md
│   │   ├── learnhouse-agent.md
│   │   ├── brevo-email-agent.md
│   │   ├── compliance-agent.md
│   │   └── web-quality-agent.md
│   ├── rules/                         # Laws all agents obey
│   │   ├── compliance-trading.md
│   │   ├── permission-matrix.md
│   │   ├── human-approval-gates.md
│   │   ├── stop-conditions.md
│   │   └── orchestration.md
│   ├── references/                    # Deep context on demand
│   │   └── skills-index.md
│   ├── commands/                      # Slash-style workflows
│   │   ├── audit-funnel.md
│   │   ├── pre-launch.md
│   │   └── provision-customer.md
│   └── audit/                         # Evidence logs
│       ├── compliance/
│       ├── web-quality/
│       ├── approvals/
│       └── escalations/
│
├── knowledge/                         # Distilled assets (factory output)
│   ├── distilled/principles/
│   ├── distilled/frameworks/
│   └── project-maps/alpha-elite/
│
├── playbook/ops/                      # Human SOPs agents reference
│   ├── learnhouse-provision-sop.md
│   └── telegram-onboarding-sop.md
│
├── sales/assets/                      # Copy drafts, PDFs
├── config/                            # Analytics, env templates
└── web/                               # WP/LearnHouse implementation notes
    ├── wordpress/
    └── learnhouse/
```

---

## Agent discoverability rules

| Question | Read first |
|----------|------------|
| What is this project? | `docs/project_brief.md` |
| What can we promise? | `docs/compliance_guardrails.md` |
| Which agent am I? | `.ai/agents/README.md` |
| What am I allowed to do? | `docs/permission-matrix.md` |
| When do I stop? | `.ai/rules/stop-conditions.md` |
| When do humans approve? | `docs/human-approval-gates.md` |
| Pre-launch checks? | `docs/qa-gates.md` |

---

## External systems (out of repo)

| System | Agent owner | Doc map |
|--------|-------------|---------|
| WordPress/Elementor | Landing Copy, CRO, Web Quality | `web/wordpress/` |
| WooCommerce + FunnelKit | FunnelKit | `docs/funnelkit_checkout_map.md` |
| LearnHouse | LearnHouse | `docs/learnhouse_lms_map.md` |
| Brevo | Brevo Email | `docs/brevo_email_sequence.md` |
| YouTube | LearnHouse | embed specs in LMS map |
| PayPal/Crypto | FunnelKit | G6 human |
| Telegram | LearnHouse + playbook | `playbook/ops/telegram-onboarding-sop.md` |

---

## `.codex/skills/` (optional)

Installed external skills referenced by Repo Skill Librarian. Not committed unless team chooses.

---

## Acceptance

- [ ] Every doc type has exactly one home path
- [ ] Agents never assume production credentials in repo
- [ ] Audit folder used for PASS/FAIL and approvals
