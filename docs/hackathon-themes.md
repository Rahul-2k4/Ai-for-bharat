# AI for Bharat 2 - Theme Statements (Offline Copy)

Last verified: 2026-04-15 (Asia/Kolkata)

## Theme 1

Unified Business Identifier (UBID) and Active Business Intelligence by Karnataka Commerce and Industry.

### Problem Summary

- Build cross-system business linking across 40+ department systems.
- Assign one UBID per real business with confidence-based matching and human review.
- Infer Active, Dormant, Closed status from one-way activity streams.

### Non-Negotiables

- No source-system modification, re-platforming, or migration.
- Use scrambled or synthetic data in sandbox for Round 2.
- Automated decisions must be explainable and reversible.
- Hosted LLM calls on raw PII are not permitted.

### What Submission Should Cover (Round 1)

- Entity resolution approach, confidence thresholds, and review workflow.
- Activity inference logic and explainability path.
- Architecture, model/tech choices, risks, and Round 2 implementation plan.

## Theme 2

Two-Way Interoperability between the Single Window System (SWS) and Department Systems by Karnataka Commerce and Industry.

### Problem Summary

- Propagate service requests both directions between SWS and legacy systems.
- Use UBID as the common join key.
- Handle schema/API heterogeneity, retries, idempotency, and drift.
- Resolve near-simultaneous conflicts with clear policy and full auditability.

### Non-Negotiables

- Neither SWS nor department systems can be modified.
- UBID is the required join key.
- Propagation must be idempotent and fully auditable.
- Round 2 runs on scrambled/synthetic sandbox data only.
- Hosted LLM calls on raw PII are not permitted.

### What Submission Should Cover (Round 1)

- Bidirectional propagation design and schema translation strategy.
- Change discovery for systems that lack native events.
- Conflict resolution policy and reversible/auditable outcomes.
- Architecture, tech choices, risks, and Round 2 implementation plan.

## Theme 3

AI-Based Tender Evaluation and Eligibility Analysis for Government Procurement by CRPF.

### Problem Summary

- Extract eligibility criteria from tender documents.
- Parse heterogeneous bidder documents (typed/scanned PDFs, Word, images, tables).
- Evaluate bidder eligibility per criterion with explainable verdicts.
- Route ambiguous cases to manual review; produce auditable consolidated reports.

### Non-Negotiables

- Criterion-level explainability is mandatory.
- Never silently disqualify bidders.
- Must support scanned documents and photographs.
- End-to-end auditability is required for government decision context.
- Round 2 runs on representative mock/redacted sandbox data.

### What Submission Should Cover (Round 1)

- Criteria extraction and mandatory/optional separation strategy.
- Multiformat bidder document parsing and mapping to criteria.
- Explainable decision logic, ambiguity handling, and review path.
- Architecture, tech/model choices, risks, and Round 2 implementation plan.

## Sources

- Theme 1 raw HTML: `tasks/research/raw/custom-tabs/theme-1.html`
- Theme 2 raw HTML: `tasks/research/raw/custom-tabs/theme-2.html`
- Theme 3 raw HTML: `tasks/research/raw/custom-tabs/theme-3.html`
- Live URLs:
  - https://www.hackerearth.com/challenges/hackathon/ai-for-bharat-2/custom-tab/theme-1/
  - https://www.hackerearth.com/challenges/hackathon/ai-for-bharat-2/custom-tab/theme-2/
  - https://www.hackerearth.com/challenges/hackathon/ai-for-bharat-2/custom-tab/theme-3/
