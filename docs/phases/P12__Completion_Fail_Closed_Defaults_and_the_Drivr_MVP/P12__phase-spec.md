---
phase: P12
name: "Completion: Fail-Closed Defaults and the Drivr MVP"
status: scoping
start_date: 2026-08-19
planned_end_date: 2026-09-19
version: 1.3.2
---

# Phase P12: Completion — Fail-Closed Defaults and the Drivr MVP

## Executive Summary

Eleven phases have built a governance framework and, in P11, a coordinator for it. **What none of
them did is use it.** The CFO's own words, recorded in SN-31: *"just doing some testing and measuring
does not count as being using it already."* Agentic mode has never been integrated in any project.

> **Restructured 2026-08-19, hours after opening, at CFO direction (SN-38).** A new **M41 — The
> Model Line-Up and Its Evidence** is inserted first, and the six original milestones shift +1
> (`M41→M42` … `M46→M47`). **Every P12 artifact predating v1.1.0 cites the old numbers and was
> correct at its date.** Nothing in the spine changed; the CFO ruled the per-level model line-up and
> directed that its evidence be collected early, which is a placement question, not a scope one.

P12's spine, in the CFO's words:

> *Completing what I think is my vision of the workflow, using the governance and the MVP of the
> harness (Drivr).*

**This is a completion phase, and that is established by evidence rather than asserted.** The CFO
described his intended workflow to a chat held deliberately ignorant of this repository, Drivr, and
every name in either. Only then was the description diffed against what is built. Five levels,
Stage 1 / Stage 2 epic-set authoring, one-level escalation, per-level acceptance gates,
default-accept, phase-scoped artifact lifetimes, agentic confined to Phase/Milestone/Epic — **all
matched.** The framework is substantially the thing its owner meant to build. What remains is the
distance between *built* and *used*.

**One disposition stands in that distance, and it is what this phase is about.** Four instances,
each verified independently on `master` at `19c77ab`, 2026-08-19:

| # | Where | Behaviour when the gating evidence is absent |
|---|---|---|
| 1 | `bin/ai-project-orchestrator:393-397` | Docker missing → prints a warning and runs the agent's command **unsandboxed on the host**, `subprocess.run(command, shell=True, ...)`. Isolation fails **open**. |
| 2 | `bin/ai-project-orchestrator:472` | `subprocess.run(["git", "add", "."])` — stages the **entire tree**, not the epic's files, then commits it under the epic's message. |
| 3 | `bin/ai-project-git-merge:269, 275-281` | `gh pr review --approve` fails → *"Warning: … Proceeding to merge"*, then a three-rung ladder ending in **`--admin`** override and `--auto`. **A test at :447-460 asserts the admin rung succeeds against a branch that returned "Branch protected."** |
| 4 | M39's completion judgment | On absent effect evidence returns `undetermined`; on strict scoring **loses to a degenerate baseline that always answers "completed."** |
| **5** | `bin/ai-project-init:328, 336-353` | Governance agent not found at the (off-by-one) source path → **writes a placeholder**, then validates the placeholder and reports success. **Found by HQ 2026-08-19; filed `P12-GH-2`; it has a live victim.** |

**These are not unrelated bugs. They are one disposition: when the evidence that should gate an
action is absent, the action proceeds.** The CFO confirmed this reading on the first four instances
explicitly. **Row 5 is HQ's own, added on the way in** — found by asking whether SN-31's four were the
complete set. They were not, which is the strongest available argument that the disposition is a
property of the system rather than a list of defects.

**Why it gates the rest.** Agentic mode is *defined* by no human being present to notice an absence.
A system that proceeds on missing evidence is therefore exactly as safe as its supervision, which
under agentic operation is zero. This is the technical content of the CFO's position that he cannot
move forward without at least one level agentic, and cannot go agentic without tightening the
foundations first.

**And the Drivr UX wants the same work.** SN-36 captured the MVP surface: a window that opens where
attention belongs, and a blocker that opens its own chat. Those are one requirement stated twice —
**the window must know, without the human, whether work is finished and whether it is stuck.** That
is row 4 plus `P10-GH-7`. The surface and the spine are not two tracks; the surface is downstream of
the signal.

---

## Vision

**By the end of P12, the framework's default on missing evidence is to stop, and a real epic has been
carried through it agentically, end to end, by Drivr.**

Three properties define completion, and they are ordered by dependency, not by preference:

1. **Fail-closed where absence means "we do not know."** Not everywhere — Carry-Over 9 of SN-31
   records the correct counter-case: *fail-open is a defect when the fallback does something, and
   safe when the fallback is no change.* The governance auto-update **check** fails open correctly.
   Sandbox absence, approval absence and effect absence do not.

2. **A completion signal that can say "I don't know" and be believed when it says "done."** M39 built
   the judgment and honestly recorded that the sole roster engine cannot produce the verdict. P12
   either makes it produce one or measures and states the limit — and either way `undetermined`
   becomes a first-class state the board renders, never folded into `in progress`.

3. **The rule that cannot be clicked.** SN-36's strongest idea, and HQ treats it as a design
   principle rather than a feature: *UI constraints to observe governance rules.* Today every rule
   here is enforced by an agent reading prose and choosing to comply. Making a rule
   **unrepresentable in the interface** is a different class of guarantee — and it is SN-31's
   fail-open finding approached from the other side.

**What P12 is not.** It is not a redesign, not a defect backlog with a phase wrapped around it, and
not more governance for its own sake. Every normative change in this phase is traceable to a
described-vs-built gap or to a verified fail-open instance.

---

## Scope

**Where P12's work lands.** Split between this repository (the `bin/` execution tier, the normative
corpus, the artifact templates) and **Drivr** at `~/soft-dev/drivr` (the surface, the recorded
mode-flip, the qualification runner). The first real agentic integration lands in whichever project
M47 selects, with its evidence recorded here.

### P12.1: The Model Line-Up and Its Evidence (M41)

**Inserted 2026-08-19 at CFO direction, after the phase opened.** SN-38 records the CFO's ruling on
the target per-level model line-up and his direction that **the evidence be collected first, as an
early step of P12.** The reason he gives is friction removal: *"I don't want to go through friction
when I need to setup the models."*

**HQ restructured rather than absorbed.** The measurement was offered a home in M42 or as a
bugfix-shaped spike; both were rejected. `governance/systems/bugfix-epic-workflow.md` excludes work
that *"requires investigation — root cause unknown, fix scope unclear"*, which is precisely what a
measurement is, and putting it in M42 would make the fail-closed milestone *"the milestone things get
put in"* — the pattern HQ named in P11 and constrained itself against. **It is a milestone.**

**The line-up, as ruled:**

| Key | Current | Target | Kind of change |
|---|---|---|---|
| `creation` | `remote:claude-opus-5` | **fable-5** | Same-tier mapping edit |
| `hq` | `remote:claude-opus-5` | **unchanged** | None |
| `phase` | `remote:claude-opus-5` | **GPT-5.6 Sol** | Same-tier mapping edit |
| `milestone` | `remote:claude-opus-5` | **Deepseek V4 Flash** | **Policy-row change — closes row P4** |
| `epic_manual` | `remote:claude-opus-5` | **local:qwen3.8:27b** | Tier change |
| `epic_dev` | `local:qwen3-coder:30b` | **held** | Gated on measurement |
| `epic_qa` | `local:qwen3-coder:30b` | **held** | Gated on measurement |

**This change routes almost nothing. It arms a set of fail-closed checks.** Five of the seven keys
are **manual-chat verification targets** (P9-M31-E31.3): a chat at that level **halts** if it opens
on a model disagreeing with the declared value. Only `epic_dev` and `epic_qa` are dispatch lanes.
**The moment the edit lands, five verification targets arm simultaneously**, and a chat opened on the
old model halts by design. That is correct behaviour and a poor surprise; **announcing it before the
edit lands is a Definition-of-Done item, not a courtesy.**

**Two harnesses, because the checks do not transfer** (CFO ruling, SN-38 — the gate binds manual-chat
verification targets **as well as** dispatch lanes; the Creation Chat's narrower lanes-only proposal
is superseded):

| Kind | Keys | Qualified by | Status |
|---|---|---|---|
| Agentic dispatch lane | `epic_dev`, `epic_qa` | Detecting **successful nothing** — tool rounds > 0, files changed > 0, claims resolving against files that exist | **To be built** |
| Manual verification target | `creation`, `phase`, `milestone`, `epic_manual` | Detecting **failed judgment** — planted defects, catches vs false alarms | **Already exists — E35.5's back-test** |

**What M41 measures, and the premise correction that shapes it.** **No comparison between
`qwen3-coder:30b` and any 27b has ever been run.** E33.2 compared `qwen2.5-coder:14b` against the
30b; E35.5's `PASS 4/5, one SPLIT, zero false alarms` over ten runs belongs to **`qwen3.6:27b`**,
chosen deliberately because Stage-2 review is general reasoning and the 30b is coder-tuned. **The only
milestone-level judgment result this project owns belongs to a 27b, not to the model currently
configured.**

- **`epic_dev` and `epic_qa` measured separately**, not as "the Epic model". They hold the same string
  today and the record treats them oppositely: `epic_dev` owns the project's **only mergeable-work
  evidence** (E33.2 Run B, E33.4); `epic_qa` owns its **only recorded fabrication** (E39.3 — `VERDICT:
  PASS`, zero tool rounds, citing a key the file does not contain, with read-only tools genuinely
  advertised). One string has been hiding the distinction.
