# Bot message templates

> **Rule:** Compliance PASS required before G1-bot launch.  
> **Checklist:** `kickstart/11-compliance-checklist.md`

Create one file per template below. Agents implement handlers to load these strings.

| File | Used by |
|------|---------|
| `start.md` | `/start` welcome + disclaimer |
| `offers.md` | `/offers` intro + per-SKU blurbs |
| `pay.md` | PayPal + crypto blocks |
| `status.md` | `/status` by tier/state |
| `learnhouse.md` | After `/admin provisioned` |
| `vip.md` | After `/admin tgdone` |
| `support.md` | Ticket acknowledgment |
| `legal.md` | `/legal` full disclaimer |

**Do not** include: signals, guarantees, financial advice, passive income.
