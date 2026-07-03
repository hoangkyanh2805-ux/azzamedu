# Alpha Elite — Landing Page CRO Design Package

> **Method:** Landing Page CRO Designer (page-cro + premium SaaS desk patterns)  
> **Visual direction:** Dark AI trading desk · premium SaaS · private operating system  
> **NOT:** cheap course page · forex signal group · hype P&L marketing  

**References adapted (compliance-safe):**
- StrategyFactory.ai → tier pricing, library grid, FAQ, Inner Circle gating, “how it works” steps  
- shadcn / Launch UI → clean sections, card borders, typography rhythm, generous whitespace  
- **AI CES Workspace PDF** → long-scroll section rhythm, before/after, timeline, pricing grid (`pdf-landing-section-map.md`)  
- Elementor → final implementation  

**Core message:** *You do not need another signal. You need a system that stops you from trading emotionally.*

Cross-check: `docs/compliance_guardrails.md` · `docs/risk-compliance-checklist.md`

---

## Design system (Elementor global)

### Color tokens

| Token | Hex | Use |
|-------|-----|-----|
| `bg-base` | `#09090b` | Page background (zinc-950) |
| `bg-elevated` | `#18181b` | Cards (zinc-900) |
| `bg-panel` | `#27272a` | Nested panels |
| `border` | `rgba(255,255,255,0.08)` | Card borders |
| `text-primary` | `#fafafa` | Headlines |
| `text-muted` | `#a1a1aa` | Body secondary |
| `accent` | `#22d3ee` | Cyan-400 — CTAs, links (desk feel) |
| `accent-muted` | `#0891b2` | Hover states |
| `success` | `#34d399` | Status dots only — **not profit** |
| `warning-disclaimer` | `#71717a` | Disclaimer text |

**Avoid:** neon green profit charts, gold Lambo imagery, $$$ iconography.

### Typography

| Element | Font | Size desktop | Size mobile |
|---------|------|--------------|-------------|
| H1 | Inter / system | 48–56px / 600 | 32–36px |
| H2 | Inter | 36–40px / 600 | 28px |
| H3 | Inter | 24px / 600 | 20px |
| Body | Inter | 16–18px / 400 | 16px |
| Label | Inter | 12px uppercase tracking | 11px |
| Mono accent | JetBrains Mono | SOP tags, SKU labels | — |

### Spacing & layout

- Max content width: **1140px** (boxed sections)  
- Section padding: **96px** desktop / **64px** mobile  
- Card radius: **12px** (shadcn default feel)  
- Grid: 12-col Elementor, 24px gutter  

### Motion

- Subtle fade-up on scroll (Elementor motion — **off on mobile** for INP)  
- No flashing tickers or fake “live profit” counters  

### Elementor kit

- Header: Theme Builder sticky  
- Footer: Theme Builder global (disclaimer always visible)  
- Forms: Elementor Pro + Brevo integration  
- Icons: Lucide-style line icons (Elementor icon set or SVG)  

---

## 1. Homepage wireframe (`/`)

