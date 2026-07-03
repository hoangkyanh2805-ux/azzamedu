# Lead Magnet Blueprint — Alpha Elite Gameplan

## Purpose
Plan, produce, and distribute **Tier 1: Free Alpha Elite Gameplan** — the lead magnet built around the **2% Rule operating framework**. Uses `marketingskills/lead-magnets` mechanics.

## When to use
Writing PDF, opt-in copy, Brevo Email 0, thank-you page.

**Naming:** Public name = **Alpha Elite Gameplan** · Core mechanism = **2% Rule framework**

---

## Asset overview

| Field | Value |
|-------|-------|
| **Name** | Alpha Elite Gameplan |
| **Subtitle** | The 2% Rule operating framework for structured, non-emotional trading |
| **Format** | PDF primary · Notion mirror optional |
| **Length** | 12–20 pages · ~15 min read |
| **Buyer stage** | Problem Aware → Solution Curious |
| **JTBD** | "I need one risk rule I can actually follow before I pay for anything" |
| **Next step** | Apprentice Operating Course |

---

## Type selection (lead-magnets skill)

| Type | Fit | Selected |
|------|-----|----------|
| Framework / guide | Owns the 2% mechanism | ✓ Primary |
| Checklist | Daily ops printable | ✓ Core |
| Template | Trading journal | ✓ Appendix |
| Calculator | Position size | Phase 2 web tool |
| Mini-course | Too deep for free | → Apprentice paid |

**Decision:** Single-mechanism framework + checklist. One job: teach **risk discipline**, not market calls.

---

## Content outline

### Cover
- **Title:** Alpha Elite Gameplan
- **Subtitle:** The 2% Rule operating framework — education only, not investment advice or profit promises
- Logo · short disclaimer

### §1 — Why emotion breaks accounts (2 pp)
- 5 signs of emotional trading
- 10-point self-audit (yes/no)
- **Banned:** implied profit from "fixing" behavior

### §2 — Signal groups vs operating systems (2 pp)
- Contrast table: alerts vs SOP / risk / review cadence
- Alpha Elite positioning (premium, not hype)
- **Key line:** "We sell the system you run — not the excitement you chase."

### §3 — The 2% rule explained (4 pp)
- Definition: max risk per trade as % of equity (educational)
- Position sizing walkthrough (hypothetical numbers)
- Pre-trade checklist (printable)
- **Required:** "Illustrative only. Past examples do not predict future results."

### §4 — 7-day operating sprint (3 pp)
- Day 1–7 micro-actions: journal, review, rule adherence
- Automation intro: support tool, not passive income
- **Banned:** "bot earns while you sleep"

### §5 — What comes next (2 pp)
- Path: Gameplan → Apprentice → VIP
- FAQ (compliance-safe)
- CTA: Apprentice Operating Course

### Appendix
- Journal template (PDF fillable or Sheet link)
- Full risk disclaimer
- Support contact

---

## Gating

| Field | Required |
|-------|----------|
| Email | ✓ |
| First name | ✓ |
| Experience level | Optional (segmentation) |
| Phone | ✗ MVP |

**Form copy (premium tone):**
> Get the Alpha Elite Gameplan — built on the 2% rule for risk discipline and daily operating habits. No hype. No signal spam. Delivered instantly.

---

## Delivery flow

```text
Landing CTA → Elementor form → Brevo list `gameplan-leads`
    → Email 0: PDF link (instant)
    → Thank-you `/gameplan-thank-you`
    → 7-day nurture (`docs/brevo_email_sequence.md`)
```

---

## File specs

| Spec | Value |
|------|-------|
| Filename | `Alpha-Elite-Gameplan-v1.pdf` |
| Max size | 5 MB |
| Design | Minimal, premium typography — no neon / Lambo imagery |
| Version | Track in `sales/assets/` |

---

## Promotion (MVP)

| Channel | Hook (anti-hype) |
|---------|------------------|
| Organic | "One rule before your next trade" — not "free signals" |
| YouTube | Description link to Gameplan |
| Blog | Content upgrade inline |

---

## Metrics

| Metric | MVP target |
|--------|------------|
| Landing → opt-in | 25–35% |
| Email 0 open | ≥ 50% |
| Click to Apprentice (D5–7) | ≥ 8% |
| Lead → paid (30d) | 3–8% |

---

## Compliance checklist

- [ ] No guaranteed profit / risk-free / passive bot language
- [ ] Disclaimer on cover + appendix
- [ ] No P&L screenshots as promise
- [ ] "Trade ideas" only as education if mentioned
- [ ] Reviewed against `docs/compliance_guardrails.md`

---

## Acceptance criteria

- [ ] PDF delivers one clear mechanism (2% rule)
- [ ] Reader understands Alpha Elite ≠ signal group
- [ ] End-to-end opt-in tested
- [ ] CTA points to Apprentice only (not VIP on day 0)
