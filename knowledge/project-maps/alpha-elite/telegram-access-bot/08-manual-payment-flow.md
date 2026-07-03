# 8 — Manual Payment Flow

> MVP payments: **PayPal** + **crypto (manual)** + **WooCommerce card** (website).  
> Bot supports manual paths where checkout is not used or proof is required.

---

## Payment channels

| Channel | Primary use | Verification |
|---------|-------------|--------------|
| **WooCommerce + PayPal** | Website checkout | WC order status = Processing/Completed |
| **PayPal manual** | DM / bot `/pay` | Admin matches email + amount + txn ID |
| **Crypto manual** | International / preference | Admin matches wallet + tx hash |
| **FunnelKit TY** | Card flow | Same as WC |

---

## User flow (bot manual path)

```text
1. User: /offers → chooses Apprentice or VIP
2. User: /pay → receives instructions (below)
3. User pays via PayPal or crypto
4. User: taps "Submit payment proof" → sends screenshot or txn ID
5. Bot: creates queue row → status payment_review
6. Admin: verifies → /admin confirm
7. Bot: notifies user → provisioning message
```

---

## PayPal instruction template

```text
PayPal payment (manual)

Send to: hello@yourdomain.com (Friends & Family or Goods — as per your policy)
Amount: {amount} USD
Reference: {email} · {sku}

After paying, reply here with:
· PayPal transaction ID
· Screenshot (optional)

We confirm within 24 business hours. Education product — no refunds for policy violations.

Trading involves risk. Not investment advice.
```

**G0:** Confirm PayPal account + Goods & Services policy on checkout.

---

## Crypto instruction template

```text
Crypto payment (manual)

Network: {USDT TRC20 / specify}
Wallet: {address}
Amount: {amount} USD equivalent
Reference: {email} · {sku}

Send exact amount. After transfer, submit:
· Transaction hash (TXID)
· Network used

Confirmation may take up to 24h. Trading involves risk.
```

**Security:** Wallet address only in bot after `/pay` — rotate if compromised.

---

## Proof submission (bot)

| Field | Required |
|-------|----------|
| Email | Yes — must match payer |
| SKU / tier | Yes |
| Transaction ID or hash | Yes |
| Screenshot | Optional |

Bot stores: `telegram_file_id`, timestamp, links to queue `id`.

---

## Admin verification checklist

- [ ] Amount matches SKU (draft: APP $297, VIP-MON $149, VIP-YR $1290)
- [ ] Reference email matches member record
- [ ] No duplicate txn ID in sheet
- [ ] PayPal/crypto received in correct account
- [ ] Create or link WooCommerce order (optional manual order for books)

---

## WooCommerce-first path (preferred)

When user pays on website:

1. User may still open bot for `/status`
2. Admin matches `wc_order_id` + billing email
3. Skip manual proof if order already **Completed**
4. Bot status set from admin or future webhook

---

## Refund / failed payment

| Event | Bot status | Action |
|-------|------------|--------|
| Rejected proof | `pending_payment` | Send reason template |
| Partial payment | hold | Request difference |
| Refund issued | `revoked` | Revoke LH + TG |

---

## Compliance footer (every payment message)

```text
Educational products only. No profit guarantees. Not financial advice.
See refund policy: https://yourdomain.com/refund-policy
```

---

## Acceptance

- [ ] Instructions never promise trading returns
- [ ] SKU amounts synced with `pricing-draft-g0.md` after G0
- [ ] Duplicate txn detection documented
