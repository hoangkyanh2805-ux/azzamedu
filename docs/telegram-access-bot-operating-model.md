# Telegram Access Bot — Agent Operating Model

> **Designed via:** `agent-os-designer`  
> **Knowledge base:** `knowledge/project-maps/alpha-elite/telegram-access-bot/`  
> **Positioning:** Member access, onboarding, support, digital delivery — **not** a signal spam bot.

---

## 1. Current state summary

| Layer | Status |
|-------|--------|
| Website funnel | HTML previews + Elementor specs in progress |
| WooCommerce / FunnelKit | Documented; G3 not live |
| LearnHouse provision | Human SOP (`playbook/ops/learnhouse-provision-sop.md`) |
| Telegram VIP add | Human SOP (`playbook/ops/telegram-onboarding-sop.md`) |
| Telegram Access Bot | **Design complete** · code not scaffolded |
| Knowledge assets | 11 files in `telegram-access-bot/` |

**Gap:** No runtime bot, no ops queue DB, no Mini App. MVP = Python bot + Sheets/Supabase + manual admin approval.

---

## 2. System objective

```text
Goal → Observe → Plan → Act → Check → Stop → Human Approval
```

**North-star:** Paid or upgrading members get correct access (LearnHouse + VIP) within 24h, with compliant messaging and full audit trail — without automating trade signals or financial advice.

---

## 3. Agent roles

| # | Agent | Contract | Responsibility |
|---|-------|----------|----------------|
| T1 | **Telegram Access** | `.ai/agents/telegram-access-agent.md` | Bot/Mini App UX, commands, templates, schema, deploy docs |
| T2 | **Telegram Admin Ops** | `.ai/agents/telegram-admin-ops-agent.md` | Provision queue, admin commands, notifications, G4/G5 handoff |
| — | Compliance (existing) | `.ai/agents/compliance-agent.md` | PASS/FAIL on all bot templates before launch |
| — | LearnHouse (existing) | `.ai/agents/learnhouse-agent.md` | LH login copy, SKU→enroll matrix |
| — | Offer Architect (existing) | `.ai/agents/offer-architect.md` | SKU/menu sync with `offer_stack.md` |
| — | FunnelKit (existing) | `.ai/agents/funnelkit-agent.md` | Checkout URLs, future WC webhooks |

**Human actors (not agents):** Admin Ops (G4/G5), Owner (G0/G1/G6), Moderators (VIP group).

---

## 4. Core functions → ownership

| # | Function | Bot runtime | Agent / human |
|---|----------|-------------|---------------|
| 1 | Auth via Telegram ID | `members.telegram_id` on `/start` | Telegram Access (schema) |
| 2 | Main menu / offers | Handlers + inline URLs | Telegram Access + Offer Architect |
| 3 | Access tier display | `/status` from `tier` + `status` | Telegram Access |
| 4 | Admin notify on apply/upgrade | `notify_admin()` | Telegram Admin Ops |
| 5 | Payment instructions | `/pay` templates | Telegram Access + Compliance |
| 6 | Manual admin approval | `/admin confirm` etc. | Telegram Admin Ops + **Human G4/G5** |
| 7 | LearnHouse instructions | Template on `lh_active` | LearnHouse + Admin Ops |
| 8 | VIP invite after approval | DM + invite link | **Human G5** only (MVP) |
| 9 | Support button | `/support` → ticket | Telegram Access |
| 10 | Source + deploy docs | `telegram-bot/` | Telegram Access |

---

## 5. Bot command flow

