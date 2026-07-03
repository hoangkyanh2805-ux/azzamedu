# PDF Landing Reference → Alpha Elite Section Map

> **Source:** `assets/pdf-landing-ref/` (rendered from `2ad91556-0c48-4f65-a591-dcd77e8ae632.pdf`)  
> **Reference product:** AI CES Workspace course landing (light blue SaaS)  
> **Target:** Alpha Elite homepage — dark/gold · compliance-safe · XAUUSD operating system  
> **Parent:** `landing-page-cro-design.md` · `wireframes/01-homepage.md`

---

## Tổng quan PDF (4 trang)

| Trang | Nội dung chính | Số section |
|-------|----------------|------------|
| 1 | Header · Hero · Before/After · System grid | 4 |
| 2 | Testimonials · Roadmap 6 bước · Results · Outcomes | 4 |
| 3 | Audience grid · Pricing 3 tier · FAQ · Contact CTA | 4 |
| 4 | Footer 3 cột | 1 |

**Layout pattern PDF:** Long-scroll SaaS course page — badge → H1 → dual CTA → trust row → contrast cards → feature grid → timeline → proof → pricing → FAQ → dark CTA band → footer.

**Visual PDF:** White/light-blue, rounded cards, pill badges, navy accent.  
**Alpha Elite adapt:** Giữ **cấu trúc section + rhythm**, đổi skin sang `alpha-elite-tokens.css` (dark/gold). **Không copy** dashboard doanh thu, ROI %, chart lợi nhuận.

---

## Section-by-section analysis & map

### S01 — Sticky Header

| PDF (CES) | Phân tích | Alpha Elite map |
|-----------|-----------|-----------------|
| Logo trái | Brand anchor | `Alpha Elite` logo gold |
| Nav: Khóa học · Lộ trình · Kết quả · Học phí · FAQ · Đăng ký | Anchor scroll | `System` · `How it works` · `Offers` · `FAQ` · `Gameplan` |
| CTA phụ: outline "Xem lộ trình" | Secondary | `View Alpha Elite System` → `#alpha-elite-system` |
| CTA chính: solid "Đăng ký ngay" | Primary | `Get Gameplan` → `#get-gameplan` |

**Section ID:** `site-header` (Theme Builder)  
**Status HTML preview:** ✅ Partial (`ae-header-gold`)  
**Elementor:** Nav Menu + Button widget

---

### S02 — Hero (`#hero-main`)

| PDF element | CES copy pattern | Alpha Elite (approved) |
|-------------|------------------|------------------------|
| Pill badge | "AI Agent CES Global" | `Private XAUUSD operating system` |
| H1 | "Làm chủ AI Agent…" | You Don't Need Another Signal… |
| Subhead | Course outcome promise | Education, structured trade ideas, automation support, SOPs, community accountability |
| Primary CTA | Đăng ký khóa học | **Get The 2% Rule Gameplan** |
| Secondary CTA | Xem lộ trình | **View Alpha Elite System** |
| Trust row (✓) | Online Zoom · Zalo support | 2% Risk Framework · Daily SOP · Private Desk |
| Right visual | Product UI card + stat card (6 buổi, 15h) | **Operating desk mock** (checklist, risk edu) — **không** session/ROI stats |

**Compliance:** Không dùng stat card kiểu "6 sessions = value". Thay bằng desk UI + footnote *UI illustration only*.

**Status HTML preview:** ✅ Done (`homepage-dark-gold.html`)

---

### S03 — Before / After Contrast

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| H2 | "Trước và sau khóa học" | **Signal-group habits vs Operating-system habits** |
| Cột trái (light) | Pain: rời rạc, thủ công, không có hệ thống | **Before:** chasing alerts · no SOP · emotional sizing · no review cadence |
| Cột phải (dark accent) | Gain: workspace, agent, automation | **After:** structured trade ideas (edu) · daily SOP · 2% risk framework · community accountability |

