---
milestone: M48
name: "Fleet Readiness, Proven by Running It"
phase: P13
status: planned
start_date: 2026-09-08
epics:
  - E48.1
  - E48.2
  - E48.3
  - E48.4
  - E48.5
  - E48.6
is_final: false
---

# Milestone M48 — Fleet Readiness, Proven by Running It

## Purpose

P12 proved one real Epic on `panchew-io`. M48 determines whether that path generalizes before P13
builds a surface on top of it. It prepares `footboard` and `home_finance` without overwriting their
active work, dispatches one real pre-existing Epic in each project through Drivr's proven headless
OpenCode-adapter path, and records enough independent evidence to tell whether useful work happened.

The milestone also establishes the first P13 cost-and-quality baseline. Usage is tied to reviewed
results, defects, rework, elapsed time, and human intervention. Missing telemetry is named rather
than estimated.

M48 may succeed with a named, understood run failure. It may not succeed with static readiness
alone, an exit code standing in for work evidence, or a failure hidden behind a green aggregate.

## Planning-Time Findings

Measured on 2026-09-08 against `ai-project-system` `cddbed7`, Drivr `114de1c`, `panchew-io`
`0b520aa`, `footboard` `d0c4c2a`, and `home_finance` `fbfc4b1`. These findings constrain the Epic
specs; execution must re-measure the relevant state at its own repository, ref, and date.

1. **The project model value is not an executable provider route.** The fleet projects declare
   `remote:deepseek-v4-flash`. Drivr passes the requested model directly to OpenCode, while the
   catalog exposes both `opencode/` and `opencode-go/` routes. M48 must record the executable route
   chosen for each attempt without creating M53's general model-selection mechanism.
2. **Credential lookup depends on the launch environment.** Drivr supplies a temporary
   `XDG_CONFIG_HOME` but inherits `XDG_DATA_HOME`. A confined value can hide the normal host
   credential store. Readiness records presence and the effective path category only; credential
   values never enter logs, artifacts, commands, or chat.
3. **The required projects are benched.** The fleet registry marks `footboard` and
   `home_finance` benched; the scheduler dispatches only active, enrolled projects. Any transition
   must be explicit and authorized. It may not be inferred from disk presence or from this spec.
4. **The proven path is the Drivr adapter, not a raw CLI replay.** P12 used
   `OpenCodeAdapter.execute(ExecutionRequest(...))` with `HostEnvironment` and an explicit route.
   A direct `opencode run` invocation alone does not prove reuse of that path.
5. **No Drivr code change is authorized by M48.** This boundary comes from the Phase Execution
   Chat Starter. Configuration, launch procedure, evidence capture, and project readiness are the
   work. If a required run needs new Drivr machinery, stop that path and escalate rather than
   absorbing it.
6. **Governance alignment is a migration, not a version edit.** `footboard` and `home_finance`
   are on v7.0.0 while the released framework is v9.0.0. `footboard` also has substantial dirty
   planning work. Each migration starts from an explicitly chosen integration baseline in an
   isolated worktree and preserves project configuration and in-flight work.
7. **`home_finance` remains invalid by the current schema.** It lacks
   `project.description`, uses `project.name: home_finance` against the hyphenated-slug rule, and
   has two schema-undefined-key warnings. No rename is authorized. The disposition must be an
   explicit, evidence-backed project supersession or a filed schema finding against the rule.
8. **The source suite mixes deterministic acceptance with a live endpoint.** With
   `visual_artifacts.enabled: true`, one integration test depends on local ComfyUI availability.
   M48 must make deterministic suite status stable and report live qualification separately.
9. **P12's raw OpenCode events expose the needed usage dimensions per step, not as a run
   summary.** Available fields include input, output, reasoning, cache read/write, and reported
   cost. M48 normalizes them without double-counting totals and preserves the raw source.
10. **`panchew-io` is verification evidence, not a third new run.** Its P12 proof is the first
    fleet run. M48 verifies that its committed `models:` block remains present and records its
    P12 baseline beside the two new runs; M53 owns making silent reversion impossible.

## Binding Constraints

1. **M48 gates M50.** No P13 UI work starts until M48 is accepted.
2. **No new surface and no Drivr implementation.** Use the P12 path as it exists. A machinery
   requirement is a named blocker and escalation.
3. **Real work only.** Each project run executes a pre-existing, parent-governed Epic that would
   have been done anyway. A synthetic probe may test transport but cannot satisfy the run.
4. **Evidence precedes judgment.** Before dispatch, commit the task-specific quality bar, record
   contract, selected repository/ref, route, and credential-presence check. Do not design the bar
   after seeing the result.
5. **The reviewer re-measures.** Preserve raw events and project commits. Record exit status, but
   never use it as the completion or quality signal.
6. **`undetermined` remains first-class.** Missing evidence, an unavailable provider, an
   authenticated allowance/resource refusal, and a confirmed execution blocker remain distinct.
