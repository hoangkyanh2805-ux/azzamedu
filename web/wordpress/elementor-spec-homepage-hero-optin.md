# Elementor Build Spec — Homepage Hero + Opt-in (Dark / Gold)

> Page: `/` (Homepage)  
> Parent: `landing-page-cro-design.md` · Wireframe: `wireframes/01-homepage.md`  
> **Theme:** Dark/gold — `design-system-dark-gold.md` · `html/alpha-elite-tokens.css`  
> **HTML reference:** `html/homepage-dark-gold.html`  
> Scope: **Section A (Hero `#hero-main`)** + **Section B (Opt-in `#get-gameplan`)**  
> Stack: Elementor Pro · Brevo form · GA4  
> **Full homepage sections:** `elementor-implementation-map.md` §7

---

## Global prerequisites

### Site Settings → Global Colors

| Name | Value | Token |
|------|-------|-------|
| AE Base | `#000000` | `--ae-bg-base` |
| AE Elevated | `#0f0f0f` | `--ae-bg-elevated` |
| AE Panel | `#1a1a1a` | `--ae-bg-panel` |
| AE Gold | `#ffd700` | `--ae-gold` |
| AE Gold Muted | `#c5a059` | `--ae-gold-muted` |
| AE Gold Deep | `#b8860b` | `--ae-gold-deep` |
| AE Glow | `#f59e0b` | `--ae-glow` |
| AE Text | `#ffffff` | `--ae-text` |
| AE Muted | `#b3b3b3` | `--ae-muted` |
| AE Disclaimer | `#8a8a8a` | `--ae-disclaimer` |
| AE Border | `rgba(255,255,255,0.1)` | `--ae-border` |
| AE Border Gold | `rgba(255,215,0,0.2)` | `--ae-border-gold` |
| AE Success dot | `#34d399` | Review mode only — **not profit** |

> **Deprecated (cyan v1):** `#22d3ee`, `#0891b2`, `#09090b` — do not use on new builds.

### Site Settings → Global Fonts

| Role | Font | Weight | Elementor |
|------|------|--------|-----------|
| Display / H1–H2 | **Anton** | 400 | Primary Headings |
| Body / UI | **Montserrat** | 400, 500, 600, 700 | Text + buttons |

Google Fonts: `Anton` + `Montserrat:wght@400;500;600;700`

### Custom CSS — paste once

**Source of truth:** copy entire `html/alpha-elite-tokens.css` into:
- **Appearance → Customize → Additional CSS**, OR  
- **Elementor → Site Settings → Custom CSS**

Minimum Elementor bridge (if not pasting full file):

```css
/* Elementor button class bridges — dark/gold */
.ae-btn-gold .elementor-button {
  background: linear-gradient(180deg, #ffd700 0%, #eab308 100%) !important;
  color: #000 !important;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700 !important;
  border-radius: 8px !important;
  padding: 14px 28px !important;
  border: none !important;
  box-shadow: 0 4px 20px rgba(234, 179, 8, 0.35);
}
.ae-btn-gold .elementor-button:hover {
  background: linear-gradient(180deg, #ffe566 0%, #ffd700 100%) !important;
}
.ae-btn-outline .elementor-button {
  background: transparent !important;
  color: #fff !important;
  border: 1px solid rgba(255, 255, 255, 0.85) !important;
  font-weight: 600 !important;
  border-radius: 8px !important;
  padding: 14px 28px !important;
}
.ae-btn-outline .elementor-button:hover {
  border-color: #ffd700 !important;
  color: #ffd700 !important;
}
.ae-eyebrow-gold {
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #c5a059;
}
.ae-disclaimer-micro {
  font-size: 12px;
  color: #8a8a8a;
  line-height: 1.5;
}
.ae-trust-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 999px;
  font-size: 12px;
  color: #b3b3b3;
}
.ae-trust-pill::before {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #ffd700;
}
.ae-desk-card-gold {
  background: linear-gradient(145deg, #141414, #0a0a0a);
  border: 1px solid rgba(255, 215, 0, 0.2);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 48px rgba(245, 158, 11, 0.1);
}
.ae-form-card-gold {
  background: linear-gradient(160deg, #121212, #080808);
  border: 1px solid rgba(255, 215, 0, 0.2);
  border-radius: 12px;
  padding: 40px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
}
@media (max-width: 767px) {
  .ae-hero-section { min-height: auto !important; padding-top: 48px !important; }
  .ae-form-card-gold { padding: 24px !important; }
}
```

### Page shell class

Add CSS class `ae-theme-gold` on **page** or outermost section wrapper to enable chart watermark + gold glow from `alpha-elite-tokens.css`.

---

# SECTION A — HERO

## Elementor hierarchy