**Section ID:** `#not-signal-group`  
**Layout:** 2-col · left `ae-card` border · right `ae-desk-card-gold` or dark elevated  
**Status:** ❌ Chưa build HTML · ✅ có trong `landing-page-cro-design.md` §1

**Compliance rewrite (tránh outcome promise):**
- ❌ "Sau khóa bạn sẽ kiếm được…"
- ✅ "Sau khi áp dụng framework, bạn có **cấu trúc** để vận hành — kết quả giao dịch vẫn phụ thuộc bạn và có rủi ro."

---

### S04 — System / Feature Grid

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| H2 | "Hệ thống AI CES Workspace" | **Inside the Alpha Elite operating system** |
| Top banner card | Flow diagram 4 bước | **Flow:** Gameplan → Apprentice → VIP Desk → Quant (education path) |
| Row 3 cards | Feature icons (workspace, agent, automation) | **Daily SOP** · **2% Risk Framework** · **Automation support docs** |
| Bottom wide card | "Capstone" project | **Private desk preview** — SOP library + review mode (no P&L) |

**Section ID:** `#system-library`  
**CTA:** Scroll to `#get-gameplan` — "See inside the Gameplan"  
**Status:** ❌ Chưa build HTML

---

### S05 — Methodology + Quote Callout

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| Left list | ✓ checkpoints methodology | ✓ Education-first modules · ✓ SOP templates · ✓ Risk protocol worksheets · ✓ Automation support literacy |
| Right dark box | Bold quote về transformation | **Quote (compliant):** *"Structure replaces guesswork. You still own every trade decision."* |

**Section ID:** `#methodology`  
**Status:** ❌ Chưa build · có thể gộp vào `#how-it-works`

---

### S06 — Testimonials

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| 3 quote cards | Avatar + name + role + quote | **Discipline quotes only** — first name, no P&L |
| Example CES | "Tôi đã tự động hóa báo cáo…" | "I finally run a pre-trade checklist every session." |

**Section ID:** `#testimonials`  
**Subline bắt buộc:** *Education and support — individual results vary. Trading involves risk.*  
**Forbidden:** win rate, profit, "$X made"

**Status:** ✅ Placeholder HTML in `homepage-dark-gold.html` — replace at G1

---

### S07 — Roadmap / Timeline (6 steps)

| PDF step | CES module | Alpha Elite step |
|----------|------------|------------------|
| 01 | Nền tảng AI | **Gameplan** — 2% rule + self-audit |
| 02 | Workspace setup | **Apprentice M1–M2** — mindset + risk protocol |
| 03 | Agent điều phối | **Apprentice M3** — Daily SOPs |
| 04 | Automation | **Apprentice M4** — Automation support literacy |
| 05 | Dashboard / báo cáo | **VIP desk** — structured trade ideas format (edu) |
| 06 | Capstone | **Quant / Inner Circle** — application only |

**Section ID:** `#how-it-works`  
**Layout:** Horizontal timeline (PDF) → Steps widget Elementor · mobile vertical  
**Compliance:** Buổi 5 PDF có "Dashboard doanh thu" → đổi thành **"Weekly review dashboard (journal — not P&L marketing)"**

**Status:** ❌ Chưa build HTML

---

### S08 — Results / Deliverables

| PDF | CES (⚠️) | Alpha Elite (compliant) |
|-----|----------|-------------------------|
| H2 | "Bạn ra về với sản phẩm thật" | **You leave with operating assets — not alerts** |
| Card 1 | Checklist deliverables | ✓ 2% sizing worksheet · ✓ Daily SOP PDF · ✓ 7-day sprint · ✓ Journal template |
| Card 2 | **Dashboard doanh thu + chart + %** | ❌ **BỎ** — thay **SOP checklist UI mock** |
| Card 3 | Report chart | ❌ **BỎ** — thay **Review cadence calendar mock** |

**Section ID:** `#deliverables`  
**Critical compliance:** Không replicate revenue dashboard, growth %, hay "1.2 tỷ" style numbers.

