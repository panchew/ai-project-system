---

# Milestone Execution Chat Starter — P10-M35

**Milestone:** P10-M35 — System-Operator Canonization
**Phase:** P10 — Fleet Adoption and Local-Inference Proving
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M35__milestone-spec.md`
**Execution Mode:** manual — the fixed P10 posture through M33/M34 was Manual/Paid from Creation
through Milestone; the ratified execution matrix (E35.4's own subject, SN-25 / HQ Ruling
2026-07-30) now permits agentic mode at this level too, but this Milestone Chat's own instance is
declared **manual** — it is the instance canonizing the rule, and does not exercise the newly
ratified permission on itself. Agentic/Local remains available at the Epic per the existing
posture.

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat** for
Milestone P10-M35.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.3.0 (Effective: 2026-07-02)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.10.0 (Effective: 2026-07-18)

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.10.0
3. This Milestone Execution Chat Starter
4. Milestone Spec (`P10-M35__milestone-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Milestone** — Stage 1: produce Epic specs
  and Epic Execution Chat Starters, commit them to `milestone/M35`, and open a PR; Stage 2:
  oversee Epic delivery, accept clean deliveries by silence — a Review Decision is the exception
  path only (PSG §11.6) — and merge each accepted Epic to `milestone/M35`.
- You MUST NOT implement project code or modify infrastructure — your scope is planning and
  delivery artifacts only. In particular, **you do not build any mechanism** — no block detector,
  no mode switch, no runner→chat channel, no dispatch wiring. Every M35 deliverable is a
  governance **record**; if an epic starts writing code that detects, switches, or dispatches,
  it has left M35's scope (Hard Constraint, milestone spec).
- You MAY create the `milestone/M35` branch (from `phase/P10`), commit Epic specs and Epic
  Execution Chat Starters, and open a PR — your planning artifacts are your deliverables.
