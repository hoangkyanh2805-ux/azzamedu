# LearnHouse Provision SOP

**Trigger:** WooCommerce order status = Processing or Completed  
**SLA:** 24 giờ từ thanh toán thành công  
**Owner:** Admin Ops

---

## SKU → Action

| SKU | LearnHouse group | Courses to enroll |
|-----|------------------|-------------------|
| AE-APP-001 | apprentice-students | Apprentice Operating Course |
| AE-VIP-MON | vip-members | Apprentice + VIP Resource Library |
| AE-VIP-YR | vip-members | Apprentice + VIP Resource Library |
| AE-QNT-001 | quant-desk | All above + Quant (when live) |

---

## Steps

### 1. Verify payment
- [ ] Order paid, not refunded
- [ ] Email matches order billing email
- [ ] Note order ID in spreadsheet/log

### 2. LearnHouse user
- [ ] Login LearnHouse admin → Users → Add
- [ ] Email = order email
- [ ] Send password reset (user sets own password)

### 3. Enroll
- [ ] Assign user group per SKU table
- [ ] Enroll listed courses
- [ ] Spot-check: user sees Module 1

### 4. Email customer
- [ ] Brevo: send `access_ready_learnhouse` template
- [ ] Or manual send with login URL `https://learn.[domain].com`
- [ ] Tag `access_ready` in Brevo

### 5. VIP only — Telegram
- [ ] Check TY form for @username
- [ ] If missing: send V0 reminder email
- [ ] Add to VIP Telegram group
- [ ] Confirm welcome pinned message visible
- [ ] Tag `telegram_added`

### 6. Close loop
- [ ] WooCommerce order note: `Provisioned YYYY-MM-DD by [name]`
- [ ] Mark complete in ops log

---

## Refund / revoke

1. Remove LearnHouse enrollment
2. Remove from Telegram
3. Update Brevo tags
4. Order note: `Access revoked YYYY-MM-DD`

---

## Escalation

- Payment unclear → hold provision, contact customer
- Duplicate order → verify before double enroll
- Email bounce → contact via alternate channel
