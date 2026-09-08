# Phase Execution Chat Starter — P13

**Phase:** P13 — Daily Fleet Operation in Drivr
**Project:** ai-project-system
**Repository:** `/home/panchew/soft-dev/ai-project-system` (https://github.com/panchew/ai-project-system)
**Phase Spec:** `docs/phases/P13__Daily_Fleet_Operation_in_Drivr/P13__phase-spec.md`
**Phase Branch:** `phase/P13`
**Execution Mode:** manual

> **Written to be self-contained.** This starter is consumed by a Phase Chat running on
> `remote:gpt-5.6-sol`, a different harness from the HQ session that wrote it. It assumes **no**
> tooling, no prior session context, and no capability beyond what it states here. Every fact it
> needs is either in this file or at a path this file names.

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat**.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.9.0 (Effective: 2026-09-03)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.12.0 (Effective: 2026-09-03)

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md
3. This Phase Execution Chat Starter
4. P13 Phase Spec
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Phase.** Stage 1: produce Milestone specs
  and Milestone Execution Chat Starters, commit them, open a PR. Stage 2: oversee Milestone
  delivery, accept clean deliveries by an in-chat acknowledgment **that names the party that
  reviewed and accepted** — silence accepts nothing (PSG §11.6) — and merge when all Milestones
  are accepted and human merge authorization is given.
- **Mode is not authority.** Whatever Execution Mode any instance runs in, Stage-2 acceptance and
  merge authorization still require the human's key.

---

## Phase Context

**Phase number:** P13
**Phase name:** Daily Fleet Operation in Drivr
**Phase spec path:** `docs/phases/P13__Daily_Fleet_Operation_in_Drivr/P13__phase-spec.md`
**Opening ruling:** `.ai-project/artifacts/rulings/2026-09-07__ai-project-system-hq__ruling__p13-opening-and-sn-47-triage.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.9.0
- AI-OPERATING-GUIDELINES.md: v2.12.0
- `.ai-project.yml` `governance.version`: `9.0.0`; released framework `v9.0.0`

**Milestones within this Phase:**

- M48 — Fleet Readiness, Proven by Running It
- M49 — Future Commits Protected
- M50 — Fleet Overview and Project Detail
- M51 — Conversational Execution and Human Intervention
- M52 — Level Extension and the Eligibility Lever
- M53 — Model Selection That Takes Effect
- M54 — Token Value, on Evidence
- M55 — Daily Fleet Adoption and the Maintenance Handoff

**Ordering constraints (binding):** **M48 gates M50.** **M50 gates M51 and M52.** **M49 is
independent** and may run in parallel from the start. M53 depends on M49's configuration boundary
and M51's inference/activity contract. M54's analysis begins from M48's baseline.

**Session objective:** produce a complete Milestone spec and a Milestone Execution Chat Starter
for each Milestone above, one Milestone at a time, and return each set to HQ Chat for review and
acceptance.

---

## Prerequisite Verification — before any planning work

**Model verification (P9-M31-E31.3).** This instance is **manual**. Read your own
harness-reported model identity and compare it with `.ai-project.yml`'s `models.phase`, which is
**`remote:gpt-5.6-sol`**. See `governance/systems/chat-hierarchy.md` "Manual Chat Model
Verification" for the mapping, the self-report method's known limits, and the
absent-block/absent-key permissive default.

**`.ai-project.yml` currently sets `model_verification: blocking`.** If both identities are
present and disagree, **STOP.** State the mismatch plainly and wait for HQ Chat/human resolution.
Do not proceed with any planning or review work. This is a documented instruction you must
follow, not a technical impossibility.

**Do not infer an exact model identity from the application name or from the identity of the
authoring chat.**

---

## Entry Conditions — verify before opening any Milestone

The Phase Spec defines three. **All three were discharged on 2026-09-07, the day the phase
opened.** Your job is to **verify and report** — not to redo them. If any check below fails, stop
and report to HQ Chat.

1. **Drivr has a private git remote.** ✅ Discharged — `https://github.com/panchew/drivr`,
   private, default branch **`main`**, 28 commits pushed.
   Verify: `git -C /home/panchew/soft-dev/drivr remote -v` returns a remote, and
   `git -C /home/panchew/soft-dev/drivr status -sb | head -1` shows `main...origin/main`.
   *Gates M50 onward. M48 and M49 change no Drivr code.*

   > **Do not check for branch protection.** An earlier draft of this condition asked for it.
   > **This framework's expectation is no branch protection** — `panchew/ai-project-system`'s own
   > `master` returns *"Branch not protected."* PR discipline here is procedural and
   > harness-enforced. **An absent protection rule is the convention, not an unmet condition.**
   > Note also that Drivr's default branch is **`main`**, not `master`.

2. **The three fleet projects' `.ai-project.yml` model additions are committed.** ✅ Discharged —
   `panchew-io` `0b520aa`, `footboard` `d0c4c2a`, `home_finance` `fbfc4b1`, all pushed. Each
   commit is scoped to `.ai-project.yml` alone; `footboard`'s 21 other in-flight planning changes
   were deliberately left uncommitted.
   Verify: `git -C /home/panchew/soft-dev/<project> status --short -- .ai-project.yml` is clean,
   for `panchew-io`, `footboard`, `home_finance`.
   *Expect `home_finance` to fail validation with **2 errors / 2 warnings** — all four are
   pre-existing (absent `project.description`; underscore in `project.name`) and are **M48's** to
   resolve. **No rename is authorized.** They are not an unmet entry condition.*
3. **`models.creation: gpt-6` is committed and the suite is green at 774.** ✅ Discharged —
   PR #283 merged as `dfb9d14`.
   Verify: `git show HEAD:.ai-project.yml | grep '^  creation:'` reads `remote:gpt-6`, and
   `PYTHONPATH=. python3 -m pytest -q` reports **774 passed**.
   *Context: `master` was red from `2ed2a48` (2026-09-07 08:44) until that PR — the divergence
   guard between `chat-hierarchy.md`'s mapping table and `.ai-project.yml` failed, 773/1. If you
   see 773 passed / 1 failed, the PR has not merged.*

**If an entry condition is unmet, report it to HQ Chat.** Do not plan around it and do not
declare it satisfied by intent.

---

## Spec Existence Requirement

The Phase spec MUST exist at the path above before this session begins.

**If the Phase spec is missing:** STOP immediately. Report it to HQ Chat. Produce nothing.

**If the Phase spec is incomplete or ambiguous:** report the issue to HQ Chat. Do NOT assume
intent or fill gaps without HQ Chat confirmation.

---

## What You May Not Reopen

**Four CFO decisions**, recorded in the opening ruling §2. These are settled:

1. `model_verification: blocking` is intentional; the configured model rows are true.
2. Drivr receives a private remote before any Drivr-code milestone opens.
3. Eight milestones, with repeatability proven in M48 rather than at the phase's end.
4. Phase/Milestone dispatch becomes representable, gated by an eligibility lever defaulting to
   **OFF**, scoped **per-project with a fleet-wide default**; **merge and acceptance authority
   stay unrepresentable by construction**, as does Creation/HQ manual-only.

**Four HQ judgements** (ruling §4) are **open to your correction, with evidence**: the
governance-updater priority, the adoption bar (two reviewed work items per pilot project, five
working days), `home_finance`'s schema resolution, and the assignment of the non-deterministic
suite to M48. They are marked precisely so you can push back on them.

**Six carry-forwards are explicitly out of scope** and must not be absorbed into milestone work:
`P12-GH-3`, the Delivery Notice location split, duplicate AOG `Error Handling` content,
closed-phase sweep scope, `P11-GH-2`, and the untemplated `rulings` class. If a milestone's work
appears to require one of them, escalate rather than absorbing it.

---

## Three Things to Carry Into Every Milestone Spec

Recorded here because each was found by reading source rather than prose, and each is easy to
lose in decomposition.

1. **Static alignment is not operational readiness.** A validator returning zero errors says a
   file parses. Any Definition of Done that rests on a config check, a parse, or catalog
   membership is incomplete. M48 exists because of this.
2. **`undetermined` is first-class and must stay visible.** P12 made it survive end to end at six
   substrates. Rendering it as *in progress* anywhere in the surface is the fail-open disposition
   drawn on a card — the interface asserting knowledge the system does not have.
3. **M52 reopens a closed capability domain and must restate what stays closed.** Phase/Milestone
   dispatch is currently unrepresentable by construction in
   `/home/panchew/soft-dev/drivr/drivr/capabilities/model.py`, not merely unimplemented. A domain
   reopened without re-stating its remaining closures loses them by drift rather than by decision.

---

## Output Requirements

Produce, in order, for each Milestone:

1. **Milestone spec** — a complete `P13-M<n>__milestone-spec.md` covering milestone goals and
   scope, Definition of Done, the Epics within it (names and brief descriptions), dependencies
   and prerequisites, and acceptance criteria.
2. **Milestone Execution Chat Starter** — a filled-in starter using
   `governance/templates/milestone-execution-chat-starter.md`, ready for HQ Chat to deliver.

**Produce one Milestone's deliverables at a time and await HQ Chat acceptance before proceeding
to the next.** Do not produce all eight simultaneously.

### Delivery format

Commit each Milestone's set to the phase branch, then hand off **by reference** per
AI-OPERATING-GUIDELINES.md §3.1.1: one reference line per artifact (artifact type + id —
repo-relative path — status), or IDE-attach plus one line of intent. **Do not echo artifact
bodies into chat output.**

*Fallback — no repo access?* For genuinely repo-less delivery only, use the four-backtick fenced
full-body form per §3.1.1, and say the fallback is in use.

After each set, explicitly request HQ Chat review before proceeding.

---

## Milestone Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

There is **no** Milestone Delivery Authorization artifact or ceremonial block. When HQ Chat
accepts a Milestone's deliverables — by an acknowledgment **naming the party that reviewed and
accepted** (role + session identity; silence accepts nothing, PSG §11.6) — acknowledge the
acceptance in-chat and proceed.

Standing merge instruction: merge epic branches to `milestone/M<n>` upon Epic acceptance, and
merge `milestone/M<n>` to `phase/P13` upon Milestone completion, HQ Chat acceptance, and
**explicit human merge authorization**. The authorization is an in-chat act; the harness enforces
human merge authorization regardless.

**`cfo_review_gate: enabled`** in this repository: merge-ready PRs surface for CFO diff review
before merge (PSG §11.6.1 — authorization is not review).

Do NOT proceed to execution or merge without HQ Chat acceptance.

---

## Execution Instructions

- Treat the Phase spec as the single source of truth for this Phase.
- Produce Milestone deliverables one Milestone at a time; await acceptance before proceeding.
- Ask questions only if blocked; resolve ambiguities against the Phase spec first, then the
  opening ruling.
- Do not expand scope beyond the eight Milestones listed.
- Do not infer missing information; escalate to HQ Chat.
- Respect the ordering constraints: M48 gates M50; M50 gates M51 and M52; M49 is independent.

---

## Completion Requirements

This Phase Chat planning session is complete when:

- [ ] The three entry conditions have been verified and reported
- [ ] A Milestone spec has been produced and accepted for all eight Milestones
- [ ] A Milestone Execution Chat Starter has been produced and accepted for all eight
- [ ] In-chat acceptance has been acknowledged for every accepted Milestone (SN-19 — no artifact)
- [ ] HQ Chat has declared the Phase planning session complete

Upon completion, declare: "Phase P13 planning complete. All Milestone specs and Chat Starters
accepted. Session closed."

---

## Question Policy

- Ask only blocking questions.
- Do not propose new features or expand Phase scope.
- Do not ask for information already present in the Phase spec or the opening ruling.
- If the Phase spec is silent on a topic, escalate to HQ Chat rather than assuming.
- **Exception:** the four marked HQ judgements (above) may be challenged with evidence without
  being treated as scope expansion.
