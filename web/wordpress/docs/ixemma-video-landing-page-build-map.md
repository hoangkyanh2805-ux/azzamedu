# ixEmma Code WordPress Video Landing Page Build Map

> Source reference copied from `C:\Users\Admin\Downloads\code-wordpress-main` into `web/wordpress/reference/ixemma-code-wordpress/`.

## Source Inputs

| Source | Location |
|---|---|
| GitHub reference repo | `web/wordpress/reference/ixemma-code-wordpress/` |
| Video guide | `https://www.youtube.com/watch?v=rhoAtqr-aDE` |
| Current Alpha Elite WordPress docs | `web/wordpress/` |
| Existing Alpha Elite landing spec | `web/wordpress/landing-page-cro-design.md` |
| Existing Elementor hero/opt-in spec | `web/wordpress/elementor-spec-homepage-hero-optin.md` |

## What The Reference Repo Teaches

The ixEmma repo is not a WordPress backup. It is a rebuild workflow for Elementor pages:

1. Write a public page blueprint.
2. Define style guide and global Elementor settings.
3. Build with Elementor Containers and native widgets.
4. Export Elementor JSON locally.
5. Keep private/generated templates separate from public docs.
6. Maintain section maps so future agents know the page structure.

Useful files:

```text
web/wordpress/reference/ixemma-code-wordpress/AGENTS.md
web/wordpress/reference/ixemma-code-wordpress/docs/STYLE_GUIDE.md
web/wordpress/reference/ixemma-code-wordpress/docs/ELEMENTOR_BUILD_NOTES.md
web/wordpress/reference/ixemma-code-wordpress/docs/REPO_STRUCTURE_AND_OUTPUT_WORKFLOW.md
web/wordpress/reference/ixemma-code-wordpress/elementor-outputs/section-maps/
web/wordpress/reference/ixemma-code-wordpress/codex-skills/
```

## Map To Alpha Elite Landing Page

Use the video + ixEmma workflow as the operating model, but keep Alpha Elite's existing dark-gold trading education positioning.

| ixEmma Pattern | Alpha Elite Equivalent |
|---|---|
| Public blueprint docs | `web/wordpress/landing-page-cro-design.md` |
| Style guide | `web/wordpress/design-system-dark-gold.md` |
| Section maps | `web/wordpress/elementor-implementation-map.md` and future `web/wordpress/section-maps/` |
| Elementor build notes | `web/wordpress/docs/elementor-v2-build-checklist.md` |
| Generated Elementor output | `web/wordpress/import/` or local/private export folder |
| Reference materials | `web/wordpress/reference/ixemma-code-wordpress/` |

## Build Workflow

### Phase 1 - Extract The Video Lessons

Create a video note file after transcript/manual review:

```text
web/wordpress/reference/ixemma-code-wordpress/video-notes/rhoAtqr-aDE-landing-page-build.md
```

Capture:

- Page structure shown in the video.
- Elementor settings used.
- Global colors, fonts, spacing.
- Container hierarchy.
- Reusable sections/components.
- Export/import process.
- Any debugging or responsive fixes.

### Phase 2 - Convert Video Into Alpha Elite Section Map

Target output:

```text
web/wordpress/section-maps/homepage-landing-section-map.md
```

Recommended Alpha Elite sections:

1. Header boundary: global header only, not part of body template.
2. Hero + opt-in: main offer, lead magnet form, trust microcopy.
3. Pain/problem section: inconsistent trading, no operating system.
4. Mechanism section: Private financial operating system, not signal group.
5. Course/offer bridge: Apprentice, VIP, Quant/Inner Circle.
6. Proof/credibility: screenshots, curriculum, process proof.
7. Lead magnet preview: Alpha Elite Gameplan.
8. FAQ/compliance: education only, no profit guarantees.
9. Final CTA: opt-in or checkout path.
10. Footer boundary: global footer only, not part of body template.

### Phase 3 - Build In Elementor

Use Elementor Containers and native widgets first:

- Heading widgets for H1/H2/H3.
- Text Editor widgets for paragraph/list copy.
- Button widgets for CTAs.
- Image widgets for real product/course visuals.
- Form/shortcode widget for opt-in if Brevo/Woo/FunnelKit requires it.
- Icon widgets only where they improve scanning.

Avoid:

- Legacy sections/columns.
- Heavy custom JavaScript.
- Embedding private media in public reference folders.
- Exporting production-sensitive JSON into public tracked files.

### Phase 4 - Save Outputs Safely

Private/generated Elementor JSON should go to a local/private output folder first:

```text
web/wordpress/import/
```

If a future public reference output is approved, copy a sanitized version into:

```text
web/wordpress/reference/ixemma-code-wordpress/elementor-outputs/references/exports/
```

Do not commit credentials, database backups, WordPress uploads, private templates, or production-only JSON unless explicitly approved.

## Alpha Elite Design Translation

Do not copy ixEmma's healthcare style literally. Use its workflow only.

Alpha Elite should keep:

- Dark/gold premium trading education identity.
- Compliance-first wording.
- Clear distinction between education, operating system, and signals.
- Real course/product visuals where possible.
- Strong mobile-first hero and opt-in.

Design source:

```text
web/wordpress/design-system-dark-gold.md
web/wordpress/html/homepage.html
web/wordpress/html/homepage-dark-gold.html
```

## Video-Derived Checklist

Use this checklist while watching `rhoAtqr-aDE`:

- [ ] Identify the final landing page sections shown in the video.
- [ ] Note Elementor global site settings.
- [ ] Note which widgets are used per section.
- [ ] Capture any custom CSS snippets.
- [ ] Capture responsive breakpoint adjustments.
- [ ] Capture export/import steps.
- [ ] Convert the video build into Alpha Elite section map.
- [ ] Update `elementor-spec-homepage-hero-optin.md` if the video suggests a better hero/opt-in structure.
- [ ] Update `elementor-implementation-map.md` after building.

## Implementation Decision

The copied ixEmma repo is a reference pattern, not the source of truth for Alpha Elite. Alpha Elite keeps its own:

- Offer positioning.
- Visual system.
- Compliance guardrails.
- Elementor import/export paths.
- Funnel/LeadHouse/Brevo/WooCommerce integration plan.

The reference is useful for discipline: blueprint first, style guide second, section map third, Elementor output last.
