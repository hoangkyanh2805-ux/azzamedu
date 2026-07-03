# Web Quality Checklist — Alpha Elite

## Purpose
Pre-launch and ongoing quality gate for WordPress/Elementor landing and funnel pages. Distilled from `addyosmani/web-quality-skills` (Lighthouse, Core Web Vitals, WCAG 2.2).

## When to use
- Before publishing any landing/sales page
- After Elementor changes
- Weekly ops on primary funnel URLs
- Agent trigger: "audit landing", "web quality check"

**Install skill:** `npx skills add addyosmani/web-quality-skills --skill web-quality-audit performance core-web-vitals accessibility seo`

---

## Target scores (Lighthouse mobile)

| Category | Minimum | Ideal |
|----------|---------|-------|
| Performance | 70 | ≥ 90 |
| Accessibility | 95 | 100 |
| Best Practices | 90 | ≥ 95 |
| SEO | 90 | ≥ 95 |

---

## Core Web Vitals

| Metric | Good | Action if fail |
|--------|------|----------------|
| **LCP** | < 2.5s | Optimize hero image, fonts, server TTFB |
| **INP** | < 200ms | Reduce JS, defer Elementor animations |
| **CLS** | < 0.1 | Set image dimensions, reserve form space |

---

## Performance budget (Elementor landing)

| Resource | Budget |
|----------|--------|
| Total page weight | < 1.5 MB |
| JavaScript (gzip) | < 300 KB |
| CSS (gzip) | < 100 KB |
| Above-fold images | < 500 KB |
| Fonts | < 100 KB |
| Third-party (Brevo, GA4) | < 200 KB |

### Performance checks
- [ ] Hero image WebP, properly sized (not 4000px wide)
- [ ] Lazy-load below-fold images
- [ ] YouTube embed: click-to-load facade (not autoload iframe)
- [ ] Limit Elementor animations on mobile
- [ ] Caching plugin enabled (page + browser)
- [ ] Brotli/Gzip on server
- [ ] No render-blocking unused CSS/JS
- [ ] LCP element = hero text or optimized hero image (not slider)

---

## Accessibility (WCAG 2.2 AA)

### Perceivable
- [ ] All images have meaningful `alt` (decorative = `alt=""`)
- [ ] Color contrast ≥ 4.5:1 body text, ≥ 3:1 large text
- [ ] Information not conveyed by color alone (form errors, states)
- [ ] Video has captions if spoken content (or transcript link)

### Operable
- [ ] All CTAs and form fields keyboard accessible
- [ ] Visible focus indicators on links/buttons/inputs
- [ ] No keyboard traps in modals/popups
- [ ] Touch targets ≥ 24×24px (44px preferred for mobile CTAs)
- [ ] Skip link or logical heading hierarchy (one H1)

### Understandable
- [ ] `<html lang="vi">` or appropriate lang
- [ ] Form inputs have visible labels (not placeholder-only)
- [ ] Error messages clear and associated with fields
- [ ] Consistent nav across landing / apprentice / vip

### Robust
- [ ] Valid HTML (no major validator errors)
- [ ] ARIA only where needed — prefer native elements

**Tools:** Lighthouse a11y · axe DevTools · keyboard-only walkthrough

---

## SEO (landing funnel)

- [ ] Unique `<title>` per page (≤ 60 chars)
- [ ] Meta description (≤ 155 chars) — system-first, not hype keywords
- [ ] Canonical URL set
- [ ] Open Graph + Twitter card image
- [ ] H1 matches page intent (one per page)
- [ ] Logical H2–H3 structure
- [ ] Internal links: Gameplan CTA, Apprentice, legal pages
- [ ] `robots.txt` allows indexing of sales pages
- [ ] Schema: `Organization` + `WebPage` (RankMath/Yoast)
- [ ] No keyword stuffing ("free forex signals" etc.)

---

## Best practices & security

- [ ] HTTPS everywhere, no mixed content
- [ ] No console errors on load
- [ ] Privacy policy + disclaimer linked in footer
- [ ] Cookie/consent if GA4 + tracking (jurisdiction-dependent)
- [ ] External links `rel="noopener"` where needed
- [ ] WP admin not exposed · security plugin baseline
- [ ] Form submissions HTTPS POST to Brevo

---

## Funnel-specific CRO + quality

- [ ] Opt-in form ≤ 3 fields · mobile full-width
- [ ] Primary CTA contrast passes a11y
- [ ] Disclaimer visible without excessive scroll (footer minimum)
- [ ] Thank-you page loads fast (no heavy upsell video autoload)
- [ ] Checkout (FunnelKit) mobile payment flow tested
- [ ] GA4 events fire: `generate_lead`, `begin_checkout`, `purchase`
- [ ] UTM parameters preserved through funnel

---

## Pre-deploy gate (required)

Run on **mobile emulation** for:
- `/` or `/alpha-elite` (landing)
- `/apprentice`
- `/gameplan-thank-you`
- `/checkout/` (FunnelKit)

| Step | Pass? |
|------|-------|
| Lighthouse mobile ≥ targets above | [ ] |
| axe 0 critical / serious | [ ] |
| Manual keyboard form submit | [ ] |
| LCP < 2.5s (field or lab) | [ ] |
| Compliance footer present | [ ] |
| No broken links | [ ] |

**Block launch if:** LCP > 4s mobile OR any critical a11y failure OR missing risk disclaimer.

---

## Weekly monitor

- [ ] PageSpeed Insights on primary URL
- [ ] Uptime check (UptimeRobot)
- [ ] Form test submission
- [ ] Check Search Console CWV report

---

## Agent routing

| Task | Skill |
|------|-------|
| Full audit | `web-quality-audit` |
| Speed fixes | `performance` + `core-web-vitals` |
| Form/CTA a11y | `accessibility` |
| Meta/schema | `seo` |

See also: `docs/landing_page_cro_framework.md` · `.ai/agents/landing-qa.md`

---

## Acceptance criteria

- [ ] All primary funnel URLs pass pre-deploy gate
- [ ] Results logged in `.ai/audit/web-quality-YYYY-MM-DD.md`
- [ ] Regressions checked after each Elementor publish
