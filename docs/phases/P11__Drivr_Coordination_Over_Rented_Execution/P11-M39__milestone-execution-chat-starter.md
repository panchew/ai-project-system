---

# Milestone Execution Chat Starter — P11-M39

**Milestone:** P11-M39 — Trustworthy Completion Signal (P10-GH-7)
**Phase:** P11 — Drivr: Coordination over Rented Execution
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M39__milestone-spec.md`
**Execution Mode:** manual — the ratified matrix permits agentic-or-manual; this instance is declared
**manual**. M39 carries the phase's load-bearing technical risk and one genuinely unsolved design
question, and the chat planning it runs paid.

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat** for
Milestone P11-M39.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.4.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.10.0

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.10.0
3. This Milestone Execution Chat Starter
4. Milestone Spec (`P11-M39__milestone-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Milestone** — Stage 1: produce Epic specs and Epic
  Execution Chat Starters, commit them to `milestone/M39`, open a PR; Stage 2: oversee Epic delivery,
  accept clean deliveries **by silence** (a Review Decision is the exception path only, PSG §11.6), and
  merge each accepted Epic to `milestone/M39`.
- You MUST NOT implement project code or modify infrastructure — planning and delivery artifacts only.
  **You do not write the completion judgment**; that is the Epics' work, in Drivr.
- You MAY create the `milestone/M39` branch **from `phase/P11`**, commit Epic specs and Starters, and
  open a PR.
- **Artifact scope (adjacency):** **Epic specs and Epic Execution Chat Starters only.** Not the
  Milestone spec (your parent's — it exists), not the Phase spec, not any M40 work.
- You do NOT dispatch Epic/Coding Agents directly — Starters go to the Phase Chat, which authorizes
  each launch.
- You report to the **Phase Execution Chat (P11)**; communicate downward only. Do NOT reach across to
  sibling milestones (M36–M38 closed; M40 unplanned).
- **Mid-flight amendments:** amend the governing Epic spec, note it in its Amendment History, notify
  the Phase Chat — **do not reach into running sessions.**
- **Merge authorization is an in-chat act, no ceremonial artifact** (SN-19 / PSG §1A under §11.6), and
  **merge authorization for a child PR belongs in the Phase Chat's Stage-2 review.** If authorization
  reaches you directly, **confirm upward before acting** — P9-GH-1's guard reaches only the Epic
  template and a live instance was recorded 2026-08-10.
- **PSG §11.6.1 is in force.** Silence accepts *your children's* clean deliveries, never HQ's output.
- **M39 is NOT P11's final milestone** (`is_final: false`). Your Closure Declaration hands back for
  **M40 planning**.

**Context scoping (P9-M30-E30.3):**
- Load at session start: this starter; the Milestone spec (full); the Phase spec **by targeted section
  only** — **§P11.4 in full** plus M39's entry in §Milestones and the phase §Acceptance Criteria; PSG
  preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §10, §11, §11.5, §11.6 (incl. §11.6.1), §12, §13C, §15;
  AOG preamble+§1, §1.1, §2, §3.7, §3.9, §3.10, §4, §5, §6, §7, §9, §12, §14, §15, §16.
- Load on trigger: PSG §5B + AOG §3.4 at closure (**§5B, not §5C**); PSG §3, §8A, §13D, §14A, §14C,
  §18; AOG §3.2, §8, §13, §17.
- Do not load: PSG/AOG changelogs; other levels' role/starter sections; §P11.5 (M40 — not yours);
  M36–M38 specs except by targeted section.

---

## Milestone Context

**Milestone number:** P11-M39 · **Name:** Trustworthy Completion Signal (P10-GH-7)
**Milestone spec:** `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M39__milestone-spec.md`
**Governance versions:** PSG **v2.4.0** / AOG **v2.10.0**

| Epic | | |
|---|---|---|
| **E39.1** | Completion judgment that does not rest on the exit code | **FIRST — binding** |
| **E39.2** | Validate against the known cases | after E39.1 |
| **E39.3** | Exercise the `epic_qa` lane and close G11 | shape depends on E39.1 |

**Session objective:** produce a complete Epic spec and Epic Execution Chat Starter for each Epic,
**one set at a time**, E39.1 first, returning each to the Phase Chat for review. Under SN-13
default-accept, the Phase Chat accepts a clean set by silence.

---

## ⚠ Read before planning — four things that decide this milestone

### 1. This is the phase's hard gate, and the temptation is sharper than M38's

**M39 gates M40.** A scheduler and a derived gate queue both depend on knowing whether a run finished,
stalled, or failed confidently wrong. Built over the current signal, either yields **constant false
escalations** or **silent no-ops that read as success.**

**Once a run can be judged complete, dispatching the next one is a short step and will look like
progress.** It is M40's. **M39 returns a verdict with its evidence; it does not schedule, queue,
notify, escalate on its own authority, or act.**

### 2. Both known cases survive as raw transcripts — the binding validation is performable

This was the milestone's largest planning risk and it is resolved:

| Case | Path |
|---|---|
| **E33.2 Run A** (truth: *did not complete*) | `.ai-project/artifacts/agentic-runs/P10-M33-E33.2/transcript-A-qwen2.5-coder-14b.json` |
| **E33.4** (truth: *completed*) | `.ai-project/artifacts/agentic-runs/P10-M33-E33.4/transcript-qwen3-coder-30b.json` |

Both directories carry a `run-record.md`. Schema: `status`, `final_answer`, `transcript`,
`iterations`, `tokens`, `model`, `duration_ms`. **There is no reconstruction excuse available.**

### 3. Measurement already rules out the two cheap mechanisms — including one M38 would have pointed you at

Read at planning time from those transcripts:

| Signal | Run A (*did not complete*) | E33.4 (*completed*) |
|---|---|---|
| exit code | **0** ❌ | **2** ❌ |
| **`status`** | **`completed`** ❌ | **`max_iterations_exceeded`** ❌ |
| `iterations` | **0** ✅ tell | 10 — nothing |
| `final_answer` | unexecuted **tool-call JSON** ✅ tell | prose claiming success — correct here |
| repository state | no commit | commit + green suite ✅ |

**`status` is wrong in both directions too.** Run A reports **`completed`** having done zero work.
**This refines M38's M1 obligation** (*"read structured status, never prose"*) — right for E38.4's
narrow question, **and not sufficient as a completion judgment.** An epic building on `status` alone
**fails the first known case.**

**The only signal correct in both is repository/artifact state delta.** That is **a direction, not a
decision** — E39.1 may build from anything it can defend, and may not use exit code or `status` alone.

### 4. `epic_qa` has no dispatch path, and E39.3's shape depends on E39.1

Measured: `bin/ai-project-orchestrator` uses `epic_qa` **only to select a model for the validation
command**; **Drivr's `ExecutionRequest` has no `role` field** (`task`, `model`, `working_dir`,
`timeout_s`, `max_iterations`, `allowed_tools`, `extra`).

