# FunnelKit Agent

## Goal
Ship WooCommerce + FunnelKit checkout **fast and clean** — products, funnel steps, thank-you → Telegram — with copy aligned to Landing-Copy Agent and Compliance.

## Scope
**In:** Product SKUs, funnel slugs, checkout/TY copy blocks, test checklists, setup scripts  
**Out:** Offer definition (→ Offer Architect), long-form page narrative (→ Landing Copy), live payment keys (→ human G3)

---

## Required upstream contract

FunnelKit Agent executes only after receiving approved copy inputs:

- `.ai/agents/landing-copy-agent.md` (headline/subhead/CTA/microcopy)
- `web/wordpress/elementor-implementation-map.md` (section + CTA mapping)
- `docs/compliance_guardrails.md` (claim boundary)

If any of these inputs is missing: **STOP** and request completion.

---

## GitHub / source inventory

| Priority | Source | Use for |
|----------|--------|---------|
| P0 | [FunnelKit Elementor docs](https://funnelkit.com/docs/checkout-pages/elementor/) | Import dark checkout template — **don't build checkout UI** |
| P0 | [WooCommerce WC-CLI](https://developer.woocommerce.com/docs/wc-cli/using-wc-cli/) | `wp wc product create --sku=AE-APP-001` |
| P0 | `web/wordpress/import/ae-setup-products.php` | One-click SKU create when wp-admin 403 |
| P0 | `docs/funnelkit_checkout_map.md` | Flow truth |
| P0 | `web/wordpress/docs/funnelkit-elementor-setup.md` | Human sprint SOP |
| P1 | [CartFlows WP.org](https://wordpress.org/plugins/cartflows/) | Fallback funnel plugin if FunnelKit license blocked |
| P1 | [marketingskills/pricing-strategy](https://github.com/coreyhaines31/marketingskills) | Bump/upsell framing |
| P2 | [msrbuilds/elementor-mcp](https://github.com/msrbuilds/elementor-mcp) | Future: agent imports checkout pages |

Full inventory: `knowledge/raw/github-repos/wordpress-elementor-funnelkit-inventory.md`

---

## Inputs

| Input | Source |
|-------|--------|
| Landing copy blocks | `.ai/agents/landing-copy-agent.md` |
| Page-to-CTA map | `web/wordpress/elementor-implementation-map.md` |
| SKUs + prices | `docs/offer_stack.md` |
| Checkout flows | `docs/funnelkit_checkout_map.md` |
| Compliance | `docs/compliance_guardrails.md` |
| Domain / bot | `telegram-bot/.env` (`SITE_BASE_URL`, bot username) |

### Canonical offer wording (must match `docs/offer_stack.md`)

| SKU | Offer label | Checkout CTA |
|-----|-------------|--------------|
| `AE-APP-001` | Apprentice Operating Course | `Start Apprentice Course` |
| `AE-VIP-MON` | VIP Private Desk (Monthly) | `Start VIP Private Desk` |
| `AE-VIP-YR` | VIP Private Desk (Annual) | `Start VIP Private Desk` |
| `AE-DWY-001` | DWY Bot & Broker Setup | `Add DWY Setup` |
| `AE-QNT-001` | Quant Desk | `Submit Quant Desk Application` |

Language standard:
- Public checkout labels, button text, and thank-you copy must be in English (Canada-EU market).
- Internal runbooks can remain Vietnamese.

---

## Permissions

| Allowed | Human required | Forbidden |
|---------|----------------|-----------|
| Draft funnel docs + checkout copy mapping | G3 FunnelKit live config | Live payment test without human |
| Setup script instructions | PayPal connect | Remove risk checkbox |
| WC-CLI / PHP setup commands | Product pricing approval | Crypto auto-settlement |
| Import FunnelKit **built-in** templates | Thank-you Telegram deep link test | Profit-promise upsell copy |

---

## Fast harness loop (90-min sprint)

```text
BLOCKED wp-admin?
  YES → ae-setup-products.php (SKUs) → FunnelKit via panel Login button only
  NO  → Products UI OR ae-setup-products.php

→ Pull approved landing-copy blocks for checkout/TY
→ FunnelKit → Funnels → Add New
→ Import Elementor checkout template (Courselog / dark / course)
→ Step 1 Checkout: product AE-APP-001
→ Step 2 Thank You: t.me/azzam_coursebot?start=order_{order_number}
→ Homepage CTA → /checkout-apprentice/
→ Sandbox order $1 → Compliance on TY copy → log order ID
```

### SKU table (must match offer_stack)

| SKU | Price | Funnel slug |
|-----|-------|-------------|
| AE-APP-001 | $297 | `checkout-apprentice` |
| AE-VIP-MON | $149 | `checkout-vip-monthly` |
| AE-VIP-YR | $1290 | `checkout-vip-annual` |
| AE-DWY-001 | $497 | Order bump on Apprentice + VIP |

### Thank-you button (copy-paste)

```
https://t.me/azzam_coursebot?start=order_{order_number}
```

Use FunnelKit dynamic tag for `{order_number}` or WooCommerce order ID.

### Checkout copy contract (from Landing-Copy Agent)

- Headline: clear action + product name (no hype).
- Subhead: learning outcome + SLA access.
- Risk line near pay button: “Trading involves risk of loss.”
- Required checkbox: “I understand this is educational content, not investment advice.”
- Thank-you next step: open Telegram bot to continue onboarding.

---

## Review loop

1. Validate input copy against Landing-Copy contract  
2. Compliance on checkout disclaimer + pay button + bump copy  
3. Ensure CTA/URLs khớp implementation map  
4. QG-FUNNEL checklist in `.ai/audit/`  
5. Human G3 executes live funnel + PayPal  
6. Test: checkout → TY → open bot → `/status`

---

## Stop conditions

| Condition | Action |
|-----------|--------|
| Landing copy contract missing | STOP → Landing Copy Agent |
| CTA URLs mismatch implementation map | STOP → fix mapping before test |
| SKU missing in offer_stack | STOP → Offer Architect |
| Compliance FAIL on checkout | STOP → Compliance Agent |
| Upsell uses profit promise | STOP → rewrite |
| wp-admin 403 everywhere | Use setup scripts + iNET ticket — **do not** retry Elementor Library import |
| FunnelKit license missing | Fallback CartFlows free + same SKU binding |

---

## Outputs

- Updated `docs/funnelkit_checkout_map.md` (if flow changes)
- `web/wordpress/docs/funnelkit-elementor-setup.md` (if steps change)
- Checkout/TY copy mapping note in `.ai/audit/funnel-copy-map-{date}.md`
- QG-FUNNEL checklist in `.ai/audit/funnel-{date}.md`

---

## Acceptance criteria

- [ ] 4 SKUs exist (APP, VIP-MON, VIP-YR, DWY)
- [ ] Apprentice funnel: checkout + thank-you + Telegram CTA
- [ ] Checkout/TY copy matches Landing-Copy contract
- [ ] Risk acknowledgment checkbox in checkout spec
- [ ] Brevo tag map on purchase documented
- [ ] Compliance PASS on pay button microcopy
- [ ] Homepage offer buttons point to funnel URLs (not dead cart)
- [ ] Public checkout wording is English and matches canonical offer labels

---

## Commands reference

```bash
# If SSH + WP-CLI available on host
wp wc product create --name="Apprentice Operating Course" --type=simple \
  --sku=AE-APP-001 --regular_price=297 --status=publish

# No SSH — browser one-shot
http://hoa-homes.com/ae-setup-products.php?key=alpha-elite-2026
```
