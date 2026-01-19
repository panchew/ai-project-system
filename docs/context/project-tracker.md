---
project: ai-project-system
context: project-tracker-integration
status: declared
last_updated: 2026-01-19
---

# Project Tracker Integration Declaration

## Overview

This document declares the tracker integration status for the **ai-project-system** project in accordance with the **Project Tracker Integration System** reference defined in [docs/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md](../systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md).

## Integration Status

**Status:** No external tracker integration

This project does not currently integrate with any external project tracking system (Jira, Azure DevOps, GitHub Projects, etc.).

## Rationale

The **ai-project-system** is a governance and execution system designed for projects.

It is maintained internally using:
- Canonical hierarchy: Phase → Milestone → Epic
- Markdown specifications in `docs/phases/`
- Branch-based delivery using `epic/*` → `milestone/*` promotion
- Completion reports in the same directory as specs

External tracker integration is neither required nor currently implemented.

## Future Integration

If external tracker integration becomes necessary, this declaration will be updated to include:

- Tracker provider (e.g., Jira, Azure DevOps)
- Canonical ↔ external mapping table
- API access method
- Sync direction (read-only, write, bidirectional)

Until then, all authority and truth resides in the versioned Markdown artifacts in this repository.

## Reference

For the complete system specification, see:
[docs/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md](../systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md)

Governing principles are defined in:
- [docs/PROJECT-SYSTEM-GUIDELINES.md](../PROJECT-SYSTEM-GUIDELINES.md)
- [docs/AI-OPERATING-GUIDELINES.md](../AI-OPERATING-GUIDELINES.md)