7. **Secrets remain absent.** Check only credential-store/path presence and route availability.
   No credential value, token, secret-bearing environment value, or secret file content is read
   into a committed artifact.
8. **Dirty work is preserved.** In particular, do not modify or clean the existing `footboard`
   checkout. Use an isolated worktree from a recorded integration baseline and stage only intended
   migration/run changes.
9. **Repository claims are bounded.** Every validation claim states repository, ref, date,
   command/check, and result. "Suite green" never silently covers another repository.
10. **A named failure is an allowed result, not a waiver.** It must identify the failed layer,
    route, evidence, and consequence for P13. A failure does not permit M50 to open unless the
    Phase Chat accepts the resulting disposition.
11. **Local inference remains parked.** M48 may produce future re-entry evidence but does not
    dispatch locally or reopen llama.cpp/non-Ollama runtimes.
12. **Out-of-scope carry-forwards stay out.** Do not absorb `P12-GH-3`, the Delivery Notice
    location split, duplicate AOG Error Handling content, closed-phase sweep scope, `P11-GH-2`,
    or the untemplated `rulings` class.

## Phase Ruling on E48.1 Rework Exhaustion

**Issued 2026-09-08 by the P13 Phase Chat** in response to
`.ai-project/artifacts/escalation-notices/2026-09-08T00_00_00Z__P13-M48-E48.1__escalation_notice.md`.
These decisions amend E48.1's contract and are not delegated back for redesign.

1. **Quality-bar ownership stays in `ai-project-system`.** Each instantiated E48.4/E48.5
   `quality-bar.yml` is an M48 evidence artifact under
   `.ai-project/artifacts/agentic-runs/P13-M48-<E>/` in this repository. It cites the selected
   project's Epic spec and acceptance criteria by target-repository path, branch, and immutable
   commit SHA. E48.1 and the M48 proof Epics write no bar into a fleet project.
2. **Pre-dispatch ordering is proved in the M48 evidence graph and runtime record.** Before invoking
   Drivr, E48.4/E48.5 commit a dispatch manifest in `ai-project-system` that contains the bar commit
   SHA and target-project worktree HEAD. The bar commit must be an ancestor of the manifest commit.
   The invocation records that manifest SHA and Drivr's runtime `dispatched_at` (or, for the direct
   P12 adapter path which has no scheduler timestamp, the supervisor's UTC `started_at` captured
   immediately before `OpenCodeAdapter.execute`). Missing ancestry, manifest identity, target HEAD,
   or runtime start time is fail-closed. Git author dates are never ordering evidence.
3. **The event adapter is source-side; no Drivr change is authorized.** E48.1's
   `bin/drivr-events-to-instrument` maps OpenCode `read`→`read_file`, `write`→`write_file`,
   `edit`→`edit_file`, and `bash`→`run_command`. `glob`, `grep`, `todowrite`, and any unknown tool
   remain executed rounds but are not relabeled as mutating calls. C-B uses the dispatch record's
   authoritative `files_changed` list/count through the instrument's `--files-changed` input; it is
   not inferred from mapped calls. Missing or malformed tool/result/files evidence yields
   `undetermined`/`ERROR`, never a fabricated zero or pass. Tests use the real P12 Drivr record
   shape and cover known, unknown, denied/error, missing, and malformed events.
4. **The proposed Structural visual uses an immutable hosted commit permalink.** Commit the Mermaid
   diagram as a sibling `.mmd` file first, push that commit, and bind the proposed visual to the
   exact GitHub `blob/<40-character-commit-SHA>/...mmd` URL. A branch URL, local path, deferred link,
   or currently unresolved URL is not a permalink. The implemented binding remains separately due
   in the Delivery Notice.
5. **Minimal quarantine hardening belongs to E48.1.** This does not absorb M49's broader
   future-commit protection. The fixed root is
   `${XDG_STATE_HOME:-$HOME/.local/state}/ai-project-system/m48-quarantine`; the implementation
   resolves canonical paths, refuses a root or destination inside any Git worktree, rejects
   symlinks and path traversal, restricts run/file components to `[A-Za-z0-9._-]+`, creates
   directories mode `0700` and files mode `0600`, and moves atomically without following links.
   The committed notice contains only a logical quarantine ID, SHA-256, redacted region metadata,
   and scan disposition — never an absolute host path or matched content. Scanner error, unsafe
   destination, or inability to apply those controls is fail-closed.

**Written `+1` extension.** PSG §11.6 permits exactly one further attempt after exhaustion when a
written decision grants it. This ruling grants E48.1 **one final rework attempt only**, solely to
apply the five decisions above and synchronize its spec/Starter. It does not reset the budget and
does not authorize execution. If that delivery is not acceptable, no additional rework is
available; M48 must escalate again.

### Final disposition — amend then close

