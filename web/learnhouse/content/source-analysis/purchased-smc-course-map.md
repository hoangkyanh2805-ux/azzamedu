# Purchased Course Source Map — SMC Udemy → Alpha Elite

> **Pipeline:** knowledge-asset-factory → learnhouse-agent → compliance-agent  
> **Source:** User-purchased PDF export · Jayce Pham Udemy curriculum screenshots  
> **Date:** 2026-07-02  
> **Legal note:** We extract **pedagogical structure and concepts** only. We do not copy instructor branding, hype copy, thumbnails, or proprietary video. Alpha Elite is a **distinct product** with compliance rewrite.

---

## Source inventory

| Field | Value |
|-------|-------|
| Original title | Advanced trading course: The complete Smart Money Concepts |
| Platform | Udemy |
| Scale | 21 sections · ~171 lectures · ~9h video |
| Core method | SMC: liquidity, FVG/IMB, manipulation, BOS/CHoCH, POI, order blocks |
| Assets | 17 downloads · quizzes · live PnL session recordings |

**Confidence:** High (6-page curriculum capture in `source-analysis/page-*.png`)

---

## What we KEEP (education value)

| Source block | Alpha Elite use |
|--------------|-----------------|
| Definition → apply → example lesson loop | Every AE lesson template |
| Liquidity, IMB/FVG, BOS/CHoCH, premium/discount | M2 Market Structure Foundations |
| Double order block + POI, trend vs break | M3 POI & Setup Framework |
| Market cycle / structure cornerstones | M3 + VIP walkthrough library |
| Trading examples (XAUUSD, indices, forex) | M6 Case walkthroughs (process-only titles) |
| Journal day reviews | M5 Session SOPs (habit metrics, not $/day) |
| Lot sizing + news awareness | M4 Risk Protocol |
| Multi-TF + confirmation vs set-and-forget | M7 Confirmation rules |
| Indicator as helper (not magic) | M8 Tools literacy |
| Mindset / mistake systems | M1 + M5 weekly review |

---

## What we REMOVE or REWRITE (compliance)

| Source (prohibited) | Alpha Elite rewrite |
|---------------------|---------------------|
| "Signal Power" / "Smart Money Signal" | **Setup confirmation checklist** |
| Live trade titles with % profit/loss | **Session review: trade 1–4** (process labels) |
| "5%/day scalp $2700" journal | **Daily journal field guide** (no dollar brag) |
| "Zero to Profitable level" | **Zero to structured execution** |
| "90% Winrate" cross-sell | **Not referenced** |
| Discord/Telegram NCI signal groups | **VIP accountability desk** (rules-first) |
| "NCI indicators for REAL TRADING" | **Optional chart tools (education)** |
| FTMO leaderboard / TOP fund claims | **Not used in AE course** |
| Monthly profit targets psychology | **Monthly process targets** |
| "Set & Forget" profit framing | **When to wait for confirmation** (SOP) |

---

## Section mapping (21 → 8 AE modules)

| Udemy section (abbrev) | AE module |
|------------------------|-----------|
| Intro / trust / community hype | **Skip** — AE has Gameplan + compliance intro in M1L1 |
| Definitions SMC (7 lec) | **M2** (7 lessons) |
| Double OB / POI / trend (5+4 lec) | **M3** (5 lessons) |
| Extra Wyckoff/Elliott/mistakes | **M8L2** (1 lesson + VIP library) |
| Trading examples all cases | **M6** (5 lessons) |
| Signal power / institutional base | **M7** (3 lessons) |
| Live Sep 26–29 sessions | **M6** walkthroughs (re-titled) |
| Trading journal + 5%/day | **M5** journal SOP |
| Bonus zero→profitable | **M1** prerequisites copy |
| 15+15 quizzes | `quizzes/quiz-bank.md` (compliance-safe) |
| Trading tips / monthly target | **M5** weekly review + **M7** |
| NCI indicators | **M8** automation literacy |
| Mindset successful traders | **M1** (already) |

---

## Agents & skills used

| Agent / skill | Role in rebuild |
|---------------|-----------------|
| knowledge-asset-factory | Source → map → reusable curriculum |
| learnhouse-agent | Lesson template, video intro, provision link |
| compliance-agent | Swap table on every lesson title + script |
| landing-copy-agent | Curriculum bullets stay synced with sales pages |
| offer-architect | Stays Apprentice SKU AE-APP-001 — expanded depth = value |

---

## Deliverables (this rebuild)

```text
web/learnhouse/
├── COURSE-REBUILD-MASTER.md
├── content/
│   ├── course-manifest.md          # v2 — 35 lessons
│   ├── source-analysis/            # PDF page captures
│   ├── apprentice-operating-course/
│   │   ├── m01 … m08               # full lesson bodies
│   ├── quizzes/quiz-bank.md
│   └── video-scripts/recording-guide.md
docs/learnhouse_lms_map.md          # updated module map
```

---

## Acceptance

- [ ] No P0 compliance phrases in lesson titles
- [ ] M2–M3 live in LearnHouse (market structure core)
- [ ] Quizzes test definitions — not "which trade wins"
- [ ] Video titles: `AE Apprentice M#L#` only on YouTube
