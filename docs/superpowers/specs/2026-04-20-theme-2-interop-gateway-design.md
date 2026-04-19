# Theme 2 Prototype Design - Interop Gateway (Draft)

Date: 2026-04-20
Track: Theme 2 - Two-Way Interoperability between SWS and Department Systems
Status: Draft for review

## 1) Objective

Build a working prototype that shows reliable, auditable, two-way synchronization between SWS and three department systems for a factory-license journey:

- Pollution NOC (KSPCB)
- Fire Safety NOC
- Labour/Factory Compliance

This prototype is designed to align tightly with the official evaluation dimensions while staying realistic for the Phase 2 window ending May 4, 2026.

## 2) Non-Negotiable Constraints

The design follows the Theme 2 constraints captured in the offline docs:

- Do not modify SWS or department source systems.
- Use UBID as the join key across systems.
- Ensure idempotent and auditable propagation.
- Use only scrambled/synthetic sandbox data in Round 2 flows and evidence.
- Handle schema and API heterogeneity.
- Handle near-simultaneous conflicting updates with explicit policy.
- Use local AI only for the prototype (no hosted LLM calls on raw data).

Reference docs:
- `docs/hackathon-themes.md`
- `docs/hackathon-evaluation.md`
- `docs/hackathon-submission-guideline.md`

## 3) Chosen Approach

Selected architecture: **Orchestrated Interop Gateway with local AI assist layer**.

Why this approach:

- Strong technical depth without overbuilding into a full platform rewrite.
- Clean demo narrative for judges: one gateway, visible policies, visible audit trail.
- Better reliability control than fully decentralized event choreography in a short hackathon timeline.
- Keeps innovation visible through local AI-assisted mapping and conflict-risk scoring.

## 4) System Architecture

### 4.1 Adapters

- `SWS Adapter`
- `Pollution Adapter`
- `Fire Adapter`
- `Labour Adapter`

Responsibilities:
- Transform native payloads to canonical schema and back.
- Isolate per-system API quirks and authentication.
- Normalize errors to gateway-level error codes.

### 4.1.1 Change Discovery

- Each adapter must declare one discovery mode: `webhook`, `polling`, or `fixture_replay`.
- For systems without native events, use scheduled delta polling with persisted cursors.
- Every discovered change must be materialized as a canonical event before idempotency and conflict checks.

### 4.2 Gateway Core

- `Sync Orchestrator`: drives SWS -> Dept and Dept -> SWS flows.
- `Idempotency Manager`: dedupe keys, replay-safe results.
- `Conflict Engine`: deterministic policy evaluation.
- `Retry & Recovery`: retry with backoff, dead-letter queue, replay controls.
- `Policy Engine`: field-level source-of-truth and transition rules.

### 4.3 Governance and Observability

- `Audit Ledger` (append-only event records).
- `Review Queue` (manual resolution for high-risk conflicts).
- `Evidence View` (side-by-side payload diff, rule hits, AI advisory, final action).
- Trace/correlation IDs propagated end to end.

### 4.4 Local AI Assist Layer

Runs locally (for example through Ollama + local model).

Uses:
- conflict-risk scoring (`low`, `medium`, `high`),
- anomaly hints.

Hard guardrail:
- AI is advisory only. It cannot bypass policy gates for high-risk conflicts.

## 5) Canonical Data Model (Minimum)

Core entities:

- `ubid`
- `application_id`
- `service_type` (`factory_license`)
- `department_records[]` where each record includes:
  - `department_type`
  - `status`
  - `source_system`
  - `source_event_id`
  - `source_version`
  - `source_timestamp`
  - `ingested_at`
  - `payload_hash`
- `documents`

Supporting metadata:

- `idempotency_key`
- `correlation_id`
- `event_type`
- `decision_reason`
- `review_required`

## 6) End-to-End Data Flow

1. Change is discovered via webhook, scheduled polling, or fixture replay from SWS or a department system.
2. Adapter normalizes payload into canonical schema.
3. Idempotency gate checks if event was already processed.
4. Conflict pre-check evaluates staleness, transition legality, and concurrent updates.
5. Local AI assigns risk score and advisory explanation.
6. Decision path:
   - low-risk deterministic case: auto-resolve and propagate,
   - high/ambiguous case: send to review queue.
7. Propagate resolved state to target systems.
8. Persist full audit event set, including retries, failures, and final action.

## 7) Conflict Resolution Policy

### 7.1 Priority Rules

