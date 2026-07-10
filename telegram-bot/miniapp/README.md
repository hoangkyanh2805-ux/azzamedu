# Alpha Elite Shop — Telegram Mini App

Static HTML shop đọc catalog từ **Supabase** (Model B) + **BottomButton** checkout.

## Files

```text
miniapp/
├── index.html
├── css/shop.css
├── js/
│   ├── config.example.js   # copy → config.js
│   ├── catalog.js          # Supabase REST + fallback
│   └── app.js              # UI + MainButton / SecondaryButton
└── README.md
```

## Setup

### 1. Supabase public read

Run in SQL Editor:

`database/migrations/003_miniapp_public_read.sql`

Lấy **anon key** (Settings → API → `anon` `public`) — **không** dùng `service_role` trong browser.

### 2. Config

```bash
cd telegram-bot/miniapp
copy js\config.example.js js\config.js
```

Edit `js/config.js`:

```javascript
window.SHOP_CONFIG = {
  supabaseUrl: "https://YOUR_PROJECT.supabase.co",
  supabaseAnonKey: "eyJ...",
  siteBaseUrl: "https://hoa-homes.com",
  gameplanPath: "/gameplan",
};
```

### 3. Host HTTPS

Telegram chỉ mở Mini App qua **HTTPS**. Gợi ý:

| Host | URL ví dụ |
|------|-----------|
| LearnHouse VPS | `https://learn.hoa-homes.com/miniapp/` |
| Cloudflare Pages | deploy folder `miniapp/` |

### 4. BotFather

`@BotFather` → your bot → **Configure Mini App** → URL trỏ `index.html`.

### 5. Bot inline button (optional)

Thêm vào `config.yaml`:

```yaml
site:
  miniapp_shop_url: https://learn.hoa-homes.com/miniapp/
```

Bot có `shop_webapp_keyboard()` trong `bot/keyboards/menus.py`.

## Local UI dev (không trong Telegram)

```bash
cd miniapp
python -m http.server 8080
```

Mở `http://localhost:8080` — dùng **fallback catalog** nếu chưa có `config.js`. Telegram WebApp API không có; nút bottom không hiện.

## Flow

```text
Supabase shop_categories + offers
        ↓
Mini App list → detail
        ↓
MainButton → openLink(FunnelKit checkout)
SecondaryButton → back to category
```

Giá/SKU từ Woo sync (`scripts/sync-woo-catalog.py`). Xem [docs/shop-catalog.md](../docs/shop-catalog.md).

## Related

- [docs/mini-app-bottom-button.md](../docs/mini-app-bottom-button.md)
- [docs/shop-catalog.md](../docs/shop-catalog.md)