**Issued 2026-09-08** in response to the final exhausted-rework notice
`.ai-project/artifacts/escalation-notices/2026-09-08T02_00_00Z__P13-M48-E48.1__escalation_notice.md`.
The Phase Chat selects **amend-then-close**. E48.1 is contract-only: it delivers the reusable
run-record, quality-bar and dispatch-manifest schemas; adapters and tests; invocation and retention
procedures; `panchew-io` baseline extraction; and eligibility record. It does **not** instantiate or
commit either target's task-specific `quality-bar.yml` or dispatch manifest. E48.4 and E48.5 each
instantiate and commit those artifacts on their own source-repository Epic branch before dispatch.

This higher-authority disposition supersedes four stale clauses in E48.1 spec v1.5.0 without a
further child edit: Context lines 59–61, Goal 3 line 76, Definition of Done lines 332–335, and
Acceptance Criteria lines 361–362. Wherever those clauses say E48.1 produces or commits an
instantiated task-specific bar, read **"E48.1 commits the reusable two-layer quality-bar contract
and enforcement schema; E48.4/E48.5 instantiate and commit each selected Epic's bar before its
dispatch."** No other E48.1 term is changed. This is a parent disposition after exhausted rework,
not another attempt or a waiver of the pre-dispatch bar.

## Phase Ruling on E48.2 Rework Exhaustion

**Issued 2026-09-08 by the P13 Phase Chat** in response to
`.ai-project/artifacts/escalation-notices/2026-09-08T03_00_00Z__P13-M48-E48.2__escalation_notice.md`.
The remaining defects are bounded representation errors, not an open design question. The Phase
Chat grants one written `+1` under PSG §11.6 solely to apply this exact correction:

1. The fixed `live` result schema is
   `{"outcome": <pass|fail|skip|deferred|config-error|undetermined>, "helper_exit": <int|null>,
   "environment": {"enabled": <bool>, "comfyui_url": <str>}, "reason": <str>}`.
2. `helper_exit` is an integer only when the helper process returned that code. It is `null` when no
   helper return code exists. Explicit opt-out therefore yields `outcome: skip`,
   `helper_exit: null`, and a reason naming the opt-out; a failure to start the helper yields
   `outcome: undetermined`, `helper_exit: null`, and the non-secret failure reason.
3. Existing returned-code mappings remain unchanged: `0`→`pass`, `4`→`fail`, `2`→`skip`,
   `5`→`deferred`, and `3`→`config-error`. Any other returned integer maps to `undetermined` while
   preserving that integer in `helper_exit`.
4. Every outcome enumeration, DoD/Starter summary, test obligation, and the proposed Mermaid visual
   must show all six outcomes. The visual mapping must include `other`→`undetermined` and must not
   imply a fabricated helper exit for opt-out.

This is exactly one final planning attempt, not a reset to three. It authorizes edits only to the
E48.2 spec, synchronized Starter, and proposed `.mmd` needed to apply the four clauses above. The
already accepted direct-helper path, delivery-report consumer, deterministic-only gate exit,
canonical-ref procedure, bounded claims, and diagram routing are closed and may not be redesigned.
No execution or merge is authorized. If the `+1` delivery is not acceptable, no further rework is
available and M48 must escalate again.

### Final E48.2 disposition — amend then close

**Issued 2026-09-09** in response to the final exhausted-rework notice
`.ai-project/artifacts/escalation-notices/2026-09-09T00_00_00Z__P13-M48-E48.2__escalation_notice.md`.
The Phase Chat selects **amend-then-close**. E48.2 spec v1.4.0 and its synchronized Starter are read
under these exact higher-authority replacements:

1. Wherever a live-outcome enumeration omits `undetermined`, read
   **`pass | fail | skip | deferred | config-error | undetermined`**. Wherever the deterministic-only
   gate rule lists non-pass live outcomes, it includes `undetermined`: none of `fail`, `skip`,
   `deferred`, `config-error`, or `undetermined` changes `bin/suite-gate`'s deterministic exit.
2. Wherever a returned-code mapping summary stops at the five known codes, append: **any other
   returned integer maps to `undetermined` and is preserved in `helper_exit`; no helper return code
   maps to `helper_exit: null`, with explicit opt-out producing `skip` and helper-start failure
   producing `undetermined`.**
3. Wherever a regression list names only available, unavailable, disabled/opt-out, locked, and
   config-error cases, replace it with this required set: **available/pass; unavailable/exit-4
   `fail`; disabled/exit-2 `skip`; explicit opt-out `skip` with `helper_exit: null`; locked/exit-5
   `deferred`; config/exit-3 `config-error`; unknown returned integer `undetermined` preserving the
   integer; helper-start failure `undetermined` with `helper_exit: null`; and deterministic-result
   reproducibility independent of endpoint availability.** Disabled and explicit opt-out are
   separate cases, not alternatives.

These replacements apply to E48.2 v1.4.0 Goal 4, D2/D3/D4 summaries, Deliverables, Definition of
Done, Acceptance Criteria, Execution Notes, and the corresponding Starter summaries and D3 line.
The v1.4.0 core schema, detailed D2 mappings, proposed Mermaid visual and immutable binding are
already correct and remain unchanged. No other E48.2 term is changed.

