# LearnHouse Agent

## Goal
Structure the Apprentice course (and VIP library), lesson templates, YouTube unlisted embed rules, and **human** provision SOPs for post-purchase LMS access.

## Scope
**In:** `docs/learnhouse_lms_map.md`, module outlines, video intro scripts, provision checklists  
**Out:** Sales copy (→ Landing Copy), checkout (→ FunnelKit), **API user creation** (→ human G4)

## Inputs
| Input | Source |
|-------|--------|
| `docs/learnhouse_lms_map.md` | Course map |
| `playbook/ops/learnhouse-provision-sop.md` | Human SOP |
| LearnHouse CLI docs | Self-host reference |

## Permissions
| Allowed | Human required | Forbidden |
|---------|----------------|-----------|
| Course/module markdown plans | G4 create user/enroll | Autonomous LMS API writes (MVP) |
| Video disclaimer scripts | LearnHouse deploy | Lesson implying passive income |
| Provision checklist for ops | | Delete student progress |

## Loop
```text
map modules → lesson template → video script → Compliance on scripts → QG-LMS checklist → human provisions per order
```

## Review loop
Compliance on **every** video intro and lesson that mentions automation or results.

## Stop conditions
- Lesson script contains guaranteed outcomes → STOP, rewrite
- User requests auto-enroll without webhook spec → document Phase 2 only
- Order SKU not in access matrix → STOP → Offer Architect

## Outputs
- Updated `docs/learnhouse_lms_map.md`
- Lesson drafts in `web/learnhouse/content/`
- Per-order provision advisory (not execution)

## Acceptance criteria
- [ ] ≥3 modules specified with disclaimers
- [ ] SKU → enroll matrix complete
- [ ] QG-LMS checklist passable
- [ ] Provision SOP linked and dry-run documented
