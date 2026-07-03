# S06: Trading EXAMPLES - All the cases with SMC

*Jayce Pham SMC — Section 6 of 20. Full chart walkthroughs applying S02–S05 + main strategy. Study with replay; mark your own charts while watching.*

---

## XAUUSD _ Double Order block by 2 POI zones

### What it is?

This is the **flagship XAUUSD case** for Jayce's core strategy: **double order block with two POI zones** to optimize risk-reward on gold. Gold moves fast, respects liquidity, and prints clean institutional footprints on H4 and M15 — ideal for SMC.

**Setup type:** Trend-follow (or post-manipulation continuation) using:

1. **POI zone #1** — primary order block after displacement / BOS (often H4 or H1 origin of move).
2. **POI zone #2** — refined OB inside or at edge of POI #1, frequently aligned with FVG or 50% equilibrium of the impulse leg.

**Why double POI on XAUUSD?**

- Single wide OB on gold often gives **poor RR** — stop must be far below sweep low.
- Splitting entry logic across two nested zones lets you place stop beyond **structural invalidation** while targeting **buy-side liquidity** above swing highs (often 1:3 to 1:5+ on prop firm rules).
- First POI may tap and react; if missed, **second POI deeper in discount** still valid if HTF narrative unchanged.

**Narrative checklist before entry:**

- Liquidity swept (equal lows or obvious swing low taken).
- Manipulation wick rejection back above sweep level.
- BOS in trade direction on HTF.
- Displacement + FVG from smart money leg.
- Two nested bullish OBs (or bearish in reverse) marked — not random rectangles.

### How to define or apply it?

**Timeframes Jayce uses on this example:**

- **Bias:** D1 + H4 structure and premium/discount.
- **POI marking:** H1/H4 for POI #1; M15 for POI #2 refinement.
- **Entry trigger:** M5/M15 BOS bounce or limit at POI #2 with momentum ≥ 18 (S05).

**Step-by-step markup:**

1. **Find liquidity pool** below recent consolidation — Asian session lows or equal lows on H4.
2. **Wait for sweep** — candle pierces lows, closes back inside range (manipulation).
3. **Mark POI #1** — last down-close candle cluster before displacement up (bullish OB) or origin of FVG.
4. **Draw impulse leg** — from sweep low to first BOS high; mark 50% and OTE (62–79%) if you use fib for confluence only.
5. **Mark POI #2** — smaller OB where M15 pullback stalls inside POI #1; often where FVG mid-point sits.
6. **Invalidation** — below sweep low (hard stop). If CHoCH bearish on H4 before entry, **void setup**.
7. **Targets** — TP1 at internal liquidity / FVG fill above; TP2 at buy-side liquidity above range high; optional runner to next HTF POI.
8. **Risk** — 1–2% account; lot size from S19 calculator. Never widen stop inside POI #2 body to "fit" lot size.

**Entry models:**

| Model | When | Risk |
|-------|------|------|
| Limit at POI #2 | Momentum ≥ 22, clear institutional base (S07) | Set & forget with alert |
| BOS bounce | Momentum 15–21 | Wait M15 mini BOS from POI |
| POI #1 only | Strong trend, shallow pullback | Tighter stop, smaller size |

**Double POI invalidation rules:**

- Price closes H4 candle **below POI #1** after BOS was bullish → narrative broken, no long.
- Both POIs **mitigated** (full traverse) without reaction → OB failed, smart money not defending.
- News spike (NFP, FOMC) through zone → skip or wait post-news structure.

### Example

**Historical XAUUSD walkthrough (course chart replay)**

**Context:** H4 range after decline; equal lows at $1,9XX zone (use your replay date). Retail short below lows.

1. **Liquidity sweep:** H4 wick takes equal lows, closes back inside range — classic manipulation.
2. **Displacement:** Next H4 candle bullish expansion, leaves FVG. POI #1 = H4 bullish OB at base of expansion.
3. **BOS:** Price breaks last H4 lower high — structure shift bullish.
4. **Pullback:** M15 corrects into POI #1; shallow reaction then deeper stab into POI #2 (nested M15 OB + unfilled FVG).
5. **Momentum:** Displacement leg strong; pullback 48% — score 20/25.
6. **Entry:** Limit at top of POI #2 or buy on M5 BOS after rejection wick. Stop 10–20 pips below sweep low (gold volatility — use structure not arbitrary pips).
7. **Management:** TP1 partial at nearest sell-side liquidity; move stop to BE only after BOS on M15 in favor — not after 5 green candles of hope.
8. **Outcome teaching point:** Win or loss, journal must show **both POIs labeled before entry**. Jayce grades students on markup, not screenshot PnL.

