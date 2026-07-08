# LearnHouse Admin Setup Checklist

Run once after production deploy. Owner: **Admin Ops**.

Production LMS: `https://learn.azzamedu.com`

---

## 1. Organization

- [ ] Log in as admin: `admin@hoa-homes.com`
- [ ] Organization name: **Azzam Gold** or **Alpha Elite** (match current dashboard branding)
- [ ] Logo uploaded
- [ ] Default language reviewed
- [ ] Footer/about links to the risk disclaimer

---

## 2. UserGroups

Create/manage groups from:

```text
Users -> UserGroups -> Create a UserGroup
```

Current access groups:

| Dashboard name | Slug | Purpose |
|---|---|---|
| SMC course | `smc-cours` | Base course / Course 1 access |
| VIP $1000 | `vip-1000` | VIP entry package + 1-2 bonus courses |
| Deposit $3k-$5k | `deposit-3k-5k` | Mid-tier deposit bundle |
| Deposit >$5k-$10k | `full-access` | Full course library |

- [ ] All four groups exist in dashboard
- [ ] Each group has a clear description
- [ ] Test user can be added through **Manage Users**
- [ ] Member count updates after adding a user

Naming note: the current dashboard slug is `smc-cours`. Keep it as-is until you intentionally rename it, then update all SOP docs and logs.

---

## 3. Courses

Current live course:

| Course | Access group |
|---|---|
| Advanced trading course : The complete Smart Money Concepts | `smc-cours` |

Planned/package courses:

| Course / library | Access groups |
|---|---|
| VIP resources / bonus courses | `vip-1000`, `deposit-3k-5k`, `full-access` |
| Mid-tier bundle courses | `deposit-3k-5k`, `full-access` |
| Full course library | `full-access` |

- [ ] Course is published
- [ ] Course visibility is private/enrolled-only if available
- [ ] Correct users/groups are enrolled
- [ ] A test learner can click **Start Learning**

---

## 4. Manual User Provision Test

Use test or real approved email:

```text
Email: hoangvu.linhan2805@gmail.com
Username: hoangvulinhan2805
Group: smc-cours
Course: Advanced SMC Course
```

Provision steps:

1. Create account via `https://learn.azzamedu.com/signup` in incognito.
2. Test login at `https://learn.azzamedu.com/login`.
3. Go to **Users -> UserGroups**.
4. Click **Manage Users** on the target group.
5. Add user.
6. Go to **Courses** and enroll the user/course if group-level access is not automatic.
7. Login as the user and confirm course visibility.
8. Send login details by Brevo/Gmail/Zalo.
9. Record the provision log.

- [ ] Login tested
- [ ] Correct group assigned
- [ ] Correct course visible
- [ ] Non-included courses hidden
- [ ] Ops log recorded

---

## 5. SMTP / Invite Members

Manual signup is the fallback. Configure SMTP only when you want LearnHouse to send invites.

Preferred SMTP provider: Brevo.

```text
Host: smtp-relay.brevo.com
Port: 587
Encryption: STARTTLS / TLS
Username: Brevo SMTP login
Password: Brevo SMTP key
From email: verified sender email
From name: Azzam Gold
```

Check dashboard first:

```text
Organization / Settings / Email / SMTP
```

If no SMTP form exists, inspect VPS config under `/opt/learnhouse` and set matching SMTP variables if LearnHouse exposes them.

- [ ] Sender email verified in Brevo
- [ ] SMTP key generated and saved in vault
- [ ] Test invite sent to internal inbox
- [ ] Invite link opens signup/login correctly

---

## 6. Go-live Sign-off

- [ ] `qg-lms-checklist.md` completed
- [ ] Provision SOP dry-run completed
- [ ] Brevo `access_ready` template includes `https://learn.azzamedu.com/login`
- [ ] Bot `LEARNHOUSE_URL` updated
- [ ] Refund/revoke path tested once with a test user

**Signed:** _______________ **Date:** _______________
