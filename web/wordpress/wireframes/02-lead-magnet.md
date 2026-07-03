# Wireframe — Lead Magnet (`/gameplan`)

Parent: `landing-page-cro-design.md`  
**HTML preview:** `html/gameplan-preview.html`  
**Elementor:** `elementor-implementation-map.md` §3

**Conversion:** form submit only  
**Nav:** minimal (logo only)

## Section order

| # | Section | CTA | Build |
|---|---------|-----|-------|
| 1 | Centered hero | → `#get-gameplan` | ✅ |
| 2 | What's inside (5 chapters) | — | ✅ |
| 3 | PDF preview mock | — | ✅ |
| 4 | Opt-in form card | Submit | ✅ |
| 5 | For / Not for | — | ✅ |
| 6 | Soft Apprentice link | `/apprentice` | ✅ |
| 7 | Footer disclaimer | — | ✅ |

## Hero copy

**H1:** The Alpha Elite Gameplan  
**Sub:** Free PDF — the 2% rule, daily SOPs, and a 7-day operating sprint.

## Form

Fields: `email`, `first_name`  
Button: `Send me the Gameplan`  
Success: redirect `/gameplan-thank-you`

## Brevo

List: `gameplan-leads` · Tag: `lead_gameplan`
