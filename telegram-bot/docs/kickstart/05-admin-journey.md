# 5 — Admin Journey

> **Owners:** Admin Ops · **SLA:** ≤24h · **Command:** `.ai/commands/telegram-provision.md`

---

## Daily loop

```text
08:00  Open /admin pending (or ops sheet)
       │
       ├─ Payment reviews → verify WC or manual proof
       ├─ VIP usernames → verify SKU + payment
       └─ Support tickets → respond
       │
12:00  Mid-day sweep (nothing >12h in payment_review)
       │
17:00  Close provisioned rows · log order notes
```

---

## Notification → action map

| Admin receives | First action | Human gate |
|----------------|--------------|------------|
| `NEW PAYMENT REVIEW` | Open WC or verify PayPal/crypto | — |
| `VIP USERNAME @x` | Confirm VIP order paid | G5 prep |
| `SUPPORT #id` | Read ticket | — |
| `UPGRADE REQUEST` | Check eligibility | G0 pricing |
| `WC WEBHOOK order` (P2) | Match member | — |

---

## Payment review journey

```text
1. Notification with queue_code, email, sku
2. Verify:
   - WooCommerce order Completed, OR
   - PayPal txn / crypto hash + amount
3. /admin confirm AE-2026-XXXX
4. Run LearnHouse SOP (G4) — outside bot
5. /admin provisioned AE-2026-XXXX
   → Bot DMs user LearnHouse template
6. If VIP SKU:
   a. Confirm @username in queue
   b. Add to VIP group (human)
   c. /admin tgdone AE-2026-XXXX
   → Bot DMs VIP welcome + pinned rules reminder
7. WooCommerce order note + audit_log row
```

---

## Rejection journey

```text
/admin reject AE-2026-XXXX insufficient_proof
  → User notified: what to resubmit
  → Status pending_payment
```

---

## Revoke journey (refund / chargeback)

```text
1. WC refund or owner decision
2. LearnHouse revoke SOP
3. Remove from Telegram VIP
4. /admin revoke AE-2026-XXXX
5. Brevo tags updated (manual)
```

---

## Admin tools

| Tool | MVP | P2 |
|------|-----|-----|
| Telegram `/admin` commands | ✓ | ✓ |
| Google Sheet queue | ✓ optional | migrate |
| Supabase dashboard | ✓ optional | primary |
| WooCommerce orders | manual lookup | webhook auto |

---

## Checklists

### Before `/admin confirm`

- [ ] Amount matches SKU (G0 prices)  
- [ ] Email matches payer  
- [ ] Not duplicate txn  
- [ ] SKU entitlement clear  

### Before `/admin tgdone`

- [ ] G4 complete (LH active)  
- [ ] VIP SKU  
- [ ] @username verified  
- [ ] User read pinned rules (onboarding step)  
- [ ] G5 human add completed  

---

## Escalation

| Case | Escalate to |
|------|-------------|
| Compliance question in ticket | Owner |
| Chargeback | Owner + revoke SOP |
| Bot down | Tech + manual email provision |
| User demands signals | Template decline + disclaimer |

---

## Audit

Log every admin action to `audit_log` + optional `.ai/audit/approvals/YYYY-MM-DD-telegram-order-{id}.md`

---

## Acceptance

- [ ] Admin can clear daily queue using bot + SOPs  
- [ ] G4 and G5 never skipped in documented happy path  
- [ ] Reject and revoke paths defined
