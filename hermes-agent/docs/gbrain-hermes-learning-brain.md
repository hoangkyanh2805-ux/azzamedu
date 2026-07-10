# GBrain + Hermes Learning Brain

> Decision doc: convert video-heavy LearnHouse courses into a long-term knowledge brain for Hermes-powered learner care.

## Goal

Build a learning support system where:

- LearnHouse stores the course experience.
- Course videos are converted into structured knowledge.
- GBrain stores long-term knowledge, citations, graph links, gaps, and nightly synthesis.
- Hermes talks to learners, checks GBrain before answering, remembers progress, and runs follow-up automations.

Hermes is the coach interface. GBrain is the long-term brain behind the coach.

## 5W1H

| Question | Answer |
|---|---|
| What | GBrain stores course knowledge, learner progress, concept maps, citations, repeated mistakes, and knowledge gaps. |
| Why | Hermes alone can forget context or answer without source grounding. GBrain gives retrieval, graph, citation, gap analysis, and dream-cycle review. |
| Who | Learners, Hermes coach, admin/mentor, and course/content team. |
| When | Before Hermes answers, after each learner interaction, during daily/weekly cron review, and whenever course content changes. |
| Where | Markdown source in this project; GBrain index/database local first, cloud later; Hermes runtime via CLI/gateway/cron. |
| How | Video -> transcript -> lesson notes -> concepts/checklists/quizzes -> GBrain import -> Hermes query/update loop. |

## Storage Model

Use three layers:

```text
1. Brain source repo
   Markdown files, course maps, transcripts, concepts, rubrics, learner state.

2. GBrain database/index
   Local PGLite first; Postgres/Supabase later when multiple agents/users need shared cloud access.

3. Hermes memory/runtime
   Chat sessions, agent skills, scheduled follow-ups, gateway integration.
```

Recommended project location:

```text
knowledge/project-maps/alpha-elite/learning-brain/
  README.md
  courses/
  lessons/
  transcripts/
  concepts/
  exercises/
  quizzes/
  rubrics/
  learners/
  learner-sessions/
  submissions/
  mistakes/
  reports/
```

Keep video files outside the brain index unless needed for audit:

```text
course-media/
  market-structure/
    03-valid-pullback.mp4

knowledge/project-maps/alpha-elite/learning-brain/
  transcripts/
  lessons/
  concepts/
```

GBrain stores references to the video and timestamps, not the raw video itself.

## Video-To-Brain Pipeline

Most course material is video, so the ingestion path is:

```text
LearnHouse video / MP4 / YouTube unlisted
-> audio extraction
-> speech-to-text transcript
-> timestamped transcript markdown
-> lesson note
-> concept cards
-> checklist/rubric
-> exercise/quiz
-> GBrain import/index
```

For each important video, generate five assets:

```text
transcripts/<course>/<lesson>.transcript.md
lessons/<course>/<lesson>.md
concepts/<concept>.md
exercises/<exercise>.md
quizzes/<lesson>-quiz.md
```

Transcript is the source memory. Lesson notes and concept cards are the teachable knowledge layer.

## File Formats

### Transcript

```markdown
---
type: transcript
course: market-structure
lesson: valid-pullback
source_video: course-media/market-structure/03-valid-pullback.mp4
duration: 00:42:10
---

# Transcript: Valid Pullback

## 00:00-03:20
Introduction and context.

## 03:21-08:45
Definition of a valid pullback.

## 08:46-14:30
Chart example and application.
```

### Lesson Note

```markdown
---
type: lesson
course: market-structure
lesson: valid-pullback
source_transcript: transcripts/market-structure/valid-pullback.transcript.md
concepts:
  - valid-pullback
  - trend-continuation
  - structure-break
---

# Valid Pullback

## Learning Goal

Learner can distinguish a valid pullback from a reversal.

## Key Ideas

- Pullback only makes sense inside trend context.
- A valid pullback should not invalidate the main structure.
- Confirmation is required before treating continuation as likely.

## Checklist

1. Is the higher timeframe trending or ranging?
2. Has the main structure been broken?
3. Which zone did price pull back into?
4. Is there continuation confirmation?

## Common Mistakes

- Entering before confirmation.
- Confusing pullback with reversal.
- Looking only at the lower timeframe.

## Citation

Source: `03-valid-pullback.mp4`, `03:21-14:30`.
```

### Concept Card

