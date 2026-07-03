# User Journey — Alpha Elite

> **Kickstart artifact #4** · Persona paths from awareness to ascension.

---

## Personas

| Persona | Goal | Entry | Success signal |
|---------|------|-------|----------------|
| **Curious trader** | Stop emotional XAUUSD/gold trades | Gameplan opt-in | Completes 7-day sprint in PDF |
| **Apprentice** | Learn operating SOPs | Paid course | Module 1 done in 7 days |
| **VIP operator** | Daily accountability + ideas | VIP membership | Active in Telegram + SOP use |
| **Desk member** | Quant layer education | Quant Desk | Engaged in desk channel |
| **Inner Circle** | High-touch cohort | Application | Invited seat (phase 2) |

---

## Journey map — primary funnel

```text
AWARENESS          CONSIDERATION         CONVERSION           RETENTION            ASCENSION
─────────          ─────────────         ──────────           ─────────            ─────────

Social / search    Landing page          Apprentice           VIP Telegram         Quant Desk
Referral      →    Gameplan opt-in   →   checkout        →    + SOP library    →   / Inner Circle
Content            7-day Brevo           LearnHouse           Weekly rhythm        DWY setup
                   Email nurture         Module progress      Accountability
```

---

## Stage 1 — Awareness → Lead

| Step | Touchpoint | User action | System | Emotion / job |
|------|------------|-------------|--------|---------------|
| 1 | Ad / post / referral | Click link | UTM tracked | “I need structure” |
| 2 | Homepage | Read positioning | Elementor | “Not another signal group” |
| 3 | Homepage | Opt in | Form → Brevo | “Give me the gameplan” |
| 4 | Thank-you | Check email note | `/gameplan-thank-you` | Expectation set |
| 5 | Inbox | Download PDF | Brevo Email 0 | Quick win — 2% rule |

**Compliance moment:** Hero + PDF disclaim risk; no profit promise.

---

## Stage 2 — Nurture → Apprentice

| Day | Email | Intent | CTA |
|-----|-------|--------|-----|
| 0 | Gameplan delivery | Deliver value | Read PDF |
| 1–2 | Emotional trading / not signal group | Educate + differentiate | PDF sections |
| 3–4 | 2% rule + operating sprint | Build habit | Checklists |
| 5–7 | Apprentice pitch + FAQ | Convert | `/apprentice` |

| Step | Touchpoint | User action | System |
|------|------------|-------------|--------|
| 6 | `/apprentice` | Read offer | Sales page |
| 7 | Checkout | Pay | FunnelKit + PayPal |
| 8 | Upsell | Accept/decline VIP | FunnelKit |
| 9 | Thank-you | Read next steps | TY page |

---

## Stage 3 — Onboard → Learn

| Step | Actor | Action | SLA |
|------|-------|--------|-----|
| 10 | Admin | Create LearnHouse user | ≤24h |
| 11 | Brevo | `access_ready` email | ≤24h |
| 12 | User | Login + Module 1 | 7d target |
| 13 | Brevo | Onboarding emails A1–A4 | Days 1–7 |

**Pain if broken:** Buyer paid but no access → refund risk.

---

## Stage 4 — VIP upgrade

| Step | Touchpoint | Action | System |
|------|------------|--------|--------|
| 14 | Upsell or email | Purchase VIP | FunnelKit |
| 15 | TY page | Submit @telegram | Form |
| 16 | Admin | Add to VIP group | Telegram |
| 17 | User | Read pinned rules | Telegram | 
| 18 | LearnHouse | VIP resource library | LMS |

**VIP value:** Structured XAUUSD trade ideas (education), SOPs, bot support docs, accountability—not guaranteed calls.

---

## Stage 5 — Ascension

| Path | Trigger | Action |
|------|---------|--------|
| **Quant Desk** | VIP engaged 30d+ | Upgrade email → checkout `AE-QNT-001` |
| **Inner Circle** | Application approved | Manual invite (phase 2) |
| **DWY Setup** | VIP checkout bump | Book setup session |

---

## Journey failure modes

| Failure | Detection | Fix |
|---------|-----------|-----|
| No Email 0 | Brevo log | Fix automation |
| Provision >24h | Order age | Ops escalation |
| Wrong course enrolled | User ticket | Admin re-enroll |
| Telegram not added | Form missing @ | Resend V0 email |
| Compliance slip in VIP chat | Mod report | G7 incident |

---

## MVP journey test script

1. New email → opt in → receive Gameplan  
2. Wait/trigger Day 5 email → click Apprentice  
3. Sandbox purchase → receive TY  
4. Admin provision → login LearnHouse → play Module 1 video  
5. (Optional) VIP upsell → Telegram added  

Log: `.ai/audit/approvals/YYYY-MM-DD-journey-test.md`
