# Copywriting Audit — Alpha Elite vs TTC `500off` Mapping

> **Framework:** [marketingskills/copywriting](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copywriting) + `knowledge-asset-factory`  
> **Source mapped:** [thetradingchannel.com/500off](https://www.thetradingchannel.com/500off) (snapshot: `uploads/500off-0.md`)  
> **Guardrails:** `docs/compliance_guardrails.md`  
> **Date:** 2026-07-02  
> **Scope:** Map conversion mechanisms from TTC landing into compliant, reusable Alpha Elite copy patterns.

---

## Executive summary

TTC `500off` có conversion mechanics mạnh (story arc, mechanism naming, offer stack, CTA recurrence, risk reversal), nhưng chứa nhiều pattern vi phạm guardrails của Alpha Elite (guarantee/risk-free/passive-income/signal-adjacent framing và urgency theater).

Hướng đúng cho Alpha Elite:

- **Reuse mechanism**, không reuse claim.
- Giữ **high-conversion structure**, thay bằng copy “system-first, education-only, risk-aware”.
- Đưa mapping vào 3 page chính: `/`, `/apprentice`, `/vip`.

---

## Source inventory + confidence

| Source | Type | Confidence | Notes |
|--------|------|------------|------|
| `uploads/500off-0.md` | Raw landing transcript | High | Long-form sales page, đủ cấu trúc và claims |
| `docs/compliance_guardrails.md` | Policy | High | NEVER/ALWAYS rules rõ |
| Existing Alpha Elite web copy | Internal baseline | Medium/High | Đang có “not signal group” positioning |

**Fact vs inference rule:** Các mục “Extracted mechanisms” là fact từ source; mục “Reuse map” là inference đã lọc compliance.

---

## Extracted mechanisms from TTC 500off

### Mechanisms worth reusing (structure only)

1. Audience self-qualification questions đầu trang  
2. “Mentor story” theo arc thất bại → hệ thống → cải thiện  
3. Named framework (ví dụ `Triple Point Trading System`) để tăng memorability  
4. Simple step model (3-step/4-step) dễ tiêu hóa  
5. Offer stack breakdown theo module  
6. Payment options ladder (one-time vs installment)  
7. Repeated CTA sau mỗi khối nội dung  
8. FAQ objection handling đầy đủ (fit/time/refund/access)  
9. Risk-reversal (refund policy) để giảm friction  
10. Proof stacking (mentor proof + student feedback) kèm disclaimer

### Mechanisms to reject

1. “Near guaranteed results”  
2. “Risk-free offer” framing  
3. Passive-income promise language  
4. Lifestyle certainty claims (“full-time income from laptop”)  
5. Pressure close / guilt close  
6. Fake scarcity / repetitive warning blocks

---

## Reuse map for Alpha Elite

## `/` Homepage

**Keep/adapt from TTC**
- Self-qualification block (“Bạn có đang...?”)  
- Named mechanism reinforcement (`2% Rule Operating Protocol`)  
- CTA recurrence per major section  
- Objection-aware FAQ

**Do not import**
- Income freedom promises  
- Guarantee rhetoric  
- Hard-pressure urgency

**Copy implementation note**
- Hero remains: “not signal group” + system framing  
- Mid-page add qualification checklist (3-5 bullets)  
- CTA object format only: `Get The 2% Rule Gameplan`

## `/apprentice`

**Keep/adapt from TTC**
- Step model for process clarity  
- Value stack by outcomes (not feature dump)  
- Payment option explanation  
- Refund terms clarity (if policy approved)

**Do not import**
- “This is last course you need” absolutes  
- Profit trajectory promises

**Copy implementation note**
- Curriculum: each module = one behavior outcome  
- Pricing block: transparent, plain-language, no inflated fake anchors

## `/vip`

**Keep/adapt from TTC**
- “Choice architecture” (old behavior vs structured desk workflow)  
- Mentorship/support positioning  
- Proof via process metrics and behavior shifts

**Do not import**
- PnL brag testimonials as primary proof  
- Scarcity warnings without real constraints

**Copy implementation note**
- CTA specific: `Start VIP Private Desk`  
- Always include risk and education disclaimer near action

---

## Red-flag phrases and patterns (ban list)

- Guaranteed profit / sure returns / fixed returns  
- Risk-free trading / risk-free offer  
- Passive income from bot  
- 99% win rate certainty transfer  
- Free VIP signals / alert channel positioning  
- Fake countdown / fake “limited seats”  
- Guilt-based pressure closes

Mapped directly to `docs/compliance_guardrails.md` NEVER table.

---

## New audit scorecard (use for future copy reviews)

| Dimension | Pass criteria |
|----------|---------------|
| Compliance Integrity | No NEVER terms; disclaimers present |
| Positioning Purity | “Operating system, not signal group” consistent |
| Mechanism Clarity | Named framework + step model clear |
| CTA Specificity | `[Action] + [What they get]` on all primary CTAs |
| Proof Quality | Process-proof > profit-proof |
| Objection Coverage | FAQ covers fit/time/risk/refund/support |
| Offer Transparency | Includes, terms, and payment options are clear |
| Tone Control | Calm premium tone, no hype theatrics |

---

## Priority actions

### P0 (block launch)

- Enforce regex gate for banned claims in landing/checkout/email copy  
- Keep short and full risk disclaimers at required locations

### P1 (before traffic)

- Standardize one named mechanism across `/`, `/apprentice`, `/vip`  
- Rewrite proof blocks to process-first, compliance-safe evidence  
- Align CTA object labels across all pages and thank-you flows  
- Add objection-led FAQ to VIP page

### P2 (optimization)

- Add self-qualification module to homepage  
- A/B test soft choice architecture section  
- Build microcopy rotation set to avoid repetitive “education only”

---

## Recommended implementation files

- `sales/assets/landing-copy.md` — final page copy blocks  
- `web/wordpress/elementor-implementation-map.md` — section + CTA routing  
- `.ai/agents/funnelkit-agent.md` — checkout copy contract  
- `.ai/audit/compliance/*.md` — PASS/FAIL logs

---

## Review workflow

```text
Map source patterns → classify keep/adapt/reject → draft page copy →
compliance scan → copy audit scorecard → publish
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-07-02 | Added TTC 500off mechanism mapping and Alpha Elite compliance-safe reuse plan |