- **Artifact scope (adjacency):** you produce artifacts only for your direct parent or direct
  children — **Epic specs and Epic Execution Chat Starters.** You MUST NOT produce the Milestone
  spec (your parent's job — it already exists) or P11 work of any kind.
- You do NOT dispatch Coding/Epic Agents directly — Epic Execution Chat Starters are delivered to
  the parent chat (Phase Chat), which authorizes each Epic-agent launch.
- You report to the **Phase Execution Chat (P10)**; you communicate downward only. Do NOT reach
  across to sibling milestones (M33, M34 — both closed) or lateral phases.
- **Mid-flight amendments:** to change scope after Epic sessions are running, amend the governing
  Epic spec, note the change, and notify the Phase Chat — do not reach into running sessions.
- **Merge authorization is an in-chat act, no ceremonial artifact** (SN-19 / PSG §1A under
  §11.6). The harness still enforces explicit human authorization before any merge.
- **This is P10's final milestone (`is_final: true`).** Your Milestone Closure Declaration
  triggers the Phase Chat's move to phase closure — say so explicitly when you declare M35
  complete.

**Context scoping (per-level context-scoping standard, P9-M30-E30.3):**
- Load at session start: this starter; the Milestone spec (full); the Phase spec **by targeted
  section only** — §P10.3 and M35's entry in §Milestones, plus the phase §Acceptance Criteria;
  PSG preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §10, §11, §11.5, §11.6, §12, §13C, §15; AOG
  preamble+§1, §1.1, §2, §3.7, §3.9, §3.10, §4, §5, §6, §7, §9, §12, §14, §15, §16.
- Load on trigger: PSG §5B/§5C + AOG §3.4 at milestone-closure time (§5C because this triggers
  phase closure); PSG §3, §8A, §13D, §14A, §14C, §18; AOG §3.2, §8, §13, §17 (visual bindings).
- Do not load: PSG/AOG changelogs, other levels' role/starter-format sections, sibling specs
  (M33/M34 — both closed and not consumed by this milestone).
- Use targeted section reads; never re-read a whole document to reach one section.

---

## Milestone Context

**Milestone number:** P10-M35
**Milestone name:** System-Operator Canonization
**Milestone spec path:** `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M35__milestone-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.3.0
- AI-OPERATING-GUIDELINES.md: v2.10.0

**Epics within this Milestone (indicative — you own final decomposition within scope):**
- **E35.1** — Fleet-operator role + no-authority-on-speech seam
- **E35.2** — Operator's standing brief
- **E35.3** — Handback + one-level escalation + Creation Chat awareness
- **E35.4** — Execution matrix ratification + mode-is-not-authority
- **E35.5** — Milestone × local-inference evidence-gathering

**Session objective:** Produce a complete Epic spec and an Epic Execution Chat Starter for each
Epic above (one Epic's set at a time), returning each set to the Phase Chat for review. Under
SN-13 default-accept, the Phase Chat accepts a clean set by silence.

**What makes M35 what it is — read before planning:**
- **This is a re-scope, not a fresh scope.** M35's content was folded from two Creation Chat
  steering notes (SN-24, SN-25) and two HQ Rulings, in one pass, per HQ's explicit instruction not
  to patch the spec twice. Every epic traces to one of those four artifacts (all cited in the
  Milestone spec's Binding Context and each Epic Detail entry) — you are not inventing scope, you
  are decomposing an already-settled record into epics.
- **Nothing is built here.** Every deliverable across all five epics is a governance record —
  normative text, a ratified table, or a recorded evaluation judgment. E35.5 is the one epic that
  *exercises* something (running a local-model review against real material), but even its
  deliverable is a recorded judgment, not a built tool.
- **No cross-repo split** — unlike M33/M34, every M35 deliverable lands in this repo. `.ai-project.yml`
  is not touched by this milestone (E35.4 records the execution matrix normatively; it does not
  change any config — the matrix restores a *possibility*, not a default).
- **E35.4 and E35.5 are the two epics most likely to raise questions — read their Epic Detail
  closely.** E35.4 must say, unambiguously, that mode restoration does not confer authority
  (Stage-2 accept/merge still need the human's key). E35.5 must back-test against the five named,
  already-adjudicated defects — not hypothetical scenarios — and its judgment is evidence for a
  further HQ call on `model-routing-policy.md` row P4, not a decision on that row itself.
- **P10-GH-7 (block-detection is untrustworthy, two-sided) is a caveat every epic touching
  handback should carry, not a problem any epic should try to fix.** It is out of scope to solve;
  it is in scope to state honestly.

---

## Spec Existence Requirement

The Milestone spec MUST be **git-tracked on `phase/P10`** at the path above before this session
begins. Verify with `git ls-files --error-unmatch docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M35__milestone-spec.md`
run on `phase/P10` — disk presence is not proof of commit.

**If the Milestone spec is missing or untracked:** STOP. Report to the Phase Chat. Do NOT produce
any artifacts until it is provided and git-tracked on `phase/P10`.

**If the Milestone spec is incomplete or ambiguous:** report to the Phase Chat. Do NOT assume
intent or fill gaps without Phase Chat confirmation.

**Model verification (P9-M31-E31.3 — required for this manual instance):** read your own
harness-reported model identity (the `# Environment` block or equivalent self-report) and compare
it to `.ai-project.yml`'s `models.milestone` value (`remote:claude-opus-5`) — see
`governance/systems/chat-hierarchy.md` "Manual Chat Model Verification" for the mapping, the
self-report method's known limits, and the absent-block/absent-key permissive default. **If both
are present and disagree, STOP** — state the mismatch plainly and wait for the Phase Chat/human.

---

## Output Requirements

Produce the following, one Epic at a time (do NOT produce all Epics' deliverables at once —
deliver one set, await Phase Chat acceptance, then proceed):

### For each Epic in this Milestone:

1. **Epic spec** — a complete `P10-M35-E35.#__spec__<epic-name>.md` covering: Epic goals and
   scope; Definition of Done; Deliverables; Dependencies and prerequisites; Acceptance criteria.
   Carry the milestone's **Hard Constraint** (nothing built; E35.5's evidence must be real) into
   every Epic spec.