**Common XAUUSD-specific errors:**

- Marking POI on M1 only — noise.
- Ignoring D1 supply above — take profit before HTF wall if momentum fades.
- Trading double POI **against** USD strength narrative on DXY without break-trend rules.

**RR optimization note:** Jayce targets minimum **1:2** on double POI with structural stop; **1:3+** when second POI is deeper and first liquidity target is far. Do not widen TP to "make RR look good" while moving stop inside sweep — that is fake RR and fails prop firm consistency checks. Partial at 1:1 optional on live funded accounts to reduce psychological pressure; journal whether partial helped or hurt over 20 trades.

**Quiz link:** S14 basic quiz asks which POI comes first in double setup — answer: HTF origin OB before LTF refinement. If you miss that question, re-watch S03 before continuing S07 signal power.

### Video
`[PENDING]` · Duration: TBD

---

## US30 - Example 2 & Example 3. Missed entry and re-entry with SMC - Double POI

### What it is?

US30 (Dow Jones CFD) is Jayce's **index scalping and swing hybrid** instrument — wide sessions, clean liquidity at session highs/lows, fast displacement during NY open. This lesson covers **two linked examples**:

- **Example 2:** Valid first entry on double POI — full execution.
- **Example 3:** **Missed entry** on first POI touch, then **rules-based re-entry** when price returns to second POI or prints new BOS bounce.

**Why missed entry is its own skill:**

Most traders either **chase** (market order after move left) or **give up** (setup still valid but they are emotionally done). Jayce's rule: *Missed entry is not a loss — undisciplined chase is a loss.*

**Re-entry is allowed only when:**

1. HTF bias and liquidity narrative **unchanged**.
2. Invalidation level **not hit** (sweep low still holds for longs).
3. New trigger appears: **POI #2 tap** OR **fresh BOS bounce** from same POI stack.
4. You did not violate daily loss limit chasing Example 2.

**Double POI on indices:** US30 POIs often form at **session open manipulation** — sweep London or Asia high/low, displacement, OB stack on M15/M5.

### How to define or apply it?

**Example 2 framework (first entry):**

1. NY pre-open: mark liquidity above overnight high on US30 M15.
2. Price sweeps high, rejects — manipulation for short (mirror for long on low sweep).
3. BOS bearish on M15; mark double POI in premium: POI #1 at H1 OB, POI #2 at refined M15 OB + FVG.
4. Entry on first tap of POI #1 with confirmation candle — Jayce takes partial or full per momentum.
5. Stop above sweep high; TP at sell-side liquidity below — often prior session low.

**Example 3 framework (missed entry → re-entry):**

| Scenario | What happened | Correct action |
|----------|---------------|----------------|
| A | Price touched POI #1 while you were away — rejected 40 pips without you | **Do not chase.** Wait POI #2 or retest |
| B | Price blew through POI #1 without reaction | Setup dead — no re-entry |
| C | Price returned to POI #2, same HTF story | **Re-entry** with BOS bounce or limit at POI #2 |
| D | New sweep took invalidation | **No re-entry** — new analysis |

**Re-entry checklist (print this):**

- [ ] Same session or next session still same H4 bias?
- [ ] Sweep level intact?
- [ ] Double POI still unmitigated or only POI #1 mitigated, POI #2 fresh?
- [ ] Momentum score recalculated ≥ 15?
- [ ] Not revenge after prior scratch?

**Size on re-entry:** Jayce often uses **same risk %** not double — re-entry is not "make back." If first was missed not lost, full 1% is fine. If first was stopped at BE, half size optional.

### Example

**US30 Example 2 — short at double POI after NY liquidity grab**

