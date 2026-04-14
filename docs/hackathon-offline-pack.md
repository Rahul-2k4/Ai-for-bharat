# Hackathon Offline Pack

This file is the "single place" to read hackathon context without opening the website every time.

Last verified: 2026-04-15 (Asia/Kolkata)

## 1) Event identity

- Name: AI for Bharat
- Platform: HackerEarth
- URL: https://www.hackerearth.com/challenges/hackathon/ai-for-bharat-2/
- Organizer shown: PanIIT / PAN IIT Bangalore Summit context
- Venue shown: Taj Yeshwantpur, Bengaluru

## 2) Participation and core rules

- Team size: min 2, max 5.
- Team participation format (not solo-only).
- Build must align with one of the event themes.
- Last submission is treated as final submission.
- Work is expected to be original (copied ideas can be disqualified).
- IP rights statement: code IP belongs to the team.

Source: `tasks/research/raw/hackerearth-ai-for-bharat-2-rules.md`

## 3) Submission model and FAQ clarifications

- Build on local environment; submit source + run instructions in zip/tar.
- Full implementation is not mandatory; a functional prototype is acceptable.
- Any language/stack/libraries can be used.
- Demo video/presentation is optional but useful.
- FAQ mentions code should be public/open for judging.

Source: `tasks/research/raw/hackerearth-ai-for-bharat-2-faq.md`

## 4) Timeline snapshot (text from page payload + official embedded timeline graphic)

### UTC timestamps from event payload

- Event start: 2026-04-10 16:30 UTC
- Event end: 2026-05-04 18:29 UTC

### Phase timeline from official timeline image

- Phase 1
  - Registrations & idea submission go live: 10 April
  - Idea submission end date: 25 April
  - Idea phase shortlist announcement: 28 April
- Phase 2
  - Prototype phase go live: 28 April
  - Prototype phase end date: 04 May
  - Top team announcement: 08 May 2026
- Phase 3
  - Onsite hackathon: 15 May, 6 PM onwards
  - Grand finale: 16 May

Source for extracted timeline text: `tasks/research/raw/images/image_urls.txt` (captured from official embedded timeline image URL)

## 5) Positioning and judging direction (extractable text)

- Real problem statements from government and industry.
- Practical deployment and measurable impact emphasized.
- Execution-first framing.
- Stated evaluation direction in summary text: problem understanding, solution quality, feasibility, impact.

Source: `tasks/research/raw/hackerearth-ai-for-bharat-2-overview.html`

## 6) Coverage status (what is fully captured vs still missing)

### Captured in repo

- Rules
- FAQ
- Team size and venue
- Time windows and phase milestones
- Submission expectations and prototype allowance
- Public summary language for judging direction
- Full custom-tab text for:
  - Evaluation Criteria
  - Submission Guideline
  - Theme 1
  - Theme 2
  - Theme 3

### Still potentially dynamic

- Registered participant count (live value on event page can change).
- Any organizer-side timeline/rule edits after this verification date.
- Detailed prize breakdown changes, if organizers update copy after capture.

## 7) Raw source inventory

- `tasks/research/raw/hackerearth-ai-for-bharat-2-rules.md`
- `tasks/research/raw/hackerearth-ai-for-bharat-2-faq.md`
- `tasks/research/raw/hackerearth-ai-for-bharat-2-overview.html`
- `tasks/research/raw/tabs/*.html`
- `tasks/research/raw/custom-tabs/*.html`
- `tasks/research/raw/images/image_urls.txt`
- `docs/hackathon-evaluation.md`
- `docs/hackathon-submission-guideline.md`
- `docs/hackathon-themes.md`

## 8) Recommendation for zero-website workflow

Use this flow during development:

1. Read this file first.
2. Use `docs/submission-checklist.md` as build/readiness gate.
3. Revisit website only for freshness checks (new rule/timeline/content updates).
