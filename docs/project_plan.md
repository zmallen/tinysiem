# Tiny SIEM : Project Plan

## Mission
Build a small, local, open-source detection engine in public to teach
detection-engineering concepts through implementation.

## Audience
Detection engineers, threat hunters, security engineers, software engineers and practitioners
learning how telemetry becomes an alert.

## Season 1 outcome
By the end of 10 weeks, the project will:
- Ingest and validate synthetic JSONL telemetry
- Normalize at least two source formats into a canonical event model
- Evaluate atomic, correlation, and simple deviation-style detections
- Enrich events with local contextual data
- Emit evidence-backed alerts with deduplication
- Run a regression-test suite against scenario fixtures
- Ship as a documented local CLI with a v0.1.0 release

## Non-goals
- Production SIEM deployment
- Live customer, employer, or personal telemetry
- A web dashboard
- Cloud-scale ingestion and storage
- Full Sigma compatibility
- Autonomous response
- Broad LLM access to data or actions

## Operating cadence
- Four 30-minute coding blocks each workweek
- One issue completed or materially advanced each week
- One tested vertical slice every two weeks
- One public concept post every two weeks
- One paid build companion every two weeks
- One tagged release and retrospective each month

## Definition of done for an issue
- Acceptance criteria are written before implementation
- Code change is focused and documented
- Positive and negative tests or fixtures exist
- Agent-generated code received independent review
- README or lesson documentation is updated if behavior changed
- The issue records what remains out of scope

## Season 1 milestones
1. Foundation: schema, JSONL ingestion, validation, fixtures, CI
2. Atomic detections: rule model, predicates, evidence-backed alerts
3. Context: enrichments, alert schema, provenance
4. Correlation: sequences, joins, thresholds, windowed state
5. Behavioral signals: first-seen, rarity, simple baselines
6. Feedback: fingerprinting, deduplication, disposition, tuning inputs
7. Testing and release: scenario suite, docs, v0.1.0 retrospective

