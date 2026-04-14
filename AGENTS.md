# AI for Bharat 2 Agent Guide

Purpose: keep this repository submission-ready while friends and AI agents work in parallel.

## Scope Rules (Non-Negotiable)

- Keep this repository hackathon-only.
- Allowed markdown locations:
  - `docs/`, `projects/main-submission/`, `projects/experiments/`, `assets/`, `.github/`, `tasks/`
  - root control docs: `README.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`
- Do not add personal journals or unrelated markdown.
- Do not rename top-level lanes without updating `docs/index.md` and `docs/decision-log.md`.

## Repository Contract

- `docs/`: source-of-truth for submission artifacts.
- `projects/main-submission/`: exactly one active candidate.
- `projects/experiments/`: parallel spikes (`exp-01-<name>`, `exp-02-<name>`, ...).
- `assets/`: screenshots, diagrams, and demo media.

## Implementation Practices

- Make small, focused commits with clear messages.
- Prefer improving existing files over adding unnecessary structure.
- If behavior/architecture changes, update docs in the same PR:
  - `docs/architecture.md`
  - `docs/demo-script.md`
  - `docs/submission-checklist.md`
  - `docs/decision-log.md`
- Keep `main` demoable.

## Verification Before Commit

Run these before opening/updating a PR:

```bash
. .venv/bin/activate
python -m pytest tests/tools/test_validate_docs_scope.py -v
python tools/validate_docs_scope.py $(git diff --name-only --cached)
```

## Branch and PR Workflow

- Branch names: `feat/<name>/<scope>`, `fix/<name>/<scope>`, `docs/<name>/<scope>`.
- Use pull requests for team collaboration instead of direct `main` pushes.
- Fill `.github/pull_request_template.md` completely.
- Include run steps + proof (logs/screenshots) for behavior changes.

## Guardrails for AI Agents

- Do not rewrite large docs unless requested.
- Do not delete teammate-authored content without explicit instruction.
- Do not introduce heavy tooling unless needed for the deliverable.
- If requirements are unclear, ask one focused question and then proceed.
