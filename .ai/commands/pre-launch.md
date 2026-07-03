# Pre-launch command

Run all QA gates before G1 publish.

## Steps

1. **Offer Architect** — confirm QG-OFFER (`docs/offer_stack.md` pricing filled)
2. **Compliance Agent** — PASS all artifacts in `sales/assets/`, public URLs draft
3. **Web Quality Agent** — QG-WEB on `/`, `/apprentice`, `/vip`, `/checkout/`, thank-you pages
4. **FunnelKit Agent** — QG-FUNNEL sandbox receipt logged
5. **LearnHouse Agent** — QG-LMS checklist
6. **Brevo Email Agent** — QG-EMAIL test walkthrough
7. **Human G1** — log approval in `.ai/audit/approvals/`

## Reference
`docs/qa-gates.md` · `docs/launch_checklist.md`
