# 5 — Offer Menu Map (Bot Catalog)

> Maps `docs/offer_stack.md` → bot menus, buttons, and checkout URLs.  
> Prices: draft G0 — `web/wordpress/pricing-draft-g0.md`

---

## Main menu structure

```text
/start
├── 📋 View Offers          → /offers
├── 🔑 My Access            → /status
├── 💳 Payment Help         → /pay
├── 🧭 Onboarding           → /onboard
├── 🎓 LearnHouse Login     → URL button (if entitled)
├── 💬 Support              → /support
└── ⚠️ Risk Disclaimer      → static message
```

---

## Offer catalog (`/offers`)

| Menu label | SKU | Price (draft) | Checkout / action | Bot behavior |
|------------|-----|---------------|-------------------|--------------|
| **Free — 2% Rule Gameplan** | — | Free | `https://[domain]/gameplan` or `#get-gameplan` | Open web opt-in — not in-bot email capture MVP |
| **Apprentice Operating Course** | `AE-APP-001` | $297 | `/checkout/?add-to-cart=AE-APP-001` | Web checkout primary; bot shows description + link |
| **VIP Private Desk — Monthly** | `AE-VIP-MON` | $149/mo | `/checkout/?add-to-cart=AE-VIP-MON` | Includes Apprentice bundle |
| **VIP Private Desk — Annual** | `AE-VIP-YR` | $1,290/yr | `/checkout/?add-to-cart=AE-VIP-YR` | Show "Save 28% vs monthly" — factual only |
| **Quant Desk** | `AE-QNT-001` | By application | `/quant-desk` | Application page — not instant buy |
| **DWY Bot & Broker Setup** | `AE-DWY-001` | $497 bump | VIP checkout bump | Mention in VIP onboarding only |
| **Inner Circle** | — | Waitlist | TBD form | P2 — "Join waitlist" link |

---

## Inline button example (conceptual)

```text
[ 🎁 Free Gameplan ]  → URL
[ 📘 Apprentice $297 ] → URL checkout AE-APP-001
[ 🏛 VIP Monthly ]     → URL checkout AE-VIP-MON
[ 🏛 VIP Annual ]      → URL checkout AE-VIP-YR
[ 📊 Quant — Apply ]   → URL /quant-desk
[ ← Back ]
```

---

## Product copy blocks (bot — compliance-safe)

### Apprentice (short)

```text
Apprentice Operating Course — 5 modules, ~14 lessons, LearnHouse access.
Includes Operating Toolkit (worksheets + SOP templates).
Education only. Not investment advice. Trading involves risk.
```

### VIP (short)

```text
VIP Private Desk — rules-first accountability, SOP library, structured trade ideas for education.
Not an alert channel. You own every trade decision.
Includes full Apprentice course.
```

---

## Entitlements per offer

| SKU | LearnHouse | Telegram VIP | Bot features unlocked |
|-----|------------|--------------|------------------------|
| Gameplan (lead) | — | — | Onboard: Gameplan checklist only |
| AE-APP-001 | Apprentice course | — | LH link when provisioned |
| AE-VIP-MON/YR | Apprentice + VIP library | VIP group (after admin) | LH + VIP status + @username flow |
| AE-QNT-001 | + Quant modules | Priority channel | Extended status |
| AE-DWY-001 | — | — | Setup session booking (manual) |

---

## Config keys (for `config.yaml`)

```yaml
site_base: https://yourdomain.com
checkout:
  AE-APP-001: /checkout/?add-to-cart=AE-APP-001
  AE-VIP-MON: /checkout/?add-to-cart=AE-VIP-MON
  AE-VIP-YR: /checkout/?add-to-cart=AE-VIP-YR
learnhouse_url: https://learn.yourdomain.com
gameplan_url: https://yourdomain.com/gameplan
```

---

## Acceptance

- [ ] Every paid SKU has working checkout URL
- [ ] No menu item says "signals", "guaranteed", or "passive income"
- [ ] Free tier routes to web capture (Brevo), not bot-only PDF leak
