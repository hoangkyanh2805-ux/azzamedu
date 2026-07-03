# MVP System Map — Alpha Elite

> End-to-end map: **mission → stack → flows → ownership → acceptance**

---

## Mission → system capabilities

| Mission step | System capability | Primary tool |
|--------------|-------------------|--------------|
| Capture leads | Opt-in landing + form | WordPress / Elementor |
| Deliver free Gameplan | Instant email + PDF | Brevo + WP media |
| Nurture to paid | 7-day email sequence | Brevo |
| Sell Apprentice | Checkout + order | WooCommerce + FunnelKit |
| Deliver course | Enroll + video lessons | LearnHouse + YouTube Unlisted |
| Upgrade to VIP | Upsell + subscription | FunnelKit + WooCommerce |
| VIP community | Private group access | Telegram (manual) |
| Route to Quant / Inner Circle | Upgrade checkout / apply | WooCommerce + email |
| DWY setup | Order bump / service SKU | FunnelKit |
| Get paid | Card + crypto | PayPal + manual crypto |

---

## System diagram

```text
                         ┌─────────────────┐
                         │     TRAFFIC      │
                         └────────┬────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │  WordPress / Elementor     │
                    │  Landing · /apprentice ·   │
                    │  /vip · legal pages        │
                    └─────────────┬─────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │ opt-in            │ purchase           │
              ▼                   ▼                    │
     ┌────────────────┐  ┌────────────────────────┐  │
     │     Brevo      │  │ WooCommerce + FunnelKit │  │
     │  · Gameplan    │  │ · Apprentice SKU        │  │
     │  · 7-day       │  │ · VIP SKU               │  │
     │  · onboarding  │  │ · bump / upsell / TY    │  │
     └───────┬────────┘  └───────────┬────────────┘  │
             │                       │ PayPal / Crypto │
             │                       ▼                 │
             │            ┌──────────────────┐         │
             │            │   Admin Ops      │         │
             │            │  (manual MVP)    │         │
             │            └────────┬─────────┘         │
             │         ┌───────────┼───────────┐       │
             │         ▼           ▼           ▼       │
             │   ┌──────────┐ ┌─────────┐ ┌─────────┐ │
             │   │LearnHouse│ │ Brevo   │ │Telegram │ │
             │   │ LMS      │ │ access  │ │ VIP     │ │
             │   └────┬─────┘ └─────────┘ └─────────┘ │
             │        │                                 │
             │        ▼                                 │
             │   ┌──────────┐                          │
             └──►│ YouTube  │                          │
                 │ Unlisted │                          │
                 └──────────┘                          │
```

---

## Offer → system routing

| Offer | Capture | Deliver | Sell | Access |
|-------|---------|---------|------|--------|
| **1. Alpha Elite Gameplan** | Elementor form | Brevo Email 0 + PDF | Free | Download link |
| **2. Apprentice Course** | Email CTA / `/apprentice` | LearnHouse course | FunnelKit + PayPal | Manual enroll ≤24h |
| **3. VIP Private System** | Upsell / `/vip` | Telegram + LMS library | FunnelKit sub | Manual TG + enroll |
| **4. Quant Desk** | VIP email / upgrade page | LearnHouse + desk channel | Checkout upgrade | Manual |
| **5. Inner Circle** | Application (phase 2) | Cohort channel | Manual / invite | Defer MVP |
| **6. DWY Setup** | VIP checkout bump | 1:1 / group session | Bump SKU | Calendar / ops |

---

## Page map (WordPress)

| URL | Purpose | Primary CTA |
|-----|---------|-------------|
| `/` | Homepage funnel | Get Alpha Elite Gameplan |
| `/apprentice` | Apprentice sales | Checkout |
| `/vip` | VIP sales | Checkout |
| `/gameplan-thank-you` | Post opt-in | Check email |
| `/thank-you/apprentice` | Post purchase | LearnHouse next steps |
| `/thank-you/vip` | Post VIP | Telegram username form |
| `/checkout/` | FunnelKit | Pay |
| Legal | privacy, terms, risk, refund | — |

---

## Data flow — happy path

### Path A — Lead only
```text
1. User submits form on Elementor
2. Brevo: add `gameplan-leads`, tag `lead_gameplan`
3. Brevo: send Email 0 with Alpha Elite Gameplan PDF
4. Redirect: /gameplan-thank-you
5. Brevo: Days 1–7 nurture → Apprentice CTA
```

### Path B — Apprentice purchase
```text
1. User clicks Apprentice CTA → FunnelKit checkout (AE-APP-001)
2. Optional bump: Risk Calculator Pack
3. PayPal payment → order Completed
4. Brevo: tag `purchased_apprentice`
5. Admin: LearnHouse user + enroll Apprentice
6. Brevo: `access_ready` email
7. FunnelKit upsell: VIP (accept or decline)
8. TY page: /thank-you/apprentice
```

### Path C — VIP purchase
```text
1. Checkout AE-VIP-MON or AE-VIP-YR
2. Optional bump: DWY Setup (AE-DWY-001)
3. PayPal → order Completed
4. Admin: LearnHouse VIP library + Telegram add
5. Brevo: VIP onboarding sequence
6. TY: collect @telegram username
```

### Path D — Quant / Inner Circle (post-MVP expand)
```text
VIP active → email or /quant upgrade → checkout AE-QNT-001
Inner Circle → application → manual approve → invite
```

---

## SKU reference

| SKU | Product |
|-----|---------|
| `AE-APP-001` | Apprentice Operating Course |
| `AE-VIP-MON` | VIP Private System (monthly) |
| `AE-VIP-YR` | VIP Private System (annual) |
| `AE-QNT-001` | Quant Desk |
| `AE-IC-APP` | Inner Circle (application) |
| `AE-DWY-001` | DWY Bot & Broker Setup |

---

## Payment matrix

| Method | MVP | Flow |
|--------|-----|------|
| PayPal | ✓ Live | WooCommerce gateway |
| Crypto | Manual | Email order ID → invoice → manual order → same TY |

---

## Ops SLA (MVP)

| Event | SLA | Owner |
|-------|-----|-------|
| Gameplan delivery | Instant (Brevo) | Automated |
| Apprentice access | ≤ 24h | Admin G4 |
| VIP Telegram add | ≤ 24h after @username | Admin G5 |
| Support reply | ≤ 12h | Ops |

SOPs: `playbook/ops/learnhouse-provision-sop.md` · `telegram-onboarding-sop.md`

---

## QA before traffic

| Gate | Doc |
|------|-----|
| Compliance all copy | `docs/compliance_guardrails.md` |
| Web quality | `docs/web_quality_checklist.md` |
| Full pre-launch | `docs/launch_checklist.md` · `.ai/commands/pre-launch.md` |

---

## MVP definition of done

A stranger can:

1. Opt in and receive **Alpha Elite Gameplan** within minutes  
2. Receive 7 nurture emails without errors  
3. Purchase **Apprentice** via PayPal  
4. Get LearnHouse login within 24h and complete Module 1  
5. (Optional) Accept VIP upsell and join Telegram within 24h of submitting @username  

---

## Doc index by stack component

| Stack | Primary doc |
|-------|-------------|
| Elementor / CRO | `landing_page_cro_framework.md` |
| Gameplan | `lead_magnet_blueprint.md` |
| Brevo | `brevo_email_sequence.md` |
| FunnelKit | `funnelkit_checkout_map.md` |
| LearnHouse | `learnhouse_lms_map.md` |
| Offers | `offer_stack.md` |
| Agents | `agent-loop-operating-model.md` |