1. Overnight high = obvious buy stops. M15 sweeps, long wick rejection.
2. Bearish displacement; FVG opens. POI #1: M15 bearish OB at top of FVG.
3. Price rallies to POI #1; student watching gets M5 CHoCH down + entry. Stop above sweep. TP1 at London low.
4. Trade works — textbook.

**US30 Example 3 — same day, student missed POI #1**

1. Student was on call; price rejected POI #1 and dropped 60 points — **no chase**.
2. Price pulls back deeper into **POI #2** (nested zone under POI #1, still below sweep high).
3. M5 prints lower high, BOS down from POI #2 edge.
4. Student enters short on BOS bounce — **valid re-entry**. Same invalidation above sweep.
5. **Wrong version:** Student market-sells at TP1 level of Example 2 because "it already dropped" — that is retail FOMO, not SMC.

**Journal note Jayce requires:** Column "Entry attempt #" — 1 for first, 2 for re-entry. If attempt #3 without new structure, flag as overtrade mistake (S05).

**Time stop on re-entry:** If price lingers inside POI #2 more than **2× your normal session window** without BOS (e.g., 45 min on M5 scalping), cancel pending limits — momentum died. US30 during lunch chop kills re-entries that looked perfect at NY open.

**Alert setup:** TradingView or MT5 alert at POI #2 edge so you do not stare at chart after missing POI #1. Missed entry discipline is **technical** (alerts + rules), not willpower alone.

**Spread and slippage on US30:** Index CFD spreads widen at session open — factor 2–4 points into stop placement. Re-entry on Example 3 must still clear **1:2 RR after spread** or Jayce skips. Demo account that ignores spread teaches false confidence; use realistic commission settings.

**Correlation check:** US30 vs NAS100 — if both show double POI but NAS already swept and ran, US30 re-entry may be **late leg**. Jayce picks **one index** per session to avoid duplicate exposure to same USD risk-on narrative.

**Video pause exercise:** At minute where POI #1 rejects, cover right side of chart. Predict: will POI #2 form or setup die? Write prediction before reveal. Trains patience muscle for live funded days when you cannot rewind.

### Video
`[PENDING]` · Duration: TBD

---

## EURCAD - Sell order - SMC with bounce power from Key level

### What it is?

**EURCAD sell case** demonstrates **Key level bounce power** combined with SMC — not every trade is pure double POI on indices. Here **Key level** (from NCI Level 1) acts as HTF wall; SMC provides **timing** for the short at premium POI into that resistance.

**Key level vs POI (S04 difference recap):**

- **Key level** — horizontal structure from weekly/daily swing highs/lows, round numbers, long-standing S/R. Price "respects" it over months.
- **POI / order block** — short-term institutional footprint after displacement. May sit **inside** or **at** key level for maximum power.

**Bounce power** = when price approaches key level from below, smart money sells into retail buys at resistance — you see:

- Liquidity build below key level (retail longs hoping breakout).
- Manipulation poke above or into key level, rejection.
- Bearish OB + FVG at key level in **premium** zone of HTF range.
- BOS down on execution TF = sell signal with key level as **magnet** for targets below.

EURCAD suits this lesson: slower than GBP pairs, cleaner reactions at daily levels, good for students transitioning from XAUUSD volatility to forex cross.

### How to define or apply it?

**Markup sequence:**

1. **D1 key level** — mark major swing high (e.g., prior month high where price failed twice).
2. **Premium/discount** — on H4 range, key level should sit in **premium** (above 50%) for sell bias.
3. **Liquidity** — equal highs just below key level or buy stops above local highs into level.
4. **Approach** — price rallies into key level; do not sell blindly on first touch.
5. **SMC confirmation** — manipulation wick into/through key level, close back below; bearish displacement leaves FVG.
6. **POI** — bearish order block at key level intersection with FVG.
7. **Entry** — sell limit at POI or BOS bounce on M15/M5; stop above manipulation wick + buffer.
8. **Targets** — discount zone of H4 range, then next liquidity pool below, then opposing key level support.

**Bounce power scoring (add to S07 institutional base):**

| Confluence | Points |
|------------|--------|
| Daily key level | +3 |
| Weekly key within 20 pips | +2 |
| Premium zone | +2 |
| Liquidity sweep into level | +3 |
| Bearish OB + FVG | +2 |
| BOS on H4 or M15 | +2 |

