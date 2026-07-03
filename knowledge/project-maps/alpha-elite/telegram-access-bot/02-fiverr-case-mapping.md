# 2 — Fiverr Case Mapping: Shop Bot → Alpha Elite

> **Source note:** Mapping is based on the **standard Telegram Shop Bot / Mini App feature set** described in the user brief — not a verbatim Fiverr gig export. Mechanisms are inferred at **medium confidence**; Alpha Elite constraints override shop-bot defaults.

---

## Feature translation matrix

| Fiverr / shop-bot feature | Generic shop behavior | Alpha Elite adaptation | MVP? |
|---------------------------|----------------------|------------------------|------|
| **Telegram Mini App** | In-chat web UI for catalog + account | Member **dashboard**: access status, links, onboarding | P1 |
| **Telegram Shop Bot** | Product browse + buy in chat | **Offer browser** → links to WP checkout (not in-bot card charge) | P0 |
| **Product catalog** | SKUs, prices, descriptions | Menu from `offer_stack.md` — compliance-safe copy | P0 |
| **Order status** | Paid / shipped / delivered | **Access status** model (payment → LMS → Telegram) | P0 |
| **Payment instruction** | Stripe / manual bank | PayPal + crypto **manual** + order ID | P0 |
| **Admin dashboard** | Web panel for orders | Sheets/Supabase queue + admin bot commands | P0 |
| **User dashboard** | Order history | Mini App: tier, LearnHouse link, VIP state | P1 |
| **Digital delivery** | Auto file / link | LearnHouse URL + Gameplan via **email** (bot shows status) | P0 |
| **Admin notification** | New order ping | Payment claim, support ticket, @username submitted | P0 |
| **WooCommerce webhook** | Auto-sync orders | **Deferred** — manual MVP first (`11-future-webhook-plan.md`) | P2 |

---

## What we deliberately do NOT port

| Shop-bot pattern | Why skip |
|------------------|----------|
| In-chat "Buy now" with instant digital unlock for trading signals | Positions as signal product |
| Push notifications for "new trade" | Alert channel framing |
| Win-rate or profit badges on products | Compliance P0 block |
| Fake scarcity / countdown in bot | `docs/compliance_guardrails.md` |
| Auto-add to VIP on payment webhook without review | MVP uses admin approve for Telegram |

---

## UI pattern mapping

```text
Fiverr Mini App typical          Alpha Elite Mini App
────────────────────────         ────────────────────────
Product grid                     Offer cards → open website
Cart + checkout                  → Redirect to FunnelKit URL
Order tracking                   Access status timeline
User profile                     Email + Telegram @ + tier
Admin orders list                Provision queue (LH + TG)
```

---

## Bot command mapping (suggested)

| Shop bot command | Alpha Elite command | Action |
|------------------|---------------------|--------|
| `/start` | `/start` | Welcome + disclaimer + main menu |
| `/shop` | `/offers` | Offer catalog (inline buttons) |
| `/orders` | `/status` | Access status lookup |
| `/pay` | `/pay` | Payment instructions |
| `/help` | `/support` | Support intake |
| — | `/onboard` | Tier-specific checklist |
| Admin `/orders` | `/admin queue` | Pending provisions |

---

## Data model delta

| Shop bot entity | Alpha Elite entity |
|-----------------|-------------------|
| `products` | `offers` (SKU, name, checkout_url, tier_level) |
| `orders` | `access_requests` (payment_claim + wc_order_id optional) |
| `order_items` | `entitlements` (learnhouse, telegram_vip, quant) |
| `users` | `members` (telegram_id, email, username, status) |
| `deliverables` | `provision_tasks` (LH enroll, TG add, email sent) |

---

## Acceptance

- [ ] Every shop feature has Alpha Elite equivalent or explicit deferral
- [ ] No mapped feature implies signal delivery or profit guarantee
- [ ] Checkout URLs use live SKUs from `docs/offer_stack.md`
