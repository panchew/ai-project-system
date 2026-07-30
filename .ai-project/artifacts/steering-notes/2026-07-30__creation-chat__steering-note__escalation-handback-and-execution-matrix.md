---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-30T17:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-25
    severity: high
    title: Autonomy must be able to hand back. An autonomous instance that becomes blocked has no way to summon a human — the chat-to-runner direction works, the runner-to-chat direction does not exist. Plus a CFO precision retiring SN-23 Ratified Decision 2's fixed posture on the Execution Mode axis, and an evidence-collection mandate on Milestone x local inference. Lands before M35 opens.
decisions:
  - "The handback rule, stated as a rule and not as an implementation: an autonomous execution instance that becomes BLOCKED — encountering something requiring human judgment it cannot supply — must be able to surface that block to a human, with enough context for the human to intervene, and the intervention is authority-bearing. Autonomy that cannot hand back is not autonomy; it is an unattended process that fails silently. The CFO's framing: it 'can run freely until something blocks it and that makes the mode switch trigger, and I get my chat opened ready for me to intervene.'"
  - "The handback travels as an ESCALATION NOTICE. The artifact type already exists (.ai-project/artifacts/escalation-notices/) and was exercised by hand during M34. No new artifact type and no new authority model is required; what is missing is that an autonomous instance cannot emit one."
  - "ESCALATION TRAVELS EXACTLY ONE LEVEL. An escalation notice goes to the issuing instance's IMMEDIATE PARENT and nowhere else. That parent then decides the direction of the next step: either resolve it and return a solution to the child, or issue ITS OWN escalation notice one level further up. No instance names a target above its parent, and no level is skipped. (CFO, 2026-07-30, restoring the framework's existing design after considering and rejecting instance-judged routing — see the rationale below.)"
  - "CREATION CHAT IS ALWAYS AWARE of all escalation notices, wherever they arise in the chain. This is VISIBILITY, never authority — the Creation Chat holds no governance authority (Seed Rule 3) and being aware of an escalation must never make it a decision point or a resolution path. Awareness is a read, not a seat."
  - "DRIVR VISUALLY REFLECTS escalation state and the chain — which instances are blocked, on what, and where in the hierarchy the escalation currently sits. P11 work; recorded here so the requirement is not re-derived."
  - "EXECUTION MATRIX — CFO precision, 2026-07-30. Execution Mode (agentic vs manual): Phase, Milestone and Epic may run either; Creation and HQ remain manual-only, permanently (SN-22). Inference locality (local vs remote): Epic may run local or remote (in force via E34.3); Phase remains remote; Creation and HQ remain remote; MILESTONE IS UNDER EVALUATION — see below."
  - "MILESTONE x LOCAL INFERENCE IS NOT RULED OUT — COLLECT DATA (CFO, 2026-07-30). The cell is neither opened by assertion nor closed. model-routing-policy.md row P4 decides paid frontier on measured grounds (largest spend share at 37%; the level where Stage-2 accept authority lives) and its revisit trigger has not fired. The CFO's direction is to gather evidence rather than decide in the abstract — consistent with run-first ordering (SN-23 #4). The cell opens or closes on that evidence."
  - "THE DATA THAT MATTERS AT MILESTONE IS REVIEW QUALITY, not throughput or cost. Row P4's stated reason for paid frontier is that Milestone is where Stage-2 accept authority lives and where errors propagate into merges. Evidence that a local model is fast or cheap at Milestone answers the wrong question; the question is whether its Stage-2 review catches what a frontier model's review catches."
  - "Technical possibility is not sufficient reason. The CFO states plainly that although any level could technically execute from local inference, 'it's not always the way to go'. The matrix is a deliberate, bounded position, not a removal of limits."
  - "Per-level GATES remain a requirement and are explicitly subject to ongoing fine-tuning. Which levels carry which gates stays an open, revisitable configuration — 'we will always keep an eye on this'. This preserves the standing principle recorded in SN-24: the system runs automatically; the human holds the keys to the gates."
  - "SN-23 Ratified Decision #2 (Manual/Paid from Creation through Milestone; Agentic/Local at the Epic) is SUPERSEDED ON THE EXECUTION MODE AXIS ONLY. Its locality half stands, with Milestone under evaluation per above. SN-23 recorded the other matrix cells as 'technically possible and revisitable later, not built now'; that clause is called for mode, and called for evidence-gathering on Milestone locality. The supersession is explicit so the change is a decision and not drift."
  - "Following the 2026-07-28 HQ Ruling on SN-24: this note names ROLES, RULES and TIERS — never implementations. What is normative is that a blocked autonomous instance hands back and that escalation travels one level; what fills those roles is P11's business."
  - "Domain split, consistent with the four-project ecosystem: executing larger units and being invocable from a manual chat is EXECUTION (Local Agent Runner). Deciding when to run, detecting the block, switching mode and surfacing the chat is COORDINATION (Drivr, P11). The rule that autonomy must hand back, that escalation travels one level, and that the human's intervention is authority-bearing, is GOVERNANCE (this repo)."
  - "Do NOT build the detector or the switch in P10. M35 records the rules; P11 builds the mechanisms. This is the same discipline SN-24 and both 2026-07-28 rulings applied."