Score ≥ 10 → high power key level sell. Below 7 → wait.

**When key level sell fails:**

- H4 close **above** key level with displacement up = breakout, not fake — **no short**; flip to break-trend long rules or stand aside.
- Slow grind through level without rejection = **low bounce power** — skip.

### Example

**EURCAD sell walkthrough**

1. **D1:** 1.47XX area = multi-touch resistance (key level). Price below it for weeks — H4 downtrend bias optional but key level sell is primary story.
2. **H4:** Price rallies from discount toward key level; 50% equilibrium crossed — entering premium.
3. **Liquidity:** M15 equal highs stack under daily key — buy stops baited.
4. **Manipulation:** H4 candle wicks into daily key, closes bearish engulfing or long upper wick.
5. **POI:** Bearish OB on H4 at key level; M15 FVG overlap for entry refinement.
6. **Momentum:** Rally into level was sharp — sell-side reaction score 19/25.
7. **Entry:** Sell on M15 BOS down after POI tap; stop 15–25 pips above wick high (pair dependent).
8. **TP:** First at H4 demand / FVG fill below; second at prior swing low liquidity.
9. **Jayce teaching point:** Without key level, same OB might be **weak** — confluence is the edge, not the rectangle color.

**Student exercise:** Replay 5 EURCAD approaches to same D1 key level; tag win/loss vs bounce power score. You should see correlation between score ≥ 10 and cleaner reactions.

**CAD news caveat:** Canadian employment and BOC rate decisions spike EURCAD through key levels without respect — check calendar. Bounce power model assumes **no imminent high-impact CAD/USD news**. Jayce reduces size 50% on cross pairs during red-folder day even when setup scores high.

**Level 1 → Level 2 bridge:** If you skipped NCI Key level module, pause here and mark 3 daily levels on EURCAD before watching sell example. SMC without key level context is like driving with map but no street names — POI floats without anchor.

**Fibonacci discipline:** Jayce uses 50% equilibrium and OTE zone **only** when key level and POI already align — fib is confluence, not primary signal. Drawing fib from wrong swing (pre-sweep micro leg) inflates bounce power score falsely; anchor from sweep low to key level touch high for sell case.

**Partial profit at key level support:** First TP at next H4 demand is conservative; aggressive traders partial 50% there and runner to liquidity pool. Journal which TP style matches your prop firm daily target — consistency beats hero trades.

### Video
`[PENDING]` · Duration: TBD

---

## USDCHF - Loss order - What went wrong?

### What it is?

This lesson is a **real loss trade on USDCHF** Jayce shows openly — not to scare you, but to prove **every system loses**. Purpose: train **post-trade diagnosis** before the next lesson's root cause drill.

**USDCHF characteristics:**

- Often inverse correlate with EURUSD; can chop in risk-on/risk-off without clear trend.
- Smaller pip moves — students **over-leverage** to "feel" profit; stops get hunted on M5 noise.
- Swiss National Bank history reminds: respect news and wide spreads.

**What the loss trade looked like (course narrative):**

Student (or Jayce demo) took a **long at bullish POI** on M15 without full confluence. Price touched POI, showed weak reaction, CHoCH down, stopped out −1R to −1.5R.

**Surface story:** "Smart money trapped me."  
**Actual story (preview S06L5):** checklist failures stacked.

### How to define or apply it?

**Loss autopsy timeline (fill within 30 min of stop):**

1. **Screenshot at entry** — what was marked?
2. **HTF bias** — D1/H4: with trade or against?
3. **Liquidity** — was sweep narrative present?
4. **POI quality** — single OB or double POI? Institutional base score (S07)?
5. **Momentum score** at entry?
6. **Entry type** — chase, limit, confirmation?
7. **Stop placement** — beyond invalidation or inside noise?
8. **News** — any red folder within 60 min?
9. **Emotional tag** — FOMO, boredom, revenge, calm?
10. **Rule broken** — which line of your one-page system (S05)?

**USDCHF loss — typical failure modes:**

