---
artifact_type: reference
title: Enrolled-project v7.0.0 bump procedure
phase: P10
milestone: M33
epic: E33.1
status: active
last_updated: 2026-07-20
---

# v7.0.0 Bump Procedure — refresh an enrolled project's governance and stamp `framework_version: v7.0.0`

This is the **repeatable lever** produced by Epic P10-M33-E33.1 and consumed by M34 to roll the
dormant fleet forward. It refreshes an already-enrolled project's installed governance to the
v7.0.0 corpus and leaves a **confirmable** `framework_version: v7.0.0` stamp. It was validated by
bumping the proving pair (`home_finance`, `local-agent-runner`) — see the E33.1 confirmation
evidence (`docs/phases/P10__.../P10-M33-E33.1__confirmation-evidence.md`).

**Scope.** This bumps *enrolled* projects — a project that already has a `.governance` submodule
and a `.ai-project.yml`. It is **not** the enrollment path for a brand-new project (that is
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
1. **Governance corpus** — the `.governance` submodule is re-pinned to the v7.0.0 tag, bringing
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
- **Target is enrolled.** It has a `.governance` submodule (`git submodule status` lists it) and a
  `.ai-project.yml` with a `governance:` block. If not enrolled, this is not the right tool — use
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

```sh
cd "$TARGET"

# 1. Dedicated branch + make the v7.0.0 tag available inside the submodule.
git checkout -b chore/framework-v7.0.0-bump
git -C .governance fetch --tags origin \
  || git -C .governance fetch /path/to/local/ai-project-system 'refs/tags/v7.0.0:refs/tags/v7.0.0'
git -C .governance rev-parse -q --verify 'v7.0.0^{commit}'   # -> 8044451c74f...

# 2. Re-pin the submodule to v7.0.0 (refreshes the whole vendored governance corpus).
git -C .governance checkout --quiet v7.0.0
git -C .governance describe --tags                            # -> v7.0.0

# 3. Refresh the OUT-OF-BAND installed agent copy from the submodule's v7.0.0 tree.
cp -f .governance/governance/agents/governance.agent.md .ai-project/agents/governance.agent.md

# 4. Edit .ai-project.yml (field-targeted; do NOT template-replace — structure varies per project):
#    - governance.version: "6.0.0" -> "7.0.0"
#    - governance.ref:      v6.0.0 -> v7.0.0
#    - add a top-level:     framework_version: v7.0.0   (the adoption stamp)

# 5. Stage EXACTLY the bump files (never `git add -A`) and commit.
git add .ai-project.yml .ai-project/agents/governance.agent.md .governance
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
  git submodule status .governance                      # -> 8044451... .governance (v7.0.0)
  sha256sum .ai-project/agents/governance.agent.md      # -> 66404389f29fa1ff8e829015b70ab8b33373dc3ac3eca3f2faea121d3da3441e
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
   does not have the v7.0.0 tag object locally; `checkout v7.0.0` fails until Step 1's
   `git -C .governance fetch --tags`. If offline, fetch the tag from a local canonical clone.
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
   `ls .ai-project/agents/`. `ai-project-system-mcp` is the known live case (M34/E34.1 closes it);
   if `hq.agent.md` is present, the fix is to install the canonical `governance.agent.md` and remove
   the superseded file — record it as a per-project deviation.
6. **Untracked content in the target.** Targets may carry untracked `.ai-project/artifacts/` dirs.
   Stage the four bump paths explicitly (Step 5); never `git add -A`, or unrelated untracked content
   lands in the bump commit.
7. **`.ai-project.yml` structure varies per project.** Key order, comments, and optional keys
   (`submodule_path`, `project.description`) differ between projects. Edit the three fields
   field-by-field (Step 4); do not overwrite the file from a template.

---

## Repeatability note (for M34 / a third project)

An operator who has never touched a project can bump it by: confirming the preconditions, running
Steps 1–5, and passing the confirmation method. The only per-project judgement is Failure Mode 5
(check for a superseded `hq.agent.md` and, if present, convert it to canonical + record the
deviation) and Failure Mode 7 (locate the three `.ai-project.yml` fields, whatever the file's
layout). Everything else is mechanical. A target that cannot be reached or refreshed is a
**recorded blocker + escalation**, never a guessed stamp (E33.1 Hard Constraint).
