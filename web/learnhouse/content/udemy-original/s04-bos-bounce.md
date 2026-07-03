# S04: Main — Double Order Block with BOS bounce

*Continuation mastery: BOS confirms trend, price bounces from double OB POI — tighter entries than pullback-only, optimized for scalps and intraday gold.*

---

## Double OB with BOS bounce

### What it is?

**Double OB with BOS bounce** is the continuation variant of the main strategy — after trend is established, price breaks structure (BOS), pulls back to **nested orderblocks**, and **bounces** with a fresh BOS on your entry timeframe without reversing character (no CHoCH against trade). Unlike generic pullback trading, **BOS bounce** demands the pullback itself end with a **mini BOS** in trend direction from the POI — proof that smart money defended the double OB and resumed expansion. The bounce is the market saying "we held the zone, now we move" — not your opinion, but structure confirmation.

Think of it as: HTF double OB defines the zone; LTF prints structure **only in trend direction** (bullish BOS in uptrend = continuation character, not reversal); then **BOS bounce** from POI is your trigger. This setup powers many Jayce **live session** entries on XAUUSD M5/M15 — high signal power, tight stop, quick partials at internal liquidity. Where S03 follow-trend can hold for days, BOS bounce can deliver 1:2 to 1:4 RR in hours with the same footprint logic.

The bounce distinguishes **absorption** from **failure**. Price taps POI, holds, displaces — BOS. Price taps POI, collapses through — CHoCH, switch to break-trend logic. BOS bounce keeps you in **follow trend** with precision timing for prop firm **low drawdown** targets. Prop firms care about daily drawdown limits — BOS bounce entries with 5-point stops on gold vs 15-point pullback-only stops mean you can take the same trade idea three times before hitting daily limit. Optimized RR is not just about target distance; it is about stop distance, and BOS bounce minimizes stop distance.

Jayce uses BOS bounce as the **intraday execution layer** on top of S03 swing framework. H4/H1 define the double OB zone (S03); M15/M5 define the bounce trigger (S04). You can have a valid S03 POI without taking it until S04 BOS bounce confirms on your execution TF. This stacking reduces false entries by roughly 30% in Jayce's backtest journal — the cost is occasionally missing the absolute best price by 2–5 points, but the saved stop-outs more than compensate. Set & Forget applies to swing bounces; scalpers take partial at first internal liquidity and trail.

### How to define or apply it?

1. Confirm HTF trend and mark **double OB POI** (H4 + H1 or H1 + M15).
2. Wait for pullback into POI in correct **premium/discount**.
3. On execution TF, watch for **hold** at POI — wick rejection, FVG CE respect, no close through OB.
4. **BOS bounce trigger:** candle **close** breaks minor swing in trend direction **after** POI touch.
5. Enter on BOS close or limit at 50% of bounce candle body; stop below/above POI OB.
6. TP1: nearest imbalance or internal high/low; TP2: HTF liquidity (BSL/SSL).
7. Sequence is mandatory: POI touch → hold → BOS. Never reverse this order.
8. BOS bounce candle should leave mini FVG — confirms displacement, not slow grind.
9. If POI touched but no BOS within 12 M15 candles (3 hours), setup weakening — reduce size or skip.
10. Scalp variant: M5 BOS bounce inside M15 POI during London open gold.
11. Swing variant: H1 BOS bounce inside H4 POI, hold to daily BSL/SSL.
12. **Chart rule:** BOS before POI touch = chasing — wait sequence POI → hold → BOS.
13. **Chart rule:** BOS bounce invalid if simultaneous HTF CHoCH against trade.
14. **Chart rule:** Wick-only BOS on M5 = weak; require M5 body close for scalp entries.
15. Set & Forget swing variant: trail stop only after TP1 at internal liquidity hit.

### Example

**Historical XAUUSD — H4/H1/M15/M5 intraday BOS bounce long, September 2024.**

**Context:** H4 uptrend, D1 HH/HL intact. Prior SSL swept at **2330**. H4 bullish BOS at **2355**. Dealing range **2330–2355**, EQ **2342.50**.

