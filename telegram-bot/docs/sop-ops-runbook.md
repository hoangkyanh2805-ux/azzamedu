# Telegram Access Bot — Ops Runbook (MVP)

> **Cadence:** Daily admin · **SLA:** ≤24h provision  
> **Human commands:** `.ai/commands/telegram-provision.md`

---

## Daily (admin ops)

| Time | Action |
|------|--------|
| Morning | `/admin pending` — clear `payment_review` |
| Midday | Check support tickets — none >12h open |
| Evening | Log provisioned count; WC order notes |

---

## Weekly

| Action | Owner |
|--------|-------|
| Compliance spot-check live templates | Owner |
| Review `audit_log` for anomalies | Admin |
| Backup Supabase or export Sheets | Tech |
| Update `09-backlog.md` | PM |

---

## Monitoring

| Signal | Alert |
|--------|-------|
| Bot process down | systemd restart + manual email provision fallback |
| Queue >24h | Owner ping |
| P0 compliance report | Disable bot (G7) |

---

## Escalation

```text
Support can't resolve → Owner
Compliance incident → G7 immediate
Bot outage >1h → Tech + playbook fallback (manual SOP only)
```

---

## Deploy / rollback

See `DEPLOYMENT.md`. Rollback: stop service, revert release, notify admins.

---

## Related SOPs

- `playbook/ops/learnhouse-provision-sop.md` (G4)  
- `playbook/ops/telegram-onboarding-sop.md` (G5)  
- `kickstart/05-admin-journey.md`
