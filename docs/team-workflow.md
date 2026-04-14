# Team Workflow

## Goal

Move fast without breaking demo readiness.

## Daily operating model

1. Pick one scoped issue per person.
2. Create a branch and open a draft PR early.
3. Push small commits every 30-90 minutes.
4. Request review once checks pass.
5. Merge and sync quickly.

## Branch naming

- `feat/<name>/<scope>`
- `fix/<name>/<scope>`
- `docs/<name>/<scope>`

## Ownership guidance

- `docs/` -> docs owner for the day.
- `projects/main-submission/src/` -> feature owners by module.
- `projects/experiments/` -> independent spike owners.
- `assets/` -> demo/storytelling owner.

## Merge policy

- No direct commits to `main` for team work.
- At least one review for non-trivial PRs.
- Keep PRs small and reversible.

## Conflict protocol

1. Prefer resolving conflicts via pair review.
2. If uncertain, keep behavior stable and log the decision in `docs/decision-log.md`.
3. Never discard teammate work without explicit confirmation.
