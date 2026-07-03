# 11 — Compliance Checklist (Telegram Bot)

> **Parent:** `docs/compliance_guardrails.md` · `knowledge/.../10-compliance-guardrails.md`

---

## Positioning check

- [ ] Bot described as **member access & onboarding** — not signals  
- [ ] BotFather description / about text reviewed  
- [ ] No "VIP signals", "alerts", "copy trades" in any template  
- [ ] VIP framed as **rules-first accountability desk**  

---

## NEVER (block launch if found)

- [ ] Guaranteed profit or win rate  
- [ ] Risk-free trading claims  
- [ ] Passive income / bot earns while you sleep  
- [ ] Financial advice ("buy/sell now")  
- [ ] Fake scarcity (false seat limits)  
- [ ] Member profit / P&L proof  
- [ ] Signal-group positioning  

---

## ALWAYS

- [ ] `/start` includes short risk disclaimer  
- [ ] `/legal` or footer links full disclaimer  
- [ ] `/offers` — education framing per tier  
- [ ] `/pay` — educational products + risk line  
- [ ] LH message — education only, user owns decisions  
- [ ] VIP message — not alert channel; admin approved  
- [ ] Support replies — no trade recommendations  

---

## Required disclaimer (short — `/start`)

```text
Alpha Elite provides trading education, SOPs, and community support —
not investment advice or guaranteed returns. Trading involves substantial risk.
You may lose capital.
```

---

## Template review log

| Template | File | Compliance | Date |
|----------|------|------------|------|
| start_welcome | `bot/templates/start.md` | | |
| offers_* | `bot/templates/offers.md` | | |
| pay_* | `bot/templates/pay.md` | | |
| status_* | `bot/templates/status.md` | | |
| lh_ready | `bot/templates/learnhouse.md` | | |
| vip_ready | `bot/templates/vip.md` | | |
| support_ack | `bot/templates/support.md` | | |
| legal_full | `bot/templates/legal.md` | | |

---

## VIP group alignment

- [ ] Pinned group message matches bot disclaimer tone  
- [ ] Mod guidelines: `playbook/ops/telegram-onboarding-sop.md`  
- [ ] Bot does not auto-post trade content to group  

---

## Mini App (P1)

- [ ] No profit charts or green "gain" hero imagery  
- [ ] Status labels neutral ("Access active")  

---

## Incident response

| Severity | Example | Action |
|----------|---------|--------|
| P0 | Profit guarantee in live bot | Disable bot · fix · re-review |
| P1 | Missing disclaimer on `/pay` | Hotfix within 24h |
| P2 | Informal oversell in template | Rewrite |

Escalate P0/P1 to owner (G7).

---

## Pre-launch sign-off

```text
Reviewer: _______________
Date: _______________
Result: PASS / FAIL
Notes:
```

Store: `.ai/audit/compliance/YYYY-MM-DD-telegram-bot.md`

---

## Swap table (quick fix)

| Avoid | Use |
|-------|-----|
| VIP signals | VIP Private Desk · accountability |
| Guaranteed access to profits | Access to education & SOPs |
| Alert when we enter | Structured ideas in SOP format (education) |
| Bot prints money | Automation support documentation |
