---
artifact_type: reference
title: Enrolled-project v7.0.0 bump procedure
phase: P10
milestone: M33
epic: E33.1
status: active
last_updated: 2026-07-29
amended_by: P10-M34-E34.1 (field findings from the first non-proving-pair application);
  P10-M34-E34.2 (multi-declaration submodule resolution + branch-base choice, from the
  three dormant-fleet applications)
---

# v7.0.0 Bump Procedure — refresh an enrolled project's governance and stamp `framework_version: v7.0.0`

This is the **repeatable lever** produced by Epic P10-M33-E33.1 and consumed by M34 to roll the
dormant fleet forward. It refreshes an already-enrolled project's installed governance to the
v7.0.0 corpus and leaves a **confirmable** `framework_version: v7.0.0` stamp. It was validated by
bumping the proving pair (`home_finance`, `local-agent-runner`) — see the E33.1 confirmation
evidence (`docs/phases/P10__.../P10-M33-E33.1__confirmation-evidence.md`).

**Scope.** This bumps *enrolled* projects — a project that already has a governance submodule
(conventionally `.governance`, but **not always** — see Failure Mode 8) and a `.ai-project.yml`. It is **not** the enrollment path for a brand-new project (that is
`bin/ai-project-init`). It does not run any project work; it only refreshes governance and stamps
the version.

---

## Chosen mechanism — Direction (B): targeted governance-file sync

The E33.1 spec left the mechanism open across three candidates (A re-run `ai-project-init`,
B targeted file sync, C scripted wrapper). **Direction (B) was chosen.**

**Why B, not A.** `bin/ai-project-init` is a project-**creation** tool, not a refresh tool. It
runs `git submodule add` (which errors when a `.governance` submodule already exists),
`mkdir -p` + stub-file creation, and regenerates `.ai-project.yml` from a fixed template. Run
against an enrolled project it either aborts on the existing submodule or clobbers the project's
hand-tuned `.ai-project.yml` (both proving-pair configs are hand-edited and diverge from the
template — e.g. `local-agent-runner` carries a `project.description` and a different key order).
Direction A is therefore unsafe for refresh. Corroborating evidence: the *last* real refresh in
the wild (home_finance's v6.0.0 bump, commits `56b93e4` / `b83e62c`) was done as a **manual
targeted sync**, not by re-running init — B matches established practice.

**Why not C (scripted wrapper).** A committed executable adds a maintenance/scope surface and, if
placed where the framework test suite collects it, risks the 363-test baseline. The step count is
small and the commands are given verbatim below, so the procedure is repeatable as written without
new code. If M34's fleet volume makes hand-running tedious, wrapping the steps below in a script is
a safe future enhancement — keep any such script out of `tests/` so it cannot affect collection.

**What "governance refresh" means here** (the three elements the Milestone spec fixes):
1. **Governance corpus** — the governance submodule (`$SUB`) is re-pinned to the v7.0.0 tag, bringing
   the whole vendored governance tree (AOG, PSG, yml-spec, templates, `governance/systems/`, and
   the canonical `governance.agent.md`) to v7.0.0.
2. **Installed agent** — the project's *out-of-band copy* of `governance.agent.md` (under
   `.ai-project/agents/`) is refreshed from the submodule's v7.0.0 tree. **This is a separate file
   from the submodule and is NOT updated by re-pinning the submodule** — see Failure Mode 3.
3. **`framework_version` stamp** — a top-level `framework_version: v7.0.0` key is written to the
   target's `.ai-project.yml` (see "Stamp location").

---

## Preconditions (check before running)

- **Target reachable and is a git repo.** You have a working clone of the target and can commit in
  it. A target that cannot be reached is a **blocker → escalate** (E33.1 Hard Constraint); do not
  stamp a project you did not refresh.
- **Target is enrolled.** It has a governance submodule (`git submodule status` lists it — whatever
  its path; see Step 0 and Failure Mode 8) and a `.ai-project.yml` with a `governance:` block. If not enrolled, this is not the right tool — use
  `bin/ai-project-init`.
- **A reachable source of the v7.0.0 tag.** Either network access to `origin`
  (`https://github.com/panchew/ai-project-system`) or a local canonical clone that has the tag
  (fallback in Step 1). v7.0.0 commit = `8044451c74f798239a51d794ebdab85b2567234e`.
