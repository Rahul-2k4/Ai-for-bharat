# AI for Bharat 2 Workspace

Submission-first repository for the HackerEarth challenge: [AI for Bharat](https://www.hackerearth.com/challenges/hackathon/ai-for-bharat-2/).

## What this repo is for

- Build one strong, demoable submission with your team.
- Keep docs, code, and submission assets aligned.
- Make collaboration predictable via branch, PR, and scope rules.

## Repository lanes

- `docs/` - source-of-truth for submission narrative and demo materials.
- `projects/main-submission/` - single active implementation candidate.
- `projects/experiments/` - isolated spikes and throwaway exploration.
- `assets/` - screenshots, diagrams, demo media used in submission docs.
- `tools/` and `tests/tools/` - small repo guardrails (docs scope validator).

## Quick start

```bash
# 1) Create and activate a venv
python3 -m venv .venv
. .venv/bin/activate

# 2) Install test dependency
pip install pytest

# 3) Run docs-scope checks
python -m pytest tests/tools/test_validate_docs_scope.py -v
python tools/validate_docs_scope.py docs/index.md projects/main-submission/README.md
```

## Team workflow (short)

1. Create a short-lived branch from `main`.
2. Keep PRs small and scoped.
3. Update docs in the same PR when behavior/architecture changes.
4. Merge only when checks and review are complete.

See [CONTRIBUTING.md](./CONTRIBUTING.md) and [docs/team-workflow.md](./docs/team-workflow.md).