**Double OB POI:**
- H4 bullish OB: **2338–2342** (discount)
- H1 nested OB: **2339–2341**
- FVG overlap: **2338.50–2340.50**
- POI center: **2340.00**

**Pullback:** H1 drift from **2355** into zone over 18 hours. Price entered POI at **2340.00** — H1 pin bar rejection, wick to **2338.80**, close **2340.50**. Hold confirmed.

**M15 sequence:** POI touch **2340.00** → 3 consolidation candles → M15 **bullish BOS** close above swing **2342.50** at **2343.00**. BOS bounce trigger fired.

**M5 refinement:** M5 BOS above **2342.80** after M15 trigger — Jayce live entry layer. Entry **2342.00** (M5 BOS close), stop **2337.00** (below H1 OB), TP1 **2350** (internal liquidity), TP2 **2356** (BSL).

**Contrast — early entry:** Trader long at **2340** on POI touch without BOS — stopped when M5 wicked to **2336.20** during absorption (-4 pts). BOS bounce entry at **2342** survived wick, captured move to **2354** (+12 pts). RR **1:2.4** to TP1, **1:2.8** to TP2.

**Result:** TP1 hit **2350** (+8 pts) in 4 hours. TP2 nearly hit **2355** (+13 pts) same session. No M15 CHoCH bearish during trade — character intact.

**Signal power:** HTF trend ✓, double OB ✓, discount ✓, POI hold ✓, BOS bounce ✓. Score **5/5**.

Live session Sep 26–29 (course S08–S11) repeats this mechanic on US30 and gold — mark POI, wait bounce BOS, execute Set & Forget with fixed risk %. Student exercise: replay this date on M5, mark POI touch time vs BOS time, calculate RR difference vs early entry.

### Video
`[PENDING]`

---

## Power of double order block zone

### What it is?

The **power of double order block zone** is **confluence stacking** — when two timeframes' OBs overlap, institutions defended **both** levels; liquidity pools cluster; FVG often sits inside the overlap; stops can be tighter; RR to same target increases dramatically. Single OB might get violated on first tap; **double OB zone** survives multiple tests and produces **higher win rate** in Jayce's backtests across XAUUSD and indices. The overlap is the smallest rectangle on your chart with the largest institutional meaning — that is where Jayce's "POI to optimize RR" title comes from.

Power increases with five factors: (1) HTF trend alignment, (2) premium/discount correct half, (3) prior liquidity sweep, (4) imbalance inside zone, (5) manipulation wick into zone before bounce. Five factors = **maximum signal power** — course S07 expands this into "Smart Money Signal power" scoring. Double zone is also **visual filter** — if H1 OB sits outside H4 OB, downgrade to single OB trade or skip. Misaligned OBs mean different timeframes disagree on where institutions defend; the overlap is the handshake between timeframes.

Retail draws one rectangle on M15; SMC operator draws **nested zones** and waits for price to enter the **overlap** — the smallest rectangle with largest institutional meaning. Optimized RR from S03 title comes from this overlap: entry at center of double zone, stop outside HTF OB edge, target unchanged at far liquidity. Example: HTF target 40 points away. Single OB entry requires 12-point stop. Double OB overlap entry requires 5-point stop. Same target, RR goes from 1:3.3 to 1:8. That is not theory — it is position sizing math that prop firms reward.

**Triple OB** (D1 + H4 + H1) is rare but elite — Jayce marks perhaps 2–3 per quarter on gold. When all three align, signal power is maximum and Set & Forget swing holds can run for weeks. The power lesson also includes **downgrade rules**: H1 bearish OB inside H4 bullish OB during H4 uptrend is not conflict — the H1 OB is your LTF entry refinement inside H4 zone. Conflict is H1 bearish OB **outside** H4 bullish OB — different story, different trade mode (potential CHoCH, not bounce).

### How to define or apply it?