This is a parent disposition after all rework was exhausted, not another attempt. E48.2 planning is
accepted under this disposition by **P13 Phase Chat, OpenCode session (`remote:gpt-5.6-sol`)**. It
authorizes no E48.2 execution or merge. E48.3 may now be submitted alone for planning review.

## Phase Ruling on E48.3 Rework Exhaustion

**Issued 2026-09-09 by the P13 Phase Chat** in response to
`.ai-project/artifacts/escalation-notices/2026-09-09T01_00_00Z__P13-M48-E48.3__escalation_notice.md`.
The Phase Chat grants one written `+1` under PSG §11.6 to apply the fixed contract below. These are
implementation terms, not choices delegated back for redesign.

### Enrollment state and evidence

1. `tracking`, `pushed`, and `ref_equal` are each `true | false | null`. `null` means the observation
   could not be made; it is never converted to `false`. `pushed` means the target branch was observed
   on the remote, not merely that a push command was attempted.
2. Query mode is read-only and exits `0` for freshly verified `delivery-ready` or recorded
   `local-only`; every `not-delivery-ready` result exits `1`. It checks both fetch and push URLs. A
   credential-bearing supplied or stored URL yields `not-delivery-ready`/`invalid-url`, `remote:
   null`, exit `1`, and no transport invocation.
3. Query precedence is fixed: no `origin` and no record→`absent`; no `origin` plus a valid local-only
   record→`local-only`; `origin` plus any local-only record→`verification-failure` conflict; `origin`
   without a local-only record→fresh read-only three-part verification. A persisted record never
   asserts delivery readiness.

### Durable local-only lifecycle and recovery

4. Mutation requires a clean worktree so no unrelated path can be committed. `--local-only` is
   allowed only without `origin`; it writes `.ai-project/enrollment.yml`, stages only that path, and
   commits it as `chore: record local-only enrollment`. Repeating it with the same valid record and
   no `origin` is a no-op success. With `origin`, it fails without mutation.
5. `--remote` validates the requested URL and any existing `origin` before mutation. A different
   existing URL fails without mutation. With a local-only record, it then requires a clean worktree,
   removes only that record, and commits the removal as `chore: transition to remote enrollment`;
   that new `HEAD` is the SHA pushed and verified. A same-URL `origin` is reverified. Once a push
   changes remote state, failure never deletes or rewinds the remote. Every post-failure boolean
   preserves its observed value, and retry resumes from the retained local/remote state.
6. `bin/ai-project-init` performs its final agent amend before forwarding to enrollment. Option
   validation happens before project creation: both enrollment options→usage exit `2`; otherwise an
   enrollment option combined with `--skip-git`→usage exit `3`. These checks have that precedence.

### Diagnostic classification and visual

7. Classification uses redacted, lowercased stderr. Compute refusal-token and credential-absence-
   token matches independently: both or neither→`undetermined`; refusal only→`authenticated-refusal`;
   credential-absence only→`credential-absent`. `repository not found` alone is not refusal evidence.
   Known non-auth Git failures and failed three-part checks remain `verification-failure`.
8. The visual sends query through stored-URL credential inspection before any absent/local-only/
   verification branch and shows the fixed artifact lifecycle and nullable observations.

### Delivery Notice boundary

9. E48.3 does not close or redesign the already-recorded `P10-GH-4` template lifecycle gap. Its
   Delivery Notice is created and committed once before review and is never updated after merge. It
   uses `status: delivered` to mean delivered for review; `completion_notice_timestamp`,
   `review_decision_timestamp`, and unknown PR/merge fields are `null`; `target_branch` is
   `milestone/M48`. The body states execution complete, no PR or merge yet, and review/authorization
   pending. On a clean path, parent merge plus named acknowledgment records acceptance separately.

This ruling grants exactly one final planning attempt, not a reset to three. It authorizes edits only
to the E48.3 spec, synchronized Starter, and proposed Mermaid visual needed to carry these nine
terms. The exclusive delivery-ready predicate, command modes, initializer placement, prerequisite
verification, eligibility boundary, and secret prohibition are closed. No execution or merge is
authorized. If the `+1` is not acceptable, no further rework is available and M48 must escalate
again.

## Final Phase Disposition on E48.3 Planning

**Issued 2026-09-09 by the P13 Phase Chat** in response to
`.ai-project/artifacts/escalation-notices/2026-09-09T02_00_00Z__P13-M48-E48.3__escalation_notice.md`.
The written `+1` is exhausted. Phase selects **amend then close** because the five remaining findings
are enumerable omissions from the fixed ruling above, not open design questions. The following
higher-authority replacements supersede the corresponding stale E48.3 v1.4.0 spec, Starter, and
proposed-visual clauses without another child edit.

