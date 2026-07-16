---
artifact_type: system_request
artifact_version: 1.0
timestamp: 2026-07-16T15:32:00Z
project_name: ai-project-system
issuer_chat: Milestone Chat (P8-M29)
status: pending
priority: normal
request_summary: Install ffmpeg system-wide for video inspection/frame extraction
---

# System Request: Install ffmpeg

## What is needed

Install `ffmpeg` (which provides `ffprobe`) system-wide via the distribution package manager,
available on `PATH` for user `panchew`.

## Why

Epic P8-M29-E29.3 (precision validation) had to judge an LTX-Video `.webm` clip
frame-by-frame. No `ffmpeg` was present, so the executing agent built a throwaway Python venv
(`imageio` + `imageio-ffmpeg` + `av`) just to extract frames — a one-time workaround it
explicitly documented as "not a project dependency change" (E29.3 Delivery Notice, Notes).
The Milestone Chat's independent verification of that delivery had to repeat the same
workaround. Clip production is a standing capability in this framework (AOG §16.7,
`governance/guides/visual-artifacts.md` §8), so video inspection will keep recurring — it
should be served by standard system tooling, not per-session venvs.

This is machine-level infrastructure, so it is requested here rather than installed ad hoc
from a project session — first exercise of the `system_request` channel
(SYSTEM-GOVERNANCE.md v1.0.0).

## Definition of Done

- `ffmpeg -version` and `ffprobe -version` both succeed in a fresh shell for user `panchew`.
- A `system_response` artifact is written back to this project's
  `.ai-project/artifacts/system-responses/` with `status: done`.
