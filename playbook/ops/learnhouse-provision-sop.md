# LearnHouse Provision SOP

**Trigger:** payment confirmed, VIP/deposit approved, or owner manually grants access.  
**SLA:** provision within 24 hours after approval.  
**Owner:** Admin Ops.

Production LMS: `https://learn.azzamedu.com`

---

## Access Groups

Use **UserGroups** as the source of truth for access. A user can belong to one or more groups.

| Dashboard group | Slug | Who gets it | Courses / access |
|---|---|---|---|
| SMC course | `smc-cours` | Base course buyer or manual grant | Advanced SMC course |
| VIP $1000 | `vip-1000` | VIP entry package | VIP access + 1-2 bonus courses |
| Deposit $3k-$5k | `deposit-3k-5k` | Deposit tier 3k-5k | Mid-tier course bundle |
| Deposit >$5k-$10k | `full-access` | Deposit tier above 5k up to 10k | Full course library |

Current dashboard groups:

- `full-access` / "Deposit >$5k-$10k"
- `deposit-3k-5k`
- `vip-1000`
- `smc-cours`

If a group name is corrected later, update this table and keep the slug consistent in ops logs.

---

## Standard Provision Flow

### 1. Verify access reason

Before creating or changing a user, confirm:

- Customer email.
- Payment/order/deposit evidence.
- Group to assign.
- Courses included.
- Whether VIP Telegram access is included.

Example:

```text
Customer: hoangvu.linhan2805@gmail.com
Reason: SMC course manual grant
Group: smc-cours
Courses: Advanced trading course : The complete Smart Money Concepts
```

### 2. Create LearnHouse user

Fast manual path while SMTP is not fully tested:

1. Open an incognito browser.
2. Go to `https://learn.azzamedu.com/signup`.
3. Create the account:

```text
Email: hoangvu.linhan2805@gmail.com
Username: hoangvulinhan2805
Password: [generate and save in vault]
```

Username rule: use the email prefix, remove dots/special characters, keep it lowercase.

4. Test login immediately at `https://learn.azzamedu.com/login`.
5. Confirm the user can reach the dashboard.

Do not send the password through Telegram bot. Use Brevo/Gmail/Zalo according to the customer support context.

### 3. Assign UserGroup

In LearnHouse admin:

1. Go to **Users -> UserGroups**.
2. Find the target group.
3. Click **Manage Users**.
4. Add the customer email/user.
5. Confirm member count increases.

Example:

```text
User: hoangvu.linhan2805@gmail.com
Group: smc-cours
```

### 4. Enroll course access

In LearnHouse admin:

1. Go to **Courses**.
2. Open the required course.
3. Use **Enroll / Manage learners**.
4. Add the user or the relevant group if LearnHouse allows group-level course access.
5. Save.

Spot-check with the user login:

- Correct courses are visible.
- `Start Learning` opens.
- Courses outside the package are hidden.

### 5. Send customer login

Copy-paste template:

```text
Chào bạn,

Tài khoản học của bạn đã sẵn sàng:

Link đăng nhập: https://learn.azzamedu.com/login
Email: hoangvu.linhan2805@gmail.com
Mật khẩu: [password đã tạo]

Sau khi đăng nhập, bấm Start Learning để bắt đầu học.

Nội dung chỉ mang tính giáo dục, không phải lời khuyên đầu tư.
```

### 6. Close the loop

Record this in Woo order note, ops sheet, or CRM:

```text
Customer: hoangvu.linhan2805@gmail.com
LearnHouse username: hoangvulinhan2805
Group: smc-cours
Courses: Advanced SMC Course
Provisioned: YYYY-MM-DD
Admin: [name]
Login tested: yes
```

If the Telegram bot queue is used:

```text
/provisioned AE-2026-XXXX
```

---

## Package Rules

| Access case | Assign group | Enroll courses | Extra ops |
|---|---|---|---|
| Course 1 only | `smc-cours` | Advanced SMC Course | No VIP Telegram |
| VIP $1000 | `vip-1000` | VIP package + 1-2 bonus courses | Add to VIP Telegram if included |
| Deposit $3k-$5k | `deposit-3k-5k` | Mid-tier bundle | Log deposit proof |
| Deposit >$5k-$10k | `full-access` | Full library | Log deposit proof + full access approval |

When in doubt, assign the narrower group first. Upgrade after owner approval.

---

## SMTP / Invite Members Quick Setup

Manual signup remains the safest fallback. Configure SMTP only when you want LearnHouse **Invite Members** to send email directly.

Recommended provider: **Brevo SMTP**.

Brevo values:

```text
Host: smtp-relay.brevo.com
Port: 587
Encryption: STARTTLS / TLS
Username: Brevo SMTP login
Password: Brevo SMTP key
From email: verified sender email
From name: Azzam Gold
```

Dashboard path to check first:

```text
Organization / Settings / Email / SMTP
```

If LearnHouse exposes SMTP fields, fill the Brevo values, save, then send one invite to a test email.

If there is no SMTP form, inspect the VPS config:

```bash
cd /opt/learnhouse
grep -R "SMTP\|MAIL\|EMAIL" -n .env* docker-compose* learnhouse.config.json 2>/dev/null
```

Set the matching variables if they exist:

```env
SMTP_HOST=smtp-relay.brevo.com
SMTP_PORT=587
SMTP_USER=[brevo smtp login]
SMTP_PASSWORD=[brevo smtp key]
SMTP_FROM_EMAIL=[verified sender email]
SMTP_FROM_NAME=Azzam Gold
SMTP_TLS=true
```

Restart after changes:

```bash
npx learnhouse restart
```

or:

```bash
docker compose restart
```

Test rule: invite a test inbox first. Do not test first on a real customer.

---

## Refund / Revoke

1. Remove user from the package UserGroup.
2. Remove course enrollment if still visible.
3. Remove from VIP Telegram if applicable.
4. Update Brevo/CRM tags.
5. Add order note:

```text
Access revoked YYYY-MM-DD by [admin]
Reason: refund / chargeback / owner decision
```

---

## Escalation

- Payment unclear -> hold provision and contact customer.
- Duplicate email/order -> verify before double-enrolling.
- Email bounce -> contact via alternate channel.
- Group/course mismatch -> assign the narrower access, then ask owner to approve upgrade.