1. Always draw **outer OB (HTF)** first, then **inner OB (LTF)** — shade overlap region distinctly.
2. Score zone power 1–5 using checklist: trend, sweep, FVG, premium/discount, manipulation.
3. **Trade only overlap** when possible — entry mid-zone, not at stray wick outside overlap.
4. If inner OB breaks but outer holds, watch **Case 1** second mitigation (S03 break-trend).
5. If both break with body closes, zone **failed** — re-mark after new BOS, no hope trading.
6. Measure zone width — if >1.5× ATR on entry TF, use CE or inner OB for precision entry.
7. Mark zone power score on chart before every entry — builds discipline and journal data.
8. Triple OB (D1+H4+H1): shade innermost overlap; this is elite POI for swing Set & Forget.
9. Zone power 4–5: full risk size. Power 3: half size. Power 1–2: skip.
10. Combine with BOS bounce trigger for entry timing inside powerful zone.
11. Retest count: first test of overlap = strongest; third test = weakest (consider skip).
12. **Chart rule:** Triple OB (D1+H4+H1) = elite POI — rare, highest RR swings.
13. **Chart rule:** Double OB against HTF trend = reversal POI only with CHoCH, not bounce.
14. **Chart rule:** Overlap <5 pips on forex / <$3 on gold = precision entry required, no market orders.
15. Journal zone power score vs outcome monthly — prove which scores deserve live risk.

### Example

**Historical US30 — D1/H4/H1 triple-stack power, November 2024.**

**Context:** Dow D1 uptrend from **38200** low. H4 markup, SSL swept at **38650** prior week. BSL target **39200** (all-time high area). D1 bullish BOS at **39000**.

**Triple OB stack:**
- D1 bullish OB: **38700–38800** (outermost)
- H4 OB: **38750–38780** (inside D1)
- H1 OB: **38760–38770** (innermost — core overlap)
- Overlap center: **38765**
- H4 FVG: **38720–38745** (filled into zone during pullback)

**Zone power score:**
1. HTF trend alignment: D1/H4 bullish ✓ (+1)
2. Liquidity sweep: SSL 38650 taken ✓ (+1)
3. FVG inside zone: 38720–38745 ✓ (+1)
4. Premium/discount: pullback to discount (below EQ 38900 of 38650–39000 range) ✓ (+1)
5. Manipulation: minor dip to 38755 wick, rejected ✓ (+1)
**Total: 5/5 — maximum signal power**

**Pullback:** 48-hour drift from **39000** into triple overlap. H1 tested **38765** twice — both held with pin bars.

**Entry:** Long **38765** (overlap center), stop **38740** (below H1 OB), target **39200** BSL. RR **1:17.4** (435 points target / 25 points risk).

**Contrast — single OB trader:** H1 OB only at **38720** (outside overlap, below H4 zone). Entry **38720**, stop **38700** (20 pts), same target **39200**. RR **1:24** looks better but stop hit on wick to **38695** during first test — stopped out (-20 pts). Triple-zone trader at **38765** survived both tests.

**Result:** US30 rallied to **39180** over 6 days (+415 pts). TP nearly hit. Set & Forget.

**Downgrade example (same week, different setup):** H1 bearish OB at **39000** but H4 bullish OB at **38750** — **no overlap**, power **2/5**. Jayce journal: "Skip — misaligned zones. Not double OB, not POI." Price later dropped to H4 zone at 38750 where valid long existed. Structure placement, not luck.

**Power lesson:** **Width of zone ≠ power** — **nested alignment** = power. Jayce: "POI to optimize RR means find overlap, not farthest target."

Student exercise: score 10 historical US30/XAUUSD setups 1–5, compare win rate by score bucket.

### Video
`[PENDING]`

---

## Market cycle theory _ Cornerstone for Price action and Market structure

### What it is?

**Market cycle theory** is the **cornerstone** linking Wyckoff, SMC phases, and everything in S02–S04. Price cycles through **accumulation** (smart money buys, range, SSL tests), **markup** (BOS up, follow trend POIs, expanding highs), **distribution** (BSL sweep, CHoCH, premium POIs, weakening displacement), and **markdown** (bearish BOS, break trend, SSL targets). Ranges are not random — they are **institutional inventory** phases before the next leg. When you know the cycle phase, you know which playbook to open — S03 follow trend or S03 break trend or S04 BOS bounce.

