# Compliance Copy Audit — Alpha Elite Landing Pages

**Date:** 2026-07-01  
**Scope:** `web/wordpress/html/*.html`, wireframes, Elementor specs, `landing-page-cro-design.md`  
**Rules:** `docs/compliance_guardrails.md`  
**Companion:** `copywriting-audit.md` · `offers-cro-audit.md` (CRO + offer design)

---

## Summary

| Status | Count |
|--------|-------|
| **FLAG → rewritten** | 6 |
| **PASS (keep)** | 12 |
| **Disclaimers (correct use of “guarantee”)** | 8 |

No instances found of: risk-free trading, fixed monthly return, passive income promise, win-rate guarantee, or explicit financial advice CTAs (“buy X now”).

---

## Flags & rewrites

### 1. `bot support` → `automation support`

| Location | Risk | Rewrite |
|----------|------|---------|
| Hero subheadline (EN) | Implies bot earns money / passive automation | **automation support** |
| `wireframes/01-homepage.md` | Same | Updated |
| `elementor-spec-homepage-hero-optin.md` | Same | Updated |
| `landing-page-cro-design.md` VIP grid | Same | **Automation support docs** |

**Approved line:**
> …structured trade ideas, **automation support**, SOPs, and **community accountability** — built around a **2% risk management framework**…

---

### 2. `no signal spam` / over-use of “signal” in positive-adjacent context

| Location | Risk | Rewrite |
|----------|------|---------|
| Tier bubble note | “Signal” framing even when negated | **Education only · no alert chasing** |

**Keep:** Hero H1 *“You don't need another signal…”* — approved core positioning (negation).

---

### 3. Trust pill `2% Risk` (standalone)

| Location | Risk | Rewrite |
|----------|------|---------|
| Hero trust pills | Could read as promise of safe/profitable sizing | **2% Risk Framework** |

---

### 4. Microcopy missing “not investment advice”

| Location | Risk | Rewrite |
|----------|------|---------|
| Hero micro (EN) | Incomplete short disclaimer | Add **Not investment advice.** |
| `homepage-dark-gold.html` footer | Short VI footer on EN page | Full EN risk block |

**Approved microcopy:**
> No profit guarantees. Trading involves risk. Built for education, structure, community accountability, and risk-aware habits. Not investment advice.

---

### 5. `disciplined execution` (borderline)

| Location | Risk | Rewrite |
|----------|------|---------|
| Hero micro | Could imply trading outcomes | **risk-aware habits** |

---

### 6. Opt-in intro (mixed VI on EN page)

| Location | Risk | Rewrite |
|----------|------|---------|
| `#get-gameplan` intro | “danh sách tín hiệu” OK but inconsistent | EN: **One PDF — educational operating framework, not a trade alert list.** |

---

## PASS — no change required

| Copy | Why safe |
|------|----------|
| *No profit guarantees. Trading involves risk.* | Explicit negation |
| *Không cam kết lợi nhuận* | Explicit negation |
| *Không phải tư vấn đầu tư* | Disclaims advice |
| *not another alert channel* | Negative differentiation |
| *Không phải nhóm tín hiệu* | Negative differentiation |
| FAQ: *Gameplan có đảm bảo lời không?* → **Không** | Question names risk; answer denies |
| Desk UI: *Risk (edu)* · *Minh họa UI · Không phải P&L thật* | Educational framing |
| *not fixed returns* (Quant wireframe) | Explicit negation |
| *not "get rich course"* (design note) | Internal guardrail |
| Trust pills: Daily SOP · Private Desk | Process, not profit |

---

## Approved positioning (use everywhere)

```text
Alpha Elite is a private financial operating system providing education,
structured trade ideas, automation support, SOPs, and community accountability —
helping traders replace emotional execution with structured habits including
2% risk management rules. Not a signal group. No profit guarantees.
```

---

## Channel checklist (landing HTML)

| Page | Footer disclaimer | Form micro | Signal-group negation | Bot/passive language |
|------|-------------------|------------|----------------------|----------------------|
| `homepage-dark-gold.html` | ✅ after fix | ✅ after fix | ✅ | ✅ after fix |
| `homepage.html` | ✅ | ✅ | ✅ | ✅ |
| `gameplan-thank-you.html` | ✅ | ✅ | ✅ | ✅ |

---

## Pre-publish grep (run before go-live)

```bash
rg -i "guaranteed profit|risk.free|passive income|win.rate|bot makes|fixed return|financial advice|buy now|VIP signal|free signal" web/wordpress/html/
```

Allowed hits: negations only (*no profit guarantees*, *not investment advice*, FAQ questions).
