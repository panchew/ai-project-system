---
type: hq_ruling
escalation_ref: .ai-project/artifacts/escalation-notices/2026-07-28T20_00_00Z__P10-M34__escalation_notice.md
opener_ref: .ai-project/artifacts/hq-openers/2026-07-28__hq-chat-opener.md
issued_by: HQ Chat (ai-project-system)
issued_to: Phase Chat (P10), Milestone Chat (P10-M34)
phase: P10
milestone: M34
date: 2026-07-28
status: active
blocking_resolved: true
---

# HQ Ruling — Paid-Frontier Model Mapping Refreshed to `claude-opus-5`; Model Routing Is Drivr's Domain

**Escalation:** P10-M34 — `claude-opus-4-8` unavailable in a manual-chat harness surface
**Raised:** Milestone Chat (P10-M34, refused to open) → Phase Chat (P10) → HQ Chat, 2026-07-28
**Answering authority:** ai-project-system HQ — the Phase Chat correctly declined this as
outside its adjacency ("produce proposals only"), and the policy it touches is HQ's to state.

---

## The halt was correct, and this ruling was written from inside it

This HQ Chat ran the E31.3 verification on open, found `claude-opus-5` against a configured
`models.hq` of `remote:claude-opus-4-8`, and **stopped** — as the M34 Milestone Chat had, and
for the same reason. Nothing in this ruling was decided before the CFO resolved the mapping in
session. The guardrail worked exactly as designed at two levels on the same day. It is not the
defect and was not overridden.

---

## Decision 1 — The five paid-frontier keys move to `remote:claude-opus-5`

`hq`, `phase`, `milestone`, `creation`, `epic_manual` → `remote:claude-opus-5`. CFO-ratified in
session, 2026-07-28.

`claude-sonnet-5` — the value the harness offered by default and the one the Escalation Notice
named as the leading candidate — is **rejected**. It is a **tier drop** below the paid-frontier
answer that policy rows P1–P4 record, and adopting it would have quietly re-decided the fixed
P10 posture (Manual/Paid from Creation through Milestone) under cover of a bug fix. The Opus
line did not go away; a *version* of it did. `/model opus` resolves to `claude-opus-5` in the
same Claude Code for VS Code surface the notice reports `claude-opus-4-8` missing from.

`epic_dev`/`epic_qa` are untouched. They remain `local:qwen2.5-coder:14b` and belong to M34's
E34.3, a different surface. Do not conflate the two.

---

## Decision 2 — This is a mapping refresh, not a policy change; M30's evidence is not re-run

**Stated explicitly, as the opener required.** A same-tier version refresh **inherits** M30's
evidence. No re-run of the evidence process is required, and none was performed.

The reasoning is the policy document's own, not HQ's invention:

- `model-routing-policy.md`'s **Change discipline** binds *rows*: "Policy **rows** change only
  with new cited evidence." Rows P1–P4 decide a **tier** — *"Paid frontier"*, *"Paid frontier,
  manual"*. They never named a model.
- `claude-opus-4-8` appears only in the **"Mapping to `.ai-project.yml`"** table — the
  *implementation* of the tier decision. Refreshing it does not touch a row, so the
  evidence rule is not engaged.
- The measured evidence still says what it said: it justifies **the Opus line** over the other
  three measured models (49.6% of spend, plurality at hq/phase/milestone — report §2.3). A
  same-tier successor inherits that justification. A *tier* change would not, which is exactly
  why `claude-sonnet-5` was refused.

Had the answer gone the other way — had the only available model been a tier down — this would
have been a row change requiring new evidence, and M34 would have stayed blocked until that
evidence existed. Recording that counterfactual so the distinction is not read as a rubber stamp.

---

## Decision 3 — A tier is never deprecated; only a version is

The Escalation Notice correctly observed that model unavailability is **not among rows P1–P5's
revisit triggers**. HQ's answer is that it never should be. A revisit trigger for unavailability
has been added to **the mapping table, not the rows** —
`model-routing-policy.md` → *"Mapping revisit trigger — model unavailability."*

Unavailability can only ever falsify a mapping. It cannot falsify a tier, because a tier is not
a thing a vendor can discontinue. Filing the trigger against the rows would have implied that
each future deprecation reopens an evidence-derived policy question; it does not, and treating
it that way is what would make this failure mode expensive every time it recurs.

Same-tier refreshes are applied under this trigger without new evidence. Anything that changes
the *tier* remains a row change and takes the Change-discipline path.

---

## Decision 4 — Per-level-per-project model routing is Drivr's domain (P11)

