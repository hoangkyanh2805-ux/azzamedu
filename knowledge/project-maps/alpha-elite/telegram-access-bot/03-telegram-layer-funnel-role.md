# 3 — Telegram Layer Role in Alpha Elite Funnel

## Position in the stack

Telegram is **not** the top-of-funnel acquisition engine for MVP. It supports **retention, access, and accountability** after (or alongside) the website.

```text
                    ACQUISITION              CONVERSION           ACCESS LAYER
                    ───────────              ──────────           ────────────

Traffic ──► WordPress / Elementor ──► WooCommerce / FunnelKit ──► LearnHouse
                │                           │                        │
                │ Brevo Gameplan            │ PayPal / crypto        │ Course delivery
                │                           │                        │
                └────────── optional ───────┴──── Telegram Bot ──────┘
                              discovery          · status / onboard
                                                 · payment help
                                                 · VIP desk (rules-first)
```

---

## When users meet the bot

| Entry point | User state | Bot job |
|-------------|------------|---------|
| Link on thank-you page | Just paid | Explain next steps + collect @username (VIP) |
| Link in Brevo email | Nurture / access ready | LearnHouse login help + support |
| Bio link / QR | Cold | Offers → website (not in-bot purchase of signals) |
| VIP group invite (after admin) | VIP active | Pinned rules — **group**, not bot broadcasts |

---

## Funnel stage alignment

| Stage | `user-journey.md` | Telegram role |
|-------|-------------------|---------------|
| Awareness | Stage 1 | Optional discovery; no trade alerts |
| Nurture | Stage 2 | Reminder to complete Gameplan; link `/apprentice` |
| Conversion | Stage 2 checkout | Payment instructions if manual path used |
| Onboard | Stage 3 | Status: "LearnHouse provisioning" → link when ready |
| VIP | Stage 4 | Username → admin queue → approved group add |
| Ascension | Stage 5 | Quant application link; no hype upsell in bot |

---

## VIP Private Desk vs bot

| VIP Telegram group | Access bot |
|--------------------|------------|
| Accountability desk, SOP discussions | Infrastructure: status, links, support |
| Structured ideas (education) in mod workflow | Never pushes entries |
| Human moderation | Automated templates only |
| Pinned compliance rules | `/start` disclaimer mirrors pinned |

**Principle:** Bot = **airport signage**. VIP group = **operating floor**.

---

## Mini App role (P1)

Embedded web UI inside Telegram for:

- Visual access timeline (payment → LH → VIP)
- One-tap open LearnHouse
- Copy payment reference
- Submit support ticket

Keeps heavy UI out of chat messages; reduces support load.

---

## Metrics (MVP)

| Metric | Target | Tool |
|--------|--------|------|
| Payment claim → admin ack | ≤4h business hours | Ops log |
| Provision complete | ≤24h | Same as SOP |
| Support first response | ≤24h | Admin notification |
| Bot compliance incidents | 0 P0 | Mod + audit |

---

## Anti-patterns

- Using bot broadcast for "daily setups" → use VIP desk with mod framing
- Replacing Brevo nurture with bot spam
- Auto-adding users to VIP without payment verification
