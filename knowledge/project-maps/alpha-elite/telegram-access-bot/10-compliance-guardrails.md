# 10 — Compliance Guardrails (Telegram Bot)

> Extends `docs/compliance_guardrails.md` and `.ai/rules/compliance-trading.md` for **bot + Mini App + VIP group entry**.

---

## Positioning (required)

**Say:** member access · onboarding · support · digital delivery · education · operating system · accountability

**Never say:** signals · alerts · guaranteed profit · risk-free · passive income · financial advice · copy our trades

---

## NEVER in bot copy (block publish)

| # | Prohibited | Example (wrong) |
|---|------------|-----------------|
| 1 | Guaranteed profit | "Join VIP to make 20%/month" |
| 2 | Signal / alert framing | "Daily XAUUSD entries posted here" |
| 3 | Risk-free | "Safe trades with our system" |
| 4 | Bot earns for you | "Automation makes money while you sleep" |
| 5 | Financial advice CTA | "Buy gold now" |
| 6 | Win-rate hype | "90% win rate members" |
| 7 | Fake urgency | "Only 3 seats" (if false) |
| 8 | Unapproved investment claims | Implied licensed advisory |

---

## ALWAYS include

### `/start` micro disclaimer (short)

```text
Alpha Elite provides trading education, SOPs, and community support — not investment advice or guaranteed returns. Trading involves substantial risk. You may lose capital.
```

### Payment / access messages

Append or link:

```text
Educational products only. No profit guarantees.
```

### Full disclaimer (footer command or `/legal`)

Mirror `docs/compliance_guardrails.md` risk block — EN primary; VI optional for VN users.

---

## VIP group vs bot

| VIP group (human mods) | Bot (automated) |
|------------------------|-----------------|
| Structured ideas in SOP format | No trade entries |
| Mod enforces education framing | Templates only |
| Pinned rules + disclaimer | `/start` mirrors pinned |

Bot must **not** auto-forward "trade ideas" to users.

---

## Support reply rules

| User asks | Bot / admin may | Must not |
|-----------|-----------------|----------|
| "When to buy?" | Point to education / SOP | Give entry price |
| "Will I profit?" | Risk disclaimer + education scope | Promise outcomes |
| "Add me to signals" | Clarify VIP is accountability desk | Agree it's signals |
| Login help | LearnHouse link | — |

---

## Mini App UI

- No P&L charts or profit green accents as promise
- Status labels: "Access active" not "Profits unlocked"
- Offer cards: feature checklists, not ROI badges

---

## Admin / mod escalation

Stop and escalate to owner if:

- User requests guaranteed-profit bot messages
- Request to broadcast live entries via bot
- Removal of disclaimers from `/start`

---

## Pre-launch checklist

- [ ] Every template in `bot/templates/` reviewed
- [ ] `/offers` copy matches `compliance-copy-audit.md` tone
- [ ] Payment messages include education + risk line
- [ ] VIP onboarding states admin approval required
- [ ] Pinned group message matches bot disclaimer
- [ ] No P0/P1 open per `docs/risk-compliance-checklist.md`

---

## Severity

| Level | Example | Action |
|-------|---------|--------|
| P0 | Profit guarantee in `/start` | Block bot launch |
| P1 | Missing disclaimer on payment flow | Fix before traffic |
| P2 | Ambiguous "passive" in offer blurb | Rewrite 24h |
| P3 | Informal oversell in support | Correct template |

---

## Review workflow

```text
Draft template → swap table self-check → Compliance Agent → PASS/FAIL → G1 human sign-off → deploy
```

Log: `.ai/audit/compliance/YYYY-MM-DD-telegram-bot.md`
