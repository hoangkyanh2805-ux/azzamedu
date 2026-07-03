# Import nhanh Homepage — không build Elementor thủ công

> **3 phút** upload child theme → full homepage dark/gold từ `homepage-dark-gold.html`

---

## Cách nhanh nhất (khuyến nghị)

### Bước 1 — Zip theme

Zip folder:

```text
web/wordpress/import/alpha-elite-child/
```

→ file `alpha-elite-child.zip` (phải chứa `style.css` ở root zip, không lồng thêm 1 folder nếu WP báo lỗi — nếu lỗi thì zip **nội dung bên trong** folder).

### Bước 2 — Upload WordPress

1. **Appearance → Themes → Add New → Upload Theme**
2. Chọn `alpha-elite-child.zip` → **Install Now → Activate**
3. Parent theme **Hello Elementor** phải đã cài (child theme cần parent)

### Bước 3 — Set homepage

**Settings → Reading**

| Setting | Value |
|---------|-------|
| Your homepage displays | **Your latest posts** (để `front-page.php` tự chạy) |

**HOẶC** nếu muốn static page:

| Setting | Value |
|---------|-------|
| Your homepage displays | A static page |
| Homepage | bất kỳ (child theme `front-page.php` vẫn override root `/`) |

### Bước 4 — Kiểm tra

Mở `https://hoa-homes.com/` → phải thấy full homepage dark/gold (hero, offers, form, FAQ…).

### Bước 5 — Tắt Coming Soon

Elementor / hosting → **tắt Maintenance / Coming soon mode**.

---

## Cách hoạt động

Child theme file `front-page.php` load nguyên `homepage-dark-gold.html` và tự sửa link:

| HTML cũ | WordPress |
|---------|-----------|
| `gameplan-preview.html` | `/gameplan` |
| `apprentice-preview.html` | `/apprentice` |
| `vip-preview.html` | `/vip` |
| `alpha-elite-tokens.css` | theme CSS |

**Không cần** kéo từng widget Elementor.

---

## Sau khi import

| Việc | Ghi chú |
|------|---------|
| Form Gameplan | Đổi `action` sang Brevo / Elementor form sau |
| Trang `/gameplan`, `/apprentice` | Import tương tự (phase 2) |
| WooCommerce | Products SKU vẫn cần tạo |
| Elementor #20 | Xóa hoặc để draft — không dùng |

---

## Cách B — Elementor import 1 widget (nếu không muốn child theme)

1. **Elementor → Templates → Import**
2. Import file `elementor-homepage-html.json`
3. Tạo page mới → Insert template

⚠️ Cách B = 1 khối HTML, khó sửa từng section trong Elementor. **Cách A tốt hơn cho MVP.**

---

## Cách C — Copy HTML vào 1 widget

1. Page → Edit with Elementor
2. 1 Section → **HTML widget**
3. Paste nội dung từ `homepage-body-fragment.html` (nếu có)
4. CSS: paste `alpha-elite-tokens.css` vào Customize → Additional CSS

---

## Troubleshooting

| Lỗi | Fix |
|-----|-----|
| Theme install failed | Zip đúng cấu trúc: `style.css` ở root archive |
| Trang trắng | Bật WP_DEBUG; kiểm tra file `homepage-dark-gold.html` trong theme |
| Không dark/gold | Hard refresh Ctrl+F5 |
| Vẫn Hello Elementor default | Activate **Alpha Elite Child** theme |
| Parent theme missing | Cài **Hello Elementor** trước |

---

## File trong package

```text
alpha-elite-child/
├── style.css
├── functions.php
├── front-page.php          ← loader
├── homepage-dark-gold.html ← source of truth
└── alpha-elite-tokens.css
```
