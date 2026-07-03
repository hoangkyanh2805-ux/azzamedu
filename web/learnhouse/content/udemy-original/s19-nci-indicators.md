# S19: UPDATE _ NCI indicators for REAL TRADING

*Jayce Pham SMC — Section 19 of 20. NCI TradingView/MT tools — imbalance power highlight + forex lot size calculator.*

---

## Imbalance - Smart Money power

### What it is?

**NCI imbalance indicator** — highlights **Fair Value Gaps** on chart per Pine/MT script in **Resources** tab. Subtitle **"Smart Money power"** ties to **S07 IMB scoring** — tool accelerates **finding** gaps; **you** assign power 0–10 and combine with institutional base score.

**What indicator does:**

- Marks bullish/bearish FVG zones with boxes or lines
- Optional **CE (50%)** line inside gap
- May show **stacked** gaps when displacement continues

**What indicator does NOT do:**

- Auto **buy/sell arrows** (official NCI script per Jayce)
- Replace liquidity sweep requirement
- Score **total power** — manual journal math required

**"REAL TRADING"** framing:** Tools for **live funded accounts** where speed matters — still subordinate to **checklist**.

**Alignment rule (S07):** If indicator shows gap you did not score manually — **re-draw candles**; wick overlap often misread. **Manual score overrides** for entry permission.

### How to define or apply it?

**Install & settings:**

1. Resources → download NCI imbalance script.
2. Apply to **XAUUSD, US30** first — teaching pairs.
3. Default lookback — do not optimize until 30 manual marks done.
4. Use **H1/M15** for scalping context; hide on M1 to reduce noise.

**Workflow with signal power:**

1. Indicator flags FVG → confirm 3-candle rule (S02).
2. Score fill status at entry moment (S07 table).
3. Check POI overlap with FVG CE.
4. Add IMB score to IB score → total power gate.
5. Entry mode per S07 (S&F vs CONF).

**With S13 liquidity indicator:** Liquidity finds pools; imbalance finds gaps — **both** feed manual footprint, not auto trades.

**2024 update (S18):** Ignore news-hour first print unless structure settles.

### Example

**Sep 28 strongest case replay with indicator**

- Stacked FVGs light up automatically — Jayce still narrates **sweep** and **nested OB** manually.
- IMB score **9** matches visual — student without tool can score same with practice.
- Entry CE limit at overlap — indicator does not place order; **you** use broker limit.

**Failure mode:** Student enters every highlighted box — repeat S18 real story — fix with **power journal**.

**Homework:** 10 charts — indicator on/off — time to mark gaps; accuracy vs manual only.

### Video
`[PENDING]` · Duration: TBD

---

## Forex lot size calculation

### What it is?

**Forex lot size calculator** (spreadsheet or TradingView risk tool in Resources) — converts **account risk %**, **stop distance in pips/points**, and **pair tick value** into **lots** so **1% risk** on Sep 26-style trades is **mathematical**, not guessed.

**Why it matters:**

- **Sep 26 −1.5%** and **+3.5%** assume **correct sizing** — wrong lot turns 1R plan into 3% accidental risk.
- Prop firms enforce **max lot** and **daily loss** — calculator keeps inside rules.
- Gold (XAUUSD) pip/tick confusion kills accounts — dedicated row in Jayce sheet.

**Inputs:**

- Account balance (or prop equity)
- Risk % per trade (e.g., 1%)
- Stop distance (structural — from sweep to entry)
- Pair / contract specification

**Output:**

- Lots (micro/mini/standard) or contracts US30

### How to define or apply it?

**Before every live click:**

1. Mark stop on chart **first** — structure not emotion.
2. Measure distance — platform ruler or calculator pip field.
3. Enter risk % — **never** increase after loss (Sep 26 rule).
4. Round lot **down** if between steps — conservative.
5. Journal: `Risk %`, `Stop pts`, `Lots`, `Planned R`.

**Pairs notes:**

| Instrument | Caution |
|------------|---------|
| XAUUSD | Volatile — verify tick value per broker |
| US30 | Points not forex pips |
| USDCHF | Slow — small stop temptation to oversize lots |

**Correlation:** Two 1% positions highly correlated ≠ 1% total exposure — Jayce reduces each to **0.5%** when US30+NAS same direction.

**S16:** Risk mindset — calculator enforces **control**, not entry hunting.

### Example

**Illustrative calculation (US30 long)**

- Account $50,000; risk 1% = $500.
- Stop 40 points; tick value $1/point/lot (broker-specific — use sheet).
- Lots = $500 / (40 × tick value) — Jayce walks through live on spreadsheet in video.

**Sep 26 Trade #2 +3.5% account:** If risk was 1.2% and exit ~3R — account % ≈ 3.6% — matches title when rounded.

**Student task:** Download calculator; compute lots for three S06 backtest stops without placing orders.

### Video
`[PENDING]` · Duration: TBD
