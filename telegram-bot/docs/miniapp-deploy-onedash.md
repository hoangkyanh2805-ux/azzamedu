# Deploy Mini App Shop — LearnHouse VPS (chi tiết)

> **URL đích:** `https://learn.azzamedu.com/miniapp/`  
> **VPS:** `162.4.176.43` · iNET OneDash  
> **Lỗi hiện tại:** LearnHouse 404 = chưa có file static tại `/miniapp/`

---

## Tổng quan luồng

```text
Supabase (catalog)     Mini App HTML (VPS)        Telegram Bot
      │                       │                        │
      │  anon key             │  /miniapp/index.html   │  WebAppInfo URL
      └───────────────────────┴────────────────────────┘
                              │
                    MainButton → hoa-homes.com checkout
```

| Đã xong | Chưa xong |
|---------|-----------|
| Supabase migration + seed | Upload `miniapp/` lên VPS |
| `miniapp/js/config.js` (anon key) | Nginx `location /miniapp/` |
| Bot `/shop` inline (4 danh mục) | Bật lại `miniapp_shop_url` |

---

## Bước 0 — Vào được VPS (fix OneDash 504)

Screenshot OneDash có thể hiện **port 24788**; runbook deploy cũ dùng **24700**. **Lấy port đúng từ OneDash → Máy chủ → chi tiết VPS** (dòng lệnh SSH họ hiển thị).

### Nếu Terminal OneDash báo `504` / Kết nối thất bại

1. **OneDash → Tổng quan** — VPS phải **Đang chạy** (không bị tắt / hết hạn).
2. **Thử lại** sau 1–2 phút (gateway OneDash đôi khi timeout).
3. **Đổi port** nếu panel ghi `24788` thay vì `24700`.
4. **Reboot VPS** từ OneDash (Tổng quan → Khởi động lại) → đợi 2 phút → mở Terminal lại.
5. **SSH từ Windows** (thay Terminal web):

```powershell
ssh root@162.4.176.43 -p 24700
# hoặc port OneDash hiển thị, ví dụ:
# ssh root@162.4.176.43 -p 24788
```

Mật khẩu: email iNET khi tạo VPS hoặc reset trong OneDash → Máy chủ → Mật khẩu.

6. **Quản lý File** (OneDash sidebar): upload file nếu Terminal vẫn lỗi — xem Bước 2B.

---

## Bước 1 — Chuẩn bị file trên máy Windows

Trong repo:

```text
telegram-bot/scripts/onedash-install-miniapp.sh   ← script cài 1 lần (đã build sẵn)
telegram-bot/miniapp/                             ← source HTML/CSS/JS
```

Nếu sửa `miniapp/` sau này, build lại script:

```powershell
cd telegram-bot
python scripts/build-onedash-miniapp-bundle.py
```

---

## Bước 2A — Cài qua Terminal (khuyến nghị)

### 2A.1 Mở script trên máy

Mở `telegram-bot/scripts/onedash-install-miniapp.sh` trong Cursor/Notepad.

### 2A.2 Copy toàn bộ

`Ctrl+A` → `Ctrl+C` (từ dòng `#!/bin/bash` đến hết).

### 2A.3 Paste vào VPS

**Cách 1 — OneDash Terminal:** paste → Enter.

**Cách 2 — SSH PuTTY / Windows Terminal:** sau khi `ssh root@...` thành công, paste → Enter.

Script tự làm:

- Giải nén file vào `/var/www/alpha-elite-miniapp/`
- Thêm `location /miniapp/` vào nginx LearnHouse
- Mount volume trong `docker-compose.yml`
- `docker compose up -d --force-recreate nginx`

### 2A.4 Kỳ vọng output cuối

```text
DONE: https://learn.azzamedu.com/miniapp/
nginx: the test is successful
```

---

## Bước 2B — Nếu Terminal không paste được (File Manager)

1. OneDash → **Quản lý File** → thư mục `/root/`
2. Upload `onedash-install-miniapp.sh`
3. Mở Terminal (hoặc SSH) chạy:

