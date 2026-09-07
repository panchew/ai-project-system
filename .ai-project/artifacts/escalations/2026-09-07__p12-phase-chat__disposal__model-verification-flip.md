---
type: disposal-note
phase: P12
subject: "model_verification — the advisory→blocking flip, and E41.5's ungated routing rows"
raised_by: "P12 Phase Execution Chat"
decided_by: "CFO (Layer-8); the flip itself is HQ's act and only HQ's"
date: 2026-09-07
status: awaiting-decision
---

# Disposal — `model_verification`, and the rows it would govern

**Prepared for P12's closure.** The phase spec's acceptance criterion requires that P12 **may not close
without disposing of this**: *flip it, or record why not.* The flip is **HQ's last act of closure and
only HQ's**. This note supplies the measurement HQ and the CFO need; it decides nothing.

**All facts below re-measured on `phase/P12` @ `2a66b4a`, 2026-09-07.**

---

## The state, measured

| | |
|---|---|
| Value | `model_verification: advisory` — `.ai-project.yml:93` |
| Enforcement in code | **none** — 0 files in `bin/`, `tests/`, `lib/` |
| Schema status | **unblessed top-level key** — the *only* warning the validator emits (`0 errors, 1 warning`) |
| Who reads it | **chats**, via `chat-hierarchy.md:391`, `:402`, `:411` |

**The "no code reads it" observation is real but was not undiscovered.** `chat-hierarchy.md:423-428`
already states it, and states it better: *"there is no code process wrapping a manual chat session…
This refusal is a **documented instruction the agent must follow** … by the agent's compliance with
governing documentation — not a technical impossibility-to-proceed. **Stating this honestly is itself
part of what this section requires.**"* The normative text is ahead of the finding. What is genuinely
new is the **schema half** (E43.4: the key is unblessed, the same drift class it closed for
`cfo_review_gate` and `rework_exhaustion_flip`) — so the key is **neither blessed by the schema nor
enforced by code**, and is held up entirely by agent compliance, by design.

## What the flip would actually do

Under `blocking` (`chat-hierarchy.md:411`), a chat whose harness-reported model and configured value
**both exist and disagree MUST stop** before any planning, review or execution — *"no continuation, no
'proceeding with caution.'"*

**The lineup it would enforce:**

| key | value | basis |
|---|---|---|
| `hq` | `remote:claude-opus-5` | measured |
| `creation` | `remote:claude-opus-5` | measured |
| `phase` | `remote:gpt-5.6-sol` | **allowance decision (SN-41), not measurement** |
| `milestone` | `remote:deepseek-v4-pro` | **allowance decision (SN-41), not measurement** |
| `epic_dev` | `remote:deepseek-v4-flash` | **allowance decision (SN-41), not measurement** |
| `epic_qa` | `remote:deepseek-v4-flash` | **allowance decision (SN-41), not measurement** |

*(Attributions read from `model-routing-policy.md:168-171`, written by E41.5 and honest on their face.)*

### The symmetry, which is the finding

