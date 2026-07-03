# First Sprint — Alpha Elite (Tuần 1–2)

> Tasks cụ thể cho 2 tuần đầu. Owner = điền tên khi assign.

---

## Sprint goal

**Tuần 2 cuối:** Lead magnet live + Apprentice checkout testable + LearnHouse staging với 1 module.

---

## Tuần 1

| # | Task | Owner | Output | Verify |
|---|------|-------|--------|--------|
| 1.1 | Finalize pricing trong `offer_stack.md` | | Prices filled | Sign-off |
| 1.2 | Write Gameplan PDF draft | | Google Doc | Compliance self-check |
| 1.3 | Design + export PDF v1 | | PDF file | < 5MB |
| 1.4 | Brevo setup + domain auth | | SPF/DKIM green | Brevo dashboard |
| 1.5 | WP landing hero + opt-in form | | Page live | Test submit |
| 1.6 | Brevo Email 0 + list automation | | Automation on | Receive test email |
| 1.7 | Thank-you page | | `/gameplan-thank-you` | Redirect works |
| 1.8 | Legal pages stub | | privacy, terms, disclaimer | Links in footer |
| 1.9 | Install marketingskills CLI | | Skills in `.codex/skills` | Agent triggers work |

**Tuần 1 exit criteria:** Opt-in → PDF email trong 5 phút.

---

## Tuần 2

| # | Task | Owner | Output | Verify |
|---|------|-------|--------|--------|
| 2.1 | `/apprentice` sales page | | Page live | CTA to checkout |
| 2.2 | WooCommerce product Apprentice | | SKU live | Add to cart |
| 2.3 | FunnelKit checkout + bump | | Checkout page | Sandbox buy |
| 2.4 | TY page Apprentice | | TY live | Order conditional |
| 2.5 | LearnHouse VPS + setup | | `learnhouse doctor` OK | HTTPS works |
| 2.6 | Course Module 1–3 upload | | Lessons playable | Mobile test |
| 2.7 | YouTube unlisted videos | | Embeds work | Not public |
| 2.8 | Brevo Sequence 1 (Email 0–7) | | Automations | Walkthrough |
| 2.9 | Provision SOP doc + test | | Playbook | Test order <24h |
| 2.10 | Full funnel QA | | Audit doc | Checklist 70%+ |

**Tuần 2 exit criteria:** Sandbox purchase → manual provision → LearnHouse login.

---

## Dependencies

```text
1.4 Brevo → 1.6 Email 0
1.5 Form → 1.6 automation
2.2 Product → 2.3 FunnelKit
2.5 LearnHouse → 2.6 content
2.9 SOP → 2.10 QA
```

---

## Daily standup prompts

1. Blocker on provision SLA?
2. Any copy without compliance review?
3. LearnHouse / WP environment status?

---

## Sprint retrospective (end week 2)

- Opt-in rate baseline?
- What delayed provision?
- Course content pace realistic?
- Defer list still valid?
