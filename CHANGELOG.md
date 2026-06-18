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