- **The incumbent measured first**, to establish the relative bar's baseline — there is currently no
  baseline for `qwen3-coder:30b` on the judgment task.
- **`qwen3.6:27b` as a real candidate, not a footnote.** Caveat: it is present in Ollama but
  **declared nowhere in `opencode.json`**, so it is not routable through the execution adapter without
  a config addition. That addition is M41's work.
- **`qwen3.8:27b` verified present on this host** — 17.7 GB, confirmed by HQ 2026-08-19 against the
  Ollama tags endpoint, discharging SN-38's Next Action 4. Like both other 27b/30b entries it exceeds
  this box's 16 GB VRAM and will partially offload.

**M41 has a split shape, and it is forced by two CFO constraints that pull opposite ways:** collect
the evidence **early**, and **land no swap until the fail-closed milestone closes** — because M42
repairs the code the lane runs through, and a model change landing with a lane repair makes the next
failure unattributable. **So M41 opens first and closes late:** its measurement epics run at the head
of the phase, and its terminal epic — the `.ai-project.yml` edit plus the `model-routing-policy.md`
mapping-table and row-P4 update, which travel together — **is gated on M42's closure.** Two
milestones concurrently in flight is already this phase's design.

**Safe to measure now:** a qualification run dispatches through the agentic lane, and Docker is
present on this host, so `bin/ai-project-orchestrator`'s unsandboxed fallback will not fire. The
dependency on M42 is real but not blocking, and is recorded rather than assumed away.

**One interaction HQ holds while scoping, stated once and not as an objection.** Epic drops to a
local 27b at the same time as Milestone — the level that *reviews* Epic — drops from paid frontier to
a Flash tier. **The reviewer and the reviewed move down together**, and P11's own record concludes
that the review chain *"caught every HQ error"*, each *"one level down, by a chat applying HQ's output
rather than reading it."* That chain is currently the system's main defence. Not a reason to refuse;
a reason for **M47 to be watched closely rather than assumed.**

---

### P12.2: Fail-Closed Execution Tier (M42)

**The three execution-tier defects, SN-31 rows 1-3.** Under **Decision 2 of SN-31 — a sequencing
constraint, not a date: they land before the first real agentic integration, not after.** Exposure
today is genuinely low *because* nothing runs agentically; all three go live simultaneously the
moment one project does.

- **Row 1 — sandbox absence.** `FileNotFoundError` on the Docker invocation currently falls through
  to host execution with `shell=True`. The fix is not "log louder": absence of isolation must abort
  the run, and any host-execution path that survives must be an **explicitly declared, recorded**
  opt-in rather than a fallback. If it is recorded, the run record says so.
- **Row 2 — `git add .`.** The commit must carry the epic's files. What "the epic's files" means is
  the design question M42 owes an answer to, and the answer must handle the case where the agent
  touched something it should not have — which `git add .` currently launders into the epic's commit.
- **Row 3 — the merge ladder.** Approval failure must abort. The `--admin` rung must go or be gated
  behind a recorded human authorization. **The test at `bin/ai-project-git-merge:447-460` encodes
  the defect as expected behaviour** — it must be inverted, not deleted, so the guard is what the
  suite asserts.

- **Row 5 — the manufactured substitute** (`P12-GH-2`, HQ, 2026-08-19). `install_hq_agent` reads a
  source path one `governance/` level short of where the submodule actually puts the agent, falls
  back to a 230-byte placeholder, and then **validates the placeholder** — readable, non-empty,
  starts with `#`, all of which a stub satisfies. `tests/test_init_agent_path.py` runs with
  `--skip-submodule` and so can only ever exercise the stub branch. **Two of this phase's instances
  are protected by their own tests.** The second init defect travels with it: `submodule_path:
  governance/` against the fleet's `.governance` convention.

**Blast radius is a scoping obligation, not an assumption.** These scripts live in `bin/` at this
repo's root and are therefore *not* inside the `governance/` submodule adopting projects consume —
but `AI-OPERATING-GUIDELINES.md`, `chat-hierarchy.md` and three guides instruct adopters to use them.
M42 determines and records who actually runs these paths today, including Drivr.

### P12.3: The Acceptance Chain, Made Structural (M43)

**Changing who does what, so the bypass class becomes unavailable rather than discouraged.**

- **The parent performs the merge, not the child** (SN-31 Decision 4). `P9-GH-1` and `P10-GH-9` both
  describe a child taking merge authorization directly and bypassing its parent's Stage-2 review;
  E40.5 patched that **behaviourally** across eight starter surfaces. **If the parent merges, the
  child never holds the authorization at all.** The E40.5 guard demotes to a backstop. Known
  consequence: `governance/templates/merge-authorization.md` is addressed to the child and becomes
  the parent's own record. ~~One template edit.~~
  > **CORRECTED 2026-08-20 (M43 spec, W4): "one template edit" understated it.** The template is
  > child-addressed **structurally** — in its subject, its fields and its post-conditions — not
  > cosmetically. This spec repeated SN-31 Decision 4's own estimate without re-deriving it against
  > the file. **E43.1 scopes to what the template actually says, not to that estimate.**
- **Accept-by-silence is tweaked, not retired** (SN-31 Decision 3). Its cheapness is what stops a
  parent producing an artifact on every happy path, and it keeps every artifact in the corpus a real
  decision. What is replaced is **silence as the sole carrier**, which cannot distinguish *reviewed
  and clean* from *never looked* from *the session died*. Note the gap is narrower than "no record":
  §11.6 already makes the merge plus the in-chat acknowledgment the acceptance record. The merge
  proves **something was accepted**, not that **a review happened**.
  > **SHARPENED 2026-08-20 (M43 spec, W3).** `chat-hierarchy.md:201-205` **already** rules that *"an
  > agentic instance's silence is not the silence §11.6 speaks of, and does not by itself accept a
  > delivery."* **Half of this problem was closed before P12 opened, and this spec did not say so.**
  > What remains is the **manual** case, where the corpus names its own load-bearing assumption —
  > *"the human's key is present at the session by construction"* — which is **a presumption about
  > attendance, not evidence of review.** *Never looked* and *the session died* are precisely the two
  > ways it fails while the words stay true. **E43.2's problem is therefore: replace an attendance
  > presumption with a cheap positive signal, keeping the property that a clean delivery costs no
  > artifact.**
- **Exhausted rework flips the receiving parent chat to manual — opt-out default** (SN-31
  Decision 5). **The first fail-closed default in the system**, and the direct counterweight to the
  finding. Its known conflict is resolved: `chat-hierarchy.md` holds that a reader determines an
  instance's mode by reading its committed starter, so **Drivr performs the flip and records it**,
  leaving the committed record the source of truth rather than contradicted by it. The switch
  follows `cfo_review_gate: enabled` in `.ai-project.yml` — the existing precedent for a governance
  gate on by default and disabled deliberately.
- **Resume restores, it never promotes** (SN-36/37). Only an instance whose committed starter
  declares `agentic` may be resumed to agentic. A button that could promote manual → agentic would
  be **granting a mode the starter never declared** — mode-granting by click. **Resume returns the
  mode, not the budget:** it does not reset the attempt counter, or the flip's own trigger would
  make the limit unenforceable by the control meant to recover from it.
- **The rework limit, reconciled** (`P12-GH-1`, SN-32, SN-36/37 Carry-Over 2). Two problems, one
  milestone: the rule reaches **one** of nine starter-shaped surfaces and zero templates, and there
  are now **two statements of what a written extension grants** — `milestone-execution-chat-starter.md:334`
  says the limit *"resets"*; the CFO's amendment grants **+1**. The amendment is **stricter** than the
  rule it invokes, and M43 must reconcile rather than stack. See `P12-GH-1`.

### P12.4: Rituals, Records, and the Normative Repairs (M44)

**Adding the missing artifacts and rituals that record continuity — the tier P11 proved is thinnest.**

- **`P11-GH-3` — a Phase Completion Declaration at PSG §5C Step 2.** *P12's opening is its own first
  customer* (digest Next Action 5). Every level below Phase has a closure artifact **before** its
  parent's gate: Epic's Delivery Notice, Milestone's Closure Declaration marked *COMPLETE (awaiting
  consolidation)*. Phase has none — §5C Step 2 names no artifact, no path and no template, so P11's
  verification checklist and phase summary landed in a **PR comment**. Step 9's declaration stays
  exactly where it is; it records the merge commit, tag and head, none of which exist earlier.
- **The HQ re-instantiation ritual (SN-35, as corrected) — and it must cover DEPARTURE, not only
  arrival.** *Adopted 2026-08-20 from the M44 spec's recommendation, on a live dated specimen.*
  **The ritual failed in real time on 2026-08-20, inside the phase building it**, with governance
  content in flight: HQ adopted three phase-spec corrections, deferred the edit, and the Phase Chat's
  reply proposing a firmer terminus could not be delivered because it could not identify which live
  session was HQ. **The nine committed openers all describe what an ARRIVING session receives. Nothing
  describes what a DEPARTING session leaves behind**, and that is the half that just failed. E44.1
  records both.
