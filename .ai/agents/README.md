# Agent Roster — Alpha Elite

Route tasks to the correct specialist. **Compliance Agent** reviews all customer-facing outputs.

## Quick routing

| User intent | Agent |
|-------------|-------|
| Map/install GitHub skills | Repo Skill Librarian |
| Pricing, tiers, SKUs | Offer Architect |
| Alpha Elite Gameplan PDF/outline | Lead Magnet |
| Hero, FAQ, sales prose | Landing Copy |
| Page structure, forms, conversion | CRO |
| Checkout, bump, upsell, TY | FunnelKit |
| Course modules, LMS, provision | LearnHouse |
| 7-day email, onboarding | Brevo Email |
| Review copy for trading claims | Compliance |
| Lighthouse, a11y, SEO | Web Quality |
| Telegram bot / Mini App access layer | Telegram Access |
| Bot admin queue, provision handoff | Telegram Admin Ops |

## Build order

`Repo Skill Librarian` → `Offer Architect` → `Lead Magnet` + `Landing Copy` + `CRO` → **`Compliance`** → `FunnelKit` + `LearnHouse` + `Brevo Email` → **`Web Quality`** → **`Compliance`** → Human G1

**Telegram bot (parallel after G3):** `Offer Architect` → `Telegram Access` + `Telegram Admin Ops` → **`Compliance`** → Human G1 (bot) + G4/G5 dry run

## Contracts

1. [repo-skill-librarian.md](repo-skill-librarian.md)
2. [offer-architect.md](offer-architect.md)
3. [lead-magnet-agent.md](lead-magnet-agent.md)
4. [landing-copy-agent.md](landing-copy-agent.md)
5. [cro-agent.md](cro-agent.md)
6. [funnelkit-agent.md](funnelkit-agent.md)
7. [learnhouse-agent.md](learnhouse-agent.md)
8. [brevo-email-agent.md](brevo-email-agent.md)
9. [compliance-agent.md](compliance-agent.md)
10. [web-quality-agent.md](web-quality-agent.md)
11. [telegram-access-agent.md](telegram-access-agent.md)
12. [telegram-admin-ops-agent.md](telegram-admin-ops-agent.md)

## Global rules

- `.ai/rules/compliance-trading.md`
- `.ai/rules/stop-conditions.md`
- `.ai/rules/orchestration.md`