```text
/start
  ├─ Register telegram_id (+ optional deep link ?start=order_{id})
  ├─ Show disclaimer (compliance required)
  └─ Main menu keyboard
       │
       ├─ /offers ──► Inline catalog
       │                 ├─ Gameplan → web URL
       │                 ├─ Apprentice → checkout AE-APP-001
       │                 ├─ VIP MON/YR → checkout
       │                 ├─ Quant → /quant-desk
       │                 └─ DWY → note (VIP bump)
       │
       ├─ /status ──► Lookup email → show tier + status timeline
       │
       ├─ /pay ──► SKU select → PayPal / crypto instructions
       │              └─ Submit proof → payment_review → admin notify
       │
       ├─ /onboard ──► Tier checklist (lead / apprentice / vip)
       │
       ├─ /support ──► Free text → ticket row → admin notify
       │
       ├─ /link {email} ──► Associate email to telegram_id
       │
       └─ /legal ──► Full risk disclaimer

Admin (ADMIN_TELEGRAM_IDS only):
  /admin pending
  /admin confirm <queue_id>
  /admin reject <queue_id> <reason>
  /admin provisioned <queue_id>     → LH done (human G4 executed)
  /admin tgdone <queue_id>        → VIP added (human G5 executed)
  /admin revoke <queue_id>
```

**Mini App (P1):** Web App opened from menu button — visual status timeline + deep links (no in-app payment).

---

## 6. User journey

```text
DISCOVER          ENGAGE              PAY                 ACCESS
────────          ──────              ───                 ──────

Bio / TY link  →  /start + disclaimer
                  /offers → website checkout (preferred)
               OR /pay → manual proof
                  /link email
                  payment_review
                       │
                       ▼ (admin confirm ≤24h)
                  provisioning
                       │
              ┌────────┴────────┐
              ▼                 ▼
         LearnHouse          VIP: submit @username
         instructions         tg_pending
              │                 │
              └────────┬────────┘
                       ▼
                  /status: active
                  Open LH / VIP rules reminder
```

**Tier labels (user-facing):** Free · Apprentice · VIP · Quant · Inner Circle (waitlist)

Maps to `06-user-access-status-model.md` internal states.

---

## 7. Admin journey

```text
NOTIFICATION (bot → admin chat)
  NEW PAYMENT REVIEW | VIP USERNAME | SUPPORT #id | WC webhook (P2)

OPEN QUEUE
  Sheet tab or /admin pending

VERIFY
  WooCommerce order OR PayPal/crypto proof

CONFIRM
  /admin confirm → payment_confirmed

PROVISION (human G4)
  LearnHouse SOP → /admin provisioned

VIP (human G5)
  Collect @username → add to group → /admin tgdone

AUDIT
  Order note + queue row + optional .ai/audit/approvals/
```

---

## 8. Permission model

| Action | Bot (automated) | Agent may advise | Human gate |
|--------|-----------------|----------------|------------|
| Send disclaimer templates | ✅ | Telegram Access | — |
| Show offer URLs | ✅ | Offer Architect | G0 prices |
| Store telegram_id + email | ✅ | — | — |
| Notify admin | ✅ | — | — |
| Confirm payment | ❌ | Admin Ops | Admin command |
| Create LearnHouse user | ❌ | LearnHouse | **G4** |
| Add to VIP Telegram | ❌ | Admin Ops | **G5** |
| Send VIP invite link | ❌ | — | **G5** |
| Broadcast trade ideas | ❌ **FORBIDDEN** | — | — |
| Change pricing in bot | ❌ | Offer Architect | **G0** |
| Deploy bot to production | ❌ | Telegram Access | **G1** |

Full matrix: `docs/permission-matrix.md` (Telegram section).

---

## 9. Stop conditions

| ID | Condition | Response |
|----|-----------|----------|
| TB-S1 | Template contains signal/profit/guarantee language | STOP → Compliance |
| TB-S2 | Auto-add VIP without G5 | STOP → Admin Ops |
| TB-S3 | Bot broadcast to all users (marketing blast) | STOP → Owner |
| TB-S4 | Payment confirm without verification evidence | STOP → Admin |
| TB-S5 | LearnHouse credentials in repo | STOP → use env |
| TB-S6 | User requests signal features in bot | STOP → escalate G7 |

Extends: `.ai/rules/stop-conditions.md`

---

## 10. Human approval gates (Telegram)

| Gate | Trigger | Blocks |
|------|---------|--------|
| **G0** | Offer prices in `/pay` and menu | Wrong amounts |
| **G1** | Bot go-live (production token) | Public bot |
| **G4** | LearnHouse enroll | `lh_active` claim |
| **G5** | VIP Telegram add | `access_active_vip` |
| **G6** | PayPal/crypto instructions live | `/pay` content |
| **G7** | Compliance incident | All bot messages |