- **The Phase Completion Declaration is the backstop terminus for any deferred phase-spec
  correction.** *Adopted 2026-08-20 from the M44 spec's recommendation.* It is **the one artifact
  guaranteed to be written while the phase is still open** (`P11-GH-3`, §5C Step 2), which makes it
  the natural catch for obligations whose owner disappears. **A deferred correction whose trigger is
  a session's continued existence is not triggered — it is hoped for**, and this instance proved it
  within four hours.
- **The HQ re-instantiation ritual (SN-35, as corrected).** The normative tier is silent — zero
  occurrences across `hq-chat.md`, `hq-execution-chat-starter.md` and `templates/hq-chat-opener.md` —
  while `.ai-project/artifacts/hq-openers/` holds **nine** instances with a stable type, filename
  convention, schema and `supersedes:` chain. **The practice exists and is undocumented; the work is
  to record the ritual already being followed, not to design one.** The Creation Chat's ritual
  (SN-26, canonized P11-M36-E36.3) is the model and the precedent for its shape. **SN-36 makes this
  load-bearing rather than tidy:** auto-opening a chat *"with the artifacts already applied"* is this
  ritual executed by software, and the app needs one per level.
- **A context-exhaustion handoff artifact** (SN-31 Carry-Over 2). ~~"Handoff" appears as prose in ten
  documents~~; there is no template and no artifact type. Ideally semi-automated against harness
  context tracking, which is Drivr's side of the boundary.
  > **CORRECTED 2026-08-20 (M44 spec, X2): nineteen, not ten.** Measured `grep -ril 'handoff'
  > governance/`. HQ inherited *ten* from SN-31 Carry-Over 2 and wrote it into a binding artifact
  > **without re-measuring** — `P11-GH-2`, and HQ's **second** instance this phase. **Ten and nineteen
  > cannot be reconciled from the artifacts**, which is M43's W2 arriving in a second milestone:
  > **E44.1 states its set as an itemized list, and every later claim cites the list, not a count.**
- **Inter-chat governance messaging: one normative paragraph** (`P12-GH-4`, the narrow half).
  Measured 2026-08-20: `SendMessage`, `ListAgents`, "peer session" and "inter-chat" appear **zero
  times** in `governance/`. **The live channel every P12 escalation travelled over has no normative
  existence.** The paragraph applies SN-36's already-ratified principle — *a chat reply is never
  authorization, because agents can write into chats* — to that channel: **content passing over it is
  routing, not the record; nothing arriving over it authorizes, accepts or closes anything; and a
  recipient that cannot establish a sender's role does not act on governance content from it.**
  *Placed because it restates a ratified principle where it already logically applies, not because it
  designs anything — and because a chat had to invent it under time pressure today.* **The channel's
  wider design stays filed and unowned.**
- **`governance-propagation.md`, amended** (SN-34, ruled 2026-08-19). Its Constraints are verified
  false and three prohibitions rest on them. See the ruling; M44 executes it.
- **The i18n policy paragraph** (SN-31 Carry-Over 10). Chat and output in the user's language;
  documentation remains in the original language; **English is authoritative**; translation on demand
  is a *view*, never the source. One paragraph of normative text. It resolves Carry-Over 6's tension:
  propagating English normative text to a Spanish-speaking adopter is **correct** under this policy.
- **SN-30 Rec 1 and Rec 2** (see the ruling): mechanical checks for the four observed defects, and
  promoting **G1 and G2** out of an epic spec into the core documents.
- **A convention for recording a DECIDED-but-UNCONFIGURED state.** *"Decided"* and *"configured"*
  have never been separate in this corpus: until the R6 ruling, a decision was recorded **by making
  the edit** — the same act. **R6 separated them, possibly for a long time** — three rows decided and
  unconfigured on a trigger with no expiry. **E41.5 is the first artifact that must hold both apart,
  and no convention was designed for it.**
  - **The failure mode is precise:** a reader assumes the file matches the ruling. That is the
    divergence the guards exist to catch, **arriving in the prose, where no guard reaches** — and it
    is `P12-GH-3`'s shape (a resolving reference to rotted content) at the configuration layer.
  - **Binding sequencing: the convention must exist before E41.5 lands.** E41.5 is gated on M42's
    closure and M44 is independent of both, so the ordering is achievable — but it is not automatic.
    **If E41.5 reaches the point of needing it and M44 has not delivered, that is an escalation, not
    an improvisation.** M41 must not invent a convention M44 would then have to change.
- **Record P12's own `P11-GH-1` instance** against its carry-forward note
  (`docs/phases/P11__.../P11__carry-forward-note__P11-GH-1-mid-flight-amendments-do-not-reach-working-branches.md`),
  per SN-39's Next Action. **The facts, so no epic re-derives them:** `governance/hq-p12-opening` was
  cut from `master` at `19c77ab`; SN-38 landed at `3eda074` and was amended at `afe5d79`, both
  **after** the cut; the phase spec on that branch carried **zero** occurrences of `SN-38`,
  `Deepseek` or `epic_qa`; **the Creation Chat found it** (SN-39), not the level below and not any
  mechanism; it was resolved by merging `master` into the branch (`0a19563`) and reconciling before
  `#215` merged (`8f5fb7c`).
  - **Cite it by artifact and defect, never by ordinal.** The carry-forward note records *two*
    instances; P11's closure record counts *four*. **The tally does not reconcile and the project has
    already ruled that it must not be used** (P11-M38 correction). An epic that writes "the fifth
    instance" reproduces the defect it is filing.
  - **This records evidence. It does not reopen the fix.** Ruling Decision 12 stands: `P11-GH-1` is
    **not scoped as work** in P12, because the phase's three parallel tracks will produce more
    evidence than a remedy designed now would rest on. Amending a prior phase's carry-forward note
    from a later phase is established practice (P10-GH-2, P11-M36-E36.5).
  - **What makes this instance worth the entry rather than a tally mark:** it fired **inside the
    phase that owns the gap**, on **HQ's own branch**, and was caught by a chat **outside the parent
    chain** — a Creation Chat reading `master` — rather than by the one-level-down review that caught
    every P11 instance. That is a different detection path from every case on file, and it is the
    part a future remedy has to account for.
- **The AOG section-numbering repair.** Order is `1, 1A, 2-9, 13, 14, 10, 11, 12, 13, 14, 16, 15`,
  with **two sections both titled "Error Handling"** (L701, L861) — so a cross-reference by title is
  ambiguous before numbering is considered. Verified still live 2026-08-19. Ruled **not** a hotfix.

### P12.5: Trustworthy Completion Signal (M45)

**Row 4 of the finding, plus `P10-GH-7`.** The prerequisite for M46, and the reason M46 cannot be run
in parallel with it.

- **`P10-GH-7`** — block detection untrustworthy in both directions, severity High, open since M35 —
  including its missing-Delivery-Notice branch (SN-31 Carry-Over 3), which the CFO arrived at
  independently and left unresolved.
- **M39's judgment on the sole roster engine.** A live OpenCode run projects `effect_ledger=None`, so
  `EFFECTS_VERIFIED` is unreachable; `undetermined` on four of six cases; loses to the degenerate
  baseline on strict scoring. **M40's F5 is the sharpest constraint and must be carried into M45's
  design: the ordered-ledger projection fixes only half the problem** — a perfect ledger on a
  read-only run still returns `NO_EFFECTS_OBSERVED` because `_decide` never reads `Role.INSPECTION`.
  Better classification and more evidence each yield a *worse* verdict.
- **`undetermined` is a first-class state** (SN-36/37, CFO-decided), never folded into `in progress`
  (the fail-open pattern drawn on a card) and never into `blocked` (which over-claims). Rendered
  visibly, the board shows the size of the problem every day — which is the pressure that keeps P12
  honest. Hidden, the dashboard looks healthy while the signal beneath it is broken.

**M45's bar must be relative and stated before the work, not after it** — E35.5's result was usable
precisely because it carried `PASS 4/5, 0 false alarms` in advance.

### P12.6: The Drivr MVP Surface (M46)

**Scoped from SN-36's visual binding, not from assumption.** Gated on M45.

**Visual binding**
- **Link:** https://claude.ai/code/artifact/688a152b-df5d-4882-b48f-26108200b92c
- **What:** mockup
- **Level:** Creation
- **State:** proposed
- **Description:** The Drivr Window — one window, four regions: a left rail of project tabs, a centre
  chat area with composer, a per-project status dashboard showing each project's current
  Phase/Milestone/Epic, and a Current Activity panel with Manual/Agentic controls and a
  go-to-blocker affordance. Rendered from the CFO's hand sketch of 2026-08-19.

