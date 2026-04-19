# Theme 2 Interop Gateway Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a working Theme 2 prototype that demonstrates auditable, two-way SWS <-> department synchronization with UBID joins, idempotency, conflict handling, and local-AI advisory.

**Architecture:** A FastAPI-based orchestration gateway sits between SWS and three department adapters (Pollution, Fire, Labour). The gateway performs change discovery, canonical normalization, idempotency checks, conflict resolution, and audited propagation. A lightweight dashboard exposes review queue and read-only evidence for judges.

**Tech Stack:** Python 3.11, FastAPI, SQLModel/SQLAlchemy, PostgreSQL, Redis, pytest, Node 20, Next.js dashboard, local Ollama client.

---

## Planned File Structure

### Backend

- Create: `projects/main-submission/src/backend/pyproject.toml`
- Create: `projects/main-submission/src/backend/app/main.py`
- Create: `projects/main-submission/src/backend/app/core/config.py`
- Create: `projects/main-submission/src/backend/app/core/logging.py`
- Create: `projects/main-submission/src/backend/app/db/session.py`
- Create: `projects/main-submission/src/backend/app/db/models.py`
- Create: `projects/main-submission/src/backend/app/schemas/canonical.py`
- Create: `projects/main-submission/src/backend/app/schemas/events.py`
- Create: `projects/main-submission/src/backend/app/connectors/base.py`
- Create: `projects/main-submission/src/backend/app/connectors/sws.py`
- Create: `projects/main-submission/src/backend/app/connectors/pollution.py`
- Create: `projects/main-submission/src/backend/app/connectors/fire.py`
- Create: `projects/main-submission/src/backend/app/connectors/labour.py`
- Create: `projects/main-submission/src/backend/app/services/change_discovery.py`
- Create: `projects/main-submission/src/backend/app/services/idempotency.py`
- Create: `projects/main-submission/src/backend/app/services/conflict_policy.py`
- Create: `projects/main-submission/src/backend/app/services/ai_advisory.py`
- Create: `projects/main-submission/src/backend/app/services/orchestrator.py`
- Create: `projects/main-submission/src/backend/app/services/audit_ledger.py`
- Create: `projects/main-submission/src/backend/app/api/routes/ingest.py`
- Create: `projects/main-submission/src/backend/app/api/routes/review.py`
- Create: `projects/main-submission/src/backend/app/api/routes/evidence.py`
- Create: `projects/main-submission/src/backend/app/api/routes/replay.py`
- Create: `projects/main-submission/src/backend/app/api/routes/health.py`
- Create: `projects/main-submission/src/backend/app/workers/poller.py`

### Dashboard

- Create: `projects/main-submission/src/dashboard/package.json`
- Create: `projects/main-submission/src/dashboard/src/app/page.tsx`
- Create: `projects/main-submission/src/dashboard/src/app/review/page.tsx`
- Create: `projects/main-submission/src/dashboard/src/app/evidence/page.tsx`
- Create: `projects/main-submission/src/dashboard/src/lib/api.ts`

### Tests

- Create: `projects/main-submission/tests/unit/backend/test_idempotency.py`
- Create: `projects/main-submission/tests/unit/backend/test_conflict_policy.py`
- Create: `projects/main-submission/tests/unit/backend/test_change_discovery.py`
- Create: `projects/main-submission/tests/contract/test_sws_adapter_contract.py`
- Create: `projects/main-submission/tests/contract/test_pollution_adapter_contract.py`
- Create: `projects/main-submission/tests/contract/test_fire_adapter_contract.py`
- Create: `projects/main-submission/tests/contract/test_labour_adapter_contract.py`
- Create: `projects/main-submission/tests/integration/test_two_way_sync.py`
- Create: `projects/main-submission/tests/integration/test_outage_recovery.py`
- Create: `projects/main-submission/tests/smoke/test_judge_demo_flow.py`

### Docs

- Modify: `docs/demo-script.md`
- Modify: `docs/architecture.md`
- Modify: `docs/submission-checklist.md`
- Create: `projects/main-submission/contracts/source-endpoint-matrix.md`
- Create: `projects/main-submission/README.md` (replace placeholder with runnable instructions)

