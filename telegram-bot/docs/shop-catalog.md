# Shop Catalog — Woo → Supabase → Bot (Model B)

> **Flow:** WooCommerce (giá/SKU thật) → `sync-woo-catalog.py` → Supabase → bot `/menu`

## Architecture

```text
WooCommerce (hoa-homes.com)     ← chủ: giá, SKU, publish
        │
        │  python scripts/sync-woo-catalog.py
        ▼
Supabase offers + shop_categories  ← chủ: bot display + tele metadata
        │
        │  catalog.source: supabase
        ▼
Telegram bot /menu
```

| Sửa ở đâu | Việc |
|-----------|------|
| **WooCommerce** | Giá, tên sản phẩm, publish/unpublish |
| **sync-rules.yaml** | Map SKU → category tele, emoji, kind |
| **Supabase** (tùy chọn) | `display_name`, `sort_order`, `active_on_bot=false` |
| **config.yaml** | `catalog.source`, secrets, site URL |

## Setup (one-time)

### 1. Supabase migration

Run in SQL Editor:

`database/migrations/002_shop_catalog.sql`

### 2. WooCommerce REST API keys

WP Admin → WooCommerce → Settings → Advanced → REST API → Add key (Read)

Add to `.env`:

```env
WC_API_URL=https://hoa-homes.com/wp-json/wc/v3
WC_CONSUMER_KEY=ck_...
WC_CONSUMER_SECRET=cs_...
```

### 3. Enable Supabase catalog in config.yaml

```yaml
catalog:
  source: supabase

database:
  provider: supabase
```

### 4. First sync

```bash
cd telegram-bot
python scripts/sync-woo-catalog.py
python scripts/sync-woo-catalog.py --dry-run   # preview only
```

### 5. Restart bot

```bash
python -m bot.main
```

Log should show: `source=supabase`

## Files

| File | Role |
|------|------|
| `sync-rules.yaml` | Categories + SKU tele metadata |
| `scripts/sync-woo-catalog.py` | Woo REST → Supabase upsert |
| `bot/catalog.py` | Load from Supabase or yaml fallback |
| `database/migrations/002_shop_catalog.sql` | `shop_categories` + offer columns |
| `database/migrations/003_miniapp_public_read.sql` | Anon read for Mini App |
| `miniapp/` | HTML shop + Supabase REST — see `miniapp/README.md` |

## Cron (recommended)

Every 15–60 minutes on server:

```bash
python scripts/sync-woo-catalog.py
```

Or after editing products in Woo Admin.

## Commands

| Command | Action |
|---------|--------|
| `/menu` `/shop` | Shop from Supabase |
| `python scripts/sync-woo-catalog.py` | Pull Woo → Supabase |

## Related

- `docs/offer-menu-map.md`
- `../../docs/offer_stack.md`
