# Telegram VIP Onboarding SOP

**Trigger:** Tag `purchased_vip` in Brevo  
**SLA:** Add to group within 24h of username received

---

## Setup (one-time)

- [ ] Create private Telegram group "Alpha Elite VIP"
- [ ] Pin message: rules + `compliance_guardrails` short disclaimer
- [ ] Admin mods assigned
- [ ] Username collection: TY page form field or Google Form

---

## Per member

1. Receive @username from form or email reply
2. Verify active WooCommerce VIP subscription/order
3. Send invite link or direct add
4. Send welcome DM template:

```text
Chào [name], chào mừng vào Alpha Elite VIP.

Đọc pinned message trước khi tham gia thảo luận.
Nội dung mang tính giáo dục — không cam kết lợi nhuận.
Giao dịch có rủi ro; quyết định thuộc về bạn.

LearnHouse: https://learn.[domain].com
```

5. Brevo tag `telegram_added`
6. Log in ops sheet

---

## Mod guidelines

- Trade ideas = education framing
- No guaranteed profit replies
- Redirect financial advice questions to disclaimer
- Escalate compliance issues to owner
