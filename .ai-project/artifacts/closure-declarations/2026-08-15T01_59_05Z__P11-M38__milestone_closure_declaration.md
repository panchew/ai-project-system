---
type: milestone-closure-declaration
milestone: M38
status: complete
completion_date: 2026-08-15
declared_by: Milestone Chat (P11-M38 — Drivr Inception, Fleet Registry, and the Execution Adapter Surface)
issued_to: Phase Chat (P11 — Drivr: Coordination over Rented Execution)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M38

Milestone **P11-M38 — Drivr Inception, Fleet Registry, and the Execution Adapter Surface** is hereby
declared **COMPLETE (awaiting consolidation)**. Six epics — **E38.1 through E38.6** — have been
executed, independently reviewed by this Milestone Chat, and merged to `milestone/M38` with explicit
human merge authorization for each (SN-19 / PSG §11.6).

**M38 is NOT P11's final milestone.** After Phase Chat review and consolidation into `phase/P11`,
the Phase Chat proceeds to **M39 planning — Trustworthy Completion Signal**. M39 still gates M40;
`phase/P11` is not merged to `master` at this closure.

Final verification on `milestone/M38` @ `61848344dc4ecd8639465174381c03f9693cc6b6`:

```text
ai-project-system: PYTHONPATH=. pytest -q
                   489 passed in 25.97s

drivr @ 31dad512858cdbb4bfb726bd1c07717ee42ba2e1:
                   47 passed in 1.07s

embedded orchestrator suite:
                   19 tests, OK
```

The first `ai-project-system` run in the review sandbox was not a product result: the sandbox denied
loopback socket creation and the configured live ComfyUI endpoint, producing 27 setup errors and one
endpoint failure after 459 tests passed. The same commit was immediately re-run at the host layer,
where all **489 tests passed**. This declaration uses the host-layer result because the affected tests
explicitly exercise loopback and live-endpoint behavior.

---

## Completion Verification

| Epic | Merge | PR | Stage-2 outcome |
|---|---|---:|---|
| **E38.1** — Drivr repository inception and enrollment | `8220d0e` | #193 | ✅ ACCEPT after `.governance` rework and one pre-merge annotation |
| **E38.2** — execution adapter surface and OpenCode adapter | `c0be776` | #195 | ✅ accepted in Milestone Chat; Stage A → Stage B gate closed |
| **E38.3** — fleet registry, §4 validator, and `framework_version` schema entry | `4d8f733` | #196 | ✅ ACCEPT after two record-integrity corrections |
| **E38.4** — `local-agent-runner` retention assessment | `2f6a506` | #197 | ✅ accepted in Milestone Chat |
| **E38.5** — milestone-context capacity evidence | `7fafa92` | #198 | ✅ ACCEPT after exact-context remeasurement and three annotations |
| **E38.6** — local/paid controlled comparison | `6184834` | #199 | ✅ ACCEPT at re-review 04 after protocol and record corrections |

E38.1, E38.3, E38.5 and E38.6 carry committed Review Decision artifacts. E38.2 and E38.4 were
reviewed and accepted in the Milestone Chat but have no separate committed Review Decision artifact;
their two-parent merge commits and the human authorizations in chat are the durable merge record.

---

## Independent milestone remeasurement

The closure does not treat the Delivery Notices as their own evidence. The Milestone Chat re-read the
merged implementations and retained machine-readable artifacts, re-ran the two repository suites,
re-ran the §4 fleet validator, inspected the Drivr adapter and environment registrations, counted the
registry entries, and checked the milestone diff for M39/M40 surfaces.

### Drivr exists, is governed, and rents execution

- Drivr exists at `~/soft-dev/drivr`, on `main` @
  `31dad512858cdbb4bfb726bd1c07717ee42ba2e1`.
- `.ai-project.yml` states `framework_version: v7.1.0` and
  `governance.submodule_path: .governance/`; `.gitmodules` names and mounts `.governance` and tracks
  `v7.1.0`.
- Confirmation evidence captured from Drivr is committed in this repository at
  `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M38-E38.1__confirmation-evidence.md`.
- Drivr's current suite passes **47/47**, grown from E38.1's established **2/2** baseline.
- `ExecutionAdapter`, `ExecutionRequest` and `ExecutionResult` form the engine-neutral interface.
  `OpenCodeAdapter` is the real engine adapter; `EchoAdapter` is the second-adapter demonstration.
  The registration tests instantiate both without changing coordination code.
- `ContainerEnvironment` is the default, with `HostEnvironment` implemented and selectable. The
  recorded decision rejects the framework's project sandbox as the OpenCode execution home: the host
  OpenCode binary is mounted into a fresh `debian:12-slim` container, provider loopback is rewritten,
  and a materialized configuration copy is used. Host dispatch remains available and its surrendered
  isolation is stated.
