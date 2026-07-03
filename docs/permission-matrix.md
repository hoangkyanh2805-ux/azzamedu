# Permission Matrix — Alpha Elite Agent OS

> Default rule: money, publish, production writes, and customer access → **human required**.

---

## Legend

- **A** = Autonomous (draft/read/audit)
- **H** = Human approval required
- **F** = Forbidden for agents

---

## By action type

| Action | Repo Skill | Offer | Lead Magnet | Landing Copy | CRO | FunnelKit | LearnHouse | Brevo | Compliance | Web Quality |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Read project docs | A | A | A | A | A | A | A | A | A | A |
| Draft markdown assets | A | A | A | A | A | A | A | A | A | A |
| Map external skills | A | — | — | — | — | — | — | — | — | — |
| Define offer/SKU docs | — | A | — | — | — | — | — | — | H | — |
| Draft customer copy | — | — | A | A | A | A | A | A | A | — |
| Compliance scan | — | — | — | — | — | — | — | — | A | — |
| Issue PASS/FAIL verdict | — | — | — | — | — | — | — | — | A | A |
| Run Lighthouse/axe specs | — | — | — | — | — | — | — | — | — | A |
| Publish WP/Elementor | F | F | F | F | F | H | F | F | F | F |
| WooCommerce product write | F | H | F | F | F | H | F | F | F | F |
| FunnelKit live config | F | F | F | F | F | H | F | F | F | F |
| LearnHouse API/user write | F | F | F | F | F | F | H | F | F | F |
| Brevo live send/automation | F | F | F | F | F | F | F | H | H | F |
| Telegram add member | F | F | F | F | F | F | H | F | F | F |
| Change live pricing | F | H | F | F | F | H | F | F | F | F |
| Delete production data | F | F | F | F | F | F | F | F | F | F |
| Override Compliance FAIL | F | F | F | F | F | F | F | F | F | F |
| Spend money / paid API scale | F | F | F | F | F | H | H | H | F | F |

### Telegram Access Bot (T1 / T2)

| Action | Telegram Access | Telegram Admin Ops | Human |
|--------|:---:|:---:|:---:|
| Draft bot templates / schema | A | A | — |
| Compliance scan bot copy | — | — | A (Compliance) |
| Deploy production bot | F | F | G1-bot |
| `/admin confirm` in production | F | H (human runs) | Admin |
| LearnHouse enroll | F | F | G4 |
| VIP Telegram add | F | F | G5 |
| Broadcast trade signals | F | F | F |
| WooCommerce webhook (P2) | H | H | G3 |

---

## Cross-agent dependencies

| Producer | Must pass before next |
|----------|----------------------|
| Offer Architect | → Lead Magnet, FunnelKit, Brevo CTAs |
| Lead Magnet draft | → Compliance → Landing Copy references |
| Landing Copy + CRO | → Compliance → Web Quality |
| FunnelKit map | → QG-OFFER + Compliance |
| Brevo templates | → Compliance → QG-EMAIL |
| LearnHouse course | → Compliance → QG-LMS |
| Telegram bot templates | → Compliance → G1-bot launch |
| Bot payment confirm | → Human admin → G4 → G5 (VIP) |

---

## Forbidden for ALL agents

1. Guaranteed profit, risk-free, fixed returns, passive bot income language  
2. Signal-group / free-signals positioning  
3. Production deploy without G1  
4. Customer provision without G4/G5  
5. Delete orders, users, or email lists  
6. Disable risk disclaimers on checkout or emails  

---

## Evidence required for human gates

| Gate | Evidence |
|------|----------|
| G0 Pricing | Updated `offer_stack.md` + owner ack |
| G1 Publish | Compliance PASS log + Web Quality PASS (if web) |
| G2 Brevo live | QG-EMAIL checklist + Compliance PASS all templates |
| G3 FunnelKit | QG-FUNNEL sandbox receipt |
| G4 LearnHouse | Order ID + provision SOP checklist |
| G5 Telegram | VIP order + @username |
| G1-bot Telegram launch | Compliance PASS `bot/templates/` + deploy checklist |

Mirror: `.ai/rules/permission-matrix.md`
