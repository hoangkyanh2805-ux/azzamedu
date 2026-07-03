# Telegram provision command

Human-executed. Agents advise only.

## Trigger
- Bot queue row `payment_confirmed`, or  
- WooCommerce order Completed (Apprentice / VIP / Quant SKU) with linked `telegram_id`

## Agent sequence

1. **FunnelKit Agent** — confirm order SKU, amount, email  
2. **Telegram Admin Ops Agent** — match queue row / `wc_order_id`  
3. **LearnHouse Agent** — checklist from `playbook/ops/learnhouse-provision-sop.md`  
4. **Compliance Agent** — LH + bot notification templates have disclaimer  
5. **Human G4** — LearnHouse user create + enroll  
6. Bot or human: `/admin provisioned <queue_id>` → user receives LH instructions  
7. **If VIP SKU:** collect @username → **Human G5** → `playbook/ops/telegram-onboarding-sop.md`  
8. **Human G5** — Telegram group add  
9. `/admin tgdone <queue_id>`  
10. Log: WooCommerce order note + queue row + `.ai/audit/approvals/YYYY-MM-DD-telegram-order-<id>.md`

## SLA
≤ 24 hours from payment confirmed

## Stop
- Payment not verified → do not confirm  
- Compliance FAIL on outbound message → fix template first  
- User requests signal channel access → send onboarding + pinned rules, not alerts
