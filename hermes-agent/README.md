# Hermes Agent Workspace

> Home base for everything related to Hermes agent design, learner-care automation, and GBrain-backed knowledge workflows.

## Purpose

This folder groups all Hermes-related planning and future implementation assets so they do not get scattered across the repo.

Hermes is the learner-facing coach layer:

- Talks to learners through CLI/gateway channels.
- Queries GBrain before answering course questions.
- Writes learner progress and sessions back into the learning brain.
- Runs reminders, follow-ups, weekly reports, and safety checks.
- Keeps trading education boundaries clear: no personalized buy/sell signals.

## Folder Map

```text
hermes-agent/
  README.md
  docs/
    gbrain-hermes-learning-brain.md
  learning-brain/
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
  skills/
  gateway/
  cron/
  ops/
  integrations/
```

## Key Docs

- `docs/gbrain-hermes-learning-brain.md` - architecture and MVP plan for video courses -> GBrain -> Hermes coach.
- `learning-brain/README.md` - source workspace for course knowledge, learner state, citations, and reports.

## Operating Model

```text
LearnHouse course videos
-> transcripts + lesson notes + concepts
-> GBrain learning brain
-> Hermes learner coach
-> learner sessions, progress, reminders, reports
```

## Next Build Targets

1. Create `skills/azzam-learning-coach/SKILL.md`.
2. Add transcript and lesson templates under `learning-brain/`.
3. Ingest the first Market Structure videos.
4. Test Hermes answers against real learner questions.
5. Add Telegram gateway notes under `gateway/`.
6. Add daily/weekly dream-cycle jobs under `cron/`.
