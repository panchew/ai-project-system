---
project: ai-project-system
phase: P10
milestone: M34
type: note
status: active
issuer_chat: Milestone Chat (P10-M34)
issued_to: Phase Chat (P10)
last_updated: 2026-07-29
---

# Carry-Forward Note — P10-GH-5: the `.ai-project.yml` validation rules are normative but unenforced

**Recorded, not fixed.** Building a validator is a framework *capability* change, which M34's
Non-Goals place outside its adoption epics. Filed here for the Phase Chat to carry to HQ or a later
phase; it will be restated in the M34 Milestone Closure Declaration.

**Origin:** E34.1 found `ai-project-system-mcp` **schema-invalid on three fields** while bumping it,
and recommended the Milestone Chat file the general case. I then audited the rest of the enrolled
fleet and confirmed it is not an isolated project.

---

## The finding

`governance/ai-project-yml-spec.md` §4 defines eleven-plus **Validation Rules** in normative language
— *"A `.ai-project.yml` file is **valid** when all of the following are true"* — including required
fields (rule 3), a `governance.version` regex (rule 5, `\d+\.\d+\.\d+`), and a `project.name` pattern
(rule 7).

**Nothing implements them.** Verified 2026-07-29 across `bin/` and `tests/`:

- No validator exists in `bin/` (`ai-project-daemon`, `ai-project-git-merge`, `ai-project-init`,
  `ai-project-orchestrator`, `ai-project-version`, `ai-project-visual`, `measure-token-burn`,
  `run-dev-agent`, and the shell helpers).
- `bin/ai-project-orchestrator` validates **only** the `visual_artifacts` block
  (`validate_visual_artifacts`). It never checks `governance.*` or `project.*`.
- Worse for detection: the orchestrator's parse path **falls back to defaults with a warning** on a
  YAML failure (`"[!] Warning: Failed to parse .ai-project.yml. Using defaults."`). A malformed
  enrolled config degrades **quietly** rather than failing loudly.
- `bin/ai-project-init` produces a valid config *by construction* for a **new** project. Nothing
  re-validates after the hand-editing that E33.1 Failure Mode 7 documents as normal and expected.

**The rules are not machine-read, and there is direct evidence of that in the spec itself:** rule 3
reads *"All **four** required fields are present"* and then lists **five** (`governance.source`,
`governance.version`, `governance.ref`, `project.name`, `project.description`). An off-by-one in a
normative checklist has survived unnoticed since P2-M6 — which is precisely what one expects of a
rule no code ever executes.

## Evidence from the fleet (audited 2026-07-29, enrolled projects only)

| Project | Violations found |
|---|---|
| `ai-project-system-mcp` | **rule 3** — `governance.ref` absent; **rule 5** — `version` held a raw commit SHA (`2bd76ff4…`); **rule 3** — `project.description` absent. First two fixed by E34.1 as part of the bump; `description` left (out of scope). |
| `courtis` | **rule 3** — `project.description` absent; **rule 5** — `version: "v4.0.1"` fails `\d+\.\d+\.\d+` on the `v` prefix |
| `fieldledger-assesment` | none detected |
| `Getawayinsured2023` | none detected |
| `footboard` | none detected |

Two of five enrolled projects carried undetected schema violations, and one of them
(`ai-project-system-mcp`) had been in that state since enrollment on 2026-07-13 — through four
framework major versions — with nothing surfacing it. It was found by a human-authored Epic reading
the file, not by any tooling.

**Note the interaction with `framework_version`:** all five projects lack it, which is *not* a
violation — the key is convention-only and deliberately unschema'd (**P10-GH-1**). GH-5 is the
converse problem: rules that *are* written down and still unenforced.

## Why it matters beyond tidiness

- **Adoption is P10's whole subject.** A fleet-adoption phase that cannot detect whether an adopted
  config is valid is measuring the wrong thing. M34's bar is *confirmable*; this is a class of state
  that is currently only confirmable by hand.
- **It scales badly with the fleet.** `registry.yml` in `ai-project-system-mcp` lists **eleven**
  project paths — more than P10's five enrolled projects. Hand-reading each config does not survive
  that growth.
- **The quiet-degradation path is the real hazard.** A required field missing does nothing visible
  until something downstream needs it; a parse failure silently substitutes defaults. Both failure
  shapes are invisible until an epic trips over them, which is exactly how this one was found.

## Candidate directions (not decided here)

1. **A `bin/ai-project-validate` (or `ai-project doctor`) that executes §4's rules** against a target
   config, exit-coded, runnable per project. Most direct; adds one executable and a maintenance
   surface. E33.1's "Why not C" note applies — keep any new script out of `tests/` so it cannot
   affect collection.
2. **A test in this repo that validates its own `.ai-project.yml`** against §4. Cheapest, and it
   guards the governance source repo — but it does nothing for adopters, who are the population that
   actually drifted.
3. **Fold validation into the existing bump procedure** as a confirmation step, so every roll-forward
   leaves a validated config behind. Zero new tooling and it rides a lever the fleet already runs;
   but it only fires when a project is bumped.
4. **Fix rule 3's count and treat §4 as documentation only** — the honest minimum if enforcement is
   judged not worth building. It should then say so, rather than reading as a spec that something
   checks.

**No recommendation from this level.** Whether the framework should own an enforcement surface at all
is a capability-scope judgment above a Milestone Chat's adjacency, and it interacts with Drivr's P11
domain (a coordinator that reads every project's config is a plausible owner of this check).

## Explicitly not done here

- No validator written, no spec rule edited, no fleet config corrected. Rule 3's off-by-one is
  **reported, not fixed** — editing the spec is a framework change.
- `courtis`'s two violations are **not** silently folded into E34.2's bump. E34.2's spec records them
  as observed state and may fix them where the bump legitimately touches those fields, but must not
  claim to have closed GH-5 by doing so.
- `project.description` in `ai-project-system-mcp` remains absent — E34.1 correctly scoped it out.
- No renumbering of P10-GH-1 (`framework_version` unschema'd), P10-GH-2 (Creation Seed lacks E31.3
  verification), P10-GH-3 (policy row P1 vs live config), or **P10-GH-4**
  (`delivery_notice.merge_details` structurally unfillable). This is **P10-GH-5**.