- **Open the app, pick a project, land where the work is.** No progress → the seeded Creation Chat.
  Progress → wherever attention belongs. Escalation **opens a chat by itself**.
  > **INPUT, recorded 2026-08-20 from a live failure.** *"Escalation opens a chat by itself"*
  > presupposes the system knows **which chat is which**. It does not. Sessions are addressable only
  > by opaque names (`ai-project-system-<hex>`); **nothing maps a session to its governance role.** On
  > 2026-08-20 the P12 Phase Chat needed to return governance content to HQ, could not identify which
  > live session was HQ, and **correctly refused to route it to an unidentified peer** — recording the
  > obligation durably instead. **That refusal was the right call**, and it is stricter than the
  > standing practice of *address the role and tolerate a wrong guess*, which is unsafe for governance
  > content in a way it is not for a question. **A role registry is a prerequisite for the auto-open
  > and go-to-blocker behaviours, not a convenience** — and it is Drivr's to own, since Drivr opens
  > the chats.
  >
  >
  > **AMENDED 2026-08-27 — the harness moved and half this input's reasoning went with it.**
  > `ListAgents` **now reports the calling session its own address** (*"This session is
  > `ai-project-system-<hex>` — the name other sessions use to message it"*). **It did not on
  > 2026-08-20.**
  >
  > **What DIES:** the claim, which lived in HQ's and the Phase Chat's messages and **never reached an
  > artifact**, that role identification is *unreachable from inside the fleet by construction and
  > requires an outside correlator.* **A session can now state its own address.** That was most of what
  > made third-party probing necessary.
  >
  > **What SURVIVES, and is the real requirement:** **names carry no role.** A fleet still cannot
  > determine *who is HQ* or *who holds M41* from the roster alone, so **the registry requirement is
  > unchanged** — it is just no longer justified by an impossibility. **M46 must build against
  > "names carry no role", not against "sessions cannot identify themselves."**
  >
  > **How it was caught, which is the part that generalizes:** the M41 Milestone Chat **drafted a
  > reply asserting the dead claim verbatim, ran the command anyway before sending, and caught it one
  > turn short of shipping.** *The dependent was a sentence in flight; the premise was the harness the
  > sentence was being written in.* **This is `P12-GH-3`'s most uncomfortable instance — not a
  > document, not a branch, not an executing context, but a claim about the environment making the
  > claim** — and the only thing that caught it was **re-measuring at the moment of use** rather than
  > trusting a finding that was correct when recorded.
  >
  > **HQ's own conduct is the counter-example and is recorded as such: HQ observed the self-address
  > line hours earlier, said so in passing, and amended nothing.** Noticing a falsifying observation
  > and not acting on it is worse than not noticing, and it is why the correction arrived from below
  > rather than from the level that saw it first.
  >
  > **Nothing had to be unwound**, and the reason is the discipline rather than luck: **the dead claim
  > was never filed.** It circulated in messages for a week and stopped at the artifact boundary.

  > **EXTENDED 2026-08-20, same day, from a second live failure — and this half is not the same
  > requirement.** A registry answers *which* session holds a role. **It does not answer how many
  > do.** On 2026-08-20 **two authentic HQ sessions ran concurrently**, both able to commit to
  > `master`. Root cause, from the CFO: **a VS Code layout change** — moving the chat from the editor
  > area to the side panel — **forked the session**, and neither fork could observe the other. **Not a
  > governance failure and not an identity failure**; both sessions were genuinely HQ.
  >
  > **The consequence is contradictory normative artifacts rather than merely lost ones**, which is
  > the sharper outcome. PR #226 declared S5 unresolved **three hours fifty-six minutes after** the
  > CFO's per-lane floor merged, and rewrote a merged gap record at `54+/130−`. **It was caught by the
  > P12 Phase Chat noticing that two rulings disagreed — by a reader, not by a mechanism** — and
  > closed unmerged.
  >
  > **Why a staleness detector would not have caught it, stated because it constrains the remedy:**
  > the offending branch's merge-base was `11906de`, **the current head**, and both merged artifacts
  > were **in its own working tree**. The session reasoned from its conversation history instead of
  > from the repository while holding the answer on disk. **Concurrency made the collision visible; it
  > did not cause it.** A remedy that detects only *"another session moved `master`"* is insufficient.
  >
  > **EXTENDED 2026-08-21 from a third live fork, and this one inverts the diagnosis.** A second
  > **M41 Milestone Chat** authored four commits on `milestone/M41` that the corresponding chat did
  > not write. **The work was correct** — re-measured by the Phase Chat, not accepted on report — and
  > it **caught a defect the incumbent missed**, sweeping a Dependencies→Blockers line still resting
  > on a falsified premise.
  >
  > **The HQ fork was caught because it CONTRADICTED.** #226 declared S5 unresolved after the ruling
  > merged; the contradiction was the signal, visible to a reader as a conflict of meaning.
  > **This fork AGREES** — same voice, same discipline, converging on the same amendments, better on
  > one point. **There was no signal.** It surfaced only because the incumbent went to do work already
  > done, and only because it read the log before editing: **a habit, not a mechanism.**
  >
  > **The property to design against, stated by the Phase Chat:** *a fork that contradicts is
  > detectable at merge; **a fork that agrees is invisible, and it silently doubles the write surface
  > for a role.*** It stays invisible until two agreeing forks write **different but both-plausible**
  > things into one artifact — **at which point there is still no conflict, no signal, and nothing in
  > the record saying which is authoritative.**
  >
  > **And the record cannot answer it retrospectively.** Measured 2026-08-21: `git log --all
  > --format='%an <%ae>' | sort -u` returns **exactly one author** across the entire repository —
  > `Francisco Guzmán <jf.guzman76@gmail.com>` — because the harness signs as the human. **The corpus
  > has no way to tell whether two artifacts in one role came from one chat or two.** That is a
  > property of the harness, not a gap in the corpus, and it means **the currency problem cannot be
  > solved by reading the record.** Exclusivity is therefore not merely the better remedy; **it may be
  > the only one that works.**
  >
  > **Two consequences that narrow the remedy space, and the second rules a class out.**
  >
  > **(a) Correctness is not safety.** From the M41 Milestone Chat: ***a fork does not have to be
  > wrong to be a problem, and being right is not evidence that it was safe.*** This milestone got
  > lucky twice — the twin's amendments were correct **and** it caught a real defect. **A remedy
  > evaluated against whether forks have produced bad output will conclude there is no problem.**
  >
  > **(b) A tie-break computed from the shared state is self-legitimizing and cannot settle a role.**
  > The M41 chat proposed *"the session whose commit most recently touched an M41 epic artifact holds
  > the role"* — a rule designating its twin, which is the only reason it carries weight from a tied
  > party. **It is unusable as a settlement for a structural reason, not a drafting one: the role
  > becomes acquirable by the very act it governs.** Whoever writes last becomes the holder, so **a
  > mistaken write retroactively legitimizes itself.** Any tie-break derived from artifacts both forks
  > mutate has this property. **Exclusivity must be enforced by something outside the state the forks
  > write** — which is Drivr's side of the boundary, not the corpus's.
  >
  > **(c) A second hazard in that rule's published form, and it is the sharpest of the three.** A ref
  > placed after `--` is read as a pathspec, so git falls back to **implicit `HEAD`**. The rule
  > therefore **does not fail — it becomes reader-dependent.**
  >
  > *Measured three ways, and each measurement corrected the last:* first reported as *"silently
  > returns nothing"*; corrected to *"empty from `master`, correct from `milestone/M41`"*; **and HQ's
  > own run returns `9940820` from `master` and `b27b4ed` from `milestone/M41` — neither of them
  > empty, and both valid-looking.** Whether a reader gets nothing or a plausible wrong commit depends
  > on the pathspec they use.
  >
  > **That last form is the catastrophic one and it is why this generalizes past one command.** A rule
  > that always fails gets noticed. A rule that returns *empty* at least has a chance of reading as
  > *no holder*. **A rule that returns a different valid-looking answer to each reader shows nobody
  > anything wrong** — and a tie-break's entire value is that both forks compute it identically.
  > **A malformed tie-break does not produce a tie; it produces two forks each confident they are
  > right, for different reasons, with no error anywhere.**
  >
  > **The general statement, from the M41 Milestone Chat:** *any form resting on implicit `HEAD` is
  > branch-dependent, in a project whose sessions share a checkout that moves under them.* **This
  > repository's shared checkout was observed on three different branches in one day, twice with two
  > HQ sessions in it.**
  >
  > **(d) This is SN-36/37's ratified principle arriving in a fourth place, not a new idea.**
  > *`undetermined` is a first-class state, never folded into another — an interface that can say
  > "I don't know" is the one worth trusting when it says "done."* The other three: E41.2's **S3** (an
  > unloadable replay case must fail loudly, never yield a shorter list); E41.1's **R6a** (config
  > present, self-report absent); and this tie-break, where **empty had no defined meaning and
  > "no holder" is exactly the reading that fires the stall override.** **Each is a check whose silent
  > failure reads as a meaningful value, and the repair adopted in all three is identical: empty means
  > UNDETERMINED and escalates.** Recorded as one citable pattern so it is not re-argued a fifth time.
  >
  > **So the property Drivr owns is exclusivity, not only identification** — the CFO's own framing on
  > reading this incident: *"it will not allow concurrent chats touching the files all over."* **A
  > scheduler that owns which session holds a role, and serializes writes, makes this class
  > unreachable rather than detectable** — SN-36's *"a rule that cannot be clicked outranks a rule
  > that is merely written"*, arriving at the process layer instead of the UI layer.
- **UI constraints observe governance rules.** No agentic option at Creation or HQ (manual-only,
  permanently, SN-22). No Phase or Milestone dispatch control — **it does not exist**, Epic only
  (SN-31 Carry-Over 1). No mode control implying merge authority (*"Mode is not authority"*).
- **The app writes committed artifacts; it does not hold state.** One principle covering auto-opened
  chats, the Manual/Agentic controls, and dashboard-managed configuration.