The CFO's position — *setting the model per level per project is in the domain of Drivr now* —
is **ratified**. It is consistent with SN-24's four-project split: AI Project System is
governance and does not coordinate; Drivr coordinates. "Which model runs which level in which
project" is routing, and routing is coordination.

The framework's own documents already draw this line from the other side: **governance decides
the tier (rows P1–P7); routing decides which model fills it (the mapping table).** That is not
a boundary invented for Drivr's convenience — it is the structure M30 shipped, made visible by
this escalation.

**The framework does not build a relocation of these values in the interim.** The CFO's
proposed interim — move the model value out of `.ai-project.yml` and into the openers — is
**accepted in intent and declined in mechanism**, on the Creation Chat's analysis, which HQ
adopts: the E31.3 guardrail reads `.ai-project.yml`, not the opener, so relocating the source
of truth means normative edits to `chat-hierarchy.md`, template changes, and test changes —
framework capability work that Drivr makes redundant. That is the trap SN-24 avoided with M35
one week ago. Deleting the keys is worse: `chat-hierarchy.md`'s **permissive default** would
have every manual chat open with "no expectation is configured," degrading the guardrail to a
disclaimer rather than relocating it.

The three-step interim is therefore adopted as proposed:

1. **Bump the pin** in `.ai-project.yml` and the policy mapping table (Decision 1 — applied).
2. **Carry the resolved model in the instantiating artifact as documentation, never as source
   of truth.** This is the CFO's instinct without the expensive part, and it builds the habit
   Drivr formalizes. Applied to `P10-M34__milestone-execution-chat-starter.md`, which quotes
   the value and now says explicitly that `.ai-project.yml` remains the only authority the
   guardrail reads.
3. **Recorded here** so no one builds routing relocation into the framework before P11.

There is a structural asymmetry worth preserving and stating: `epic_dev`/`epic_qa` must stay
machine-readable because `bin/ai-project-orchestrator` reads them at dispatch. Only the manual
levels could ever live in prose artifacts. **The carrier follows the reader** — manual chats
are instantiated by a human from an artifact, agentic dispatch by a machine from config. Drivr
eventually reads both, which is why both collapse into it later.

---

## Decision 5 — HQ applied the change directly, as a bounded and recorded exception

`governance/systems/hq-chat.md` says HQ "does not write production code or modify source
files." HQ crossed that line here, deliberately, once, and records why:

**There was no one to delegate to.** Every level that could normally apply this was refused by
the very defect being fixed — `epic_manual` was pinned to `claude-opus-4-8`, so a manual Epic
chat refuses; the agentic lane is `local:qwen2.5-coder:14b`, which E33.2 proved emits exit 0
with zero work. Delegating would have required overriding the E31.3 guardrail to let a chat
open, which is precisely what the opener forbade. HQ was the only unblocked authority, and only
because the CFO's in-session resolution is the remedy the guardrail is designed to wait for.

**Scope of the exception, stated so it is not read as precedent:** a value substitution across
six files, no new capability, no new schema, no behavior change. The only production-source
touch is `bin/ai-project-orchestrator`'s `DEFAULT_MODELS` constant (three lines), which the
suite's divergence guard requires to move in lockstep with the config — a partial application
would have left the suite red, violating the very policy↔config invariant this fix exists to
honor.

**Acceptance gate: the suite.** `366 passed, 0 failures, 0 skips` — identical to the
independently re-verified pre-change baseline. Applied:

| File | Change |
|---|---|
| `.ai-project.yml` | five paid-frontier keys; spec pointer → v2.6.0; provenance comment |
| `.ai-project/artifacts/reference/token-measurement/model-routing-policy.md` | mapping table; rationale generalized to "the Opus line"; version-refresh note; new mapping revisit trigger. **Rows P1–P7 untouched.** |
| `governance/systems/chat-hierarchy.md` | mapping table; new "Values are versions; the decision behind them is a tier" note |
| `governance/ai-project-yml-spec.md` | §3.1 comments, §3.4 field table, format examples, v2.5.0 → **v2.6.0** + changelog |
| `bin/ai-project-orchestrator` | `DEFAULT_MODELS` (hq/phase/milestone) |
| `tests/test_model_config.py` | `EXPECTED_MANUAL_ONLY_VALUE` |
| `docs/phases/P10.../P10-M34__milestone-execution-chat-starter.md` | stale quoted literal corrected + Decision 4 step 2 note |

Historical records were deliberately **not** rewritten — `audit-report.md`,
`token-burn-dataset.md`, the P9 epic artifacts, and the closure declarations still say
`claude-opus-4-8` because that is what was measured and what happened. Evidence is not
retconned to match current config.

