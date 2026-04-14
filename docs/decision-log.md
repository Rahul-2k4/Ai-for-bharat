# Decision Log

## 2026-04-15 - Baseline Repository Structure

### Decision

Adopt an umbrella structure with strict lanes:

- `docs/`
- `projects/main-submission/`
- `projects/experiments/`
- `assets/`

### Why

A lane-based layout prevents chaos during multi-person collaboration and keeps submission assets discoverable.

### Impact

- Faster onboarding for friends.
- Lower merge conflict risk across docs/code/assets.
- Clear separation between stable candidate and experiments.

## 2026-04-15 - Branch-Based Team Workflow

### Decision

Use short-lived feature/docs/fix branches and PR-first collaboration on a shared repo.

### Why

This aligns with GitHub flow and keeps review quality high under hackathon time pressure.

### Impact

- Cleaner history.
- Better reviewability.
- Safer integration into `main`.
