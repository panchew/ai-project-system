# M7 Execution Setup Instructions

**Issued by:** Milestone Chat (M7 — CLI Initialization Tool)  
**Date:** 2026-04-27  
**Authority:** Milestone Chat planning session authorization  
**Recipient:** Coding Agent(s) working on M7 Epic closures

---

## Context

The Milestone M7 planning session (Milestone Chat) has completed and delivered:

1. ✅ **E7.1 spec** — Design locked, Phase Chat accepted
2. ✅ **E7.2 spec + implementation** — Staged on `epic/E7.2` branch, ready to commit
3. ✅ **E7.3 spec** — Untracked, awaiting branch setup
4. ✅ **E7.4 spec** — Untracked, awaiting branch setup

**Current git state:**
- Branch `epic/E7.2` exists and has staged files ready for commit
- Branch `milestone/M7` does **NOT** exist yet (must be created)
- E7.1, E7.3, E7.4 epic branches do **NOT** exist yet (must be created)
- E7.1 spec files are untracked (must be moved to `epic/E7.1` branch)

---

## Your Task

You must **establish the proper git infrastructure and close E7.1 formally** before E7.2 implementation can be merged. This is a prerequisite for M7 execution.

### Step 1: Create `milestone/M7` Branch

The milestone branch is the target for all epic PRs. Create it from the latest `milestone/M6`:

```bash
git fetch origin
git checkout -b milestone/M7 origin/milestone/M6
git push -u origin milestone/M7
```

**Verify:**
```bash
git branch -a | grep milestone/M7
# Expected: * milestone/M7 (or remotes/origin/milestone/M7 if on different branch)
```

---

### Step 2: Create `epic/E7.1` Branch and Close E7.1

E7.1 is a **planning-only epic** (no code implementation). It needs formal closure with a completion report and PR.

#### 2a. Create the branch

```bash
git checkout -b epic/E7.1 milestone/M7
```

#### 2b. Move the untracked E7.1 spec files to this branch

The following files are currently untracked in the working directory:
- `docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.1__spec__cli-architecture.md`

Add them to the branch:

```bash
git add docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.1__spec__cli-architecture.md
```

#### 2c. Create an E7.1 completion report

Create a file: `docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.1__completion__cli-architecture.md`

Content template:

```markdown
---
project: ai-project-system
phase: P2
milestone: M7
epic: E7.1
type: completion
status: complete
completed_date: 2026-04-27
---

# Epic E7.1 Completion Report — Design CLI Architecture & Hierarchical Docs Structure

## Delivered

- [x] Epic specification locked: `P2-M7-E7.1__spec__cli-architecture.md`
- [x] CLI command interface fully documented (all flags, arguments, options, defaults)
- [x] Folder hierarchy specified with justification for each directory
- [x] `.ai-project.yml` initialization format specified
- [x] CLI flow documented (happy path + error paths)
- [x] Platform support requirements defined (macOS 10.14+, Linux 18.04+, Windows WSL2)
- [x] Error messages and user feedback specified
- [x] Success metrics for E7.2 verification defined

## Specification Status

**Locked and Ready for Implementation:** E7.2 can implement per the specification without design ambiguity.

## Phase Chat Acceptance

**Accepted:** 2026-04-27 by Phase Chat (P2 — Adoption Architecture & Multi-Project Support)

**Acceptance Review:**
- ✅ CLI interface fully documented
- ✅ Folder hierarchy specified
- ✅ `.ai-project.yml` format clear
- ✅ Design aligns with P2 architecture
- ✅ E7.2 can implement without ambiguity

## Next Steps

E7.1 is closed. E7.2 implementation (Implement CLI Scaffolding) is authorized and ready to proceed.
```

#### 2d. Commit the E7.1 completion

```bash
git add docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.1__completion__cli-architecture.md
git commit -m "E7.1: Design CLI Architecture & Hierarchical Docs Structure

- Specification locked and Phase Chat accepted
- CLI interface documented with all flags and options
- Folder hierarchy specified with justifications
- Platform support and error handling documented
- Ready for E7.2 implementation"
```

#### 2e. Create PR from `epic/E7.1` to `milestone/M7`

```bash
git push -u origin epic/E7.1
```

Then create a pull request:
- **Title:** `E7.1: Design CLI Architecture & Hierarchical Docs Structure`
- **Base:** `milestone/M7`
- **Head:** `epic/E7.1`
- **Description:**

```markdown
## E7.1 — Design CLI Architecture & Hierarchical Docs Structure

**Planning Epic — Closed**

### Summary
Design the `ai-project init` CLI command structure, interface, folder hierarchy, and workflows. Specification locked and Phase Chat accepted.

### Deliverables
- [x] Epic specification: `P2-M7-E7.1__spec__cli-architecture.md`
- [x] Completion report: `P2-M7-E7.1__completion__cli-architecture.md`

### Status
✅ **Phase Chat Acceptance:** 2026-04-27

### Next
Awaiting merge authorization from Phase Chat. E7.2 implementation (Implement CLI Scaffolding) is authorized to proceed pending this merge.
```

