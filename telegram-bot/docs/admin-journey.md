# Admin Journey

## Daily ops loop

```text
Morning: /queue → triage new items
For each AE- code:
  1. Verify payment (PayPal, crypto, or WooCommerce order)
  2. /confirm <code>
  3. G4: Create LearnHouse user (playbook/ops/learnhouse-provision-sop.md)
  4. /provisioned <code> → bot sends LH instructions
  5. If VIP SKU: G5 add to Telegram group (telegram-onboarding-sop.md)
  6. /tgdone <code> → bot sends VIP welcome
```

## Notification sources

| Event | Admin alert |
|-------|-------------|
| Payment proof submitted | Telegram DM with queue code, SKU, email |
| Support ticket | Telegram DM with ticket code |
| Future: WooCommerce webhook | Order paid → auto queue row (P2) |

## Admin commands reference

| Command | When to use |
|---------|-------------|
| `/queue` | See all open provision items |
| `/confirm AE-2026-0042` | Payment verified |
| `/provisioned AE-2026-0042` | LearnHouse account created |
| `/tgdone AE-2026-0042` | User added to VIP group |

## G4 — LearnHouse provision (human)

1. Open LearnHouse admin
2. Create user with buyer email
3. Assign course bundle per SKU
4. Note provision time in queue / audit log
5. Run `/provisioned` in bot

**SLA:** ≤ 24 business hours from `/confirm`

## G5 — Telegram VIP (human)

1. Collect @username (DM or queue notes)
2. Verify Module 1 complete (policy)
3. Send private invite or add to group
4. Run `/tgdone`

**SLA:** ≤ 24 business hours after G4 for VIP SKUs

## Reject / suspend

| Case | Action |
|------|--------|
| Fraudulent payment proof | Mark `revoked`, reply via support |
| Chargeback | Revoke LH + remove from VIP |
| Policy violation in VIP | Suspend per desk rules |

Update `members.status` in Supabase; bot `/status` reflects on next read.

## Audit

Log every admin action in `audit_log` (production Supabase). MVP memory store: rely on Telegram message history.

## Config

Set admin Telegram IDs in `config.yaml`:

```yaml
admin:
  telegram_ids:
    - 123456789
```

Only these IDs can run `/queue`, `/confirm`, `/provisioned`, `/tgdone`.