**So "exercise the `epic_qa` lane" requires a path that does not exist.** The resolution is a coupling:
a **QA-role second pass is an admissible component of E39.1's judgment**. If E39.1 chooses it, the path
is built there and E39.3 exercises it. If not, E39.3 justifies building one **or reports G11 still
open with the reason.**

> **Extract E39.1's QA-pass decision before you write E39.3's spec.** Do not discover it at execution.
> This is the M37 shape — an epic whose feasibility depends on a path that may not exist. It cost M37
> an escalation, a ruling and a posture round-trip; the M38 gate made it cost nothing; **here it costs
> a paragraph, if you take it.**

---

## Binding Constraints — reproduce these in the Epic specs

1. **Validation against BOTH known cases is the milestone's hard requirement** — Run A → *did not
   complete*; E33.4 → *completed*. *A design that cannot be shown against both is not delivered.*
2. **Neither the exit code NOR `status` alone.** The second half is added on measured evidence and is
   equally binding.
3. **Nothing in M40 is built** — no scheduler, gate queue, thin surface, approval link, or
   competing-model review.
4. **G11 closes only on a real captured `epic_qa` run**, committed as an artifact. **Never by
   inference, by a relabelled dev-lane run, or by validating historical transcripts.** *Reporting it
   still open with a reason is an acceptable outcome; a false claim is not.*
5. **Row P4 is not decided**, and M38's findings (capacity FAIL; local MISS/paid CATCH on **one** pair;
   C3's ceiling distinction) are **inputs, not conclusions.**
6. **Drivr still rents** — no inference, no model loop, no agent client.
7. **Structural diagram** on any delivery amending a normative document **in this repo**.
8. **P10-GH-10 is named, not scoped — and it bites hardest here.** ~3-in-10 full-suite failures,
   passes in isolation. **M39's evidence is suite-shaped**, so a spurious red is likelier to be
   mistaken for a finding. **Re-run and record BOTH results.**

---

## Suite baselines — state which repo you mean

| Repo | Baseline | Invocation |
|---|---|---|
| `ai-project-system` | **489** | `PYTHONPATH=. pytest -q` (bare `pytest` fails collection) |
| `drivr` | **47** | bare `pytest` from its root |

**M38's artifacts cite 393 for this repo. That is stale** — B2.1 and E38.3 added 96 tests. **Measure on
the branch you are on.**

---

## Method obligations — each was paid for in this phase

