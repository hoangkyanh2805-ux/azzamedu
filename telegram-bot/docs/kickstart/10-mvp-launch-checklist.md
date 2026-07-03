# 10 — MVP Launch Checklist

> **Gate:** G1-bot (Telegram bot production) + dependencies G0, G3, G6 as applicable

---

## Pre-build

- [ ] `01-project-mission.md` agreed — not a signal bot  
- [ ] `09-backlog.md` Now items assigned  
- [ ] Supabase or Sheets provisioned  
- [ ] Schema applied (`06-database-schema.md`)  
- [ ] `config.yaml` filled (not committed)  
- [ ] BotFather bot created (name, description, about)  

---

## Code complete

- [ ] `/start` — auth + disclaimer  
- [ ] `/offers` — 5 offers (Gameplan, Apprentice, VIP, Quant, DWY)  
- [ ] `/status` — Free, Apprentice, VIP, Quant, Inner Circle labels  
- [ ] `/pay` — PayPal + crypto instructions  
- [ ] Payment proof → `payment_review` + admin notify  
- [ ] `/support` — ticket + admin notify  
- [ ] `/admin confirm|provisioned|tgdone|revoke`  
- [ ] Upgrade / apply → admin notify  
- [ ] LearnHouse instruction template wired  
- [ ] VIP post-approval message wired  
- [ ] Admin restricted to `ADMIN_TELEGRAM_IDS`  

---

## Compliance (`11-compliance-checklist.md`)

- [ ] All templates Compliance PASS  
- [ ] No signal/profit/guarantee language  
- [ ] `/start` disclaimer present  
- [ ] `/legal` full risk text  
- [ ] Audit log: `.ai/audit/compliance/YYYY-MM-DD-telegram-bot.md`  

---

## Integration

- [ ] Checkout URLs match `docs/offer_stack.md` SKUs  
- [ ] `LEARNHOUSE_URL` correct  
- [ ] Thank-you page links to bot (optional deep link)  
- [ ] Admin ops trained on `05-admin-journey.md`  
- [ ] `.ai/commands/telegram-provision.md` dry run completed  

---

## Deploy

- [ ] VPS / hosting ready  
- [ ] `DEPLOYMENT.md` followed (webhook or polling prod)  
- [ ] TLS valid (webhook / Mini App)  
- [ ] systemd restart tested  
- [ ] Secrets not in git  
- [ ] BotFather command list set  

---

## Post-launch smoke test

- [ ] `/start` from fresh account  
- [ ] `/offers` links open  
- [ ] Test proof → admin notification  
- [ ] Test confirm → provisioned → user DM  
- [ ] VIP: username → tgdone flow  
- [ ] `/support` ticket received  
- [ ] Rollback procedure documented  

---

## Human sign-off

| Gate | Approver | Date |
|------|----------|------|
| G0 Pricing | Owner | |
| G6 Payment text | Owner | |
| Compliance | Reviewer | |
| G1-bot Launch | Owner | |

Evidence: `.ai/audit/approvals/YYYY-MM-DD-telegram-bot-launch.md`

---

## MVP rule verification

- [ ] Confirmed: manual G4 LearnHouse + manual G5 VIP acceptable  
- [ ] No auto VIP join without admin  
- [ ] SLA ≤24h communicated in bot copy