- A real end-to-end OpenCode invocation ran through the adapter. Its task result was intentionally
  not converted into a completion verdict; M39 owns that judgment.
- The adapter's usable `qwen3-coder:30b` limit is **32,768**, observed after load from Ollama
  `/api/ps`. The stock/trained maximum of **262,144** is recorded but not used.

### The fleet is a data structure and §4 is executable

- `.ai-project/registry/fleet-registry.yml` contains **15 project entries**, exceeding the milestone
  spec's inherited fourteen-project floor. It includes `panchew-io`, `fieldledger-assesment`, Drivr,
  `ai-stack`, and `character-factory`.
- The accepted 2026-08-11 enumeration found **17 immediate directories**, excluded two confirmed
  worktrees, and classified **15/15 projects**: 13 enrolled and two unenrolled. Nine enrolled configs
  were §4-valid and four were §4-invalid.
- The registry distinguishes `active`, `benched`, and `archived`; zero projects were silently inferred
  to be archived. Recorded decisions and proposals remain distinguishable.
- `bin/ai-project-validate` enforces the checkable rules in `ai-project-yml-spec.md` §4 and reports
  schema-drift warnings separately from errors. Its negative controls and **96 repository tests**
  (79 validator plus 17 registry tests at final accepted state) demonstrate rejection of invalid
  input and invariants over the committed fleet snapshot.
- A closure-time `--fleet /home/panchew/soft-dev --json` run reproduced the accepted four invalid
  enrolled configs and their eight errors. It also counted the two E38 worktrees separately, exactly
  the layer distinction the registry records.
- `P10-GH-1` was **folded in**, not parked: `governance/ai-project-yml-spec.md` v2.8.0 defines the
  optional `framework_version` field, its self-referential-source exemption, and §4 rule 26.
- Fleet-state transitions are an append-only recorded human action. `transitions: []`; no timer, hook,
  inactivity rule, scheduler, or automatic state mutation exists.

### The three evidence questions were answered without taking M39's decisions

1. **`local-agent-runner`: retain for now, principally for C3.** E38.4 assessed all three candidates
   against C1, C2 and C3. OpenCode has no Python in-process entry point for Python Drivr (C1); its
   typed-tool path does not recover or reject the measured unusable values as the runner does (C2);
   and it distinguishes finish, crash and abort but returns ordinary `finish: "stop"` when its
   configured step ceiling is reached (C3). The runner retains the explicit
   `max_iterations_exceeded` status / exit 2 distinction. The E38.4 harness was first verified against
   a known nonzero case. Nothing was retired, and Route B.2 did not fire.
2. **Milestone-context capacity: FAIL at the loaded deployment window.** E38.5 reconstructed
   **147,571 bytes** of prescribed session-start source and tested a documented **147,626-byte**
   superset. Ollama encoded **38,465 input token IDs**, evaluated 32,767 within the observed
   **32,768-token** loaded window, preserved the tail instruction, and lost the position-zero marker
   without warning. This is a fourth capacity axis. It does **not** decide routing-policy row P4;
   G-P4-a/b/c remain unaffected.
3. **Controlled comparison: valid pair completed both ways.** Under the pre-registered rubric and
   G1/G2, local run 2 used Drivr's `OpenCodeAdapter` in `ContainerEnvironment` with
   `qwen3-coder:30b` and scored **MISS**. Paid run 3 used a fresh human-operated, packet-only
   `claude-opus-5` session and scored **CATCH**. The invalid local run 1 and paid runs 1–2 remain
   preserved and excluded for their recorded protocol defects. The comparison changes no routing
   policy and leaves the “therefore” to the CFO and M39.

---

## Milestone Definition of Done — verified

