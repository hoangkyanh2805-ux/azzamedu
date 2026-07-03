# Chuyển sang Elementor + FunnelKit (thanh toán & thu thông tin)

> Domain: `hoa-homes.com`  
> Bot checkout links: `AE-APP-001`, `AE-VIP-MON`, `AE-VIP-YR`

---

## Tổng quan luồng

```text
Homepage (Elementor)     → lead Gameplan form → Brevo
Sales page /offers CTA   → FunnelKit Checkout → WooCommerce order
Thank-you page           → link Telegram bot + email user
Telegram bot             → access status + manual PayPal/crypto
```

| Layer | Tool | Vai trò |
|-------|------|---------|
| Design | Elementor | Sửa homepage bằng **Edit with Elementor** |
| Checkout | **FunnelKit** (CartFlows) | 1-page checkout, order bump, thank-you |
| Payments | WooCommerce + PayPal | Thu tiền, lưu order |
| Lead | Brevo / Elementor form | Email, tên, experience |
| Access | Telegram bot + Supabase | Sau thanh toán |

---

## PHẦN A — Chuyển homepage sang Elementor (Cách B)

### A1. Upload child theme Elementor mode

File: `web/wordpress/import/alpha-elite-child-elementor.zip`

1. **Appearance → Themes → Add New → Upload**
2. Activate **Alpha Elite Child (Elementor)**
3. Theme này **không** có `front-page.php` → WP không override HTML nữa

*(Hoặc giữ theme cũ: File Manager → đổi tên `front-page.php` → `front-page.php.bak`)*

### A2. Import template Elementor

1. **Templates → Saved Templates → Import Templates**
2. Chọn: `web/wordpress/import/elementor-alpha-elite-homepage.json`
3. Import xong → thấy template **Alpha Elite Homepage**

### A3. Tạo page Homepage

1. **Pages → Add New** → Title: `Homepage`
2. **Edit with Elementor**
3. Folder icon → **Templates → My Templates** → insert **Alpha Elite Homepage**
4. **Publish**

### A4. Set trang chủ

**Settings → Reading**

| Setting | Value |
|---------|-------|
| Your homepage displays | **A static page** |
| Homepage | **Homepage** |

### A5. Kiểm tra

- `http://hoa-homes.com/` → dark/gold giống trước
- Đăng nhập admin → vào `/` → thấy **Edit with Elementor**

### A6. CSS

Child theme tự load `alpha-elite-tokens.css`.  
Nếu thiếu style: **Appearance → Customize → Additional CSS** → paste thêm file CSS từ repo.

### A7. Form Gameplan trên homepage

Form HTML trong widget → **đổi sang Elementor Form** (khuyến nghị):

| Field | Type |
|-------|------|
| Email | Email, required |
| First name | Text, required |
| Trading experience | Select |

**Actions → Webhook / Brevo** → list `gameplan-leads`  
Redirect → `/gameplan-thank-you/`

---

## PHẦN B — WooCommerce products (bắt buộc trước FunnelKit)

**Products → Add New** (3 sản phẩm):

| Name | SKU | Price | Type |
|------|-----|-------|------|
| Apprentice Operating Course | `AE-APP-001` | 297 | Simple |
| VIP Private Desk — Monthly | `AE-VIP-MON` | 149 | Simple* |
| VIP Private Desk — Annual | `AE-VIP-YR` | 1290 | Simple* |

\*MVP: bán one-time trước; subscription sau.

**WooCommerce → Settings → General**  
Country + currency USD

**WooCommerce → Settings → Accounts**  
☑ Allow customers to place orders without an account (guest)  
☑ Allow customers to create an account during checkout

→ FunnelKit sẽ thu **email, tên, billing** tại checkout.

---

## PHẦN C — FunnelKit checkout funnel

### C1. Cài plugin

- **FunnelKit** (hoặc CartFlows Pro)
- Activate license

### C2. Tạo funnel — Apprentice

**FunnelKit → Funnels → Add New**

