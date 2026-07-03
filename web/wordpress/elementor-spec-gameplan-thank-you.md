# Elementor Build Spec — Gameplan Thank You Page (Dark / Gold)

> Page: `/gameplan-thank-you`  
> Parent: `landing-page-cro-design.md` · Pairs with: `elementor-spec-homepage-hero-optin.md` v2.0  
> **Theme:** Dark/gold — `design-system-dark-gold.md` · `html/alpha-elite-tokens.css`  
> **HTML reference:** `html/gameplan-thank-you.html`  
> **Trigger:** Elementor form redirect after Gameplan opt-in (homepage or `/gameplan`)  
> Stack: Elementor Pro · Brevo Email 0 (async) · GA4 · optional YouTube unlisted

> **Deprecated:** v1.0 cyan (`#22d3ee`, `#09090b`, Inter) — do not use on new builds.

---

## Page purpose

| Goal | How |
|------|-----|
| Confirm opt-in success | Clear “check your email” state |
| Set expectations | PDF via email, not instant browser download |
| Reduce support tickets | Spam folder tip, sender address |
| Nurture next step | Soft Apprentice CTA (no hard sell) |
| Track conversion | GA4 `generate_lead` on page view |
| Compliance | Disclaimer visible; no profit promises |

**Do not:** offer direct PDF download on this page (keeps email capture honest + enables Brevo nurture).  
**Exception:** backup link in Email 0 only, not on TY page MVP.

---

## Reuse global kit

Same as `elementor-spec-homepage-hero-optin.md` v2.0 — no duplicate setup:

| Item | Source |
|------|--------|
| Global colors | AE Base `#000000`, AE Gold `#ffd700`, AE Muted `#b3b3b3`, etc. |
| Fonts | **Anton** (display) · **Montserrat** (body/UI) |
| CSS file | Copy `html/alpha-elite-tokens.css` |
| Button classes | `.ae-btn-gold`, `.ae-btn-outline` |
| Utility classes | `.ae-eyebrow-gold`, `.ae-disclaimer-micro` |

### Additional CSS (thank-you page)

```css
.ae-ty-page {
  min-height: 80vh;
  display: flex;
  flex-direction: column;
}
.ae-success-icon {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: rgba(255, 215, 0, 0.1);
  border: 1px solid rgba(255, 215, 0, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 28px;
  box-shadow: 0 0 32px rgba(245, 158, 11, 0.15);
}
.ae-success-icon svg {
  width: 30px;
  height: 30px;
  stroke: #ffd700;
  fill: none;
  stroke-width: 2.5;
}
.ae-step-card {
  background: linear-gradient(160deg, #121212, #080808);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 24px;
  text-align: left;
  height: 100%;
  transition: border-color 0.2s;
}
.ae-step-card:hover { border-color: rgba(255, 215, 0, 0.2); }
.ae-step-num {
  font-size: 11px;
  font-weight: 700;
  color: #ffd700;
  letter-spacing: 0.12em;
  margin-bottom: 10px;
}
.ae-apprentice-card {
  background: linear-gradient(145deg, #141414, #0a0a0a);
  border: 1px solid rgba(255, 215, 0, 0.2);
  border-radius: 12px;
  padding: 32px;
  max-width: 640px;
  margin: 0 auto;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 40px rgba(245, 158, 11, 0.06);
}
.ae-minimal-header .elementor-widget-image img {
  max-height: 36px;
  width: auto;
}
@media (max-width: 767px) {
  .ae-step-card { margin-bottom: 12px; }
}
```

---

## Theme Builder — Minimal header (this page only)

**Apply:** Elementor → Theme Builder → Header → Display Conditions → **Singular** → Page `Gameplan Thank You` only

### Header structure

```text
Section: ae-minimal-header
└── Column 100%
    └── Image (logo) → link to /
```

| Setting | Value |
|---------|-------|
| Height | 72px |
| Background | `#000000` |
| Border bottom | `1px solid rgba(255,255,255,0.1)` |
| Padding | 16px 24px |
| Logo max height | 36px |
| **No** nav menu | — |
| **No** CTA button | — |

---

# SECTION 1 — SUCCESS HERO

## Elementor hierarchy

```text
Section: ae-ty-hero
└── Column (100%, max 720px centered)
    ├── HTML (success icon)
    ├── Text (eyebrow)
    ├── Heading H1
    ├── Text Editor (subhead)
    ├── Text Editor (sender tip)
    └── Text Editor (disclaimer micro)
```

## Section settings

| Setting | Value |
|---------|-------|
| **CSS Classes** | `ae-ty-hero ae-ty-page` |
| Layout | Boxed 1140px, content max **720px** |
| Padding | Top 64px, Bottom 48px (desktop) · Top 48px mobile |
| Background | `#000000` |
| Align | Center |

