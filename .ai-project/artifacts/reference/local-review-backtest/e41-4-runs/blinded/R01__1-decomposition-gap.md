# Blinded run record — R01

**Packet:** `packet-1-decomposition-gap.md` | **Attempt:** 1 | **Opaque run ID:** `R01`

**Stop/finish reason:** `stop` | **exit:** 0
**Elapsed (s):** 74.278 | **No tuning applied:** true | **Sampling:** vendor defaults

**Model response (verbatim, unedited):**

````text
NOT SOUND

## Item-by-item trace

### Milestone Definition of Done

| # | Milestone DoD item | Guaranteed by | Verdict |
|---|---|---|---|
| 1 | "E33.1, E33.2, and E33.3 each meet their Definition of Done above" | E33.1/E33.2/E33.3 DoDs (each epic spec's DoD reproduces the milestone's Epic-Detail DoD verbatim) | Covered |
| 2 | "All three epic branches merged to `milestone/M33`" | Each epic DoD: "all changes on `epic/P10-M33-E33.x`; PR opened to `milestone/M33`"; the merge itself is the Milestone Chat's act | Covered |
| 3 | "Both `home_finance` and `local-agent-runner` are stamped `framework_version: v7.0.0` (confirmable), **each with a committed run record** for at least one real Agentic/Local epic executed under the fixed posture" | Stamp half: E33.1. Run-record half: **nothing** | **NOT COVERED** |
| 4 | "A documented, repeatable enrolled-project v7.0.0 bump procedure exists and shows evidence of application to the pair" | E33.1 DoD 1–3 ("documented … and is repeatable (a reader could follow it against a project the procedure was never run on)"; "Both proving-pair projects are stamped …"; "Confirmation evidence is committed …") | Covered |
| 5 | "The Ollama-vs-llama.cpp+Qwen3.6 runtime decision is recorded with the run's own reasons" | E33.2 DoD 3 (four dimensions named) | Covered |
| 6 | "Real burn/validation data from the run exists in the governance record, with an explicit, evidence-backed honesty judgment on `measure-token-burn`'s numbers for that run" | E33.3 DoD 1 and 4 | Covered (for whichever run E33.2 produced) |
| 7 | "Full suite green on `milestone/M33` for changes touching this repo (363 baseline …)" | E33.1/E33.2/E33.3 DoD suite clauses | Covered |
| 8 | "Milestone Closure Declaration produced" | Milestone Chat's own artifact, outside epic scope | N/A — correctly not an epic obligation |

### Milestone Acceptance Criteria

| # | Milestone AC | Guaranteed by | Verdict |
|---|---|---|---|
| 1 | "`framework_version: v7.0.0` is stamped and confirmable in both proving-pair projects, **and each has a committed run record** for at least one real Agentic/Local epic under the fixed posture (E33.1, E33.2)" | E33.1 for the stamps; **no epic** for "each has a committed run record" | **NOT COVERED** |
| 2 | "The runtime decision … recorded in the run evidence with the run's own reasons — not an abstract memo" | E33.2 AC 1 ("traceable to a real run's observations — a reader sees *which run* produced *which reasons* across the four dimensions") | Covered |
| 3 | "Real burn/validation data … with a stated, evidence-backed judgment **that** `measure-token-burn`'s numbers for that run **can be trusted**" | E33.3 DoD 4 / AC 1 — but these guarantee only "can / cannot be trusted, because …" | Partially covered — see secondary finding below |
| 4 | "A documented, repeatable v7.0.0 bump procedure exists and has been applied to the pair" | E33.1 DoD 1–2, AC 1 | Covered |
| 5 | "Every decision (runtime, measurement-trust) traces to a real run … Where a run could not complete, an explicit blocker-and-escalation stands in its place" | E33.2 DoD 4 + AC 3; E33.3 Hard Constraint | Covered for the run(s) actually attempted — but compounds finding 1 (see below) |
| 6 | "The full suite is green at milestone delivery for changes touching this repo" | All three epic DoDs | Covered |

---

## Primary finding — the pair vs. the single run

The milestone commits to a real governed run on **both** proving-pair projects. E33.2 commits to a run on **one**.

Milestone side (DoD item 3):

> "Both `home_finance` and `local-agent-runner` are stamped `framework_version: v7.0.0` (confirmable), **each with a committed run record for at least one real Agentic/Local epic executed under the fixed posture**"

Milestone side (AC 1):

> "`framework_version: v7.0.0` is stamped and confirmable in both proving-pair projects, and **each has a committed run record** for at least one real Agentic/Local epic under the fixed posture (E33.1, E33.2)."

Milestone side (Goal 1):

