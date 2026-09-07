---

# Milestone Execution Chat Starter — P11-M37

**Milestone:** P11-M37 — Corpus Record Conventions
**Phase:** P11 — Drivr: Coordination over Rented Execution
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M37__milestone-spec.md`
**Execution Mode:** manual — the ratified matrix permits agentic-or-manual here, but this instance is
declared **manual**. M37's two epics are corpus-precision work routed manual/paid, and the chat
planning them runs the same way.

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat** for
Milestone P11-M37.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.4.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.10.0

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.10.0
3. This Milestone Execution Chat Starter
4. Milestone Spec (`P11-M37__milestone-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Milestone** — Stage 1: produce Epic specs and Epic
  Execution Chat Starters, commit them to `milestone/M37`, open a PR; Stage 2: oversee Epic delivery,
  accept clean deliveries **by silence** (a Review Decision is the exception path only, PSG §11.6), and
  merge each accepted Epic to `milestone/M37`.
- You MUST NOT implement project code or modify infrastructure — planning and delivery artifacts only.
  **M37 records conventions and applies them mechanically; it builds no enforcement.** No test, no
  linter, no validator (Hard Constraint, milestone spec).
- You MAY create the `milestone/M37` branch **from `phase/P11`**, commit Epic specs and starters, and
  open a PR — your planning artifacts are your deliverables.
