# Contributing

## Branching

- Create a branch from `main`.
- Use descriptive names:
  - `feat/<name>/<scope>`
  - `fix/<name>/<scope>`
  - `docs/<name>/<scope>`

## Pull requests

- Keep PRs reviewable in under ~300 lines when possible.
- Link issues with `Closes #<id>` when applicable.
- Include:
  - what changed,
  - why,
  - how to test,
  - any screenshots/demo notes.

## Required checks

```bash
. .venv/bin/activate
python -m pytest tests/tools/test_validate_docs_scope.py -v
python tools/validate_docs_scope.py $(git diff --name-only --cached)
```

## Collaboration norms

- Prefer branch-based collaboration over forks for core teammates.
- Pull `main` frequently to reduce merge conflicts.
- Never force-push shared branches.
- Keep secrets out of git history.