> "`home_finance` and `local-agent-runner` are **each** stamped `framework_version: v7.0.0` (confirmable) and **each** has carried at least one real Agentic/Local epic end-to-end under the fixed posture, with a committed run record"

Epic side (E33.2 DoD, first item):

> "At least one real Agentic/Local epic ran on **a proving-pair project** under the fixed posture, and its run record is committed to the governance record"

And E33.2 makes the singular reading explicit rather than incidental — its Design Decision 1 is headed:

> "**Which proving-pair project's first real epic to run**" … "**`local-agent-runner`'s own work.** … **`home_finance`'s own work.** … Choose on the basis of which offers a **genuine, scoped, reviewable** unit of real work"

So a fully compliant E33.2 delivery — one run on one chosen project, everything else spotless — leaves the milestone DoD and AC 1 unsatisfiable. Nothing in E33.1 (which explicitly disclaims this: "**Run the first real Agentic/Local epic or make the runtime decision** — that is E33.2") or E33.3 (which reads E33.2's data and forbids "**Re-run or re-scope E33.2** … No new Agentic/Local run") makes up the difference.

The blocker escape hatch does not close the gap. E33.2 DoD item 4 reads:

> "**Any project whose run could not complete** has an explicit blocker record + escalation (not a substituted decision)"

That clause is scoped to a run that was attempted and failed. Under E33.2's Design Decision 1, the un-chosen project's run is never attempted at all, so it is not a project "whose run could not complete" — no blocker record is owed for it, and none is required by any DoD item. The result is a project with neither a run record nor a blocker record, which is exactly the state milestone AC 5 was written to forbid ("Where a run could not complete, an explicit blocker-and-escalation stands in its place").

Note the defect originates upstream: the milestone spec's own Epic Detail for E33.2 says "at least one real Agentic/Local epic executed on **a** proving-pair project", and its In Scope says "running a **genuine** epic of **a target project's** own work" — both singular, contradicting the milestone's own Goal 1, DoD, and AC 1, which are plural. The Epic Chats faithfully implemented the singular Epic Detail. But Stage-2 soundness is judged against the milestone's DoD and Acceptance Criteria, and those are not delivered. The fix is either to make E33.2's DoD require a run (or an explicit blocker-and-escalation) for **each** of the two projects, or — if one run was genuinely the intent — to amend the milestone DoD/Goal 1/AC 1 down to one project and accept that "the proving pair carries at least one real governed epic" means the pair collectively, not each member. That amendment has consequences worth surfacing, since E33.1 bumps both projects and M34's fleet roll-forward inherits a runtime decision evidenced on only one of them.

## Secondary finding — AC 3's outcome guarantee

Milestone AC 3:

> "Real burn/validation data from the run exists in the repo, with a stated, evidence-backed judgment **that `measure-token-burn`'s numbers for that run can be trusted** (E33.3, P9-GH-2)."

E33.3 AC 1:

> "The repo records a stated judgment — **"the run's numbers can / cannot be trusted, because …"** — backed by the captured data; **there is no third state where the check was skipped**"

AC 3, read strictly, requires a *positive* trust finding; E33.3 guarantees only that a judgment in either direction is recorded. An E33.3 that honestly concludes "cannot be trusted, because the tool mis-parses the newer run-metadata layout" fully meets its own DoD while failing milestone AC 3 on its face. This is milestone-internal drafting looseness rather than a decomposition error — the milestone's own DoD item 6 ("an explicit, evidence-backed honesty judgment"), its E33.3 Epic-Detail AC ("can/cannot be trusted"), and its Notes all sanction either outcome, so E33.3 is aligned with the milestone's evident intent. AC 3 should be reworded to match ("a stated judgment on whether … can be trusted") so the milestone cannot be failed by an honest negative result.

## What is solidly covered

- E33.1's DoD is a clean superset of the milestone's E33.1 obligations, and it correctly hardens the "stamped **and** confirmable" bar into evidence that is verifiable from this repo (target repo + commit + stamp location + method), which is what milestone AC 1's stamp half and AC 4 need.
- The cross-repo record/evidence split is carried verbatim into all three epics, so "committed" resolves consistently and no epic promises to merge target-repo code onto `phase/P10`.
- The Hard Constraint is embedded in each epic with the correct local bite (sequencing gate in E33.1, run-authenticity in E33.2, judgment-must-be-about-real-numbers in E33.3), so milestone AC 5's "no un-run abstraction" is genuinely enforced for the work each epic does undertake.
- The dependency chain E33.1 → E33.2 → E33.3 is stated identically on both sides, and E33.3's non-negotiables (capture + judgment, extent scalable) match the milestone's "conditional in extent, not in existence".
````