```text
Section: ae-hero-section  [CSS ID: hero-main]
├── Column (50%) — Content
│   ├── Widget: Text Editor (eyebrow)
│   ├── Widget: Heading (H1) — gold gradient class
│   ├── Widget: Text Editor (subhead)
│   ├── Inner Section (2 buttons row)
│   │   ├── Column: Button .ae-btn-gold
│   │   └── Column: Button .ae-btn-outline
│   ├── Widget: Text Editor (disclaimer micro)
│   ├── Inner Section (tier bubble + note)  [CSS ID anchor: alpha-elite-system]
│   └── Inner Section (trust pills row)
└── Column (50%) — Desk preview
    └── Widget: HTML .ae-desk-card-gold
```

---

## Section A — Settings

| Setting | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| **CSS ID** | `hero-main` | — | — |
| **CSS Classes** | `ae-hero-section` | — | — |
| **Layout** | Boxed, width **1140px** | Full width boxed | Full width |
| **Min height** | `90vh` max, or **720px** | `auto` | `auto` |
| **Padding** | Top 120px, Bottom 96px | Top 96px, Bottom 64px | Top 80px, Bottom 48px |
| **Background** | Color `#000000` | same | same |
| **Column gap** | 48px | 32px | 24px |
| **Vertical align** | Middle | Top | Top |
| **Reverse columns** | No | No | **Yes** (content first, desk below) |

### Background (Section → Advanced → Custom CSS)

```css
selector {
  background-color: #000000;
  background-image:
    radial-gradient(ellipse 55% 45% at 75% 45%, rgba(245, 158, 11, 0.22) 0%, transparent 65%),
    radial-gradient(ellipse 40% 30% at 15% 85%, rgba(234, 179, 8, 0.08) 0%, transparent 60%);
}
```

Optional: paste chart watermark from `alpha-elite-tokens.css` `body::before` on page level.

---

## Column A1 — Content (50%)

### Widget 1: Eyebrow (Text Editor)

**CSS Classes:** `ae-eyebrow-gold`

```html
<span class="ae-eyebrow-gold">Private XAUUSD operating system</span>
```

| Style | Value |
|-------|-------|
| Margin bottom | 16px |

---

### Widget 2: Heading (H1)

**CSS Classes:** `ae-hero-title` (from `alpha-elite-tokens.css`)

| Setting | Value |
|---------|-------|
| Title | You Don't Need Another Signal. You Need A System That Stops You From Trading Emotionally. |
| HTML Tag | **H1** |
| Font | Anton (or apply `.ae-hero-title` via HTML widget if gradient needed) |
| Size | clamp ~42–68px desktop / 32–36px mobile |
| Transform | Uppercase |
| Line height | 0.92–1.0 |
| Max width | 600px |

**Gold gradient:** use Custom CSS class `.ae-hero-title` — do not set flat white color in Elementor if class applied.

```css
/* Already in alpha-elite-tokens.css */
.ae-hero-title {
  font-family: 'Anton', sans-serif;
  text-transform: uppercase;
  background: linear-gradient(180deg, #ffd700 0%, #eab308 50%, #b8860b 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 14px rgba(255, 215, 0, 0.28));
}
```

---

### Widget 3: Subhead (Text Editor)

```html
<p style="color:#b3b3b3;font-size:17px;line-height:1.65;max-width:560px;margin:0;">
  Education, structured trade ideas, automation support, SOPs, and community accountability —
  on a 2% risk framework. No guessing. No signal chasing.
</p>
```

| Style | Value |
|-------|-------|
| Margin top | 20px |
| Margin bottom | 20px |

---

### Inner Section: CTA buttons

**Layout:** 2 columns · gap 12px · stack full-width on mobile

#### Widget 5a: Primary button

| Setting | Value |
|---------|-------|
| **CSS Classes** | `ae-btn-gold` |
| Text | Get The 2% Rule Gameplan |
| Link | `#get-gameplan` |
| Min height | 48px |

**GA4:** `data-event="click_gameplan_cta"` `data-location="hero"`

#### Widget 5b: Secondary button

| Setting | Value |
|---------|-------|
| **CSS Classes** | `ae-btn-outline` |
| Text | View Alpha Elite System |
| Link | `#alpha-elite-system` |

---

### Widget 4: Disclaimer micro (after CTAs)

**CSS Classes:** `ae-disclaimer-micro`

```html
<p class="ae-disclaimer-micro" style="margin:16px 0 0;">
  No profit guarantees. Trading involves risk. Built for education, structure, community accountability, and risk-aware habits. Not investment advice.
</p>
```

---

### Inner Section: System preview row (optional)

**CSS ID on wrapper:** `alpha-elite-system`

Tier bubble + note — replicate from `homepage-dark-gold.html` or use Icon Box:
- **Free / PDF** bubble
- Text: *2% Rule Gameplan — risk management framework, daily SOP checklist, 7-day operating sprint. Free · education only · no alert chasing.*