SMC footprint maps to cycle: test liquidity = spring in accumulation; absorbing = inside range; imbalance = start of markup/markdown; manipulation = spring/upthrust at cycle turn; POI = edge of value; retail + institutions together = breakout from range **after** smart money positioned. Without cycle lens, BOS and CHoCH are isolated events; with it, you know **which playbook** — follow trend in markup, break trend at distribution, **stand aside** in late markdown before next accumulation unless clear POI. Jayce's Sunday weekly prep for XAUUSD starts with one label: "We are in ___ phase." That label determines which course section is active.

Jayce uses cycle theory to **filter sessions**: trade aggressive follow trend + BOS bounce in markup; trade break trend at distribution; **stand aside** in late markdown before next accumulation unless clear POI. Elliott wave intro (S05) extends this; cycle is the **practical** desk version for XAUUSD weekly planning. You do not need to count waves — you need to identify whether institutions are building inventory (range), expanding (trend), or offloading (reversal). The cycle answers the question every student asks: "Why did my follow-trend long fail?" — Because the cycle shifted to distribution and you applied markup playbook to distribution price action.

The cycle also explains **phase sequencing** from S02. Accumulation is heavy Phase 0–1 (liquidity tests, absorbing). Markup is Phase 2–5 repeating (imbalance, manipulation on pullbacks, POI entries, expansion). Distribution is Phase 0–3 at the top (sweep, imbalance down, manipulation up, CHoCH). Markdown is Phase 4–5 repeating on the downside. Full cycle is macro; footprint phases are micro within each cycle leg. Both required for **real result** Jayce promises in intro — not indicator gambling.

### How to define or apply it?

1. **Identify phase** on D1/H4: range = acc/dist; trend = markup/markdown.
2. **Accumulation signs:** compression, repeated SSL sweeps, failure to make new lows, bullish CHoCH to start markup.
3. **Markup signs:** HH/HL, BOS sequence, pullbacks to discount double OB, BOS bounces.
4. **Distribution signs:** HH slowing, BSL sweeps, bearish CHoCH, premium POIs failing to reach new highs.
5. **Markdown signs:** LH/LL, bearish BOS, rallies to premium POI for shorts.
6. Match strategy: markup = S03 follow trend + S04 BOS bounce; distribution = break trend Cases 1–3.
7. Transition phases are choppy — reduce size 50% until BOS confirms new phase.
8. Late markdown before accumulation: stand aside unless clear SSL sweep + CHoCH bullish at range low.
9. Weekly prep: label XAUUSD "cycle phase" in journal before Monday.
10. Monthly review: which phase produced most RR? Usually markup follow-trend and distribution break-trend.
11. Cycle phase on D1 governs; H4 can be one phase ahead (early distribution while D1 still markup) — caution zone.
12. **Chart rule:** Do not apply markup longs in distribution — win rate collapses.
13. **Chart rule:** Transition phases choppy — reduce size until BOS confirms new phase.
14. **Chart rule:** Accumulation ranges can last weeks — patience, do not force trend trades inside range.
15. Replay historical year marking only cycle phases — pattern recognition in 2 hours.

### Example

**Historical XAUUSD — D1/H4 full cycle quarter, Q1–Q2 2024.**

**Q1 Accumulation (January–February) — 1980–2000:**
Repeated SSL sweeps to **1975–1980**, H4 range compression, failure to make new lows below **1978**. Smart money accumulating long inventory. D1 candles showing long lower wicks at SSL. Bullish CHoCH on H4 at **1995** signaled markup beginning. Playbook: watch for long POI on CHoCH, not aggressive shorting of range lows.
- Trades: 2 long POIs at **1988** and **1992** (discount), both +15–20 pts. No shorts inside range.

**Markup (February–April) — 2000→2080:**
Series of H4 bullish BOS: **2010, 2035, 2060, 2080**. Follow trend double OB entries every pullback:
- Long at **2015** (H4/H1 double OB), target **2035**, RR 1:5, +20 pts
- Long at **2042** (BOS bounce M15), target **2060**, RR 1:3.5, +18 pts
- Long at **2065** (discount POI), target **2080**, RR 1:4, +15 pts
BOS bounces on M15 inside H4 POI — S04 entries every 5–8 days. Win rate ~70%.

