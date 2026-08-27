---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-08-27T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-40
    severity: critical
    title: The model lineup is locked across four surfaces and one of them halts the next chat — switching models is a ratchet, and it is the friction the CFO hit in the wild
  - id: SN-41
    severity: high
    title: Set the CFO's model lineup as BASELINE — Claude spend confined to Creation and HQ, Opus 5 only, Fable 5 cancelled
  - id: SN-42
    severity: high
    title: The baseline routes Epic to a remote non-Claude engine and no dispatch path can run one — this, not local inference, is the productivity unlock
  - id: SN-43
    severity: medium
    title: Local inference is PARKED, re-enterable — the north star is unchanged, the sequence is
  - id: SN-44
    severity: medium
    title: Token burn is structural (>150k context), and one mechanism this chat handed the CFO had no bound on it
  - id: SN-45
    severity: medium
    title: panchew-io surfaced an adoption gap, not a panchew-io problem — the framework assumes a configured remote
  - id: SN-46
    severity: medium
    title: Paired external critiques of seed.md — the same model reversed its most harmful recommendation on one sentence of framing, at identical confidence; the strongest specimen SN-37's qualification gate has
decisions:
  - "Claude allowance is spent in Creation Chat and HQ Chat only. Opus 5 only, not Fable 5 for now. This cancels SN-38's scheduled models.creation -> fable-5 edit; that edit never landed and must not."
  - "The model lineup, as BASELINE: Creation = Claude Opus 5; HQ = Claude Opus 5; Phase = GPT 5.6 Sol; Milestone = Deepseek V4 Pro; Epic = Deepseek V4 Flash."
  - "Model switching must remain possible until the CFO declares it is OK to enforce the gates for switching models. Until that declaration, no gate — including SN-37's model-qualification gate — blocks a lineup change."
  - "Agentic runs working properly matters more, for productivity, than local inference. Local inference needs a lot of measuring that is only holding back real-life results."
  - "Local inference is parked and re-enterable, not dropped. The north star (automate without surrendering control of any single node) is unchanged; only the sequence changed."
  - "These changes travel as Steering Note -> HQ ruling -> one PR, outside P12's milestone machinery. They are governance configuration, not phase work."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

This note closes a returning Creation Chat session (2026-08-27) convened by the CFO ahead of P12's
close, after several days spent working other projects — principally `panchew-io` — under this
framework and other models. It hands HQ six binding CFO decisions and seven concerns, whose single
organising claim is the CFO's own: **be more productive, work better, not harder.**

**Severities below are the Creation Chat's rating, not the CFO's.** HQ may re-rate. The decisions
are the CFO's and are not open for re-debate (Rule 3: this chat holds no authority; the CFO's
words carry it).

---

## Concerns for HQ Triage

### SN-40 — Switching models is a ratchet, and the ratchet is the friction [CRITICAL]

**Detail:** The CFO reported that "trying to switch model really caused friction while trying to
make progress in my other project," and named "tight constraint on using other models (tried
setting manually my own choices)" as one of three unstable pillars behind `panchew-io`'s friction.

This chat verified the mechanism. A model choice is locked in **four** surfaces that must be
edited in lockstep:

1. `.ai-project.yml` `models:` block.
2. `.ai-project/artifacts/reference/token-measurement/model-routing-policy.md`'s mapping table —
   `tests/test_model_config.py::test_policy_mapping_agrees_with_yml_block` asserts per-key
   agreement between 1 and 2.
3. `tests/test_model_config.py` itself, which hard-codes `EXPECTED_MANUAL_ONLY_VALUE` and per-key
   expected constants (`test_config_manual_only_key_matches_expected_value`,
   `test_config_epic_dev_is_expected_local_model`).
4. `governance/templates/seed.md`'s *Prerequisite Verification*, backed by
   `governance/systems/chat-hierarchy.md` "Manual Chat Model Verification", which on a mismatch
   instructs the chat to **refuse, unconditionally** — "no continuation, no 'proceeding with
   caution'."

Surfaces 1–3 make a switch a coordinated multi-file edit plus a suite run. Surface 4 makes a
*mistaken* switch stop the next chat from opening at all. That combination is the friction, and it
is a property of the framework rather than of the CFO's process.

