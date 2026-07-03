# S07: How to define the power of Smart Money Signal - New update

*Jayce Pham SMC — Section 7 of 20. **New update** section: ranks POI quality so you stop treating every order block as "90% winrate." Directly answers when to aggressive limit vs wait — and what to do when chart shows both buy and sell SMC.*

---

## Define POI zone power by Institutional base

### What it is?

**Smart Money Signal power** starts with the **institutional base** — the origin zone where institutions accumulated or distributed before the displacement leg that created BOS and FVG. Not every colored OB is institutional; Jayce grades **POI zone power** by how closely the zone matches where smart money actually transacted size.

**Institutional base (definition in this course):**

The last opposing candle cluster (or consolidation) **immediately before** a **violent displacement** candle that:

- Breaks structure (BOS/CHoCH),
- Leaves **imbalance (FVG)**,
- Often follows a **liquidity sweep** or manipulation wick.

**High-power institutional base traits:**

1. **Fresh** — first retest after creation (0–1 prior taps).
2. **Tight** — zone height ≤ 1× ATR on execution TF (not a 80-pip smear on M15).
3. **Displacement origin** — OB is the candle(s) before the impulse, not random mid-trend pause.
4. **Sweep narrative** — liquidity taken before displacement into OB.
5. **HTF alignment** — base sits in correct premium/discount for direction.
6. **Time/session** — formed during London/NY kill zone for that pair (especially US30, XAUUSD).
7. **No mitigation** — price has not fully traded through base body since creation.

**Low-power (fake) OB traits:**

- Mid-range rectangle with no sweep story.
- Tested 3+ times — institutions already exited.
- Formed in Asian chop with no displacement.
- Huge zone — "OB" drawn on 20 candles because indicator said so.
- Against D1 bias without break-trend qualification.

**Institutional base power score (0–15):**

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Freshness | 3+ taps | 2 taps | 0–1 taps |
| Tightness | >1.5 ATR wide | ~1 ATR | <0.7 ATR |
| Displacement quality | None | Moderate BOS | Strong BOS + FVG |
| Liquidity sweep | None | Weak | Clear manipulation |
| HTF zone | Wrong premium/discount | Neutral | Correct half |
| Session | Asia only | Overlap partial | London/NY |

**Interpretation:**

- **12–15:** Strong Smart Money Signal — candidate for double POI + optimized RR.
- **8–11:** Medium — confirmation required (BOS bounce).
- **≤7:** Weak — **not institutional** for Jayce's system; skip or watch only.

This replaces guessing "is this smart money?" with a **number on your journal**.

### How to define or apply it?

**Marking workflow (every POI before trade):**

1. Identify displacement candle — mark it first, work backward to OB.
2. Measure zone height in pips/points; compare ATR(14) on same TF.
3. Count prior taps since OB formed.
4. Document sweep: screenshot liquidity level taken.
5. Score table → sum → write on chart **IB: 13/15** example.
6. If stacking double POI, **both** zones score; use **lower** of two for system decision (weakest link).

**Institutional base + double POI synergy:**

- POI #1 (HTF) scores 14, POI #2 (LTF) scores 11 → trade with **confirmation** on POI #2 even if POI #1 looked set-and-forget eligible.
- Both ≥ 12 → Jayce allows aggressive limit on POI #2 edge (next lesson ties to imbalance).

**Pair notes:**

- **XAUUSD:** Displacement is violent — allow slightly wider OB if H4 origin.
- **US30:** Session open bases score +1 if sweep of overnight high/low clear.
- **Forex crosses (EURCAD):** Add key level confluence from S06 — can add +2 to effective power if daily level intersects OB.

**When institutional base fails after entry:**

- H4 close through base = invalidation, exit per plan — do not re-label OB lower to avoid loss.
- Power was scored wrong — RCA tag `OVERSTATED_IB` in journal (link S06 USDCHF).

### Example

**Compare two bullish POIs on same XAUUSD day**

**POI A — IB score 14:**

