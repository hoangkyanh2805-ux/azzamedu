# MVP Launch Checklist — Alpha Elite

> **Kickstart artifact #9** · Minimum checks before opening traffic.  
> Extended version: `launch_checklist.md` · Agent command: `.ai/commands/pre-launch.md`

---

## Pre-flight (all must pass)

### Ground truth
- [ ] `project-mission.md` agreed by owner
- [ ] Pricing filled — no `[FILL]` on launch SKUs (`offer_stack.md`)
- [ ] Domain + SSL live on WordPress
- [ ] Brevo SPF/DKIM/DMARC verified
- [ ] PayPal sandbox **and** live micro-test completed (G6)

### Lead path (Path A)
- [ ] Alpha Elite Gameplan PDF uploaded
- [ ] Compliance PASS on PDF (`risk-compliance-checklist.md`)
- [ ] Homepage opt-in → Brevo list `gameplan-leads`
- [ ] Email 0 delivers PDF in <5 min (test inbox)
- [ ] 7-day automation walkthrough on test contact
- [ ] `/gameplan-thank-you` works

### Landing quality
- [ ] `web_quality_checklist.md` PASS on `/`
- [ ] Disclaimer in footer (all public pages)
- [ ] Mobile form usable (≤3 fields)
- [ ] GA4 `generate_lead` fires

### Paid path (Path B — Apprentice)
- [ ] `/apprentice` live + Compliance PASS
- [ ] `AE-APP-001` checkout completes (FunnelKit)
- [ ] Risk checkbox on checkout required
- [ ] TY page shows 24h access expectation
- [ ] Brevo tag `purchased_apprentice` on test order
- [ ] Provision SOP dry run ≤24h (`playbook/ops/learnhouse-provision-sop.md`)

### LMS
- [ ] LearnHouse HTTPS + `learnhouse doctor` OK
- [ ] Modules 1–3 published, videos play mobile
- [ ] Video 15s disclaimer on each lesson

### VIP (if launching in same release)
- [ ] VIP SKU + checkout tested
- [ ] Telegram pinned message Compliance PASS
- [ ] Username collection on VIP TY page
- [ ] Telegram add SOP tested

### Legal
- [ ] Privacy, terms, risk disclaimer, refund policy linked in footer

### Human gates logged
- [ ] G0 pricing approved
- [ ] G1 publish approved — `.ai/audit/approvals/`
- [ ] G3 checkout live approved
- [ ] G6 payment approved

---

## Soft launch (recommended)

- [ ] 10–20 warm contacts invited
- [ ] Monitor 48h: opt-in rate, Email 0 opens, errors
- [ ] Fix P0 within 4h

## Public launch

- [ ] UTM links on all campaigns
- [ ] Ops inbox monitored
- [ ] Daily metrics sheet started

---

## Definition of done

```text
Stranger → opt-in → Gameplan → nurture → buy Apprentice → LearnHouse M1 within 24h
```

Optional: VIP upsell + Telegram within 24h of @username.

---

## Rollback

If P0 compliance issue after launch:
1. Unpublish affected page / pause Brevo automation  
2. Fix + re-run `risk-compliance-checklist.md`  
3. Log `.ai/audit/escalations/`  
4. Correction post if needed (G7)
