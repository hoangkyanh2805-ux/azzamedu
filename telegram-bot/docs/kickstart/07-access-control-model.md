# 7 — Access Control Model

## Layers

```text
Layer 1: Telegram identity     telegram_id (Bot API)
Layer 2: Member tier           free | apprentice | vip | quant | inner_circle
Layer 3: Pipeline status       payment_review … access_active_vip
Layer 4: Entitlements          learnhouse | telegram_vip | quant_channel
Layer 5: Human gates           G4 LearnHouse · G5 Telegram VIP
```

---

## Tier → entitlements

| Tier | LearnHouse | VIP Telegram | Quant channel |
|------|:----------:|:------------:|:-------------:|
| Free | — | — | — |
| Apprentice | Apprentice course | — | — |
| VIP | Apprentice + VIP library | ✓ after G5 | — |
| Quant | + Quant modules | ✓ | ✓ after approval |
| Inner Circle | manual | ✓ | manual |

---

## Bot feature access (what UI shows)

| Feature | free | apprentice | vip | quant | inner_circle |
|---------|:----:|:----------:|:---:|:-----:|:------------:|
| `/offers` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `/pay` | ✓ | ✓ | ✓ | ✓ | — |
| `/status` | ✓ | ✓ | ✓ | ✓ | ✓ |
| LH link button | — | when `lh_active` | when `lh_active` | when `lh_active` | manual |
| VIP onboarding | — | — | when paid | — | manual |
| Mini App dashboard | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## Admin RBAC

| Role | telegram_id in | Can |
|------|----------------|-----|
| **User** | — | User commands only |
| **Admin ops** | `ADMIN_TELEGRAM_IDS` | `/admin *` |
| **Owner** | admin list | + config, revoke policy |
| **Moderator** | VIP group admin | Group only — not bot admin |

Bot does **not** grant admin by username alone — numeric ID allowlist only.

---

## Human approval gates

| Gate | Unlocks | Bot may |
|------|---------|---------|
| **G0** | Prices in `/pay` | Show amounts after owner sign-off |
| **G6** | Payment instructions | Show PayPal/crypto addresses |
| **G4** | LearnHouse access claim | Send LH URL after `/admin provisioned` |
| **G5** | VIP group | Send invite text after `/admin tgdone` |
| **G1-bot** | Production bot | Public `/start` |

Bot **cannot** skip G4/G5 at MVP.

---

## Agent permissions (AI layer)

| Action | Bot code | Human |
|--------|----------|-------|
| Store telegram_id | auto | — |
| Confirm payment | — | admin |
| Enroll LearnHouse | — | G4 |
| Add VIP member | — | G5 |
| Broadcast signals | **FORBIDDEN** | — |

See `docs/permission-matrix.md` Telegram section.

---

## Status transitions (allowed)

| From | To | Actor |
|------|-----|-------|
| `lead` | `payment_review` | user submits proof |
| `payment_review` | `payment_confirmed` | admin confirm |
| `payment_confirmed` | `provisioning` | system |
| `provisioning` | `lh_active_apprentice` | admin provisioned |
| `lh_active_*` | `tg_pending` | user submits @username (VIP) |
| `tg_pending` | `access_active_vip` | admin tgdone |
| `*` | `revoked` | admin revoke |

Invalid transitions return error to admin command.

---

## Future: webhook (P2)

WooCommerce `order.completed` may set `payment_confirmed` automatically — VIP Telegram still requires G5.

---

## Acceptance

- [ ] No code path sets `access_active_vip` without admin `tgdone`  
- [ ] Admin IDs configured via env — not in source  
- [ ] Tier labels match offer menu (5 products)
