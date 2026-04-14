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

## Plan - Offline Hackathon Completeness (2026-04-15)

- [x] Validate availability of custom-tab raw HTML for `evaluation-criteria`, `submission-guideline`, and `theme-1/2/3`.
- [x] Extract full tab content from raw HTML and verify it is parseable offline.
- [x] Publish tab-specific docs in `docs/` (`hackathon-themes.md`, `hackathon-evaluation.md`, `hackathon-submission-guideline.md`).
- [x] Update `docs/hackathon-offline-pack.md` coverage to reflect full tab capture.
- [x] Update `docs/index.md` navigation for new offline docs.
- [x] Run `python3 tools/validate_docs_scope.py` on all changed markdown docs.
- [ ] Commit and push to `main`.

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

## Review - Offline Completeness Pass (2026-04-15)

### What was implemented

- Added offline reference docs for all custom tabs:
  - `docs/hackathon-themes.md`
  - `docs/hackathon-evaluation.md`
  - `docs/hackathon-submission-guideline.md`
- Updated `docs/hackathon-offline-pack.md` to mark custom-tab coverage as captured.
- Updated `docs/index.md` and `docs/hackathon-brief.md` to include links to offline tab docs.
- Added raw source organization notes in `tasks/research/raw/images/README.md` and preserved raw custom-tab HTML in `tasks/research/raw/custom-tabs/`.

### Verification evidence

- `python3 tools/validate_docs_scope.py docs/index.md docs/hackathon-brief.md docs/hackathon-offline-pack.md docs/hackathon-themes.md docs/hackathon-evaluation.md docs/hackathon-submission-guideline.md` -> success.
- Spot audit via `rg` confirms theme/evaluation/submission content and links are present in docs.

### pass@k self-check

- pass@1: yes for this offline completeness pass.