---

### Task 1: Bootstrap Backend Service

**Files:**
- Create: `projects/main-submission/src/backend/pyproject.toml`
- Create: `projects/main-submission/src/backend/app/main.py`
- Create: `projects/main-submission/src/backend/app/api/routes/health.py`
- Test: `projects/main-submission/tests/unit/backend/test_health.py`

- [ ] **Step 1: Write the failing health test**

```python
from fastapi.testclient import TestClient
from app.main import app


def test_health_ready():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd projects/main-submission/src/backend && pytest ../../tests/unit/backend/test_health.py -v`
Expected: FAIL (`ModuleNotFoundError` or missing route)

- [ ] **Step 3: Implement minimal FastAPI app + health route**

```python
# app/main.py
from fastapi import FastAPI
from app.api.routes.health import router as health_router

app = FastAPI(title="Theme2 Interop Gateway")
app.include_router(health_router)
```

- [ ] **Step 4: Re-run test and confirm pass**

Run: `cd projects/main-submission/src/backend && pytest ../../tests/unit/backend/test_health.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add projects/main-submission/src/backend projects/main-submission/tests/unit/backend/test_health.py
git commit -m "feat: bootstrap FastAPI gateway with health endpoint"
```

### Task 2: Canonical Event and Audit Models

**Files:**
- Create: `projects/main-submission/src/backend/app/schemas/canonical.py`
- Create: `projects/main-submission/src/backend/app/db/models.py`
- Test: `projects/main-submission/tests/unit/backend/test_canonical_schema.py`

- [ ] **Step 1: Write failing schema test for per-department records**
- [ ] **Step 2: Run failing test**
- [ ] **Step 3: Implement canonical schema with `department_records[]` fields**
- [ ] **Step 4: Re-run unit test**
- [ ] **Step 5: Commit**

### Task 3: Change Discovery Layer (Webhook/Polling/Fixture Replay)

**Files:**
- Create: `projects/main-submission/src/backend/app/services/change_discovery.py`
- Create: `projects/main-submission/src/backend/app/workers/poller.py`
- Test: `projects/main-submission/tests/unit/backend/test_change_discovery.py`

- [ ] **Step 1: Write failing tests for discovery modes**

```python
def test_webhook_mode_returns_event_batch():
    ...

def test_poll_mode_uses_last_seen_cursor():
    ...

def test_fixture_replay_mode_rehydrates_canonical_events():
    ...
```

- [ ] **Step 2: Run tests and verify fail**
- [ ] **Step 3: Implement discovery service contract (`webhook`, `polling`, `fixture_replay`) with durable cursor storage**
- [ ] **Step 4: Re-run tests and verify pass**
- [ ] **Step 5: Commit**

### Task 4: Idempotency and Replay Safety

**Files:**
- Create: `projects/main-submission/src/backend/app/services/idempotency.py`
- Modify: `projects/main-submission/src/backend/app/services/orchestrator.py`
- Test: `projects/main-submission/tests/unit/backend/test_idempotency.py`

- [ ] **Step 1: Write failing tests for duplicate suppression**
- [ ] **Step 2: Run tests to confirm failure**
- [ ] **Step 3: Implement key strategy (`source_system + source_event_id + payload_hash`)**
- [ ] **Step 4: Re-run tests and confirm no duplicate side effects**
- [ ] **Step 5: Commit**

### Task 5: Conflict Policy Engine

**Files:**
- Create: `projects/main-submission/src/backend/app/services/conflict_policy.py`
- Test: `projects/main-submission/tests/unit/backend/test_conflict_policy.py`

