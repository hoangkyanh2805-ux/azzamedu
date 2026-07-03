# LearnHouse — Alpha Elite LMS

Self-hosted course delivery for **Apprentice Operating Course** and **VIP Resource Library**.

| System | Role |
|--------|------|
| WooCommerce | Payment + order truth |
| LearnHouse | Course delivery, progress |
| YouTube Unlisted | Video hosting (embed only) |
| Brevo | `access_ready` email |
| Admin | Manual enroll ≤ 24h (MVP) |

**Customer-facing language:** English (Canada + EU market standard per `docs/offer_stack.md`).

---

## Repo layout

```text
web/learnhouse/
├── README.md                    # This file
├── deploy-guide.md              # VPS + CLI setup
├── admin-setup-checklist.md     # Org, groups, courses in LH UI
├── qg-lms-checklist.md          # Pre-launch quality gate
└── content/
    ├── course-manifest.md       # Full course index
    ├── apprentice-operating-course/
    │   ├── m01-operating-mindset.md
    │   ├── m02-2pct-rule.md
    │   ├── m03-daily-weekly-sops.md
    │   ├── m04-automation-support.md
    │   └── m05-path-to-vip.md
    ├── worksheets/              # Downloadable SOP templates
    └── vip-resource-library/    # VIP-only section structure
```

---

## Quick start (ops)

### Local test (Windows — no VPS yet)

1. **One-time:** Docker Desktop + WSL2 → see `local-test-guide.md`
2. Run `.\scripts\local-setup.ps1` from `web/learnhouse/`
3. Open http://localhost:8080

### Production VPS

1. **Deploy** — follow `deploy-guide.md` → `learn.hoa-homes.com` (or your subdomain)
2. **Admin** — follow `admin-setup-checklist.md` (org, groups, courses)
3. **Content** — paste lessons from `content/` into LearnHouse lesson editor
4. **Videos** — upload unlisted YouTube, embed per lesson
5. **Test** — create test student, complete M1 on mobile
6. **Provision** — `playbook/ops/learnhouse-provision-sop.md`

---

## SKU → access

| SKU | Group | Courses |
|-----|-------|---------|
| AE-APP-001 | apprentice-students | Apprentice Operating Course |
| AE-VIP-MON/YR | vip-members | Apprentice + VIP Resource Library |
| AE-QNT-001 | quant-desk | All + Quant (phase 2) |
| AE-DWY-001 | — | No LMS change (setup session only) |

---

## Related docs

- `docs/learnhouse_lms_map.md` — course map (project truth)
- `playbook/ops/learnhouse-provision-sop.md` — human provision SOP
- `telegram-bot/docs/learnhouse-delivery-flow.md` — bot delivery after G4
- `web/wordpress/course-curriculum-copy.md` — landing curriculum copy source

---

## MVP acceptance

- [ ] `npx learnhouse doctor` passes on VPS
- [ ] HTTPS live at `https://learn.[domain].com`
- [ ] M1–M3 lessons published with unlisted embeds
- [ ] Test student completes M1 on mobile
- [ ] Manual provision dry-run < 24h SLA
- [ ] `qg-lms-checklist.md` signed off
