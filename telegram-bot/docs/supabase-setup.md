# Supabase Setup — Alpha Elite Telegram Bot

Hướng dẫn wire Supabase từ zero → test connection → chạy bot production-safe.

---

## Tổng quan

| Thành phần | Vai trò |
|------------|---------|
| `database/schema_supabase.sql` | Tạo bảng members, queue, tickets |
| `.env` | `DATABASE_URL` + `SUPABASE_SERVICE_KEY` |
| `config.yaml` | `database.provider: supabase` |
| `scripts/test_supabase.py` | Test CRUD trước khi bật bot |

Bot dùng **service_role key** server-side qua PostgREST. Không dùng anon key trong bot.

---

## Bước 1 — Tạo Supabase project

1. Vào [https://supabase.com/dashboard](https://supabase.com/dashboard)
2. **New project** → đặt tên `alpha-elite-bot`
3. Chọn region gần user (Singapore / Tokyo nếu VN)
4. Đặt database password → **Save password** (dùng cho SQL admin, không paste vào bot)

Đợi project status = **Active** (~2 phút).

---

## Bước 2 — Chạy schema SQL

1. Supabase Dashboard → **SQL Editor** → **New query**
2. Mở file repo: `telegram-bot/database/schema_supabase.sql`
3. Copy toàn bộ → Paste → **Run**

Kỳ vọng: `Success. No rows returned` (hoặc seed offers OK).

### Kiểm tra bảng

**Table Editor** phải thấy:

- `members`
- `provision_queue`
- `support_tickets`
- `audit_log`
- `offers` (5 rows seed)

Nếu lỗi `type already exists` → schema đã chạy rồi, bỏ qua.

---

## Bước 3 — Lấy credentials

### Project URL

**Project Settings → API → Project URL**

```
https://abcdefghijklmnop.supabase.co
```

→ gán vào `.env` key `DATABASE_URL`

### Service role key

**Project Settings → API → service_role** (secret)

⚠️ **Không** dùng `anon` key.  
⚠️ **Không** commit key lên git.  
⚠️ Chỉ chạy trên server / máy dev của bạn.

→ gán vào `.env` key `SUPABASE_SERVICE_KEY`

---

## Bước 4 — Cấu hình bot

### `.env`

```env
DATABASE_URL=https://YOUR_PROJECT.supabase.co
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Giữ nguyên `TELEGRAM_BOT_TOKEN` và `ADMIN_TELEGRAM_IDS`.

### `config.yaml`

```yaml
database:
  provider: supabase
```

**Trước khi test xong**, có thể để `memory`. Sau khi test PASS → đổi sang `supabase`.

---

## Bước 5 — Test connection

```powershell
cd telegram-bot
python scripts/test_supabase.py
```

### Output mong đợi

```text
OK  : Connected. offers table readable (3 sample rows).
OK  : Member upserted tg:999999999 ...
OK  : Queue created: AE-2026-0001
OK  : Queue status -> payment_confirmed
OK  : init_store() selected SupabaseStore
ALL TESTS PASSED
```

Xóa data test:

```powershell
python scripts/test_supabase.py --cleanup
```

### Lỗi thường gặp

| Lỗi | Nguyên nhân | Cách fix |
|-----|-------------|----------|
| `401 Unauthorized` | Sai key hoặc dùng anon key | Dùng **service_role** |
| `404` trên `/members` | Chưa chạy schema | Chạy lại `schema_supabase.sql` |
| `DATABASE_URL must be Supabase project URL` | Dán nhầm `postgresql://...` | Dùng URL dạng `https://xxx.supabase.co` |
| `permission denied` / RLS | Hiếm với service_role | Kiểm tra key đúng service_role |
| `Expected SupabaseStore but got MemoryStore` | `config.yaml` vẫn `memory` | Đổi `provider: supabase` |

---

## Bước 6 — Bật bot với Supabase

1. `config.yaml` → `database.provider: supabase`
2. Restart bot:

```powershell
python -m bot.main
```

Log kỳ vọng:

```text
Database backend: SupabaseStore
Alpha Elite Access Bot starting (polling)
```

3. Telegram: `/start` → kiểm tra **Table Editor → members** có row mới

---

## Luồng data sau khi wire

```text
/start
  → upsert members (telegram_id)

Payment proof
  → insert provision_queue
  → update members.status = payment_review

/confirm AE-...
  → update queue + member status
  → push user "payment confirmed"

/provisioned AE-...
  → status lh_active_*
  → push LearnHouse template

/tgdone AE-...
  → status access_active_vip
  → tier vip
```

---

## Bảo mật

- [ ] `service_role` chỉ trong `.env` / server env
- [ ] `.env` và `config.yaml` trong `.gitignore`
- [ ] Không expose Supabase qua Mini App client trực tiếp (MVP)
- [ ] Rotate key nếu lỡ leak

---

## Rollback về memory (dev)

```yaml
database:
  provider: memory
```

Restart bot — data Supabase vẫn giữ trên cloud.

---

## Checklist go-live

- [ ] Schema chạy OK
- [ ] `python scripts/test_supabase.py --cleanup` PASS
- [ ] `database.provider: supabase`
- [ ] `/start` tạo row trong `members`
- [ ] Payment proof tạo row trong `provision_queue`
- [ ] Admin `/queue` thấy item sau restart bot