- **Board vocabulary:** `queued` / `in progress` for active work, **plus `undetermined`**. `queued` is
  a property of the serialized inference lane, **not of the epic** — two epics of one milestone may
  both be active while one holds the lane.
- **Approval, reconciled without weakening either rule.** The chat is where the judgment is
  **formed**; the signed one-time link is what **carries the key**. A chat reply is never
  authorization — *the reason is the threat model, not ceremony:* **agents can write into chats**, so
  a reply-authorizes design lets an agent author its own approval and close the loop on itself.
- **Escalate-further is an explicit human control**, advancing the chain **one** level (SN-25); it
  does not skip levels.
- **Single-window is re-weighted from "explicitly not a requirement" (P11) toward central.** Recorded
  as a deliberate change rather than drift. It does not contradict headless-first: a client of a
  headless daemon is still headless-first.
- **In-app diff review is a nice-to-have.** §11.6.1 requires the review to happen, not to happen in
  any particular place; GitHub or an IDE satisfies it.
- **The model-qualification gate (SN-37)**, with its PASS bar set **as part of this work, not
  deferred to first use.** The bar is **relative and objective**: run the suite against the
  **incumbent** first; the candidate must be no worse on every objective check and strictly better on
  at least one, over an absolute floor of **tool rounds > 0 and files changed > 0**. No subjective
  quality score — judgment is precisely what cannot be trusted from the thing under test. **Its first
  job is detecting successful nothing**, because this project has recorded that failure in **three** runs,
  itemized rather than counted (see the M46/M47 criteria below) — E33.2 Run A, E39.3, and E41.2's DEV RUN 2: E33.2's
  14b returned exit 0 having done nothing; E39.3's dispatches returned confident `VERDICT: PASS` with
  zero tool rounds, citing a config key the file does not contain. Both pass any subjective read.
  They fail only on counts. Drivr is the runner — run the suite, gate the swap, record the result;
  no inference of its own.

### P12.7: First Real Agentic Integration (M47)

> **SN-42 lands here by preference, not by default (CFO, 2026-08-27).** Remote agentic dispatch —
> making an Epic actually run on `deepseek-v4-flash` — is placed in P12 by HQ ruling, and **the CFO's
> stated preference is to EXTEND M47 rather than create an eighth milestone**: *"Better if avoid an
> additional milestone, but let's do it if justified."*
>
> **So the Phase Chat's default is extension, and a new milestone is an escalation it must justify —
> not a free choice and not a forbidden one.** The bar is the work's actual size, not tidiness.
>
> **Why it is here at all:** with local inference parked, all three Epic keys are remote, and **every
> dispatch path in this repository was built for `local:` values served by Ollama.** M47 cannot run
> until remote dispatch exists. **It is a prerequisite M47 silently assumed was solved, not a new
> objective.**

**The phase's proof, and the reason the other five milestones exist.**

One real epic, in one real project, carried end to end agentically by Drivr — dispatched, executed,
completion-judged, gated, escalated if it blocks, handed back to its parent, merged by its parent.
Not a measurement run and not a demo: **work that would have been done anyway, done this way
instead.**

- **Project selection is M47's first decision and must be recorded with its reasoning.** The proving
  pair (`home_finance`, `local-agent-runner`) and Drivr itself are the candidates on current
  evidence; HQ does not pre-empt the choice.
- **M42 is a hard prerequisite** — this is the sequencing constraint, discharged.
- **The run record is the deliverable**, including what the framework got wrong. A clean run that
  surfaced nothing is a weaker result than a run that surfaced a real defect, and M47 should be
  scoped to say so in advance.

---

## Out of Scope

- **llama.cpp and any non-Ollama local runtime** — **CLOSED by CFO decision**, not parked. Its
  hardware trigger is void and no phase re-inherits it.
- **Push / WhatsApp notification** — deferred, unchanged.
- **Sidekick-for-external-projects** — a **Brief-level identity question**. No phase inherits it as
  an unstated pivot.
- **Phase and Milestone agentic dispatch.** It does not exist (SN-31 Carry-Over 1); the CFO places it
  in the roadmap. P12 confines agentic to Epic and makes the *interface* refuse to imply otherwise.
  **"Mode is not authority" is kept anyway** — under the near-term posture it never fires, because
  the only agentic level accepts nothing. It becomes load-bearing the moment the bar moves up, which
  is the stated goal.
- **Governance auto-update as a full reconciler.** SN-31 Carry-Over 9 is *"nice if possible"*, and its
  own scope warning is honoured: *"fix already-broken installs"* turns an updater into a
  **reconciler**, materially larger than the rest. **Split, not carried as one unit** — see the
  ruling.
- **SN-30 Recs 3, 4 and 5** — the observability tier and the exposition-reduction pair. Deferred with
  reasoning; see the ruling.
- **The per-level model and mode mapping** (SN-31 Carry-Over 8) — a plan, not an instruction, to be
  assessed and measured before adoption. No configuration change is authorized.
- **`model-routing-policy.md` row P4** — still the CFO's call, on his timing. Untouched here.

---

## Milestones

**Three binding constraints, none of them stylistic:** **M42 gates M47** by CFO decision;
**M45 gates M46** because the surface's two central behaviours *are* the completion signal; and
**M41's terminal epic is gated on M42's closure** — measure early, land late. M43 and M44 are
independent of each other and of the M45/M46 pair.

**M41 starts first and finishes late.** Its measurement epics are the head of the phase; its
`.ai-project.yml` edit waits for M42. Do not read its milestone number as a claim that it closes
first.

### M41: The Model Line-Up and Its Evidence

The CFO's ruled line-up, measured before it lands. `epic_dev` and `epic_qa` measured **separately**;
the incumbent measured **first** to set the relative bar's baseline; `qwen3.6:27b` added to
`opencode.json` so it is routable; `qwen3.8:27b` (present, verified) competing against it. E35.5's
existing back-test qualifies the four verification targets; a minimal successful-nothing instrument
qualifies the two lanes. **Terminal epic — the `.ai-project.yml` edit with the
`model-routing-policy.md` mapping-table and row-P4 update — is gated on M42's closure, and announces
the change to every level before it lands.**

### M42: Fail-Closed Execution Tier

Rows 1-3 and 5 of the finding. Sandbox absence aborts or is a recorded explicit opt-in; staging is
scoped to the epic; approval failure aborts and the `--admin` rung goes or is gated behind recorded
human authorization; `ai-project-init` stops manufacturing a governance agent it could not find, and
its path defects are fixed together. **Both self-protecting tests inverted** (`ai-project-git-merge`
`:447-460`, `test_init_agent_path.py`) so the suite asserts the guard. Blast radius determined and
recorded, including the fleet sweep for existing placeholder agents.

### M43: The Acceptance Chain, Made Structural

Parent performs the merge; accept-by-silence keeps its cheapness and loses silence as sole carrier;
the rework-exhaustion flip to manual as an opt-out default performed and recorded by Drivr; resume
restores mode but not budget; the rework limit consolidated across all starter-shaped surfaces and
its two extension statements reconciled to one (`P12-GH-1`).

### M44: Rituals, Records, and the Normative Repairs

`P11-GH-3`'s Phase Completion Declaration at §5C Step 2 with a template; the HQ re-instantiation
ritual recorded; the context-exhaustion handoff artifact; `governance-propagation.md` amended per
ruling; the i18n paragraph; SN-30 Recs 1-2; the AOG section-numbering repair; **P12's own
`P11-GH-1` instance recorded against its carry-forward note** (SN-39); **a convention for the
decided-but-unconfigured state R6 created**, which must exist before E41.5 lands.

### M45: Trustworthy Completion Signal

`P10-GH-7` including its missing-Delivery-Notice branch; M39's judgment made able to reach a verdict
on the roster engine or its limit measured and stated, carrying M40's F5 constraint; `undetermined`
first-class. Bar stated before the work.

### M46: The Drivr MVP Surface

SN-36's binding built, with governance rules made unrepresentable in the interface; the board
vocabulary including `undetermined`; approval as formed-in-chat / carried-by-link; escalate-further
as a one-level control; SN-37's qualification gate with its bar set in the same work.

### M47: First Real Agentic Integration

One real epic, one real project, end to end through Drivr. Project selection recorded with reasoning.
Run record is the deliverable, including what the framework got wrong.

---

## Success Criteria

### P12 is Complete When:

1. ✅ **`epic_dev` and `epic_qa` are measured separately, against the incumbent**, and the record
   states which model each row should hold and why — ending the period in which one string filled
   both keys and hid a mergeable-work result and a fabrication behind the same value.
2. ✅ **Every row of the line-up that moves has passed its harness before it lands** — the four
   verification targets on E35.5's planted-defect back-test, the two lanes on the successful-nothing
   checks. `hq` moves freely because it does not move.
3. ✅ **The line-up is in `.ai-project.yml`, `model-routing-policy.md`'s mapping table and row P4 agree
   with it, and every level was warned before the five verification targets armed.**
4. ✅ **No path in `bin/` proceeds on absent gating evidence.** Sandbox absence aborts or is a
   recorded explicit opt-in; staging is epic-scoped; approval failure aborts; the `--admin` rung is
   gone or gated behind recorded human authorization; **`ai-project-init` never manufactures a
   governance agent**, and finds the real one.
