# Knowledge Distillation — Alpha Elite (Source Batch)

> Pipeline: Raw Source → Insight → Principle → Framework → Project Map → Reusable Asset  
> Generated via `knowledge-asset-factory`

---

## Source inventory

| # | Source | Type | Confidence | Role in project |
|---|--------|------|------------|-------------------|
| 1 | User brief (positioning, stack, compliance) | Requirements | High | Project truth |
| 2 | `coreyhaines31/marketingskills` | GitHub skills (35+) | High | CRO, lead magnets, email, copy |
| 3 | `marketingskills/lead-magnets/SKILL.md` | Sub-skill | High | Lead magnet structure |
| 4 | `addyosmani/agent-skills` | GitHub skills | Medium | Agent loop patterns |
| 5 | `addyosmani/web-quality-skills` | GitHub skills | High | Landing quality checklist |
| 6 | `awesome-agent-skills` | Curated index | Medium | Skill discovery |
| 7 | LearnHouse docs / CLI | LMS platform | High | Course delivery |
| 8 | Existing `docs/*.md` | Prior assets | High | Baseline to refine |

---

## Key extracted insights

### Insight 1 — Positioning mechanism (not headline)
**Mechanism:** Conversion improves when you *disqualify* hype-seekers early. "Not a signal group" + "operating system" filters wrong-fit leads and reduces refund/chargeback risk.  
**Principle:** `Anti-hype qualification` — premium brands sell discipline, not dopamine.  
**Asset:** `knowledge/distilled/principles/anti-hype-qualification.md`

### Insight 2 — Lead magnet = one rule, one job
**Mechanism:** `lead-magnets` skill — match magnet to buyer stage. Problem-aware traders need a *single actionable framework* (2% rule), not a course preview.  
**Principle:** `One magnet, one mechanism` — The 2% Rule Gameplan owns risk framing; Apprentice owns execution depth.  
**Asset:** `docs/lead_magnet_blueprint.md`

### Insight 3 — Stack separation of concerns
**Mechanism:** WP sells, LearnHouse delivers, Brevo nurtures, Telegram retains — each system has one job. Manual provision acceptable at low volume.  
**Principle:** `Commerce truth ≠ LMS truth` — WooCommerce order is source of truth; LearnHouse enroll is derived state.  
**Asset:** `docs/architecture.md`, `docs/funnelkit_checkout_map.md`

### Insight 4 — Compliance as conversion asset
**Mechanism:** Trading education brands that show risk early attract serious operators and repel lawsuit-prone hype buyers.  
**Principle:** `Disclaimer is trust signal` — not legal footnote only.  
**Asset:** `docs/compliance_guardrails.md`

### Insight 5 — Web quality = CRO enabler
**Mechanism:** `web-quality-skills` — slow mobile landing kills opt-in before copy matters. LCP < 2.5s is part of funnel design.  
**Principle:** `Performance is conversion`  
**Asset:** `docs/web_quality_checklist.md`

---

## Reusable frameworks distilled

| Framework | Description | Reuse beyond Alpha Elite |
|-----------|-------------|--------------------------|
| **Operating System Funnel** | Free framework → paid course → membership → desk | Any high-ticket education/coaching |
| **Manual Provision MVP** | Pay → admin → LMS → email → community | Any self-host LMS + WP stack |
| **7-Day Nurture Arc** | Deliver → differentiate → educate → pitch → close | B2C info products |
| **Compliance Swap Table** | NEVER/ALWAYS word replacements | Any fintech/trading education |

---

## Project map — keep / improve / defer

| Item | Action |
|------|--------|
| 10 core docs | **Improve** — premium tone, 2% Rule Gameplan naming, 7-day email |
| `launch_checklist.md` | **Keep** — separate from web quality |
| `web_quality_checklist.md` | **Create** — from web-quality-skills |
| Auto LearnHouse enroll | **Defer** Phase 2 |
| Inner Circle full launch | **Defer** |
| Signal-group positioning | **Delete** everywhere |

---

## Asset → storage map

| Asset | Path | Type |
|-------|------|------|
| Project brief | `docs/project_brief.md` | Brief |
| Offer stack | `docs/offer_stack.md` | Sales |
| Repo skill map | `docs/repo_skill_map.md` | Map |
| Lead magnet blueprint | `docs/lead_magnet_blueprint.md` | Playbook |
| Landing CRO | `docs/landing_page_cro_framework.md` | Framework |
| FunnelKit map | `docs/funnelkit_checkout_map.md` | Playbook |
| LearnHouse map | `docs/learnhouse_lms_map.md` | Playbook |
| Brevo 7-day | `docs/brevo_email_sequence.md` | Template |
| Compliance | `docs/compliance_guardrails.md` | Rules |
| Web quality | `docs/web_quality_checklist.md` | Checklist |

---

## Skill candidates

| Skill | Trigger | Priority |
|-------|---------|----------|
| `alpha-elite-compliance` | Trading copy review | P0 |
| `funnelkit-ops` | Checkout/bump/upsell | P0 |
| `learnhouse-provision` | Post-purchase enroll | P1 |
| `web-quality-audit` (external) | Pre-launch landing | P0 |

---

## Acceptance criteria (batch)

- [ ] All 10 assets use premium, system-first, anti-hype voice
- [ ] Lead magnet named "The 2% Rule Gameplan" consistently
- [ ] Brevo nurture = 7 days (not 14)
- [ ] No signal-group / guaranteed profit / passive bot language
- [ ] Web quality checklist maps to Lighthouse + WCAG 2.2
- [ ] Each asset cross-references compliance guardrails

---

## Next actions

1. Fill pricing in `offer_stack.md`
2. Produce Gameplan PDF from `lead_magnet_blueprint.md`
3. Run `web_quality_checklist.md` before launch traffic
4. Install: `npx skills add coreyhaines31/marketingskills addyosmani/web-quality-skills`