- After sweep of H4 equal lows, single large H4 bullish candle; FVG on M15.
- OB = 2 candles, 12 pips on M15, never retested.
- Discount of H4 range; London open displacement.
- **Action:** High power — double POI strategy eligible; limit at retest with stop below sweep.

**POI B — IB score 6:**

- Mid-range M15 consolidation, slow grind up, no sweep.
- OB drawn on 8 candles, 35 pips wide, tested twice last session.
- **Action:** Skip — retail zone labeled SMC. Student forcing this is why Jayce added **New update** signal power section.

**Backtest drill:** Last 20 XAUUSD trades on demo — score IB retrospectively. Plot R-multiple vs score bucket. Course expectation: average R improves sharply above 12.

**Double institutional base stacking:** When H4 OB contains M15 OB from **same displacement event** (not two random OBs), add +1 bonus to IB score — Jayce calls this **nested institutional base**. When two OBs from **different days** overlap, do **not** stack bonus; use lower score only. This distinction prevents over-rating messy charts.

**Mitigation nuance:** Partial wick through OB body is not full mitigation — full **close** through zone on execution TF counts as tap. H4 wick through M15 OB while M15 still holds = M15 trade valid, H4 caution flag −1 point on IB score.

### Video
`[PENDING]` · Duration: TBD

---

## Define POI zone power by Imbalance signal

### What it is?

The second pillar of Smart Money Signal power is the **imbalance signal** — Fair Value Gap (FVG) or inefficiency left by displacement. Institutions often defend POIs that **overlap or sit at the edge of unfilled imbalance** because unfilled FVG represents **unpaid prices** price may revisit before continuing (or reject from when selling).

**Imbalance signal power factors:**

1. **Size of FVG** — larger gap relative to ATR = stronger institutional urgency (not infinite — absurd gaps may be news gaps, separate rules).
2. **Fill status** — **unfilled** or **50% filled** = higher power; **fully mitigated** = FVG signal spent.
3. **Alignment with POI** — OB body **intersects** FVG (ideal) vs POI far from FVG (weaker).
4. **Directional match** — bullish FVG under bullish OB for longs.
5. **Stacked imbalances** — multiple FVGs same direction without fill = **imbalance stack** (very strong on US30 momentum days).
6. **CE (consequent encroachment)** — 50% of FVG as precision entry; Jayce uses for RR optimization inside double POI.

**Imbalance power score (0–10):**

| Factor | Points |
|--------|--------|
| FVG unfilled | +3 |
| 50% CE only touched | +2 |
| Fully filled before POI test | 0 |
| POI overlaps FVG 50%+ | +2 |
| POI adjacent but not overlapping | +1 |
| Stacked FVG (2+) same direction | +2 |
| FVG against HTF bias | −3 (disqualify) |

**Combined signal power (institutional base + imbalance):**

```
Total Power = IB score (0–15) + IMB score (0–10) = 0–25
```

| Total | Label | Jayce default |
|-------|-------|---------------|
| 20–25 | **Strongest Smart Money Signal** | Set & forget eligible + scale plan |
| 15–19 | **Strong** | BOS bounce or limit 50% size |
| 10–14 | **Medium** | Confirmation only, half risk |
| <10 | **Weak / no signal** | No trade |

Course quizzes reference **"strongest case"** Sep 28 live (6R) vs **"weak case"** Sep 27 — difference is largely **total power score** on chart before click.

### How to define or apply it?

**Step-by-step imbalance markup:**

1. After displacement, draw FVG (3-candle rule: gap between wick of candle 1 and wick of candle 3).
2. Mark CE line at 50% of FVG.
3. Extend POI rectangle — highlight **overlap region** with FVG (high-power pocket).
4. Score fill status at moment of potential entry — not at OB creation yesterday.
5. Add IMB score to journal next to IB score.

**Entry placement by imbalance:**

| IMB score | Entry style |
|-----------|-------------|
| 8–10 | Limit at POI–FVG overlap or CE |
| 5–7 | Wait rejection wick + mini BOS |
| <5 | Do not use imbalance as excuse to enter |

**Imbalance traps (2024 update S18 echoes):**

