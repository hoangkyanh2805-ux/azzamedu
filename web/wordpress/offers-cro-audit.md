# Offers & CRO Audit — `web/` Folder

> **Frameworks:** [marketingskills/offers](https://github.com/coreyhaines31/marketingskills/tree/main/skills/offers) v1.0.0 · [marketingskills/cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/cro) v2.0.0  
> **Companion:** `copywriting-audit.md` · `compliance-copy-audit.md`  
> **Offer source:** `docs/offer_stack.md`  
> **Date:** 2026-07-01 (pass 2)

---

## Executive summary

| Lens | Score | Binding constraint |
|------|-------|-------------------|
| **Offer design** | ⚠️ 6/10 | Pricing unfilled · weak bonus stack on paid tiers · no real scarcity |
| **CRO — homepage** | ✅ 7.5/10 | Strong hero + opt-in; testimonials now placeholder |
| **CRO — funnel pages** | ✅ 7/10 | Single-goal LPs good; apprentice/vip need price anchors |
| **Compliance** | ✅ PASS | Offer framing avoids guarantee/scarcity traps |

**Diagnosis (offers skill):** This is not a "weak copy" problem — it's a **perceived likelihood + time-to-value** problem until pricing, real testimonials, and Gameplan PDF ship. Copy and structure are ahead of offer completeness.

---

## Part 1 — Offer audit (Value Equation)

### Brand constraint

Alpha Elite **cannot** use profit guarantees, fake scarcity, or bonus inflation (`$50K value` stacks). Risk reversal = **education clarity + process transparency**, not money-back profit promises.

### Value equation by tier

Scoring 1–10 per lever: Dream outcome · Perceived likelihood · Time delay (lower better) · Effort (lower better)

#### Tier 1 — Free Gameplan

| Lever | Score | Notes |
|-------|-------|-------|
| Dream outcome | 7 | "Stop emotional trading" — clear, compliant |
| Perceived likelihood | 6 | PDF not in repo yet; TY page sets expectation |
| Time delay | 9 | Free · email in minutes |
| Effort | 9 | Name + email only |

**Anatomy check:**

| Component | Status | Recommendation |
|-----------|--------|----------------|
| Core deliverable | ✅ | 2% rule + SOP + 7-day sprint |
| Bonus stack | ⚠️ | Add: printable checklist PDF page, journal template link in Email 0 |
| Guarantee | N/A (free) | Compliance disclaimer = trust signal |
| Scarcity | ❌ skip | Never fake countdown |
| Name | ✅ | "2% Rule Gameplan" — specific, not hype |
| Price | ✅ Free | Clear |

**Offer fix (P1):** Ship PDF asset · align Email 0 chapters with `gameplan-preview.html` chapter list.

---

#### Tier 2 — Apprentice Operating Course

| Lever | Score | Notes |
|-------|-------|-------|
| Dream outcome | 8 | "Install operating protocol" |
| Perceived likelihood | 5 | No testimonials live · pricing TBD |
| Time delay | 6 | ~14 lessons — specify "first win" (Day 1 SOP install) |
| Effort | 5 | LearnHouse + worksheets — moderate |

**Anatomy check:**

| Component | Status | Recommendation |
|-----------|--------|----------------|
| Core deliverable | ✅ | 5 modules, worksheets, LearnHouse |
| Bonus stack | ✅ | Operating Toolkit — 6 templates on `/apprentice` |
| Guarantee | ⚠️ | Use **process guarantee**: "Complete M1–M3 worksheets or we'll help you find the right tier" — NOT profit refund |
| Scarcity | ❌ | No fake seat limits |
| Name | ✅ | Apprentice Operating Course |
| Price | ✅ **$297 draft** | G0 sign-off before WooCommerce |

**Offer fix (P0 for revenue):** Fill `AE-APP-001` price in `offer_stack.md` + HTML offer cards.

**Bonus stack draft (compliant):**

```text
Core: 14 lessons · 5 modules · LearnHouse lifetime access
Bonus 1: Printable 2% sizing worksheet (PDF)
Bonus 2: Daily + weekly SOP templates
Bonus 3: Journal workflow Notion/Google Sheet template
Bonus 4: Automation support literacy checklist (M4 summary)
```

No dollar "value" claims — list deliverables only.

---

#### Tier 3 — VIP Private Desk

| Lever | Score | Notes |
|-------|-------|-------|
| Dream outcome | 8 | Private desk, accountability |
| Perceived likelihood | 5 | Mock UI labeled illustrative — good compliance, weak proof |
| Time delay | 7 | Immediate channel access after checkout |
| Effort | 6 | Requires Apprentice completion (implicit) |

**Anatomy check:**

| Component | Status | Recommendation |
|-----------|--------|----------------|
| Core deliverable | ✅ | Telegram desk, SOP library, structured ideas (edu) |
| Bonus stack | ⚠️ | DWY bump (`AE-DWY-001`) under-documented on `/vip` |
| Guarantee | N/A | Monthly cancel = natural risk reversal |
| Scarcity | ⚠️ | Only **real** limits (e.g. desk capacity) — document if true |
| Name | ✅ | VIP Private Desk / VIP Private System |
| Price | ✅ **$149/mo · $1,290/yr draft** | G0 sign-off before WooCommerce |

**Offer fix:** Highlight **annual savings %** when prices set · add "what's NOT included" row (already in comparison table ✅).

---

#### Tier 4 — Quant Desk

| Lever | Score | Notes |
|-------|-------|-------|
| Dream outcome | 7 | Ascension — quant education |
| Perceived likelihood | 6 | Application gate increases seriousness |
| Time delay | 4 | Manual review — friction by design |
| Effort | 4 | Application form + VIP tenure expectation |

**CRO note:** Application friction is appropriate for high-touch tier. Form placeholder guides compliant answers ✅.

---

### Offer anti-patterns avoided ✅

- No fake countdown / seat counters  
- No "$X value" bonus inflation  
- No profit guarantee as risk reversal  
- No course-bro "secret method" naming  

---

## Part 2 — CRO audit (by page)

### Homepage `/` — `homepage-dark-gold.html`

**Goal:** Gameplan opt-in · **Type:** Homepage

| CRO dimension | Status | Notes |
|---------------|--------|-------|
| Value prop clarity (5s) | ✅ | H1 + trimmed subhead |
| Headline | ✅ | Pain-first, differentiated |
| CTA hierarchy | ✅ | Primary Gameplan · secondary View System |
| Visual hierarchy | ✅ | Dark/gold scannable sections |
| Trust / social proof | ⚠️ | **Placeholder testimonials added** `#testimonials` — replace at G1 |
| Objection handling | ✅ | not-signal-group + FAQ + who-its-for |
| Friction | ✅ | Opt-in: name + email only |

#### Quick wins (implemented)

- [x] Trim hero subheadline (2 sentences)
- [x] Testimonials placeholder before offers ladder
- [x] Specific tier CTAs (`Start Apprentice Course`, etc.)

#### High-impact (remaining)

| Change | Impact | Effort |
|--------|--------|--------|
| Real testimonials (G1) | High | Medium |
| Pricing on offer cards | High | Low (when G0) |
| Activity strip (compliant) | Medium | Low |
| Video demo section | Medium | Medium |

#### Test ideas

| Hypothesis | Variant |
|------------|---------|
| Subhead A/B | Current trim vs. add "private XAUUSD" in sentence 1 |
| CTA above fold | Single CTA only (remove secondary) on paid traffic |
| Testimonials position | Before vs. after `who-its-for` |
| Opt-in form | Add chapter bullet preview above form |

---

### Gameplan LP `/gameplan` — `gameplan-preview.html`

**Goal:** Email capture · **Type:** Landing page

| Dimension | Status |
|---------------|--------|
| Message match | ✅ Single offer |
| Single CTA | ✅ |
| Navigation | ⚠️ Minimal — OK for ads |
| Complete argument | ✅ 5 chapters + who NOT for |

**CRO quick win:** Remove header nav on paid traffic (Elementor: landing template no menu).

---

### Thank you `/gameplan-thank-you`

**Goal:** Confirm + nurture Apprentice

| Dimension | Status |
|---------------|--------|
| Expectation setting | ✅ "sending" not "sent" |
| Next step | ✅ Soft CTA |
| Support reduction | ✅ 3 steps + FAQ |
| Spec alignment | ✅ `elementor-spec-gameplan-thank-you.md` v2.0 dark/gold |

---

### Apprentice `/apprentice`

**Goal:** Checkout `AE-APP-001`

| Dimension | Status | Fix |
|---------------|--------|-----|
| Value prop | ✅ | — |
| Price anchor | ❌ TBD | Fill price |
| Curriculum depth | ✅ | Accordion modules |
| Risk reversal | ⚠️ | Add process-focused refund policy copy at G1 |
| CTA | ✅ | Start Apprentice Course |

---

### VIP `/vip`

**Goal:** Checkout VIP SKU

| Dimension | Status |
|---------------|--------|
| Differentiation | ✅ Not alert channel |
| Plan comparison | ✅ Monthly/annual |
| Recommended plan | ✅ Annual featured |
| Mock desk disclaimer | ✅ |

**Test:** Sticky CTA copy — `Start VIP Private Desk` vs. `Run Your Private Desk`.

---

### Quant `/quant-desk`

**Goal:** Application submit

| Dimension | Status |
|---------------|--------|
| Qualification | ✅ Exclusions list |
| Form friction | ✅ Appropriate fields |
| CTA | ✅ Submit Quant Desk Application |

---

## Part 3 — Funnel CRO map

```text
Traffic
  → Homepage OR /gameplan (opt-in)     [CRO: message match, 2 fields max]
  → /gameplan-thank-you                 [CRO: nurture, no hard sell]
  → Brevo D2–7                          [CRO: one CTA per email]
  → /apprentice                         [CRO: price + bonus stack]
  → /vip                                [CRO: annual default, comparison]
  → /quant-desk                         [CRO: application quality > volume]
```

**Leak points:**

1. Email 0 not wired — users hit TY with no PDF  
2. Pricing TBD — `begin_checkout` has no price in dataLayer  
3. Placeholder testimonials — perceived likelihood capped  

---

## Part 4 — Priority action matrix

| Priority | Offers | CRO |
|----------|--------|-----|
| **P0** | G0 sign-off on draft prices | Wire Brevo Email 0 + PDF |
| **P1** | Apprentice bonus PDFs in `sales/assets/` | Replace testimonial placeholders (G1) |
| **P1** | Document DWY bump on VIP page | Add GA4 `begin_checkout` with SKU + price |
| **P2** | Process guarantee copy (legal review) | A/B hero subhead on paid traffic |
| **P2** | Real desk capacity scarcity (if true) | Activity strip section |
| **P3** | Inner Circle waitlist offer | ~~Video demo on homepage~~ → wire YouTube ID |

---

## Part 5 — Banned patterns check (offers skill)

Scanned `web/wordpress/html/` for offer-skill banned vocabulary:

| Term | Found? |
|------|--------|
| game-changing / revolutionary | ❌ No |
| secret / hidden method | ❌ No |
| limited time (fake) | ❌ No |
| worth $X / $Y value | ❌ No |
| 100% guaranteed (unqualified) | ❌ No — only negations |

**PASS**

---

## Changelog

| Date | Change |
|------|--------|
| 2026-07-01 | Draft pricing in HTML · Apprentice Operating Toolkit section |
| 2026-07-01 | Hero subhead trimmed · testimonials placeholder · TY spec v2.0 dark/gold |
