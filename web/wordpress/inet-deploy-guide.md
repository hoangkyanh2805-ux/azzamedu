# Deploy WordPress/WooCommerce — iNET OnePortal + hoa-homes.com

> **Domain chính:** `hoa-homes.com`  
> **Panel:** [iNET OnePortal](https://one.inet.vn)  
> **Bot:** Offers/checkout links đã trỏ `https://hoa-homes.com`  
> **HTML source:** `web/wordpress/html/*.html`

---

## Tổng quan kiến trúc

```text
hoa-homes.com (iNET WP-H1 hosting)
  ├── /              → homepage (Alpha Elite dark/gold)
  ├── /gameplan      → lead magnet + Brevo
  ├── /apprentice    → sales $297
  ├── /vip           → sales VIP
  ├── /checkout      → WooCommerce + FunnelKit
  └── /quant-desk    → application form

learn.hoa-homes.com  → LearnHouse (phase sau, subdomain riêng)

Telegram bot (azzam_coursebot)
  └── Thank-you page deep link → t.me/azzam_coursebot?start=order_{id}
```

---

## Phase 1 — iNET OnePortal (ngày 1)

### 1.1 Kiểm tra domain

OnePortal → **Dịch vụ → Tên miền** → `hoa-homes.com` = **Đang hoạt động**

### 1.2 Kiểm tra hosting trial

OnePortal → **Dịch vụ → Hosting** → tìm gói **WP-H1** gắn `hoa-homes.com`

| Nếu thấy | Làm gì |
|----------|--------|
| Hosting Active | Vào **Quản lý** / **cPanel** / **DirectAdmin** |
| Chưa gắn domain | Add domain `hoa-homes.com` vào hosting |
| Chỉ có domain, chưa hosting | Dùng trial WP-H1 đã tạo |

### 1.3 DNS (nếu domain + hosting cùng iNET)

Thường iNET **tự trỏ** khi mua hosting + domain cùng tài khoản.

Nếu site chưa mở → **Tên miền → hoa-homes.com → Bản ghi (DNS)**:

| Type | Host | Value |
|------|------|-------|
| A | `@` | IP hosting (lấy trong panel hosting) |
| A | `www` | IP hosting |
| CNAME | `learn` | (sau) trỏ LearnHouse |

### 1.4 SSL

Panel hosting → **SSL / Let's Encrypt** → bật cho `hoa-homes.com` + `www`

Kiểm tra: `https://hoa-homes.com` không báo "Not secure"

---

## Phase 2 — Cài WordPress (ngày 1)

### Trong panel iNET (WordPress hosting)

1. **WordPress Installer** / **Zozo Website** / **Softaculous**
2. Chọn domain: `hoa-homes.com`
3. Điền:

| Field | Giá trị |
|-------|---------|
| Site name | Alpha Elite |
| Admin user | `ae_admin` (không dùng `admin`) |
| Admin password | mạnh, lưu password manager |
| Admin email | `hoang.xuanhiep1986@gmail.com` |
| Language | English (hoặc VI) |

4. Cài xong → login `https://hoa-homes.com/wp-admin`

### Theme + plugin ngay sau cài

**Theme:** Hello Elementor (cài từ WP repo)

**Plugins (thứ tự):**

| # | Plugin | Bắt buộc MVP |
|---|--------|--------------|
| 1 | Elementor | ✅ |
| 2 | Elementor Pro | ✅ (cần license) |
| 3 | WooCommerce | ✅ |
| 4 | Brevo for WordPress | ✅ Gameplan |
| 5 | Wordfence Security | ✅ |
| 6 | FunnelKit / CartFlows | P1 checkout đẹp |

**Settings → Permalinks:** Post name (`/%postname%/`)

---

## Phase 3 — Dark/gold brand (ngày 2)

1. Copy `web/wordpress/html/alpha-elite-tokens.css`
2. **Appearance → Customize → Additional CSS** → paste
3. Elementor → Site Settings:
   - Colors: `#000000`, `#ffd700`, `#b3b3b3` (xem `elementor-implementation-map.md`)
   - Fonts: Anton (headings) + Montserrat (body)

**Không deploy** `homepage.html` (cyan legacy).

---

## Phase 4 — Pages MVP (ngày 2–4)

| Slug | Build từ | CTA |
|------|----------|-----|
| `/` | `homepage-dark-gold.html` | `#get-gameplan` |
| `/gameplan` | `gameplan-preview.html` | Form → thank you |
| `/gameplan-thank-you` | `gameplan-thank-you.html` | Apprentice CTA |
| `/apprentice` | `apprentice-preview.html` | Add to cart AE-APP-001 |
| `/vip` | `vip-preview.html` | AE-VIP-MON / AE-VIP-YR |

Map chi tiết: `web/wordpress/elementor-implementation-map.md`

---

## Phase 5 — WooCommerce products (ngày 3)

**WooCommerce → Products → Add new**

| Name | SKU | Price | Type |
|------|-----|-------|------|
| Apprentice Operating Course | `AE-APP-001` | $297 | Simple |
| VIP Private Desk — Monthly | `AE-VIP-MON` | $149 | Subscription* |
| VIP Private Desk — Annual | `AE-VIP-YR` | $1,290 | Subscription* yearly |
| DWY Bot & Broker Setup | `AE-DWY-001` | $497 | Simple (bump only) |

\*Cần WooCommerce Subscriptions hoặc FunnelKit subscription — hoặc MVP bán one-time trước.

**Payments → PayPal:** kết nối `hoang.xuanhiep1986@gmail.com`

Test URL (khớp bot):
```
https://hoa-homes.com/checkout/?add-to-cart=AE-APP-001
https://hoa-homes.com/checkout/?add-to-cart=AE-VIP-MON
```

---

## Phase 6 — Thank-you + Telegram bot (ngày 4)

Sau order thành công, thank-you page **bắt buộc** có:

**Headline:** Payment received — one more step

**Body:** Open Telegram to complete onboarding and receive LearnHouse access.

**Button:**
```
https://t.me/azzam_coursebot?start=order_{order_id}
```
(Thay `azzam_coursebot` nếu đổi username bot)

**Compliance line:** Education only — not investment advice.

---

## Phase 7 — Brevo Gameplan (ngày 4)

1. Tạo list `gameplan-leads` trên Brevo
2. Plugin Brevo → connect API
3. Form `/gameplan` + homepage opt-in → list trên
4. Automation: gửi PDF Gameplan (upload asset)

---

## Checklist go-live hoa-homes.com

- [ ] `https://hoa-homes.com` + SSL OK
- [ ] Homepage dark/gold live
- [ ] Gameplan form → Brevo
- [ ] SKU `AE-APP-001`, `AE-VIP-MON`, `AE-VIP-YR` tạo xong
- [ ] PayPal test payment OK
- [ ] Thank-you có nút Telegram bot
- [ ] Bot `.env` `SITE_BASE_URL=https://hoa-homes.com`
- [ ] Bot Offers → checkout không 404
- [ ] Footer risk disclaimer

---

## iNET panel — menu thường gặp

| OnePortal sidebar | Dùng để |
|-------------------|---------|
| **Tên miền → Bản ghi** | DNS A/CNAME |
| **Hosting → Quản lý** | cPanel / WP admin / SSL |
| **Email** | Email @hoa-homes.com (optional) |
| **SSL** | Certificate riêng nếu cần |

---

## Lưu ý gói WP-H1 (2 CPU / 2GB RAM)

Đủ cho MVP + Elementor + WooCommerce traffic thấp. Khi lên VIP members nhiều, cân nhắc upgrade hoặc Cloud VPS.

**Trial 7 ngày:** build xong checkout + 1 test order trước khi hết trial.

---

## Branding: hoa-homes.com vs Alpha Elite

Domain là `hoa-homes.com` nhưng **brand trên site vẫn là Alpha Elite** (title, copy từ HTML preview). Domain chỉ là URL — không cần đổi toàn bộ copy.

Sau này mua `alphaelite.com` → redirect 301 hoặc đổi `SITE_BASE_URL` trong bot.

---

## Liên kết repo

| File | Mục đích |
|------|----------|
| `web/wordpress/html/homepage-dark-gold.html` | Homepage |
| `web/wordpress/elementor-implementation-map.md` | Elementor build map |
| `web/wordpress/pricing-draft-g0.md` | Giá draft |
| `telegram-bot/.env` | Bot URLs |
| `docs/offer_stack.md` | SKU + tiers |
