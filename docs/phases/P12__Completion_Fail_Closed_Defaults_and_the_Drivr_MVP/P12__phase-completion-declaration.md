---
type: phase-completion-declaration
phase: P12
name: "Completion: Fail-Closed Defaults and the Drivr MVP"
status: COMPLETE (awaiting consolidation)
declared_date: 2026-09-07
declared_by: Phase Chat (P12)
acceptance_model: "SN-13 default-accept as amended by P12-M43-E43.2 — a clean delivery is accepted by an acknowledgment that NAMES the party that reviewed and accepted; silence accepts nothing."
---

# Phase P12 Completion Declaration

**Phase P12 — Completion: Fail-Closed Defaults and the Drivr MVP is COMPLETE (awaiting
consolidation).**

All seven planned Milestones are fully closed into `phase/P12`. **The phase remains open**: this
declaration is written at §5C Step 2 and does not close it. Step 9's Phase-Closure Declaration, on
`master`, records the delivered state after consolidation.

> **This is the first Phase Completion Declaration ever written**, and P12 built the artifact it is
> being closed with. M44's E44.1 landed the template and named it at §5C Step 2 to discharge
> `P11-GH-3` — *phase closure has no pre-merge completion artifact*, a gap the **CFO** found. The
> phase's opening said it would be its own first customer; this document is that.

---

## ⚠ THE ONE SENTENCE THIS PHASE SHOULD BE READ BY

> **When the evidence that should gate an action is absent, the action proceeds — that was the
> finding P12 opened on, confirmed in four instances; and the phase's work was to make absence stop
> the action instead, at the execution tier, the acceptance chain, the completion signal, the
> surface, and finally in one real agentic run that can be shown to have done work rather than
> merely to have exited.**

---

## Verification Checklist

Each phase completion criterion, with its verification status. **All twenty are satisfied.**

| # | Completion criterion (phase spec §Success Criteria) | Status |
|---|---|---|
| 1 | `epic_dev`/`epic_qa` measured separately against the incumbent | **Satisfied** — M41 |
| 2 | Every moved row passed its harness before landing | **Satisfied** — M41, with the landing recorded honestly as CFO-decided outside the machinery |
| 3 | Line-up, policy mapping table and row P4 agree | **Satisfied** — M41; row P4's language rewritten by M44/E44.2 |
| 4 | **No path in `bin/` proceeds on absent gating evidence** | **Satisfied** — M42 (sandbox absence aborts, staging epic-scoped, approval failure aborts, `--admin` gone, `ai-project-init` never manufactures an agent) |
| 5 | The suite asserts the guard rather than the defect | **Satisfied** — M42's inverted tests; `tests/test_init_agent_path.py` green |
| 6 | **A child never holds merge authorization** | **Satisfied** — M43/E43.1; every milestone consolidation since was performed by the parent |
| 7 | **Acceptance is distinguishable from absence** | **Satisfied** — M43/E43.2; *silence accepts nothing* |
| 8 | Exhausted rework flips the parent to manual by default | **Satisfied** — M43/E43.4, blessed in the yml spec |
| 9 | Resume restores the declared mode, never promotes, never resets the counter | **Satisfied** — M43/E43.4 |
| 10 | **One statement governs the rework limit**, itemized to every surface | **Satisfied** — M43/E43.3; `P12-GH-1` **closed** (0 → 7 of 25 templates) |
| 11 | **Phase closure has a pre-merge completion artifact** | **Satisfied** — M44/E44.1; **this document is its first instance** |
| 12 | HQ re-instantiation ritual in one normative place | **Satisfied** — M44/E44.1, recorded from nine instances with three divergences reported |
| 13 | Context-exhaustion handoff has a type and template | **Satisfied** — M44/E44.1 |
| 14 | `governance-propagation.md` states only true constraints | **Satisfied** — M44/E44.5; all three Constraints struck under two clauses |
| 15 | AOG sections uniquely numbered and titled | **Satisfied** — M44/E44.4; `1..18` monotonic, fenced examples byte-identical |
| 16 | **The completion signal is trustworthy, or its limit is measured** | **Satisfied** — M45; `_decide` reads `Role.INSPECTION`, `undetermined` first-class end to end, `P10-GH-7` **re-rated on measured evidence** |
| 17 | **Drivr's MVP surface makes ≥3 governance rules unrepresentable** | **Satisfied** — M46/E46.3; a **closed** capability domain, not runtime validation |
| 18 | A model may not be swapped without a qualification suite whose bar preceded it | **Satisfied** — M46/E46.5; bar `95f7656` precedes gate `f33af95` |
| 19 | **One real epic carried end to end agentically by Drivr** | **Satisfied** — M47; `P1-M1-E1.1` on `panchew-io`, **111 tool rounds, 21 files**, instrument verdict `PASS` |
| 20 | Parked and deferred items recorded with triggers; llama.cpp **closed** | **Satisfied** — phase spec `:604`, *"CLOSED by CFO decision, not parked"* |

**Additionally disposed at closure:** the phase spec's `model_verification` criterion — **disposed by
its second path, *record why not*** (CFO, 2026-09-07). See §Carry-Forwards, `P12-CF-1`.

**Suite:** `774 passed` (`PYTHONPATH=. pytest -q`, `phase/P12`, 2026-09-07). **Config:** `0 errors,
0 warnings`. **Drivr:** `581 passed` at `main` `114de1c`.
*The `ai-project-system` count is **environment-dependent** — `766+1 skipped` / `767` / `766+1 failed`
are the same suite before this session's `+7`; the variance is the live-ComfyUI integration test.*

---

## Milestone Table

