# Provision customer command

Human-executed. Agents advise only.

## Trigger
WooCommerce order Completed — Apprentice or VIP SKU

## Agent sequence

1. **FunnelKit Agent** — confirm order SKU and tags
2. **LearnHouse Agent** — output provision checklist from `playbook/ops/learnhouse-provision-sop.md`
3. **Compliance Agent** — verify access email template has disclaimer
4. **Brevo Email Agent** — confirm `access_ready` template ID
5. **Human G4** — create LearnHouse user + enroll
6. **Human G5** — Telegram add if VIP
7. Log order note + `.ai/audit/approvals/YYYY-MM-DD-order-<id>.md`

## SLA
≤ 24 hours from payment
