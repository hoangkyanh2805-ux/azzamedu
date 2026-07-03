# 4 — User Journey

## Journey A — Free lead (Gameplan)

```text
1. User finds bot (bio link / thank-you page / ad)
2. /start → disclaimer + menu
3. /offers → Free Gameplan → opens website opt-in
4. Brevo delivers PDF (off-bot)
5. /onboard → Gameplan 7-day checklist
6. Optional: /offers → Apprentice when ready
```

**Tier:** Free · **Status:** `lead`

---

## Journey B — Website checkout (preferred)

```text
1. User buys on WooCommerce / FunnelKit
2. Thank-you page: "Open Telegram bot" ?start=order_{id}
3. /start → links telegram_id + order (P2 auto; MVP manual /link email)
4. /status → provisioning
5. Admin G4 → bot sends LearnHouse instructions
6. VIP: user /onboard → submit @username
7. Admin G5 → bot: VIP invite instructions
8. /status → Access active
```

---

## Journey C — Manual PayPal / crypto

```text
1. /offers → choose tier
2. /pay → instructions + amount
3. User pays externally
4. Submit proof (screenshot / txn ID)
5. /status → "Payment under review"
6. Admin confirm → provisioning → G4 → G5 (if VIP)
```

---

## Journey D — Support

```text
1. /support
2. User describes issue (login, payment, VIP delay)
3. Ticket created → admin notified
4. Admin replies out-of-band or via bot reply template
5. Ticket closed
```

---

## Journey E — Quant Desk

```text
1. /offers → Quant Desk → website application
2. /status → Free or Apprentice until approved
3. Admin manual tier upgrade after application review
4. /onboard → Quant desk rules (education only)
```

---

## Journey F — Inner Circle (deferred)

```text
Waitlist link only — no automated invite at MVP
Tier label: Inner Circle · status manual
```

---

## Touchpoint matrix

| Step | Bot | Website | Email | Human |
|------|:---:|:-------:|:-----:|:-----:|
| Discover offers | ✓ | ✓ | ✓ | — |
| Pay card | link | ✓ | receipt | — |
| Pay manual | ✓ | — | — | verify |
| LearnHouse access | notify | — | ✓ | G4 enroll |
| VIP group | notify | form | ✓ | G5 add |
| Support | ✓ | — | optional | reply |

---

## Emotional beats (design intent)

| Moment | User feels | Bot must |
|--------|------------|----------|
| /start | Cautious (trading niche) | Clear disclaimer + calm tone |
| After pay | Anxious | "Under review" + SLA 24h |
| LH ready | Relieved | Direct link + first step |
| VIP pending | Waiting | Explain admin approval — not rejection |
| Support | Heard | Ticket ID + no hype |

---

## Compliance moments

- `/start` — short risk disclaimer  
- `/offers` — no profit promises  
- `/pay` — education product + risk line  
- `/onboard` VIP — rules-first desk, not signals  

---

## Acceptance

- [ ] Each journey has defined tier/status transitions  
- [ ] No journey promises trading outcomes  
- [ ] VIP never instant without admin path