1. **Every mutation requires a clean worktree.** This includes `--local-only`, transition from a
   local-only record, and ordinary `--remote` enrollment when no local-only record exists. URL and
   existing-origin validation remain read-only preflight; after they pass, any path that would add or
   change `origin`, set upstream, create/remove the enrollment record, commit, or push rejects a
   dirty worktree before its first mutation.
2. **Credential inspection precedes every query branch.** Query first inspects both stored fetch and
   push URLs when `origin` exists. If either is credential-bearing, the result is
   `not-delivery-ready`/`invalid-url`, `remote: null`, exit `1`, with no transport invocation,
   regardless of local-only-record presence. Only credential-safe stored URLs reach the four-case
   absent/local-only/conflict/fresh-verification table.
3. **Read the proposed visual with this exact mutation route replacing its stale `--remote` edges.**
   Every `--remote` path enters requested-URL and existing-origin credential/compatibility preflight,
   then the blanket clean-worktree gate. A valid local-only record is removed alone and committed as
   `chore: transition to remote enrollment`; that resulting `HEAD` is then used for origin/upstream
   mutation as needed, push, and three-part verification. Without a local-only record, the same route
   performs origin/upstream mutation as needed, then pushes and verifies the current `HEAD`. Any
   post-push failure retains local and remote state and observed nullable booleans; retry re-enters
   preflight from that retained state. Query still enters stored-URL credential inspection before
   any four-case branch and never enters mutation.
4. **Regression and DoD coverage is explicit and conjunctive.** It covers query exit `0` for freshly
   verified `delivery-ready` and valid recorded `local-only`; exit `1` for every
   `not-delivery-ready` result; independent stored fetch/push credential detection with no transport;
   all four query-precedence cases plus credential-bearing-origin combinations; dirty-worktree
   rejection before every mutation mode; exact-path staging and exact commit messages for creation
   and transition; transition-commit `HEAD` as the pushed/verified SHA; both initializer-option usage
   exits and their precedence over project creation; refusal-only, credential-absence-only, both,
   neither, repository-not-found-only, and known non-auth classifier cases; and retained-state retry
   after post-push failure.
5. **No settled surface is delegated.** E48.3 uses the fixed query, `--local-only`, and `--remote`
   command modes in the enrollment helper; `bin/ai-project-init` forwards an enrollment mode only
   after its final agent amend; and the pre-review Delivery Notice uses the fixed path, nullable
   schema, `status: delivered`, `target_branch: milestone/M48`, and append-only lifecycle in term 9.
   Execution planning may choose implementation mechanics only inside these boundaries.

No other E48.3 term changes. The nullable evidence schema, query exits, committed local-only
lifecycle, initializer usage codes, ambiguity-first classifier, exclusive delivery-ready predicate,
prerequisite and eligibility boundaries, secret prohibition, and bounded Delivery Notice convention
remain accepted as written. `P10-GH-4` remains open and outside E48.3.

This is a final parent disposition after all rework was exhausted, not another attempt or waiver.
E48.3 planning is accepted under this disposition by **P13 Phase Chat, OpenCode session
(`remote:gpt-5.6-sol`)**. It authorizes no E48.3 execution or merge. E48.4 may now be submitted alone
for planning review; its execution remains barred until every parent prerequisite and explicit
project-eligibility decision is satisfied.

## Planned Epics

Six Epics. E48.1, E48.2, and E48.3 may proceed in parallel. E48.4 and E48.5 require E48.1's
accepted pre-run contract, deterministic acceptance from E48.2, and explicit project eligibility.
E48.6 requires both project attempts and their independent reviews.

- **E48.1 — Operational Evidence and Run Gate**
- **E48.2 — Deterministic Acceptance, Live Qualification Separate**
- **E48.3 — Enrollment Completes the Delivery Substrate**
- **E48.4 — Footboard Readiness and Real Epic Run**
- **E48.5 — Home Finance Disposition and Real Epic Run**
- **E48.6 — Fleet Cost-and-Quality Baseline**

Every Epic Chat is manually supervised. The real project work inside E48.4 and E48.5 is agentic;
the Epic Chat collecting and judging that evidence remains manual. Mode is not authority.

## Epic Detail

### E48.1 — Operational Evidence and Run Gate

Define and prove the common pre-run contract before either project result is visible.

**Scope and deliverables**

- A versioned run-record contract covering every attempt: task/project/level, repository and
  branch/ref, Drivr ref, declared model identity, executable provider route, effective launch
  environment category, credential-store presence without values, timestamps/elapsed time, raw
  event source, completion judgment, work-evidence counts, review result, defects, rework, human
  intervention, and missing-data fields.
- A tested normalization path for uncached input, cache creation/write, cache reads, output,
  separately reported reasoning, and provider-reported cost. Raw counts and economic evidence
  remain separate; overlapping provider totals are not summed twice.
