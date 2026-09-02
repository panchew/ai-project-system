# Blinded run record — R02

**Packet:** `packet-1-decomposition-gap.md` | **Attempt:** 2 | **Opaque run ID:** `R02`

**Stop/finish reason:** `stop` | **exit:** 0
**Elapsed (s):** 61.861 | **No tuning applied:** true | **Sampling:** vendor defaults

**Model response (verbatim, unedited):**

````text
NOT SOUND

## Item-by-item trace

### Milestone Definition of Done

**1. "E33.1, E33.2, and E33.3 each meet their Definition of Done above"** — guaranteed trivially by each epic meeting its own DoD, and each epic's DoD does restate its milestone-level Epic Detail DoD faithfully. Covered.

**2. "All three epic branches merged to `milestone/M33`"** — each epic DoD ends with "PR opened to `milestone/M33`"; the merge itself is the Milestone Chat's act. Normal division of labour, not a gap.

**3. "Both `home_finance` and `local-agent-runner` are stamped `framework_version: v7.0.0` (confirmable), each with a committed run record for at least one real Agentic/Local epic executed under the fixed posture"** — **NOT guaranteed.** The stamp half is covered by E33.1. The run-record half is not covered by any epic.

Milestone side:
> "Both `home_finance` and `local-agent-runner` are stamped … **each with a committed run record for at least one real Agentic/Local epic** executed under the fixed posture"

E33.2 side (its entire DoD commitment on this point):
> "- [ ] At least one real Agentic/Local epic ran on **a proving-pair project** under the fixed posture, and its run record is committed to the governance record"

"A proving-pair project" is one project, not both. This is not an accident of phrasing — E33.2 is built around picking one:
> "### 1. Which proving-pair project's first real epic to run … **Choose** on the basis of which offers a genuine, scoped, reviewable unit of real work"

and its Scope of Work §1: "**Select** the proving-pair project (Design Decision 1)". Its Deliverables likewise say "at least one real Agentic/Local epic executed on **a** proving-pair project", singular. There is no clause anywhere in E33.2 that obliges a second run on the other project.

The blocker escape hatch does not close this. E33.2's DoD says:
> "- [ ] **Any project whose run could not complete** has an explicit blocker record + escalation (not a substituted decision)"

A project that was deliberately not selected as the run target is not a project "whose run could not complete" — no run was attempted, so no blocker exists to record. So under E33.2 as written, the unchosen project ends the milestone with neither a run record nor a blocker record, and milestone DoD item 3 and AC 1 are unmet while every epic DoD is fully satisfied. That is the definition of an unsound decomposition.

Note the milestone spec is itself the origin of the slip: its Goal 1 and DoD/AC say **each**, while its own §Epic Detail → E33.2 DoD says "**a** proving-pair project". E33.2 inherited the weaker of the two. The mismatch is real either way, because the milestone's DoD and Acceptance Criteria are what the decomposition must satisfy.

Corroborating signal: E33.3's grounding, written after E33.2 was executed, cites exactly one run directory — `.ai-project/artifacts/agentic-runs/P10-M33-E33.2/` with "Run A `qwen2.5-coder:14b`" and "Run B `qwen3-coder:30b`" — i.e. two model runs of one epic on one target, not one governed epic per proving-pair project. The gap materialised in practice.

**4. "A documented, repeatable enrolled-project v7.0.0 bump procedure exists and shows evidence of application to the pair"** — covered by E33.1 DoD items 1–3 ("documented with its mechanism and reasoning, and is repeatable (a reader could follow it against a project the procedure was never run on)"; both projects stamped; confirmation evidence citing repo + commit + stamp location + verification method).

**5. "The Ollama-vs-llama.cpp+Qwen3.6 runtime decision is recorded with the run's own reasons"** — covered by E33.2 DoD item 3, including the four dimensions (quality, throughput, loadability, review burden).

**6. "Real burn/validation data from the run exists in the governance record, with an explicit, evidence-backed honesty judgment"** — covered by E33.3 DoD items 1 and 4.

**7. "Full suite green on `milestone/M33` for changes touching this repo (363 baseline …)"** — each epic carries the clause; E33.3 additionally guards the `measure-token-burn` behaviour contract. Covered.

**8. "Milestone Closure Declaration produced"** — Milestone Chat's artifact, correctly outside epic scope.

### Milestone Acceptance Criteria

**AC 1** — "`framework_version: v7.0.0` is stamped and confirmable in both proving-pair projects, **and each has a committed run record** for at least one real Agentic/Local epic under the fixed posture." First clause: E33.1. Second clause: **not guaranteed** — same mismatch as DoD item 3, quoted above.

**AC 2** — traceability of the runtime decision to a real run: E33.2 AC 1 ("a reader sees *which run* produced *which reasons* across the four dimensions"). Covered.

**AC 3** — "Real burn/validation data … with a stated, evidence-backed judgment that `measure-token-burn`'s numbers for that run **can be trusted**." E33.3 delivers "the run's numbers **can / cannot** be trusted, because …". Secondary, non-fatal mismatch: a well-formed "cannot be trusted" finding fully satisfies E33.3 but does not literally satisfy AC 3's positive wording. The milestone's own §Epic Detail E33.3 AC and §Notes make clear the intent is the honesty judgment, not a mandated verdict, so I read this as sloppy AC drafting rather than a coverage hole — but it should be corrected to "can or cannot be trusted, stated and evidence-backed" so the milestone cannot be failed by an honest negative result.

**AC 4** — repeatable bump procedure applied to the pair: E33.1 DoD + AC. Covered.

**AC 5** — "Every decision traces to a real run … Where a run could not complete, an explicit blocker-and-escalation stands in its place": E33.2 and E33.3 Hard Constraint sections and DoD items cover the attempted-but-blocked case. They do **not** cover the never-attempted case, which is the mechanism by which AC 1 fails.

**AC 6** — suite green: covered by all three epics.

## Verdict

One requirement — the milestone's headline "proving pair" claim, appearing in Goal 1, DoD item 3, and AC 1 — is guaranteed by no epic. E33.1 guarantees the *bump* on both projects; E33.2 guarantees a real governed run on only **one**, by explicit design. All three epics can pass their own DoDs in full while `home_finance` or `local-agent-runner` ends M33 stamped at v7.0.0 but never having carried a real governed epic — leaving the milestone's central assertion ("Adoption is demonstrated, not asserted — the proving pair carries at least one real governed epic end-to-end") half-unproven, and half of AC 1 unmet.

Minimal fix: amend E33.2's DoD to "at least one real Agentic/Local epic ran on **each** proving-pair project … and any project whose run could not complete **or was not attempted** has an explicit blocker record + escalation", and reconcile the milestone's §Epic Detail → E33.2 DoD ("a proving-pair project") with its own DoD/AC ("each"). Alternatively, if a single-target run is genuinely the intent, weaken milestone DoD item 3 / AC 1 to match and drop the "each" language from Goal 1 — but that materially reduces what the milestone proves and should be a recorded, ratified scope change, not an inherited drafting slip.
````