```markdown
---
type: concept
name: valid-pullback
course: market-structure
related_lessons:
  - lessons/market-structure/valid-pullback.md
prerequisites:
  - trend
  - swing-high-low
  - market-structure
---

# Valid Pullback

A valid pullback is a temporary retracement inside the main trend that does not invalidate the larger structure.

## Signs

- Price moves temporarily against the main trend.
- The larger HH/HL or LH/LL structure remains intact.
- Price often returns into a key zone, order block, FVG, or liquidity area.

## Common Learner Mistakes

- Treating every drop as reversal.
- Ignoring higher timeframe context.
```

## Knowledge Graph

GBrain should connect these entities:

```text
learner -> enrolled_in -> course
learner -> completed -> lesson
learner -> struggles_with -> concept
learner -> submitted -> chart_review
lesson -> teaches -> concept
concept -> prerequisite_of -> concept
mistake -> remediated_by -> exercise
quiz -> checks -> concept
report -> summarizes -> learner
```

Example:

```text
nguyen-van-a
-> struggles_with -> pullback-vs-reversal
-> assigned -> mark-5-valid-pullbacks
-> source_lesson -> market-structure/valid-pullback
```

## Hermes Runtime Behavior

Create a Hermes skill named `azzam-learning-coach`.

Skill responsibilities:

- Query GBrain before answering course questions.
- Cite the source lesson/timestamp when available.
- Ask diagnostic questions before giving explanations.
- Update learner progress after meaningful interactions.
- Detect repeated mistakes and assign remediation.
- Refuse personalized trade calls/signals; keep responses educational.
- Create gap notes when GBrain lacks a concept, citation, or exercise.

Learner question flow:

```text
Learner asks Hermes
-> Hermes detects intent
-> Hermes queries GBrain
-> GBrain returns synthesis + citations + gaps
-> Hermes responds as coach
-> Hermes writes learner session/progress back to brain
```

Chart review flow:

```text
Learner submits chart
-> Hermes asks learner to mark structure/range/pullback
-> Hermes queries rubric/checklist from GBrain
-> Hermes reviews reasoning, not trade entry
-> Mistake and next exercise are stored
```

## Dream Cycle

Daily or nightly job:

- Find learners inactive for 3 days.
- Find repeated mistakes by learner.
- Find concepts with many learner failures.
- Generate daily follow-up list.
- Generate weekly learner summaries.
- Detect missing transcripts, citations, quizzes, or rubrics.
- Deduplicate similar concept cards.

Output examples:

```text
reports/daily/2026-07-10.md
reports/weekly/2026-W28.md
gaps/missing-citations.md
gaps/lesson-needs-quiz.md
```

## Cost And Setup

Start local, then move to cloud only when learner usage requires it.

| Stage | Storage | Hosting | Cost Profile |
|---|---|---|---|
| MVP local | Markdown + PGLite | Local machine | Near $0 except LLM/transcription API |
| Small online | Markdown + PGLite/Postgres on VPS | VPS | Roughly $5-20/month plus LLM/API |
| Production | Git repo + Supabase/Postgres/pgvector | VPS/Railway/Fly/Render | Roughly $10-50+/month plus LLM/API |

Main variable cost is not GBrain. It is:

- Transcription for video.
- Embeddings/reranking for retrieval.
- LLM responses to learners.
- Optional cloud database/hosting.

## Simple Effective MVP

Phase 1:

1. Create `learning-brain` folder structure.
2. Pick one course: Market Structure.
3. Convert 5-10 important videos into timestamped transcripts.
4. Distill each video into lesson note, concept card, checklist, quiz, and exercise.
5. Import/index with GBrain locally.
6. Create Hermes skill `azzam-learning-coach`.
7. Test against real learner questions.

Phase 2:

1. Add Telegram gateway through Hermes.
2. Store learner sessions in the brain.
3. Add daily follow-up and weekly progress reports.
4. Ingest the remaining three courses.

Phase 3:

1. Move database to shared Postgres/Supabase if needed.
2. Add admin dashboard/reporting.
3. Add automated gap checks and content improvement queue.

## Non-Negotiables

- Do not place full course content directly inside Hermes prompts.
- Keep raw transcript with timestamp for citation.
- Keep lesson/concept/checklist/exercise separate.
- Store learner state as structured markdown/YAML, not only chat history.
- Maintain trading education boundaries: no personalized buy/sell signals.
