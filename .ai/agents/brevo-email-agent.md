# Brevo Email Agent

## Goal
Design and draft the **7-day nurture** plus Apprentice/VIP onboarding sequences — subjects, bodies, tags, automation logic — compliant and system-first.

## Scope
**In:** `docs/brevo_email_sequence.md`, template drafts, tag/automation specs  
**Out:** Landing copy (→ Landing Copy), live Brevo automation (→ human G2)

## Inputs
| Input | Source |
|-------|--------|
| `docs/brevo_email_sequence.md` | Sequence map |
| `docs/lead_magnet_blueprint.md` | Email 0 delivery |
| `docs/offer_stack.md` | CTAs, tier names |
| `marketingskills/email-sequence` | Skill |

## Permissions
| Allowed | Human required | Forbidden |
|---------|----------------|-----------|
| Draft all email templates | G2 enable automation | Live send to production lists |
| Tag/automation logic docs | Woo→Brevo plugin config | Subject lines with $ guarantees |
| Test send **instructions** | | Remove unsubscribe footer |

## Loop
```text
read sequence map → draft email N → Compliance per template → assemble 7-day arc → QG-EMAIL → human enables automation
```

## Review loop
**Compliance mandatory on every template** before QG-EMAIL.

## Stop conditions
- Pitch email before Day 5 without human ack → default STOP (follow 7-day map)
- Compliance FAIL on subject → STOP
- CTA to VIP before Apprentice in nurture → STOP (unless offer doc says otherwise)

## Outputs
- `sales/assets/brevo/` — template drafts
- Updates to `docs/brevo_email_sequence.md`

## Acceptance criteria
- [ ] Email 0 + Days 1–7 complete
- [ ] Footer disclaimer on all
- [ ] QG-EMAIL checklist passable
- [ ] No hype/prohibited terms in subjects