| Failure | Symptom on chart |
|---------|------------------|
| Counter-trend long | D1 bearish, buying M15 OB "because oversold" |
| No liquidity sweep | POI in middle of range, no stop hunt story |
| Weak POI | Wide zone, many prior touches (mitigated OB) |
| Asian session chop | 5 CHoCH on M5, spread eats edge |
| Stop too tight | Stop inside POI body, wick takes you before move |
| Ignored DXY | USD strengthening, CHF not weak enough for pair long |

**Jayce rule after loss:** No next trade for **minimum 30 minutes** — journal first. On prop firm day, loss 1.5% (Sep 26 reference) still inside daily max if rules followed; **second trade only if checklist fresh**, not tilt-revenge.

### Example

**USDCHF long loss — play-by-play**

1. **Setup claimed:** Bullish M15 OB after pullback in "uptrend."
2. **Chart reality:** H4 showing lower highs; D1 resistance 20 pips above. Uptrend only on M5 — **no HTF bias**.
3. **Liquidity:** No sweep of lows; POI floated mid-range — **no manipulation**.
4. **POI:** Old OB tested 4 times in 2 days — **mitigated**, not fresh institutional base.
5. **Momentum:** Pullback 70% deep, overlapping candles — score **11/25**.
6. **Entry:** Market buy on first green candle — **no BOS bounce confirmation**.
7. **Stop:** 8 pips below OB — inside noise; M5 sweep takes stop, then price barely rallies without you.
8. **Result:** −1.2% account.

**What went wrong (one sentence):** Traded a **weak, mitigated POI** against **H4 structure** with **no liquidity narrative** and **no confirmation** — SMC vocabulary used, SMC rules not followed.

**Homework:** Pause video before Jayce reveals errors; write your own list, then compare. Gap = your learning edge.

**Loss is tuition, not identity:** Jayce shows USDCHF loss publicly so you normalize red trades before funded challenge. Prop firms do not fail you on one −1R; they fail you on **repeated rule breaks** after loss. Emotional sequence after stop: close platform 10 min → fill autopsy → only then decide if next setup qualifies.

**Pair selection lesson:** USDCHF is **teaching pair** for loss review — slow, mean-reverting, punishes lazy HTF markup. After this two-lesson block, Jayce suggests focusing execution on XAUUSD + US30 where your journal sample size grows faster. Forex crosses only when key level story is obvious like EURCAD sell.

**Compare to Sep 26 live:** First trade loss 1.5% same day recovered — difference is **system allowed loss size** and **next trades followed checklist**. USDCHF loss student did not have that discipline yet; S06L5 fixes it with RCA.

**Red flag self-audit (answer honestly before next trade):**

- Did I mark chart or copy Telegram idea?
- Can I explain liquidity story in one sentence?
- Would I take same trade if nobody was watching?
- Is this trade proving something after loss?

Three "no" answers → mandatory sit-out remainder of session. Jayce uses this gate in competition prep; it is stricter than indicator rules because psychology is the hidden leverage killer on slow pairs like USDCHF.

**Screenshot discipline:** Save **entry**, **mid-trade**, and **stop hit** screenshots with same markup layers visible. Loss review without entry-time screenshot is guesswork — you will rewrite memory to favor ego. S12 journal section uses same three-panel format for winning days too.

**Pre-loss checklist replay:** Re-open the USDCHF chart and run S07 power scoring **as if before entry**. Document IB, IMB, and momentum in journal retroactively. The gap between your retro score and what you felt at click time is the lesson — not the dollar loss.

### Video
`[PENDING]` · Duration: TBD

---

## USDCHF - Find root cause and corrective action

### What it is?

Continuation of the USDCHF loss — Jayce's **root cause analysis (RCA)** method and **one corrective action** for the next week. Root cause is not "market manipulated" — it is the **deepest repeatable process failure** that, if fixed, prevents a **class** of losses.

**RCA levels:**

1. **Symptom** — stopped out on USDCHF long.
2. **Immediate cause** — CHoCH down through POI.
3. **Contributing causes** — no HTF bias, weak momentum, tight stop.
4. **Root cause** — e.g., *"I trade any OB I see without S07 power checklist"* or *"I skip HTF markup on forex crosses."*
5. **Corrective action** — **one** habit change, measurable next 20 trades.

