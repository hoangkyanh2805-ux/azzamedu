# Direct Udemy -> Existing LearnHouse Course SOP

Use this SOP when the goal is to copy a Udemy course into an existing course on `https://learn.azzamedu.com` as-is.

This is a direct web import workflow. It does not use local LearnHouse as a staging database, does not create a new course unless the user asks for one, and does not rewrite Udemy content.

## Roles / agent packaging

| Layer | Name | Responsibility |
|---|---|---|
| Skill | `learnhouse-production-sync` | Owns LearnHouse production API, course sync, QA, and runbooks. |
| Workflow | Direct Udemy -> Existing Course Import | Takes a source Udemy course and fills a target LearnHouse course. |
| Operator / agent | Course Import Operator | Runs the checklist, confirms target UUID, creates skeleton, updates metadata, attaches videos/resources, QA. |
| Sub-role | Source Mapper | Captures Udemy title, subtitle, about/description, what-you-will-learn, sections, lessons, video/resource map. |
| Sub-role | LearnHouse Course Operator | Uses API/dashboard to update only the intended target course. |
| Sub-role | Video/Resource Import Operator | Attaches logged-in Udemy videos and downloadable files to matching LearnHouse lessons. |
| Sub-role | QA Reviewer | Checks counts, order, metadata, access, preview, and learner view. |

## Inputs required

- Source Udemy course URL.
- Target LearnHouse course URL.
- Target LearnHouse API UUID. URL UUID normally needs the `course_` prefix for API calls.
- Admin access to `https://learn.azzamedu.com`.
- `LEARNHOUSE_ADMIN_PASSWORD` in the shell environment, not committed to git.
- Backup/export first if the target course already has valuable content.
- Logged-in Udemy access for videos/resources. Public Udemy page is only enough for metadata/curriculum first-pass.

## Hard rules

- Do not run `seed-udemy-clone.py` for this direct mode. It is for the old Advanced SMC clone and can wipe/recreate a course.
- Do not run `sync-local-to-prod.py` unless the source of truth is intentionally local LearnHouse.
- Do not create a new course when the user gives a target course URL.
- Do not rewrite, translate, summarize, or customize Udemy lesson text unless requested.
- Do not delete chapters/activities on production during import.
- Keep the existing publish/public state unless the user asks to change it.

## Standard workflow

1. Confirm source and target.
   - Source example: `https://www.udemy.com/course/advanced-forex-trading-master-multiple-timeframe-to-trade/`
   - Target example: `https://learn.azzamedu.com/course/f0b9e0d8-240b-47b5-8c39-1a713dccdc0a`
   - API UUID example: `course_f0b9e0d8-240b-47b5-8c39-1a713dccdc0a`

2. Capture source structure.
   - Title, subtitle, public description/about.
   - What-you-will-learn bullets.
   - Section names and lesson titles in Udemy order.
   - Video duration/resource list from logged-in Udemy if available.

3. Confirm target course exists by API.
   - List courses and match `course_uuid` exactly.
   - Abort if the UUID does not match the intended course.

4. Create skeleton only.
   - Add missing chapters and missing lessons.
   - Preserve existing matching chapters/lessons.
   - No body rewrite in this step.

5. Update course metadata as-is.
   - `name` only if needed.
   - `description` from Udemy subtitle.
   - `about` from Udemy description/about.
   - `learnings` from Udemy what-you-will-learn bullets.

6. Attach videos/resources.
   - Use logged-in Udemy source or user-provided exports.
   - Match by section index + lesson title.
   - Attach to the existing LearnHouse lesson, not a new lesson.

7. QA.
   - Section count matches Udemy.
   - Lesson count matches Udemy.
   - Order matches Udemy.
   - Course metadata appears on public/learner page.
   - Videos/resources open from learner account.
   - No duplicate course was created.
   - No unrelated course was edited.

## Script: `import-mtf-skeleton.py`

This script is a case-specific skeleton importer for the MTF Udemy course. It is safe to rerun because it creates only missing chapters/lessons and skips existing lesson titles.

Run pattern:

```powershell
cd web\learnhouse\scripts
$env:LEARNHOUSE_API='https://learn.azzamedu.com/api/v1'
$env:LEARNHOUSE_ADMIN_EMAIL='admin@hoa-homes.com'
$env:LEARNHOUSE_ADMIN_PASSWORD='<set locally, never commit>'
$env:TARGET_COURSE_UUID='course_f0b9e0d8-240b-47b5-8c39-1a713dccdc0a'
python .\import-mtf-skeleton.py
```

Expected result for the MTF case:

```text
9 sections
26 lessons
0 duplicate lessons on rerun
```

For the next Udemy course, copy this script or create a new `import-<course>-skeleton.py`, then replace only:

- `TARGET_COURSE_UUID`
- `CURRICULUM`
- expected section/lesson counts

## MTF import case log

- Source: `https://www.udemy.com/course/advanced-forex-trading-master-multiple-timeframe-to-trade/`
- Target: `https://learn.azzamedu.com/course/f0b9e0d8-240b-47b5-8c39-1a713dccdc0a`
- API UUID: `course_f0b9e0d8-240b-47b5-8c39-1a713dccdc0a`
- Imported skeleton: 9 sections, 26 lessons.
- Metadata updated: title, subtitle/description, about, and learning bullets.
- Remaining manual/pass-2 work: attach logged-in Udemy videos and downloadable resources to the matching lessons.
