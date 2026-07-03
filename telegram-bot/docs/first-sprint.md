# First Sprint — Telegram Access Bot (Weeks 1–2)

> Aligns with `kickstart/08-sprint-roadmap.md` S0 + S1  
> **Sprint goal:** Polling dev bot with `/start`, `/offers`, `/pay`, `/status`, admin notifications.

---

## Week 1 — S0 Foundation

| # | Task | Output | Verify |
|---|------|--------|--------|
| 1.1 | Read kickstart `01` + `11` | Team aligned | Mission signed |
| 1.2 | BotFather: create bot | Token in `.env` | `getMe` OK |
| 1.3 | Choose Supabase **or** Sheets | Decision in `09-backlog` | Connection test |
| 1.4 | Apply schema | Tables/sheets | Insert test member |
| 1.5 | `config.yaml` from example | Local config | URLs valid |
| 1.6 | `handlers/start.py` + disclaimer | `/start` | Disclaimer visible |
| 1.7 | Main menu keyboard | 6 buttons | All route |

**Week 1 exit:** `/start` registers `telegram_id` in DB.

---

## Week 2 — S1 User flows

| # | Task | Output | Verify |
|---|------|--------|--------|
| 2.1 | `handlers/offers.py` — 5 products | Inline keyboard | Links open |
| 2.2 | `handlers/status.py` — 5 tier labels | Status text | Mock tiers |
| 2.3 | `handlers/pay.py` + proof FSM | Queue row | Row in DB |
| 2.4 | `notify.py` → admin chat | Push message | Admin receives <5s |
| 2.5 | `handlers/support.py` | Ticket | Admin notified |
| 2.6 | `handlers/link.py` | Email on member | `/link test@x.com` |
| 2.7 | Draft all `bot/templates/*.md` | 8 templates | Self-check compliance |
| 2.8 | Compliance review | PASS log | `11-compliance-checklist` |

**Week 2 exit:** Journey B/C from `04-user-journey.md` works on dev bot.

---

## Dependencies

| Blocker | Unblocks |
|---------|----------|
| G0 pricing | Live `/pay` amounts (can use draft for dev) |
| G6 payment accounts | Production PayPal/crypto text |
| G3 WooCommerce | Real order IDs in tests |

---

## Not in this sprint

- Admin `/admin` commands (Week 3 / S2)  
- Production deploy (Week 4 / S3)  
- Mini App (S4)  
- WooCommerce webhook (P2)  

---

## Daily standup questions

1. What queue rows are open?  
2. Any compliance copy changes?  
3. Blocked on G0/G6/G3?  

---

## Sprint review criteria

- [ ] All Week 1–2 tasks in `09-backlog` Now/Next marked Done or moved  
- [ ] Demo recorded: start → offers → pay proof → admin notify  
- [ ] No P0 compliance issues open