**Primary conversion:** Gameplan opt-in  
**Secondary:** Explore Apprentice  

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ STICKY HEADER                                                            │
│ [Logo Alpha Elite]          How it works · Offers · FAQ    [Get Gameplan]│
├──────────────────────────────────────────────────────────────────────────┤
│ HERO (2-col: 55/45)                                                      │
│ ┌─────────────────────────────┐  ┌──────────────────────────────────┐  │
│ │ Eyebrow: PRIVATE FINANCIAL   │  │ DESK PREVIEW (mock UI card)      │  │
│ │ OPERATING SYSTEM             │  │ · SOP checklist panel            │  │
│ │                              │  │ · 2% risk meter (educational)    │  │
│ │ H1: You don't need another   │  │ · "Today's review" not P&L       │  │
│ │ signal. You need a system.   │  │ Optional: 60s muted demo video   │  │
│ │                              │  └──────────────────────────────────┘  │
│ │ Sub: education, trade ideas, │                                          │
│ │ automation support, SOPs...  │                                          │
│ │ Micro disclaimer (1 line)    │                                          │
│ │                              │                                          │
│ │ [Get Alpha Elite Gameplan]   │                                          │
│ │ [Explore Apprentice →]       │                                          │
│ │ Trust: 2% Rule · SOPs · Desk │                                          │
│ └─────────────────────────────┘                                          │
├──────────────────────────────────────────────────────────────────────────┤
│ LOGO STRIP (optional) — "Built for operators, not alert chasers"         │
│ text labels only, no broker logos implying endorsement unless licensed   │
├──────────────────────────────────────────────────────────────────────────┤
│ DIFFERENTIATION — "Not a signal group" (2-col contrast table)            │
│ Signal-group habits  vs  Operating-system habits                         │
├──────────────────────────────────────────────────────────────────────────┤
│ SYSTEM LIBRARY PREVIEW (StrategyFactory-inspired, compliant)             │
│ 3 cards: Daily SOP · 2% Risk Framework · Automation Support Docs         │
│ CTA: "See inside the Gameplan" → scroll to opt-in                        │
├──────────────────────────────────────────────────────────────────────────┤
│ HOW IT WORKS — 4 steps (horizontal timeline)                             │
│ Gameplan → Apprentice → VIP Desk → Quant / Inner Circle                  │
├──────────────────────────────────────────────────────────────────────────┤
│ ACTIVITY STRIP (compliant — no P&L)                                      │
│ "Community operating rhythm" — anonymized: SOP reviews, module completes │
│ NOT: live profit feed                                                    │
├──────────────────────────────────────────────────────────────────────────┤
│ VIDEO DEMO — "Inside the operating system" (90s, YouTube unlisted embed) │
│ Founder/system walkthrough — education only                              │
├──────────────────────────────────────────────────────────────────────────┤
│ OFFER LADDER PREVIEW — 3 visible cards (Gameplan free · Apprentice · VIP)│
│ Quant + Inner Circle as text links below                                 │
├──────────────────────────────────────────────────────────────────────────┤
│ LEAD MAGNET SECTION — opt-in form (duplicate anchor #get-gameplan)       │
│ Form: email, first name | [Send me the Gameplan]                         │
├──────────────────────────────────────────────────────────────────────────┤
│ TRUST / PROOF — discipline testimonials (see §8)                       │
├──────────────────────────────────────────────────────────────────────────┤
│ FAQ — accordion (6–8 items, compliance-forward)                          │
├──────────────────────────────────────────────────────────────────────────┤
│ FINAL CTA band                                                           │
│ [Get the Gameplan]  ·  disclaimer short line                             │
├──────────────────────────────────────────────────────────────────────────┤
│ FOOTER — links, full risk disclaimer, privacy, terms, refund             │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Lead magnet page wireframe (`/gameplan`)

**Use when:** dedicated ad landing URL separate from homepage.  
**Primary conversion:** opt-in only (no nav distraction).

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ MINIMAL HEADER — logo only, no menu                                      │
├──────────────────────────────────────────────────────────────────────────┤
│ HERO (centered, narrow 720px)                                            │
│ H1: The Alpha Elite Gameplan                                             │
│ Sub: The 2% rule, daily SOPs, and a 7-day operating sprint — free PDF   │
│ Bullet row: ✓ Risk framework  ✓ SOP checklists  ✓ Not a signal list     │
├──────────────────────────────────────────────────────────────────────────┤
│ WHAT'S INSIDE — 5 chapter cards (horizontal scroll mobile)               │
├──────────────────────────────────────────────────────────────────────────┤
│ PREVIEW PANEL — blurred PDF mock / chapter 1 excerpt image               │
├──────────────────────────────────────────────────────────────────────────┤
│ OPT-IN FORM (card elevated on dark bg)                                   │
│ [email] [first name]  [Send me the Gameplan]                             │
│ Privacy link · micro disclaimer                                          │
├──────────────────────────────────────────────────────────────────────────┤
│ WHO IT'S FOR / NOT FOR — two columns                                     │
│ For: traders who want structure · Not for: signal chasers                │
├──────────────────────────────────────────────────────────────────────────┤
│ SOFT PITCH — "When you're ready to go deeper" → link /apprentice         │
├──────────────────────────────────────────────────────────────────────────┤
│ FOOTER minimal + full disclaimer                                         │
└──────────────────────────────────────────────────────────────────────────┘
```

**Thank-you (`/gameplan-thank-you`):** `elementor-spec-gameplan-thank-you.md` — check email, video, soft Apprentice CTA.

---

## 3. Apprentice sales page wireframe (`/apprentice`)

**Primary conversion:** checkout click  
**Tone:** course-as-system-install, not "get rich course"

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ HEADER (full nav)                                                        │
├──────────────────────────────────────────────────────────────────────────┤
│ HERO                                                                     │
│ Eyebrow: APPRENTICE OPERATING COURSE                                     │
│ H1: Install the habits before you upgrade the desk                       │
│ Sub: LearnHouse · modules · SOPs · automation support (education)        │
│ [Enroll in Apprentice] → checkout   [See curriculum ↓]                   │
├──────────────────────────────────────────────────────────────────────────┤
│ OUTCOME STRIP — 3 icons: Discipline · Risk protocol · Review cadence     │
├──────────────────────────────────────────────────────────────────────────┤
│ CURRICULUM — module accordion (5 modules, lesson count, time)            │
│ M1 Mindset · M2 2% Rule · M3 SOPs · M4 Automation · M5 Path to VIP       │
├──────────────────────────────────────────────────────────────────────────┤
│ PLATFORM PREVIEW — LearnHouse screenshot in device frame                 │
├──────────────────────────────────────────────────────────────────────────┤
│ WHO THIS IS FOR / NOT FOR                                                │
├──────────────────────────────────────────────────────────────────────────┤
│ PRICING CARD — single column centered                                    │
│ Price · what's included · what's not (no Telegram VIP)                   │
│ [Enroll now] · refund policy link                                        │
├──────────────────────────────────────────────────────────────────────────┤
│ FAQ                                                                      │
├──────────────────────────────────────────────────────────────────────────┤
│ STICKY MOBILE BAR — price + [Enroll]                                     │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 4. VIP sales page wireframe (`/vip`)

**Primary conversion:** VIP checkout  
**Visual:** membership / private desk — StrategyFactory VIP tier energy, compliant copy

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ HERO                                                                     │
│ Eyebrow: VIP PRIVATE SYSTEM                                              │
│ H1: Your private operating desk — not another alert channel              │
│ Sub: Telegram accountability, SOP library, structured trade ideas (edu)  │
│ [Join VIP] monthly/annual toggle                                         │
├──────────────────────────────────────────────────────────────────────────┤
│ DESK FEATURES — 2x2 grid                                                 │
│ Telegram VIP · SOP Library · Trade idea format (education) · Automation support docs │
├──────────────────────────────────────────────────────────────────────────┤
│ COMPARISON TABLE — Apprentice vs VIP (checkmarks, no fake savings timer) │
├──────────────────────────────────────────────────────────────────────────┤
│ TELEGRAM PREVIEW — blurred mock of pinned rules + structured update      │
│ NOT: signal feed screenshot with entries                                 │
├──────────────────────────────────────────────────────────────────────────┤
│ PRICING — 2 cards: Monthly · Annual (highlight annual calmly)            │
│ Includes Apprentice bundle note                                          │
│ [Start VIP]                                                              │
├──────────────────────────────────────────────────────────────────────────┤
│ UPSELL NOTE — DWY Bot & Broker Setup available at checkout (text link)   │
├──────────────────────────────────────────────────────────────────────────┤
│ FAQ + disclaimer                                                         │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Quant Desk application page wireframe (`/quant-desk`)

**Primary conversion:** application submit OR upgrade checkout (VIP required)  
**MVP:** application form + qualify copy; full checkout can link `AE-QNT-001`

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ HERO (narrow)                                                            │
│ Eyebrow: QUANT DESK · BY APPLICATION                                   │
│ H1: Quantitative desk education for operators already running VIP        │
│ Sub: Research workflows, desk SOPs — not fixed returns                   │
├──────────────────────────────────────────────────────────────────────────┤
│ REQUIREMENTS — must have active VIP · completed Apprentice M3+ preferred │
├──────────────────────────────────────────────────────────────────────────┤
│ WHAT YOU GET — list (education, priority channel, desk workflows)        │
│ WHAT YOU DON'T — no managed account, no profit promise                   │
├──────────────────────────────────────────────────────────────────────────┤
│ APPLICATION FORM                                                         │
│ name · email · VIP order ID · trading experience · why Quant (textarea)  │
│ checkbox: I understand trading risk · not investment advice              │
│ [Submit application]                                                     │
├──────────────────────────────────────────────────────────────────────────┤
│ OR: [VIP member? Upgrade to Quant Desk →] checkout link if self-serve    │
├──────────────────────────────────────────────────────────────────────────┤
│ INNER CIRCLE TEASER — single line + link waitlist (phase 2)              │
├──────────────────────────────────────────────────────────────────────────┤
│ FAQ + footer disclaimer                                                  │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Section-by-section Elementor build notes

| Section | Elementor widgets | Settings |
|---------|-------------------|----------|
| **Sticky header** | Theme Builder header · Nav Menu · Button | Transparent → solid `bg-base` on scroll; CTA button accent |
| **Hero** | 2-col section · Heading · Text · Button ×2 · Image/Video | Right: PNG mock or HTML widget desk UI; lazy video |
| **Differentiation** | Icon box ×2 or Table widget | Left column muted red labels (habits to avoid) — no alarmist imagery |
| **Library cards** | Icon box ×3 in 3-col | Equal height cards `bg-elevated` border |
| **How it works** | Steps widget or Numbered icons | Connect with subtle line; mobile = vertical |
| **Activity strip** | Text carousel or static badges | Pre-written compliant lines only |
| **Video** | Video widget facade | Click-to-load YouTube unlisted |
| **Offer ladder** | Price Table or Flip box ×3 | Middle card slightly elevated (VIP later — on homepage highlight Apprentice) |
| **Opt-in form** | Form widget → Brevo | 2 fields; success → `/gameplan-thank-you` |
| **Testimonials** | Testimonial carousel | Text-only cards |
| **FAQ** | Accordion | Schema FAQ optional (no misleading answers) |
| **Footer** | Theme Builder footer | 3-col links + disclaimer block full width |
| **Pricing pages** | Price Table + Toggle (monthly/year) | WooCommerce add-to-cart links or FunnelKit URLs |
| **Quant form** | Form → email/admin or Brevo list | Notification to ops |

**Performance:** WebP images · max 2 fonts · disable heavy motion mobile · see `web_quality_checklist.md`

---

## 7. CTA map

| Page | Primary CTA | Target | Secondary CTA | Target |
|------|-------------|--------|---------------|--------|
| `/` | Get Alpha Elite Gameplan | `#get-gameplan` form | Explore Apprentice | `/apprentice` |
| `/gameplan` | Send me the Gameplan | form submit | — | — |
| `/gameplan-thank-you` | View Apprentice Course | `/apprentice` | Back home | `/` |
| `/apprentice` | Enroll in Apprentice | `/checkout/?add-to-cart=AE-APP-001` | Get free Gameplan | `/gameplan` |
| `/vip` | Start VIP | checkout VIP SKU | Compare Apprentice | `/apprentice` |
| `/quant-desk` | Submit application | form | Upgrade (VIP) | checkout `AE-QNT-001` |
| Header (global) | Get Gameplan | `/gameplan` or `#get-gameplan` | — | — |
| Footer | Risk disclaimer | anchor `#risk` | Legal links | policies |

**GA4 events:** `generate_lead` · `click_apprentice_cta` · `begin_checkout` · `submit_application`

---

## 8. Trust / proof block plan

### Allowed proof types

| Block | Content | Placement |
|-------|---------|-----------|
| **Discipline quotes** | "I finally follow a pre-trade checklist" — first name only | Homepage, Apprentice |
| **Completion stats** | "X% finish Module 1" — only if true | Homepage activity strip |
| **System metrics** | Module count, SOP pages, desk hours — not ROI | VIP page |
| **Process transparency** | How trade ideas are documented (education) | VIP, FAQ |
| **Founder intro** | 90s video — operating philosophy | Homepage hero alt |

### Forbidden proof

- P&L screenshots · win rate % · "member made $X" · before/after balance · live profit ticker

### Recommended layout (homepage)

```text
[Section title] Operators building structure
[3 cards] Quote · Quote · Quote
[Subline] Education and support — individual results vary. Trading involves risk.
```

### StrategyFactory pattern — adapted

They use "live trading" feeds → **we use** "operating rhythm" feed:
- "Member completed weekly review"
- "SOP library updated: Pre-trade checklist v2"
- "Office hours: Thu 8pm ICT"

---

## 9. Mobile layout notes

| Section | Mobile behavior |
|---------|-----------------|
| Header | Hamburger · sticky CTA "Gameplan" visible |
| Hero | Stack vertical — headline → sub → CTA → desk image below |
| Forms | Full-width fields · 48px min button height |
| Library cards | Horizontal scroll snap OR stack |
| Comparison tables | Scroll horizontal wrapper or accordion |
| Pricing | Single card visible · toggle above |
| Video | 16:9 responsive · facade required |
| Sticky enroll bar | Apprentice/VIP pages only · 64px height · z-index below modals |
| Footer disclaimer | Readable 14px min · no tiny legal text |
| Touch targets | 44×44px minimum all CTAs |
| Typography | H1 max 36px · line-height 1.2 |

**Test viewports:** 390px (iPhone) · 768px (iPad) · sticky form not obscured by iOS Safari bar

---

## 10. CRO checklist (pre-publish)

### Message & positioning
- [ ] Hero communicates **system not signals** in 5 seconds
- [ ] Core line present: *You don't need another signal…*
- [ ] Approved phrase in subhead (education, trade ideas, automation support, SOPs, community)
- [ ] No NEVER-table terms (`risk-compliance-checklist.md`)

### Conversion
- [ ] One primary CTA per page
- [ ] Form ≤3 fields on opt-in pages
- [ ] Checkout links use correct SKU URLs
- [ ] Thank-you routes configured
- [ ] Mobile sticky CTA on sales pages

### Trust & compliance
- [ ] Disclaimer visible homepage (hero micro + footer full)
- [ ] No P&L proof imagery
- [ ] FAQ answers "guaranteed profit?" with clear No
- [ ] Quant page states application/education framing

### Technical
- [ ] `web_quality_checklist.md` PASS
- [ ] Brevo form test submission
- [ ] GA4 events fire
- [ ] LCP < 2.5s mobile
- [ ] Compliance Agent PASS logged

### Elementor
- [ ] Global colors/fonts in Site Settings
- [ ] Theme Builder header/footer applied all pages
- [ ] No Elementor unused CSS bloat (experiments off if needed)

---

## Page file index

| Wireframe | Path in Elementor |
|-----------|-------------------|
| Homepage | `/` |
| **PDF section map** | `pdf-landing-section-map.md` |
| **Elementor implementation** | `elementor-implementation-map.md` |
| Lead magnet | `/gameplan` |
| Thank you | `/gameplan-thank-you` |
| Apprentice | `/apprentice` |
| VIP | `/vip` |
| Quant Desk | `/quant-desk` |

**Agent handoff:** Landing Copy Agent → copy blocks · CRO Agent → verify CTA map · Compliance Agent → PASS · Web Quality Agent → launch gate

---

*Package version 1.0 — Alpha Elite Landing Page CRO Design*