**The flip halts exactly the levels whose configured values were never verified, and spares exactly the
levels whose were.** `hq` and `creation` survive because they are measured and did not move. Every
level the gate actually governs — Phase, Milestone, Epic — holds an allowance-set value that **no
measurement supports**, and E41.4's back-test for `phase`/`milestone` was delivered **five days after
the landing it would have gated** (E41.5's discharge record; both gates recorded MOOT).

**This is not hypothetical.** This Phase Chat self-reports `claude-opus-5`; `models.phase` is
`remote:gpt-5.6-sol`. **Under `blocking`, the next Phase Chat refuses on its first substantive turn.**
So would every Milestone and Epic chat not running the configured engine.

**Arming the gate would therefore enforce an aspiration against reality**, and the thing that stops is
the working level, not the level that set the values.

## The options

**A — Flip as decided (2026-08-27).** Arms the gate at closure. Consequence: working-level chats refuse
until each level runs its configured engine. Honest, and severe.

**B — Bless the key, independent of the value.** The unblessed-key warning is a **gap, not a decision**:
E43.4 blessed `cfo_review_gate` and `rework_exhaustion_flip` in one change and left this one because it
was out of M43's scope. **This should happen whichever way the flip goes.**

**C — Record why not, with a trigger.** Explicitly permitted by the criterion. Keeps `advisory`, states
the reason (the values are allowance-set and unmeasured), and names what re-arms it.

**D — Reconcile the lineup first, then flip.** Either move the four values to what the levels actually
run, or measure them with **E46.5's qualification suite** — which now exists, with its bar committed
before it ran.

## Recommendation

**B unconditionally, then D, then A** — and **C is the honest fallback** if D is not wanted now.

Bless the key regardless; that is a defect with no decision attached. Then reconcile the four
allowance-set rows before arming a refusal on them — **P12 built the instrument for exactly this**
(E46.5's gate detects *successful nothing* on the itemized historical set, with `PASS`/`FAIL`/
`COULD_NOT_MEASURE`). Flipping before reconciling arms a fail-closed gate on values the phase itself
records as unsupported, and the first thing it stops is P13's Phase Chat.

**If the CFO prefers to flip now anyway, that is a legitimate call** — the gate erring toward refusal is
the phase's own disposition — but it should be taken knowing the working levels halt on day one and the
values causing it were never gated.

## What travels with this

**E41.5's ungated rows dispose here, as one item.** They are the same four rows: `phase`, `milestone`,
`epic_dev`, `epic_qa`, all *configured-but-ungated*. Whatever disposes the flip disposes them.

**Also unresolved and adjacent** — `epic_manual: remote:deepseek-v4-flash` carries no attribution row in
the policy's mapping table at all, and R6's surface confirmation for it was never performed.

---

## AMENDMENT — 2026-09-07, and it corrects this note twice over

**Step 1 (bless) is DONE** — `phase/P12` `36e89d2`: yml-spec §3.9, §4 rule 29, declaration-block entry,
`KNOWN_TOP_LEVEL`. Spec 2.9.0 → 2.10.0. Config now **0 errors, 0 warnings**; suite **767 → 774**.
Falsified both directions. §3.9 states in its own text that blessing adds **no enforcement**, with a
test asserting it says so.

**Step 2 (reconcile) was mis-scoped by this note, in two ways. Both corrections narrow it.**

### Correction 1 — `epic_dev` and `epic_qa` are NOT governed by this key

`chat-hierarchy.md:313-314`, verbatim: *"It governs **manual** instances only — agentic dispatch's
model selection is E31.2's surface, untouched here."* The section's mapping names **five
manual-verification keys**: `creation`, `hq`, `phase`, `milestone`, `epic_manual` — and describes
`epic_dev`/`epic_qa` as the **agentic-dispatch lanes, explicitly distinct**.

**So the flip cannot halt an epic dispatch lane, and never could.** This note's "four rows" framing was
wrong. **Billing being resolved unblocks nothing for this decision** — it unblocks measuring the two
lanes the key does not govern.

### Correction 2 — the rows that DO matter cannot be measured, by this framework's own design

The three unmeasured keys the flip governs — **`phase`, `milestone`, `epic_manual`** — are all
**manual-chat** levels.

- `drivr/capabilities/model.py:20-21`: *"`dispatch` is not constructible at `phase` or `milestone`. It
  is constructible at `epic` only."* **M46/E46.3 made phase/milestone dispatch unrepresentable** — one
  milestone ago, deliberately.
- `bin/successful-nothing-instrument:64`: `LANES = ("epic_dev", "epic_qa")`, and `:378` raises on
  anything else. **Zero mentions of `phase` or `milestone`.**

**Therefore the recommendation "measure them with E46.5's qualification gate" was impossible for every
row it applied to.** The gate measures dispatch lanes; the governed keys are manual levels; and the
framework made those levels undispatchable on purpose. **A manual chat's backing model cannot be
qualified by a dispatch instrument, and P12 built it that way.**

### The disposal, restated correctly

| key | configured | basis | under `blocking` |
|---|---|---|---|
| `hq` | `remote:claude-opus-5` | measured | **survives** |
| `creation` | `remote:claude-opus-5` | measured | **survives** |
| `phase` | `remote:gpt-5.6-sol` | allowance (SN-41) | **refuses** — this chat self-reports `claude-opus-5` |
| `milestone` | `remote:deepseek-v4-pro` | allowance (SN-41) | **refuses**, if run on anything else |
| `epic_manual` | `remote:deepseek-v4-flash` | allowance, **and no attribution row in the policy mapping at all** | **refuses**, if run on anything else |
| `epic_dev` / `epic_qa` | `remote:deepseek-v4-flash` | allowance (SN-41) | **not governed** — dispatch lanes |

**Measurement is not available for the three that matter. That leaves two honest paths:**

**(i) Set the three to what actually runs.** These are manual Claude Code sessions; this Phase Chat
self-reports `claude-opus-5`. If Milestone and manual-Epic chats do too, the true value for all three is
`remote:claude-opus-5` — which would make the config **true**, make `blocking` **safe to arm**, and
close the gap without a measurement campaign that cannot be run. **The values are the CFO's to set**
(the escalation test: changing a value the CFO enumerated escalates).

**(ii) Record why not, with the structural reason.** Now much stronger than when this note was written:
*the governed levels cannot be qualified by the instrument this phase built, because this phase made
them undispatchable.* Keep `advisory`, name the trigger.

**Recommended: (i), then flip.** It is cheap, it is true, and it removes the only reason `blocking` was
dangerous. **(ii) is the correct fallback** and is not a failure — it is the criterion's own second
path, with a better reason than it had this morning.

**`epic_dev`/`epic_qa` dispose separately** as E41.5's ungated-rows carry-forward. Billing is resolved,
so E46.5's gate **can** now measure them — but that is a different item and does not gate this flip.
