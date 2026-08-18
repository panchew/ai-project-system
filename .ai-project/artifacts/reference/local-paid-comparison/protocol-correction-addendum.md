---
artifact_type: protocol_correction
artifact_version: 1.0
timestamp: 2026-08-14T19:30:00Z
issuer_chat: Epic Agent (P11-M38-E38.6)
issuer_role: Epic Agent
status: pre-registered
epic_id: P11-M38-E38.6
milestone_id: P11-M38
phase_id: P11
project_name: ai-project-system
governs: Review Decision 2026-08-14T19:06:56Z (REJECT, action: rework)
---

# Protocol-Correction Addendum — E38.6 resubmission

**This addendum is committed BEFORE any replacement run.** It is the pre-registered
authorization for replacement runs, per Review Decision `2026-08-14T19:06:56Z` (Findings 1
and 2). Git history proves it precedes the replacement runs it authorizes.

## 1. Paid run 1 is a protocol-invalid trial

**Paid run 1 is identified as a protocol-invalid trial — not a scored arm and not a
candidate result.** It violated the frozen condition that the paid arm receive **the blinded
packet content only**, because it had repository access and read the committed answer
(`927b7fa`). Its INVALID classification stands; it is preserved in the record and is not
scored, not selected, and not used in any judgment.

**Authorization for one replacement paid arm:** exactly one replacement paid run is
authorized, solely because the original violated a frozen execution condition. Its frozen
conditions:

- a fresh manual session at `models.epic_manual` (`remote:claude-opus-5`);
- **the original blinded packet content only** — nothing else, no repository, no git, no
  search, no post-fix artifacts, no web;
- no evaluator follow-up, no clarification, no re-prompting;
- the **original rubric unchanged**;
- wall-clock start and end timestamps captured.

## 2. Local run 1 is a protocol-invalid trial (environment mismatch)

**Local run 1 is identified as a protocol-invalid trial — not a scored arm and not a
candidate result.** It violated the frozen condition that the local arm run through Drivr's
`OpenCodeAdapter` in `ContainerEnvironment (debian:12-slim)`; it ran **directly on the host**
via a bare `opencode run` invocation. Its retained output is preserved in the record and is
not scored, not selected, and not used in any judgment. (The Delivery Notice's `host`
statement was accurate; the conflict was with the registered condition, and the reviewer
correctly identified it.)

**Authorization for one replacement local arm:** exactly one replacement local run is
authorized, solely because the original did not follow a frozen execution condition. Its
frozen conditions:

- Drivr's `OpenCodeAdapter`;
- `ContainerEnvironment` (`debian:12-slim`), drivr's default;
- model `ollama/qwen3-coder:30b`;
- working directory: the same isolated, git-free workspace with the two pre-fix files
  (`.ai-project/registry/fleet-registry.yml` and `tests/test_fleet_registry.py`);
- the original blinded packet content as the task;
- the original rubric unchanged;
- wall-clock start and end timestamps captured.

## 3. No best-of-N, no prompt tuning, no suppression

Every run made — original and replacement — stays in the record. The replacement is not
selected *as better* than the invalid trial; it is the only valid run, and the invalid
trial is retained as the protocol-failure record. No prompt is tuned, no packet is edited.

## 4. Ordering

This addendum is committed **before** replacement runs 2 (local) and 2 (paid) are made. The
resulting valid local/paid pair is scored against the original rubric; the judgment is
recomputed from that pair only.
