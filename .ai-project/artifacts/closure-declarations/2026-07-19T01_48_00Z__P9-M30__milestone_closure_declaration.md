---
type: milestone-closure-declaration
milestone: M30
status: complete
completion_date: 2026-07-19
declared_by: Milestone Chat (P9-M30 — Token Measurement & Model-Tier Audit)
issued_to: Phase Chat (P9 — Context Handling and Token Efficiency)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M30

Milestone **P9-M30 — Token Measurement & Model-Tier Audit** is hereby declared **COMPLETE
(awaiting consolidation)**. All four epics — the three planned by the Milestone spec plus
E30.4, added mid-flight by P9 phase spec v1.1.0 (`e490394`, HQ's SN-23 triage) — have been
executed, independently verified by this Milestone Chat (diff review, live suite re-runs on
each epic branch, acceptance-grep checks, evidence-traceability spot-checks — not Delivery
Notices trusted on faith), accepted under PSG §11.6 default-accept, and merged to
`milestone/M30` with explicit human merge authorization for each (SN-19/§11.6). Full test
suite is green on consolidated `milestone/M30` @ `1edf04f`: **307 passed, 0 failed, no new
skips**.

**M30 is the first P9 milestone, not the last (`is_final_milestone: false`).** Two
milestones remain: **M31 (dual-mode + guardrail) consumes this milestone's outputs under
the CFO-ratified binding order** — the recorded frontier-vs-local policy and the refreshed
`.ai-project.yml` `models:` block are its direct inputs — and **M32 (SN-21 canonization +
hygiene) is independent**, schedulable by the Phase Chat at its discretion. This
declaration triggers Phase Chat consolidation of PR #135 (`milestone/M30 → phase/P9`); it
does not trigger phase closure.

## Completion Verification

✅ **E30.1 — Token-burn instrumentation (merged PR #136, `e7aef45`).** Mechanism = hybrid
A+B+C-lite: `bin/measure-token-burn` parses harness session JSONL usage blocks (72
sessions, deduplicated by API message id), attributes level/task by documented
deterministic rules with per-row confidence flags; corpus tokenized via tiktoken o200k
proxy; local ollama counts extracted from the committed P7 run (`bin/run-dev-agent`
untouched). Dataset at `.ai-project/artifacts/reference/token-measurement/` — level ×
task-type matrix with every empty cell carrying a numbered structural or gap record
(G1–G10), paid/local split, by-model mix, billed context medians. Aggregates only; no
conversation content committed (verified). Suite 307/0.

✅ **E30.2 — Audit report + policy derivation (merged PR #137, `3ad159a`).** Audit report +
`model-routing-policy.md` (rows P1–P7, each tracing to report sections and G-ids) beside
the dataset; `.ai-project.yml` `models:` refreshed — `hq`/`phase`/`milestone` →
`remote:claude-opus-4-8` (the measured workhorse; the stale `gpt-4o`/`claude-3-5-sonnet`
entries never ran one session in the window — grep verified clean), `epic_qa` →
`local:qwen2.5-coder:14b` (gap-grounded, G11); yml-spec v2.4.0 with §3.4 defaults updated
+ provenance note. Headline: ≈$623/35-day window; cache re-reads 48.5% of weighted cost;
parent-chat mixed sessions 53% of spend vs epic execution 23% — **context-load reduction
outranks model downgrade as the cost lever**. New gaps G11/G12. Hard Constraint verified:
every policy row cites data or a recorded gap.

✅ **E30.3 — Evidence-driven context-load reduction (merged PR #138, `25b5c57`).** The
deliberately-deferred epic, sized by evidence after E30.1/E30.2 merged (Sizing Decision
recorded in its spec: bounded middle path). Delivered: per-level context-scoping standard
(`context-scoping.md`) with full composition tables; pack reduction implemented in the
three starter templates — **epic 29,336 → 12,005 (−59%), milestone 36,614 → 15,971
(−56%), phase 30,478 → 14,586 (−52%) proxy tokens** with component arithmetic and
reproduction method; billed-median improvement claimed only as forward-looking. The
composition data corrected the spec's dedup-first hypothesis to section-scoping-first —
recorded with measurements, the measured-first discipline operating as designed.
Bounded-scope finding: ≥60–80% of per-call context is beyond document control; dominant
lever is behavioral (G7). New gap G13. Authorized hygiene fix (`.ai-project.yml:3` →
v2.4.0) included.

✅ **E30.4 — Reference-don't-display reconciliation, SN-23 (merged PR #139, `1edf04f`).**
Both CFO-ratified SN-23 decisions implemented: AOG §3.1.1 (v2.10.0) generalized into the
single normative reference-first handoff rule (canonical reference line; producer no-echo
half; consumer selective-read half), with the fenced full-body form retained as the marked
repo-less fallback on every surface that previously mandated it (paste not deleted —
platform agnosticism preserved). Eight surfaces edited coherently, including two mandating
surfaces found beyond the spec's named four (required by the acceptance grep over all of
`governance/`); protocol v1.3.0; E30.3's template content preserved (rebase constraint
held). Evidence: `echo-cost-note.md` — median −3,160 proxy tokens per starter handoff,
−1,815 per notice paste, honest bound stated, G14 recorded. Acceptance grep verified
clean by this Milestone Chat on the epic branch. The epic practiced its own rule; so does
this declaration's delivery.

## Milestone Definition of Done — verified

- ✅ E30.1–E30.3 each meet their Definition of Done (verified per-epic above); E30.4 meets
  its spec's DoD under phase spec v1.1.0
- ✅ All four epic branches merged to `milestone/M30` (PRs #136–#139, each human-authorized)
- ✅ Real captured token data committed: level × task-type matrix, corpus overhead
  separable, every uncaptured cell an explicit gap (G-series G1–G14 across the milestone)
- ✅ Audit report, recorded policy (documented home: reference artifact beside the
  dataset), and refreshed `models:` block exist and agree with each other (policy ↔ block
  mapping table verified identical; divergence declared an error for M31's guardrail)
- ✅ E30.3's sizing decision and proportionate outcome recorded with evidence
- ✅ Full suite green on `milestone/M30` @ `1edf04f`: 307/0, no regressions, no new skips
- ✅ This Milestone Closure Declaration produced (`is_final: false` — M31/M32 remain)

## Milestone Acceptance Criteria — verified

1. ✅ Measurement report exists with real (not estimated) per-level, per-task-type data,
   corpus overhead included, gaps explicit (E30.1/E30.2)
2. ✅ Policy recorded in its documented home; `.ai-project.yml` grep shows no
   `gpt-4o`/`claude-3-5-sonnet` remnant (E30.2)
3. ✅ Every policy statement traces to captured data or a recorded gap — none to
   assumption (Hard Constraint, verified row-by-row at E30.2 acceptance)
4. ✅ Context-load reduction exists with before/after numbers (E30.3) — no third state
5. ✅ Suite green at milestone delivery, no regressions, no new skips

## Handed to the Phase Chat

- **Consolidation:** PR #135 (`milestone/M30 → phase/P9`) is ready for Phase Chat
  acceptance and human-authorized merge.
- **Owed amendment (GH-8 precedent):** the M30 Milestone spec's epic list still reads
  E30.1–E30.3; the Phase Chat owes the amendment adding E30.4 (this milestone proceeded
  under phase spec v1.1.0's authority; recorded here so the gap is closed at
  consolidation, not forgotten).
- **M31 inputs (binding order):** the policy (rows P1–P7), the refreshed `models:` block
  (guardrail verification target), and these carried recommendations: align
  `bin/ai-project-orchestrator` `DEFAULT_MODELS` (still hardcodes falsified names;
  runtime-inert here) and extend the E26.2 consistency-guard tests beyond `epic_dev`;
  one-task-one-session discipline at parent levels (G7 — the dominant measured cost
  behavior); a post-M31 mechanism recapture to verify billed-median movement
  (forward-looking claims from E30.3/E30.4); epic-level local-offload experiment under
  dual-mode (policy row P5); price-weight TTL caveat (+18% bound if 1h-TTL writes).
- **Open gap register:** G1–G14 (G1/G3 structural; G13 HQ/Creation packs qualitative;
  G14 historical billed echo share not isolable; revisit triggers recorded per gap in
  the dataset, report, scoping standard, and echo-cost note).
- **Unowned future work:** within-session task segmentation in `bin/measure-token-burn`
  (measurement precision; report §8) — recorded, not scheduled.

---

**Milestone P9-M30 planning and delivery complete. All four Epic specs, Chat Starters, and
Epic deliveries accepted; all epic branches merged. M30 is not the final P9 milestone —
M31 consumes its policy output next (binding order); M32 is scheduled independently by the
Phase Chat. Session closes on Phase Chat consolidation of PR #135.**