5. ✅ **The suite asserts the guard rather than the defect** — the inverted tests at
   `bin/ai-project-git-merge:447-460` and `tests/test_init_agent_path.py` fail if the admin override
   is reachable unrecorded, or if a placeholder agent is installable at all.
6. ✅ **A child never holds merge authorization.** The parent performs the merge; the E40.5 guard is
   a backstop, and `merge-authorization.md` is the parent's record.
7. ✅ **Acceptance is distinguishable from absence** — a clean delivery still costs no artifact, and
   *reviewed and clean* is no longer indistinguishable from *nobody looked*.
8. ✅ **Exhausted rework flips the parent to manual by default**, Drivr records the flip, and the
   committed starter remains the source of truth.
9. ✅ **Resume restores the declared mode and does not reset the attempt counter**, and no control
   exists that promotes a manual-declared instance to agentic.
10. ✅ **One statement governs the rework limit**, reachable from every starter-shaped surface and
    every template, with a single answer to what a written extension grants.
11. ✅ **Phase closure has a pre-merge completion artifact** — a Phase Completion Declaration at §5C
    Step 2 with a template, marked `COMPLETE (awaiting consolidation)`, which is what the reviewing
    level receives; Step 9's declaration is unmoved.
12. ✅ **An HQ re-instantiation ritual exists in one normative place**, naming the committed artifacts
    a re-opened HQ session receives and where openers live.
13. ✅ **A context-exhaustion handoff artifact has a type and a template.**
14. ✅ **`governance-propagation.md` states only true constraints**, and each surviving prohibition
    stands on a stated reason rather than an expired one.
15. ✅ **The AOG's sections are uniquely numbered and uniquely titled**, and no cross-reference is
    ambiguous by title.
16. ✅ **The completion signal is trustworthy on the roster engine, or its limit is measured and
    stated**, with `P10-GH-7` closed or re-rated on evidence; `undetermined` is first-class and
    rendered.
17. ✅ **Drivr's MVP surface exists and makes at least three governance rules unrepresentable** — no
    agentic at Creation/HQ, no Phase/Milestone dispatch, no mode control implying merge authority.
18. ✅ **A model may not be swapped without passing a qualification suite whose bar was set before it
    ran**, and the suite detects *successful nothing* on the **itemized** historical set — **E33.2 Run A,
    E39.3, and E41.2's DEV RUN 2** *(corrected 2026-09-04 from "both recorded historical failures")*.
19. ✅ **One real epic in one real project has been carried end to end agentically by Drivr**, with
    its run record — including the framework's own failures during it — committed.
20. ✅ **The parked and deferred items are recorded with their triggers**, and llama.cpp is recorded
    **closed**, not parked.

---

---

## Acceptance Criteria

The CFO (Layer 8) will accept P12 complete when:

- [ ] `epic_dev` and `epic_qa` carry separate recorded measurements, each against the incumbent
      `qwen3-coder:30b` baseline, with the chosen value for each row and its reasoning committed
- [ ] `qwen3.6:27b` is declared in `opencode.json` and routable through the execution adapter;
      `qwen3.8:27b`'s presence is re-confirmed at run time, not inherited from this spec
- [ ] The four verification-target rows have E35.5 back-test results recorded (catches, false
      alarms, runs); the two lanes have successful-nothing results (tool rounds, files changed,
      claims resolving) — and any row that fails its harness is **escalated to the CFO, not
      silently dropped or silently landed**
- [ ] `.ai-project.yml` carries the ruled line-up; `model-routing-policy.md`'s mapping table **and**
      row P4 are updated in the same change, with row P4 recorded as **closed by CFO ruling** and
      the Change discipline satisfied **by decision, stated as such** — not filed as a same-tier
      refresh
- [ ] The `.ai-project.yml` edit merged **after** M42 closed, and every level was notified before it
      landed
- [ ] `bin/ai-project-orchestrator`'s Docker-absent path no longer reaches `shell=True` host execution
      as a silent fallback, and any surviving host path is declared and recorded per run
- [ ] The epic commit contains the epic's files, and the handling of out-of-scope modifications is
      specified rather than laundered
- [ ] `bin/ai-project-git-merge` aborts on approval failure; the `--admin` rung is removed or gated;
      the test at `:447-460` asserts the guard and fails if the override is reachable unrecorded
- [ ] `bin/ai-project-init` locates the governance agent after a real (non-`--skip-submodule`)
      install, has no stub-writing branch, and writes a `submodule_path` matching the fleet
      convention; `tests/test_init_agent_path.py` fails if a placeholder is installable
- [ ] The fleet is swept for existing 230-byte placeholder agents and each one is repaired or
      recorded, `social-stories-creator` included
- [ ] A recorded HQ or Phase determination names every caller of these three scripts, Drivr included
- [ ] The normative corpus states that the **parent** merges, and `merge-authorization.md` is
      addressed to the parent
- [ ] Accept-by-silence still produces no artifact on the happy path, and the acceptance record
      distinguishes a performed review from an absent one
- [ ] `.ai-project.yml` carries the rework-flip switch on the `cfo_review_gate` pattern, default
      enabled; Drivr performs and records the flip; `chat-hierarchy.md`'s committed-starter invariant
      is intact
- [ ] Resume is specified: restores the declared mode, never promotes, does not reset the counter
- [ ] The 3-attempt rule and its extension semantics appear once normatively and are reachable from
      all nine starter-shaped surfaces and all three starter templates
- [ ] `governance/templates/phase-completion-declaration.md` exists; PSG §5C Step 2 names it; §5C
      Step 6 reviews it; Step 9 is unchanged
- [ ] One normative document describes HQ re-instantiation, naming the artifacts and the opener
      directory; `hq-chat.md` and the opener template cite it rather than restating it
- [ ] A handoff artifact type and template exist, with the Drivr-side tracking boundary stated
- [ ] `governance-propagation.md`'s Constraints are true as measured on its amendment date, and each
      Non-Goal that survives carries its own reason
- [ ] `AI-OPERATING-GUIDELINES.md` sections are `1..n` with no duplicate number and no duplicate
      title; all internal cross-references updated; the version bumped
- [ ] A convention exists for recording a **decided-but-unconfigured** state, it is in place **before
      E41.5 lands**, and a reader of `.ai-project.yml` or `model-routing-policy.md` can tell which
      rows are decided-and-configured from which are decided-and-pending
- [ ] SN-30 Rec 1's checks exist under `tests/`; G1 and G2 live in a core document, not an epic spec
- [ ] `P11-GH-1`'s carry-forward note carries P12's own instance with its dated commits, its
      out-of-chain detection path, and **no ordinal** — and the note still records the gap as open and
      unscoped
- [ ] `P10-GH-7` is closed or re-rated with recorded evidence, including the missing-Delivery-Notice
      branch
- [ ] The completion judgment reaches a verdict on the roster engine, or a recorded measurement
      states the limit and why; M40's F5 (`Role.INSPECTION` unread by `_decide`) is addressed
      explicitly, not incidentally
- [ ] `undetermined` renders as its own board state and is never mapped to `in progress` or `blocked`
- [ ] Drivr's window matches SN-36's binding in its four regions, and three named governance rules
      have no representable control
- [ ] The qualification runner **distinguishes "measured and failed" from "could not measure", and
      records which** — a runner that cannot tell an empty credential store from an unreachable target
      reports a clean-looking negative and fails at the thing it was commissioned for
- [ ] The qualification suite's bar is committed **before** its first run, is relative to the
      incumbent, and flags **the itemized successful-nothing set — E33.2 Run A, E39.3, and E41.2's
      DEV RUN 2** — as failures when replayed. *(Corrected 2026-09-04: this line and the "twice" above
      named a pair while the M47 criterion below named three. **"Both" was a count standing where a
      list belongs** — Hard Constraint 1, in the phase's own success criteria. The **`llama3.1:8b`
      overpack is NOT in this set**: it is a context-declaration defect caught by the bar's context
      check, a different class from a run that reports success having done nothing.)*
- [ ] **The M47 proof run is checked by `bin/successful-nothing-instrument`**, and its run record
      carries **tool rounds, files changed and claims-resolution** rather than an exit status.
      *"A real epic ran agentically end to end" is not the claim; the claim is "…and we can show it
      did work."* Three recorded runs satisfy the first and fail the second — E33.2 Run A, E39.3,
      and E41.2's DEV RUN 2
- [ ] A real epic ran agentically end to end through Drivr in a named project, with the project
      choice, the run record, and the framework's own failures during it committed
- [ ] The full suite is green at delivery (**549 baseline on `master`**, no regressions, no skips
      introduced to route around changes) for changes touching this repo
- [ ] **`model_verification` is flipped from `advisory` to `blocking` as the LAST act of P12's
      closure, performed by HQ** (CFO decision 2026-08-27; ordering corrected 2026-08-27 after the
      Phase Chat found the deadlock). **P12 may not close without disposing of this**: flip it, or
      record why not. **SN-37's model-qualification gate resumes binding lineup changes at the same
      moment**, as does HQ's suspended fidelity condition.
      - **WHO: HQ, and only HQ.** `models.hq` and `models.creation` are `remote:claude-opus-5` and
        those chats self-report the same, so **HQ and Creation survive the flip. Every Phase,
        Milestone and Epic chat halts on it** — they run on Claude while the baseline configures
        `gpt-5.6-sol`, `deepseek-v4-pro` and `deepseek-v4-flash`.
      - **WHEN: after §5C's sequence is complete** — after the merge, the tag and the Phase-Closure
        Declaration. **Not "as part of" closure.** *The chat that runs the closure is the one the flip
        would stop*, so a flip mid-sequence halts the executor half-finished and the phase cannot
        close itself. **Deferring the flip to the boundary was right; placing it inside the boundary
        was not.**
      - **Consequence, stated rather than discovered:** after the flip, **all Phase, Milestone and
        Epic work must open in a harness providing the configured models.** That is the intended
        migration, and P13's chats are its first customers.