**Status:** ❌ Chưa build HTML

---

### S09 — Outcomes (Checklist + Skill Pills)

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| Left | "Những gì bạn mang về" checklist | **What the Gameplan installs:** habits list (education) |
| Right dark box | Skill pills (tags) | Pills: `Pre-trade SOP` · `2% sizing` · `Weekly review` · `Journal` · `Risk protocol` · `Accountability` |

**Section ID:** `#outcomes`  
**Compliance:** Pills = **skills/habits**, không phải "earn $X" hay "passive income"

**Status:** ❌ Chưa build HTML

---

### S10 — Audience Grid (10 cards)

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| 10 persona cards | Người đi làm, startup, marketing… | **Rút gọn 2 cột** (PDF quá dài cho trading) |
| Tag cloud | Nhiều industry tags | **For:** serious XAUUSD traders · operators wanting structure |
| | | **Not for:** signal chasers · guaranteed-profit seekers |

**Section ID:** `#who-its-for`  
**Layout:** PDF 5×2 grid → Alpha **2-col contrast** (gọn hơn, đủ CRO)

**Status:** ❌ Chưa build · wireframe lead magnet có For/Not for

---

### S11 — Pricing (3 tiers)

| PDF tier | CES | Alpha Elite offer |
|----------|-----|-------------------|
| Left | Cơ bản | **Gameplan** — Free |
| Center (featured) | Pro — "Ưu đãi tốt nhất" | **Apprentice** — featured mid card |
| Right | Enterprise | **VIP** — monthly/annual link |

**Section ID:** `#offers`  
**Note:** Quant + Inner Circle = text links below (không cần 4th card trên homepage)  
**Compliance:** Không "ROI", không fake countdown, giá TBD until G0 pricing gate

**Status:** ❌ Chưa build HTML

---

### S12 — FAQ Accordion

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| ~8 questions | Học online? Hoàn tiền? | Signal group? · Profit guarantee? · What's in Gameplan? · Automation = bot income? · LearnHouse access? |

**Section ID:** `#faq`  
**Mandatory Q:** *Does this guarantee profits?* → **No.**  
**Mandatory Q:** *Is this a signal group?* → **No.**

**Status:** ❌ Homepage HTML · ✅ partial `gameplan-thank-you.html` FAQ

---

### S13 — Dark CTA Band + Contact

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| Dark gradient section | Đăng ký + hotline + email + địa chỉ | **Final CTA:** Get The 2% Rule Gameplan |
| Left card | Registration CTA | Form shortcut hoặc button → `#get-gameplan` |
| Right | Contact list | Support email · Telegram (ops) · **no** "hotline cam kết lời" |

**Section ID:** `#final-cta`  
**Status:** ❌ Chưa build HTML

---

### S14 — Footer

| PDF | CES | Alpha Elite |
|-----|-----|-------------|
| 3 columns | About · Khóa học links · Liên hệ | About · System links · Legal |
| Bottom bar | © 2024 CES Global | © Alpha Elite + **full risk disclaimer** |
| Tagline | Creative - Effective - Sustainable | **Education · Structure · Accountability** |

**Section ID:** `#risk` (footer anchor)  
**Status:** ✅ Partial — disclaimer có, thiếu 3-col links

---

## Master section order (homepage)

Map PDF → Alpha Elite wireframe (merged với `01-homepage.md`):

