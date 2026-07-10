# Offer Menu Map

> Maps `docs/offer_stack.md` → bot menus, buttons, checkout URLs.  
> Prices: draft G0 — update after owner sign-off.

## Main menu

```text
/start
├── 🛒 Shop (/menu)     ← category browse
├── 🔑 My Access
├── 💳 Payment Help
├── 🧭 Onboarding
├── 💬 Support
└── ⚠️ Risk Disclaimer
```

## Shop categories

| Category | ID | Products |
|----------|-----|----------|
| 📚 Khóa học | `khoa_hoc` | Apprentice `AE-APP-001` |
| 🏛 Membership | `membership` | VIP MON/YR, Quant apply |
| 🎁 Free | `free` | Gameplan |
| 🔧 Services | `services` | DWY bump |

## Offer catalog (flat reference)

| Menu label | SKU | Price (draft) | Checkout / action |
|------------|-----|---------------|-------------------|
| Free — 2% Rule Gameplan | — | Free | `/gameplan` (web opt-in) |
| Apprentice Operating Course | `AE-APP-001` | $297 | WooCommerce cart |
| VIP Private Desk — Monthly | `AE-VIP-MON` | $149/mo | WooCommerce cart |
| VIP Private Desk — Annual | `AE-VIP-YR` | $1,290/yr | WooCommerce cart |
| Quant Desk | `AE-QNT-001` | Application | `/quant-desk` |
| DWY Bot & Broker Setup | `AE-DWY-001` | $497 bump | VIP checkout bump |
| Inner Circle | — | Waitlist | P2 |

## Entitlements

| SKU | LearnHouse | Telegram VIP | Bot unlock |
|-----|------------|--------------|------------|
| Gameplan | — | — | Onboarding checklist |
| AE-APP-001 | Apprentice | — | LH link when provisioned |
| AE-VIP-MON/YR | Apprentice + VIP | After G5 | Status + VIP flow |
| AE-QNT-001 | + Quant modules | Priority channel | Extended status |
| AE-DWY-001 | — | — | Setup session (manual) |

## Compliance copy rules

- No "signals", "guaranteed", "passive income"
- VIP = rules-first accountability desk, not alert channel
- Free Gameplan routes to web capture (Brevo), not in-bot PDF

## Config keys

```yaml
checkout:
  AE-APP-001: /checkout/?add-to-cart=AE-APP-001
  AE-VIP-MON: /checkout/?add-to-cart=AE-VIP-MON
  AE-VIP-YR: /checkout/?add-to-cart=AE-VIP-YR
site:
  base_url: https://yourdomain.com
  learnhouse_url: https://learn.yourdomain.com
  gameplan_url: /gameplan
```

## Acceptance

- [ ] Every paid SKU has working checkout URL
- [ ] Menu copy passes compliance checklist
- [ ] Prices match published site after G0