- [ ] **Step 1: Write failing tests for conflict classes C1-C4 and field-level source-of-truth rules**
- [ ] **Step 2: Run tests to confirm fail**
- [ ] **Step 3: Implement policy engine with field ownership (`department` for regulatory fields, `SWS` for applicant metadata)**
- [ ] **Step 4: Implement transition-legality checks and ordering (`source_version` -> `source_timestamp` with skew budget -> manual`)**
- [ ] **Step 5: Re-run tests and confirm deterministic outputs**
- [ ] **Step 6: Commit**

### Task 6: Local AI Advisory (Conflict-Risk Only)

**Files:**
- Create: `projects/main-submission/src/backend/app/services/ai_advisory.py`
- Test: `projects/main-submission/tests/unit/backend/test_ai_advisory.py`

- [ ] **Step 1: Write failing test with mocked local inference client**
- [ ] **Step 2: Run and verify fail**
- [ ] **Step 3: Implement advisory interface returning `risk_level` + `reason`**
- [ ] **Step 4: Re-run tests and verify pass**
- [ ] **Step 5: Commit**

### Task 7: Two-Way Orchestration and Adapter Contracts

**Files:**
- Create: `projects/main-submission/src/backend/app/connectors/*.py`
- Create: `projects/main-submission/src/backend/app/services/orchestrator.py`
- Create: `projects/main-submission/contracts/source-endpoint-matrix.md`
- Test: `projects/main-submission/tests/contract/test_sws_adapter_contract.py`
- Test: `projects/main-submission/tests/contract/test_pollution_adapter_contract.py`
- Test: `projects/main-submission/tests/contract/test_fire_adapter_contract.py`
- Test: `projects/main-submission/tests/contract/test_labour_adapter_contract.py`
- Test: `projects/main-submission/tests/integration/test_two_way_sync.py`

- [ ] **Step 1: Write source-endpoint matrix (`sandbox` vs `contract-tested synthetic mock`) for all 4 source systems**
- [ ] **Step 2: Write failing adapter contract tests (one per adapter)**
- [ ] **Step 3: Run contract tests and verify fail**
- [ ] **Step 4: Implement adapters to satisfy contracts and canonical transforms**
- [ ] **Step 5: Write failing integration test for SWS -> 3 depts and dept -> SWS**
- [ ] **Step 6: Implement orchestrator flow and rerun integration test**
- [ ] **Step 7: Run contract + integration tests and verify pass**
- [ ] **Step 8: Commit**

### Task 8: Retry, DLQ, and Outage Recovery

**Files:**
- Modify: `projects/main-submission/src/backend/app/services/orchestrator.py`
- Create: `projects/main-submission/src/backend/app/api/routes/replay.py`
- Create: `projects/main-submission/tests/integration/test_outage_recovery.py`
- Create: `projects/main-submission/tests/unit/backend/test_replay_endpoint.py`

- [ ] **Step 1: Write failing integration test for one-department outage + recovery**
- [ ] **Step 2: Run and verify fail**
- [ ] **Step 3: Add retry with backoff + DLQ + replay endpoint**
- [ ] **Step 4: Re-run integration tests and verify eventual convergence**
- [ ] **Step 5: Add unit tests for replay endpoint behavior and rerun**
- [ ] **Step 6: Commit**

### Task 9: Audit Ledger and Read-Only Evidence APIs

**Files:**
- Create: `projects/main-submission/src/backend/app/services/audit_ledger.py`
- Create: `projects/main-submission/src/backend/app/api/routes/evidence.py`
- Create: `projects/main-submission/src/backend/app/api/routes/review.py`
- Test: `projects/main-submission/tests/unit/backend/test_audit_ledger.py`
- Test: `projects/main-submission/tests/unit/backend/test_evidence_api.py`
- Test: `projects/main-submission/tests/unit/backend/test_review_resolution_api.py`

- [ ] **Step 1: Write failing tests for required audit/evidence fields (`correlation_id`, `decision_reason`, `payload_diff`, `rule_hits`, `ai_advisory`, `final_action`, `review_status`)**
- [ ] **Step 2: Run tests and verify fail**
- [ ] **Step 3: Implement append-only ledger writes including reversibility metadata (`compensating_action_template` or `non_reversible`)**
- [ ] **Step 4: Implement review-resolution API for `approve`, `reject`, and `corrective_sync/manual_action` paths**
- [ ] **Step 5: Implement evidence query endpoints returning full judge-facing evidence payload**
- [ ] **Step 6: Re-run tests and verify pass**
- [ ] **Step 7: Commit**

### Task 10: Judge Demo Dashboard (Minimal)

**Files:**
- Create: `projects/main-submission/src/dashboard/*`
- Test: `projects/main-submission/tests/smoke/test_judge_demo_flow.py`

- [ ] **Step 1: Write failing smoke test for review queue resolution and evidence pages**
- [ ] **Step 2: Run smoke test and verify fail**
- [ ] **Step 3: Implement dashboard with minimal review actions (`approve`, `reject`, `corrective_sync`) and read-only evidence page**
- [ ] **Step 4: Re-run smoke test and verify pass**
- [ ] **Step 5: Commit**

### Task 11: Submission Artifacts and Demo Script

**Files:**
- Modify: `docs/demo-script.md`
- Modify: `docs/architecture.md`
- Modify: `docs/submission-checklist.md`
- Modify: `projects/main-submission/README.md`

- [ ] **Step 1: Add score-evidence checklist entries that map each scoring bucket to concrete artifacts**
- [ ] **Step 2: Update docs with exact run commands, demo flow, source-endpoint matrix, and evidence payload mapping**
- [ ] **Step 2: Update docs with exact run commands, demo flow, source-endpoint matrix, evidence payload mapping, and synthetic-data declaration**
- [ ] **Step 3: Run docs scope validator**

Run: `python3 tools/validate_docs_scope.py docs/demo-script.md docs/architecture.md docs/submission-checklist.md projects/main-submission/README.md`
Expected: PASS

- [ ] **Step 4: Re-run validator and confirm pass**
- [ ] **Step 5: Commit**

### Task 12: Final Verification Gate

**Files:**
- Modify: `tasks/todo.md` (review outcomes)

- [ ] **Step 1: Run unit tests**

Run: `cd projects/main-submission/src/backend && pytest ../../tests/unit -v`
Expected: PASS

- [ ] **Step 2: Run integration tests**

Run: `cd projects/main-submission/src/backend && pytest ../../tests/integration -v`
Expected: PASS

- [ ] **Step 3: Run smoke test**

Run: `cd projects/main-submission/src/backend && pytest ../../tests/smoke/test_judge_demo_flow.py -v`
Expected: PASS

- [ ] **Step 4: Verify dashboard surface**

Run:
- `cd projects/main-submission/src/dashboard && npm install`
- `cd projects/main-submission/src/dashboard && npm run build`

Expected: BUILD SUCCESS

- [ ] **Step 5: Run acceptance-proof checks from spec matrix**

Run:
- `cd projects/main-submission/src/backend && pytest ../../tests/integration/test_two_way_sync.py -k ubid -v`
- `cd projects/main-submission/src/backend && pytest ../../tests/unit/backend/test_audit_ledger.py -k correlation -v`
- `cd projects/main-submission/src/backend && pytest ../../tests/integration/test_outage_recovery.py -v`

Record:
- UBID join proof (all target systems linked by UBID)
- 100% correlation_id propagation on demo events
- synthetic/sandbox-only dataset evidence note
- queue depth and p95 latency snapshot

Expected: PASS + artifacts captured

- [ ] **Step 6: Run docs lane checks + repo guardrails**

Run:
- `python3 tools/validate_docs_scope.py $(git diff --name-only)`
- `. .venv/bin/activate && python -m pytest tests/tools/test_validate_docs_scope.py -v`

Expected: PASS

- [ ] **Step 7: Commit verification evidence update**

```bash
git add tasks/todo.md docs projects/main-submission
git commit -m "chore: record verification evidence for theme 2 prototype"
```

---

## Scope Guardrails

- Keep AI advisory local and non-authoritative.
- Keep evidence view read-only for MVP, while allowing minimal review-resolution actions.
- Keep data synthetic/sandbox-only.
- Do not add non-essential infrastructure beyond MVP acceptance criteria.

## Suggested Commit Cadence

- 1 commit per task (12 total target).
- Keep each commit independently testable.

## Dependencies To Install (when execution starts)

- Backend: `fastapi`, `uvicorn`, `sqlalchemy`, `sqlmodel`, `redis`, `httpx`, `pytest`
- Dashboard: `next`, `react`, `typescript`
- Local AI runtime: `ollama` (already available locally or install before Task 6)