| # | Section ID | PDF source | Alpha priority | HTML status |
|---|------------|------------|----------------|-------------|
| 1 | `site-header` | S01 | P0 | ✅ partial |
| 2 | `hero-main` | S02 | P0 | ✅ done |
| 3 | `not-signal-group` | S03 | P0 | ✅ |
| 4 | `what-you-learn` | S04 | P0 | ✅ |
| 5 | `methodology` | S05 | P1 | ❌ |
| 6 | `how-it-works` | S07 | P0 | ✅ |
| 6b | `curriculum` | PDF curriculum | P0 | ✅ |
| 7 | `deliverables` | S08 | P1 | ❌ |
| 8 | `outcomes` | S09 | P2 | ❌ |
| 9 | `testimonials` | S06 | P2 | ❌ |
| 10 | `activity-strip` | — | P2 | ❌ (Alpha-only, no PDF) |
| 11 | `video-demo` | — | P2 | ✅ placeholder |
| 12 | `who-its-for` | S10 | P1 | ✅ |
| 13 | `offers` | S11 | P0 | ✅ |
| 14 | `get-gameplan` | S02 CTA repeat | P0 | ✅ done |
| 15 | `faq` | S12 | P0 | ✅ |
| 16 | `final-cta` | S13 | P1 | ❌ |
| 17 | `risk` / footer | S14 | P0 | ✅ partial |

---

## Visual translation (PDF blue → Alpha gold)

| PDF token | CES value | Alpha Elite token |
|-----------|-----------|-------------------|
| Page bg | `#F8FAFC` white | `--ae-bg-base` `#000` |
| Card bg | `#FFFFFF` | `--ae-bg-elevated` / `ae-desk-card-gold` |
| Primary accent | Blue `#2563EB` | Gold gradient `--ae-gold` |
| Dark feature card | Navy `#1E3A5F` | `#141414` + gold border |
| CTA primary | Blue pill button | `.ae-btn-gold` |
| CTA secondary | Outline blue | `.ae-btn-outline` |
| Badge | Light blue pill | `.ae-badge-seal` / `.ae-eyebrow-gold` |
| Border radius | 12–16px | 12px cards · 999px pills |

---

## Compliance: PDF elements → DO NOT port

| PDF element | Lý do | Thay bằng |
|-------------|-------|-----------|
| Dashboard doanh thu + line chart | Implied profit / fixed return | SOP checklist UI |
| % tăng trưởng (+24%) | Performance promise | Module completion / review cadence |
| "Sản phẩm thật" nếu = revenue tool | Misleading for trading edu | "Operating assets (templates, SOPs)" |
| "AI Agent tự động…" hype | Passive automation promise | "Automation support — you own decisions" |
| Pricing "ROI" badges | Fixed return | Feature checklist only |
| Testimonial nói về tiền | Member profit claim | Discipline / structure quotes |

---

## Copy stubs (ready for Elementor)

### S03 — Not a signal group

**H2:** Not a signal group. An operating system.

| Signal-group habits | Operating-system habits |
|---------------------|-------------------------|
| Chasing entries from alerts | Structured trade ideas inside SOPs (education) |
| Random position sizing | 2% risk management framework |
| No journal or review | Daily SOP + weekly accountability |
| Isolated guessing | Community accountability |

### S07 — How it works (timeline labels)

1. **Gameplan** — Free PDF · 2% rule + 7-day sprint  
2. **Apprentice** — LearnHouse modules · SOP install  
3. **VIP Desk** — Private channel · structured ideas (edu)  
4. **Quant** — Application · desk workflows (edu)

### S11 — Offers (card headlines)

| Tier | Headline | CTA |
|------|----------|-----|
| Gameplan | Start with structure — free | Get Gameplan |
| Apprentice | Install the operating habits | Enroll |
| VIP | Run your private desk | Join VIP |

---

## Implementation handoff

| Deliverable | File |
|-------------|------|
| Section map (this doc) | `pdf-landing-section-map.md` |
| Wireframe order | `wireframes/01-homepage.md` |
| Hero + opt-in spec | `elementor-spec-homepage-hero-optin.md` |
| HTML preview (P0) | `html/homepage-dark-gold.html` |
| PDF page images | `assets/pdf-landing-ref/page-1..4.png` |
| Compliance rules | `compliance-copy-audit.md` |

**Next build sprint:** S03 → S04 → S07 → S11 → S12 → S15 (sections chưa có trong HTML preview).

---

*Mapped from CES AI Workspace PDF reference — structure only; Alpha Elite copy and compliance per `docs/compliance_guardrails.md`.*
