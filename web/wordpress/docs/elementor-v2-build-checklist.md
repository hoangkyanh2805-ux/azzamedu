# Elementor V2 Build Checklist (Drag-Drop Sections)

Use this checklist to rebuild homepage as true Elementor sections (not one HTML widget).

---

## Fast path MVP (recommended)

For the first launch, use the FunnelKit hero opt-in form as the primary conversion element in the hero section so you avoid extra form setup. Build the rest of the page quickly by following the reference blueprint and section map instead of custom coding each block.

### Recommended approach
- Reuse the hero form from the FunnelKit flow for the main opt-in in the hero section.
- Keep the form fields lean: Email, First Name, Experience.
- Route the form to the same thank-you page / Brevo list used by the funnel.
- Build the remaining sections from the reference package in the same order:
  - Hero
  - Not Signal Group
  - Video
  - What You Learn
  - How It Works
  - Offers
  - Gameplan Form
  - FAQ
  - Final CTA
  - Risk Footer

### Speed rules
- Use native Elementor containers and sections.
- Reuse the dark/gold visual system from the reference assets.
- Copy the content from the existing landing copy docs rather than inventing new messaging.
- Do not over-customize; ship a clean MVP first, then refine after data comes in.

---

## 0) Pre-check (2 minutes)

- Ensure theme is `Alpha Elite Child (Elementor)`.
- Ensure Elementor plugin is active.
- Ensure Coming Soon mode is OFF.
- Keep `docs/offer_stack.md` and `sales/assets/landing-copy.md` open in another tab.

---

## 1) Create page `Homepage v2`

1. WP Admin -> Pages -> Add New
2. Title: `Homepage v2`
3. Click `Edit with Elementor`
4. Page Settings (gear icon, bottom-left):
   - Page Layout: `Elementor Canvas`
   - Hide Title: `Yes`
5. Publish (first save)

---

## 2) Global style setup in Elementor

1. Top-left hamburger -> Site Settings
2. Global Colors:
   - Primary accent: `#ffd700`
   - Background: `#000000`
   - Elevated: `#0f0f0f`
   - Text: `#ffffff`
   - Muted: `#b3b3b3`
3. Typography:
   - Headings: Anton
   - Body: Montserrat
4. Save

---

## 3) Build homepage sections (native containers)

Build each section as a separate Container. Use IDs exactly below.

### Section A: Hero (`hero-main`)
- Structure: 2 columns (content + visual)
- Widgets:
  - Heading (eyebrow)
  - Heading (H1)
  - Text Editor (subhead)
  - 2 Buttons (`Get The 2% Rule Gameplan`, `View Alpha Elite System`)
  - Text Editor (micro risk line)
  - Right column: Image or Inner Container for desk visual

### Section B: Not Signal Group (`not-signal-group`)
- Structure: heading block + 2 cards columns
- Widgets:
  - Heading
  - Text Editor
  - Two Icon List widgets (What we are not / What we are)
  - Text Editor (close line)

### Section C: Video (`video-demo`)
- Structure: heading + Video widget + CTA
- Widgets:
  - Heading
  - Text Editor
  - Video widget (YouTube unlisted)
  - Button (`Get The 2% Rule Gameplan`)

### Section D: What You Learn (`what-you-learn`)
- Structure: heading + 3 columns
- Widgets:
  - Heading
  - Text Editor
  - 3 Icon Box widgets (Risk Framework / Execution SOP / Review Loop)

### Section E: How It Works (`how-it-works`)
- Structure: heading + 4 columns
- Widgets:
  - Heading
  - 4 Icon Box widgets (Step 1..4)
  - Button (`Get The 2% Rule Gameplan`)

### Section F: Offers (`offers`)
- Structure: heading + 3 pricing cards
- Widgets:
  - Heading
  - 3 columns, each:
    - Heading (offer name)
    - Heading/Text (price)
    - Icon List (features)
    - Button
- Button links:
  - Apprentice -> `/checkout-apprentice/`
  - VIP Monthly -> `/checkout-vip-monthly/`
  - VIP Annual -> `/checkout-vip-annual/`

### Section G: Gameplan Form (`get-gameplan`)
- Structure: heading + Form
- Widgets:
  - Heading
  - Text Editor
  - Elementor Form (Email, First Name, Experience)
  - Button label: `Send Me The Gameplan`
  - Risk micro line under form

### Section H: FAQ (`faq`)
- Structure: heading + Accordion
- Widgets:
  - Heading
  - Accordion (6-8 questions from `sales/assets/landing-copy.md`)

### Section I: Final CTA (`final-cta`)
- Structure: centered
- Widgets:
  - Heading
  - Text Editor
  - Button (`Get The 2% Rule Gameplan`)

### Section J: Risk Footer (`risk`)
- Structure: single container
- Widgets:
  - Text Editor (full disclaimer)
  - Optional Nav Menu / links

---

## 4) Copy source for each section

- Use `sales/assets/landing-copy.md` for all headlines/body/FAQ.
- Use canonical CTA labels from `docs/offer_stack.md`:
  - `Get The 2% Rule Gameplan`
  - `Start Apprentice Course`
  - `Start VIP Private Desk`
  - `Submit Quant Desk Application`
  - `Add DWY Setup`
  - `Book 1:1 Review`

---

## 5) Publish and set as front page

1. Click `Update` in Elementor
2. WP Admin -> Settings -> Reading
3. Your homepage displays -> `A static page`
4. Homepage -> `Homepage v2`
5. Save

---

## 6) QA (must pass)

- Open `hoa-homes.com` in Incognito
- Confirm section IDs exist and anchors scroll correctly
- Confirm CTA URLs are live
- Confirm public copy is English (Canada-EU)
- Confirm risk micro line + footer disclaimer present

---

## 7) Next after homepage

- Build `/apprentice` and `/vip` using same native container style.
- Then configure FunnelKit checkout pages to match CTA labels from `docs/offer_stack.md`.