| # | Item | Status |
|---:|---|---|
| 1 | E38.1 through E38.6 each meet their own DoD | ✅ accepted per Epic |
| 2 | All six Epic branches merged to `milestone/M38` | ✅ `8220d0e`, `c0be776`, `4d8f733`, `2f6a506`, `7fafa92`, `6184834` |
| 3 | Drivr exists, is enrolled at a stated `framework_version`, and confirmation evidence is committed here | ✅ `v7.1.0`; E38.1 confirmation evidence |
| 4 | Adapter interface exists; real engine invoked end-to-end; environment/isolation decision recorded | ✅ E38.2 |
| 5 | A second adapter can be added without changing coordination | ✅ `EchoAdapter` registration demonstration |
| 6 | Declared context limit derives from `/api/ps`, not trained maximum | ✅ 32,768 observed; 262,144 rejected as denominator |
| 7 | The required fleet is classified, including named edge cases | ✅ accepted snapshot classifies 15/15, including all named cases |
| 8 | A validator enforces §4 and has run against the real fleet | ✅ re-run at closure; known invalid configs reported rather than hidden |
| 9 | P10-GH-1 folded in or parked with reason | ✅ folded into yml spec v2.8.0 |
| 10 | Fleet transitions are recorded human actions; nothing automatic exists | ✅ empty append-only transition log, no automation |
| 11 | Runner retention answered across C1/C2/C3; harness nonzero control verified; nothing retired | ✅ retain principally for C3 |
| 12 | Milestone-context capacity measured; row P4 explicitly not decided | ✅ capacity FAIL; P4 untouched |
| 13 | Local/paid comparison run and recorded both ways under G1/G2 | ✅ valid local-2 / paid-3 pair |
| 14 | Nothing from M39/M40 built | ✅ no completion judgment, scheduler, derived gate queue, or thin surface |
| 15 | G11 not claimed without a real `epic_qa` run | ✅ not claimed |
| 16 | Structural diagram on every delivery amending a normative document | ✅ E38.3 fired the constraint and carries the diagram; no other Epic amended the normative tier |
| 17 | This repository's suite green, no regressions or new skips; Drivr baseline stated | ✅ 489/489 here; Drivr 47/47 current, 2/2 inception baseline |
| 18 | Milestone Closure Declaration produced (`is_final: false`) | ✅ this document; M39 planning follows consolidation |

---

## Acceptance Criteria — verified

1. ✅ **Drivr exists, is governed, and calls a CLI tool that owns inference** through an adapter
   interface with a demonstrated second implementation.
2. ✅ **A real engine ran**, with the dispatch environment, host fallback, config materialization,
   loopback rewrite, and surrendered isolation recorded.
3. ✅ **The fleet became a committed data structure**: the accepted snapshot classifies all fifteen
   measured projects, and the §4 validator demonstrably rejects invalid input.
4. ✅ **Runner retention rests on C1/C2/C3 evidence and nothing was retired**; C3's configured-ceiling
   distinction is available to M39 without rediscovery.
5. ✅ **Milestone-context capacity was measured as a fourth axis and row P4 was untouched.**
6. ✅ **The local/paid comparison was run and recorded both ways**; invalid trials were excluded rather
   than laundered into the valid pair.
7. ✅ **The M39/M40 hard gate remains intact.** Drivr reports execution observations and does not
   decide completion; no scheduler or derived gate queue exists.
8. ✅ **This repository's final host-layer suite is green: 489 passed.**

---

## Closure findings and handoff

### 1. The registry is a dated human record, and the fleet moved after its accepted snapshot

The accepted E38.3 registry measured `~/soft-dev` on **2026-08-11** and classified all fifteen
projects then present. Closure-time enumeration on 2026-08-15 sees two additional config-less
directories not in that snapshot:

| Directory | Created | Contents at closure |
|---|---|---|
| `interview-practice-luflox` | 2026-08-12 | Ruby interview-practice files; no `.ai-project.yml` |
| `practice` | 2026-08-14 | two Ruby practice files; no `.ai-project.yml` |

This does not falsify M38's dated acceptance claim: the milestone required the original fourteen
project directories and E38.3 classified fifteen. It does demonstrate that the registry is not an
automatic inventory and must never be described as timelessly exhaustive. Whether either directory
is a fleet project, and its initial classification if so, is a **new recorded human action**. This
declaration neither guesses nor mutates the registry.

### 2. Four enrolled configs remain invalid by design of this milestone's scope

The validator reports eight errors across `ai-project-system-mcp`, `courtis`, `home_finance`, and
`social-stories-creator`. E38.3 was authorized to classify and validate, not edit enrolled projects.
The invalid states are evidence that enforcement is real, not unresolved validator work. The
accepted escalation record preserves the remediation questions.

### 3. M39 receives evidence, not conclusions disguised as plumbing

M38 hands M39 three load-bearing facts: OpenCode does not expose configured ceiling exhaustion as a
distinct returned completion signal; the current 32,768-token deployment silently truncates M38's
session-start context; and the valid controlled task was caught by the paid arm but missed by the
local arm. M38 deliberately does not convert any of those facts into row-P4 movement, routing policy,
or completion judgment.

---

## Consolidation instruction

Submit this declaration to the **P11 Phase Chat** as the **M38 Milestone Review Request**. After a
Phase-level ACCEPT and explicit human authorization, merge `milestone/M38` into `phase/P11`. Then,
and only then, proceed to **M39 planning**.