- **FVG fill ≠ automatic reversal** — sometimes fill then continue; need BOS + POI, not "fill and fade" alone.
- **Tiny FVG on M1** — noise, no power.
- **News FVG** — gap may not behave like structural imbalance; skip first hour.

**NCI indicator note (S19):** Imbalance indicator highlights gaps — **you still score power manually**. Tool finds; brain grades.

### Example

**US30 long — stacked imbalance + institutional base**

1. NY open sweep of lows; M5 displacement leaves **FVG #1**.
2. Pullback fills 40% of FVG #1, bounces; second leg up leaves **FVG #2** unfulfilled.
3. Bullish OB at bottom of FVG #1 overlaps CE of FVG #2 pocket.
4. IB score: 13. IMB score: 9 (stacked, POI overlap, CE hold). **Total 22 — strongest case.**
5. Jayce: limit at overlap, stop below sweep, TP at buy-side liquidity — Sep 28 style management (partials + runner).

**USDCHF loss revisited (S06):**

- Small ill-defined "FVG" in chop; fully filled before entry.
- IMB score: 2. IB score: 8. **Total 10** — system says confirmation at best; student took market long. **Signal power math predicted failure.**

**Practice:** Mark 10 historical FVGs on XAUUSD M15; score each; only trade replay entries where total ≥ 15 for 2 weeks demo — compare trade count (lower) and average R (higher).

**CE entry precision:** Consequent encroachment at 50% FVG is where Jayce places limit in **strongest cases** (Sep 28 6R narrative) — tight stop, best RR. Requires total power ≥20; never CE-entry on score 12 just because gap looks clean.

**Imbalance + institutional base conflict:** Rare case: IB 15 but IMB 3 (FVG fully filled before retest). **Total 18 looks tradable** — Jayce downgrades to confirmation only because imbalance energy spent. Power is minimum of story legs, not naive sum only; use judgment column in journal: `IMB spent Y/N`.

**S19 indicator alignment:** NCI imbalance highlight should match your manual FVG — if tool shows gap you did not score, re-draw candles; often wick overlap was misread. Manual score always overrides indicator for entry permission.

### Video
`[PENDING]` · Duration: TBD

---

## When to Set & Forget? When to wait for confirmation?

### What it is?

**Set & Forget** = place limit order at POI (or CE) with stop and TP predefined, **walk away** — no candle-by-candle micromanagement. Works only on **high power** signals and correct session context.

**Wait for confirmation** = no limit at first touch; require **price action proof** — typically **BOS bounce** (M5/M15 structure break in trade direction after POI tap) or **CHoCH** for reversal entries.

Jayce is explicit: beginners should **default confirmation** until journal proves discipline. Set & forget is **optimization for experienced operators**, not laziness.

**Why confirmation matters:**

- Weak POIs fake out first touch — BOS bounce filters 30–40% of losers in Jayce's backtest samples (course claim — verify on your demo).
- Set & forget on medium power = stopped on wick then price runs without you — double pain.

**Set & forget requirements (ALL must be YES):**

| Gate | Requirement |
|------|-------------|
| Power | Total IB+IMB ≥ **20** |
| Momentum | Wave momentum ≥ **20/25** (S05) |
| HTF | D1+H4 same bias |
| Session | London or NY active for instrument |
| News | No high impact in next 60 min |
| Risk | Limit order only — no market chase after miss |
| Psychology | Calm tag — not FOMO |

**Confirmation required when ANY:**

- Total power 10–19.
- First POI touch after long rally (late trend).
- Asian session on US30/XAUUSD unless swing hold.
- Prior trade was loss < 2 hours ago — Jayce suggests confirmation + half size.
- Prop firm challenge near daily drawdown limit.

**Confirmation patterns Jayce uses:**

1. **BOS bounce** — POI tap → internal structure break direction of trade → enter on retest of broken level or 50% of bounce leg.
2. **CHoCH + POI** — for reversals after sweep.
3. **Twin tap** — POI touched twice with rejection wicks, second tap with BOS (US30 re-entry S06).

