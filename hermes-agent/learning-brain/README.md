# Alpha Elite Learning Brain

> Workspace for mapping LearnHouse course content into a GBrain-backed knowledge system for Hermes learner care.

## Purpose

This folder will hold the source-of-truth markdown used to build the learner support brain:

- Course maps
- Timestamped video transcripts
- Lesson notes
- Concept cards
- Exercises and quizzes
- Rubrics/checklists
- Learner profiles and sessions
- Mistake maps
- Daily/weekly reports

The implementation decision doc lives at:

```text
hermes-agent/docs/gbrain-hermes-learning-brain.md
```

## Recommended Structure

```text
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
```

## First MVP Scope

Start with Market Structure only:

1. Export or transcribe 5-10 core videos.
2. Create timestamped transcript files.
3. Distill each video into lesson notes.
4. Extract concept cards and checklists.
5. Build one chart-review rubric.
6. Test Hermes against real learner questions.

## Data Boundary

Raw videos should stay outside the brain repo unless a specific audit need appears. The brain should store:

- Video path or URL
- Timecode citations
- Transcript text
- Distilled knowledge
- Learner progress and feedback

## Operating Rule

Hermes is the coach. GBrain is the long-term memory and knowledge graph. LearnHouse remains the course delivery system.
