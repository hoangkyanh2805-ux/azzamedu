# Mindset Course - Direct Udemy -> Existing LearnHouse Import

Use `learnhouse-production-sync` in **Direct Web Import into Existing Course** mode.

## Source and target

| Field | Value |
|---|---|
| Source Udemy | `https://www.udemy.com/course/the-mindset-must-know-before-learning-trading-and-investing/` |
| Target LearnHouse dashboard | `https://learn.azzamedu.com/dash/courses/course/b2acf623-7983-4fe4-bb7f-5b2447faa998/general` |
| Target learner URL | `https://learn.azzamedu.com/course/b2acf623-7983-4fe4-bb7f-5b2447faa998` |
| Target API UUID | `course_b2acf623-7983-4fe4-bb7f-5b2447faa998` |
| Workflow | Direct Udemy -> Existing Course Import |
| Operator / agent | Course Import Operator |

## Rules

- No rewrite.
- No customization.
- No compliance edits.
- No local staging.
- No new course creation.
- Do not run `seed-udemy-clone.py`.
- Do not run `sync-local-to-prod.py`.
- Preserve section order.
- Preserve lecture titles.
- Preserve original articles/resources as much as possible.
- Add videos/resources only to matching lessons.
- Target this course only: `course_b2acf623-7983-4fe4-bb7f-5b2447faa998`.

## Public manifest first pass

Public Udemy page confirms:

| Item | Capture |
|---|---|
| Title | The mindset must know before learning trading and investing |
| Short description | Level 0 preparation for learning trading strategies |
| Public duration | 1h59m on-demand video |
| Rating snapshot | 4.7 |
| Public learning bullets | 6 bullets captured from the public page |
| Requirements | Motivation/commitment note captured from the public page |
| Audience | New traders and experienced struggling traders |

Production metadata status:

| Field | Status |
|---|---|
| `name` | Synced to target course |
| `description` | Synced to target course |
| `about` | Synced to target course |
| `learnings` | Synced to target course |
| `published` | Preserved as existing value (`False` at sync time) |

## 1. Exact curriculum capture table

This table must be completed from **logged-in Udemy curriculum** or an exported course package before any chapter/lesson skeleton import.

| Section # | Udemy section title | Lecture # | Udemy lecture title | Type | Duration | Resources/articles | Verified source |
|---:|---|---:|---|---|---|---|---|
| TBD | TBD | TBD | TBD | video/article/quiz | TBD | TBD | logged-in Udemy/export |

Gate: do not create `import-mindset-skeleton.py` with guessed titles. Use only verified section/lecture titles.

## 2. LearnHouse section mapping

| Udemy section # | Udemy section title | LearnHouse chapter title | Action |
|---:|---|---|---|
| TBD | TBD | exact same as Udemy | create if missing; skip if exists |

Mapping rule: LearnHouse chapter title must match Udemy section title as-is.

## 3. Lesson/activity mapping

| Udemy section # | Udemy lecture # | Udemy lecture title | LearnHouse activity title | Action |
|---:|---:|---|---|---|
| TBD | TBD | TBD | exact same as Udemy | create if missing; skip if exists |

Mapping rule: activity title must match Udemy lecture title as-is. Match video/resource imports by section index + lecture title.

## 4. Per-lecture video/resource import checklist

For every lecture:

- [ ] Confirm Udemy section index.
- [ ] Confirm Udemy lecture title exactly.
- [ ] Confirm matching LearnHouse chapter exists.
- [ ] Confirm matching LearnHouse activity exists.
- [ ] Add video only to the matching LearnHouse activity.
- [ ] Add article/resource files only to the matching LearnHouse activity.
- [ ] Do not create duplicate activity for video/resource.
- [ ] Open learner preview and verify video/resource loads.

## 5. Per-section QA checklist

For every section:

- [ ] Section order matches Udemy.
- [ ] Chapter title matches Udemy section title.
- [ ] Lecture count matches Udemy section.
- [ ] Lecture order matches Udemy.
- [ ] Lecture titles match Udemy exactly.
- [ ] Videos/resources are attached only to matching lessons.
- [ ] No extra lessons created.
- [ ] No missing lessons.

## 6. Final QA checklist

- [ ] Target course URL is still `https://learn.azzamedu.com/course/b2acf623-7983-4fe4-bb7f-5b2447faa998`.
- [ ] API UUID is still `course_b2acf623-7983-4fe4-bb7f-5b2447faa998`.
- [ ] No new duplicate course was created.
- [ ] No other LearnHouse course was modified.
- [ ] Course metadata is visible on learner page.
- [ ] Section count matches logged-in Udemy curriculum.
- [ ] Lecture count matches logged-in Udemy curriculum.
- [ ] Every video/resource opens from learner account.
- [ ] Import script rerun is idempotent: 0 new chapters, 0 new lessons.

## Execution pattern after curriculum verification

Create a course-specific script from the MTF importer:

```text
web/learnhouse/scripts/import-mindset-skeleton.py
```

Replace only:

- `TARGET_COURSE_UUID` -> `course_b2acf623-7983-4fe4-bb7f-5b2447faa998`
- `CURRICULUM` -> verified Mindset section/lecture structure
- expected section/lecture count

Run pattern:

```powershell
cd web\learnhouse\scripts
$env:LEARNHOUSE_API='https://learn.azzamedu.com/api/v1'
$env:LEARNHOUSE_ADMIN_EMAIL='admin@hoa-homes.com'
$env:LEARNHOUSE_ADMIN_PASSWORD='<set locally, never commit>'
$env:TARGET_COURSE_UUID='course_b2acf623-7983-4fe4-bb7f-5b2447faa998'
python .\import-mindset-skeleton.py
python .\import-mindset-skeleton.py
```

Expected second run: created chapters `0`, created lessons `0`, skipped lessons equals total verified lecture count.

## Current production state checked

- Target course confirmed by API: `course_b2acf623-7983-4fe4-bb7f-5b2447faa998`.
- Current target course id: `3`.
- Current chapter count at last check: `0`.
- Current lesson count at last check: `0`.
- Metadata has been synced from the public Udemy first pass.