### How to define or apply it?

**Decision tree (print beside monitor):**

```
POI identified
    → Score IB + IMB + Momentum
        → Total < 10 → SKIP
        → Total 10–19 → CONFIRMATION (BOS bounce)
        → Total ≥ 20 → Check set & forget gates
            → All YES → LIMIT at POI/FVG overlap, alerts on
            → Any NO → downgrade to CONFIRMATION or SKIP
```

**Order types:**

- **Set & forget:** Buy/Sell limit at POI edge or CE; GTC until session end or invalidation; **do not** move limit closer to chase.
- **Confirmation:** No resting limit at first touch; alert when price enters zone; watch for BOS; market or stop entry on retest with defined SL.

**Management differs:**

| Style | After entry |
|-------|-------------|
| Set & forget | Trust SL/TP; optional BE after HTF BOS — no scalping partials if plan was runner |
| Confirmation | Can partial earlier because later entry — worse RR but higher win probability |

**Sep 26 live lesson tie-in:** First trade loss 1.5% — likely confirmation case traded aggressive or power overstated. Later scalps profited with **clearer BOS** entries — same day, different **entry rule discipline**.

**Journal column:** `Entry mode: S&F | CONF` — review monthly which mode fits your personality and score buckets.

### Example

**Case 1 — XAUUSD set & forget valid**

- Double POI after sweep; IB 14, IMB 8, momentum 23 → total 22.
- London open; no news; calm.
- Sell limit at bearish POI–FVG overlap in premium (mirror logic for shorts).
- Stop/TP set; walk away 2 hours. **Correct process.**

**Case 2 — Same chart, 4 hours later, power degraded**

- POI mitigated once; FVG 80% filled; momentum 14.
- Total power now 13.
- Student leaves old limit — **wrong.** Cancel stale limits when fill status changes.

**Case 3 — EURCAD key level (S06)**

- Key level + POI; total 17 — **confirmation zone.**
- Wait H4 rejection wick + M15 BOS down; enter on retest.
- Slightly worse price, better survival rate.

**Homework:** 10 demo trades — force 5 S&F only on score ≥20, 5 CONF on score 15–19. No trades below 15. Submit spreadsheet in Udemy Q&A if stuck — Jayce replies 4–12h.

**Mobile trap:** Set & forget does not mean check phone every 2 minutes moving stop. Either trust bracket orders or use confirmation style and watch session. Prop firm rule violations often come from **manual interference**, not from initial plan.

**Stale limit rule:** Cancel unfilled limits at **session end** if POI not tapped — overnight gap through zone without you is luck, not skill. Re-score next morning; power scores change when FVG fills overnight.

**Beginner default (first 90 days):** Jayce recommends **100% confirmation mode** until 30 journaled trades with ≥85% checklist compliance, then trial set & forget on **one** pair only (XAUUSD or US30).

### Video
`[PENDING]` · Duration: TBD

---

## Risky case: SMC signal on both up and down directions, how to trade?

### What it is?

The **riskiest chart condition** in SMC: at the same time, markup shows **valid-looking buy POI** and **valid-looking sell POI** — both with some institutional base, both near liquidity. Retail freezes or **doubles exposure** betting both directions. Jayce's **New update** rule: **structure hierarchy decides; you do not trade both.**

**Why both-side signals appear:**

- **Range market** — premium OB at top, discount OB at bottom — both "correct" in isolation.
- **Multi-timeframe conflict** — H4 bullish, M15 bearish CHoCH.
- **Overlapping sessions** — Asia range, London sweep both sides same day.
- **Student over-marking** — too many OBs on chart, forcing narratives.

**Danger:**

- Hedging both sides = pay spread twice, guaranteed loss on one, psychological chaos.
- Flipping direction after loss on side A to side B in same range = **revenge roulette**.

**Jayce principle:** *One bias, one direction per instrument per session* unless flat and **new** HTF structure forms after full invalidation of first idea.

### How to define or apply it?

**Hierarchy to break the tie (top wins):**