- **Artifact scope (adjacency):** you produce **Epic specs and Epic Execution Chat Starters** only. Not
  the Milestone spec (your parent's job — it exists), not the Phase spec, not any M38/M39/M40 work.
- You do NOT dispatch Epic/Coding Agents directly — starters go to the Phase Chat, which authorizes
  each launch.
- You report to the **Phase Execution Chat (P11)**; communicate downward only. Do NOT reach across to
  sibling milestones (M36 closed; M38–M40 unplanned).
- **Mid-flight amendments:** amend the governing Epic spec, note it in its Amendment History, notify
  the Phase Chat — **do not reach into running sessions.** Escalate up if blocking.
- **Merge authorization is an in-chat act, no ceremonial artifact** (SN-19 / PSG §1A under §11.6). The
  harness still enforces explicit human authorization before any merge.
- **PSG §11.6.1 is in force.** For any HQ-authored delivery the CFO is the mandatory **diff** reviewer
  and default-accept does not apply. Silence accepts *your children's* clean deliveries, never HQ's.
- **M37 is NOT P11's final milestone** (`is_final: false`). Your Closure Declaration hands back to the
  Phase Chat, which proceeds to **M38 planning** — not to phase closure.

**Context scoping (P9-M30-E30.3):**
- Load at session start: this starter; the Milestone spec (full); the Phase spec **by targeted section
  only** — §P11.2 and M37's entry in §Milestones, plus the phase §Acceptance Criteria; PSG
  preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §10, §11, §11.5, §11.6 (incl. §11.6.1), §12, §13C, §15;
  AOG preamble+§1, §1.1, §2, §3.7, §3.9, §3.10, §4, §5, §6, §7, §9, §12, §14, §15, §16.
- Load on trigger: PSG §5B + AOG §3.4 at closure (**§5B, not §5C** — M37 is not final); PSG §3, §8A,
  §13D, §14A, §14C, §18; AOG §3.2, §8, §13, §17 (**the diagram obligation fires for both epics**).
- Do not load: PSG/AOG changelogs; other levels' role or starter-format sections; the phase spec's
  §P11.3/§P11.4/§P11.5 (M38–M40 — not yours); M36's specs except by targeted section.

---

## Milestone Context

**Milestone number:** P11-M37
**Milestone name:** Corpus Record Conventions
**Milestone spec path:** `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M37__milestone-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.4.0
- AI-OPERATING-GUIDELINES.md: v2.10.0

**Epics within this Milestone — contents are FIXED at these two:**
- **E37.1** — System-tier versioning convention (P10-GH-8) *(HQ Ruling 2026-08-04)*
- **E37.2** — Artifact-ID citation forms (`GH-`, escalation notices) *(HQ Ruling 2026-08-05)*

**Session objective:** produce a complete Epic spec and an Epic Execution Chat Starter for each Epic
above (one Epic's set at a time), returning each set to the Phase Chat for review. Under SN-13
default-accept, the Phase Chat accepts a clean set by silence.

---

## ⚠ Read this before anything else — M37 is a NEW milestone and the numbers moved

**P11 was restructured from four milestones to five on 2026-08-05, CFO-directed** (phase spec
**v1.1.0**, `bfe2eca`). **M37 is the inserted milestone.** Everything that was M37 shifted one slot:
old M37 (Drivr) → **M38**, old M38 (completion signal) → **M39**, old M39 (coordination) → **M40**.

**Your two governing rulings predate the restructure and cite the OLD epic IDs.** They are correct at
their dates and are **deliberately not rewritten** (HQ Ruling 2026-08-01 Decision 4 — *a bookkeeping
defect never rewrites a citation* — plus the SN-15 precedent). **Read them through this table:**

| The ruling says | You are planning |
|---|---|
| `M37/E37.6` (2026-08-04, versioning convention) | **E37.1** |
| `M37/E37.7` or `M38/E38.7` (2026-08-05, citation forms) | **E37.2** |

**Do not "fix" the rulings' epic IDs.** They are historical citations and the v1.1.0 changelog carries
the mapping.

**One instruction in the 2026-08-05 ruling is spent — do not act on it.** It upgraded the Phase Chat's
permission to **split M37** from *permitted* to *recommended*. That applied to **old** M37 at seven
epics, which is the condition the restructure resolved by creating this milestone. **This M37 has two
epics and fixed contents; there is nothing to split.** The split permission now belongs to M38.

---

## What makes M37 what it is — read before planning

- **You are executing two rulings, not deciding anything.** The versioning convention is decided; the
  four citation-form questions are answered. Your job is decomposition and precision, not analysis.
- **Entirely in-repo, zero Drivr dependency.** Nothing in M38–M40 depends on either epic. Placement
  here is a judgment about record integrity, not dependency — the same judgment that put M36 first.
- **The contents fence is the load-bearing rule of this milestone.** M37 exists *because* old M37
  became *"the milestone things get put in"* — seven epics, four of them carry-forward hygiene routed
  there one ruling at a time. HQ named that pattern and constrained itself; the CFO fixed it
  structurally. **M37 is not a home for `P10-GH-4`, `P10-GH-6`, `P10-GH-10` or anything else. Adding
  requires a ruling, not a passing judgment.**
- **The specific way this milestone could grow a third epic is a test.** E37.1 gives seventeen
  documents a uniform shape, which makes *"assert every `governance/systems/` document has a `version`
  and a `## Changelog`"* a three-line test that would pass on delivery. **Do not write it, and do not
  let an epic write it.** If an epic judges the guard valuable it **records the recommendation and
  escalates**. B3.1's carve-out exists for that class and this milestone is not it. E36.4 held this
  exact line under real pressure when handed a verification command and declining to promote it into a
  committed test.
- **E37.2's cheapness is the hazard, and it is already ruled on.** The `PSG:605` fix is two characters.
  E36.5 was capable of making it, named the cheapness as the reason not to, and declined — and HQ
  explicitly refused to undercut that judgment by acting informally. **The same reasoning binds E37.2:
  it is not a licence to make other "obviously right" small fixes it happens to notice.**

---

## Binding Constraints — reproduce these in the Epic specs

All nine are in the Milestone spec under "Binding Constraints". Summarised so no Epic spec is written
without them in view:

1. **No backdated reconstruction — permanently out of scope, not deferred.** E37.1 seeds
   forward-looking only.
2. **The seven already-compliant documents are left untouched.**
3. **`chat-hierarchy.md`'s seeding row comes from the 2026-08-05 erratum, NOT from HQ Ruling
   2026-08-04 Decision 5.** See the callout below — this is the milestone's single most skippable-looking
   and least skippable dependency.
4. **Nothing is renumbered.** `P6-GH-10…15` / `P7-GH-16…21` are ratified historical exceptions.
5. **The `GH-` prefix names the phase that FILED an item, permanently.** *The record names the
   disposition; the identifier names the origin.* `P10-GH-8` is the worked proof.
6. **E37.2's four rules are recorded ONCE**, alongside E36.1's "Steering Note ID Allocation" section in
   `creation-chat-guide.md` — not duplicated per directory.
7. **The `rulings/` date-only ambiguity is report-and-leave and NOT in scope.**
8. **Both epics carry a Structural diagram** (Mermaid, fenced, in-repo, no ComfyUI). E37.1's diff spans
   ten documents — this is where a reviewer most needs the map.
9. **Neither epic reopens M36.**

### Constraint 3 in full — the erratum, not the ruling

**HQ Ruling 2026-08-04 Decision 5 states the forward-looking count is *"two, not three"*, naming both
amendments as `creation-chat-guide.md`. That count is wrong, and HQ has footnoted it** (Ruling
2026-08-05, Part 1).

The verified count is **three amendments across two unversioned documents**:

| # | Epic | Document |
|---|---|---|
| 1 | E36.1 | `creation-chat-guide.md` — new "Steering Note ID Allocation" section |
| 2 | E36.1 | **`chat-hierarchy.md`** — ±3, two SN-23 citations date-qualified in normative text |
| 3 | E36.3 | `creation-chat-guide.md` — Re-instantiation Ritual reconciliation |

**An E37.1 seeding row for `chat-hierarchy.md` written from Decision 5 would record that document as
unamended by M36.** Source the row from the erratum and from M36's Closure Declaration §D5, which
records all three as Amendments 1–3 of 3.

**Why this happened, worth knowing so it is not repeated:** the Phase Chat's 2026-08-04 routing carried
two corrections, one raising the count and one lowering it. HQ verified and applied the one that
lowered it and dropped the one that raised it — asymmetric verification, in a ruling whose subject is
record integrity. **The lesson generalizes and applies to you: a count in a ruling is a floor too.**

---

## Verified at planning time — treat every inventory as a FLOOR

The Phase Chat re-measured on `phase/P11` rather than citing the rulings. **Two figures in the record
are wrong**; both are corrected here so your epics do not inherit them.

| Fact | Verified |
|---|---|
| `governance/systems/` documents | **17** |
| Compliant (`version` + `## Changelog`) | **7** |
| **E37.1's ten targets** | `chat-hierarchy.md`, `creation-chat-guide.md`, `epic-execution-chat-starter.md`, `governance-propagation.md`, `hq-chat.md`, `hq-execution-chat-starter.md`, `milestone-execution-chat-starter.md`, `phase-execution-chat-starter.md`, `PROJECT-TRACKER-INTEGRATION-SYSTEM.md`, `start-a-project.md` |
| Bare `GH-<n>` under `governance/` | **exactly one** — `PROJECT-SYSTEM-GUIDELINES.md:605` |
| E36.1's allocation section | `creation-chat-guide.md:161` (subsections 166 / 187 / 209) |
| Suite on `phase/P11` | **377 passed / 0 failed / 0 skipped / 0 xfailed** |

**Correction 1 — the `GH-` live-ID count is 39, not the ruling's 38, and a naive sweep returns 41.**
`P11-GH-1` was filed after the ruling (+1 live). `P6-GH-1` and `P6-GH-2` appear **only as pre-renumber
historical references** — SN-15 moved them to `P6-GH-12`/`P6-GH-13` — so they are strings, not live IDs
(−2). **E37.2 must distinguish live IDs from historical pre-renumber references**, or it will report 41
and overcount or report 38 and miss `P11-GH-1`.

**Correction 2 — the escalation-notice shorthand has three occurrences, and one path is misstated.**
The ruling names two; verified there are three: `governance/systems/chat-hierarchy.md:271`,
`governance/ai-project-yml-spec.md:660`, **and `governance/ai-project-yml-spec.md:6`** (lower-case,
in the §Introduced In line). Also **`ai-project-yml-spec.md` lives at `governance/`, not
`governance/systems/`** — so it is *not* one of E37.1's seventeen documents. **Do not assume the two
epics' file sets overlap there. E37.2 performs its own exhaustive sweep.**

**Also carry to both epics — P10-GH-10, measured:**
`tests/test_artifact_router.py::test_daemon_extensions_error_branches` fails **~3 in 10 full-suite
runs** (M36 Finding 2, upgraded from a recorded ~10%), passes 5/5 in isolation, and is untouched by
anything in M37. **A red suite on that test alone is not evidence of a defect in your epic** — re-run,
and record both results rather than only the green one.

---

## Spec Existence Requirement

The Milestone spec MUST be **git-tracked on `phase/P11`** at the path above before this session
begins. Verify with
`git ls-files --error-unmatch docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M37__milestone-spec.md`
on `phase/P11`. Disk presence is not proof of commit.

**`milestone/M37` branches from `phase/P11` at or after `c9edd25`** (the master→phase sync). Branching
from an earlier point gives you a phase spec that does not know this milestone exists.

**If the Milestone spec is missing or untracked:** STOP and report to the Phase Chat.

**If it is incomplete or ambiguous:** report upward — **except** where it explicitly assigns a design
decision to you (E37.1's starting-version scheme; E37.2's placement of the four rules within the one
section that holds them). Those are yours: pick a direction, document the reasoning, proceed.

**Model verification (P9-M31-E31.3 — required, this instance is manual):** read your own
harness-reported model identity and compare it to `.ai-project.yml`'s `models.milestone`
(`remote:claude-opus-5`). See `governance/systems/chat-hierarchy.md` "Manual Chat Model Verification".
**If both are present and disagree, STOP** — state the mismatch and wait for the Phase Chat/human.

**Check your branch before every commit.** This repository is worked by multiple sessions and gets left
on whatever branch the last one used; M36's Finding 4 records a false "content is missing" alarm from
exactly this. Every M36 Epic Starter carried a branch check as its first prerequisite — continue that.

---

## ⚠ P11-GH-1 — this document cannot update itself once you branch

**P11-GH-1** (`05038ac`, HQ, 2026-08-04) records that PSG §13D's downward channel is broken: *"that
same source is not the same file across branches."* A parent amends on its branch; children carry
copies frozen at branch time. It has already fired twice in this phase — M36's Milestone Chat could not
see Decision 5, and `phase/P11` could not see spec v1.0.2.

**Interim practice, binding on you until P11-GH-1 is resolved:**

1. **Before planning, and again before each epic's execution, check whether `phase/P11` has moved** —
   `git log --oneline milestone/M37..phase/P11`. Do not assume this starter or the spec is current.
2. **The Phase Chat will notify you in-chat of any amendment** and will not rely on the spec channel
   alone. **An in-chat amendment notice is authoritative over this file's frozen copy.**
3. **If this starter or the spec is contradicted by a merged ruling on `phase/P11`, the ruling wins** —
   report the contradiction upward rather than reconciling it silently.

---

## Execution Posture for M37's Epics — SPLIT (binding, CFO decision 2026-08-05)

**The two epics run under different postures. This is deliberate and is not a drafting inconsistency.**

| Epic | `Execution Mode` | Model key | Resolves to |
|---|---|---|---|
| **E37.1** | **`agentic`** | **`models.epic_dev`** | **`local:qwen3-coder:30b`** |
| **E37.2** | `manual` | `models.epic_manual` | `remote:claude-opus-5` |

The milestone spec's v1.0.0 put both on manual/paid as the Phase Chat's own call while explicitly
leaving the E37.1 override open. **The CFO took that option** (spec v1.1.0, §Amendment History).

**Why the split, so you can defend it:** E37.1 is repetitive, mechanically verifiable, and carries a
**cheap ground truth** — afterwards either all seventeen documents comply or they do not, checkable in
one command. E37.2 is two characters in the framework's highest-authority document plus four normative
rules whose whole value is precision, with no upside to risking it. **Running one local and one paid in
one milestone is a controlled comparison** rather than one ambiguous result, and that evidence is wanted
by M38 and M39.

### Two guardrails you must implement — they are the reason the switch is safe

**G1 — put the `chat-hierarchy.md` changelog row into E37.1's Epic spec as a VERBATIM literal string.**
Not instructions for deriving it from the erratum — the actual text, to be copied. **You author that
string**, from the 2026-08-05 erratum and M36's Closure Declaration §D5. This is E37.1's only
non-uniform row among ten and therefore its only judgment call; G1 turns it into transcription. *"One
exception among ten uniform items"* is exactly the shape a weaker model flattens, and a flattening lands
in ten governance documents at once.

**G2 — judge E37.1's completion yourself, mechanically. Never from the exit code.** P10-GH-7 stands:
the exit code is untrustworthy in **both** directions on this stack (E33.2 Run A returned exit 0 having
done zero work; E33.4 returned exit 2 having produced complete, green work). Acceptance rests on **your
own re-measurement** — 17 of 17 compliant, the seven shown untouched, no reconstructed history. **Record
the exit code; do not rely on it.** A green exit is not evidence and a red exit is not a verdict.

### What does NOT change because E37.1 is agentic

- **Mode is not authority.** Stage-2 acceptance and merge authorization stay human-keyed. An agentic
  Epic holds exactly the authority the Epic level always held.
- **Your Stage-2 review does not get lighter.** Same depth, and your own instance stays manual/paid.
- **All nine binding constraints and the Hard Constraint apply identically.** Agentic mode is not a
  licence to build enforcement, reconstruct history, or renumber anything.
- **G11 is NOT closed by this, and must not be claimed.** `epic_qa` has **no dispatch mechanism** —
  `bin/ai-project-orchestrator` says so in its own comments — so an agentic E37.1 exercises the **dev
  lane only**. Closing G11 remains M39's.

### Dispatch mechanics — verified on this host 2026-08-05, no config change needed

`.ai-project.yml` already carries `epic_dev: local:qwen3-coder:30b`. Verified present: the ollama
endpoint at `http://localhost:11434` is reachable, `qwen3-coder:30b` is pulled, and
`ai-project-sandbox:latest` exists.

- **E37.1 must be DISPATCHED, not opened.** `bin/ai-project-orchestrator` resolves `epic_dev`, exports
  `AI_PROJECT_ACTIVE_MODEL`, and runs inside the sandbox; `bin/run-dev-agent` maps `local:<tag>` to the
  bare ollama tag and refuses loudly with **exit class 5** if the model is genuinely unavailable
  (P9-M31-E31.2 — *"local loadability is never assumed"*). **Pasting an agentic starter into a chat
  window is a manual run wearing an agentic label.** The declaration and the dispatch must agree.
- **Do NOT put the E31.3 manual model check in E37.1's starter.** Agentic instances verify against
  `epic_dev`/`epic_qa` through E31.2's dispatch-time guard instead — the Epic Starter template already
  encodes this distinction. E37.2's starter **does** carry the manual check, against `epic_manual`.
- **You do not dispatch directly.** E37.1's starter goes to the Phase Chat, which authorizes the launch,
  exactly as for a manual epic.

> **A failed or partial agentic run on E37.1 is a usable result, not a delivery failure.** The epic's
> substance can be completed manually and the local-lane finding still stands as the evidence this
> posture was chosen to gather. **Record what happened either way** — what the run produced, what your
> re-measurement found, and where the two disagreed. An experiment whose only acceptable outcome is
> success is not gathering evidence.

---

## Output Requirements

Produce, **one Epic's set at a time**:

1. **Epic spec** — `P11-M37-E37.<n>__spec__<epic-name>.md` covering: goals and scope; the binding
   constraints that apply, **reproduced rather than cited**; deliverables; Definition of Done —
   including the Structural diagram obligation and the Hard Constraint's no-enforcement rule;
   dependencies and prerequisites; acceptance criteria. **For E37.1, the spec must additionally carry
   the `chat-hierarchy.md` changelog row as a verbatim literal string (G1).**
2. **Epic Execution Chat Starter** — using `governance/templates/epic-execution-chat-starter.md`, with a
   branch check as its first prerequisite and **the posture from the split table above**:
   - **E37.1** — `Execution Mode: agentic`, routing to `models.epic_dev`. **No E31.3 manual model
     check** (agentic instances use E31.2's dispatch-time guard). State that it is **dispatched through
     `bin/ai-project-orchestrator`**, not opened as a chat.
   - **E37.2** — `Execution Mode: manual`, routing to `models.epic_manual`, **with** the E31.3 manual
     model check.

Commit both to `milestone/M37`, then hand off **reference-first per AOG §3.1.1** — committed path plus a
one-line summary, never the body echoed into chat. Four-backtick fenced full-body form only for a
genuinely repo-less consumer, and say the fallback is in use.

After each set, explicitly request Phase Chat review before proceeding.

> **Do NOT produce the Milestone spec** (it exists), **the Phase spec**, or any M38/M39/M40 artifact.

---

## Epic Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

Per SN-19 and PSG §1A gate scoping / §11.6 there is **no Epic Delivery Authorization artifact or
ceremonial block**. When the Phase Chat accepts an Epic's deliverables (by silence on the happy path),
acknowledge in-chat and proceed. Standing merge instruction: **merge `epic/P11-M37-E37.<n>` to
`milestone/M37` upon Epic completion, Phase Chat acceptance, and explicit human merge authorization** —
an in-chat act, enforced by the harness regardless.

Do NOT proceed to execution or merge without Phase Chat acceptance.

---

## Execution Instructions

- Treat the Milestone spec as the single source of truth for this Milestone.
- Produce Epic deliverables one Epic at a time; await acceptance before proceeding.
- **Coordinate the one file-contention point deliberately.** Both epics touch
  `governance/systems/creation-chat-guide.md` — E37.1 adds front matter and a `## Changelog`; E37.2 adds
  rules alongside §Steering Note ID Allocation (line 161). Regions differ, but **whichever epic lands
  second owns reconciling the changelog**: if E37.2 lands second it adds its own row to the section
  E37.1 created; if it lands first, E37.1's seeding row must record E37.2's change. **Decide the order
  and say so in both Epic specs** rather than discovering it at merge.
- **Verify, do not inherit.** This phase has now had three binding claims propagate unverified into
  specs — the phase spec's Ollama context note (corrected v1.0.1), the P11 starter's constraint 2a
  mechanism, and Decision 5's amendment count. **Every line number, path, ID and count in the Milestone
  spec is a verified-at-planning-time fact, not a guarantee.** Re-check at execution time and report
  differences rather than silently adapting.
- Ask questions only if blocked — resolve ambiguities against the Milestone spec first.
- Do not expand scope beyond the two Epics. **The fence is the point of this milestone.**
- Do not infer missing information; escalate to the Phase Chat.

---

## Completion Requirements

This Milestone Chat session is complete when:

- [ ] An Epic spec has been produced and accepted for both Epics
- [ ] An Epic Execution Chat Starter has been produced and accepted for both, **each carrying its own
      posture per the split table** — E37.1 `agentic` / `models.epic_dev`, E37.2 `manual` /
      `models.epic_manual`
- [ ] **G1 is discharged** — E37.1's Epic spec carries the `chat-hierarchy.md` row as a verbatim literal
- [ ] In-chat acceptance has been acknowledged for both (SN-19 — no artifact)
- [ ] The Phase Chat has declared the Milestone planning session complete

Upon completion, declare: "Milestone P11-M37 planning complete. Both Epic specs and Chat Starters
accepted. Session closed."

On **M37 execution** completion (both epics merged to `milestone/M37`), produce the Milestone Closure
Declaration with `is_final: false` — it hands back to the Phase Chat for **M38 planning**, not phase
closure. **If either epic recommended an enforcement guard, the Closure Declaration records the
recommendation and its escalation** — it does not record a built one.

**The Closure Declaration must additionally record the local-lane result** (E37.1's split posture):
what the agentic run produced, the exit code it returned, what your own re-measurement found, and
**where the two disagreed if they did** — that disagreement is the most valuable single datum this
milestone can produce, and it feeds M39's completion-signal work directly. **State explicitly that G11
is not closed** and that only the dev lane ran.

---

## Question Policy

- Ask only blocking questions.
- Do not propose new epics or expand Milestone scope. **Contents are fixed at two items by CFO
  direction; adding requires a ruling.**
- Do not ask for information already in the Milestone spec.
- **CLOSED — do not reopen, re-park or re-inherit:** whether history is reconstructed (**no,
  permanently**); whether anything is renumbered (**no** — ratified historical exceptions); what the
  `GH-` prefix means (**the phase that filed it, permanently**); the `rulings/` date-only ambiguity
  (**report-and-leave, affirmed**); whether this is a B-series bugfix (**no** — it edits governance
  documents, a boundary HQ held three times); whether M36 reopens (**no**); whether M37 splits (**no** —
  that recommendation was spent by the restructure).
- **Design decisions that are yours — pick a direction, document the reasoning, proceed:** E37.1's
  starting-version scheme for the ten seeded documents; E37.2's exact placement of the four rules within
  the one section that holds them; the landing order of the two epics given the `creation-chat-guide.md`
  contention.
- **Do not scope in:** any Drivr work; the adapter surface, fleet registry, completion signal or
  scheduler (M38–M40); **any enforcement test, linter or validator**; `P10-GH-4`, `P10-GH-6`,
  `P10-GH-10`, `P10-GH-5`, `P10-GH-1` (the last two stay with the registry in M38), `P9-GH-1`,
  `P9-GH-3`, `P10-GH-3`, `P10-GH-7`, `P10-GH-9`, `P8-GH-2`, ComfyUI precision, or the sidekick identity
  question.
- Escalate to the Phase Chat for any gap not covered here.