- [ ] The phase closure declaration restates the parked/deferred items with their triggers and
      records llama.cpp as **closed**

---

## Dependencies

### Internal
- **v8.0.0 corpus on `master`** — PSG v2.4.0 / AOG v2.10.1, suite **549/0** measured 2026-08-19
- **PSG §11.6.1** — the CFO as mandatory diff reviewer for HQ-authored deliveries; authorization is
  not review
- **`governance/systems/chat-hierarchy.md`** — the ratified execution matrix, *mode is not authority*,
  and the committed-starter invariant M43's flip must not break
- **SN-25** — one-level escalation; the terminus of M46's escalate-further control
- **Drivr at `~/soft-dev/drivr`** — scheduler, derived gate queue, headless surface, signed
  one-time-link approval, no inference of its own
- **M39's completion judgment and M40's F5** — the starting point and the constraint for M45
- **`P11-GH-1`** — mid-flight spec amendments do not reach working branches. **Fired four times in
  P11.** P12 runs six milestones with parallelism; the Phase Chat should expect it.

### External / CFO-side
- **The ruled model line-up (SN-38)** — five keys move, two are held pending M41's measurement.
  **`hq` is unchanged, which is why this HQ session did not halt.**
- **Availability of the four remote targets** — fable-5, GPT-5.6 Sol, Deepseek V4 Flash. HQ has
  verified **only** the local models on this host. **Availability of the remote three is unverified
  and is the CFO's**; M41 must confirm before it measures, not after.
- **Project selection for M47** — HQ does not pre-empt it
- **A reachable engine** for M45 and M47. An engine now resolves in the sandbox (M40, reversing M38)
  on the **reverse** endpoint shape from B2.1; this remains the phase's most fragile assumption
- **The hosted ComfyUI behind a fixed `ngrok` URL** — in spec as written; availability is explicitly
  the CFO's responsibility. §17.4 already **fails closed** here, recording intent and deferring
  rather than fabricating a render, and is a worked model for what P12 generalizes
- **The escalation terminus** (SN-36/37 Carry-Over 1) — when a blocker reaches the CFO and he cannot
  resolve it there, nothing is above him and the corpus has no name for that state. Rare; P12 does
  not depend on it; returned to him below

---

## Timeline

Planned 2026-08-19 → 2026-09-19, one month, **seven** milestones after the 2026-08-19 restructure. **The estimate is HQ's and is soft.** P11
planned four weeks, restructured to five milestones mid-flight, and closed in seventeen days. M47 is
the item with genuine schedule risk, because it is the only one whose success depends on a real
project having real work available.

---

## Reference

### Governing Steering Notes

| Note | Date | Carries |
|---|---|---|
| **SN-31** | 2026-08-18 | The spine; the four-instance fail-open finding; eight ratified decisions |
| **SN-32** | 2026-08-18 | The rework limit reaches one surface — filed as `P12-GH-1` |
| **SN-33** | 2026-08-18 | SN-30 unactioned; a Steering Note that reached its target and left no mark |
| **SN-34** | 2026-08-18 | `governance-propagation.md`'s Constraints are false |
| **SN-35** | 2026-08-18 | HQ re-instantiation — **corrected 2026-08-19, severity low** |
| **SN-36** | 2026-08-19 | Drivr's MVP surface, bound as a §7 visual |
| **SN-37** | 2026-08-19 | The model-qualification gate |
| **SN-30** | 2026-08-11 | The external assessment at issue #192, routed — triaged in P12's opening ruling |
| **SN-38** | 2026-08-19 | The ruled model line-up; SN-37's gate scoped to verification targets too; row P4 closed |

### Governing Rulings
- `.ai-project/artifacts/rulings/2026-08-19__ai-project-system-hq__ruling__p12-opening-and-sn-30-37-triage.md`
  — this phase's opening ruling
- `.ai-project/artifacts/rulings/2026-08-05__ai-project-system-hq__ruling__artifact-id-citation-forms.md`
  — the `GH-` prefix names **the phase that filed it, permanently**

### Key Reference Documents
- `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11__phase-closure-declaration.md`
- `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11__carry-forward-note__P11-GH-3-*.md`
- `.ai-project/artifacts/progress-digests/2026-08-17__hq__progress-digest.md`
- `.ai-project/artifacts/hq-openers/2026-08-19__hq-chat-opener.md`

### Binding Decisions (settled — NOT for re-debate)

Twenty-three decisions across SN-31 and SN-36/37 are **inputs, not proposals.** The load-bearing
ones, restated so a working chat need not chase them:

1. P12's spine is **completion**, not redesign.
2. The three execution-tier defects land **before the first real agentic integration** — a sequencing
   constraint, not a date.
3. Accept-by-silence is **tweaked, not retired**.
4. **The parent performs the merge**, not the child.
5. Exhausted rework **flips the receiving parent to manual**, opt-out default, Drivr records it.
6. **Resume restores, never promotes**; it returns the mode, not the budget.
7. A written extension grants **exactly one further attempt**, not a reset to three.
8. **`undetermined` is a first-class board state**, never folded into another.
9. The qualification bar is **relative and objective**, over a floor of tool rounds > 0 and files
   changed > 0. No subjective quality score.
10. **The chat is where judgment is formed; the signed link carries the key.** A chat reply is never
    authorization.
11. **The app writes committed artifacts; it does not hold state.**
12. `queued` is a property of **the lane**, not the epic.
13. **Escalate-further advances one level**, consistent with SN-25.
14. **In-app diff review is a nice-to-have**; §11.6.1 requires the review, not its location.
15. **Single-window is re-weighted toward central** — a deliberate change from P11, not drift.
16. **Generative reachability needs no governance change** — a hosted ComfyUI behind a fixed `ngrok`
    URL satisfies `comfyui_url` as specified.
17. **Unchanged, confirmed deliberately:** per-instance Execution Mode in the committed starter;
    *mode is not authority*; PSG §11.6.1.
18. **i18n:** user's language for chat and output; documentation in the original language; English
    authoritative; translation is a view.
19. **The model line-up is ruled** (SN-38): `creation`→fable-5, `phase`→GPT-5.6 Sol,
    `milestone`→Deepseek V4 Flash, `epic_manual`→`local:qwen3.8:27b`, `hq` unchanged.
20. **`milestone`→Deepseek V4 Flash is a POLICY-ROW change, not a mapping refresh**, and it **closes
    row P4**. Change discipline satisfied **by CFO decision**, which must be stated plainly rather
    than disguised as a same-tier refresh.
21. **SN-37's gate binds manual-chat verification targets as well as dispatch lanes** — CFO ruling;
    the Creation Chat's lanes-only proposal is **superseded**. **Two harnesses**, because the checks
    do not transfer.
22. **The evidence is collected first**, as an early step of P12, inserted after the phase opened —
    the CFO's call to make, and made.
23. **`epic_dev` and `epic_qa` are measured separately**, and the incumbent is measured to set the
    relative bar's baseline.
24. **No model swap lands until M42 closes.** A model change and a lane repair landing together makes
    the next failure unattributable.

### HQ Triage Decisions (2026-08-19 ruling)

Recorded in the ruling; summarized here. Six milestones with M42 gating M47 and M45 gating M46;
`P12-GH-1` and `P12-GH-2` filed; SN-30 Recs 1-2 placed in M44 and Recs 3-5 deferred with reasoning; the AOG
renumbering ruled **not** a hotfix; `governance-propagation.md` amended; governance auto-update
**split**, with only the updater half admissible and the reconciler half returned.

### Open Items — Returned to the CFO

Not decided here, and named so their status is explicit rather than unknown:

1. **The escalation terminus** — no defined disposition when a blocker reaches the top unresolved.
2. **Governance auto-update's two sub-questions** — what happens when an **apply** fails partway, and
   whether "mark superseded" narrows for explicitly immutable artifacts.
3. **Digest Open Decision 3** — the `local-agent-runner` retention **bar**, and model-watch cadence.
   SN-37's gate is the natural instrument for both; the numbers remain his. **Partially discharged by
   SN-38:** the gate's scope and its relative bar are now ruled, so what remains is the retention
   bar's threshold and the cadence at which re-tests fire.
4. **Digest Open Decision 4** — whether the `P11-GH-2` sibling pattern earns its own record. **Left
   to the CFO deliberately: HQ is the party it indicts.**
5. **Digest Open Decision 5** — the artifact-type inventory. `rulings` has **no template** despite
   being the most consequential class HQ produces, and `field-evidence` was minted by HQ without one.
   **Both implicate HQ**, which is why HQ places neither unasked.