- A committed reusable two-layer quality-bar contract and enforcement schema. E48.4/E48.5 each
  instantiate and commit the selected project Epic's task-specific bar before its dispatch.
- A reproducible adapter-level invocation procedure using Drivr's `OpenCodeAdapter`, not a raw CLI
  substitute, including presence-only route and credential checks.
- Re-measurement that `panchew-io`'s seven-key `models:` block remains committed, plus extraction
  of the available P12 run baseline under the new contract. Missing P12 fields stay missing.
- The explicit authority record required to move each target from benched to eligible, or a named
  block if that authorization is not supplied. This Epic does not infer or grant eligibility.

**Acceptance criteria**

- [ ] E48.1's reusable contract/schema is committed; E48.4/E48.5 are fail-closed until their own
      instantiated task-specific quality bar is committed before dispatch
- [ ] Normalization is tested against representative complete, partial, and missing telemetry
- [ ] Route identity and model identity are distinct in every record
- [ ] Credential diagnostics prove presence only and emit no values
- [ ] The invocation exercises `OpenCodeAdapter.execute`
- [ ] `panchew-io` model persistence and available P12 baseline are independently verified
- [ ] Each benched target has explicit human transition authority recorded, or remains blocked with
      that missing authority named

### E48.2 — Deterministic Acceptance, Live Qualification Separate

Make "suite green" reproducible while preserving honest evidence about the configured live visual
endpoint.

**Scope and deliverables**

- Separate deterministic acceptance from live ComfyUI qualification so identical source and an
  unchanged declared test mode produce the same acceptance result.
- Keep live endpoint testing available and default behavior explicit; do not convert an expected
  live check into an unreported skip or mock.
- Report deterministic test totals and live qualification status independently, including the
  environment and reason for any intentional skip.
- Add regression coverage for endpoint available, unavailable, and explicitly skipped states.

**Acceptance criteria**

- [ ] Deterministic acceptance no longer depends on machine-local endpoint availability
- [ ] Live qualification remains runnable and is never represented as deterministic coverage
- [ ] Pass, fail, and skip semantics are explicit and tested
- [ ] P13 delivery reports can state one unambiguous source-suite gate

### E48.3 — Enrollment Completes the Delivery Substrate

Close SN-45: initialization currently creates a local repository but no remote enrollment path,
even though governed delivery depends on PRs.

**Scope and deliverables**

- Add an explicit, fail-closed enrollment step or option to the supported initialization path that
  can establish and verify the configured remote/tracking relationship without embedding
  credentials.
- Preserve an intentional local-only choice as an explicit result rather than silently treating it
  as fleet-ready.
- Cover remote present, remote absent, invalid/failing remote, and intentional local-only cases.
- Document the boundary between creating/configuring a remote and project eligibility in the fleet
  registry. Enrollment does not auto-activate or dispatch a project.

**Acceptance criteria**

- [ ] A newly initialized project cannot be reported delivery-ready without a verified remote or
      an explicit local-only disposition
- [ ] Diagnostics contain no credential values
- [ ] Enrollment alone changes neither fleet eligibility nor execution state
- [ ] Automated tests cover all supported outcomes

### E48.4 — Footboard Readiness and Real Epic Run

Migrate `footboard` safely and execute one real pre-existing Epic through the accepted M48 run
gate.

E48.4 is an `ai-project-system` proof-and-coordination Epic, following P12 E47.3's pattern. Its
record and Delivery Notice land in this repository. It does not become `footboard`'s parent:
project-side migration and product work are planned, accepted, and merged by `footboard`'s own
hierarchy, with cross-project direction routed through the governed System HQ channel when needed.

**Scope and deliverables**

- Record the chosen integration baseline and preserve the dirty governance-bump/planning checkout
  untouched by using an isolated worktree and branch.
- Reconcile governance pin, installed agent copies, adoption stamp, and project configuration as
  an explicit v7.0.0-to-v9.0.0 migration; remove no project-owned setting by template overwrite.
- Validate the project and verify its remote/tracking and explicit fleet eligibility.
- Select a real Epic already present in `footboard`'s accepted Milestone plan. Its current Epic spec
  and Starter must be produced or confirmed and accepted by `footboard`'s own parent chain before
  dispatch; do not invent proving work inside M48.
- Dispatch it headlessly through Drivr's adapter with the precommitted quality bar and evidence
  contract, then preserve raw evidence and project commits.
- Obtain independent project-level review and record defects, rework, elapsed time, intervention,
  completion judgment, and all available usage dimensions.

**Acceptance criteria**

- [ ] Existing dirty work is byte-for-byte outside this Epic's changes and remains unstaged
- [ ] Governance migration is complete and validated from the recorded integration baseline
- [ ] The benched-to-eligible transition has explicit human authority recorded
- [ ] A real Epic accepted by `footboard`'s own parent was attempted through the adapter path with
      an explicit route
- [ ] Independent evidence shows useful work, or a named and understood failure explains why not
- [ ] The record contains no credential value and estimates no missing telemetry

