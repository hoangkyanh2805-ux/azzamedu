# Human Approval Gates — Alpha Elite

> **Kickstart artifact #8** · No agent or deploy step skips these for production impact.

---

| Gate | Trigger | Approver | Evidence | Blocks |
|------|---------|----------|----------|--------|
| **G0** | Pricing, SKU, bundle changes | Project owner | `offer_stack.md` updated | Checkout, sales copy |
| **G1** | Publish page, PDF, public doc | Owner + compliance | Compliance PASS + Web Quality (if web) + `.ai/audit/approvals/` | Traffic |
| **G2** | Brevo automation/broadcast live | Owner | QG-EMAIL + all templates Compliance PASS | Nurture to real list |
| **G3** | FunnelKit/WooCommerce live | Tech + owner | QG-FUNNEL sandbox receipt | Real payments |
| **G4** | LearnHouse user create/enroll | Admin ops | Order ID + SOP checklist | Course access |
| **G5** | Telegram VIP add | Admin ops | @username + VIP order | Community access |
| **G6** | PayPal live / crypto process | Owner | Test transaction | Revenue |
| **G7** | Compliance incident | Owner immediately | Escalation log | All publish until cleared |

---

## MVP manual access (requires G4 + G5)

```text
Payment success (G3 already done)
  → Human G4: LearnHouse user + enroll
  → Brevo access email
  → Human G5: Telegram (VIP only)
```

**SLA:** ≤24h · SOP: `playbook/ops/learnhouse-provision-sop.md`

---

## Approval log template

Path: `.ai/audit/approvals/YYYY-MM-DD-<artifact>.md`

```markdown
# Approval
- Gate: G1
- Artifact: Homepage /
- Approver:
- Date:
- Compliance audit:
- Web quality audit:
- Notes:
```

---

## What agents may NOT do without human gate

- Publish WordPress/Elementor  
- Enable live Brevo automations  
- Create WooCommerce products at live prices  
- Configure live FunnelKit  
- Create LearnHouse users  
- Add Telegram members  
- Override Compliance FAIL  

Mirror: `.ai/rules/human-approval-gates.md` · Matrix: `permission-matrix.md`