---

### Inner Section: Trust pills

**CSS Classes on each pill:** `ae-trust-pill`

| Pill | Text |
|------|------|
| 1 | 2% Risk Framework |
| 2 | Daily SOP |
| 3 | Private Desk |

Layout: horizontal flex, gap 10px, wrap on mobile. Gold dot via `::before` in CSS.

---

## Column A2 — Desk preview (50%)

### Option A (recommended MVP): HTML Widget

**CSS Classes:** `ae-desk-card-gold`

```html
<div class="ae-desk-card-gold" role="img" aria-label="Operating desk preview">
  <div style="display:flex;justify-content:space-between;margin-bottom:16px">
    <span style="font-size:11px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:#8a8a8a;">Operating desk</span>
    <span style="font-size:12px;color:#34d399;display:flex;align-items:center;gap:6px">
      <span style="width:6px;height:6px;border-radius:50%;background:#34d399"></span>
      Review mode
    </span>
  </div>
  <div style="background:#1a1a1a;border-radius:8px;padding:16px;margin-bottom:12px">
    <div style="font-size:11px;color:#8a8a8a;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:10px">Pre-trade checklist</div>
    <div style="font-size:14px;color:#fff;margin-bottom:8px">☐ Sized to 2% risk framework</div>
    <div style="font-size:14px;color:#888;margin-bottom:8px">☐ Journal SOP</div>
    <div style="font-size:14px;color:#888">☐ Weekly review</div>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
    <div style="background:#1a1a1a;border-radius:8px;padding:12px">
      <div style="font-size:11px;color:#8a8a8a">Risk framework (edu)</div>
      <div style="font-size:22px;font-weight:700;color:#ffd700">2%</div>
    </div>
    <div style="background:#1a1a1a;border-radius:8px;padding:12px">
      <div style="font-size:11px;color:#8a8a8a">State</div>
      <div style="font-weight:600;color:#fff;font-size:14px">Structured</div>
    </div>
  </div>
  <p style="margin-top:14px;font-size:11px;color:#555;line-height:1.4">
    UI illustration only · Not real account data · Trading involves risk.
  </p>
</div>
```

### Option B: Image widget

Export from `homepage-dark-gold.html` hero · WebP <150KB · alt: *Operating desk illustration*

---

## Hero — Mobile responsive checklist

| Element | Mobile rule |
|---------|-------------|
| H1 | 32–36px, line-height ~1 |
| Subhead | 16px |
| Buttons | Stack full-width, 12px gap, min-height 48px |
| Desk card | Full width, margin-top 32px |
| Motion effects | **Disabled** |

---

# SECTION B — OPT-IN (`#get-gameplan`)

On full homepage this section appears after `#offers` (see `homepage-dark-gold.html`). Dedicated ad landing: use `gameplan-preview.html` → `/gameplan`.

## Elementor hierarchy

```text
Section: ae-optin-section  [CSS ID: get-gameplan]
├── Column (100%)
│   ├── Widget: Heading (H2) — gold gradient
│   ├── Widget: Text Editor (intro)
│   ├── 3× Icon Box (optional features row)
│   ├── Inner Section .ae-form-card-gold — max-width 480px
│   │   └── Widget: Form (Elementor Pro)
│   ├── Widget: Text Editor (privacy + disclaimer)
```

---

## Section B — Settings

| Setting | Value |
|---------|-------|
| **CSS ID** | `get-gameplan` |
| **CSS Classes** | `ae-optin-section` |
| **Layout** | Boxed 1140px |
| **Padding** | 80px top/bottom desktop · 56px mobile |
| **Background** | `#000000` |
| **Border top** | `1px solid rgba(255,255,255,0.1)` |

---

## Widget B1: Section heading (H2)

| Setting | Value |
|---------|-------|
| Title | Get The 2% Rule Gameplan — Free |
| HTML Tag | H2 |
| Align | Center |
| Font | Anton |
| Size | 36–40px desktop / 28px mobile |
| Style | Gold gradient (match `.ae-section-head h2` in tokens) |
| Margin bottom | 12px |

Custom CSS for H2 in opt-in section:

```css
.ae-optin-section h2 {
  font-family: 'Anton', sans-serif;
  text-transform: uppercase;
  background: linear-gradient(180deg, #ffd700, #b8860b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

---

## Widget B2: Intro (Text Editor, center)

```html
<p style="text-align:center;color:#b3b3b3;font-size:17px;max-width:560px;margin:0 auto 36px;line-height:1.65;">
  One PDF — an educational operating framework, not a trade alert list.
