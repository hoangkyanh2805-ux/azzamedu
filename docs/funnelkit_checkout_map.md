# FunnelKit Checkout Map — Alpha Elite

## Purpose
WooCommerce + FunnelKit flows for premium course/membership checkout — calm UX, compliance at pay button, bump/upsell without hype.

## Stack
```text
WordPress → WooCommerce (orders) → FunnelKit (checkout UX)
    → PayPal / Crypto manual → Brevo tags → Manual LearnHouse + Telegram
```

---

## Entry points

| Product | URL pattern | Flow |
|---------|-------------|------|
| Apprentice | `/checkout/?add-to-cart=AE-APP-001` | Primary paid conversion |
| VIP | `/checkout/?add-to-cart=AE-VIP-MON` | Upsell or direct |
| From email D5–7 | `/apprentice` → checkout | Warm nurture |

---

## Flow 1 — Apprentice (primary)

```text
/apprentice or Brevo Day 5–7 CTA
    → FunnelKit Checkout (Apprentice)
    → Order bump: 2% Risk Calculator Pack (PDF)
    → PayPal payment
    → Upsell: VIP first month (calm, no fake timer)
        → Accept → VIP one-click
        → Decline → Apprentice Thank You
    → TY: LearnHouse access instructions (24h SLA)
```

---

## Flow 2 — VIP direct

```text
/vip
    → FunnelKit Checkout (VIP)
    → Order bump: DWY Bot & Broker Setup
    → PayPal
    → Upsell: Quant Desk intro (optional)
    → TY: Telegram username collection
```

---

## Checkout page copy

**Above fold:**
> Complete your enrollment in **[Product]**. Access instructions arrive by email within 24 hours. Trading involves risk. This is education and operating support — not a profit guarantee.

**Pay button microcopy:**
> I understand trading involves risk of loss.

**Required checkbox:**
- [ ] I have read the risk disclaimer and understand this is educational content.

---

## Order bumps

### Bump A — Apprentice checkout
| Field | Value |
|-------|-------|
| Product | 2% Risk Calculator Pack (PDF + Sheet) |
| Headline | Add the position-size calculator pack |
| Copy | Educational sizing tool for the 2% rule — not trading advice |
| Price | ~15–25% of Apprentice |

### Bump B — VIP checkout
| Field | Value |
|-------|-------|
| Product | DWY Bot & Broker Setup |
| Headline | Done-with-you automation setup |
| Copy | Guided broker + bot configuration support — you retain full control |
| Compliance | Not managed trading |

---

## Upsell pages

### Post-Apprentice → VIP
- 3-min calm video: what's inside VIP (SOP library, community, structured ideas)
- No profit montage
- Decline: "Continue with Apprentice only" → TY

### Post-VIP → Quant Desk
- Education-focused overview
- Soft — optional ascension

---

## Thank-you pages

### `/thank-you/apprentice`
1. Order confirmed #{{order_id}}
2. Next: email within 24h with LearnHouse login
3. Start Module 1 when access arrives
4. Secondary link: VIP overview (if declined upsell)
5. Disclaimer footer

**Brevo:** tag `purchased_apprentice` · start onboarding Sequence 2

### `/thank-you/vip`
1. VIP confirmed
2. Submit Telegram @username (form)
3. Added within 24h
4. Read pinned community rules
5. Disclaimer

**Brevo:** tag `purchased_vip` · Sequence 3

---

## Payments

| Method | MVP | Notes |
|--------|-----|-------|
| PayPal | ✓ | WooCommerce PayPal Payments |
| USDT TRC20 | Manual | Customer sends USDT on TRON/TRC20, then submits Order ID + TxID for admin review |
| Stripe | Phase 2 | — |

---

## Post-purchase ops (MVP manual)

```text
Order Completed
    → Brevo tag
    → Admin alert
    → LearnHouse user + enroll (SOP)
    → Brevo access_ready email
    → VIP: Telegram add
```

SOP: `playbook/ops/learnhouse-provision-sop.md`

---

## WooCommerce + FunnelKit config

- [ ] Guest checkout on
- [ ] FunnelKit replaces default checkout
- [ ] One bump per flow (MVP)
- [ ] TY router by cart SKU
- [ ] Order emails include disclaimer
- [ ] Subscription plugin for VIP if recurring

---

## Metrics

| Metric | Target |
|--------|--------|
| Checkout completion | > 65% |
| Bump take rate | 15–25% |
| VIP upsell (post-Apprentice) | 10–18% |

---

## Acceptance criteria

- [ ] Sandbox + live test purchase
- [ ] Compliance checkbox required
- [ ] TY + Brevo tags correct
- [ ] No prohibited terms on checkout
