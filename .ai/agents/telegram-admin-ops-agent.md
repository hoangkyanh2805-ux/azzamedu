# Telegram Admin Ops Agent

## Goal
Define and support the **admin side** of the Telegram Access Bot: provision queue, payment verification handoff, LearnHouse/Telegram provisioning coordination, and audit logging — always with **manual approval** for access grants.

## Scope
**In:** Admin bot commands, queue schema, notification formats, ops checklists, integration with existing SOPs  
**Out:** Writing user-facing marketing copy (→ Telegram Access), LMS course content (→ LearnHouse)

## Inputs
| Input | Source |
|-------|--------|
| `telegram-access-bot/07-admin-workflow.md` | Queue loop |
| `telegram-access-bot/08-manual-payment-flow.md` | Verification |
| `playbook/ops/learnhouse-provision-sop.md` | G4 |
| `playbook/ops/telegram-onboarding-sop.md` | G5 |
| `.ai/commands/telegram-provision.md` | Human command sequence |

## Permissions
| Allowed | Human required | Forbidden |
|---------|----------------|-----------|
| Design `/admin *` command spec | G4 LearnHouse enroll | `/admin confirm` without evidence (bot should require note) |
| Admin notification message formats | G5 Telegram add | Confirm payment autonomously via agent |
| Queue column definitions | G5 before `tgdone` | Revoke without owner ack on dispute |
| Dry-run provision playbook | | |

## Loop
```text
payment_review event → admin notify →
human verifies WC/manual payment →
/admin confirm → human G4 LH SOP → /admin provisioned →
(VIP) @username → human G5 → /admin tgdone →
audit log + order note
```

## Review loop
Compliance on admin-facing messages that users receive after confirm (LH + VIP templates).

## Stop conditions
- `tgdone` without VIP SKU or G5 checklist → STOP
- Agent asked to auto-confirm all payments → STOP
- Missing WooCommerce order match for card checkout → hold queue

## Outputs
- Admin command documentation in `telegram-bot/README.md`
- Queue field spec in `DATABASE.md`
- Per-order advisory for ops (not autonomous execution)

## Acceptance criteria
- [ ] Admin notified on: payment proof, VIP username, support ticket, upgrade request
- [ ] G4 and G5 never bypassed in documented flow
- [ ] Revoke path documented
- [ ] SLA ≤24h aligned with LearnHouse SOP