---

### Widget 1: Success icon (HTML)

```html
<div class="ae-success-icon" aria-hidden="true">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
  </svg>
</div>
```

---

### Widget 2: Eyebrow (Text)

| Setting | Value |
|---------|-------|
| Text | Gameplan requested |
| **CSS Classes** | `ae-eyebrow-gold` |
| Align | Center |

---

### Widget 3: Heading H1

| Setting | Value |
|---------|-------|
| Title | **Check your email** |
| HTML Tag | H1 |
| Font | Anton |
| Size | 44px desktop / 28px mobile |
| Style | Uppercase, gold gradient text (match hero) |
| Align | Center |

---

### Widget 4: Subhead (Text Editor)

```html
<p style="text-align:center;color:#b3b3b3;font-size:18px;line-height:1.65;margin:16px auto 0;max-width:560px;">
  We're sending your <strong style="color:#ffffff;">Alpha Elite Gameplan</strong> now.
  It includes the 2% rule, daily SOP checklist, and 7-day operating sprint — education only.
</p>
```

---

### Widget 5: Sender tip (Text Editor)

```html
<p style="text-align:center;color:#8a8a8a;font-size:15px;margin-top:20px;line-height:1.6;">
  From: <strong style="color:#b3b3b3;">hello@yourdomain.com</strong><br>
  Subject: <strong style="color:#b3b3b3;">[Alpha Elite] Your Gameplan is ready</strong>
</p>
```

Replace `yourdomain.com` with live Brevo FROM domain.

---

### Widget 6: Disclaimer micro

```html
<p class="ae-disclaimer-micro" style="text-align:center;margin-top:16px;">
  Trading involves risk. No profit guarantees. Educational content only.
</p>
```

---

# SECTION 2 — CHECK EMAIL STEPS

## Elementor hierarchy

```text
Section: ae-ty-steps
└── Column 100%
    └── Inner Section — 3 columns
        ├── Column 33%: HTML step card 1
        ├── Column 33%: HTML step card 2
        └── Column 33%: HTML step card 3
```

## Section settings

| Setting | Value |
|---------|-------|
| Padding | 48px top/bottom |
| Background | `#000000` |
| Column gap | 16px |
| Mobile | Columns stack, 100% width each |

### Step cards (HTML widget ×3)

#### Step 1 — Open inbox

```html
<div class="ae-step-card">
  <div class="ae-step-num">STEP 1</div>
  <div style="font-size:17px;font-weight:600;color:#ffffff;margin-bottom:8px;">Open your inbox</div>
  <p style="font-size:14px;color:#b3b3b3;margin:0;line-height:1.55;">
    Usually arrives in 1–3 minutes. Search for <strong style="color:#ffffff;">Alpha Elite</strong> if you don't see it.
  </p>
</div>
```

#### Step 2 — Check spam

```html
<div class="ae-step-card">
  <div class="ae-step-num">STEP 2</div>
  <div style="font-size:17px;font-weight:600;color:#ffffff;margin-bottom:8px;">Check spam</div>
  <p style="font-size:14px;color:#b3b3b3;margin:0;line-height:1.55;">
    Mark as safe so you receive the full Day 2–7 email sequence.
  </p>
</div>
```

#### Step 3 — Start Day 1

```html
<div class="ae-step-card">
  <div class="ae-step-num">STEP 3</div>
  <div style="font-size:17px;font-weight:600;color:#ffffff;margin-bottom:8px;">Start Day 1</div>
  <p style="font-size:14px;color:#b3b3b3;margin:0;line-height:1.55;">
    Complete the emotional-trading self-audit in the PDF before your next session.
  </p>
</div>
```

---

# SECTION 3 — INTRO VIDEO (optional, recommended)

| Setting | Value |
|---------|-------|
| H3 | **60 seconds: what Alpha Elite actually is** |
| Sub | A quick walkthrough of the operating system — not a signal pitch. |
| Video | YouTube unlisted · **no autoplay** · click-to-load |
| Aspect ratio | 16:9 |

**Compliance script (video must say):** education only, trading involves risk, not investment advice.

---

# SECTION 4 — WHAT TO DO NEXT (optional)

| Setting | Value |
|---------|-------|
| H2 | **While you wait** |
| List style | Icon gold `#ffd700`, text `#b3b3b3` |

| # | Text |
|---|------|
| 1 | Read Email 1 tomorrow — five signs of emotional trading |
| 2 | Print the pre-trade checklist from the Gameplan |
| 3 | When ready, explore the **Apprentice Operating Course** → `/apprentice` |

---

# SECTION 5 — SOFT APPRENTICE CTA