**Distribution (April–May) — 2070–2085:**
HH slowing — H4 BOS at **2080** weak displacement, small FVG. BSL sweep **2088**, H4 bearish CHoCH below **2070**. Premium bearish double OB **2075–2082**. Playbook switch: break trend Case 3 short.
- Short at **2078**, stop **2092**, target **2040**, RR 1:2.7, +38 pts

**Markdown (May–July) — 2080→2020:**
Bearish H4 BOS sequence: **2060, 2040, 2020**. Short POIs in premium on every rally:
- Short at **2055** (premium POI), target **2030**, +25 pts
- Short at **2048** (BOS bounce), target **2025**, +23 pts
No longs until new accumulation base forming at **2020**.

**Trader error case:** Trader applied follow-trend longs during **distribution** (April, entries at **2075** POI in premium) — lost on 3 consecutive pullbacks (-8, -12, -10 pts). Same trader switching to **break trend** at CHoCH **2070** captured markdown (+38 pts) and subsequent shorts (+48 pts net).

**Cycle cornerstone answer:** "Which section of course applies **this week**?" — Not random strategy hopping. January = accumulation watch. March = S03+S04 markup. May = S03 break trend. June = markdown shorts only.

Connect to phases 0–5: full cycle is macro; footprint phases are micro within each cycle leg. Student exercise: mark Q1–Q2 2024 XAUUSD D1 chart with 4 cycle labels, count trades per phase, calculate profit % per phase.

### Video
`[PENDING]`

---

## Difference between BOS/Key level and POI

### What it is?

Students confuse **BOS/key level** with **POI** and enter at wrong price — this lesson separates them permanently. **BOS/key level** is a **structure line** — swing high/low, break point, equilibrium, session high. It tells you **what happened** (structure broke, level holds narrative). **POI** is a **zone** (orderblock overlap) where you **place orders** — it tells you **where to execute** with stop and target. BOS is the alarm clock; POI is the address where you show up. Confusing them is why retail shorts at the BOS break level and gets stopped on retest — they entered at the alarm, not the address.

BOS is **confirmation**, not entry. Key level from NCI Level 1 is broader support/resistance from higher timeframe swings. POI is SMC-specific refined OB after liquidity + premium/discount. You can have BOS **at** key level without valid POI (no OB overlap = chase). You can have POI **below** key level in discount (better RR) while BOS already printed higher. The ideal sequence: key level sets narrative → BOS confirms timing → POI defines price. Never reverse. Retail reverses it daily: sees key level break (narrative), enters at break (no POI), stop hit on retest to POI they did not wait for.

**BOS bounce** = event at structure (timing). **Double OB POI** = location for risk (price). Key level break **without** return to POI = breakout chase (retail). Key level break, retest POI, BOS bounce = Jayce system. Signal power combines: BOS confirms **timing**; POI defines **price**; key level confirms **narrative** on weekly map. All three together = maximum confluence. Any one alone = incomplete trade plan.

Jayce summary for this lesson: "BOS/key level = brain; POI = hand." Double OB BOS bounce = brain says go, hand pulls trigger at zone. The brain without the hand enters at wrong price with wide stop. The hand without the brain enters at beautiful POI against trend with no CHoCH/BOS gate. Master difference before S06 live cases and S07 signal power scoring. This lesson prevents the most common funded account failure: right direction, wrong entry, tight stop at wrong level.

NCI Level 1 key level + Level 2 SMC POI = full stack for funded accounts. Key level tells you the weekly battlefield; POI tells you where to dig foxhole. BOS tells you when the battle shifted. Students who complete both levels trade smaller but more precisely — prop firm metrics improve because stop distance shrinks while target distance stays the same. That is optimized RR in one sentence.

### How to define or apply it?

