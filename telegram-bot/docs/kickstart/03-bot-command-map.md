# 3 — Bot Command Map

> **Auth:** Every `/start` registers `telegram_id`. Optional `?start=order_{wc_id}` deep link.

---

## User commands

| Command | Handler | Description |
|---------|---------|-------------|
| `/start` | `handlers.start` | Disclaimer + main menu; upsert member |
| `/menu` | `handlers.menu` | Return main keyboard |
| `/offers` | `handlers.offers` | Inline catalog (5 offers) |
| `/status` | `handlers.status` | Tier + status timeline |
| `/pay` | `handlers.pay` | SKU select → PayPal/crypto instructions |
| `/onboard` | `handlers.onboard` | Checklist by tier |
| `/support` | `handlers.support` | Free-text ticket → admin |
| `/link` | `handlers.link` | Associate email to telegram_id |
| `/legal` | `handlers.legal` | Full risk disclaimer |

---

## Main menu keyboard

```text
┌─────────────────┬─────────────────┐
│  📋 Offers      │  🔑 My Access   │
├─────────────────┼─────────────────┤
│  💳 Payment     │  🧭 Onboarding  │
├─────────────────┼─────────────────┤
│  💬 Support     │  ⚠️ Disclaimer  │
└─────────────────┴─────────────────┘
```

Maps to commands above.

---

## `/offers` inline actions

| Button | Action |
|--------|--------|
| Free Alpha Elite Gameplan | URL → `{site}/gameplan` |
| Apprentice Course | URL → checkout `AE-APP-001` |
| VIP Private System | Submenu: Monthly / Annual |
| Quant Desk | URL → `{site}/quant-desk` |
| Done-With-You Setup | Text: VIP checkout bump `AE-DWY-001` |
| ← Back | Main menu |

---

## `/pay` flow

```text
/pay
  → Select SKU (APP / VIP-MON / VIP-YR / Quant note)
  → Show PayPal + crypto blocks (G6 approved text)
  → [Submit payment proof] → FSM: wait for photo/text
  → Save queue row → status payment_review
  → notify_admin("NEW PAYMENT REVIEW")
```

---

## `/status` display tiers

| Label shown | Internal `tier` |
|-------------|-----------------|
| Free | `free` |
| Apprentice | `apprentice` |
| VIP | `vip` |
| Quant | `quant` |
| Inner Circle | `inner_circle` |

---

## Admin commands (`ADMIN_TELEGRAM_IDS` only)

| Command | Action |
|---------|--------|
| `/admin` | Help text |
| `/admin pending` | List open queue rows |
| `/admin confirm <code>` | → `payment_confirmed` + notify user |
| `/admin reject <code> <reason>` | → `pending_payment` + notify user |
| `/admin provisioned <code>` | LH instructions sent (after human G4) |
| `/admin tgdone <code>` | VIP complete (after human G5) |
| `/admin revoke <code>` | → `revoked` |

---

## Callback data (inline buttons)

| pattern | Purpose |
|---------|---------|
| `offer:gameplan` | Open gameplan URL |
| `offer:app` | Apprentice checkout |
| `offer:vip:mon` | VIP monthly |
| `offer:vip:yr` | VIP annual |
| `offer:quant` | Quant page |
| `pay:sku:AE-APP-001` | Payment instructions |
| `pay:submit` | Start proof upload FSM |
| `onboard:{tier}` | Tier checklist |

---

## Mini App (P1)

| Entry | URL |
|-------|-----|
| Menu button | `https://bot.yourdomain.com/miniapp/` |
| WebApp data | `telegram_id` via `initData` validation |

Shows: status timeline, LH button, support link.

---

## BotFather command list

```text
start - Main menu and disclaimer
offers - View offers and checkout links
status - Your access status
pay - Payment instructions (PayPal / crypto)
onboard - Onboarding checklist
support - Contact support
legal - Risk disclaimer
```

---

## Handler file map (implementation)

```text
bot/handlers/
├── start.py
├── offers.py
├── status.py
├── pay.py
├── onboard.py
├── support.py
├── admin.py
└── common.py          # disclaimer, keyboards
```
