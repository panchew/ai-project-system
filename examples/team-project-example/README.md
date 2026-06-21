# Taskflow — Team Project Example

This directory is a **ready-to-reference example** of the AI Project System applied to a real-world team project. It shows how a 5-person team builds a Task Management App using the Phase → Milestone → Epic governance model.

Use it as a template when starting a new project or onboarding new team members.

---

## What This Example Shows

- A complete **Phase P1** structure with 3 Milestones and 9 Epics
- **5 team roles** with explicit decision authorities (CFO, Phase Lead, Developer 1, Developer 2, Reviewer)
- **Real-looking artifact files** (Completion Notices, Review Decisions, Delivery Notices) in the standard format
- A **rejected Epic** (E1.2) showing the rework cycle from rejection to acceptance
- A **Bugfix Epic (B1.1)** using the expedited workflow
- **Parallel Epic execution** (E1.1 and E1.2 run concurrently in M1)
- A step-by-step **walkthrough** from Phase approval to Delivery Notice

---

## Directory Structure

```
team-project-example/
├── .ai-project/
│   └── artifacts/
│       ├── completion-notices/   ← Epic agents submit these when done
│       ├── review-decisions/     ← Phase Lead issues Accept or Reject
│       └── delivery-notices/     ← Epic agents produce after merge
├── docs/
│   └── phases/
│       └── P1__Task_Management_App/
│           ├── P1__phase-spec.md              ← Phase specification
│           ├── M1__Core_Backend/
│           │   ├── M1__milestone-spec.md
│           │   ├── E1.1__spec__user-authentication.md
│           │   ├── E1.2__spec__task-crud-api.md
│           │   └── E1.3__spec__database-schema.md
│           ├── M2__Frontend/
│           │   ├── M2__milestone-spec.md
│           │   ├── E2.1__spec__login-ui.md
│           │   ├── E2.2__spec__task-dashboard.md
│           │   └── E2.3__spec__search-and-filter.md
│           └── M3__Polish_and_Deploy/
│               ├── M3__milestone-spec.md
│               ├── E3.1__spec__performance-optimization.md
│               ├── E3.2__spec__ci-cd-pipeline.md
│               └── B1.1__spec__auth-session-bugfix.md  ← Bugfix Epic
├── src/                  ← Placeholder (real projects have code here)
├── tests/                ← Placeholder (real projects have tests here)
├── README.md             ← This file
├── TEAM_SETUP.md         ← Team roles and decision authorities
└── WALKTHROUGH.md        ← Step-by-step one full Epic cycle
```

---

## Key Files to Read First

| File | What it explains |
|------|-----------------|
| [TEAM_SETUP.md](TEAM_SETUP.md) | Who does what, who decides what |
| [WALKTHROUGH.md](WALKTHROUGH.md) | Step-by-step: one Epic from start to finish |
| [P1__phase-spec.md](docs/phases/P1__Task_Management_App/P1__phase-spec.md) | What Phase P1 covers and its exit criteria |
| [M1__milestone-spec.md](docs/phases/P1__Task_Management_App/M1__Core_Backend/M1__milestone-spec.md) | How Milestone M1 is structured and sequenced |

---

## Example Project: Taskflow (Task Management App)

This example uses a fictional **Task Management App** called Taskflow as its project domain. The project, team members, and artifact contents are entirely fictional and exist only for illustration.

**Fictional team:**
- Morgan Chen — CFO
- Alex Rivera — Phase Lead
- Jamie Park — Developer 1
- Sam Torres — Developer 2
- Casey Kim — Reviewer

---

## How to Use This as a Template

### Starting a New Project

1. **Copy the directory structure** into your new repository:
   ```
   examples/team-project-example/docs/phases/  → your-repo/docs/phases/
   examples/team-project-example/.ai-project/  → your-repo/.ai-project/
   ```

2. **Replace the content** of each spec file with your project's actual scope. Keep the YAML front-matter structure identical, just update field values.

3. **Fill in TEAM_SETUP.md** with your team's real names, roles, and email addresses.

4. **Read the governance documents** before executing your first Epic:
   - `governance/PROJECT-SYSTEM-GUIDELINES.md`
   - `governance/systems/artifact-communication-protocol.md`
   - `governance/systems/roles-authorization-team-governance.md`

### Adapting the Artifact Format

Every artifact file follows this structure:
```
<ISO-timestamp>__<P#-M#-E#.#>__<artifact-type>.md
```

Example: `2026-06-02T10-00-00Z__P1-M1-E1.1__completion-notice.md`

The timestamp uses hyphens instead of colons for filesystem compatibility.

All three artifact types (Completion Notice, Review Decision, Delivery Notice) have YAML front-matter + Markdown body. See `governance/systems/artifact-communication-protocol.md` for the full field reference.

### Adapting the Bugfix Workflow

When a production bug is discovered:
1. Report to HQ Chat with severity and scope estimate
2. HQ Agent evaluates and may approve a Bugfix Epic (B#.# ID)
3. Use the expedited path: HQ review within 4 hours, branch `bugfix/B#.#`
4. See `B1.1__spec__auth-session-bugfix.md` for the minimal spec format

See `governance/systems/bugfix-epic-workflow.md` for the complete rules.

---

## What Makes a Good Epic Spec

Looking at the examples in this directory:

**Realistic scope:** Each Epic is one unit of work completable in 1-4 days. Not a feature; not a task — an Epic.

**Distinct content:** E1.1 (Auth), E1.2 (Task CRUD), E1.3 (Schema) are genuinely different work with different deliverables, not variations of the same thing.

**Clear Definition of Done:** Each DoD item is a checkbox that the implementing developer can verify objectively (not "done when it feels right").

**Named decision authorities:** The `Execution Notes` section in each Epic spec names who implements and who reviews.

---

## Validation

The artifact files in this example are validated by:

```bash
pytest tests/test_example_project_artifacts.py -v
```

This test suite (14 test cases) checks:
- YAML front-matter parses without errors
- All required fields are present for each artifact type
- Artifact filenames match the naming convention
- At least one Accept and one Reject review decision exist
- Epic IDs follow the `P#-M#-E#.#` pattern
- Team roles in artifacts match `TEAM_SETUP.md`

---

## Reference

- [AI Project System Governance](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md)
- [Artifact Communication Protocol](https://github.com/panchew/ai-project-system/blob/master/governance/systems/artifact-communication-protocol.md)
- [Roles and Authorization Guide](https://github.com/panchew/ai-project-system/blob/master/governance/systems/roles-authorization-team-governance.md)
- [Bugfix Epic Workflow](https://github.com/panchew/ai-project-system/blob/master/governance/systems/bugfix-epic-workflow.md)
