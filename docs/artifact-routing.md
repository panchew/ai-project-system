# Artifact Routing System Documentation

This document explains the architecture, routing algorithm, artifact lifecycle, and error handling strategy of the background daemon artifact integration in the AI Project System.

---

## 1. Routing Algorithm

The background daemon determines the target chat and reference for each of the three artifact types based on frontmatter fields.

### A. Completion Notice
Completion Notices flow from a child chat (such as an Epic Chat) upward to its parent chat.
- **Milestone Chat**: If `milestone_id` is present in the frontmatter, the notice is routed to the Milestone Chat for that milestone (e.g., `P1-M1`).
- **Phase Chat**: If `milestone_id` is absent but `phase_id` is present, it is routed to the Phase Chat (e.g., `P1`).
- **HQ Chat**: If neither ID is present, it defaults to the main HQ Chat.

**Trigger Payload Example (`route_completion_{epic_id}.json`):**
```json
{
  "action": "route_artifact",
  "artifact_type": "completion_notice",
  "artifact_path": "/path/to/project/.ai-project/artifacts/completion-notices/completion_notice.md",
  "epic_id": "P4-M14-E14.2",
  "parent": "milestone",
  "parent_ref": "P4-M14",
  "timestamp": "2026-06-01T12:00:00Z"
}
```

### B. Review Decision
Review Decisions flow from a parent chat back down to the child chat.
- **Epic Chat**: If `epic_id` is present, it routes the decision back to that Epic Chat (e.g., `P4-M14-E14.2`).
- **Milestone Chat**: If `epic_id` is absent but `milestone_id` is present, it routes to that Milestone Chat (e.g., `P4-M14`).
- **Phase Chat**: If only `phase_id` is present, it routes to that Phase Chat (e.g., `P4`).
- **HQ Chat**: Defaults to the HQ Chat.

**Trigger Payload Example (`route_review_{target_ref}.json`):**
```json
{
  "action": "route_artifact",
  "artifact_type": "review_decision",
  "artifact_path": "/path/to/project/.ai-project/artifacts/review-decisions/review_decision.md",
  "decision": "accept",
  "target": "epic",
  "target_ref": "P4-M14-E14.2",
  "timestamp": "2026-06-01T13:00:00Z"
}
```

### C. Delivery Notice
Delivery Notices represent the final merge/closure of work and are routed upward for acknowledgment.
- Determined identically to Completion Notices: `milestone_id` → Milestone Chat, `phase_id` only → Phase Chat, else → HQ Chat.

**Trigger Payload Example (`route_delivery_{ref_key}.json`):**
```json
{
  "action": "route_artifact",
  "artifact_type": "delivery_notice",
  "artifact_path": "/path/to/project/.ai-project/artifacts/delivery-notices/delivery_notice.md",
  "epic_id": "P4-M14-E14.2",
  "parent": "milestone",
  "parent_ref": "P4-M14",
  "timestamp": "2026-06-01T13:15:00Z"
}
```

---

## 2. Artifact Lifecycle

Artifact files undergo five distinct stages during background processing:

```
[Detection] ──> [File Locking] ──> [Parsing & Validation] ──> [Idempotency Check] ──> [Routing Trigger] ──> [Archiving]
```

1. **Detection**: The background daemon continuously polls the following directories for `*.md` files:
   - `.ai-project/artifacts/completion-notices/`
   - `.ai-project/artifacts/review-decisions/`
   - `.ai-project/artifacts/delivery-notices/`
2. **File Locking & Stability**: The daemon waits for the writing process to complete by:
   - Checking that the file size has stabilized (no change in size for at least 100ms).
   - Attempting to acquire an exclusive advisory lock using `fcntl.flock()`.
3. **Parsing & Schema Validation**: Once the lock is acquired, the daemon reads the file contents and passes them to the `ArtifactParser`. The parser splits the YAML frontmatter, normalizes date and numeric formats, and validates the schema according to the artifact's type spec.
4. **Idempotency Verification**: A unique signature `artifact_type:ref_id:timestamp` is calculated for the artifact. If this signature has already been processed (tracked in `.ai-project/processed_artifacts.json`), the daemon skips routing and archives the file immediately.
5. **Trigger Creation**: The routing trigger payload is generated and written as a JSON file to `.ai-project/queue/` (e.g. `route_completion_P4-M14-E14.2.json`).
6. **Archiving**:
   - **On Success**: The original markdown artifact is moved to `.processed/` under its source directory.
   - **On Failure**: Malformed or invalid artifacts are moved to `.failed/` under their source directory with error logs.

---

## 3. Error Handling & Robustness

The routing engine is designed to handle failure modes without losing data or crashing the background daemon service.

| Failure Mode | Detection / Cause | Recovery Mechanism |
| :--- | :--- | :--- |
| **Partial Writes** | File is being written when detected. | File size checked for stability + `flock` exclusive lock; waits up to 2 seconds for write completion. |
| **Malformed YAML** | Invalid YAML syntax inside delimiters. | Handled by `ArtifactParser` (`ArtifactParseError`). Moved to `.failed/` and error logged. |
| **Invalid Schema** | Required fields missing or wrong data types. | Handled by `ArtifactParser` (`ArtifactSchemaError`). Moved to `.failed/` and error logged. |
| **Concurrent Write Locks** | Lock held by another process indefinitely. | Times out after 2.0s, log logged, file skipped to be processed on next loop iteration. |
| **Trigger Write Failure**| Disk full or permission error writing trigger. | Exception caught; original file is NOT moved to `.processed/` and instead archived in `.failed/` to avoid trigger loss. |

---

## 4. Daemon Logs Example

The daemon maintains a complete audit trail in `.ai-project/logs/daemon.log`:

```
[*] Daemon loop started (PID: 3675543)
[INFO] Detected new artifact file: 2026-06-01T12_00_00Z__P4-M14-E14.2__completion_notice.md
[✓] Routed Completion Notice P4-M14-E14.2 to milestone Chat (P4-M14)
[INFO] Moved 2026-06-01T12_00_00Z__P4-M14-E14.2__completion_notice.md to .processed/
[INFO] Detected new artifact file: 2026-06-01T13_00_00Z__P4-M14-E14.2__review_decision.md
[✓] Routed Review Decision (accept) for P4-M14-E14.2 to epic Chat
[INFO] Moved 2026-06-01T13_00_00Z__P4-M14-E14.2__review_decision.md to .processed/
[INFO] Detected new artifact file: invalid_artifact.md
[ERROR] Error processing artifact invalid_artifact.md: Missing required field: deliverables
[INFO] Moved invalid_artifact.md to .failed/
```