```bash
chmod +x /root/onedash-install-miniapp.sh
bash /root/onedash-install-miniapp.sh
```

---

## Bước 2C — Deploy từ Windows (khi SSH local OK)

```powershell
cd "G:\Other computers\My Computer\Project\webkhoahoc\telegram-bot"
python scripts/deploy-miniapp-vps.py
```

Cần `web/learnhouse/scripts/deploy-production.env` có `VPS_PASSWORD` và **đúng `VPS_PORT`**.

---

## Bước 3 — Kiểm tra sau deploy

Trên VPS:

```bash
curl -sI https://learn.azzamedu.com/miniapp/ | head -5
ls -la /var/www/alpha-elite-miniapp/
```

| Kết quả | Ý nghĩa |
|---------|---------|
| `HTTP/2 200` + `content-type: text/html` | OK |
| `404` + trang LearnHouse | Nginx chưa route `/miniapp/` — chạy lại script hoặc sửa tay |
| `502/504` | Container nginx/app chưa lên — `docker ps` |

Trên trình duyệt (không cần Telegram):

`https://learn.azzamedu.com/miniapp/`

Phải thấy **Alpha Elite Shop** + 4 danh mục (không phải LearnHouse 404).

---

## Bước 4 — Bật nút 📱 trong bot

Sửa `telegram-bot/config.yaml`:

```yaml
site:
  miniapp_shop_url: ${MINIAPP_SHOP_URL}
```

`.env` đã có:

```env
MINIAPP_SHOP_URL=https://learn.azzamedu.com/miniapp/
```

Restart bot:

```powershell
cd telegram-bot
# dừng bot cũ nếu đang chạy
python -m bot.main
```

Telegram: `/shop` → nút **📱 Mở Shop App** (trên 4 danh mục).

---

## Bước 5 — BotFather (tùy chọn)

`@BotFather` → bot → **Bot Settings** → **Configure Mini App** → URL:

```text
https://learn.azzamedu.com/miniapp/
```

Giúp mở shop từ menu bot / attachment menu.

---

## Sửa nginx thủ công (nếu script WARN)

Tìm thư mục LearnHouse:

```bash
docker ps | grep nginx
COMPOSE_DIR=$(docker inspect <nginx_container_name> --format '{{index .Config.Labels "com.docker.compose.project.working_dir"}}')
nano $COMPOSE_DIR/extra/nginx.prod.conf
```

Thêm **trong block `server` listen 443**:

```nginx
location /miniapp/ {
    alias /var/www/alpha-elite-miniapp/;
    index index.html;
}
```

Thêm volume trong `docker-compose.yml` (service `nginx`):

```yaml
- /var/www/alpha-elite-miniapp:/var/www/alpha-elite-miniapp:ro
```

```bash
cd $COMPOSE_DIR && docker compose up -d --force-recreate nginx
docker exec <nginx_container> nginx -t
```

---

## Troubleshooting

| Triệu chứng | Nguyên nhân | Fix |
|-------------|-------------|-----|
| LearnHouse **404** trong Telegram | Chưa deploy `/miniapp/` | Bước 2 |
| OneDash Terminal **504** | Gateway / VPS sleep / sai port | Bước 0 |
| Shop trống / lỗi catalog | Anon key hoặc RLS | Kiểm tra `config.js` + migration 003 |
| Nút 📱 không hiện | `miniapp_shop_url` comment | Bước 4 |
| Pay mở browser đúng | Bình thường | FunnelKit trên hoa-homes.com |

---

## Checklist go-live Mini App

- [ ] `curl -I https://learn.azzamedu.com/miniapp/` → 200
- [ ] Browser thấy 4 category + giá
- [ ] `config.yaml` bật `miniapp_shop_url`
- [ ] Bot restart
- [ ] `/shop` → 📱 mở được shop (không 404)
- [ ] Chọn offer → MainButton → checkout Woo