references:
  - "HQ Ruling 2026-07-28 on SN-24 — governance names the ROLE; P11 names the thing that runs it. This note is written to that discipline."
  - "HQ Ruling 2026-07-28 on paid-frontier model mapping — governance names the tier; routing names the model."
  - "governance/systems/chat-hierarchy.md 'Execution Mode' (P9-M31-E31.1) — the declaration mechanism this precision restores to its full scope."
  - "model-routing-policy.md row P4 — the evidence-derived decision the Milestone locality evaluation must engage with."
  - "P9-GH-1 — the merge-authorization hole at Milestone->Phase and Phase->HQ; the authority class the one-level escalation rule protects."
---

# Creation Chat Steering Note — Autonomy Must Be Able to Hand Back

## Purpose

Direction-setting session held in the Creation Chat on 2026-07-30, CFO present, immediately
after M34 closed. The CFO's account of where it came from: working the M34 epics while
running a second project (`social-stories-creator`) in parallel and getting progressively
more familiar with agentic-AI practice.

**M35 has not opened.** No M35 artifacts exist in the phase directory. This note lands
before it, deliberately — as SN-24 did, and for the same reason.

---

## Concern for HQ Triage

### SN-25 — Autonomy must be able to hand back [HIGH]

Severity confirmed by the CFO (2026-07-30); the decisions are the CFO's.

**Detail.** The framework can dispatch work to run unattended. It has no way for that work
to call for help. An autonomous instance that hits something requiring human judgment has
exactly two exits — finish wrongly, or stop silently — and the M33 evidence shows a reader
cannot reliably tell which happened.

M35 is the milestone that records what the fleet operator is and what it may do. **An
operator that cannot hand back is under-specified.** The rule belongs in M35's normative
record, before M35 is written.

---

## What already exists — the ask is smaller than it looks

**The chat → runner direction works today.** E33.4's run record: the Epic Chat dispatched
`bin/run-dev-agent` directly on the host against the `home_finance` checkout, and E33.2 took
the same path. A manual, paid chat delegating a bounded unit to local inference is not a new
capability — it is how both proving-pair runs actually happened.

**What does not exist is the reverse: runner → chat.** That asymmetry is the whole of this
concern.

**Execution Mode at Phase and Milestone is already normative.** `chat-hierarchy.md`
(P9-M31-E31.1) already states that Execution Mode applies to *"Phase, Milestone, and Epic
instances only,"* and records the gap in its own words: *"no dispatch mechanism yet consumes
a Phase/Milestone agentic declaration; wiring the orchestrator to those levels is future
implementation work, not a defect in this declaration mechanism."* P9 opened that door;
SN-23's posture narrowed it for P10. **The ask is dispatch, not permission.**

---

## The execution matrix (CFO precision, 2026-07-30)

| Level | Execution Mode | Inference locality | Change? |
|---|---|---|---|
| Creation | Manual only (permanent, SN-22) | Remote | unchanged |
| HQ | Manual only (permanent, SN-22) | Remote | unchanged |
| Phase | **Agentic or manual** | Remote | mode restored to E31.1 baseline; **dispatch unimplemented** |
| Milestone | **Agentic or manual** | **Remote — local under evaluation** | mode restored; **locality open as an evidence question** |
| Epic | Agentic or manual | Local or remote | already in force (E34.3) |

---

## Escalation travels exactly one level

**The rule.** An escalation notice goes to the issuing instance's **immediate parent** and
nowhere else. The parent then decides the direction of the next step: **resolve it and
return a solution to the child**, or **issue its own escalation notice** one level further
up. No instance names a target above its parent; no level is skipped.

**This is the framework's existing design, restored.** The CFO considered allowing the
issuing instance to judge the reach of its own escalation — an Epic Chat deciding that a
given blocker belongs to HQ rather than to its Milestone — and rejected it in session, on
the ground that it breaks the design that was already right.

**Why it holds.** Instance-judged routing would let **a child choose its own judge**: an
Epic routing directly to HQ steps around the Milestone Chat's Stage-2 authority, and the
parent may never learn its own epic is blocked. That is the same authority class as
**P9-GH-1**, the merge-authorization hole still open at Milestone→Phase and Phase→HQ. The
one-level rule keeps the chain of oversight unbroken by construction rather than by
discipline.

**It also already works.** M34's escalation is the worked example: the Milestone Chat could
not open, the **Phase Chat** — its parent — diagnosed it and issued **its own** notice to
HQ, and HQ ruled. Two hops, each level exercising its own judgment, no level bypassed. The
reach was reached without anyone having to guess at it from below.