**The mechanism is not wrong; its default is.** The unconditional refusal was written deliberately
after the 2026-07-28 incident, where a Creation Chat ran `claude-opus-5` against a configured
`remote:claude-opus-4-8` and opened anyway (SN-26). That reasoning stands. What it did not
anticipate is a CFO who is *deliberately* moving the lineup and needs the freedom to do so.

**One thing is NOT a blocker, and HQ should not spend on it:** the value format already permits
non-Claude remotes. `governance/ai-project-yml-spec.md` §3.4's Format Constraints give
`remote:gemini-1.5-pro` as an example. No schema change is needed to express GPT or Deepseek
values.

**Required action:** Make mismatch behaviour **advisory by default** — the chat states the mismatch
plainly in its first substantive response and proceeds — with an explicit opt-in switch that
restores the unconditional refusal, defaulting **off** until the CFO declares the gates enforce
(Decision 3). Relax surfaces 2 and 3 so a lineup change is a configuration edit rather than a
test-constant edit; the *divergence* guard (yml agrees with policy) is worth keeping, the
*hard-coded expected values* are not. The honesty requirement is unchanged: an unstated skip would
be as dishonest as a false refusal claim, and that clause of `chat-hierarchy.md` must survive.

---

### SN-41 — Set the lineup as BASELINE [HIGH]

**Detail:** The CFO's words: "I need to set the models lineup AS BASELINE." The lineup, verbatim in
substance:

| Level | Engine | Rationale (CFO's) |
|---|---|---|
| Creation | Claude **Opus 5** | "My Claude allowance must be used in Creation Chat and HQ Chat" |
| HQ | Claude **Opus 5** | same |
| Phase | **GPT 5.6 Sol** | — |
| Milestone | **Deepseek V4 Pro** | — |
| Epic | **Deepseek V4 Flash** | — |

"Only Opus 5, not Fable 5 for now."

**This cancels SN-38.** SN-38 scheduled `models.creation` to move `remote:claude-opus-5` ->
`fable-5`; SN-39 flagged it as the trap waiting for the next Creation Chat session. The edit never
landed on master. **It must not land.** This session's Prerequisite Verification passed precisely
because it had not.

**Two items HQ must resolve before writing the block — this chat will not guess them (Rule 2):**

1. **Exact value strings.** `[PROPOSED — confirm]` `remote:gpt-5.6-sol`,
   `remote:deepseek-v4-pro`, `remote:deepseek-v4-flash`. The CFO named the engines, not their
   config slugs. The framework's format requires `remote:<provider-and-model-name>`; the precise
   identifiers must come from the CFO or from the providers, not from this chat.
2. **"Epic" is one word covering three keys.** The block has `epic_dev`, `epic_qa`, and
   `epic_manual`. The CFO said "Epic by Deepseek V4 Flash." Whether Flash covers the QA lane and a
   manually-run Epic chat as well as the Dev lane is **unresolved and must be asked**, not
   inferred. Note that `epic_qa` has never had a trustworthy captured run (G11's history), so
   assigning it silently would place an unmeasured engine in the one lane already known to produce
   worthless verdicts.

**Required action:** Rule on both items above, then land the lineup across the surfaces SN-40
identifies, in one PR. Record the `models:` block's own provenance honestly: unlike the
E30.2 defaults, **this lineup is a CFO allowance decision, not a measurement-grounded mapping**,
and the block's comments currently claim the latter for every value. Do not let the new values
inherit an evidence claim they do not have.

---

### SN-42 — The baseline routes Epic to an engine no dispatch path can run [HIGH]

**Detail:** The CFO ranked this himself: "I realized it's more important (for productivity) to have
agentic run properly working than local inference."

SN-41's baseline sends Epic to **Deepseek V4 Flash — a remote, non-Claude engine.** Every agentic
dispatch path in this repository was built for `local:` values served by Ollama. P11-M37 recorded
that **agentic dispatch has never worked end-to-end here**: the sandbox could not reach ollama,
the runner was absent from the image, and B2.1 fixed the *endpoint* while `discover_runner()` still
wanted a binary the image lacks. M38 then found no engine reachable at all; M40 found one
resolving on the reverse endpoint shape.

So the lineup is a one-PR config change, and **making Epic actually run on Deepseek V4 Flash is
the real work.** These are the same item as the CFO's productivity ranking, and on this chat's
reading it is the single largest lever on his output that this framework controls.

**Required action:** Treat "agentic dispatch against a remote non-Claude engine" as the phase-level
productivity objective, and scope it where HQ judges it belongs — P12 if it fits its spine
(*Completion: Fail-Closed Defaults and the Drivr MVP*), P13 if it does not. This concern asks HQ to
**place** it, not to fix it here. Note the adjacency HQ should not lose: a dispatch lane that
cannot tell a finished run from a silent nothing is the completion-signal problem P12 already owns,
and a new engine class does not exempt it.

---

### SN-43 — Local inference is PARKED, re-enterable [MEDIUM]

**Detail:** CFO's words: "Local inference needs a lot of measuring that is only holding me back from
producing real life results in my projects." He also named "using unmeasured local model for epic"
as the first of `panchew-io`'s three unstable pillars.

Asked directly whether local was parked or dropped, the CFO chose **parked, re-enterable**: local
stays the long-term goal for control, is off the critical path and off the baseline until agentic
runs work, and no measurement work is scoped until he re-opens it.

**The north star is unchanged.** "Automate the pipeline without surrendering control of any single
node" still stands, and local execution is still its finest-grained expression. What changed is
**sequence, not commitment** — and HQ should record it that way, because a future reader will
otherwise read the baseline's all-remote lineup as an abandonment it is not.

**Required action:** Record the park explicitly, with its re-entry condition (agentic runs working
properly — SN-42). Scope no new local-inference measurement work. Existing proven local
configuration (`qwen3-coder:30b`, evidenced by E33.2/E33.4) is not deleted, only removed from the
baseline. Row P4 and the other long-standing local questions stay parked with it rather than being
answered on the way past.

---

### SN-44 — Token burn is structural, and one mechanism had no bound [MEDIUM]

**Detail:** Three separate CFO observations, one root:

1. "Most of my tokens were burned because of long running context." His harness attributes
   **90–100% of last-24h usage to sessions at >150k context**, with session limits at 97–100%.
2. "When I (accidentally) discovered that chats in this project AND Claude could send message to
   each other I let that run and they burned my tokens so fast."
3. "It's important for me to use my token allowance in the most possible efficient way, ASAP."

On (1): `chat-hierarchy.md`'s **G7 session discipline** — one task, one session — already exists,
adopted 2026-07-19 on M30's measured finding that mixed-task milestone and phase sessions accounted
for 53% of spend versus 23% for single-task epic sessions. **It is recorded as guidance, not a
requirement.** The CFO's own measurement now corroborates M30's from the other direction. Whether
guidance is enough is HQ's call; this chat notes only that the mechanism was written, the evidence
has since doubled, and the burn continued.

On (2): the inter-chat messaging capability was surfaced to the CFO **by this chat**, as a way for
governance levels to reach each other without making him the courier. That advice was correct in
purpose and **shipped without a bound** — no cap on rounds, no budget, no stopping condition. Two
chats left talking to each other is an unattended process consuming allowance, which is the same
shape as the silent-failure class this framework exists to catch. The Creation Chat owns this one.

**Required action:** Rule on whether G7 should bind rather than advise. Separately, before
inter-chat messaging is used again, require an explicit bound on any chat-to-chat exchange (a round
cap, a stated purpose, and a terminating condition). Do not scope new measurement instrumentation
to answer either question — `P9-GH-2` already records that `measure-token-burn` cannot verify its
own reduction claims, and re-opening it would repeat exactly the pattern SN-43 just parked.

---

### SN-45 — panchew-io surfaced an adoption gap, not a panchew-io problem [MEDIUM]

**Detail:** The CFO named three unstable pillars behind `panchew-io`'s friction. Two are SN-40 and
SN-43. The third is distinct: **"not having a remote properly configured (github repo)."**

This framework's governance runs on PRs, branches, merge authorizations and delivery notices — it
assumes a configured remote by construction, and `bin/ai-project-init` does not establish one.
Whatever bit the CFO on `panchew-io` will bite every future project enrolled the same way. It is
adjacent to, but distinct from, the init defects already on record (FM 12's placeholder-agent
install; init's §4-invalid output).

**Required action:** Record as an adoption gap against the init/enrollment path, and place it. This
chat does not propose a fix. Note that the P11 ecosystem was four projects and the CFO has three
more unplaced (`content-creation-pipeline`, `wheelie`, `panchew-io`), so the enrollment path is
about to be exercised three more times.

---

### SN-46 — Paired critiques of `seed.md`: the same model, reversed, at identical confidence [MEDIUM]

**Detail:** The CFO had an external LLM critique `governance/templates/seed.md`, passed the critique
verbatim, then told the critic one fact — **the Seed is pasted into the agent, not read by the
human** — and passed the revised critique. Both are on the record with the CFO.

**The pair is worth more than either half.** The first critique's headline recommendation was *"move
Prerequisite Verification to the end — the model check doesn't belong before the human even
speaks."* The second says *"Prerequisite Verification is perfectly designed... for a model, that
check should be blocking — and it is,"* and calls it safety-critical. **Same file, same reviewer,
opposite verdicts, decided entirely by one sentence about audience — and the confidence and the
formatting are indistinguishable between them.**

That is the finding. Not that the reviewer was wrong once: that **nothing in its output signalled
which of the two readings it was operating under.** A qualification gate that scores output quality
would have passed both. SN-37's gate exists to detect *successful nothing*, and this is the cleanest
captured specimen this project has — produced at zero cost, with its own control built in, because
the CFO happened to run the second pass.

**Assessment of the revised critique, which is materially better.** Its diagnosis is **correct and
this chat endorses it**: the Seed conflates *operational rules that always apply* (Rules 1–3, 5)
with *bootstrap workflow for this session only* (Rule 4, "What to Do Right Now"), and does not
visibly separate them.

Its proposed fix, however, is a **regression, and this session falsifies it by construction:**

> Proposed "Rule 6 — Mode Detection": *Inception (no Steering Note passed)* -> follow "What to Do
> Right Now"; *Re-instantiation (Steering Note + Progress Digest passed)* -> take direction from the
> Steering Note.

**The CFO opened this session by pasting the Seed and nothing else.** Under the proposed rule, the
discriminator "no Steering Note passed" evaluates true, and this chat would have branched to
*Inception* and asked *"Tell me about your project"* — of a repository at P12 with eleven phases
closed. The Seed as written does not have that failure: Rule 5 says *"If you are a re-opened session
and those artifacts were not passed to you, **ask for them** before proceeding."* **Absence of
artifacts is a prompt to ask, never a signal to infer.** The proposed rule replaces an explicit
instruction to ask with an inference from absence — the exact class of move Rules 1–2 exist to
forbid.

The other recommendations, assessed:

| Rec | Verdict |
|---|---|
| 1 — explicit mode branching | **Diagnosis right, mechanism wrong.** Rule 5 already carries the branch ("*A re-opened session is not a new project... take direction from the latest Steering Note's Next Action — not from 'What to Do Right Now' below*"). What is missing is **salience**, not the rule. Any signpost added must keep *ask when artifacts are absent* and must **not** discriminate on whether artifacts were passed. |
| 2 — "do NOT generate artifacts as substitutes" | **Already normative — but in the guide, not the Seed.** `creation-chat-guide.md` says a project with no `genesis.md` *"does not render one for this purpose"* and that no Project Brief is expected for re-instantiation. This surfaces a real fragility the critique did not name: **the Seed's cite-don't-restate discipline means an agent that does not follow the pointer loses the guards.** It held on this session, which followed the pointer. It is a dependency, not a guarantee. |
| 3 — keep the reasoning, add execution guards | Directionally fine, too vague to action as stated. |
| 4 — visually separate always-apply rules from workflow steps | **Valid, cheap, take it.** This is the same edit as the first critique's surviving recommendation (surface Rule 4's full-path / bootstrap fork earlier, rather than mid-Rule-4 after the reader has been told to produce a Brief and an HQ Opener). One change satisfies both. |

**Required action, in two parts of very different cost:**

1. **Cheap, do it:** visibly separate the Seed's permanent Rules of Engagement from its
   session-dependent workflow, and surface Rule 4's full-path / bootstrap fork at the top of that
   rule. Optionally raise Rule 5's existing branch to a signpost. **Reject the passed-artifacts
   discriminator explicitly and on the record**, citing this session, so it is not re-proposed by the
   next reviewer — as the first critique's "move verification to the end" would otherwise have been.
2. **The evidence half, worth more:** file **both** critiques as field evidence for SN-37's
   model-qualification gate, as a matched pair with the framing sentence that separates them. Note
   that `.ai-project/artifacts/field-evidence/` **has no template** (a P11 carry-forward) — HQ should
   decide whether filing this specimen is the occasion to write one, or whether the pair is attached
   to an existing artifact type instead.

**One caution on how this specimen is used.** It shows a reviewer's verdict swinging on framing. It
does **not** show that the second reading is correct because it is second, or that framing repairs
judgment in general — the revised critique still produced a falsifiable recommendation, and this
chat caught it only because it was the live counterexample. Do not let the pair be cited as
"context fixes the model."

---

## Decisions Already Made

These are the CFO's, taken this session. HQ implements; it does not re-debate.

1. **Claude allowance is spent in Creation Chat and HQ Chat only. Opus 5 only, not Fable 5 for
   now.** This cancels SN-38's scheduled `models.creation` -> `fable-5` edit. That edit never
   landed and must not.
2. **The lineup, as BASELINE:** Creation = Claude Opus 5; HQ = Claude Opus 5; Phase = GPT 5.6 Sol;
   Milestone = Deepseek V4 Pro; Epic = Deepseek V4 Flash.
3. **Model switching must remain possible until the CFO declares it is OK to enforce the gates for
   switching models.** Until that declaration, **no gate blocks a lineup change — including
   SN-37's model-qualification gate**, which the CFO had previously ruled binds manual verification
   targets. That earlier ruling is suspended for lineup changes, not reversed; it resumes when the
   CFO declares enforcement.
4. **Agentic runs working properly matters more, for productivity, than local inference.**
5. **Local inference is parked and re-enterable, not dropped.** The north star is unchanged; the
   sequence changed.
6. **Routing: Steering Note -> HQ ruling -> one PR, outside P12's milestone machinery.** These are
   governance configuration, not phase work. Chosen over amending P12 (too slow) and over an
   unrecorded direct edit (a `P11-GH-1`-shaped record gap).

---

## Carry-Over Open Items

Non-blocking. Carried from SN-39 unless noted.

1. **The Drivr UX vision is still `State: proposed`** (SN-36). Its `implemented` twin becomes due
   when M45 builds the surface; comparing the two is the Creation Chat's job.
2. **Four unplaced topics, now more urgent than at SN-39:** `content-creation-pipeline`, `wheelie`,
   `panchew-io`, and the harness vision. The ecosystem was four projects at P11; these make seven.
   This is a **Brief-level identity question**, and SN-45 shows it is no longer purely theoretical —
   the CFO is already working in one of them.
3. `github.com/spec-kit` and `gonzalezpazmonica/pm-workspace` — offered as sources to mine, never
   opened. Low cost, non-urgent, still available.
4. **The Progress Digest stream is stale for re-instantiation purposes.** The most recent digest
   (2026-08-17) predates every commit of P12's execution and predates the most recent Steering
   Note. The Re-instantiation Ritual's Step 3 therefore handed this session one live artifact and
   one consumed one. Not a defect in any artifact — a gap in cadence. **New this session.**

---

## Next Action

HQ Chat should:

1. **Resolve SN-41's two open items with the CFO before writing anything** — the exact
   `remote:` value strings, and whether "Epic" means `epic_dev` alone or also `epic_qa` and
   `epic_manual`. Both are tagged `[PROPOSED — confirm]` above and neither may be inferred.
2. **Rule on SN-40**, the ratchet: mismatch advisory by default, opt-in enforcement defaulting off,
   and relaxation of the hard-coded test constants while keeping the yml-vs-policy divergence
   guard.
3. **Land 1 and 2 together in a single PR** to master, per Decision 6 — outside P12's milestone
   machinery. This is the CFO's unblock for `panchew-io` and should not wait on anything else in
   this note.
4. **Place SN-42** — agentic dispatch against a remote non-Claude engine — in P12 or P13 per HQ's
   judgment of P12's spine. This is the largest productivity lever in the note.
5. **Record SN-43's park** with its re-entry condition, and scope no local-inference measurement.
6. **Triage SN-44, SN-45, SN-46** at HQ's cadence. None blocks 1–4. Note that **SN-46 splits**:
   its Seed edit is cheap and optional, but its paired-critique specimen bears on SN-37's
   model-qualification gate, which is live P12 work — route the two halves separately rather than
   triaging the concern as one low-value item.

**A note on how this note itself should be handled.** The CFO's session limit was at 97–100% while
this was written, and his stated constraint is "use my token allowance in the most possible
efficient way, ASAP." Items 1–3 are the ones that convert to his productivity this week. If HQ can
only do one thing before its own context fills, do those.