---

## Decision 6 — Two items recorded, not fixed

**P10-GH-2 — The Creation Chat Seed does not implement the E31.3 model verification.** E31.3's
own mapping table lists `creation` as one of the five manual-verification keys, and
`chat-hierarchy.md` defines the ritual, but the Creation Chat Seed never picked it up. The
2026-07-28 Creation Chat consequently ran `claude-opus-5` against a configured
`remote:claude-opus-4-8` **and opened anyway**. That gap is the only reason any manual
governance chat was able to run at all this week — an accidental escape hatch that happened to
be load-bearing. It must be closed on its merits, and closing it will make Creation Chat
subject to the same halt this session began with. Owner: unassigned. Severity: Medium.

> **Amendment 2026-08-04 (P11-M36-E36.5) — the P10-GH-2 paragraph above rests on a false premise,
> and the item is re-diagnosed.** The original text is left unedited, deliberately; this note
> corrects it. This amends **no other part of this ruling**.
>
> *"The Creation Chat Seed never picked it up"* is not what happened.
> `governance/templates/seed.md` has carried the E31.3 **Prerequisite Verification** section since
> commit **`d7ee7cd` (2026-07-19)** — **nine days before this ruling** — and
> `governance/templates/genesis.md` carries it from the same commit. The 2026-07-31 Creation Chat
> session, opened from `seed.md`, **ran the check.**
>
> **The real defect was the re-instantiation *ritual*, not the Seed.**
> `governance/systems/creation-chat-guide.md` handed a re-opened session three artifacts, **none of
> which carried a model check**, because the only one that would (`genesis.md`) is not rendered in
> this project. That is why the 2026-07-28 session recorded above was able to open anyway — the
> escape hatch was in the ritual, not in the Seed.
>
> **That defect is now CLOSED.** E36.3 (merged `d8f4871`) canonized a single re-instantiation ritual
> that opens with the Seed and carries the E31.3 check as an explicit **Step 4**.
>
> **A future owner should read the ritual (`governance/systems/creation-chat-guide.md`), not
> `seed.md`.** Sources: **SN-26** (Required action 1); **HQ Ruling 2026-08-01, Decision 8**.

**P10-GH-3 — Policy row P1 contradicts the live config.** Row P1 states *"No `models:` key
exists or is needed"* for the creation level; E31.3 then added `creation:` to `.ai-project.yml`
anyway. `tests/test_model_config.py` does not catch it — `creation` and `epic_manual` sit
outside its five-key `MODEL_KEYS` guard by design. **Not fixed here on purpose:** the
contradictory text lives inside row P1's cell, and editing a row is exactly the act Decision 2
reserves for the evidence path. It is documentation drift, not a behavioral defect, and it is
not blocking anything. Owner: unassigned. Severity: Low.

Both carry forward to the P10 phase closure declaration alongside P10-GH-1.

---

## Decision 7 — M34 is unblocked; SN-24 acknowledged

**M34 is unblocked.** The Milestone Chat may reopen against the corrected `models.milestone`
and proceed to Stage 1 delivery of E34.1 / E34.2 / E34.3. Its earlier refusal requires no
remediation — it was correct, and the corrected starter now says so in place.

**SN-24 is acknowledged and remains open to HQ.** M35's *form* — a chat-shaped System Chat
operator with a daily seed — is superseded by Drivr's headless daemon; its *content* survives.
Not actioned this session: M35 is unscheduled and nothing depends on it today. The binding
instruction is that **the M35 form amendment happens before any M35 planning work begins**, not
during it. The Phase Chat carries this into M35 scoping.

---

## The root cause, and what was deliberately not built

Pinning `models:` to an exact model **version** means every deprecation halts every manual
governance chat until a policy decision is made. This is that failure mode's first real
occurrence and it will recur at every subsequent deprecation.

The structural fix — pin to a tier, resolve the version through an indirection — is **not built
here**, and the omission is a decision rather than an oversight. That indirection is routing;
routing is Drivr's (Decision 4). Building it in P10 would produce framework machinery P11
replaces, for the sake of a substitution that costs one commit and a green suite.

What P10 gets instead is the cheap durable part: the distinction is now **written down** in the
two documents that name a version (Decisions 2 and 3), so the next deprecation is a recognized,
triggered mapping refresh rather than a fresh escalation and a stopped phase.

---

## No Further Escalation Required

The Phase Chat may mark the Escalation Notice resolved on receipt, citing this ruling. The
mapping is decided and applied, the evidence question is answered explicitly, the domain
boundary is ruled, two gaps are recorded, and M34 may open.