1. **`P11-GH-2` — state the layer, the time and the scope of every verification.** Four axes have
   fired: **environment**, **time**, **scope**, and **literal-vs-rendered** (a grep matching example
   text inside a fenced block, or missing a phrase because of inline markdown). **The Phase Chat has
   produced instances of all four**, including twice while reviewing M38.
2. **G2 — the reviewer re-measures; the executor's report is not the evidence.**
3. **G1 — remove derivation steps.** One non-uniform element among many gets **quoted verbatim**.
4. **Cite by artifact + defect, never by ordinal.** The count tally collided at "nine" when two chats
   incremented the same stale base. Any total is **a floor with its date and base.**
5. **Cross-repo claims carry a date or commit anchor**, never present tense.
6. **Every inventory is a floor.**
7. **Check the branch before every commit; verify pushes at `origin`.** `git log -1 <branch>` proves
   nothing. **One worktree per chat** — normative since P5-M20-E20.2, ignored four times in P11.
8. **Commit the Closure Declaration.** M38's was authored and left **untracked** until the Phase Chat
   caught it at consolidation — the *"disk presence is not proof of commit"* hazard landing on the one
   artifact whose job is to be the permanent record.

---

## Spec Existence Requirement

The Milestone spec MUST be **git-tracked on `phase/P11`** — verify with
`git ls-files --error-unmatch docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M39__milestone-spec.md`.
**Branch `milestone/M39` from `phase/P11` only after confirming it is current** (`git log --oneline
milestone/M39..phase/P11`); **P11-GH-1 has fired three times in this phase.**

**Model verification (P9-M31-E31.3 — required, manual instance):** compare your harness-reported model
identity to `.ai-project.yml`'s `models.milestone` (`remote:claude-opus-5`). **If both are present and
disagree, STOP.**

**If the spec is missing, untracked, incomplete or ambiguous:** report to the Phase Chat — **except**
where it explicitly assigns a design decision to an epic (E39.1's mechanism **and its QA-pass
decision**; E39.2's evidence format; E39.3's dispatch path if warranted).

---

## Output Requirements

Produce, **one Epic's set at a time**, E39.1 first:

1. **Epic spec** — `P11-M39-E39.<n>__spec__<epic-name>.md`: goals and scope; applicable binding
   constraints **reproduced, not cited**; deliverables; DoD; dependencies; acceptance criteria.
   **Cross-repo epics must state how evidence will be captured from Drivr and committed here.**
2. **Epic Execution Chat Starter** — from `governance/templates/epic-execution-chat-starter.md`, with a
   **branch check as its first prerequisite**, `Execution Mode: manual` → `models.epic_manual`, the
   E31.3 manual check, and the **working suite invocation per repo**.

Commit both to `milestone/M39`, hand off **reference-first per AOG §3.1.1** — path plus a one-line
summary, never the body. Then request Phase Chat review before the next Epic.

> **Do NOT produce the Milestone spec, the Phase spec, or any M40 artifact. Do not write Drivr's code.**

---

## Completion Requirements

- [ ] Epic spec + Starter produced and accepted for all three Epics
- [ ] E39.1's **QA-pass decision** extracted and consumed by E39.3's spec
- [ ] In-chat acceptance acknowledged for each (SN-19 — no artifact)
- [ ] The Phase Chat has declared the planning session complete

Declare: *"Milestone P11-M39 planning complete. All three Epic specs and Chat Starters accepted.
Session closed."*

On **execution** completion, produce the Closure Declaration with `is_final: false` — **and commit
it.** It must record: the judgment's mechanism and what it reads; **both known-case verdicts** with
any post-hoc tuning disclosed; **the two-case limit**; **G11's unambiguous status**; and **that nothing
from M40 was built.**

---

## Question Policy

- Ask only blocking questions.
- Do not propose new epics or expand scope. A fourth epic is an escalation.
- **CLOSED — do not reopen:** whether the exit code may be used (**no**); whether `status` alone may be
  (**no** — measured); whether row P4 moves (**no**); whether `local-agent-runner` is retired (**no**);
  whether M40 work starts (**no** — M39 gates it); whether G11 may be claimed by inference (**no**).
- **Yours — decide, document, proceed:** E39.1's mechanism and its QA-pass decision; E39.2's evidence
  format and how it demonstrates non-overfitting; E39.3's dispatch path if warranted.
- **Do not scope in:** the scheduler, derived gate queue, thin surface, signed one-time-link approval,
  competing-model review (all **M40**); P10-GH-10; the four §4-invalid enrolled configs; the two open
  `bin/ai-project-init` defects; P9-GH-1/P10-GH-9 (M40); P9-GH-3, P8-GH-2, ComfyUI precision, or the
  sidekick identity question.
- Escalate to the Phase Chat for any gap not covered here.
