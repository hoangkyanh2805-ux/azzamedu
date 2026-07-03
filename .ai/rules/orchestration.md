# Orchestration Rules — Alpha Elite

## 1. Compliance is mandatory
No customer-facing artifact reaches human G1 without **Compliance Agent PASS** logged in `.ai/audit/compliance/`.

## 2. Web pages need dual gate
Landing, sales, checkout skin, thank-you: **Compliance PASS** then **Web Quality PASS** (or documented human waiver).

## 3. Offer truth is single source
`docs/offer_stack.md` wins conflicts for SKUs, tier names, CTAs. **Offer Architect** reconciles.

## 4. Producer agents do not publish
Draft in `docs/`, `sales/assets/`, `web/` only. Humans execute G1–G6.

## 5. Parallel work allowed
After Offer Architect + Compliance on offer doc:
- FunnelKit ∥ LearnHouse ∥ Brevo Email may proceed in parallel
- All must pass Compliance before respective live gates

## 6. Tone law (all agents)
Premium · system-first · anti-hype · education, trade ideas, automation support, SOPs, community support

## 7. Handoff format

```markdown
## Handoff: <From Agent> → <To Agent>
- Artifact: <path>
- Compliance: PASS <audit file> | PENDING
- Notes:
- Blockers:
```

## 8. Command shortcuts
- Full pre-launch: `.ai/commands/pre-launch.md`
- Funnel audit: `.ai/commands/audit-funnel.md`
- Customer provision: `.ai/commands/provision-customer.md`
