# First-Principles Requirements — Alpha Elite

> Kickstart supplement · Business outcome → workflows → integrations → guardrails.

---

## Business outcome

Launch a compliant funnel that converts traffic into Apprentice students and VIP members for a **trading education operating system** (XAUUSD-capable, not signal-group positioned).

---

## User workflows (MVP)

| # | Workflow | Actor | System |
|---|----------|-------|--------|
| W1 | Opt in for Gameplan | Visitor | Elementor → Brevo |
| W2 | Receive nurture | Lead | Brevo 7-day |
| W3 | Purchase Apprentice | Buyer | FunnelKit → PayPal |
| W4 | Access course | Student | LearnHouse (manual enroll) |
| W5 | Upgrade VIP | Member | FunnelKit + Telegram |
| W6 | Provision access | Admin | LearnHouse + Brevo + Telegram |

---

## Data model (logical)

| Entity | Key fields | Source |
|--------|------------|--------|
| Lead | email, name, tags | Brevo |
| Order | SKU, status, email | WooCommerce |
| Student | email, enrollments | LearnHouse |
| VIP member | order_id, @telegram | Ops log |

---

## Integrations

| Integration | MVP | Phase 2 |
|-------------|-----|---------|
| Form → Brevo | ✓ | — |
| Order → Brevo tags | ✓ | — |
| Order → LearnHouse | Manual | Webhook API |
| PayPal | ✓ | Stripe optional |
| Crypto | Manual invoice | Gateway |

---

## Guardrails

- No guaranteed profit, risk-free, passive bot, signal-group positioning  
- Manual provision SLA ≤24h  
- Compliance before every publish (G1)  

See: `risk-compliance-checklist.md`

---

## Acceptance

- [ ] Workflows W1–W4 demonstrable end-to-end  
- [ ] W5–W6 documented in playbook SOPs
