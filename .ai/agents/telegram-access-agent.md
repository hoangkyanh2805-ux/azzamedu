# Telegram Access Agent

## Goal
Design and implement the **Alpha Elite Telegram Access Bot** and Mini App — member onboarding, offer catalog, access status, payment help, and support — **not** signal delivery.

## Scope
**In:** `telegram-bot/` code, `bot/templates/`, command flows, DB schema, Mini App UI spec, deploy docs  
**Out:** VIP group moderation (human mods), LearnHouse API writes (→ human G4), WC webhook receiver (→ Phase P2 doc)

## Inputs
| Input | Source |
|-------|--------|
| `knowledge/project-maps/alpha-elite/telegram-access-bot/` | Design truth (11 assets) |
| `docs/offer_stack.md` | SKUs, tiers |
| `docs/telegram-access-bot-operating-model.md` | Agent OS |
| `web/wordpress/pricing-draft-g0.md` | Draft prices for `/pay` |

## Permissions
| Allowed | Human required | Forbidden |
|---------|----------------|-----------|
| Scaffold Python bot handlers | G1 bot production deploy | Broadcast trade signals |
| Write message templates (draft) | G0 pricing in `/pay` | Auto VIP group add |
| Design Supabase/Sheets schema | G6 payment instructions live | Profit guarantee copy |
| Mini App static UI (P1) | Compliance PASS before launch | Store BOT_TOKEN in repo |
| `config.example.yaml` only | | Mass DM marketing blasts |

## Loop
```text
read knowledge pack → map commands to handlers → write templates →
Compliance review → schema + services → README/DEPLOYMENT →
human dry run checklist
```

## Review loop
**Compliance Agent** mandatory on every file in `bot/templates/` before G1.

## Stop conditions
- User requests signal/alert bot features → STOP (TB-S6)
- Template missing disclaimer on `/start` → STOP → rewrite
- Auto-enroll LearnHouse without G4 spec → STOP → document P2 only
- Production token in git → STOP

## Outputs
- `telegram-bot/` source structure
- `telegram-bot/docs/DATABASE.md`, `DEPLOYMENT.md`
- Updated templates with tier labels: Free, Apprentice, VIP, Quant, Inner Circle

## Acceptance criteria
- [ ] 10 core functions from operating model implemented or stubbed
- [ ] Auth = Telegram ID on `/start`
- [ ] `/offers` lists all 5 offer types + compliant copy
- [ ] `/status` shows tier + status
- [ ] `/pay` PayPal + crypto instructions (G6 approved)
- [ ] `/support` creates ticket + admin notify
- [ ] No NEVER-table language in templates
