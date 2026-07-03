# Design System — Dark / Gold (từ reference image)

> Map visual từ hình reference → Alpha Elite landing · Elementor + CSS  
> Reference: `assets/reference-dark-gold-hero.png`

---

## Image → Token map

| Element trong hình | Alpha Elite token | Hex / value |
|--------------------|-------------------|-------------|
| Nền đen tuyền | `--ae-bg-base` | `#000000` |
| Nền card / bubble | `--ae-bg-elevated` | `#0a0a0a` → `#141414` gradient |
| Panel tối | `--ae-bg-panel` | `#1a1a1a` |
| Gold headline | `--ae-gold` | `#FFD700` |
| Gold muted / metallic | `--ae-gold-muted` | `#C5A059` |
| Gold deep | `--ae-gold-deep` | `#B8860B` |
| Glow amber | `--ae-glow` | `#F59E0B` |
| Glow soft | `--ae-glow-soft` | `rgba(234, 179, 8, 0.2)` |
| Text chính | `--ae-text` | `#FFFFFF` |
| Text phụ | `--ae-muted` | `#B3B3B3` |
| Disclaimer | `--ae-disclaimer` | `#8A8A8A` |
| Viền pill trắng | `--ae-border-pill` | `rgba(255,255,255,0.85)` |
| Viền subtle | `--ae-border` | `rgba(255,255,255,0.1)` |
| Chart watermark | `--ae-chart-opacity` | `0.06` – `0.12` |

---

## Typography map

| Vai trò trong hình | Font Google | Elementor global | CSS |
|-------------------|-------------|------------------|-----|
| Headline GOLD caps | **Anton** hoặc Bebas Neue | Primary Heading | `font-family: 'Anton', sans-serif` |
| Logo / eyebrow | Montserrat 500 | Secondary | `letter-spacing: 0.2em; uppercase` |
| Body / sub | **Montserrat** hoặc Inter | Text | `font-weight: 400–500` |
| Price / CTA bold | Montserrat 700 | Accent | `font-weight: 700` |

### Google Fonts import

```html
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Headline style (giống hình)

```css
.hero-title {
  font-family: 'Anton', 'Bebas Neue', Impact, sans-serif;
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: 400;
  text-transform: uppercase;
  line-height: 0.92;
  letter-spacing: -0.02em;
  background: linear-gradient(180deg, #FFD700 0%, #EAB308 45%, #B8860B 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  filter: drop-shadow(0 0 12px rgba(255, 215, 0, 0.25));
}
```

---

## Background map

### Layer 1 — Base

```css
background-color: #000000;
```

### Layer 2 — Candlestick watermark (mờ, giống hình)

Dùng SVG pattern hoặc image overlay `opacity: 0.08`, `mix-blend-mode: luminosity`.

```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url('../assets/chart-watermark.svg');
  background-size: cover;
  background-position: center;
  opacity: 0.08;
  pointer-events: none;
  z-index: 0;
}
```

**Elementor:** Section → Background → Image → overlay opacity 8–12%.

### Layer 3 — Radial gold glow (behind hero visual)

```css
background-image:
  radial-gradient(ellipse 55% 45% at 75% 45%, rgba(245, 158, 11, 0.22) 0%, transparent 65%),
  radial-gradient(ellipse 40% 30% at 20% 80%, rgba(234, 179, 8, 0.08) 0%, transparent 60%);
