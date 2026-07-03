# Elementor Implementation Map — Alpha Elite (Landing-Copy First)

> **Source of truth:** `html/*.html` + `alpha-elite-tokens.css`  
> **Stack:** WordPress · Elementor · WooCommerce · FunnelKit · Brevo  
> **Primary agents:** `.ai/agents/landing-copy-agent.md` + `.ai/agents/funnelkit-agent.md`  
> **Rule:** copy must pass Compliance before publish

---

## 0. Fast path (không phụ thuộc wp-admin import)

| Step | File | URL / action |
|------|------|--------------|
| 1 | `import/alpha-elite-child-elementor.zip` | Upload theme → Activate |
| 2 | `import/ae-setup-once.php` + `elementor-alpha-elite-homepage.json` | Upload vào `public_html` |
| 3 | Run | `http://hoa-homes.com/ae-setup-once.php?key=alpha-elite-2026` |
| 4 | `import/ae-setup-products.php` | `http://hoa-homes.com/ae-setup-products.php?key=alpha-elite-2026` |
| 5 | Xóa file setup | Bảo mật |
| 6 | FunnelKit | Build checkout theo `funnelkit-agent.md` |

---

## 1. Landing-Copy Agent Full Pack (copy-paste standard)

This section is the canonical public-copy pack for Canada-EU traffic.  
Use these exact labels and core blocks before custom refinements.

### 1.1 Global copy contract

- **Positioning:** Alpha Elite is a trading operating system, not a signal group.
- **Voice:** Calm, premium, process-first, anti-hype.
- **Promise:** Behavioral/process outcomes only; no guaranteed financial outcome.
- **Language:** Public pages, CTAs, checkout labels, and thank-you copy are English.
- **CTA model:** Use object CTAs only (`Start Apprentice Course`, not `Get Started`).
- **Compliance:** Micro risk line near action + full footer disclaimer.

### 1.2 Canonical offer labels and CTAs

| Offer | SKU | Canonical CTA |
|-------|-----|---------------|
| 2% Rule Gameplan | `AE-GP-000` (internal optional) | `Get The 2% Rule Gameplan` |
| Apprentice Operating Course | `AE-APP-001` | `Start Apprentice Course` |
| VIP Private Desk (Monthly) | `AE-VIP-MON` | `Start VIP Private Desk` |
| VIP Private Desk (Annual) | `AE-VIP-YR` | `Start VIP Private Desk` |
| Quant Desk | `AE-QNT-001` | `Submit Quant Desk Application` |
| DWY Bot & Broker Setup | `AE-DWY-001` | `Add DWY Setup` |
| Inner Circle (1:1) | no public checkout SKU | `Book 1:1 Review` |

### 1.3 Homepage (`/`) master blocks

| Section ID | Copy objective | Mandatory copy direction | CTA |
|------------|----------------|--------------------------|-----|
| `hero-main` | Problem framing | “System over signals” + behavioral outcome | `#get-gameplan` |
| `not-signal-group` | Qualification | “What we are / what we are not” contrast | `#offers` |
| `video-demo` | Mechanism proof | Show workflow, not profit montage | `#offers` |
| `what-you-learn` | Value articulation | 3-6 outcomes tied to SOP/risk/journal | `#offers` |
| `how-it-works` | Clarity | 4-step process from gameplan to desk | `#get-gameplan` |
| `offers` | Decision | Apprentice / VIP Monthly / VIP Annual | checkout URLs |
| `get-gameplan` | Capture | Low-friction form intro + risk micro line | submit |
| `faq` | Objections | Fit, risk, support, timeline, refund | `#offers` |
| `final-cta` | Close | Repeat core thesis + direct next action | `#offers` |

**Approved homepage core lines**
- Hero headline: `You don't need another signal. You need a system that stops emotional trading.`
- Hero subhead: `Education, structured trade process, and accountability around a 2% risk framework.`
- Offer microcopy: `Educational program - not investment advice.`

### 1.4 Apprentice page (`/apprentice`) copy spec

**Hero**
- Headline: process-installation promise (not income promise)
- Subhead: risk, SOP, journal, review cadence
- Primary CTA: `Start Apprentice Course`

**Value stack**
- 5 modules presented by outcome
- Include SOP templates and review workflow

**Objection block**
- Who this is for / not for
- Time expectation and skill-level clarity

**Risk line (mandatory)**
- `Trading involves risk. Educational content only.`

### 1.5 VIP page (`/vip`) copy spec

**Hero**
- Position as continuity desk, not signal room
- Primary CTA: `Start VIP Private Desk`

**Core sections**
- Desk rhythm and accountability cadence
- Structured market context support
- Comparison vs Apprentice (scope, not superiority hype)

