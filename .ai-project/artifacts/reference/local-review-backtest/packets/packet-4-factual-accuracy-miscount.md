<!-- ===================================================================== -->
<!-- AUDIT HEADER — read by humans, NEVER sent to the model.               -->
<!-- The prompt is EXACTLY the bytes after the PROMPT-BEGIN marker line.   -->
<!-- ===================================================================== -->

# Packet 4 — factual-accuracy judgment (ground truth: MISCOUNT, 21 claimed vs 20 actual)

**Defect (E35.5 spec, row 4):** E34.2's delivery notice asserted `footboard`'s dirty working tree held
**21 entries (2 modified + 19 untracked)**. The verbatim porcelain it summarises holds **20 (2 + 18)**.
Corrected after the fact in `c64ebe7`.

**Note on the two directions:** the *substantive* claim the count supports — that the tree is
identical before and after — is **correct**. A reviewer that rejects the identity claim itself scores a
**false alarm**; only the arithmetic is wrong.

**Provenance — verbatim from committed files on `milestone/M35`:**

- Section 1 is `git show cd45828:docs/phases/P10__.../P10-M34-E34.2__delivery-notice.md`, the
  pre-correction text (`cd45828` is the notice's own commit; `c64ebe7` is the later fix).
- Section 2 is the verbatim `footboard` pre-state block from
  `docs/phases/P10__.../P10-M34-E34.2__confirmation-evidence.md` §`footboard` → Pre-state (verbatim).

**Excised (blinding record) — none of the following appears below:**

- Commit `c64ebe7` and its message ("Said 21 entries (2 modified + 19 untracked); actual is 20
  (2 + 18)") — states the finding outright.
- The corrected text of the delivery notice, i.e. every version at or after `c64ebe7`.
- The M34 Milestone Closure Declaration.
- The rest of `P10-M34-E34.2__confirmation-evidence.md` beyond the verbatim porcelain block, which
  carries E34.2's own review conclusions.

<!-- PROMPT-BEGIN -->
You are performing a **Stage-2 review** of a governance delivery notice under the AI Project System
framework. A delivery notice makes factual claims about work that was performed; your job as reviewer
is to check those claims against the underlying evidence and decide whether the notice can be
**ACCEPTED** as accurate, or must be **REJECTED** for correction.

Background: an epic bumped three enrolled repositories to a new framework version. Two of the three
had dirty working trees — uncommitted work belonging to their owners — and the epic was required to
prove that this owner work survived the bump untouched.

---

## 1. The claim, as written in the delivery notice

> ## Proof each dirty target's owner work survived
>
> **`footboard`** — `git status --porcelain` after the bump is **identical to the pre-state, line for
> line** (21 entries: 2 modified tracked + 19 untracked). Corroborated by the commit's own contents:
>
> ```
> $ git show --stat --oneline HEAD
> b00bb16 chore(governance): bump to framework v7.0.0
>  .ai-project.yml                        |  10 +-
>  .ai-project/agents/governance.agent.md | 261 +++++++++++++++++++++++++++++++++
>  .governance                            |   2 +-
>  3 files changed, 270 insertions(+), 3 deletions(-)
> ```

---

## 2. The underlying evidence the claim summarises

This is the verbatim pre-state capture for `footboard`, recorded before the bump:

```
$ git rev-parse --abbrev-ref HEAD
milestone/M1
$ git log --oneline -1
51b5cc6 P1: Create milestone specs and execution chat starters
$ git status --porcelain
 M docs/phases/P1__Online_1v1_MVP/P1__phase-spec.md
 M genesis.md
?? .ai-project/artifacts/hq-openers/
?? .ai-project/artifacts/phase-starters/
?? .ai-project/artifacts/system-requests/
?? .ai-project/artifacts/system-responses/
?? .ai-project/seed.md
?? docs/phase-execution-chat-starter.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.1-epic-execution-chat-starter.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.1__spec__WebSocket_Service_Implementation.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.2-epic-execution-chat-starter.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.2__spec__Rooms_Manager.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.3-epic-execution-chat-starter.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.3__spec__Engine_Integration.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.4-epic-execution-chat-starter.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.4__spec__Clock_Management_System.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.5-epic-execution-chat-starter.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.5__spec__Match_Persistence.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.6-epic-execution-chat-starter.md
?? docs/phases/P1__Online_1v1_MVP/P1-M1-E1.6__spec__Connection_Handling.md
$ git submodule status
 a59509f45b410f34dbfa617ede554bcc3b15de41 .governance (v5.1.0)
$ ls .ai-project/agents/
ls: cannot access '.ai-project/agents/': No such file or directory
```

The post-bump `git status --porcelain` was byte-identical to the listing above.

---

## 3. Your task

State your decision as **ACCEPT** or **REJECT** on its own line, then give your reasons.

Check every factual assertion in section 1 against the evidence in section 2. For each assertion,
say whether it holds. If any assertion does not hold, state precisely what is wrong and what the
correct value is.
