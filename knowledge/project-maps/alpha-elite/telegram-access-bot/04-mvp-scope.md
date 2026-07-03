# 4 — MVP Scope: Telegram Access Bot

## MVP definition

**Goal:** Replace ad-hoc DMs and spreadsheet chaos with a single bot + ops queue that supports manual payment confirmation, LearnHouse provisioning tracking, and VIP Telegram approval — compliant copy only.

**Timeline fit:** Sprint after WordPress checkout live (see `docs/sprint-roadmap.md`).

---

## In scope (P0 — ship first)

### Bot (Python)

- [ ] `/start` — welcome, risk disclaimer, main menu keyboard
- [ ] `/offers` — inline catalog → URLs (`05-offer-menu-map.md`)
- [ ] `/pay` — PayPal + crypto instructions + how to submit proof
- [ ] `/status` — lookup by email (+ optional order ID)
- [ ] `/support` — forward message to admin chat + ticket ID
- [ ] `/onboard` — tier checklist (Gameplan / Apprentice / VIP)
- [ ] Payment proof upload (photo/text) → creates queue row
- [ ] VIP: collect `@username` → queue for admin

### Admin

- [ ] Admin Telegram chat ID — notifications only
- [ ] `/admin pending` — list open provisions
- [ ] `/admin confirm <id>` — mark payment verified
- [ ] `/admin provisioned <id>` — mark LH + optional TG done
- [ ] Google Sheets **or** Supabase table (pick one for MVP)

### Integrations (manual)

- [ ] Deep links to LearnHouse login URL (config)
- [ ] Deep links to WP checkout per SKU
- [ ] No WooCommerce webhook in P0

---

## P1 (after P0 stable)

- [ ] Telegram Mini App — user dashboard (status timeline)
- [ ] Brevo tag sync on status change (optional script)
- [ ] Quant application form link + status
- [ ] EN/VI message templates toggle

---

## P2 (defer)

- [ ] WooCommerce order webhook (`11-future-webhook-plan.md`)
- [ ] Auto LearnHouse user create via API
- [ ] Crypto payment verifier API
- [ ] In-bot Stripe / Telegram Payments
- [ ] Inner Circle application workflow

---

## Datastore decision

| Option | Pros | Cons | MVP pick |
|--------|------|------|----------|
| **Google Sheets** | Zero infra, ops-friendly | Rate limits, no strong typing | ✅ Fastest MVP |
| **Supabase** | Real DB, auth, future webhooks | Setup time | ✅ If dev capacity exists |

**Recommendation:** Start Sheets for ≤50 members/month; migrate to Supabase when webhook phase starts.

---

## Suggested repo layout (when coding)

```text
telegram-bot/
├── README.md
├── requirements.txt
├── config.example.yaml      # no secrets in git
├── bot/
│   ├── main.py
│   ├── handlers/
│   ├── keyboards/
│   ├── templates/           # message copy — compliance reviewed
│   └── services/
│       ├── sheets.py        # or supabase.py
│       └── provision.py
└── miniapp/                 # P1 static or FastAPI
    └── index.html
```

---

## Out of scope (explicit)

- Signal broadcasting
- Trade idea generation
- Portfolio tracking
- Replacing LearnHouse or WooCommerce
- Public unlisted VIP group links in bot

---

## Definition of done (MVP)

1. Test user completes: offers → pay instructions → submit proof → admin confirms → status shows `access_active`
2. VIP test: username submitted → admin approves → user receives invite instructions
3. All templates in `10-compliance-guardrails.md` checklist PASS
4. Ops runbook linked from `07-admin-workflow.md` followed in dry run
