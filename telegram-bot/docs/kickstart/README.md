# Alpha Elite Telegram Access Bot — Kickstart Pack

> **Orchestrated via:** `project-kickstart-os`  
> **Parent repo:** Alpha Elite (`webkhoahoc`)  
> **Agent OS:** `docs/telegram-access-bot-operating-model.md`  
> **Knowledge pack:** `knowledge/project-maps/alpha-elite/telegram-access-bot/`

---

## Artifact index

| # | Document | Purpose |
|---|----------|---------|
| 1 | [01-project-mission.md](01-project-mission.md) | Mission, audience, success metrics, non-goals |
| 2 | [02-stack-architecture.md](02-stack-architecture.md) | Components, integrations, deployment view |
| 3 | [03-bot-command-map.md](03-bot-command-map.md) | Commands, menus, handlers |
| 4 | [04-user-journey.md](04-user-journey.md) | Member flows end-to-end |
| 5 | [05-admin-journey.md](05-admin-journey.md) | Ops, provision, approval |
| 6 | [06-database-schema.md](06-database-schema.md) | Tables, enums, MVP datastore |
| 7 | [07-access-control-model.md](07-access-control-model.md) | Tiers, permissions, gates |
| 8 | [08-sprint-roadmap.md](08-sprint-roadmap.md) | Phases S0–S4 |
| 9 | [09-backlog.md](09-backlog.md) | Now / Next / Later / Blocked |
| 10 | [10-mvp-launch-checklist.md](10-mvp-launch-checklist.md) | Go-live gates |
| 11 | [11-compliance-checklist.md](11-compliance-checklist.md) | Trading-claims guardrails |
| 12 | [12-future-webhook-plan.md](12-future-webhook-plan.md) | WooCommerce → bot path |

---

## MVP rule (canonical)

```text
Payment or apply request
  → admin review
  → admin creates LearnHouse user (G4)
  → admin approves Telegram VIP access (G5)
  → bot sends instructions
```

Manual access is **acceptable** at MVP.

---

## Code & deploy

| Path | Content |
|------|---------|
| `telegram-bot/` | Python source (scaffold) |
| `telegram-bot/docs/DEPLOYMENT.md` | systemd, Docker, env |
| `telegram-bot/docs/DATABASE.md` | Full SQL DDL |
| `.ai/agents/telegram-access-agent.md` | Build agent |
| `.ai/commands/telegram-provision.md` | Human provision |

---

## Start here (week 1)

1. Read `01-project-mission.md` + `11-compliance-checklist.md`  
2. Pick Supabase **or** Sheets (`06-database-schema.md`)  
3. Execute sprint S0 in `08-sprint-roadmap.md`  
4. Track tasks in `09-backlog.md`
