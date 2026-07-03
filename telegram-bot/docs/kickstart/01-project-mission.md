# 1 — Project Mission: Alpha Elite Telegram Access Bot

## One-line mission

Build a **Telegram Bot + Mini App** that gives members **compliant access infrastructure** — offers, status, onboarding, payment help, support, and admin-approved VIP desk entry — **not** trade signals or financial advice.

---

## Problem

After website checkout, members need a single place to:

- Know what they bought and what’s next  
- Get LearnHouse login help  
- Submit VIP @username for admin approval  
- Pay via PayPal/crypto when not using card checkout  
- Contact support without DM chaos  

Today this is manual email + ops spreadsheet. The bot standardizes it without becoming a signal channel.

---

## Audience

| Persona | Need |
|---------|------|
| **Free lead** | Gameplan path, offer discovery |
| **Apprentice buyer** | LH access status + onboarding |
| **VIP member** | VIP approval status + desk rules reminder |
| **Quant applicant** | Application link + status |
| **Admin ops** | Queue, notifications, audit trail |

---

## Success metrics (MVP)

| Metric | Target |
|--------|--------|
| Payment → admin notified | < 5 min (automated) |
| Payment confirmed → LH instructions | ≤ 24h (human G4) |
| VIP @username → group add | ≤ 24h after G4 (human G5) |
| Support ticket → admin notified | < 5 min |
| Compliance incidents (P0) | 0 at launch |
| Signal-style broadcasts | 0 (forbidden) |

---

## Non-goals (explicit)

- ❌ Signal / alert broadcasting  
- ❌ Guaranteed profit or win-rate messaging  
- ❌ Automated trade execution  
- ❌ Replacing WooCommerce checkout (website remains primary)  
- ❌ Auto-add VIP without admin (MVP)  
- ❌ LearnHouse API auto-enroll (MVP — manual G4)

---

## Positioning statement

> Alpha Elite Telegram Access Bot is **member access and onboarding infrastructure** for a private trading **education** operating system. It delivers digital access coordination — not investment advice or trade alerts.

---

## Constraints

- Compliance: `docs/compliance_guardrails.md` + `11-compliance-checklist.md`  
- Human gates G4 (LearnHouse), G5 (Telegram VIP), G1-bot (launch)  
- Python + Telegram Bot API  
- Supabase or Google Sheets for MVP DB  
- PayPal + crypto manual first  

---

## Assumptions

- WordPress / WooCommerce / FunnelKit checkout exists or ships in parallel  
- LearnHouse provision stays manual ≤24h at MVP  
- VIP group moderation remains human  
- English primary; Vietnamese optional later  

---

## Parent project alignment

| Alpha Elite artifact | Bot dependency |
|---------------------|----------------|
| `docs/offer_stack.md` | Offer menu + SKUs |
| `playbook/ops/learnhouse-provision-sop.md` | G4 |
| `playbook/ops/telegram-onboarding-sop.md` | G5 |
| `web/wordpress/pricing-draft-g0.md` | `/pay` amounts (G0) |

---

## Acceptance (mission level)

- [ ] Stakeholder agrees: bot is **access layer**, not signal product  
- [ ] MVP manual provision rule accepted  
- [ ] Success metrics measurable from queue + audit log
