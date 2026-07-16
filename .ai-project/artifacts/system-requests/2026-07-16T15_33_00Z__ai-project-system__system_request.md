---
artifact_type: system_request
artifact_version: 1.0
timestamp: 2026-07-16T15:33:00Z
project_name: ai-project-system
issuer_chat: Milestone Chat (P8-M29)
status: pending
priority: normal
request_summary: Provision a local storage backend for hosted visual artifacts and declare its canonical path
---

# System Request: Provision local visual-artifacts storage backend

## What is needed

A local, machine-level storage backend directory for **hosted visual artifacts** (generated
images/clips referenced by link from governed projects, per AOG §16.5 by-link storage), with:

1. A canonical root location **of System HQ's choosing** — this is machine infrastructure, so
   the location decision belongs to the system, not to any one project. (The CFO has already
   decided the *mechanism*: local storage for now, cloud complexity deferred until ever needed.)
2. A per-project layout convention beneath it (suggested:
   `<root>/<registered-project-name>/visuals/<phase-milestone>/...`), consistent with the MCP
   registry's project names.
3. Read/write access for user `panchew` (and thus for project agents operating as that user).
4. The **canonical absolute path declared in the `system_response`**, so requesting projects
   can mint stable `file://` links for their §7 visual bindings. Stability matters: these
   links are committed into governance artifacts, so the path should be one the system does
   not expect to reorganize.

Initial consumer: this project needs
`<root>/ai-project-system/visuals/P8-M29/` to exist (or be creatable by the project's own
agents) for two files: one `.png` (~218 KB, FLUX-schnell render) and one `.webm` (~74 KB,
LTX-Video clip).

## Why

Epic P8-M29-E29.3 (precision validation) produced this project's first two real generated
artifacts, but its delivery is blocked on hosting: AOG §16.5 requires generated binaries to be
hosted and referenced **by link, never committed**, and no storage backend has ever actually
existed on this machine — every prior reference to "the adopter owns the storage backend" was
policy prose. Cloud hosting attempts failed in-session (GitHub Gist rejects binaries; the
Google Drive upload path was hard-blocked). The CFO has ruled: local storage for now.

Two E29.3 DoD items ("both cases hosted by link"; "both `Level: Epic` §7 bindings complete")
and part of the M29 milestone Definition of Done hang on this. M29 is the sole and final P8
milestone, so this also gates the P8 phase delivery.

## Definition of Done

- The storage root exists at a system-chosen canonical path, writable by `panchew`.
- The per-project layout convention is stated.
- A `system_response` artifact is written back to this project's
  `.ai-project/artifacts/system-responses/` with `status: done` and the canonical absolute
  path declared, at which point the E29.3 Epic Execution Chat can host its two artifacts and
  complete its bindings.
