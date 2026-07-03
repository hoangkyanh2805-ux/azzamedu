# Stop Conditions — Alpha Elite Agent OS

## Global (all agents)

| ID | Condition | Response |
|----|-----------|----------|
| G-S1 | Missing `docs/compliance_guardrails.md` | STOP — load rules |
| G-S2 | User requests NEVER-table language | STOP — escalate Compliance / G7 |
| G-S3 | Production write requested | STOP — cite human gate |
| G-S4 | 3 failed Compliance loops | STOP — human owner |
| G-S5 | Sources of truth conflict | STOP — identify reconciler agent |
| G-S6 | Credentials not in secure env | STOP — list safe options |

## Retry policy
- Transient tool/read failures: retry ≤3
- Validation/compliance failures: no retry without changed input
- After 3 failures: escalate with evidence

## Escalation format

```text
Stopped because: <condition>
Goal affected: <agent goal>
Evidence: <audit path, quotes, errors>
Safe next options:
  1. ...
  2. ...
Recommended: ...
Approval needed: <gate ID + approver role>
```

## Agent-specific

| Agent | Stop if |
|-------|---------|
| Repo Skill Librarian | Unknown repo; skill recommends hype copy |
| Offer Architect | `[FILL]` pricing when checkout asked; signal tier requested |
| Lead Magnet | Magnet becomes signal list; no disclaimer in outline |
| Landing Copy | No CRO wireframe; Compliance FAIL ×3 |
| CRO | Fake proof/urgency spec; >3 form fields without ack |
| FunnelKit | SKU missing; no risk checkbox in flow |
| LearnHouse | Passive income lesson; auto-enroll without spec |
| Brevo Email | Live send requested; missing footer |
| Compliance | Override demanded; unknown channel |
| Web Quality | P0 open; URL down |
| Telegram Access | Signal bot feature requested; disclaimer missing; token in repo |
| Telegram Admin Ops | tgdone without G5; auto-confirm all payments |