1. **D1 structure** — bullish BOS → only long POIs unless D1 CHoCH bearish closed.
2. **H4 premium/discount** — in H4 range, **sell premium POI only, buy discount POI only** — never buy premium POI just because it exists.
3. **Liquidity objective** — which side has **un swept** liquidity magnet? Price often moves to liquidity **before** reversing — trade **with path to liquidity** first (not forever).
4. **Higher total power score** — buy POI 12 vs sell POI 18 → **sell only**.
5. **HTF POI vs LTF POI** — HTF wins when conflict.
6. **If still tied (score within 2 points)** → **NO TRADE** — best edge is skip.

**Both-side decision table:**

| Condition | Action |
|-----------|--------|
| D1 up, sell POI in H4 premium, buy POI in discount | Trade **one**: either sell premium setup OR wait discount long after sell completes — **not simultaneous** |
| D1 up, buy POI in premium (weak) | **Skip long** — premium buys against value rule |
| Range, equal power both sides | **Skip** until sweep + CHoCH |
| Sweep highs then bearish BOS | **Short only** until invalidation |
| Sweep lows then bullish BOS | **Long only** until invalidation |

**TF/2 standard (S18 2024 update preview):** When LTF signal conflicts HTF, use **HTF for bias, LTF/2 or LTF for entry** only in direction of HTF — do not take LTF counter signal as full trade.

**Practical session rule:**

- Mark **both** POIs if you see them — transparency.
- Circle **active** POI per hierarchy; gray out the other.
- If price hits gray POI, **no trade** — wait for active side or reassess after H4 close.

### Example

**XAUUSD inside H4 range — classic both-side trap**

**Chart:**

- Range high liquidity unswept at $2,0XX.
- Range low liquidity already swept this morning.
- Bearish OB at premium near high (sell signal).
- Bullish OB at discount near low (buy signal).

**Wrong retail:**

- Buy discount because "support" + sell premium because "resistance" — both open.

**Jayce hierarchy:**

1. D1 still bullish bias — prefer longs **but** discount POI already used after sweep; now price mid-range.
2. **Unswept liquidity at range high** — magnet up first.
3. Sell POI at premium only **after** sweep of highs + bearish BOS **if** D1 allows reversal; OR
4. Wait for high sweep, then **long** from POI if bullish continuation (trend-follow) with new displacement.

**Actual playbook Jayce demonstrates:**

- Morning: swept lows → long from discount POI (power 21) — **one direction**.
- Afternoon: price at premium, sweep highs, bearish BOS, sell POI (power 19) — **after** long closed or invalidated — **not overlapping**.

**US30 both-side NY open:**

- Overnight high and low both marked; double POI short after high sweep **wins** over low buy POI because sweep narrative + BOS down first — buy POI invalidated when low breaks.

**Journal tag:** `BOTH_SIDE_SEEN` → document which rule picked winner → if skipped, tag `SKIP_TIE` — Jayce says skips are **A+ trades**.

**Final exam preview (S17):** Expect question on both-side chart image — correct answer is often **no trade** or **trade liquidity side after sweep**, never hedge both.

**Mindset close:** SMC gives many **possible** entries; professionals earn from **filtered** entries. Signal power + hierarchy turns chaos into one click or zero clicks — zero is valid.

**Hedging myth:** Some brokers allow lock positions; Jayce does **not** teach hedge-both-sides as strategy — doubles spread, masks indecision, breaks prop firm rules on many platforms. Pick hierarchy winner or flat.

**Re-score after sweep:** Both-side charts often resolve after **one** liquidity pool clears. When highs sweep, recalculate power on bearish POI only; bullish discount POI may invalidate if lows break. Dynamic reassessment every H4 close prevents frozen bias.

**Section 7 completion checklist:**

- [ ] Score IB + IMB on 5 historical charts without trading
- [ ] Label each S&F vs CONF decision in writing
- [ ] Document one both-side skip with hierarchy reasoning
- [ ] Pass S15 advanced quiz signal-power questions before S08 live sessions

### Video
`[PENDING]` · Duration: TBD