| Milestone | Epics | PR | Merge commit (into `phase/P12`) |
|---|---|---|---|
| M41 — The Model Line-Up and Its Evidence | E41.1–E41.5 | #241 | `3925aea` |
| M42 — Fail-Closed Execution Tier | E42.1–E42.5 | #248 | `90335ca` |
| M43 — The Acceptance Chain, Made Structural | E43.1–E43.4 | #254 | `33256f4` |
| M44 — Rituals, Records, and the Normative Repairs | E44.1–E44.6 | #262 | `c43ad1b` |
| M45 — Trustworthy Completion Signal | E45.1–E45.4 | #267 | `cd1b490` |
| M46 — The Drivr MVP Surface | E46.1–E46.5 | #273 | `393a240` |
| M47 — First Real Agentic Integration | E47.1–E47.3 | #279 | `2a66b4a` |

**Seven milestones, thirty-two epics.** Every milestone consolidation was performed by the parent
(E43.1) on explicit CFO authorization, and every acceptance from M43 onward was a **named**
acknowledgment (E43.2).

---

## Phase Summary

P12 was scoped as **completion, not redesign**, on a confirmed finding: *when the evidence that should
gate an action is absent, the action proceeds.* It closed that disposition at every tier it had been
found in — `bin/` no longer proceeds on absent gating evidence; a child cannot hold merge
authorization and acceptance is no longer indistinguishable from absence; the completion signal can
say **`undetermined`** and carry it end to end without folding; and the Drivr surface makes three
governance rules **unrepresentable** rather than merely validated.

It then **used** what it built: one real epic on a real project, carried end to end agentically
through Drivr and checked by an instrument whose bar was committed before it ran — so the record shows
the work was **done**, not merely that a process exited. `undetermined` became a first-class state at
six substrates; `P12-GH-1` and `P12-GH-2` closed; `P10-GH-7` was re-rated on measured evidence.

**What a successor receives:** a framework whose gates fail closed by construction rather than by
compliance, a completion signal that can admit ignorance, a surface that cannot express the violations
it used to validate, and a proof run that states its own limits — **one project, one epic, one
engine.**

---

## Carry-Forwards — recorded with owners and triggers

**Closed during P12:** `P12-GH-1` (rework limit reached one surface — E43.3), `P12-GH-2` (init
manufactures a placeholder and validates it — E42.4/E42.5; **its note had gone stale `active` and was
closed at this declaration's assembly**).

| ID | Item | Owner | Trigger |
|---|---|---|---|
| **`P12-CF-1`** | **`model_verification` flip, `advisory → blocking`.** Disposed by *record why not* (CFO, 2026-09-07). The three governed rows that would halt **cannot be measured** — the key governs manual instances only, E46.3 made phase/milestone dispatch unconstructible, and the instrument's lanes are `epic_dev`/`epic_qa`. **The key is blessed** (§3.9, rule 29). | HQ | **Arm when `models.phase`, `models.milestone` and `models.epic_manual` name what those chats actually run on.** E41.5's ungated rows, `epic_manual`'s missing attribution row, and R6's unperformed surface confirmation ride with this. |
| `P12-GH-3` | Derived-claim rot — a correction is itself a derived-claim event | unowned | Filed with its trigger; M44 confirmed **not absorbed** |
| `P12-GH-4` | The inter-chat channel is ungoverned | partially landed | Narrow half landed in M44/E44.3; the remainder is open |
| `P12-GH-5` | Declared context exceeds loaded | unowned | Filed with its trigger |
| — | **Drivr has no remote** — every Drivr commit exists on one disk; no PR exists for any Drivr change | Phase/HQ | CFO has ruled *"Drivr code local-only for now"*; revisit on publication-model decision |
| — | **Delivery Notice location split** — the corpus is **bi-located** (`.ai-project/artifacts/delivery-notices/` vs `docs/phases/…`); template and practice disagree, no test catches it | unowned | Observed since **P11-M40**; M44 reproduced **both sides in a single milestone** |
| — | **Duplicate `Error Handling` content in the AOG** — the *title* collision is resolved, the duplicated *content* is not | unowned | M44/E44.4, in scope: no content deletion |
| — | **Closed-phase sweep scope** — does *corpus-wide* include the closed record? | unowned | E44.4 correctly left P6/P7/P8 untouched; wants a ruling **before** a future sweep asks |
| — | **The `ai-project-system` suite is non-deterministic where `visual_artifacts.enabled: true`** — the live-ComfyUI test runs, skips or fails by machine; a full run took 38 s vs 176–213 s, and produced pass / fail / pass on identical commits | unowned | **Never formally filed until now.** *"Suite green" is the gate every closure reports against* |
| — | **`panchew-io` reverted a CFO-authorized `models:` block through its own restructure** — the fix `863eb49` is orphaned from `main` and `milestone/M1`; the file has **no `models:` block** | fleet | M47 Finding 1, verified live 2026-09-07. Trigger: any fleet project whose governed config can be silently reverted by its own restructure |

---

## Notes

- This declaration is **Step 2 of the PSG §5C phase-closure sequence** — written **while the phase is
  still open**, before the README update, version bump and git tag (Steps 3, 4, 8), and before Step
  9's Phase-Closure Declaration on `master`.
- **Step 6 reviews this artifact.** Its verification checklist and milestone table are what the
  reviewing level receives; Step 9's declaration is unmoved and records the delivered state after
  consolidation.
- **Acceptance model:** SN-13 default-accept **as amended by E43.2** — a clean delivery is accepted by
  an acknowledgment that **names** the party that reviewed and accepted. **Silence accepts nothing.**