```html
<div class="ae-apprentice-card">
  <div class="ae-eyebrow-gold" style="margin-bottom:12px;">When you're ready for the full system</div>
  <h3 style="font-family:'Anton',sans-serif;font-size:22px;font-weight:400;text-transform:uppercase;letter-spacing:0.04em;color:#ffffff;margin:0 0 12px;">
    Install your complete operating habits
  </h3>
  <p style="font-size:15px;color:#b3b3b3;line-height:1.65;margin:0;">
    The Gameplan is your map. The <strong style="color:#ffffff;">Apprentice Operating Course</strong> is where you build SOPs,
    risk protocol, and automation support on LearnHouse. Then upgrade to VIP Private Desk when you're ready.
  </p>
</div>
```

### Buttons (centered, below card)

| Button | Class | Link |
|--------|-------|------|
| View Apprentice Course | `ae-btn-gold` | `/apprentice` |
| Back to homepage | `ae-btn-outline` | `/` |

**GA4:** `click_apprentice_cta` · `location=thank_you`

---

# SECTION 6 — MINI FAQ

| # | Question | Answer |
|---|----------|--------|
| 1 | I didn't receive the email | Wait 5 minutes, check spam, search "Alpha Elite". Still nothing? Email hello@yourdomain.com |
| 2 | Is this a signal group? | **No.** Alpha Elite is an education and operating-system community — structured trade ideas inside SOPs, not an alert channel. |
| 3 | Does the Gameplan guarantee profits? | **No.** It's an educational framework including the 2% risk rule. Trading involves substantial risk of loss. Not investment advice. |

Accordion: title `#ffffff`, content `#b3b3b3`, border `rgba(255,255,255,0.1)`, open state border gold.

---

# SECTION 7 — FOOTER

Use global footer or compact block:

```html
<p style="text-align:center;font-size:12px;color:#666;line-height:1.6;max-width:800px;margin:48px auto 24px;padding:0 24px;">
  <strong>RISK WARNING:</strong> Trading forex, crypto, and XAUUSD involves substantial risk of loss.
  Alpha Elite provides education, structured trade ideas, automation support, SOPs, and community accountability —
  not investment advice or guaranteed returns. Past results do not guarantee future outcomes.
  <a href="/risk-disclaimer" style="color:#c5a059;">Full disclaimer</a> ·
  <a href="/privacy-policy" style="color:#c5a059;">Privacy</a>
</p>
```

---

# GA4 & tracking

```html
<script>
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: 'generate_lead',
    form_id: 'gameplan',
    page_location: 'thank_you',
    funnel_step: 'gameplan_optin_complete'
  });
</script>
```

| Event | Trigger |
|-------|---------|
| `click_apprentice_cta` | Apprentice button click |
| `video_play` | Optional — video widget play |

---

# Brevo coordination

| Item | Setting |
|------|---------|
| PDF delivery | Brevo Email 0 (not TY page) |
| TY copy tense | **"sending"** not "sent" |
| Tag | `lead_gameplan` on form submit |
| Email 0 subject | `[Alpha Elite] Your Gameplan is ready — start with the 2% rule` |

---

# Elementor form redirect

| Action | Setting |
|--------|---------|
| Redirect | `https://yourdomain.com/gameplan-thank-you` |
| Open in new tab | **Off** |
| Query strings | Do not pass email in URL |

---

# SEO

| Setting | Value |
|---------|-------|
| Robots | `noindex, follow` |
| Title | `Thank You — Alpha Elite Gameplan` |
| Meta description | `Check your email for the Alpha Elite Gameplan PDF.` |

---

# Build checklist

- [ ] Page slug `/gameplan-thank-you` published
- [ ] Minimal header (logo only) · dark `#000000` background
- [ ] **No cyan** `#22d3ee` anywhere on page
- [ ] Gold success icon + step numbers
- [ ] Copy matches `gameplan-thank-you.html` (EN)
- [ ] Sender email matches Brevo FROM address
- [ ] Form redirect tested from homepage + `/gameplan`
- [ ] GA4 `generate_lead` fires once per visit
- [ ] Brevo Email 0 within 5 min of test opt-in
- [ ] Apprentice CTA → `/apprentice`
- [ ] Footer disclaimer + legal links
- [ ] `noindex` set
- [ ] Mobile 390px QA

---

# Vietnamese copy pack (optional geo-target)

| Element | VI |
|---------|-----|
| H1 | Kiểm tra email |
| Sub | Chúng tôi đang gửi **Alpha Elite Gameplan** — framework 2%, SOP hàng ngày, sprint 7 ngày. Nội dung giáo dục. |
| Primary CTA | Xem Khóa Apprentice |
| FAQ signal Q | Đây có phải nhóm tín hiệu không? |

Use WPML/Polylang or separate page — default build is **EN**.

---

*Spec v2.0 — Dark/gold theme. Supersedes cyan v1.0 (`#22d3ee`).*
