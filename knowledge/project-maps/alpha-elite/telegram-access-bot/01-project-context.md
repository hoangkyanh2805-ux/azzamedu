# 1 — Project Context: Alpha Elite Telegram Access Bot

## Purpose

Build a **Telegram Bot + optional Mini App** as the **member access and operations layer** for Alpha Elite — a private XAUUSD trading **education and operating system**, not a signal group.

The bot helps paying and prospective members:

- View available offers (catalog → website checkout)
- Check order / access status
- Receive onboarding instructions
- Contact support
- Get **manual** payment instructions (PayPal / crypto at MVP)
- Receive **admin-approved** VIP Telegram group access

It does **not** broadcast trade entries, guaranteed profits, or financial advice.

---

## Product positioning

| Alpha Elite is | Alpha Elite is not |
|----------------|-------------------|
| Education + SOPs + community accountability | Signal spam / alert channel |
| Structured trade ideas inside frameworks | Copy-trade service |
| Manual VIP desk access after payment | Instant unvetted group join |
| Access + onboarding infrastructure | Trading bot that earns for you |

Approved line (from `docs/compliance_guardrails.md`):

> Private financial operating system — education, structured trade ideas, automation support, SOPs, and community support — with 2% risk discipline.

---

## Stack (MVP → growth)

| Layer | MVP | Future |
|-------|-----|--------|
| **Telegram** | Bot API + Mini App (Web App) | Same |
| **Runtime** | Python 3.11+ | Container on VPS |
| **Bot framework** | `python-telegram-bot` or `aiogram` | Either |
| **Database** | Google Sheets **or** Supabase | Supabase preferred at scale |
| **Payments** | PayPal + crypto **manual** confirm | WooCommerce webhooks |
| **LMS** | LearnHouse — **manual** enroll ≤24h | API / webhook enroll |
| **Website checkout** | WordPress + WooCommerce + FunnelKit | Primary conversion path |
| **Email** | Brevo (parallel nurture) | Tags sync from bot optional |

---

## Actors

| Actor | Role |
|-------|------|
| **Prospect** | Discovers bot or site; may request Gameplan |
| **Customer** | Paid Apprentice / VIP / Quant |
| **Admin Ops** | Confirms payment, provisions LearnHouse, approves Telegram |
| **Moderator** | VIP group rules — not bot automation |
| **Compliance reviewer** | Blocks prohibited bot copy before launch |

---

## Boundaries

**In scope for bot**

- Offer catalog (links to WP pages / checkout)
- Access status lookup by email + order ref
- Payment instruction messages (templates)
- Onboarding checklists (Gameplan, Apprentice, VIP)
- Support ticket intake (message → admin)
- VIP username collection → admin queue
- Admin alerts on new payment claims

**Out of scope (MVP)**

- Live trade alerts / signal feeds
- Automated trade execution
- Profit tracking / P&L dashboards
- Instant Telegram join without admin approval
- Licensed investment advice

---

## Success criteria (MVP)

- [ ] User can see offers and open correct checkout URL
- [ ] User can submit manual payment proof → admin notified
- [ ] Admin can mark paid → status updates → customer notified
- [ ] LearnHouse + VIP steps documented in bot messages
- [ ] All bot copy passes compliance checklist (`10-compliance-guardrails.md`)
- [ ] ≤24h provision SLA aligned with `playbook/ops/learnhouse-provision-sop.md`

---

## Repo links

- Offers: `docs/offer_stack.md` · draft prices: `web/wordpress/pricing-draft-g0.md`
- Journey: `docs/user-journey.md` stages 3–4 (onboard + VIP)
- System map: `docs/mvp-system-map.md`
