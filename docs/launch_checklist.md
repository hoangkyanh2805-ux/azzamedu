# Launch Checklist — Alpha Elite MVP

> Checklist end-to-end trước khi mở traffic. Đánh dấu `[x]` khi hoàn thành.

---

## Phase 0 — Foundation (Tuần 0)

### Tài liệu & governance
- [ ] `project_brief.md` reviewed by stakeholder
- [ ] `offer_stack.md` pricing filled in
- [ ] `compliance_guardrails.md` team briefing done
- [ ] `.ai/rules/compliance-trading.md` in place
- [ ] Domain DNS plan documented

### Skills & tooling
- [ ] `npx skills add coreyhaines31/marketingskills --skill lead-magnets page-cro email-sequence`
- [ ] Brevo account + domain authenticated (SPF/DKIM/DMARC)
- [ ] GA4 property + conversion events defined
- [ ] PayPal business account connected

---

## Phase 1 — Lead Magnet (Tuần 1)

### Content
- [ ] Alpha Elite Gameplan PDF v1 written
- [ ] Compliance review PASS on PDF
- [ ] PDF uploaded (WP media + Brevo)
- [ ] Optional: Notion public duplicate

### Capture
- [ ] Elementor opt-in form live on landing
- [ ] Form → Brevo list `gameplan-leads`
- [ ] Brevo Email 0 automation tested
- [ ] Thank-you page `/gameplan-thank-you` live
- [ ] Test opt-in end-to-end (real email)

### CRO baseline
- [ ] Hero headline = compliant (see `landing_page_cro_framework.md`)
- [ ] Mobile form usable
- [ ] PageSpeed mobile ≥ 70

---

## Phase 2 — Landing & CRO (Tuần 1–2)

### Pages live
- [ ] `/` homepage funnel
- [ ] `/apprentice` sales page
- [ ] `/vip` sales page
- [ ] `/privacy-policy`
- [ ] `/terms`
- [ ] `/risk-disclaimer` (or combined legal page)
- [ ] `/refund-policy`

### CRO
- [ ] All CTAs tracked in GA4
- [ ] FAQ section complete
- [ ] Footer disclaimer all pages
- [ ] OG/social preview images
- [ ] 5-second clarity test passed (3 outsiders)

---

## Phase 3 — WooCommerce + FunnelKit (Tuần 2)

### Products
- [ ] SKU AE-APP-001 Apprentice created
- [ ] SKU AE-VIP-MON / AE-VIP-YR created
- [ ] Product descriptions compliance-reviewed
- [ ] Product images/icons

### FunnelKit
- [ ] Custom checkout replaces default
- [ ] Order bump on Apprentice checkout
- [ ] Order bump on VIP checkout (DWY)
- [ ] Upsell: VIP post-Apprentice
- [ ] Thank-you pages per product
- [ ] PayPal sandbox test purchase PASS
- [ ] PayPal live test purchase PASS (small amount)
- [ ] Checkout risk checkbox enabled

### Integrations
- [ ] WooCommerce → Brevo tags on purchase
- [ ] Admin order notification email/Slack

---

## Phase 4 — LearnHouse LMS (Tuần 2)

### Infrastructure
- [ ] VPS provisioned
- [ ] `learnhouse setup` completed
- [ ] SSL active on subdomain
- [ ] `learnhouse doctor` all green
- [ ] Backup cron scheduled

### Content
- [ ] Organization branded
- [ ] Apprentice course ≥ 3 modules published
- [ ] YouTube unlisted videos embedded
- [ ] Video disclaimers recorded
- [ ] Test student account can complete Module 1

### Ops SOP
- [ ] `playbook/ops/learnhouse-provision-sop.md` team trained
- [ ] Manual provision tested with test order
- [ ] Brevo `access_ready` email template live

---

## Phase 5 — Email Nurture (Tuần 2)

### Brevo automations
- [ ] Sequence 1: Gameplan Day 0–14
- [ ] Sequence 2: Apprentice onboarding
- [ ] Sequence 3: VIP onboarding
- [ ] Compliance footer all templates
- [ ] Unsubscribe link works
- [ ] Test walkthrough full Sequence 1

---

## Phase 6 — Telegram (Tuần 2–3)

- [ ] VIP Telegram group created (private)
- [ ] Pinned message: rules + disclaimer
- [ ] Admin mod guidelines documented
- [ ] Username collection form (VIP TY page or Google Form)
- [ ] Manual add SOP tested
- [ ] Welcome message template ready

---

## Phase 7 — Pre-launch QA (Tuần 3)

### Full funnel test (fresh email)

```text
Opt-in Gameplan
    → Receive Email 0
    → Click Apprentice CTA
    → Complete checkout (sandbox/real)
    → Receive TY page
    → Admin provision LearnHouse (<24h)
    → Receive access email
    → Login + watch Module 1
    → (VIP path) Submit Telegram → added <24h
```

- [ ] Full test documented with screenshots in `.ai/audit/launch-qa-YYYY-MM-DD.md`

### Compliance final pass
- [ ] All public URLs scanned for prohibited terms
- [ ] Checkout + emails + PDF + course PASS
- [ ] Telegram pin PASS

### Performance
- [ ] Landing LCP < 2.5s mobile
- [ ] LearnHouse video playback mobile OK
- [ ] No broken links (Screaming Frog or manual)

---

## Phase 8 — Launch (Go-live)

### Soft launch
- [ ] Invite 10–20 warm contacts
- [ ] Monitor opt-in rate 48h
- [ ] Monitor first purchases
- [ ] Fix P0 bugs within 4h

### Public launch
- [ ] Organic posts scheduled (UTM tagged)
- [ ] Support inbox monitored
- [ ] Daily metrics dashboard (sheet or Brevo)

---

## Post-launch Week 1

| Day | Task |
|-----|------|
| D+1 | Review opt-in rate, email deliverability |
| D+3 | Review provision SLA, customer feedback |
| D+7 | CRO review: drop-off points |
| D+7 | First weekly newsletter sent |

### Metrics to log

| Metric | Actual | Target |
|--------|--------|--------|
| Opt-in rate | | ≥ 30% |
| Email 0 open | | ≥ 50% |
| Apprentice sales (week 1) | | baseline |
| Provision SLA | | < 24h |
| Refunds | | < 3% |

---

## Defer list (explicitly NOT launch blockers)

- [ ] Crypto auto-checkout
- [ ] LearnHouse API auto-provision
- [ ] Inner Circle application flow
- [ ] Abandoned cart recovery
- [ ] Paid ads scale
- [ ] A/B testing infrastructure

---

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Project owner | | | |
| Compliance review | | | |
| Technical (WP/LMS) | | | |
| Ops (provision) | | | |

---

## Emergency rollback

Nếu P0 compliance issue sau launch:
1. Unpublish affected page / pause ads
2. Fix copy within 4h
3. Re-run compliance review
4. Post correction if needed (email/Telegram)
5. Log incident in `.ai/audit/`

---

*Cập nhật checklist sau mỗi launch phase. Version 1.0 — MVP.*