### E48.5 — Home Finance Disposition and Real Epic Run

Resolve `home_finance`'s schema state explicitly, migrate it safely, and execute one real
pre-existing Epic through the accepted M48 run gate.

E48.5 is an `ai-project-system` proof-and-coordination Epic. Its schema-disposition record, run
record, and Delivery Notice land in this repository. It does not become `home_finance`'s parent:
project configuration, migration, and product work remain under `home_finance`'s hierarchy, with
cross-project direction routed through System HQ when needed. M48 may file a schema finding against
the rule; it does not amend the source schema.

**Scope and deliverables**

- Decide the `project.name: home_finance` conflict with evidence: either a separately authorized,
  recorded project supersession or a filed schema finding against the rule. No silent rename is
  permitted; M48 does not amend the source schema.
- Resolve the absent description and explicitly dispose of the two schema-undefined-key warnings;
  report the exact post-change validator result.
- Record the accepted integration baseline and reconcile governance pin, installed agent,
  adoption stamp, and project configuration as a v7.0.0-to-v9.0.0 migration.
- Select a real Epic already present in `home_finance`'s accepted M1 plan. E1.1 is already delivered
  and cannot be replayed as new proof; a remaining planned Epic must receive its own accepted spec
  and Starter from `home_finance`'s parent chain before dispatch.
- Dispatch it headlessly through Drivr's adapter with the precommitted quality bar and evidence
  contract, then preserve raw evidence and project commits.
- Obtain independent project-level review and record defects, rework, elapsed time, intervention,
  completion judgment, and all available usage dimensions.

**Acceptance criteria**

- [ ] Every original schema error and warning has an explicit recorded disposition
- [ ] No project rename occurs without separate human authorization and a supersession record
- [ ] Governance migration is complete and validated from the recorded integration baseline
- [ ] The benched-to-eligible transition has explicit human authority recorded
- [ ] A remaining real Epic accepted by `home_finance`'s own parent was attempted through the
      adapter path with an explicit route; delivered E1.1 was not replayed
- [ ] Independent evidence shows useful work, or a named and understood failure explains why not
- [ ] The record contains no credential value and estimates no missing telemetry

### E48.6 — Fleet Cost-and-Quality Baseline

Consolidate the P12 `panchew-io` evidence and both M48 attempts into the record that decides whether
the proven path generalized.

**Scope and deliverables**

- A raw-data-derived baseline for all three pilots. Per attempt, report context composition where
  attributable; uncached input; cache creation/write; cache reads; output; reasoning; elapsed time;
  provider-reported cost or allowance evidence; reviewed result; defects; rework; and human
  intervention.
- Independent re-measurement from raw events and repository commits rather than acceptance of each
  executor's summary.
- A comparability statement: task, model/provider, and context differences are visible so none is
  presented as a context-saving effect.
- A readiness result per project and one bounded fleet conclusion: `n=3`, or the named failure and
  its consequence. A partial result does not silently become `n=3`.
- A list of what the framework got wrong, what data was unavailable, and which findings block M50,
  re-scope later P13 work, or remain owned by later milestones.

**Acceptance criteria**

- [ ] Every normalized count is reproducible from a cited raw source
- [ ] Reviewed quality evidence appears beside usage evidence for each project
- [ ] Missing fields are `unavailable` with reasons, never zero-filled or estimated
- [ ] Subscription allowance pressure and cash/API cost remain distinct
- [ ] The fleet conclusion is no larger than the evidence and explicitly states whether M50 may open

## Dependencies and Prerequisites

**Satisfied phase entry conditions**

- Drivr has private `origin`, and `main` tracks `origin/main`.
- The three pilot projects' model additions are committed and pushed.
- `models.creation: remote:gpt-6` is committed and the source suite baseline is 774 passing.

**Internal ordering**

- E48.1, E48.2, and E48.3 may run in parallel.
- E48.4 and E48.5 require accepted E48.1 evidence/quality contracts, accepted E48.2 deterministic
  suite semantics, explicit fleet eligibility, and their own parent-governed real Epic.
- E48.6 requires completed attempts and independent reviews from E48.4 and E48.5.

**External authority and environment**

- Human authorization is required for fleet-registry eligibility changes, project/schema
  supersession, Stage-2 acceptance, and merge authorization. Cross-project direction is routed by
  a System HQ request/response and, where work belongs to another governed project, a steering note
  into that project's HQ; routing never commands or substitutes for that project's acceptance.
- The intended headless launch environment must expose the selected provider route and the normal
  host credential store. Presence may be tested; values may not be printed.
- Provider allowance/resource availability is external. An authenticated refusal is recorded as
  such and not relabeled as a credential failure.

## Definition of Done

- [ ] All six M48 Epics are delivered, accepted, and merged through the `ai-project-system` M48
      gate; every completed project-side change and real Epic delivery is separately accepted and
      merged through the owning project's hierarchy, or the named failure records why that delivery
      could not complete