| Step | Type | URL slug |
|------|------|----------|
| 1 | **Checkout** | `checkout-apprentice` |
| 2 | **Thank You** | `thank-you-apprentice` |

**Checkout step:**
- Product: `AE-APP-001` ($297)
- Layout: single column, dark style (match site)
- Fields: Email, First name, Last name (optional), Country
- Payment: PayPal + Card (nếu có Stripe)

**Order bump (optional):**
- `AE-DWY-001` $497 — "DWY Bot & Broker Setup"

**Thank You step:**
- Headline: Payment received — one more step
- Button URL:
  ```
  https://t.me/azzam_coursebot?start=order_{order_id}
  ```
  (FunnelKit dynamic tag: `{order_number}` hoặc custom field — dùng order ID WooCommerce)
- Copy: Complete onboarding in Telegram for LearnHouse access.

### C3. Funnel VIP

Tương tự:
- `checkout-vip-monthly` → `AE-VIP-MON`
- `checkout-vip-annual` → `AE-VIP-YR`
- Thank-you → cùng Telegram deep link

### C4. Gắn CTA homepage / sales page

Trong Elementor homepage, section **Offers**:

| Button | Link |
|--------|------|
| Apprentice | `https://hoa-homes.com/checkout-apprentice/` |
| VIP Monthly | `https://hoa-homes.com/checkout-vip-monthly/` |
| VIP Annual | `https://hoa-homes.com/checkout-vip-annual/` |

Cập nhật `telegram-bot/.env` checkout paths nếu dùng funnel slug thay WooCommerce default cart.

### C5. Redirect WooCommerce cart (optional)

**FunnelKit → Settings**  
Enable: Replace default WooCommerce checkout with funnel

Hoặc giữ URL bot hiện tại:
```
/checkout/?add-to-cart=AE-APP-001
```
→ redirect rule tới funnel checkout URL.

---

## PHẦN D — Thu thông tin user

| Kênh | Data thu | Lưu ở đâu |
|------|----------|-----------|
| Gameplan form | email, name, experience | Brevo list |
| FunnelKit checkout | email, name, billing, order | WooCommerce order |
| Telegram bot | telegram_id, email (proof) | Supabase `members` |
| Thank-you CTA | link bot + order meta | User connects TG |

### WooCommerce → Telegram (phase 2)

Order meta `_ae_telegram_id` khi user mở bot từ thank-you.  
Webhook → `telegram-bot/bot/webhooks/woocommerce.py` (đã có scaffold).

---

## PHẦN E — PayPal

**WooCommerce → Settings → Payments → PayPal**

- Connect business: `hoang.xuanhiep1986@gmail.com`
- Test mode OFF khi live
- Test 1 order $1 product trước

---

## Checklist go-live

- [ ] Child theme Elementor active, không còn `front-page.php` override
- [ ] Homepage = Elementor page, **Edit with Elementor** hiện
- [ ] 3 products SKU đúng
- [ ] Funnel Apprentice + Thank-you + Telegram button
- [ ] PayPal connected
- [ ] Test order → thank-you → mở bot → `/status`
- [ ] Gameplan form → Brevo
- [ ] Tắt Coming Soon

---

## File trong repo

| File | Mục đích |
|------|----------|
| `import/alpha-elite-child-elementor.zip` | Theme CSS only, Elementor editable |
| `import/elementor-alpha-elite-homepage.json` | Import template homepage |
| `import/scripts/build_elementor_homepage_json.py` | Regenerate JSON từ HTML |
| `html/homepage-dark-gold.html` | Source design |

---

## Thứ tự làm hôm nay (90 phút)

1. Upload `alpha-elite-child-elementor.zip` + activate (15 ph)
2. Import JSON + tạo page Homepage + Reading (20 ph)
3. WooCommerce 3 products (20 ph)
4. FunnelKit 1 funnel Apprentice + thank-you (25 ph)
5. Test checkout + bot link (10 ph)
