# Artifact Schema Reference

This document defines the schema definitions, field types, and validation rules for the three canonical artifact types in the AI Project System:
1. **Completion Notice** (`completion_notice`)
2. **Review Decision** (`review_decision`)
3. **Delivery Notice** (`delivery_notice`)

These schemas are defined programmatically in `lib/artifact_schemas.py` and enforced by `lib/artifact_parser.py`.

---

## 1. Completion Notice (`completion_notice`)

### Core Fields

| Field | Type | Required | Description | Validation Rule |
|---|---|---|---|---|
| `artifact_type` | `string` | Yes | Must be `"completion_notice"`. | Exact match |
| `artifact_version` | `string` | Yes | Artifact format version (e.g., `"1.0"`). | Auto-coerced to string |
| `timestamp` | `iso8601` | Yes | ISO-8601 UTC timestamp of creation. | `YYYY-MM-DDTHH:MM:SSZ` |
| `issuer_chat` | `string` | Yes | Source chat (e.g., `"Epic Agent (P4-M1-E1.1)"`). | String type |
| `issuer_role` | `string` | Yes | Creator's role (e.g., `"Epic Agent"`). | String type |
| `status` | `string` | Yes | Must be `"ready_for_review"`. | Exact match |
| `epic_id` | `string` | Yes | Target Epic ID. | Format: `P#-M#-E#.#` or `B#.#` |
| `milestone_id` | `string` | Yes | Milestone parent reference ID. | Format: `P#-M#` |
| `phase_id` | `string` | Yes | Phase grandparent reference ID. | Format: `P#` |
| `project_name` | `string` | Yes | Name of the workspace/project. | String type |
| `deliverables` | `list` | Yes | Array of deliverable objects. | Must not be empty |
| `blockers` | `list` | No | Array of blocker objects (optional). | List type if provided |
| `qa_status` | `string` | Yes | Quality assurance check outcome. | Must be `"passed"`, `"failed"`, or `"blocked"` |
| `pr_details` | `dict` | Yes | Pull Request metadata block. | Must match structural rules below |

### Sub-objects

#### Deliverable Structure
Every item in the `deliverables` list must contain:
- `name` (`string`): Short name/label of the deliverable.
- `path` (`string`): Path inside the repository.
- `type` (`string`): One of `"spec"`, `"implementation"`, `"report"`, `"pr"`.
- `status` (`string`): One of `"ready"`, `"pending"`, `"failed"`.

#### PR Details Structure
The `pr_details` dictionary must contain:
- `number` (`int` or string `"pending"`): PR identifier.
- `title` (`string`): Heading of the pull request.
- `target_branch` (`string`): Branch where code is proposed to merge.
- `url` (`string`): URL to pull request or `"not_created_yet"`.

---

## 2. Review Decision (`review_decision`)

### Core Fields

| Field | Type | Required | Description | Validation Rule |
|---|---|---|---|---|
| `artifact_type` | `string` | Yes | Must be `"review_decision"`. | Exact match |
| `artifact_version` | `string` | Yes | Artifact format version (e.g., `"1.0"`). | Auto-coerced to string |
| `timestamp` | `iso8601` | Yes | ISO-8601 UTC timestamp of review decision. | `YYYY-MM-DDTHH:MM:SSZ` |
| `issuer_chat` | `string` | Yes | Source chat (e.g., `"Milestone Agent (P4-M1)"`). | String type |
| `issuer_role` | `string` | Yes | Creator's role (e.g., `"Milestone Agent"`). | String type |
| `decision` | `string` | Yes | Decision. | Must be `"accept"` or `"reject"` |
| `epic_id` | `string` | No | Reference Epic ID (optional at milestone level).| Format: `P#-M#-E#.#` or `B#.#` |
| `milestone_id` | `string` | No | Milestone reference ID. | Format: `P#-M#` |
| `phase_id` | `string` | No | Phase reference ID. | Format: `P#` |
| `project_name` | `string` | Yes | Name of the workspace/project. | String type |
| `completion_notice_timestamp` | `iso8601` | Yes | Timestamp of the Completion Notice reviewed. | `YYYY-MM-DDTHH:MM:SSZ` |
| `feedback` | `string` | Yes | Comments, notes, or rejection reasoning. | String type |
| `authorization` | `dict` | Yes | Proceeding instructions block. | Must match structural rules below |

*Note: At least one of `epic_id`, `milestone_id`, or `phase_id` must be present.*

### Sub-objects

#### Authorization Structure
The `authorization` dictionary must contain:
- `action` (`string`): Must be `"merge"` (if decision is accept) or `"rework"` (if decision is reject).
- `merge_instruction` (`string` or null): Step-by-step guidance for merging or reworking the branch.

---

## 3. Delivery Notice (`delivery_notice`)

### Core Fields

| Field | Type | Required | Description | Validation Rule |
|---|---|---|---|---|
| `artifact_type` | `string` | Yes | Must be `"delivery_notice"`. | Exact match |
| `artifact_version` | `string` | Yes | Artifact format version (e.g., `"1.0"`). | Auto-coerced to string |
| `timestamp` | `iso8601` | Yes | ISO-8601 UTC timestamp of delivery. | `YYYY-MM-DDTHH:MM:SSZ` |
| `issuer_chat` | `string` | Yes | Source chat (e.g., `"Epic Agent (P4-M1-E1.1)"`). | String type |
| `issuer_role` | `string` | Yes | Creator's role (e.g., `"Epic Agent"`). | String type |
| `status` | `string` | Yes | Must be `"delivered"`. | Exact match |
| `epic_id` | `string` | No | Target Epic reference ID. | Format: `P#-M#-E#.#` or `B#.#` |
| `milestone_id` | `string` | No | Milestone reference ID. | Format: `P#-M#` |
| `phase_id` | `string` | No | Phase reference ID. | Format: `P#` |
| `project_name` | `string` | Yes | Name of the workspace/project. | String type |
| `merge_details` | `dict` | Yes | Detailed pull request merge outcomes. | Must match structural rules below |
| `duration` | `dict` | Yes | Timespan tracking block. | Must match structural rules below |
| `final_artifacts` | `list` | Yes | List of committed deliverables. | Must match structural rules below |
| `completion_notice_timestamp` | `iso8601` | Yes | Reference to initial completion notice. | `YYYY-MM-DDTHH:MM:SSZ` |
| `review_decision_timestamp` | `iso8601` | Yes | Reference to matching review decision. | `YYYY-MM-DDTHH:MM:SSZ` |

*Note: At least one of `epic_id`, `milestone_id`, or `phase_id` must be present.*

### Sub-objects

#### Merge Details Structure
The `merge_details` dictionary must contain:
- `pr_number` (`int` or `string`): Merged pull request number.
- `pr_url` (`string`): GitHub pull request URL.
- `merge_commit` (`string`): SHA commit hash representing the merge.
- `merge_timestamp` (`iso8601`): ISO timestamp of the merge.
- `merge_strategy` (`string`): Must be `"squash"`, `"rebase"`, or `"merge"`.
- `target_branch` (`string`): Target branch into which code was merged.

#### Duration Structure
The `duration` dictionary must contain:
- `start_date` (`string`): Work start date (`YYYY-MM-DD`).
- `end_date` (`string`): Merge/completion date (`YYYY-MM-DD`).
- `elapsed_days` (`int`): Total days elapsed.

#### Final Artifacts Structure
Each item in `final_artifacts` list must contain:
- `name` (`string`): Deliverable item name.
- `path` (`string`): File path inside the repository.
- `type` (`string`): One of `"spec"`, `"implementation"`, `"report"`.