**Optional bump cue**
- Mention `Add DWY Setup` as implementation support, not performance booster

### 1.6 Checkout and thank-you microcopy

- Checkout headline: `Complete your enrollment in [Offer Name]`
- Risk line: `Trading involves risk of loss.`
- Required checkbox: `I understand this is educational content, not investment advice.`
- Thank-you CTA: Telegram onboarding deep link with `{order_number}`

### 1.7 Forbidden copy (hard fail)

- Any guaranteed-profit or fixed-return phrasing
- Any “risk-free trading” phrasing
- Any passive-income-from-bot promise
- Any fake scarcity/countdown
- Any PnL brag as primary claim

### 1.8 Landing-copy QA gate

- [ ] Canonical offer labels and CTAs match `docs/offer_stack.md`
- [ ] Public-facing copy is English (Canada-EU standard)
- [ ] One primary CTA per section
- [ ] Risk line near action and full footer disclaimer present
- [ ] Compliance review logged before publish

---

## 2. Page map (HTML → WordPress)

| WP slug | HTML preview | Owner agent | Primary CTA |
|---------|--------------|-------------|-------------|
| `/` | `homepage-dark-gold.html` | Landing Copy + CRO | `#get-gameplan` |
| `/gameplan` | `gameplan-preview.html` | Landing Copy | Form |
| `/gameplan-thank-you` | `gameplan-thank-you.html` | FunnelKit + Landing Copy | Apprentice checkout |
| `/apprentice` | `apprentice-preview.html` | Landing Copy + FunnelKit | `checkout-apprentice` |
| `/vip` | `vip-preview.html` | Landing Copy + FunnelKit | `checkout-vip-*` |
| `/quant-desk` | `quant-desk-preview.html` | Landing Copy | Application form |

---

## 3. Global setup standards

- Colors/fonts: `design-system-dark-gold.md` + `html/alpha-elite-tokens.css`
- Required plugins: Elementor, WooCommerce, FunnelKit (or CartFlows fallback), Brevo
- Theme notes: dùng `alpha-elite-child-elementor`, không dùng legacy `homepage.html` (cyan)

---

## 4. Funnel URLs and SKU truth

| SKU | Offer | Checkout URL |
|-----|-------|--------------|
| AE-APP-001 | Apprentice | `/checkout-apprentice/` |
| AE-VIP-MON | VIP Monthly | `/checkout-vip-monthly/` |
| AE-VIP-YR | VIP Annual | `/checkout-vip-annual/` |
| AE-DWY-001 | DWY setup bump | bump/upsell only |

Bot deep link trên thank-you:

```text
https://t.me/azzam_coursebot?start=order_{order_number}
```

---

## 5. Build order (production)

```text
S0 homepage live via ae-setup-once.php
S1 WooCommerce SKUs via ae-setup-products.php
S2 Apprentice funnel (checkout + thank-you + Telegram)
S3 PayPal connect + sandbox test
S4 Gameplan page + Brevo form
S5 Apprentice/VIP sales pages polish
S6 Web quality + compliance gates
```

---

## 6. Agent routing

| Task | Agent | Output |
|------|-------|--------|
| Page copy draft | Landing Copy Agent | landing blocks + CTA/microcopy |
| Section/wireframe | CRO Agent | structure + form logic |
| Checkout/TY | FunnelKit Agent | funnel setup + test plan |
| Claims/legal | Compliance Agent | PASS/FAIL verdict |
| Performance/accessibility | Web Quality Agent | launch checklist |

---

## 7. Go-live QA checklist

- [ ] Homepage render đúng trên tab ẩn danh (không admin bar)
- [ ] 4 SKU tồn tại đúng giá
- [ ] Apprentice checkout chạy và vào đúng thank-you
- [ ] Telegram deep link mở bot đúng param order
- [ ] Compliance PASS cho homepage + checkout + TY
- [ ] Public-facing copy and checkout labels are English (Canada-EU standard)
- [ ] Mobile 390px không vỡ layout
- [ ] Xóa file setup khỏi server

---

## 8. File index

| Asset | Path |
|-------|------|
| Landing copy contract | `.ai/agents/landing-copy-agent.md` |
| Funnel agent | `.ai/agents/funnelkit-agent.md` |
| One-click homepage | `import/ae-setup-once.php` |
| One-click products | `import/ae-setup-products.php` |
| Elementor JSON | `import/elementor-alpha-elite-homepage.json` |
| Child theme | `import/alpha-elite-child-elementor.zip` |
| Funnel SOP | `docs/funnelkit-elementor-setup.md` |

---

*Implementation map v3.0 — landing-copy-agent full chuẩn + funnel execution.*