</p>
```

---

## Widget B3: Features row (optional)

3 columns — match `homepage-dark-gold.html`:

| Title | Description |
|-------|-------------|
| 2% Rule | Risk management framework |
| Daily SOP | Checklist |
| 7-Day Sprint | Operating habits |

Card: `border: 1px solid rgba(255,255,255,0.1)`, title color `#ffd700`.

---

## Widget B4: Form card

**Structure:** Inner Section · class `ae-form-card-gold` · max-width **480px** · centered

### Form fields

| # | Field | Label | Required |
|---|-------|-------|----------|
| 1 | Email | Email | Yes |
| 2 | Text | First name | Yes |
| 3 | Select | Trading experience | No |

**Experience options:** Just starting · 6–24 months · 2+ years

### Form actions

| Action | Config |
|--------|--------|
| Redirect | `/gameplan-thank-you` |
| Brevo list | `gameplan-leads` |
| Tag | `lead_gameplan` |

### Form button styling

| Element | Value |
|---------|-------|
| Label | Send Me The Gameplan |
| **CSS Classes** | `ae-btn-gold` |
| Width | 100% |
| Background | Gold gradient (via class) |
| Text | `#000000` |
| Border radius | 8px |

### Form field styling

| Element | Value |
|---------|-------|
| Label | `#b3b3b3` Montserrat 13px |
| Field bg | `#1a1a1a` |
| Field border | `1px solid rgba(255,255,255,0.1)` |
| Field text | `#ffffff` |
| Focus border | `#ffd700` |
| Focus ring | `0 0 0 2px rgba(255,215,0,0.15)` |
| Error | `#f87171` |

---

## Widget B5: Privacy + disclaimer

```html
<p style="text-align:center;font-size:12px;color:#8a8a8a;margin-top:20px;line-height:1.6;">
  Educational emails from Alpha Elite.
  <a href="/privacy-policy" style="color:#ffd700;">Privacy Policy</a>.<br>
  Trading involves risk. No profit guarantees. Not investment advice.
</p>
```

---

# Header (Theme Builder)

| Element | Spec |
|---------|------|
| Background | `rgba(0,0,0,0.88)` + blur |
| Border bottom | `1px solid rgba(255,255,255,0.1)` |
| Logo | `.ae-logo-gold` — Montserrat caps, Elite in gold |
| Nav | How it works · Offers · FAQ |
| Badge (optional) | `.ae-badge-seal` — "Free Gameplan" |
| CTA | `.ae-btn-gold` · "Get Gameplan" → `#get-gameplan` or `/gameplan` |

---

# GA4 / tracking

| Event | Trigger | Parameters |
|-------|---------|------------|
| `generate_lead` | Thank-you page view | `form_id=gameplan` |
| `click_gameplan_cta` | Hero primary | `location=hero` |
| `scroll_to_optin` | `#get-gameplan` in viewport | — |

---

# Build order (checklist)

### Global (S0)
- [ ] Global colors §2.1 pasted
- [ ] Anton + Montserrat loaded
- [ ] Full `alpha-elite-tokens.css` in Custom CSS
- [ ] Theme Builder header/footer dark/gold

### Hero
- [ ] Section ID `hero-main` · 2 columns · reverse mobile
- [ ] Eyebrow → H1 gold → subhead → CTAs → disclaimer
- [ ] Secondary → `#alpha-elite-system`
- [ ] Trust pills `.ae-trust-pill`
- [ ] Desk HTML `.ae-desk-card-gold`
- [ ] Gold radial background CSS
- [ ] Preview 390px

### Opt-in
- [ ] Section ID `get-gameplan`
- [ ] H2 gold gradient + intro
- [ ] Form in `.ae-form-card-gold`
- [ ] Brevo `gameplan-leads` + redirect thank-you
- [ ] Compliance PASS — `compliance-copy-audit.md`

### Quality
- [ ] `web_quality_checklist.md`
- [ ] No cyan `#22d3ee` left on page
- [ ] LCP = text-first hero

---

# Vietnamese copy alternate (optional)

H1:
> Bạn không cần thêm một kênh tín hiệu. Bạn cần một hệ thống giúp bạn ngừng giao dịch theo cảm xúc.

Primary CTA: `Nhận Alpha Elite Gameplan`  
Form button: `Gửi Gameplan cho tôi`

Keep disclaimer in VI per `docs/compliance_guardrails.md`.

---

# Related docs

| Doc | Purpose |
|-----|---------|
| `design-system-dark-gold.md` | Full token map |
| `html/homepage-dark-gold.html` | Visual reference |
| `elementor-implementation-map.md` | All pages + build sequence |
| `elementor-spec-gameplan-thank-you.md` | Thank-you page |
| `compliance-copy-audit.md` | Copy QA |

---

*Spec v2.0 — Dark/gold theme. Supersedes cyan v1.0 (`#22d3ee`). Other homepage sections: `elementor-implementation-map.md` §7.*