6. **`model-routing-policy.md` row P4** — **CLOSED 2026-08-19 by CFO ruling** (SN-38), open on his
   timing since P10. Recorded here as discharged rather than deleted, so the item's history survives.
7. **The per-level model mapping** — **RULED** (SN-38); it was a plan and is now a decision, gated on
   M41's measurement. **The per-level *mode* mapping remains a plan** awaiting measurement, and is
   still his.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.3.3 | 2026-09-04 | **Reconciles the successful-nothing set, which this spec stated three different ways.** `:563` said the failure was recorded **twice**; the qualification criterion said *"flags **both** E33.2 and E39.3"*; the M47 criterion said **three** — *E33.2 Run A, E39.3, and E41.2's DEV RUN 2*. **The set is three, itemized.** *"Both"* and *"twice"* were **counts standing where a list belongs** — Hard Constraint 1, in this spec's own success criteria, which is why the discrepancy survived three amendments unnoticed. Also records that the **`llama3.1:8b` overpack is not a member**: it is a context-declaration defect caught by the bar's context check, a different class from a run reporting success having done nothing. **Escalated by the M46 Milestone Chat at planning close** (its Finding 4) after the Phase Chat's M46 spec propagated a fourth variant. |
| 1.3.2 | 2026-08-27 | **Amends the M46 role-identification input: the harness moved.** `ListAgents` now reports a session its own address; it did not on 2026-08-20. **The *requires-an-outside-correlator* claim dies** — it lived in messages and **never reached an artifact**, so nothing had to be unwound. **The registry requirement survives, re-justified**: names carry no role, which is what M46 must build against. Caught by the M41 chat running the command instead of asserting from memory, one turn short of shipping — `P12-GH-3` with a claim-in-flight about the environment as its dependent. **HQ had seen the self-address line hours earlier and amended nothing**, which is recorded here as the counter-example. |
| 1.3.1 | 2026-08-27 | **Ordering defect in v1.3.0's own criterion, found by the P12 Phase Chat and corrected.** The flip was placed *as part of* closure; **the Phase Chat runs the closure and is one of the chats the flip halts**, so a mid-sequence flip stops the executor half-finished and the phase cannot close itself. **Now the LAST act, performed by HQ** — the only level besides Creation that survives it. Deferring to the boundary was right; placing it *inside* the boundary was not. **No decision changed; only who acts and when.** |
| 1.3.0 | 2026-08-27 | **Two CFO decisions recorded with their consequences, not merely their content.** **(a) `model_verification` flips to `blocking` AT P12's CLOSURE**, as an acceptance criterion the phase cannot close without disposing of — deferred to the boundary **specifically so no chat halts mid-execution**, since Phase and Milestone chats run on Claude while the baseline configures GPT and Deepseek. SN-37's gate and HQ's suspended fidelity condition resume at the same moment. **The trigger is an EVENT, not a session's survival** — the failure mode this phase recorded twice. **(b) SN-42's shape: EXTEND M47 by CFO preference**, with a new milestone available as a justified escalation rather than a free choice. No epic added, no ordering change. |
| 1.2.0 | 2026-08-23 | **Two acceptance criteria added from the P12 Phase Chat's scope judgments, both accepted by HQ as properties the deliverable must already have rather than items beside it.** **M46:** the qualification runner must distinguish *measured and failed* from *could not measure* — SN-37's gate exists to detect *successful nothing*, and Drivr's `XDG_DATA_HOME` inheritance is that defect inside the gate's own infrastructure. **M47:** the proof run must be checked by `bin/successful-nothing-instrument`, because M47 dispatches through a parse M42 does not repair, so **the phase's proof could otherwise be an instance of the phase's organizing defect and its gate would pass it.** No epic, ordering or scope change. |
| 1.1.7 | 2026-08-21 | **Corrects (c) before merge, twice over.** The tie-break's published form was reported as *silently returns nothing*, then as *empty from `master`, correct from `milestone/M41`*; **HQ's own run returns a different valid-looking commit from each branch and empty from neither.** The mechanism is implicit `HEAD`, so the rule is **reader-dependent rather than broken** — and *a rule returning a different valid-looking answer to each reader shows nobody anything wrong*, which is worse than always-failing or empty. Generalizes: **any form resting on implicit `HEAD` is branch-dependent in a project whose sessions share a moving checkout.** Adds **(d)**: this is SN-36/37's ratified `undetermined` principle in a **fourth** place beside E41.2's S3 and E41.1's R6a — each a check whose silent failure reads as a meaningful value, all three repaired identically as *empty means undetermined and escalates*. |
| 1.1.6 | 2026-08-21 | Adds two consequences that **narrow the remedy space** for the M46 currency input. **Correctness is not safety** — *a fork does not have to be wrong to be a problem*; a remedy judged on whether forks produced bad output will conclude there is no problem. And **a tie-break computed from the shared state is self-legitimizing**: the role becomes acquirable by the act it governs, so a mistaken write retroactively legitimizes itself — **ruling out any tie-break derived from artifacts both forks mutate**, and placing exclusivity outside the state the forks write. Records the silent-failure hazard in such a rule's published form, where *empty* reads as *no holder* and both forks conclude they should act. |
| 1.1.5 | 2026-08-21 | **Extends the M46 currency input a third time, from a fork that AGREED.** A second M41 Milestone Chat authored four correct commits the incumbent did not write — and **caught a defect the incumbent missed.** The HQ fork was detectable because it contradicted; **an agreeing fork produces no signal and silently doubles a role's write surface**, staying invisible until two agreeing forks write different-but-both-plausible content into one artifact. Also records that **git attribution cannot answer it retrospectively** — one author across the entire repository, since the harness signs as the human — so **exclusivity may be the only remedy that works**, not merely the better one. Extends the existing input; no new gap record, no epic, ordering or acceptance-criterion change. |
| 1.1.4 | 2026-08-20 | Files **`P12-GH-4`** — the live inter-chat channel is in daily governance use and has **zero** occurrences in `governance/`. **Split:** the narrow half (one normative paragraph applying SN-36's ratified chat-reply principle to the channel) is **placed in M44**; the channel's wider design is **filed unowned**, triggered by M46's role registry or by any proposal to let something other than a committed artifact carry an acceptance. |
| 1.1.4 | 2026-08-20 | **Extends the M46 role-identification input with its currency half**, from a second live failure the same day: **two authentic HQ sessions ran concurrently**, root-caused by the CFO to a **VS Code layout change** that forked the session. A registry answers *which* session holds a role and **not how many do**; the outcome is **contradictory** normative artifacts (PR #226, closed unmerged) rather than lost ones, caught by a reader rather than a mechanism. Records that a staleness detector would **not** have caught it — the offending branch's merge-base was the current head and both merged artifacts were in its working tree. **The property is exclusivity, not only identification**, per the CFO's reading that Drivr *"will not allow concurrent chats touching the files all over."* Extends an existing input rather than filing a fifth gap record. No epic, ordering or acceptance-criterion change. |
| 1.1.3 | 2026-08-20 | **Discharges the three annotations HQ adopted on accepting M43/M44 and then deferred** — W3's sharpening, W4's understatement, X2's count — recorded in place rather than by rewrite. **The deferral's trigger was a session's continued existence, and it failed within four hours**; M44 spec v1.0.1 recorded the obligation as unowned, which is how it survived. Also adopts M44's two recommendations into M44's scope: **the HQ ritual must cover DEPARTURE**, on a live dated specimen, and **the Phase Completion Declaration is the backstop terminus** for deferred phase-spec corrections. Records the role-identification gap as an **M46 input**. No epic, ordering or acceptance-criterion change. |
| 1.1.2 | 2026-08-20 | Answers the P12 Phase Chat's M44 scope question. **PLACED in M44:** a convention for the decided-but-unconfigured state the R6 ruling created, with binding sequencing — it must exist before E41.5 lands, and a collision is an escalation rather than an improvisation. **DECLINED and filed instead:** derived-claim rot, as **`P12-GH-3`** — phase-scale, no bounded deliverable, and placing it would be the *"milestone things get put in"* pattern HQ has twice refused. |
| 1.1.1 | 2026-08-19 | Folds SN-39's Next Action into **M44**: record P12's own `P11-GH-1` instance against that gap record's carry-forward note, with its facts, its out-of-chain detection path, and an explicit instruction to cite by artifact and defect rather than by ordinal. **Records evidence; does not reopen the fix** — Decision 12 stands. |
| 1.1.0 | 2026-08-19 | **Restructured to seven milestones at CFO direction (SN-38), hours after opening.** A new **M41 — The Model Line-Up and Its Evidence** is inserted first; **the six original milestones shift +1**, mapping `M41→M42`, `M42→M43`, `M43→M44`, `M44→M45`, `M45→M46`, `M46→M47`. **Every P12 artifact predating this row cites the old numbers and was correct at its date**; the opening ruling carries the same mapping in its Amendment. The two original binding orders are preserved under the new numbers (`M42→M47`, `M45→M46`) and a third is added: M41's terminal epic is gated on M42's closure. Also records the ruled line-up, row P4's closure by CFO ruling, and SN-37's widened gate scope. |
| 1.0.0 | 2026-08-19 | Initial phase spec. Opens P12 on SN-31's spine per the 2026-08-19 HQ ruling; six milestones M42-M47; the four fail-open instances re-verified on `19c77ab` as the phase's organizing evidence. |