2. **Epic Execution Chat Starter** — a filled-in starter using
   `governance/templates/epic-execution-chat-starter.md`, ready to deliver to an Epic/Coding
   Agent. E35.1–E35.4 are governance-record epics (no local run required — declare `Execution
   Mode: manual` or leave absent per the absence-means-manual default). **E35.5 is the one epic
   that may warrant `Execution Mode: agentic`** if its back-test is conducted via a dispatched
   local-model run rather than a hand-run manual evaluation — your design decision; document
   whichever you choose.

### Delivery format

Commit each Epic's deliverables to `milestone/M35`, then hand them off **by reference** per AOG
§3.1.1 (E30.4, live since v7.0.0): one reference line per artifact (artifact type + id —
repo-relative path — status), or IDE-attach + one-line intent. Do NOT echo the artifact bodies
into chat. *Fallback — no repo access?* Use the four-backtick fenced full-body form per AOG
§3.1.1, and say the fallback is in use.

After each set, explicitly request Phase Chat review before proceeding to the next Epic.

---

## Epic Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

Per SN-19 and PSG §1A / §11.6, there is **no Epic Delivery Authorization artifact or ceremonial
block**. When the Phase Chat accepts an Epic's deliverables (by silence on the happy path),
acknowledge the acceptance **in-chat** and proceed. The standing merge instruction is: **merge
`epic/P10-M35-E35.#` to `milestone/M35` upon Epic completion, Phase Chat acceptance, and explicit
human merge authorization** — the authorization is an in-chat act (the harness enforces human
merge authorization regardless).

Do NOT proceed to execution or merge without Phase Chat acceptance.

---

## Execution Instructions

- Treat the Milestone spec as the single source of truth for this Milestone.
- Produce Epic deliverables one Epic at a time; await acceptance before proceeding.
- **E35.1–E35.4 have no hard ordering among them.** E35.5 has no hard dependency on the other
  four and may run in parallel — sequence it wherever fits your session's flow.
- Ask questions only if blocked — resolve ambiguities against the Milestone spec first. The
  governance-surface location for E35.4's record (`chat-hierarchy.md` is the phase spec's
  expectation, not a fixed requirement) and E35.5's evaluation mechanism are open design
  decisions for you and the Epic Chats — pick a direction, document the reasoning, proceed. They
  are not blockers to escalate.
- Do not expand scope beyond this Milestone's Epics. In particular: do not build any mechanism
  (Hard Constraint), do not decide `model-routing-policy.md` row P4 (E35.5 produces evidence for
  a further HQ call, not the decision itself), and do not touch M33/M34 (both closed) or any P11
  work.
- Do not infer missing information; escalate to the Phase Chat.

---

## Completion Requirements

This Milestone Chat session is complete when:

- [ ] An Epic spec has been produced and accepted for every Epic in this Milestone
- [ ] An Epic Execution Chat Starter has been produced and accepted for every Epic
- [ ] In-chat acceptance has been acknowledged for every accepted Epic (SN-19 — no artifact)
- [ ] The Phase Chat has declared the Milestone planning session complete

Upon completion, declare: "Milestone P10-M35 planning complete. All Epic specs and Chat Starters
accepted. Session closed." **Because M35 is P10's final milestone, also state plainly when the
Milestone itself later closes** that the Phase Chat's next step is phase closure
(`phase/P10 → master`, PSG §5C).

---

## Question Policy

- Ask only blocking questions.
- Do not propose new features or expand Milestone scope.
- Do not ask for information already present in the Milestone spec.
- The settled items (SN-24's form-neutral operator; SN-25's handback rule, one-level escalation,
  Creation Chat awareness-only, the ratified execution matrix with mode-is-not-authority, and the
  Milestone × local evidence mandate; both HQ Rulings in full) apply as recorded — do not
  re-examine them. In particular: do not re-litigate whether mode confers authority (it does not),
  and do not re-litigate whether P9-GH-1 is closed by the one-level rule (it is not).
- If the Milestone spec is silent on a topic, escalate to the Phase Chat rather than assuming.