**What the child still does** is describe the blocker fully — nature, what was attempted,
what it could not resolve. That is the *content* of the notice, and it is what lets the
parent route correctly. Judgment about the problem stays with the instance closest to it;
judgment about where it goes stays with the level that holds authority over it.

**Creation Chat awareness.** The Creation Chat is aware of all escalation notices wherever
they arise. This is nearly free today — escalation notices are committed artifacts a
re-instantiated Creation Chat can simply read — and it is a *retrieval* property, not a
subscription. It must stay that way: if awareness ever becomes "the Creation Chat resolves
escalations," Seed Rule 3 is broken and the framework has recreated, one level down, the
thing it exists to prevent.

---

## Milestone × local inference — collect data, decide on evidence

**Not ruled out, not opened.** The CFO's direction is to **gather evidence** rather than
settle it by assertion in either direction — the same instinct that made M33 produce a
runtime decision from a run instead of a memo (SN-23 #4, run-first ordering).

**What the evaluation must not do is measure the wrong thing.** Row P4's stated reason for
paid frontier is not cost alone — it is that **Milestone is where Stage-2 accept authority
lives** and where errors propagate into merges. Evidence that a local model is fast or cheap
at Milestone answers a question nobody is asking. **The question is whether a local model's
Stage-2 review catches what a frontier model's review catches** — whether it would have
caught M33's decomposition gap, or E33.2's false-positive completion, or the footboard
dirty-entry miscount M34 had to correct.

**A cheap data path exists that needs no new capability.** Milestone × local does **not**
require agentic dispatch — a **manual** Milestone Chat can run on a local model today. That
is the Manual/Local cell SN-23 set aside as "technically possible... off the critical path."
Notably, `Getawayinsured2023` already carries exactly that configuration in its own
`.ai-project.yml` (`phase` and `milestone` pointed at `qwen3.6:27b`, which is present on the
host at Q4_K_M). The fleet is already positioned to produce this evidence; whether to
harvest it, and under what protocol, is HQ's call.

**Row P4's own revisit trigger** (within-session task segmentation landing) remains unfired,
because **P9-GH-3 is still carried forward and unowned.** Whether the evaluation supplies an
independent basis to amend P4, or whether P4 waits on its recorded trigger, should be stated
rather than assumed.

---

## The dependency this whole idea rests on

**You cannot escalate on a block you cannot detect**, and block detection is measured broken:

- **E33.2 Run A — exit 0, zero work.** False positive; the validation command would also
  have passed on the unchanged repo.
- **E33.4 — exit 2, complete and green work.** False negative.

Two-sided and corroborated across two projects: **on this stack the exit code is not a
completion signal.** A handback built over an unreliable block signal yields either constant
false escalations — the human becomes the bottleneck again, worse than before — or silent
no-ops that read as success.

**And the lane that would supply a trustworthy signal has never run.** M34's closure carries
**G11 — zero captured QA-role runs.** `epic_qa` has a config key and a policy row and no
evidence behind it. The capability that would answer *"is this instance stuck, finished, or
confidently wrong"* is the one that has never been exercised.

This is the load-bearing risk, not scope. Run-first ordering says the answer comes out of a
real run.

---

## M35 disposition

SN-24 was ruled **accepted, amended to the role** (2026-07-28): M35 names the operator by
role, naming neither a chat nor a daemon, and **M35 stays in P10**.

This note adds to M35's **content**, in the same role-level language: the operator role
includes **handing back on a block**, the handback is authority-bearing, and escalation
travels exactly one level.

**Observation, not a request:** this is the second amendment to a milestone that has not
opened. Rather than patch M35 twice, it may be cleaner to let the Phase Chat **re-scope M35
from current understanding** when it opens, folding both amendments in at once.

---

## Requested HQ actions

1. **Rule on the handback rule** — that a blocked autonomous instance must be able to surface the block to a human with sufficient context, that it travels as an escalation notice, and that the intervention is authority-bearing. Role-level language only.
2. **Record the one-level escalation rule normatively** — parent-only targeting, parent decides resolve-or-escalate — and note it as the standing protection against the P9-GH-1 authority class.
3. **Record Creation Chat awareness as visibility-only**, with the Seed Rule 3 boundary stated, so it cannot drift into a resolution path.
4. **Ratify the execution matrix** and record that it **supersedes SN-23 Ratified Decision #2 on the Execution Mode axis only** — the locality half stands, with Milestone under evaluation.
5. **Direct the Milestone × local evaluation** — what evidence is sufficient, that it must measure **review quality** rather than throughput, whether to harvest the configuration already live in `Getawayinsured2023`, and whether the result may amend row P4 independently of its unfired trigger.
6. **Direct M35's treatment** — fold this into M35's content, and decide whether M35 is amended a second time or re-scoped once when it opens.
7. **Record the block-detection dependency and G11** as the load-bearing risk on any future handback work, so it is not discovered late.
8. **Confirm nothing here is built in P10.** M35 records the rules; P11 builds the mechanisms.
