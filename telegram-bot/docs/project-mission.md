# Project Mission — Alpha Elite Telegram Access Bot

## One-line mission

Build a **Telegram Bot / Mini App** that gives members **compliant access infrastructure** — offers, status, onboarding, payment help, support, and admin-approved VIP desk entry — **not** trade signals or financial advice.

## Problem

After website checkout, members need one place to:

- See what they bought and what happens next
- Get LearnHouse login help
- Submit VIP @username for admin approval
- Pay via PayPal/crypto when not using card checkout
- Contact support without DM chaos

The bot standardizes ops without becoming a signal channel.

## Audience

| Persona | Need |
|---------|------|
| Free lead | Gameplan path, offer discovery |
| Apprentice buyer | LearnHouse status + onboarding |
| VIP member | VIP approval status + desk rules |
| Quant applicant | Application link + status |
| Admin ops | Queue, notifications, audit |

## Success metrics (MVP)

| Metric | Target |
|--------|--------|
| Payment → admin notified | < 5 min |
| Payment confirmed → LH instructions | ≤ 24h (human G4) |
| VIP @username → group add | ≤ 24h after G4 (human G5) |
| Support ticket → admin notified | < 5 min |
| Compliance P0 incidents | 0 at launch |
| Signal-style broadcasts | 0 (forbidden) |

## Non-goals

- Signal / alert broadcasting
- Guaranteed profit or win-rate messaging
- Automated trade execution
- Replacing WooCommerce checkout
- Auto-add VIP without admin (MVP)
- LearnHouse API auto-enroll (MVP)

## Positioning

> Alpha Elite Telegram Access Bot is **member access and onboarding infrastructure** for a private trading **education** operating system. It delivers digital access coordination — not investment advice or trade alerts.

## Stack

| Layer | Choice |
|-------|--------|
| Bot | Telegram Bot API, Python (`python-telegram-bot`) |
| DB MVP | Supabase (recommended) or Google Sheets |
| Payments MVP | PayPal + crypto manual; WooCommerce primary |
| LMS | LearnHouse — manual provision (G4) |
| Website | WordPress / WooCommerce / FunnelKit |

## Human gates

| Gate | Owner | Action |
|------|-------|--------|
| G4 | Ops | Create LearnHouse user |
| G5 | Ops | Approve VIP Telegram access |
| G1-bot | Compliance | Launch sign-off |

## Canonical MVP rule

```
Payment/apply → admin review → admin creates LearnHouse user
→ admin approves Telegram VIP → bot sends onboarding instructions
```