```

---

## UI components từ hình → Alpha Elite (compliant)

| Hình gốc | Dùng cho Alpha Elite | Compliance note |
|----------|----------------------|-----------------|
| Pill border subhead | ✅ Subhead / positioning line | OK |
| Gold headline | ✅ Hero H1 gradient | OK |
| Price bubbles $10/$30 | ⚠️ → **Tier cards** Apprentice/VIP | Không fake urgency date |
| PRE-ORDER wax seal | ⚠️ → **Badge** "Operating System" | Không "pre-order profit" |
| 3D gold coins | ❌ **Bỏ** | Gợi ý lợi nhuận — thay desk UI |
| Hand + phone chart | ✅ Hero visual | Chart = education, không P&L flex |
| Logo top-left | ✅ Alpha Elite logo | — |

---

## Component CSS (copy Elementor HTML widget)

### Pill subhead (như hình)

```css
.pill-message {
  display: inline-block;
  border: 1px solid rgba(255, 255, 255, 0.85);
  border-radius: 999px;
  padding: 12px 24px;
  color: #ffffff;
  font-size: 0.95rem;
  line-height: 1.5;
  max-width: 520px;
}
```

### Price / tier bubble (adapted)

```css
.tier-bubble {
  width: 88px;
  height: 88px;
  border-radius: 50%;
  background: linear-gradient(180deg, #222222 0%, #000000 100%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
}
.tier-bubble::after {
  content: '';
  position: absolute;
  bottom: 8px;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 8px;
  border-bottom: 3px solid #FFD700;
  border-radius: 0 0 50% 50%;
}
.tier-bubble .price {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 1.25rem;
  color: #fff;
}
```

### Primary button (gold solid)

```css
.btn-gold {
  background: linear-gradient(180deg, #FFD700 0%, #EAB308 100%);
  color: #000000;
  font-weight: 700;
  border: none;
  border-radius: 8px;
  padding: 14px 32px;
  box-shadow: 0 4px 20px rgba(234, 179, 8, 0.35);
}
.btn-gold:hover {
  background: linear-gradient(180deg, #FFE566 0%, #FFD700 100%);
  box-shadow: 0 6px 28px rgba(234, 179, 8, 0.45);
}
```

### Seal badge (thay PRE-ORDER)

```css
.badge-seal {
  display: inline-flex;
  align-items: center;
  padding: 8px 16px;
  background: linear-gradient(135deg, #C5A059, #FFD700);
  color: #000;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.4);
}
/* Text: "FREE GAMEPLAN" hoặc "OPERATING SYSTEM" — không PRE-ORDER profit */
```

### Desk card (thay phone + coins)

Giữ card UI operating desk — nền `#141414`, viền gold mờ:

```css
.desk-card-gold {
  background: linear-gradient(145deg, #141414, #0a0a0a);
  border: 1px solid rgba(255, 215, 0, 0.15);
  border-radius: 16px;
  box-shadow:
    0 25px 60px rgba(0, 0, 0, 0.7),
    0 0 40px rgba(245, 158, 11, 0.12);
}
```

---

## Elementor global settings

| Setting | Value |
|---------|-------|
| Default colors Primary | `#FFD700` |
| Default colors Secondary | `#000000` |
| Default colors Text | `#FFFFFF` |
| Default colors Accent | `#EAB308` |
| Body font | Montserrat 16px |
| H1 font | Anton 52px uppercase |
| Button border radius | 8px |
| Button background | Gold gradient |
| Button text | `#000000` |

### Section hero (Elementor)

- Background: `#000000` + custom CSS radial glow  
- Column gap: 48px  
- Right column: Image widget (phone mock) **hoặc** HTML desk card  
- Motion: fade-up desktop only  

---

## File assets trong repo

| File | Mục đích |
|------|----------|
| `html/alpha-elite-tokens.css` | CSS variables + utilities |
| `html/homepage-dark-gold.html` | Preview full theme |
| `assets/reference-dark-gold-hero.png` | Reference gốc |

---

## Alpha Elite compliance khi dùng theme này

**Giữ:** dark luxury, gold accent, chart texture, pill subhead, premium typography  

**Không copy từ hình:**
- Floating coins / motion blur money  
- % profit / guaranteed entries headline  
- Fake countdown pre-order pressure  
- P&L screenshot trên phone  

**Luôn có:** disclaimer micro dưới hero + footer risk warning  

---

## Quick swap: cyan → gold

Trong `homepage.html` cũ, thay:

| Cũ (cyan desk) | Mới (gold ref) |
|----------------|----------------|
| `--accent: #22d3ee` | `--accent: #FFD700` |
| cyan radial glow | amber radial glow |
| Inter only H1 | Anton H1 gradient |
| `.btn-primary` cyan | `.btn-gold` |

Dùng file `homepage-dark-gold.html` làm preview chính.