New sub-evidence: `.ai/audit/approvals/YYYY-MM-DD-telegram-bot-launch.md`

---

## 11. Database schema (MVP)

See `telegram-bot/docs/DATABASE.md` for full DDL.

**Core tables:** `members`, `provision_queue`, `support_tickets`, `audit_log`

**Member tier enum:** `free` | `apprentice` | `vip` | `quant` | `inner_circle`

**Status enum:** See `06-user-access-status-model.md`

---

## 12. Folder structure

```text
telegram-bot/                    # Runtime (Python)
├── README.md                    # Quick start + deploy pointer
├── requirements.txt
├── config.example.yaml
├── docs/
│   ├── DATABASE.md
│   └── DEPLOYMENT.md
├── bot/
│   ├── main.py
│   ├── config.py
│   ├── handlers/
│   ├── keyboards/
│   ├── templates/               # Compliance-reviewed copy
│   └── services/
│       ├── db.py                # Supabase or sheets adapter
│       ├── notify.py
│       └── compliance.py
└── miniapp/                     # P1
    └── index.html

knowledge/project-maps/alpha-elite/telegram-access-bot/  # Design truth
docs/telegram-access-bot-operating-model.md              # This file
.ai/agents/telegram-access-agent.md
.ai/agents/telegram-admin-ops-agent.md
.ai/commands/telegram-provision.md
playbook/ops/telegram-onboarding-sop.md                  # VIP human SOP
```

---

## 13. MVP manual process

1. User pays on website **or** submits manual proof in bot  
2. Admin verifies payment (WC or manual)  
3. Admin runs LearnHouse SOP (G4)  
4. Bot sends LH instructions (`/admin provisioned`)  
5. VIP: user sends @username → admin adds group (G5) → `/admin tgdone`  
6. Bot updates `/status`  

**SLA:** ≤24h · No WooCommerce webhook in MVP.

---

## 14. Future WooCommerce webhook path

Phase P2 — full spec: `telegram-access-bot/11-future-webhook-plan.md`

```text
WC order.completed → webhook service → update members + notify admin
User links telegram via ?start=order_{id}
Optional: LearnHouse API auto-enroll
VIP Telegram remains G5 until policy changes
```

---

## 15. Compliance (non-negotiable)

- Every `/start` shows short risk disclaimer  
- `/offers` and `/pay` use education framing only  
- No trade alerts, win rates, or profit promises  
- VIP = accountability desk, not signal channel  
- Full rules: `telegram-access-bot/10-compliance-guardrails.md`

---

## 16. Multi-agent workflow (build bot)

```text
Offer Architect → sync SKUs/menu
       ↓
Telegram Access Agent → handlers + templates + schema + deploy docs
       ↓
Compliance Agent → PASS all templates
       ↓
Telegram Admin Ops Agent → admin commands + queue SOP
       ↓
Human G6 (payment text) + G0 (prices) + G1 (bot launch)
       ↓
Dry run: test order → G4 → G5 → /status active
```

---

## 17. Acceptance criteria

- [ ] All 10 core functions mapped to handler + owner  
- [ ] Schema documented; no secrets in git  
- [ ] Admin cannot `tgdone` without G5 checklist  
- [ ] Compliance PASS on `bot/templates/*.md`  
- [ ] Deploy doc covers systemd/Docker + env vars  
- [ ] Webhook deferred; manual path tested once  
- [ ] Agent contracts + command in `.ai/`  
- [ ] Not positioned as signal bot in any template  

---

## 18. Related files

| Doc | Path |
|-----|------|
| Knowledge pack index | `knowledge/project-maps/alpha-elite/telegram-access-bot/README.md` |
| Deploy | `telegram-bot/docs/DEPLOYMENT.md` |
| Provision command | `.ai/commands/telegram-provision.md` |
| Global agent OS | `docs/agent-loop-operating-model.md` |