- **Known working-tree state.** Prefer a clean tree so the bump commit is isolated. Untracked
  content (e.g. an `.ai-project/artifacts/` dir) is fine but **must not be swept into the commit** —
  stage explicitly (Step 5), never `git add -A`.
- **A dedicated branch.** Do the bump on a `chore/framework-v7.0.0-bump` branch, not directly on
  the project's authoritative branch. Pushing/merging that branch is the **project owner's (CFO's)
  call**, an outward action outside this procedure.

---

## Procedure (ordered steps)

Let `TARGET` be the path to the enrolled project. Run from `TARGET`.

**Step 0 — resolve the submodule path first; do not assume `.governance`.** It varies per project
(Failure Mode 8), and `.gitmodules` may declare **more than one** submodule, including orphans
(Failure Mode 10). Every command below uses `$SUB`, so resolving it once makes the rest verbatim-safe.

```sh
cd "$TARGET"

# 0. Resolve the actual submodule path (do NOT hardcode .governance).
#    `.gitmodules` is a declaration file and can contain stale/orphaned entries, so
#    intersect what it declares with what git actually tracks as LIVE (git submodule
#    status lists live submodules only) and with what exists on disk. See FM 8 and FM 10.
LIVE="$(git submodule status | awk '{print $2}')"
SUB="$(git config -f .gitmodules --get-regexp '^submodule\..*\.path$' | awk '{print $2}' |
  while read -r p; do
    printf '%s\n' "$LIVE" | grep -qx "$p" && [ -d "$p" ] && echo "$p"
  done)"
n="$(printf '%s' "$SUB" | grep -c .)"
[ "$n" -eq 1 ] || { echo "expected exactly 1 live governance submodule, got $n: [$SUB] — STOP"; }
echo "$SUB"        # `.governance` (proving pair, Getawayinsured2023, footboard, courtis)
                   # or `governance` (ai-project-system-mcp)

# 1. Dedicated branch + make the v7.0.0 tag available inside the submodule.
#    Choose the BASE deliberately — see FM 11 before running this.
git checkout -b chore/framework-v7.0.0-bump
git -C "$SUB" fetch --tags origin \
  || git -C "$SUB" fetch /path/to/local/ai-project-system 'refs/tags/v7.0.0:refs/tags/v7.0.0'
git -C "$SUB" rev-parse -q --verify 'v7.0.0^{commit}'   # -> 8044451c74f...

# 2. Re-pin the submodule to v7.0.0 (refreshes the whole vendored governance corpus).
git -C "$SUB" checkout --quiet v7.0.0
git -C "$SUB" describe --tags                            # -> v7.0.0

# 3. Refresh the OUT-OF-BAND installed agent copy from the submodule's v7.0.0 tree.
cp -f "$SUB/governance/agents/governance.agent.md" .ai-project/agents/governance.agent.md

# 3b. Legacy installs only (Failure Mode 5): remove a superseded/placeholder agent, tracked.
[ -e .ai-project/agents/hq.agent.md ] && git rm .ai-project/agents/hq.agent.md

# 4. Edit .ai-project.yml (field-targeted; do NOT template-replace — structure varies per project):
#    - governance.version: "6.0.0" -> "7.0.0"   (quoted semver; if it holds a raw SHA, see FM 7)
#    - governance.ref:      v6.0.0 -> v7.0.0    (if the key is absent, ADD it — it is REQUIRED)
#    - add a top-level:     framework_version: v7.0.0   (the adoption stamp)

# 4b. Check .gitmodules for a SECOND recorded pin (Failure Mode 9).
grep -n 'branch' .gitmodules   # a raw SHA here is invalid; see FM 9 for the fix

# 5. Stage EXACTLY the bump files (never `git add -A`) and commit.
#    Add .gitmodules only if step 4b changed it.
git add .ai-project.yml .ai-project/agents/governance.agent.md "$SUB"
git commit -m "chore(governance): bump to framework v7.0.0"
```

Then run the confirmation method (below) and record the result. **Do not report the project bumped
until its own verification passes.**

---

## Stamp location + confirmation method

- **Stamp location:** a top-level `framework_version: v7.0.0` key in the target's `.ai-project.yml`.
  Chosen because `.ai-project.yml` is the one file guaranteed to exist in *every* enrolled project
  (uniform for M34), and because SN-23's fleet-state check greps for `framework_version` — this puts
  the stamp exactly where the phase's "stamped **and confirmable**" bar looks.
- **Confirmation method** (run against the target; all three must pass):

  ```sh
  grep '^framework_version:' .ai-project.yml            # -> framework_version: v7.0.0
  grep -E '^  (version|ref):' .ai-project.yml           # -> "7.0.0" / v7.0.0
  git submodule status "$SUB"                           # -> 8044451... <SUB> (v7.0.0)
  sha256sum .ai-project/agents/governance.agent.md      # -> 66404389f29fa1ff8e829015b70ab8b33373dc3ac3eca3f2faea121d3da3441e
  ```

  On a **legacy install** (Failure Mode 5) or a target with a **dirty tree** (Failure Mode 6), add
  these two — they prove the fix landed *and* that nothing else was swept up:

  ```sh
  ls .ai-project/agents/        # -> governance.agent.md ONLY (no hq.agent.md)
  git status --porcelain        # -> the owner's pre-existing dirty paths, still exactly as found
  ```

  The agent sha `66404389…` is the canonical v7.0.0 `governance.agent.md` (14711 bytes). A mismatch
  means Step 3 was skipped — the project is running a stale agent while claiming v7.0.0 (Failure
  Mode 3).

---

## Known failure modes (discovered while applying this procedure)

1. **`ai-project-init` is not a refresh tool (Direction A trap).** It creates; it does not update.
   Against an enrolled project it aborts on the existing `.governance` submodule or clobbers the
   hand-tuned `.ai-project.yml`. Do not use it to bump — this is why the procedure is Direction B.
2. **The v7.0.0 tag is not pre-fetched in the target's submodule.** A target last pinned at v6.0.0
   (or, as in `ai-project-system-mcp`, at a raw SHA eight commits past v5.1.0) does not have the
   v7.0.0 tag object locally; `checkout v7.0.0` fails until Step 1's `git -C "$SUB" fetch --tags`.
   If offline, fetch the tag from a local canonical clone. Confirmed in the wild twice.
3. **The installed `governance.agent.md` is an out-of-band COPY — re-pinning the submodule does NOT
   refresh it (load-bearing).** `.ai-project/agents/governance.agent.md` was copied at
   enrollment/last-bump and lives *outside* the submodule. Skip Step 3 and the project silently runs
   the v6.0.0 agent (sha `7bfedafb…`) while its `.ai-project.yml` claims v7.0.0. Both proving-pair
   projects carried the stale v6.0.0 agent before this bump — always re-copy and re-verify the sha.
4. **`framework_version` is not defined in the yml-spec.** `governance/ai-project-yml-spec.md`
   defines `governance.{source,version,ref,submodule_path}` but has no `framework_version` field.
   The stamp is a deliberately-added top-level key. Formalizing it in the yml-spec is a
   **framework-repo (capability) change, out of scope for adoption epics** (E33.1/M34) — flagged to
   the Milestone/Phase chat as a candidate GH item so the field is schema-blessed rather than
   convention-only.
5. **P6-GH-15 (superseded `hq.agent.md`) — check per project; it did NOT bite the proving pair.**
   Both `home_finance` and `local-agent-runner` carry canonical `governance.agent.md` (not the
   superseded `hq.agent.md`), so the hazard did not apply here. The *current* `bin/ai-project-init`
   install path (`bin/ai-project-init:328,334`) copies canonical `governance.agent.md`, so new
   installs are clean. **Legacy installs must still be checked** — before Step 3, verify the target
   has `.ai-project/agents/governance.agent.md` and NOT an `hq.agent.md`:
   `ls .ai-project/agents/`. `ai-project-system-mcp` was the known live case — **closed by
   P10-M34-E34.1** (bump commit `95e6168`), which found the file was **not a stale agent but a
   230-byte placeholder stub** ("under development in Milestone M8"). Expect either shape. There is
   nothing to preserve or migrate in the placeholder case: the fix is `git rm` (tracked deletion, not
   an unlinked file) plus the canonical install — and it is a **delete, not a migration**. Record it
   as a per-project deviation.
6. **Uncommitted content in the target — untracked *and* modified-tracked.** Targets may carry
   untracked `.ai-project/artifacts/` dirs **and modified tracked files that are the owner's
   in-flight work** (`ai-project-system-mcp` carried a modified `registry.yml`, +10 lines, during
   E34.1). Stage the bump paths explicitly (Step 5); never `git add -A`. **A clean `git status` at
   the end is a failure signal, not success** — it means you committed someone else's work. Capture
   `git status --porcelain` *before* touching anything and diff it against the after state.
7. **`.ai-project.yml` structure varies per project — including missing and mistyped fields.** Key
   order, comments, and optional keys (`submodule_path`, `project.description`) differ. Edit
   field-by-field (Step 4); never template-overwrite. Two variants seen in the wild beyond simple
   reordering (both in `ai-project-system-mcp`, E34.1):
   - **`governance.ref` absent.** The yml-spec marks it **REQUIRED**
     (`governance/ai-project-yml-spec.md`, validation rule 3). **Add it** (`ref: v7.0.0`) rather than
     recording a confirmation deviation — the file was schema-invalid without it.
   - **`governance.version` holding a raw 40-char SHA** instead of a quoted semver. The spec requires
     a quoted semver and explicitly disallows non-pinned/other forms. Replace with `"7.0.0"`; the SHA
     belongs in `ref` (and here was superseded by the tag anyway).
8. **The submodule path is NOT always `.governance` (breaks every command verbatim).**
   `ai-project-system-mcp` uses `path = governance`. Steps 1, 2, 3, 5 and the confirmation method all
   hardcoded `.governance` before E34.1 and **fail — or worse, half-succeed — on such a target.**
   Resolve the path first (Step 0) and use `$SUB` throughout. Note the target may *also* carry a
   `governance.submodule_path` key in `.ai-project.yml`; `.gitmodules` is the authority, since that
   is what git itself reads.
9. **`.gitmodules` can carry a SECOND recorded pin, and it can be a raw SHA.**
   `ai-project-system-mcp` had `branch = 2bd76ff4…` — a commit SHA in a field that expects a branch
   name, which `git submodule update --remote` cannot resolve either way. Re-pinning the submodule
   does **not** touch this line, so the stale SHA survives an otherwise-correct bump and the project
   still records the old pin. **Fix: delete the `branch` line.** That converges on the
   fleet-canonical `path` + `url` shape carried by both proving-pair projects, and avoids putting a
   tag in a field git only resolves as `refs/remotes/origin/<branch>`. The real pin is the gitlink
   (a SHA by design, unavoidably) plus `governance.ref` in `.ai-project.yml`. Stage `.gitmodules`
   with the bump if you change it.
10. **`.gitmodules` can declare MORE THAN ONE submodule, including an orphan — the pre-E34.2 Step 0
    resolved `$SUB` to a multi-line string and halted.** `courtis` declares two:
    `[submodule "governance"] path = governance branch = v2.0.0` and
    `[submodule ".governance"] path = .governance`. Only `.governance` is live; the `governance`
    path **does not exist on disk and is absent from `git submodule status`** — an orphaned
    declaration left behind by an old layout, carrying a stale `branch = v2.0.0` (an FM 9 defect,
    three majors older, in a submodule that no longer exists). The old one-liner
    (`... | awk '{print $2}'`) returned both paths, `$SUB` became `"governance\n.governance"`, and
    the `[ -d "$SUB" ]` guard fired: *"submodule path not found — STOP."*
    **The halt was correct behaviour — it refused to guess — but the operator was left to resolve
    it by hand.** Fix (now in Step 0): **intersect the declared paths with `git submodule status`
    (live submodules only) and with on-disk existence**, then require exactly one survivor. A
    genuine multi-submodule project still stops, which is right — a human must say which submodule
    carries governance. **Do not hand-edit around the guard**; disambiguate, then remove the orphan
    stanza entirely (`courtis` commit `a2e95a9`) — deleting only its `branch` line per FM 9 would
    leave a declaration for a path that does not exist and Step 0 would keep tripping. Stage
    `.gitmodules` with the bump. The replacement resolver was verified against all six enrolled
    projects (`courtis`, `footboard`, `Getawayinsured2023`, `home_finance`, `local-agent-runner`,
    `ai-project-system-mcp`), including the FM 8 `governance` path.
11. **The procedure never said what to branch `chore/framework-v7.0.0-bump` FROM, and on a dirty
    target the obvious answer can be impossible.** Preferred base is the project's **default
    branch** (`main`/`master`), so the bump is an isolated, independently-publishable change rather
    than one that drags unmerged governance work along. But a project sitting on an in-flight
    branch with **uncommitted changes to a file that does not exist on the default branch** cannot
    be switched: git aborts with *"Your local changes to the following files would be overwritten
    by checkout"*, and the only ways through are to commit or stash **the owner's** work — both
    forbidden. Observed live in `footboard` (modified `docs/phases/P1__.../P1__phase-spec.md`,
    untracked on its default branch), which was therefore bumped **from its in-flight milestone
    branch**. **Decide the base per project, before Step 1, and record the choice and the reason.**
    When you are forced onto a working branch, say so in the roadmap **and** name the consequence:
    the bump commit inherits that branch's unmerged ancestry, so it is *not* independently
    publishable — the owner must merge the in-flight branch first or cherry-pick the bump commit
    onto the default branch once their work lands. Three bases, three different answers in E34.2:
    `Getawayinsured2023` → `main` (clean tree, and `main` already carried everything the bump
    needed); `courtis` → `main` (already checked out, so no switch and no risk);
    `footboard` → in-flight milestone branch (default branch unreachable, as above).

---

## Repeatability note (for M34 / a third project)

An operator who has never touched a project can bump it by: confirming the preconditions, running
Steps 0–5, and passing the confirmation method. The per-project judgement calls are Failure Mode 5
(superseded *or placeholder* agent → canonical + record the deviation), Failure Mode 7 (locate the
`.ai-project.yml` fields whatever the layout, and add/repair `ref` and `version` if the file is
schema-invalid), Failure Mode 8 (resolve the submodule path — **Step 0, before anything else**),
Failure Mode 9 (check `.gitmodules` for a second recorded pin), Failure Mode 10 (multiple/orphaned
submodule declarations), and Failure Mode 11 (**choose and record the branch base before Step 1**).
Everything else is mechanical. A target that cannot be reached or refreshed is a **recorded blocker
+ escalation**, never a guessed stamp (E33.1 Hard Constraint).

**Amendment note (P10-M34-E34.1, 2026-07-29).** Failure Modes 8 and 9 and the Step 0 path resolution
were added after the first application to a project *outside* the proving pair. E33.1 validated the
procedure on two projects that happened to share a layout; `ai-project-system-mcp` differed in four
ways, and the two that break commands silently (8 and 9) were invisible until a third project was
tried. Treat "validated on the proving pair" as "not yet generalized" for any future lever of this
kind.

**Amendment note (P10-M34-E34.2, 2026-07-29).** Failure Modes 10 and 11 and the rewritten Step 0
resolver were added after applying the procedure to the remaining three dormant projects
(`Getawayinsured2023`, `footboard`, `courtis`) — all three reached v7.0.0. The pattern from E34.1
held for a second time: **each new project found defects the previous ones could not.** FM 10 was
predicted before execution (the Milestone Chat read `courtis`'s `.gitmodules` while planning) and
reproduced exactly; FM 11 was **not** predicted — it surfaced only when `git checkout main` refused
on `footboard`. Two observations worth carrying into any future fleet lever:

- **A guard that halts is doing its job, but a halt the operator must resolve by hand is unfinished
  work.** Step 0 correctly refused to guess on `courtis`; the amendment turns that refusal into a
  resolution and keeps the refusal for the genuinely ambiguous case.
- **The steps a procedure omits are as costly as the ones it gets wrong.** FM 11 is not a bug in any
  command — it is a decision the procedure never named, and it had a different answer for each of
  the three projects.

Six projects are now bumped (proving pair + `ai-project-system-mcp` + these three). The failure-mode
list has grown at every single application, so treat it as still-incomplete.
