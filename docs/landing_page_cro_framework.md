# Landing Page CRO Framework — Alpha Elite

## Purpose
Conversion architecture for premium, anti-hype landing pages on WordPress/Elementor. Combines `marketingskills/page-cro` with system-first positioning.

## When to use
Building or revising `/`, `/alpha-elite`, `/apprentice`, `/vip`.

**Quality gate:** `docs/web_quality_checklist.md`

---

## North-star metrics

| Page | Primary conversion | MVP target |
|------|-------------------|------------|
| Homepage | Alpha Elite Gameplan opt-in | 25–35% |
| Apprentice | Checkout click | 8–15% of warm traffic |
| VIP | Checkout / apply | Segment-dependent |

---

## Premium design principles

1. **Calm visual hierarchy** — whitespace, restrained palette, no neon profit imagery  
2. **System language** — SOP, framework, operating, discipline  
3. **Early qualification** — repel signal-chasers in hero subhead  
4. **Risk visible** — disclaimer near first CTA builds trust with serious buyers  
5. **One primary action** — Gameplan opt-in above fold; Apprentice secondary  

---

## Homepage architecture

```text
┌──────────────────────────────────────────┐
│ Header: Logo · "Get the Gameplan" (sticky) │
├──────────────────────────────────────────┤
│ HERO: Problem → System promise → Opt-in    │
│       Micro disclaimer line                │
├──────────────────────────────────────────┤
│ NOT a signal group (differentiation)       │
├──────────────────────────────────────────┤
│ 3 pillars: 2% Rule · SOPs · Automation     │
├──────────────────────────────────────────┤
│ How the operating system works (4 steps)   │
├──────────────────────────────────────────┤
│ Offer ladder preview (subtle, no hype)     │
├──────────────────────────────────────────┤
│ Proof: discipline stories (no P&L flex)    │
├──────────────────────────────────────────┤
│ FAQ (compliance-forward)                   │
├──────────────────────────────────────────┤
│ Final CTA + full disclaimer footer         │
└──────────────────────────────────────────┘
```

---

## Hero copy framework

### Headline (recommended)
**Stop trading on emotion. Start operating with structure.**

### Alternates (A/B)
- **B:** A private financial operating system for serious traders  
- **C:** The 2% rule, daily SOPs, and automation support — not another signal group  

### Subheadline
> Alpha Elite delivers education, trade ideas, automation support, SOPs, and community support — built around risk discipline. No profit guarantees. No hype.

### Primary CTA
`Get the Alpha Elite Gameplan` → opt-in anchor

### Secondary CTA
`Explore Apprentice Course` → `/apprentice`

### Trust row (text only)
`2% Risk Framework` · `Daily SOPs` · `Private Community`

**Banned in hero:** win rates, member profit, "free signals", countdown timers

---

## Differentiation block

**H2:** This is not a signal group.

| Signal-group pattern | Alpha Elite operating system |
|---------------------|------------------------------|
| Chase alerts | Follow documented SOPs |
| Size by feel | Size by 2% rule |
| No review cadence | Daily / weekly reviews |
| Hype in chat | Structured education + support |

---

## Form CRO (`form-cro` skill)

| Rule | Spec |
|------|------|
| Fields | email, first_name, [experience] max |
| CTA button | `Send me the Gameplan` |
| Privacy | Link below form |
| Mobile | Single column, 44px touch targets |
| a11y | Labels, contrast, keyboard — see web quality checklist |

**Form intro (premium):**
> Get the Alpha Elite Gameplan. Built on the 2% rule. One educational PDF. No signal spam.

---

## Objection → FAQ snippets

| Objection | Response angle |
|-----------|----------------|
| Guaranteed returns? | No. Education and frameworks only. |
| vs signal groups? | We build operating habits, not alert addiction. |
| Bot passive income? | Automation support — you own every decision. |
| Minimum capital? | Risk % framework applies to any size — no capital promises. |

---

## Social proof (compliant)

**Use:** completion rates, SOP adoption quotes, "clarity" testimonials  
**Avoid:** P&L screenshots, % monthly gain, "life changed money" hooks  

---

## GA4 events

| Event | Trigger |
|-------|---------|
| `generate_lead` | Gameplan form success |
| `scroll_75` | 75% depth |
| `click_apprentice_cta` | Secondary CTA |
| `view_offer_section` | Offer block in viewport |

---

## A/B roadmap (post-MVP)

| Test | Hypothesis |
|------|------------|
| Headline A vs C | "Not signal group" in headline lifts qualified opt-ins |
| Disclaimer above vs below fold | Above fold increases serious lead quality |
| Video founder 90s | Trust lift without hype |

---

## Pre-publish CRO + quality gate

- [ ] Compliance review PASS  
- [ ] `web_quality_checklist.md` PASS  
- [ ] Form → Brevo test  
- [ ] 5-second test: visitor says "system/education" not "signals"  
- [ ] Mobile checkout path from Apprentice CTA verified  

---

## Acceptance criteria

- [ ] Single primary conversion (Gameplan opt-in) per homepage  
- [ ] Zero hype/profit-prohibited terms in hero  
- [ ] Disclaimer visible on first screen or sticky footer  
- [ ] Lighthouse mobile performance ≥ 70  
