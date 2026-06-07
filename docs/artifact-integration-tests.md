# Integration Tests for Multi-Artifact Workflows

This document details the design, execution, and coverage of the comprehensive integration test suite created for the multi-artifact communication and routing protocol of the **AI Project System**.

The integration tests reside in `tests/integration/` and simulate full end-to-end multi-agent chat environments, continuous daemon background loops, error recoveries, and concurrent workload processing.

---

## Running the Integration Tests

To run the complete test suite (both unit and integration tests) with code coverage metrics:

```bash
PYTHONPATH=. pytest --cov=lib --cov-report=term-missing
```

To run only the integration tests:

```bash
PYTHONPATH=. pytest tests/integration/
```

To run a specific test scenario:

```bash
PYTHONPATH=. pytest tests/integration/test_artifact_happy_path.py
```

---

## Test Scenarios Covered

The suite covers the following 7 critical scenarios, designed to represent real-world agent and human interactions:

### 1. Scenario 1: Happy Path (Completion → Accept → Delivery)
- **Path:** `tests/integration/test_artifact_happy_path.py`
- **Workflow:** An Epic Agent produces a Completion Notice → daemon detects, routes to Milestone Chat, and archives the file → Milestone Agent reviews and produces an ACCEPT Review Decision → daemon detects, routes back to Epic Chat, and archives → Epic Agent merges the PR and produces a Delivery Notice → daemon detects, routes to Milestone Chat, and archives.
- **Verification:** Ensures correct state transitioning, folder restructuring, JSON routing triggers in `.ai-project/queue/`, and matching daemon audit logging.

### 2. Scenario 2: Rejection & Rework
- **Path:** `tests/integration/test_artifact_rejection_path.py`
- **Workflow:** Completion Notice (v1.0) is rejected with specific feedback by the Milestone Agent → routed back to Epic Chat → Epic Agent conducts rework and issues a new Completion Notice (v1.1) → Milestone Agent accepts reworked completion.
- **Verification:** Ensures that v1.0 is marked rejected, v1.1 is parsed and tracked as a new iteration, and the `ArtifactParser` indexing maintains chronological sorting (newest first).

### 3. Scenario 3: Escalation
- **Path:** `tests/integration/test_artifact_escalation_path.py`
- **Workflow:** Completion Notice is produced at Epic level → Milestone Agent receives it but cannot decide (due to ambiguity) → Milestone escalates to Phase Chat by producing a Review Decision targeting Phase P1 → Phase reviews and issues an acceptance direction targeting the Milestone Chat → Milestone issues final ACCEPT Review Decision back to Epic Chat.
- **Verification:** Ensures multi-hop hierarchical escalation routing works correctly without losing artifacts.

### 4. Scenario 4: Manual Mode
- **Path:** `tests/integration/test_manual_mode.py`
- **Workflow:** Simulates copy-pasting an artifact block directly from raw text (simulating chat history) → parses content directly and validates content structure.
- **Verification:** Verifies that artifact formatting is copy-paste friendly (only standard printable text characters) and that manual operations can coexist seamlessly alongside agentic queue processing.

### 5. Scenario 5: Agentic Mode (Continuous Background Loop)
- **Path:** `tests/integration/test_agentic_mode.py`
- **Workflow:** Spawns a background thread running `daemon_artifact_monitoring_loop` with a fast sampling interval (0.05 seconds).
- **Verification:** Ensures that the continuous loop autonomously scans, detects, parses, routes, and logs all three artifact types in real time.

### 6. Scenario 6: Error Scenarios & Failure Recovery
- **Path:** `tests/integration/test_error_scenarios.py`
- **Workflows:**
  - **Corrupted YAML:** Malformed YAML delimiters/keys are gracefully caught and moved to `.failed/` without crashing the daemon.
  - **Missing Fields:** YAML missing required fields (like `deliverables`) is caught and archived to `.failed/`.
  - **Invalid References:** Invalid reference ID formats (e.g. non-ISO IDs like `E14-1`) are rejected and archived to `.failed/`.
  - **Concurrency Lock Timeout:** Employs `fcntl.flock` to exclusively lock an artifact. The daemon gracefully logs a timeout and does not move or lose the file, leaving it in place for retry. Once the lock is released, the daemon successfully processes it.

### 7. Scenario 7: Parallel Workloads
- **Path:** `tests/integration/test_parallel_artifacts.py`
- **Workflow:** Simulates 5 concurrent Epics completing simultaneously (within 100ms) under the same milestone by writing 5 Completion Notices, 5 Review Decisions, and 5 Delivery Notices concurrently.
- **Verification:** Validates that the daemon routing logic processes 15+ simultaneous artifacts with zero race conditions, zero duplicates, and zero lost files.

---

## Test Infrastructure & Shared Fixtures

The test suite relies on pytest shared fixtures defined in `tests/integration/conftest.py`:

- `tmp_project`: Constructs a fresh, isolated temporary project directory simulating real `.ai-project` directories (e.g. `artifacts/completion-notices`, `queue`, `logs`).
- `clean_loggers`: Autouse fixture that purges and closes global logger handlers between tests. This prevents Pytest singleton-state leakages across test boundaries.
- `make_completion_notice`, `make_review_decision`, `make_delivery_notice`: Return customizable factory functions to write valid YAML-frontmatter markdown artifacts dynamically inside tests.

---

## Code Coverage Metrics

The parser and router components achieve extremely high coverage:

| Module | Statements | Missing Lines | Coverage | Description |
| :--- | :--- | :--- | :--- | :--- |
| `lib/artifact_parser.py` | 216 | 0 | **100%** | Full frontmatter splitting and schemas validation |
| `lib/artifact_schemas.py` | 160 | 2 | **99%** | Field type, formatting, and structural checks |
| `lib/artifact_router.py` | 235 | 11 | **95%** | Safe directory monitoring, file locking, and routing triggers |
| `lib/daemon_extensions.py` | 74 | 7 | **91%** | One-off scanning and background monitor loops |
| **TOTAL** | **701** | **20** | **97%** | Comprehensive high-reliability test gate |