- Regulatory-critical fields: department system preferred.
- Applicant/profile metadata: SWS preferred.
- Same authority tier: compare `source_version` first; if absent, compare `source_timestamp` within a defined clock-skew budget; if still tied or missing metadata, route to manual review.
- Irreversible transitions: force human review if contradiction is detected.

### 7.2 Conflict Classes

- `C1 Duplicate`: no-op with replay-safe response.
- `C2 Out-of-order`: reject as stale using version-first ordering, then timestamp ordering.
- `C3 Concurrent divergent`: rule-based winner or manual queue.
- `C4 Cross-field inconsistency`: always manual review.

### 7.3 Reversibility

Each auto-applied mutation stores either a compensating action template or a `non_reversible` flag.
Rollback is available only for reversible demo states under gateway control and is fully audited.
For irreversible or externally committed states, reviewers create corrective sync or manual-action records.

## 8) Score-Evidence Matrix

| Score bucket | Proof artifact | Demo moment | Acceptance metric |
| --- | --- | --- | --- |
| Problem Relevance and Understanding (20%) | Factory-license swimlane and field-ownership map | Opening context segment | UBID join shown across all 3 departments |
| Technical Implementation and Innovation (25%) | Replay/conflict/retry test report with logs | Failure-injection segment | 0 duplicate side effects; stale-event handling explained by policy |
| Real-World Deployability and Gov Feasibility (25%) | Outage recovery trace + audit extract | Recovery segment | System converges after reconnect, with no hidden writes |
| Demo Quality and Presentation (15%) | 5-minute script + deterministic seed dataset | Full walkthrough | Demo completes without manual patching |
| Scalability and Long-Term Impact (15%) | Burst-run metrics snapshot | Closing segment | Queue depth and p95 latency are reported |

Verification minimums:
- 100% of demo events carry `correlation_id`.
- 100% of conflicts carry explicit `decision_reason`.
- All demo evidence is generated from sandbox/synthetic inputs only.

## 9) MVP Scope vs Stretch Scope

### MVP (must ship)

- SWS + 3 department adapters using sandbox endpoints where available, otherwise contract-tested synthetic mocks only
- canonical model + UBID join strategy
- idempotency keys + replay-safe behavior
- retry + DLQ handling
- conflict policy engine + review queue
- local AI advisory for conflict-risk explanation only
- audit ledger + read-only evidence view
- 5-minute demo and repository docs

### Stretch (only if MVP is stable)

- richer analytics dashboard,
- auto-generated policy suggestions from historical cases,
- synthetic-load benchmark report automation.

## 10) Build Milestones (Phase 2 Target)

- Day 1-2: data contracts, adapters skeleton, canonical model, audit schema.
- Day 3-4: sync orchestrator, idempotency, retry, and replay logic.
- Day 5-6: conflict engine + review queue + corrective-action path.
- Day 7: local AI advisory integration and guardrails.
- Day 8: end-to-end tests, demo polish, video run-through, submission prep.

## 11) Risks and Mitigations

- Risk: adapter instability from heterogeneous mocks.
  - Mitigation: fixed adapter contract tests and schema fixtures.
- Risk: conflict logic becomes opaque.
  - Mitigation: decision_reason required for every resolution path.
- Risk: AI introduces non-determinism.
  - Mitigation: AI advisory only; deterministic policy remains authoritative.
- Risk: demo fragility.
  - Mitigation: deterministic seed data and replayable demo script.

## 12) References

- Hackathon evaluation criteria:
  - https://www.hackerearth.com/challenges/hackathon/ai-for-bharat-2/custom-tab/evaluation-criteria/
- Hackathon submission guideline:
  - https://www.hackerearth.com/challenges/hackathon/ai-for-bharat-2/custom-tab/submission-guideline/
- Theme 2 statement:
  - https://www.hackerearth.com/challenges/hackathon/ai-for-bharat-2/custom-tab/theme-2/
- GovStack architecture cross-functional requirements:
  - https://specs.govstack.global/architecture/6-cross-functional-requirements/6.3-architecture
- GovStack messaging requirements:
  - https://specs.govstack.global/messaging/6-functional-requirements
- AWS Builders' Library (idempotent API retries):
  - https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
- Azure Compensating Transaction pattern:
  - https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction
- W3C Trace Context:
  - https://www.w3.org/TR/trace-context-1/
- OpenTelemetry context propagation:
  - https://opentelemetry.io/docs/concepts/context-propagation/
- X-Road audit log event model:
  - https://docs.x-road.global/Architecture/spec-al_x-road_audit_log_events.html
