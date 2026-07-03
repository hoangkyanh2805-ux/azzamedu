# User Journey

## Journey A — Free lead (Gameplan)

1. User finds Alpha Elite website or bot link
2. `/start` → disclaimer + main menu
3. **Offers** → taps **Free Gameplan** → website opt-in (Brevo)
4. **Onboarding** → Gameplan checklist
5. Optional: explores Apprentice/VIP offers

**Bot tier:** `free` · **Status:** `lead`

---

## Journey B — Website checkout (Apprentice / VIP)

1. User buys on WooCommerce (primary path)
2. Thank-you page: "Open Telegram bot" deep link
3. `/start` → bot upserts member by `telegram_id`
4. User taps **My Access** → `pending_payment` or `lead` until linked
5. User submits payment proof if paid off-site OR admin links `wc_order_id` (P2 webhook)
6. Admin confirms → LearnHouse provisioned (G4) → bot sends LH instructions
7. VIP: user may submit @username → admin adds to group (G5) → `/tgdone`

---

## Journey C — Manual PayPal / crypto

1. `/start` → **Payment**
2. Reads PayPal email + crypto wallet
3. Pays externally
4. **Submit payment proof** → email + screenshot/TX ID
5. Receives queue code `AE-YYYY-NNNN`
6. **My Access** shows `payment_review`
7. After admin approval → same as Journey B steps 6–7

---

## Journey D — Quant Desk application

1. **Offers** → **Quant Desk** → website `/quant-desk`
2. Fills application form (not instant buy)
3. Admin reviews → manual tier upgrade
4. Bot status updated to `quant` / `access_active_quant`

---

## Journey E — Support

1. **Support** → describe issue
2. Ticket `SUP-NNNN` created
3. Admin notified in Telegram
4. Human replies via email or DM (MVP manual)

---

## Status labels (user-facing)

| Label | Meaning |
|-------|---------|
| Free member | Gameplan / browsing |
| Payment under review | Proof submitted |
| Setting up access | Admin working G4 |
| LearnHouse ready | LH login sent |
| VIP — awaiting admin approval | @username / group pending |
| VIP access active | G5 complete |

---

## Touchpoints checklist

- [ ] `/start` disclaimer visible
- [ ] Checkout URLs match live WooCommerce SKUs
- [ ] LearnHouse URL correct in config
- [ ] VIP invite message matches actual group policy
