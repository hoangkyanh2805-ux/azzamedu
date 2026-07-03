# QA Gates — Alpha Elite Agent OS

> Quality gates between agent outputs and human publish approval.

---

## Gate flow

```text
Producer → QG-COMP (required) → QG-WEB (if HTML/page) → QG-domain (if applicable) → Human G1
```

---

## QG-COMP — Compliance Gate

**Owner:** Compliance Agent  
**Blocks:** All customer-facing artifacts

| Check | Pass criteria |
|-------|---------------|
| NEVER table | Zero P0 prohibited terms |
| ALWAYS positioning | Approved phrase present where required |
| Disclaimer | Present per channel rules |
| Tone | Premium, anti-hype, system-first |
| Signal group | Not positioned as signal/alert product |

**Output:** `PASS` | `FAIL` + line-level notes → `.ai/audit/compliance/`

**No bypass.** Override requires human G7 + documented exception.

---

## QG-WEB — Web Quality Gate

**Owner:** Web Quality Agent  
**Blocks:** Landing, sales pages, thank-you, checkout skin

| Check | Pass criteria |
|-------|---------------|
| Lighthouse mobile Performance | ≥ 70 |
| Accessibility | ≥ 95, 0 critical axe |
| LCP | < 2.5s (lab) |
| CLS | < 0.1 |
| Form a11y | Labels, contrast, keyboard |
| SEO | Title, meta, canonical, H1 |
| Funnel | Disclaimer footer, CTA tracking |

**Reference:** `docs/web_quality_checklist.md`

---

## QG-OFFER — Offer Integrity Gate

**Owner:** Offer Architect Agent  
**Blocks:** FunnelKit wiring, sales copy CTAs

| Check | Pass criteria |
|-------|---------------|
| SKUs defined | All products in `offer_stack.md` |
| Pricing filled | No `[FILL]` placeholders |
| Ladder consistent | CTA points to correct tier |
| Bump/upsell map | Matches `funnelkit_checkout_map.md` |

---

## QG-FUNNEL — Checkout Gate

**Owner:** FunnelKit Agent  
**Blocks:** Live payments

| Check | Pass criteria |
|-------|---------------|
| Sandbox purchase | End-to-end PASS |
| Risk checkbox | Required on checkout |
| TY routing | Correct per SKU |
| Brevo tags | Fire on test order |
| Bump/upsell | Totals correct |

---

## QG-LMS — Course Gate

**Owner:** LearnHouse Agent  
**Blocks:** Course public launch

| Check | Pass criteria |
|-------|---------------|
| ≥ 3 modules | Content live |
| Video disclaimers | 15s intro each |
| Test enroll | Student completes M1 mobile |
| Provision SOP | Documented + dry run |

---

## QG-EMAIL — Email Gate

**Owner:** Brevo Email Agent  
**Blocks:** Live automation

| Check | Pass criteria |
|-------|---------------|
| 7-day sequence | All templates exist |
| Footer disclaimer | Every email |
| Test walkthrough | Full arc on test contact |
| Subject lines | Pass swap table |
| Unsubscribe | Works |

---

## Pre-launch composite gate

All must PASS before G1:

- [ ] QG-OFFER
- [ ] QG-COMP (all public artifacts)
- [ ] QG-WEB (all funnel URLs)
- [ ] QG-FUNNEL (sandbox + live micro-test)
- [ ] QG-LMS
- [ ] QG-EMAIL
- [ ] Human G1 sign-off logged

---

## Review loop limits

| Loop | Max iterations | Escalate to |
|------|----------------|-------------|
| Producer → Compliance | 3 | Human owner |
| CRO → Web Quality | 2 | Tech + Web Quality |
| Offer → FunnelKit | 2 | Offer Architect + human G0 |
