# AI for Bharat - Execution Plan

## Plan

- [x] Collect and verify hackathon context using `defuddle` + multi-source research.
- [x] Extract reusable repo structure patterns from `/Users/rahul/Desktop/Metadata/MetadataHack`.
- [x] Create baseline collaboration scaffold in this repo (`docs/`, `projects/`, `assets/`, `.github/`, control docs).
- [x] Add guardrails for scope and contribution workflow (`AGENTS.md`, `CONTRIBUTING.md`, PR template, issue templates).
- [x] Populate submission-focused docs (`docs/index.md`, brief, architecture, demo script, checklist, decision log).
- [x] Add lightweight docs-scope validator and tests for markdown lane enforcement.
- [x] Write onboarding README and working agreements for teammates.
- [x] Run verification checks and record outcomes.

## Review

### What was implemented

- Initialized a collaboration-first hackathon repository scaffold modeled on `MetadataHack`.
- Added submission docs lanes, main/experiment code lanes, and assets lane.
- Added GitHub collaboration artifacts (`PR template`, issue templates, contribution guide).
- Added docs-scope validator with unit tests.
- Added challenge context brief using defuddle extracts from HackerEarth pages.

### Verification evidence

- `python -m pytest tests/tools/test_validate_docs_scope.py -v` -> 6 passed.
- `python tools/validate_docs_scope.py README.md docs/index.md projects/main-submission/README.md` -> success.
- `python tools/validate_docs_scope.py src/README.md` -> expected failure (confirms guardrail catches out-of-scope markdown).

### pass@k self-check

- pass@1: no (one validator normalization bug for `.github/...` path).
- pass@2: yes (fixed `_normalize` and reran checks successfully).
