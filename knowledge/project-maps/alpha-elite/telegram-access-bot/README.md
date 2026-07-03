# Alpha Elite — Telegram Access Bot Knowledge Pack

> **Pipeline:** knowledge-asset-factory  
> **Source:** Telegram Shop Bot / Mini App case study (Fiverr-style feature set) → Alpha Elite member access infrastructure  
> **Status:** MVP design · not production code  
> **Last updated:** 2026-07-01

---

## What this is

Reusable knowledge assets for building a **Telegram Bot + Mini App** that handles member access, onboarding, support, and manual payment routing — **not** a signal-spam or alert bot.

Primary website checkout remains **WordPress / WooCommerce / FunnelKit**. Telegram is the **post-purchase access layer** and optional discovery channel.

---

## Asset index

| # | Asset | File |
|---|--------|------|
| 1 | Project context | [01-project-context.md](01-project-context.md) |
| 2 | Fiverr case mapping | [02-fiverr-case-mapping.md](02-fiverr-case-mapping.md) |
| 3 | Telegram layer in funnel | [03-telegram-layer-funnel-role.md](03-telegram-layer-funnel-role.md) |
| 4 | MVP scope | [04-mvp-scope.md](04-mvp-scope.md) |
| 5 | Offer menu map | [05-offer-menu-map.md](05-offer-menu-map.md) |
| 6 | User access status model | [06-user-access-status-model.md](06-user-access-status-model.md) |
| 7 | Admin workflow | [07-admin-workflow.md](07-admin-workflow.md) |
| 8 | Manual payment flow | [08-manual-payment-flow.md](08-manual-payment-flow.md) |
| 9 | LearnHouse delivery flow | [09-learnhouse-delivery-flow.md](09-learnhouse-delivery-flow.md) |
| 10 | Compliance guardrails | [10-compliance-guardrails.md](10-compliance-guardrails.md) |
| 11 | Future webhook plan | [11-future-webhook-plan.md](11-future-webhook-plan.md) |

---

## Related repo artifacts

| Topic | Path |
|-------|------|
| Offers + SKUs | `docs/offer_stack.md` |
| User journey | `docs/user-journey.md` |
| LearnHouse provision | `playbook/ops/learnhouse-provision-sop.md` |
| Telegram VIP add | `playbook/ops/telegram-onboarding-sop.md` |
| Compliance (global) | `docs/compliance_guardrails.md` |
| Provision command | `.ai/commands/provision-customer.md` |

---

## Source inventory

| Source | Type | Confidence | Notes |
|--------|------|------------|-------|
| User brief (Telegram Shop Bot / Mini App features) | Requirements | High | Feature list provided in chat |
| Generic Fiverr Telegram shop patterns | Inferred pattern | Medium | Not verbatim gig text — mapped by mechanism |
| Alpha Elite `docs/` + `playbook/` | Project truth | High | SKUs, SOPs, compliance already defined |
| WooCommerce / FunnelKit maps | Integration context | High | `docs/funnelkit_checkout_map.md` |

---

## Agent OS (implementation)

| Doc | Path |
|-----|------|
| Operating model | `docs/telegram-access-bot-operating-model.md` |
| **Kickstart pack (12 artifacts)** | `telegram-bot/docs/kickstart/README.md` |
| Agent contracts | `.ai/agents/telegram-access-agent.md`, `telegram-admin-ops-agent.md` |
| Provision command | `.ai/commands/telegram-provision.md` |
| Source + deploy | `telegram-bot/` |

---

**`telegram-access-bot-builder`** — use when implementing bot handlers, Mini App UI, or ops queue. Depends on: `docs/compliance_guardrails.md`, `06-user-access-status-model.md`, `07-admin-workflow.md`.

---

## Next actions

1. Choose MVP datastore: **Google Sheets** (fastest) vs **Supabase** (scale) — see `04-mvp-scope.md`  
2. Scaffold Python bot (`python-telegram-bot` or `aiogram`) with menu from `05-offer-menu-map.md`  
3. Wire admin notifications before user-facing Mini App  
4. Defer WooCommerce webhooks until manual flow stable — `11-future-webhook-plan.md`
