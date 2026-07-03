# Brevo Email Sequence — 7-Day Nurture

## Purpose
Post–Alpha Elite Gameplan nurture that delivers value, reinforces system-first positioning, and converts to Apprentice — without hype.

## When to use
Brevo automation setup, copywriting, compliance review.

**Source:** `marketingskills/email-sequence` · Arc: Deliver → Differentiate → Educate → Pitch → Close

---

## Lists & tags

### Lists
| List | Entry |
|------|-------|
| `gameplan-leads` | Opt-in Alpha Elite Gameplan |
| `customers-apprentice` | Purchased Apprentice |
| `customers-vip` | Purchased VIP |

### Tags
| Tag | When |
|-----|------|
| `lead_gameplan` | Form submit |
| `engaged_7d` | Opened 2+ emails in 7 days |
| `clicked_apprentice` | Clicked Apprentice CTA |
| `purchased_apprentice` | WooCommerce order |
| `purchased_vip` | WooCommerce VIP order |
| `access_ready` | LearnHouse provisioned |

---

## Sequence 1 — 7-day nurture (post opt-in)

**Entry:** Subscribe `gameplan-leads`  
**Exit:** Tag `purchased_apprentice` or `purchased_vip`  
**Goal:** Trust → Apprentice conversion

---

### Email 0 — Instant (on subscribe)

| Field | Content |
|-------|---------|
| **Subject** | `[Alpha Elite] Your Gameplan is inside — start with the 2% rule` |
| **Preview** | Risk framework + daily checklist — inside |
| **Body** | Thank you · calm tone · PDF/Notion link · "Not a signal list" one-liner |
| **CTA** | Download Gameplan |
| **Footer** | Full risk disclaimer |

---

### Day 1 — The real cost of emotional trades

| Field | Content |
|-------|---------|
| **Subject** | Five signs you're trading on emotion |
| **Body** | Pull from Gameplan §1 · self-audit prompt |
| **CTA** | Complete audit in PDF |
| **Tone** | Diagnostic, not dramatic |

---

### Day 2 — Not a signal group

| Field | Content |
|-------|---------|
| **Subject** | This is not a signal group. Here's what we build instead. |
| **Body** | Operating system vs alert chasing · SOP + 2% + support |
| **CTA** | Read Gameplan §2 |
| **Compliance** | No competitor bashing · focus on what we are |

---

### Day 3 — The 2% rule in practice

| Field | Content |
|-------|---------|
| **Subject** | How the 2% rule actually works (with numbers) |
| **Body** | Educational sizing example · hypothetical · disclaimer inline |
| **CTA** | Use pre-trade checklist from Gameplan |
| **Banned** | Win rate brags · guaranteed outcomes |

---

### Day 4 — Your first operating week

| Field | Content |
|-------|---------|
| **Subject** | Days 1–3 of the 7-day operating sprint |
| **Body** | Actionable steps from Gameplan §4 |
| **CTA** | Start Day 1 today |
| **PS** | Automation = support tool, not passive income |

---

### Day 5 — Who Apprentice is for

| Field | Content |
|-------|---------|
| **Subject** | Ready to go deeper than a PDF? |
| **Body** | Apprentice outline · who it's for / not for · calm pitch |
| **CTA** | View Apprentice Operating Course → `/apprentice` |
| **Compliance** | Education only · no profit promise |

---

### Day 6 — FAQ before you decide

| Field | Content |
|-------|---------|
| **Subject** | Common questions (risk, refunds, what VIP is not) |
| **Body** | 5 FAQs from compliance-safe list |
| **CTA** | Apprentice course page |
| **Tone** | Transparent, premium |

---

### Day 7 — Closing invitation

| Field | Content |
|-------|---------|
| **Subject** | Last note on the Gameplan — then we get quiet |
| **Body** | Respectful close · no fake scarcity · optional Apprentice CTA |
| **CTA** | Enroll in Apprentice |
| **Branch** | No click → move to `newsletter-weekly` (evergreen tips, no hype) |

---

## Sequence 2 — Apprentice onboarding (post-purchase)

| # | Timing | Subject direction |
|---|--------|-------------------|
| A0 | On `access_ready` | LearnHouse login ready |
| A1 | Day 1 | Complete Module 1 in 48h |
| A2 | Day 3 | Journal setup check-in |
| A3 | Day 5 | When VIP makes sense (soft upgrade) |
| A4 | Day 7 | Week-one support check-in |

---

## Sequence 3 — VIP onboarding (post-purchase)

| # | Timing | Subject direction |
|---|--------|-------------------|
| V0 | Instant | Welcome VIP — Telegram username form |
| V1 | After Telegram add | Read pinned rules first |
| V2 | Day 3 | VIP resource library on LearnHouse |
| V3 | Day 7 | Quant Desk overview (optional, no pressure) |

---

## Subject line rules

**Do:** Specific, calm, system language  
**Don't:** `$`, "guaranteed", "free signals", ALL CAPS urgency

---

## Compliance footer (every email)

```text
Alpha Elite provides education, trade ideas, automation support, SOPs, and community support.
Trading involves substantial risk of loss. This is not investment advice. No profit is guaranteed.
Past results do not indicate future performance. {{ unsubscribe }}
```

---

## Automation logic

```text
[Opt-in] → tag lead_gameplan → Email 0 → Days 1–7
[Woo Apprentice] → stop Sequence 1 → wait access_ready → Sequence 2
[Woo VIP] → stop upsell paths → Sequence 3
```

---

## Metrics

| Email | Open | CTR |
|-------|------|-----|
| Email 0 | ≥ 55% | ≥ 40% download |
| Day 5 pitch | ≥ 35% | ≥ 8% |
| Day 7 | ≥ 30% | ≥ 6% |

Unsubscribe < 0.5% per send.

---

## Acceptance criteria

- [ ] Exactly 7 nurture emails after Email 0 (or 8 total touches in week 1)
- [ ] Every template compliance-reviewed
- [ ] Test contact completes full arc
- [ ] WooCommerce tags stop nurture on purchase