---

### Step 3: Move E7.2 to Proper Branch and Create PR

E7.2 has already been implemented and has staged files on `epic/E7.2`. You need to commit and create the PR.

#### 3a. Commit the staged files

You are currently on `epic/E7.2`. Verify the staged files:

```bash
git status
```

Expected output:
```
Changes to be committed:
  - bin/ai-project-init
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.2__completion__cli-scaffolding.md
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.2__spec__cli-scaffolding.md
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.2__test-report.md
```

Commit:

```bash
git commit -m "E7.2: Implement ai-project init Command (Scaffolding)

- Implemented bash CLI that scaffolds P2 project structure
- Creates docs/, .github/agents/, .gitignore, README.md, .ai-project.yml
- Validates project names per spec
- Initializes git repository with initial commit
- Handles error cases: invalid name, existing directory, git missing
- Provides clear user feedback
- All tests pass: happy path, error cases, flags
- Deployment: /bin/ai-project-init"
```

#### 3b. Push and create PR

```bash
git push -u origin epic/E7.2
```

Create a pull request:
- **Title:** `E7.2: Implement ai-project init Command (Scaffolding)`
- **Base:** `milestone/M7`
- **Head:** `epic/E7.2`
- **Description:**

```markdown
## E7.2 — Implement `ai-project init` Command (Scaffolding)

**Implementation Epic — Ready for Review**

### Summary
Implement the `ai-project init` bash CLI that scaffolds a new P2-conformant project with correct folder structure and git initialization.

### Deliverables
- [x] CLI command: `bin/ai-project-init`
- [x] Epic specification: `P2-M7-E7.2__spec__cli-scaffolding.md`
- [x] Completion report: `P2-M7-E7.2__completion__cli-scaffolding.md`
- [x] Test report: `P2-M7-E7.2__test-report.md`

### Tests Passed
- [x] Happy path: `ai-project init test-project` creates all required folders
- [x] Project name validation: rejects invalid names, suggests corrections
- [x] Git initialization: repository created with initial commit
- [x] `.ai-project.yml` creation: valid YAML with governance reference
- [x] Error handling: directory exists, git missing, invalid flags
- [x] Platforms: tested on Linux (Windows WSL2 compatible)

### Status
✅ **Phase Chat Acceptance:** 2026-04-27

### Next
Awaiting HQ authorization to merge. E7.3 implementation (Govern Submodule Integration) is blocked pending this merge.
```

---

### Step 4: Create `epic/E7.3` and `epic/E7.4` Branches (Setup Only)

These epics are not yet ready for implementation, but the branches should exist for future work.

#### 4a. Create `epic/E7.3` branch

```bash
git checkout -b epic/E7.3 milestone/M7
# Don't push yet
```

#### 4b. Create `epic/E7.4` branch

```bash
git checkout -b epic/E7.4 milestone/M7
# Don't push yet
```

Return to `master` or `milestone/M7`:

```bash
git checkout milestone/M7
```

---

### Step 5: Update M7 Milestone Spec (Untracked File)

The M7 milestone spec file is currently untracked:
- `docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7__milestone.md`

This file should be added to `milestone/M7` branch:

```bash
git checkout milestone/M7
git add docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7__milestone.md
git commit -m "Add M7 Milestone specification"
git push origin milestone/M7
```

---

### Step 6: Summary of Git State After Setup

After completing all steps, your git state should be:

```
Branches:
  milestone/M7 (created, pushed)
    ├── epic/E7.1 (PR created, awaiting merge)
    ├── epic/E7.2 (PR created, awaiting merge)
    ├── epic/E7.3 (created, not yet pushed)
    └── epic/E7.4 (created, not yet pushed)

Files in place:
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7__milestone.md
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.1__spec__cli-architecture.md
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.1__completion__cli-architecture.md
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.2__spec__cli-scaffolding.md
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.2__completion__cli-scaffolding.md
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.2__test-report.md
  - bin/ai-project-init (executable)
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.3__spec__governance-integration.md
  - docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M7-E7.4__spec__hq-agent-deployment.md

Pull Requests:
  - epic/E7.1 → milestone/M7 (awaiting merge)
  - epic/E7.2 → milestone/M7 (awaiting merge)
```

---

## Authorization & Governance

**This setup is authorized by Milestone Chat** per the Epic Execution Chat Starters issued for each Epic.

**Governance rules in effect:**
1. All commits must include clear commit messages referencing the Epic
2. PRs must include proper descriptions (use templates above)
3. Do NOT merge PRs; await Phase Chat authorization
4. E7.3 and E7.4 cannot begin implementation until E7.2 is merged
5. All work follows PROJECT-SYSTEM-GUIDELINES.md v2.0.0

---

## Questions?

If you encounter issues:
- **Design clarifications:** Refer to the Epic specs
- **Git problems:** Ensure `origin` is configured correctly and branches exist
- **Governance questions:** Escalate to Phase Chat

**Ready to proceed?**
