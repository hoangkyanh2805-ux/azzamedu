# Repo & Skill Map — Alpha Elite

## Purpose
Route external agent skills to Alpha Elite funnel workflows. Reusable across projects building WP + LMS + email stacks.

## Source inventory

| Source | URL | Confidence | Alpha Elite role |
|--------|-----|------------|------------------|
| marketingskills | github.com/coreyhaines31/marketingskills | High | CRO, copy, email, lead magnets |
| lead-magnets | `skills/lead-magnets/SKILL.md` | High | 2% Rule Gameplan structure |
| agent-skills | github.com/addyosmani/agent-skills | Medium | Agent contracts |
| web-quality-skills | github.com/addyosmani/web-quality-skills | High | Landing audit |
| awesome-agent-skills | Curated index | Medium | Discovery |

---

## Install commands

```bash
# Marketing — minimum viable set
npx skills add coreyhaines31/marketingskills \
  --skill lead-magnets page-cro copywriting email-sequence form-cro pricing-strategy

# Web quality — landing gate
npx skills add addyosmani/web-quality-skills \
  --skill web-quality-audit performance core-web-vitals accessibility seo

# Agent patterns (optional)
npx skills add addyosmani/agent-skills
```

**Local index:** `.ai/references/skills-index.md` · `.codex/skills/`

---

## marketingskills → asset map

| Skill | Alpha Elite output | Path |
|-------|-------------------|------|
| `lead-magnets` | The 2% Rule Gameplan blueprint | `docs/lead_magnet_blueprint.md` |
| `page-cro` + `form-cro` | Landing CRO framework | `docs/landing_page_cro_framework.md` |
| `copywriting` | Sales copy drafts | `sales/assets/` |
| `email-sequence` | 7-day Brevo nurture | `docs/brevo_email_sequence.md` |
| `pricing-strategy` | Offer ladder / anchoring | `docs/offer_stack.md` |
| `cro` | Funnel audit | `docs/launch_checklist.md` |
| `analytics` | GA4 events | `config/analytics-events.md` |
| `seo` | Landing meta | `docs/web_quality_checklist.md` |

### lead-magnets — extracted mechanism
1. **One magnet = one mechanism** → 2% rule only at free tier  
2. **Gating minimal** → email + name  
3. **Instant delivery** → Brevo Email 0  
4. **Measure quality** → Apprentice conversion, not raw lead volume  

---

## web-quality-skills → asset map

| Skill | Output | Path |
|-------|--------|------|
| `web-quality-audit` | Full pre-launch gate | `docs/web_quality_checklist.md` |
| `performance` | Elementor speed budget | Same |
| `core-web-vitals` | LCP/INP/CLS targets | Same |
| `accessibility` | Form + CTA WCAG | Same |
| `seo` | Meta, schema, crawl | Same |

**Trigger:** Any Elementor publish → run Landing QA agent + web quality checklist.

---

## agent-skills → agent OS map

| Pattern | Alpha Elite agent | Path |
|---------|-------------------|------|
| Structured review | Compliance Reviewer | `.ai/agents/compliance-reviewer.md` |
| Implementation guide | Funnel Builder | `.ai/agents/funnel-builder.md` |
| Quality gate | Landing QA | `.ai/agents/landing-qa.md` |
| SOP advisor | Ops Provisioner | `.ai/agents/ops-provisioner.md` |

---

## awesome-agent-skills — use as index only

Do not bulk-install. Record candidates in `knowledge/project-maps/alpha-elite/source-distillation.md`.

---

## Task → skill routing

| User / task | Invoke |
|-------------|--------|
| Plan lead magnet | `lead-magnets` + compliance rules |
| Write landing hero | `copywriting` + `page-cro` + anti-hype principle |
| Audit before launch | `web-quality-audit` + `docs/web_quality_checklist.md` |
| Email nurture | `email-sequence` + `docs/brevo_email_sequence.md` |
| Checkout setup | internal funnel map + `pricing-strategy` |
| Review trading copy | `compliance-reviewer` agent |

---

## Internal skill candidates

| Skill | Path | Priority |
|-------|------|----------|
| `alpha-elite-compliance` | `.codex/skills/alpha-elite-compliance/` | P0 |
| `funnelkit-ops` | `.codex/skills/funnelkit-ops/` | P0 |
| `learnhouse-provision` | `.codex/skills/learnhouse-provision/` | P1 |

---

## Gaps & defer

| Gap | Action |
|-----|--------|
| WooCommerce ↔ LearnHouse webhook skill | Phase 2 |
| Vietnamese copywriting skill | Human review + `copywriting` |
| FunnelKit upstream skill | Use `funnelkit-ops` internal |

---

## Acceptance criteria

- [ ] Skills installed for lead-magnets, page-cro, email-sequence, web-quality-audit
- [ ] Each of 10 core docs references source skill where applicable
- [ ] Compliance agent blocks publish on P0 violations