1. **Key level:** horizontal from HTF swing, session open, obvious S/R — mark with **line** (thin, one price).
2. **BOS:** dynamic structure break — mark with **label** at break candle (not a zone).
3. **POI:** shaded **rectangle** — double OB overlap only (zone, not line).
4. Workflow: key level sets bias → BOS confirms phase → POI sets entry — **never reverse order**.
5. Entry checklist: "Is this a line or a zone?" — lines are alerts; zones are orders.
6. If price at key level but not in POI, **wait** — do not equate them.
7. Key level break is not entry — wait for retest of POI near or beyond key level.
8. Multiple key levels can exist; only one POI is valid per setup (the double OB overlap).
9. BOS can occur far from POI — do not enter at BOS price, wait for pullback to POI.
10. **Chart rule:** POI can exist without BOS (limit anticipation) — advanced; default wait BOS bounce.
11. **Chart rule:** BOS at key level without POI nearby = often liquidity event, not entry.
12. **Chart rule:** Do not shade key level as POI — different tools, different purposes.
13. NCI Level 1 key level + Level 2 SMC POI = full stack for funded accounts.
14. Quiz: screenshot chart, cover POI — can you still see where to enter? If no, you marked only lines.
15. Journal every loss tagged "BOS entry" vs "POI entry" — quantify the cost of confusion.

### Example

**Historical EURUSD — D1/H4/M15 BOS vs POI confusion resolved, August 2024.**

**Context:** **1.0800** major H4/D1 key level (prior year support, now resistance after break). EURUSD broke down through **1.0800** in July. D1 bearish bias. Traders watching retest of **1.0800** for short continuation.

**Panel A — Wrong entry (BOS chase):**

H4 broke below **1.0785** (minor swing low) — **bearish BOS** printed. Retail shorted **1.0785** immediately on "BOS breakdown, momentum!" Stop **1.0795** (tight, at key level). Price rallied to retest **1.0800** key level and POI zone — stopped at **1.0795** (-10 pips). Direction was correct (eventually dropped), entry was wrong.

**Panel B — Correct entry (POI + BOS bounce):**

SMC analysis: POI was **bearish double OB 1.0795–1.0802** in **premium** (above EQ 1.0750 of current leg) — retest zone above broken key level **1.0800**. This is the address, not the alarm.

Price rallied from **1.0785** to **1.0798** (into POI, tagged key level **1.0800**). H1 pin bar rejection at **1.0799**. M15 **bearish BOS** at **1.0792** after POI touch — BOS bounce (timing confirmed).

**Trade:** Short **1.0793**, stop **1.0805** (above POI + key level), target **1.0720** SSL. RR **1:6.1**.

**Result:** EURUSD dropped to **1.0725** over 3 days (+68 pips). POI entry survived retest; BOS chase entry stopped.

**Panel C — CHoCH vs POI (second lesson in same example):**

**CHoCH** at **1.0820** (structure event — character changed from bullish correction to bearish resumption). **POI** at **1.0810–1.0815** (zone, 10 pips below CHoCH level). CHoCH told reversal narrative; POI gave entry **10 pips better** with **tighter stop** (5 pips vs 15 pips if entering at CHoCH break).

Short at POI **1.0812**, stop **1.0818**, target **1.0750**. RR **1:10.3**. Result: +62 pips.

**Key level 1.0800** was narrative ("support failed, now resistance"). Not the short entry button. BOS at **1.0785** was timing alarm for those already positioned — not entry for new shorts.

**Jayce summary table:**
| Element | Type | Function | Entry? |
|---------|------|----------|--------|
| Key level 1.0800 | Line | Narrative/bias | NO — alert only |
| BOS 1.0785 | Event | Timing confirm | NO — wait POI |
| POI 1.0795–1.0802 | Zone | Execution | YES — after BOS bounce |
| CHoCH 1.0820 | Event | Reversal gate | NO — wait POI |

**Profit % difference:** BOS chase -1R. POI entry +6.1R. Same week, same pair, same direction. Brain + hand = funded account. Brain only = blown account.

Student exercise: find 5 charts where you entered at BOS instead of POI. Recalculate RR if you had waited for POI. Journal the cumulative pip difference.

Master difference before S06 live cases and S07 signal power scoring.

### Video
`[PENDING]`