Jayce insists: **one fix at a time**. Traders who rewrite entire system after one loss never build data.

### How to define or apply it?

**5 Whys (USDCHF loss applied):**

1. Why loss? — Price broke below POI and hit stop.
2. Why enter there? — Looked like bullish OB on M15.
3. Why was that OB valid to me? — Saw green candle bounce hope.
4. Why no filter? — Did not run momentum or institutional base score.
5. Why not run checklist? — Rushed after missing prior US30 trade (emotional link).

**Root cause candidate:** *Entry without mandatory pre-trade checklist because of FOMO from prior missed trade.*  
This links US30 Example 3 discipline to USDCHF loss — **chase psychology**, not pair-specific.

**Corrective action examples (pick ONE):**

| Root cause | Corrective action (20-trade trial) |
|------------|-------------------------------------|
| No HTF bias | No entry until D1+H4 screenshot in journal |
| Weak POI | S07 score < 12 = physical hand off mouse |
| No confirmation | Only BOS bounce entries for 2 weeks |
| FOMO after miss | 15-min timer after any missed setup |
| Over size on forex | Max 1% on crosses, 1.5% XAUUSD/US30 only |
| No news check | ForexFactory open on second monitor — mandatory |

**Measure success of fix:** Track **process compliance %**, not win rate, for next 20 trades. Jayce expects win rate to lag 5–10 trades after behavior change.

**Corrective action anti-patterns:**

- "I will never trade USDCHF again" — avoids learning, not fixing process.
- "I will use smaller stop" — tighter stop without better entry = more losses.
- "I need new indicator" — adds complexity before discipline.

### Example

**Jayce's filled RCA sheet for USDCHF loss (course template)**

```
Pair: USDCHF | Date: [replay] | Result: -1.2R
HTF bias documented? NO — root contributor
Liquidity sweep? NO
POI power score: 8/15 — FAIL threshold 12
Momentum: 11/25 — FAIL
Emotional tag: FOMO (missed US30)
ROOT CAUSE: Traded without completing S07 checklist due to FOMO
CORRECTIVE ACTION (next 20 trades): 
  - Complete digital checklist click-through before order; 
  - if any FAIL, close chart 10 minutes
SUCCESS METRIC: 18/20 trades with full checklist YES
REVIEW DATE: [+2 weeks]
```

**Two weeks later (student pattern Jayce cites):**

- Trades taken: 14 (fewer — good).
- Checklist compliance: 19/20.
- USDCHF re-attempt only once with score 14 + H4 alignment — small win or BE; irrelevant.
- **Real win:** US30 double POI skipped once due checklist FAIL on momentum — that skip would have been old-system loss.

**Integration with S12 journal:** RCA row becomes standard column: `Root cause tag` + `Corrective action ID`. After 3 months, pivot table your root causes — top tag gets next month's single fix.

**Jayce closing message for S06:** Examples are not recipes to copy prices — they are **decision trees**. XAUUSD teaches double POI power; US30 teaches patience; EURCAD teaches key level confluence; USDCHF teaches honesty. Pass S14–S15 quizzes, then replay all five on demo same week.

**RCA template download:** Use Resources tab PDF journal format — columns: Pair, Setup type, IB score, IMB score, Momentum, Entry mode, Result, Root cause tag, Corrective action ID, Compliance Y/N. One row per trade; pivot monthly. Students who fill RCA same day improve checklist compliance 2× vs end-of-week batch entry (Jayce Q&A recurring answer).

**Transition to S07:** Every loss in S06 would have been **skipped or downgraded** if signal power section existed in trader's workflow before click. Watch S07 next with USDCHF chart still open — re-score IB+IMB; feel the threshold gap.

**Accountability partner option:** Discord discussion pairs (not signal sharing) — swap RCA sheets weekly. External eyes catch "I knew it was weak but took it anyway" patterns faster than solo review. Jayce endorses peer markup review; forbids peer trade copying.

**Corrective action review at day 14:** If compliance metric under 80% on 20-trade trial, **extend same action** another 20 trades — do not add new fixes. Traders who stack five fixes after one loss rebuild nothing. One habit, six weeks, measured.

### Video
`[PENDING]` · Duration: TBD
