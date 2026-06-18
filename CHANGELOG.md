# Changelog

All notable changes to the AI Project System are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- **Daemon orchestrator path resolution** (E17.1): The daemon previously resolved
  the orchestrator binary strictly at `<PROJECT_ROOT>/bin/ai-project-orchestrator`.
  When the daemon runs from a governance submodule with `--project-root .` pointing
  at the consuming project, the orchestrator is not under that project's `bin/` — it
  ships inside the governance package next to the daemon. Startup therefore failed
  with "orchestrator not found", blocking all Epic execution for projects pinned to
  the v2.0.0 submodule layout.

  The daemon now searches an ordered, cached set of conventional locations and falls
  back to its own directory, which always contains the orchestrator:

  1. `<PROJECT_ROOT>/bin/ai-project-orchestrator` (self-referential repo / vendored)
  2. `<PROJECT_ROOT>/governance/bin/ai-project-orchestrator` (legacy convention)
  3. `<PROJECT_ROOT>/.governance/bin/ai-project-orchestrator` (canonical submodule)
  4. `<daemon dir>/ai-project-orchestrator` (orchestrator shipped beside daemon)

  The fix is transparent: no manual intervention or environment variables are required
  after `git clone`. Projects already working on the v3.0.0+ layout are unaffected.
  Resolution is cached after the first successful lookup, and if the orchestrator
  cannot be found the daemon now prints a clear error naming every path it tried.

### Added

- `ai-project-daemon --check` command that verifies the orchestrator can be located
  and prints its resolved path (exit 0 if found, exit 1 with the searched paths
  otherwise). Honors `--project-root`.
- **HQ Execution Chat Starter** (E17.2): new `governance/systems/hq-execution-chat-starter.md`,
  completing the HQ → Phase → Milestone → Epic set of system starters. Adds P4 sections
  for the artifact system, the bugfix workflow, the production deployment gate, and the
  team roles & decision matrix, with worked Completion Notice / Review Decision / Delivery
  Notice examples and a reference to the M16 example project.
- **Three governance artifact templates** (E17.2): `merge-authorization.md`,
  `epic-closure-notice.md`, and `escalation-notice.md` in `governance/templates/`, each
  with schema, section guidance, and a filled example.
- **P4 Governance System Guide** (E17.2): `docs/team-collaboration/P4-governance-system-guide.md`,
  the entry point linking every P4 team-collaboration doc. Every P4 doc now links back to it.
- **Starter branch-name lint check** (E17.2): `tests/test_starter_lint.py` flags
  `milestone/M<n>` references in Epic starters whose number is not a real milestone
  (catching the recurring `M14`→`M144` / `M17`→`M147` typo) without flagging legitimate
  cross-references. Wired into `pytest`.

### Changed

- **Milestone Execution Chat Starter** (E17.2): added worked accept/reject Review Decision
  examples, a Rework Cycle section (max 3 attempts), and an Escalation Path section.
- **Documentation** (E17.2): expanded the team FAQ (now 23 questions) and Troubleshooting
  Guide (now 16 entries, including the E17.1 "orchestrator not found" root cause, the
  branch-name typo check, SLA timezone drift, and "Spec Complete" inaccuracy); added a P4
  section and "Get started with P4" / "Run the example" links to the main README.

### Fixed

- **Obsolete "Epic Completion Report" terminology** (E17.2): replaced with the current
  Completion Notice / Delivery Notice terms across the P4 and governance Epic starters.
- **Milestone branch-name typos** (E17.2): corrected `milestone/M144` → `milestone/M14`
  in the three M14 Epic starters.
