---
artifact_type: progress_digest
artifact_version: 1.0
timestamp: 2026-07-31T22:30:00Z
issuer_chat: HQ Chat
target: Creation Chat
project_name: ai-project-system
period_covered: 2026-07-20 to 2026-07-31
supersedes: .ai-project/artifacts/progress-digests/2026-07-20__hq__progress-digest.md
purpose: P11 scoping handoff — P10 is closed; HQ cannot self-scope a phase
---

# Progress Digest — ai-project-system (2026-07-20 to 2026-07-31)

**For the Creation Chat, to open P11 scoping.** P10 is closed. HQ cannot scope a phase — the
Creation Chat sets the spine — so this digest exists to make that session start from the
converged state rather than reconstruct it.

> **Amendment 2026-08-04 (P11-M36-E36.2) — `SN-1` in this digest was renumbered to `SN-29`.**
> Every `SN-1` below (Ruling summary #5, Open Decision #3, Open Decision #5) refers to the
> Layer-8/CFO Steering Note
> (`.ai-project/artifacts/steering-notes/2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md`),
> which was filed claiming an ID already held by the 2026-06-12 Creation Chat note. **HQ Ruling
> 2026-08-01, Decision 3** ruled it misnumbered and ordered the renumber to `SN-29`. The text is
> left as issued rather than rewritten — it was correct at its date, and recording the rename here
> keeps it legible *as* a rename. Nothing this digest reports is changed.

---

## Phase Status

**P10 — Fleet Adoption and Local-Inference Proving: CLOSED 2026-07-31 at `v7.1.0`.**
Merge `bb727a5` on `master`, tag `v7.1.0`, Phase Closure Declaration `4598d4d`. Fifth phase
closed through PSG §5C's canonical 9-step sequence. **12 epics across 3 milestones.** Suite
**366 passed / 0 failed / 0 skipped**, independently re-verified by HQ at closure validation.

| Milestone | Epics | What it actually produced | Merge |
|---|---|---|---|
| M33 — Proving Pair | 4 | The repeatable v7.0.0 bump procedure; **two real Agentic/Local epics** advancing `local-agent-runner` and `home_finance`'s own code, not demos; the Ollama-vs-llama.cpp runtime question settled by the run (keep Ollama, raise the model tier) | `2180aa4` |
| M34 — Fleet Roll-forward | 3 | P6-GH-15 **closed in the wild**; `courtis`, `Getawayinsured2023`, `footboard` at confirmable `framework_version: v7.0.0`; epic lanes routed to `qwen3-coder:30b` | `44c4159` |
| M35 — System-Operator Canonization | 5 | `fleet-operator.md` + `fleet-operator-brief.md`; the handback and one-level-escalation rules; the ratified execution matrix with *mode is not authority*; a blinded local-review back-test | `3914890` |

**Version bump v7.0.0 → v7.1.0 (minor) — ratified by HQ**, not merely unopposed. P10 added
permanent governance surfaces but invented no new execution-model axis and no new participant
class; the execution matrix *restored* the P9-M31-E31.1 baseline, and `fleet-operator.md` wrote
down a role already running by hand. P6's adoption-phase precedent fits; P7's and P9's do not.

**P11: not scoped, not opened.** Recorded direction is **Drivr** (SN-24) — coordination daemon,
gates, thin surface, headless-first. That is direction, not a spine.

---

## HQ Decisions Made in This Period

Five rulings. All are recorded artifacts; this is the summary, not the record.

1. **Paid-frontier model mapping refreshed** (2026-07-28, `6ce2214`) — `claude-opus-4-8` vanished
   from the harness and the E31.3 guardrail correctly halted *every manual chat level at once*,
   including HQ's own opening. Moved five keys to `claude-opus-5`. Ruled that **a tier is never
   deprecated, only a version** — policy rows decide tiers, only the mapping table names a model —
   so M30's evidence stood and was not re-run. Per-level-per-project routing ruled **Drivr's
   domain (P11)**; no relocation built.
2. **SN-24 — M35's operator form** (2026-07-28, `ecd489e`) — accepted, and amended one step
   further than asked: M35 names the operator by **role**, naming *neither* a chat nor a daemon.
   The defect was not that "System Chat" was the wrong implementation; it was that a normative
   record named an implementation at all.
3. **SN-25 — handback and the execution matrix** (2026-07-30, `e5201dd`) — the handback rule
   accepted with its destination corrected to **the immediate parent** (the chain terminates at a
   manual level by construction, SN-22). One-level escalation recorded normatively, explicitly
   **not** closing P9-GH-1. Execution matrix ratified with **mode is not authority** attached.
4. **Row P4 — Milestone × local inference** (2026-07-31, `d7b1de8`) — **row unchanged; Milestone
   remains paid frontier.** A decision, not a deferral. See Open Decisions #2 for what this does
   and does not settle.
5. **SN-1 — System HQ routing and origination** (2026-07-31, this session) — CFO decisions D1–D4
   accepted; codification **placed in P11** as a small documentation amendment. See Open
   Decisions #3.

**A process fact worth carrying:** the same rule was learned twice this phase from opposite
directions — *governance names the tier, routing names the model* (ruling 1) and *governance
names the role, P11 names the thing that runs it* (ruling 2). Both close one class of defect: a
normative document pinned to a value something outside its control is free to change.

---

## Open Decisions — for the Creation Chat

**1. What is P11's spine?** The only thing gating further work. Drivr is the recorded direction
(SN-24: four-project ecosystem, headless-first, gates in-app, the human inside the governance
graph rather than above it), but a direction is not a spine, and SN-24's own carried caution
belongs in the room: **all four projects are infrastructure; none is a platform and none earns
revenue.** The P11 Brief should state the leverage case as a **choice**, not let it read as
though the infrastructure were the goal. — *before any P11 work begins.*

**2. Does P11 carry the block-detection problem, and where?** **P10-GH-7 (High)** is the
prerequisite for everything Drivr's handback surface implies: the completion signal is
untrustworthy in **both** directions (exit 0 with zero work; exit 2 with complete green work),
and **G11** stands at zero captured `epic_qa` runs. M35 recorded the handback *rule*; nothing
detects the block it is a rule about. Building coordination on this signal yields constant false
escalations or silent no-ops. — *at P11 scoping.*

**3. Where does the System HQ codification (SN-1) sit?** Accepted and ready to slot: a small,
self-contained documentation amendment to `system-hq.md` recording D1–D3, Authority Boundary
verbatim-frozen across three documents as a DoD item, reusing `steering_note` for the routed-to-B
leg rather than inventing a type. Independent of Drivr, no dependencies. It needs a milestone
with room, not analysis. — *at P11 scoping.*

**4. Does P9-GH-1 finally get an owner?** Carried unowned since P9. **P10-GH-9 (High,
trigger-gated)** re-rated it: while Phase and Milestone were manual by fixed posture, a human sat
at those gates *by construction* and compensated for the missing merge-authorization guard. The
ratified matrix removed that compensation without touching the guard. **Trigger: before the first
Phase or Milestone agentic dispatch is wired** — which is plausibly early P11 work. — *at P11
scoping.*

**5. Two unenrolled projects, unchanged.** `ai-stack` and `character-factory` — noted, not
addressed, per SN-23. `ai-stack` surfaced again in SN-1 as the unregistered ComfyUI host that
prevented the first true A→B routing instance. Classify or leave. — *low urgency.*

**6. Sidekick-for-external-projects.** Still an identity question (pivot vs. addition),
Project-Brief territory, deliberately undecided in P10 and unchanged. — *Brief-level, not phase
scope.*

---

## What Row P4 Settled, and What It Did Not

Recorded separately because it is the item most likely to be misread as "local inference failed."

**It did not fail.** E35.5 back-tested `qwen3.6:27b` (Q4_K_M) against five known-ground-truth
defects from this repo's own history — pre-registered rubric, blinded packets, ten scored runs,
every run committed including the ones that hurt — and **passed 4 of 5 with zero false alarms**.
The strongest single result: **exit-code untrust generalises to a local reviewer.** It rejected
the exit-0-zero-work run and accepted the exit-2-complete-work run, reasoning from transcript,
diff and suite rather than the status code — the exact two-sided judgment P10-GH-7 records as
measured-broken in automated detection.

**Candidacy was earned. Adoption was not.** The decisive finding is the shape of the miss, not
the miss: two runs of the same prompt at the same settings gave **identical diagnoses and
opposite prescriptions**. At Milestone the remedy *is* the decision. Behind that sit three
untested faculties, now named as gates — measured prescription variance (**G-P4-a**), unassisted
search and absence-detection over a real branch (**G-P4-b**), and tool-using verification of a
claim before ruling on it (**G-P4-c**).

**The corroborating "natural experiment" does not exist.** `Getawayinsured2023` routes
`milestone:` to **`remote:`**`qwen3.6:27b`. E35.5 verified that premise before relying on it and
found it false — which is itself the best argument in Decision 3 of the row P4 ruling, and the
single most valuable correction P10 produced.

---

## Carry-Forwards to P11

Full definitions in the Phase Closure Declaration. Priority order, not ID order:

| ID | Priority | One line |
|---|---|---|
| **P10-GH-7** | **High** | Block detection untrustworthy both directions + G11 unexercised QA lane — prerequisite for any handback mechanism |
| **P10-GH-9** | **High** (trigger-gated) | Agentic parents × default-accept × P9-GH-1; trigger is the first Phase/Milestone agentic dispatch |
| P9-GH-1 | Medium (raised) | Merge-authorization routing guard patched at Epic level only; templates unpatched |
| P10-GH-2 | Medium | Creation Chat's re-instantiation Seed lacks the E31.3 model-verification check **⚠ false premise — re-diagnosed; see the note below this table** |
| P10-GH-5 | Medium | `ai-project-yml-spec.md` §4 validation rules normative but unenforced; drift observed to 3 of 6 enrolled projects |
| P10-GH-10 | Medium | Flaky `test_artifact_router.py` test weakens "full suite green" as evidence (~10% observed) |
| P10-GH-1/3/4/6/8 | Low | Convention-only `framework_version`; row P1 vs live config; unfillable `merge_details`; starter-lint false positives; unversioned `governance/systems/` docs |
| P9-GH-3 | Low | Within-session segmentation; **row P4 does not wait on it** |

> **Amendment 2026-08-04 (P11-M36-E36.5) — P10-GH-2's one-line summary above is false, and the item
> is re-diagnosed.** The original row is left unedited, deliberately; this note corrects it.
>
> `governance/templates/seed.md` has carried the E31.3 **Prerequisite Verification** section since
> commit **`d7ee7cd` (2026-07-19)** — **nine days before** the 2026-07-28 HQ Ruling that filed the
> gap — and `governance/templates/genesis.md` carries it from the same commit. The 2026-07-31
> Creation Chat session, opened from `seed.md`, **ran the check.** The Seed does not lack it.
>
> **The real defect was the re-instantiation *ritual*, not the Seed.**
> `governance/systems/creation-chat-guide.md` handed a re-opened session three artifacts, **none of
> which carried a model check**, because the only one that would (`genesis.md`) is not rendered in
> this project. **That defect is now CLOSED** — E36.3 (merged `d8f4871`) canonized a ritual that
> opens with the Seed and carries the E31.3 check as an explicit **Step 4**.
>
> **A future owner should read the ritual (`governance/systems/creation-chat-guide.md`), not
> `seed.md`.** Sources: **SN-26** (Required action 1); **HQ Ruling 2026-08-01, Decision 8**.

**Parked, each on its own trigger, restated unchanged:** the llama.cpp + Qwen3.6 **Q8_0** trial
(pending Mac-class ~42 GB hardware — the Q4_K_M back-test candidate is a different artifact and
did not touch this trigger); competing-model code review; the ComfyUI precision investigation;
P8-GH-2.

---

## Blocking Concerns

**None.** No open PRs. `master` is at `ae046fc` with the suite green. P10 is closed, tagged, and
its closure record corrected. Nothing in the framework is waiting on HQ.

The one thing waiting is P11 itself, and it is waiting on the Creation Chat.

---

## Next Actions

1. **Creation Chat: open the P11 scoping session** and set the spine (Open Decision #1). Everything
   else in this digest is input to that session, not competing work.
2. **Triage the four scoping-time decisions** (#2–#5) into P11 scope or explicit, recorded defers —
   in particular whether block detection (P10-GH-7) is scoped *before* anything is built on the
   handback rule M35 recorded.
3. **Carry SN-24's P11 opener obligations forward** — the four-project ecosystem, the headless-first
   inversion (*a dashboard is a surface for watching; the more agentic the machine, the less there
   is to watch*), and the CFO's infrastructure-is-not-a-platform caution.
4. **On P11 open, HQ produces the Phase Execution Chat Starter** — a binding planning contract, per
   `hq-chat.md`. HQ does not infer a spine to write it from.

---

## Closing Note

P10 was the phase where the framework stopped governing only its own construction. Six enrolled
projects carry a confirmable stamp; two ran genuine Agentic/Local epics against their own code; a
runtime question was settled by running it rather than arguing it, and a review-quality question
was answered with a blinded back-test rather than an opinion.

The most useful record P10 leaves is not the clean pass. It is the corrections: a decomposition
gap found at its own closure review, a model-availability halt that worked exactly as designed
and stopped two chat levels rather than letting them run wrong, a "natural experiment" a Milestone
Chat checked before relying on and reported did not exist, and — filed today — a closure
declaration that claimed the config contract held still during the phase in which it moved twice.
Each of those was caught by a level doing its own verification instead of accepting the level
below on its word. That habit, more than any document P10 produced, is what should survive into
P11.