- [ ] `footboard` and `home_finance` each attempted one real pre-existing Epic headlessly through
      Drivr's P12 adapter path, or a named and understood failure explains why not
- [ ] `panchew-io`'s model block is verified present and its P12 proof is normalized without
      invented data
- [ ] Provider routes and credential-store presence are resolved in the intended launch environment
      without exposing values
- [ ] Governance migrations use recorded integration baselines and preserve in-flight work
- [ ] `home_finance`'s two errors and two warnings have explicit dispositions; no silent rename
- [ ] SN-45's enrollment gap is closed and tested
- [ ] Deterministic source-suite acceptance is stable; live visual qualification is separate
- [ ] Cost and quality are reported together from raw evidence, with missing fields named
- [ ] The fleet conclusion states `n=3` or names and explains every failure
- [ ] Repository/ref/date and verification command are stated for each delivery claim
- [ ] The Phase Chat explicitly decides whether M48's evidence opens M50

## Milestone Acceptance Criteria

- [ ] Static validation is not used as proof that dispatch works
- [ ] A reader can distinguish work evidence, completion judgment, provider/credential state,
      reviewed quality, and economic evidence for every attempt
- [ ] No exit code or executor prose stands in for independent evidence
- [ ] `undetermined` and unavailable data remain visible rather than rendered as success or progress
- [ ] No secret value appears in committed changes, logs, or delivery artifacts
- [ ] Existing user work in all pilot repositories remains intact
- [ ] Claims do not exceed the repositories, refs, dates, and attempts actually reviewed

## Out of Scope

- Drivr UI, conversational execution, Phase/Milestone dispatch, eligibility-lever implementation,
  model-selection UI, or a general provider-route resolver
- New Drivr execution machinery
- Local inference or any non-Ollama runtime
- Git-history investigation or rewriting
- General corpus cleanup or the six explicitly carried unowned findings
- Automatic governance updater completion; M48 records current compatibility/readiness only

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.6.0 | 2026-09-09 | Final E48.3 exhausted-`+1` disposition: amend then close. Supersedes the five stale E48.3 v1.4.0 surfaces with exact blanket clean-worktree, credential-first query precedence, complete mutation-visual route, regression/DoD matrix, and closed command/path/schema replacements. Accepts E48.3 planning under the parent disposition; authorizes no execution or merge and permits E48.4 planning review next. |
| 1.5.0 | 2026-09-09 | Resolves E48.3's exhausted-rework escalation with one written `+1` and a fixed enrollment state machine: nullable independent observations; read-only query precedence and exits; credential-safe stored URLs; committed local-only/transition lifecycle; retained-state retry; exact init usage exits; ambiguity-first diagnostic classification; synchronized visual; and a bounded, append-only pre-review Delivery Notice convention that does not claim to close `P10-GH-4`. No execution, merge, redesign, or budget reset is authorized. |
| 1.4.0 | 2026-09-09 | Final E48.2 exhausted-rework disposition: amend then close. Supersedes stale five-outcome and incomplete regression summaries in E48.2 v1.4.0/Starter with exact six-outcome, unknown-return, non-invocation, and complete regression replacements. Accepts E48.2 planning under the parent disposition; authorizes no execution or merge and permits E48.3 planning review next. |
| 1.3.0 | 2026-09-08 | Resolves E48.2's exhausted-rework escalation with exactly one written `+1`. Fixes the live-result contract to six outcomes including `undetermined`, makes `helper_exit` integer-or-null without fabricated non-invocation evidence, freezes known/unknown mappings, and requires the synchronized Starter and visual to mirror the contract. No redesign, execution, merge, or budget reset is authorized. |
| 1.2.0 | 2026-09-08 | Final exhausted-rework disposition: amend then close. Makes E48.1 contract-only in its own Epic Detail and explicitly assigns instantiated target bars/manifests to E48.4/E48.5. Supersedes the four stale E48.1 v1.5.0 prose clauses by exact replacement from this higher-authority contract; no further child rework, no waiver, and no execution authorization. |
| 1.1.0 | 2026-09-08 | Resolves E48.1's exhausted-rework escalation at the Phase-owned contract boundary. Rules source-repository quality-bar ownership, source-graph manifest ancestry plus runtime dispatch time, a complete source-side Drivr-event mapping with authoritative `files_changed`, immutable commit-permalink visuals, and bounded out-of-Git quarantine hardening. Grants exactly one written `+1` E48.1 planning attempt; no reset and no execution authorization. |
| 1.0.0 | 2026-09-08 | Initial M48 spec. Six Epics put the evidence contract and stable acceptance gate before two isolated project migrations and real runs, close SN-45 separately, and consolidate cost with independently reviewed quality. Records that both targets are currently benched, model identity is not an executable route, credential lookup inherits `XDG_DATA_HOME`, M48 changes no Drivr code, and a named understood failure is an allowed result but not a silent waiver. |
