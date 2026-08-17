---
artifact_type: agentic_run_evidence
artifact_version: 1.0
timestamp: 2026-08-17T17:23:00Z
epic_id: P11-M40-E40.1
milestone_id: P11-M40
phase_id: P11
project_name: ai-project-system
---

# Unattended dispatch evidence — P11-M40-E40.1

**Three runs, dispatched by `drivr`'s scheduler with no human starting any of them.** This is
Deliverable D3, and it is committed here rather than in `drivr` because **`drivr` has no git
remote**: a Drivr-side artifact is not independently retrievable, so *"verify the push at
`origin`"* is not performable there and a reviewer must be handed the evidence in a repository
that does have one.

## What makes "unattended" checkable rather than asserted

The claim is not that a human never typed anything — a human started the scheduler. The claim
is that **no human started any of these runs**, and the sequence is what evidences it:

| Time (UTC) | Event | Artifact that shows it |
|---|---|---|
| **17:21:37** | `bin/drivr-serve` started. Queue **empty**, no journal, no runs directory. | `serve-started-at.txt`, `serve.log` |
| **17:22:02** | Three jobs enqueued by a **separate process** (`--enqueue` writes a file and dispatches nothing). | `runs/*/job.json` → `enqueued_at` |
| 17:22:02 → 17:23:07 | The scheduler noticed each job on its poll loop and dispatched it. | `journal.ndjson` → `dispatched_at`, `dispatched_by`, `dispatched_by_pid` |

`--enqueue` and `serve` are deliberately separate operations: if the same command both queued
and ran the work, *"no human started this run"* would not be a checkable statement about
anything.

## The three runs, and why three

They were not chosen to all succeed. Two were designed, the third's outcome was not — and it
is the most informative of them.

| Job | Project | Expectation | Verdict (`drivr.judgment`) | Disposition (scheduler) |
|---|---|---|---|---|
| `…-f58f17ea` | ai-project-system | `inspecting` | `no-effects-observed` / `no-effects` | **`done`** — `read_only_completion: true` |
| `…-39168925` | drivr | `mutating` | **`effects-verified`** / `covering-verification` | **`done`** |
| `…-efcf592b` | drivr | `inspecting` | `no-effects-observed` / `no-effects` | **`not-done`** |

**Run 1 is the §F5 case, live.** The judgment says `no-effects-observed`, whose
`reading()` is `did-not-complete`. The run did exactly what it was asked to do. The scheduler
dispositions it `done` because the job was dispatched to inspect, and records the divergence
in `disposition.txt` rather than resolving it silently.

**Run 2 is what was unreachable before this epic.** `EFFECTS_VERIFIED` from a **live** OpenCode
run, reached through E39.1's ordering rule (`covering-verification`) on a ledger projected from
the engine's own stream. `verdict.txt` carries the whole reasoning, including the four signals
it ignored and why.

**Run 3 was not planned and is the sharpest evidence here.** The model emitted
`<function=read>…</function>` **as plain text** instead of calling the tool, so the ledger was
observed and **empty** — `()`, not `None`. The scheduler therefore refused it:
*"an ordered ledger was observed and it is empty: the run called nothing."* The negative is
**earned**, and it is earned only because `()` and `None` are kept apart. Had the ledger been
absent instead, the honest answer would have been `undetermined`, and the contract returns
exactly that in the other case.

Run 3 also reproduces, inside a real unattended dispatch, the intermittent tool-calling failure
measured during this epic's design: the same model and prompt shape produced real tool calls in
10 of 12 observed runs and prose imitation in 2. **The lane's engine is not reliable, and the
ledger is what makes an unreliable run visible instead of creditable.**

## Constraint 7 — the completion judgment was run on every run, and both are reported

*Never read a QA verdict without first running the completion judgment on the run that produced
it.* Applied here to the models' own prose claims:

* **Run 1** — asked for a `framework_version` key that **`.ai-project.yml` does not contain**.
  The model read the file (one real `tool_use`) and answered *"The file .ai-project.yml does not
  contain a framework_version key."* An honest negative. Judgment agrees nothing changed.
  **Worth recording against M39:** on the `epic_qa` lane, this same model returned
  `VERDICT: PASS` **citing that same key**, with **zero tool calls**. Here it had tools that
  worked, and it did not fabricate. One data point on a different dispatch path — not a general
  claim about fabrication rates.
* **Run 2** — the model claimed *"The file LANE-PROOF.txt has been successfully created."* The
  judgment independently confirms it: one effect (`Wrote file successfully.`), a covering
  verification at `exit_code: 0`, and `files_changed` carrying `LANE-PROOF.txt` from a
  before/after snapshot the model had no hand in. Claim and evidence agree.
* **Run 3** — the model claimed nothing and did nothing. The judgment refused it. No success
  claim was taken at face value anywhere in this set.

## The lane held: one reasoning job at any instant

Measured from the journal's own timestamps — the three dispatch windows do not overlap:

```
…f58f17ea -> …39168925: gap +0.016s
…39168925 -> …efcf592b: gap +0.005s
```

`lane_waited_s` is `0.0` on all three, which is the honest reading and not a contradiction: each
run had finished before the next was claimed, so no dispatch ever had to *wait*. **This
therefore evidences that the lane serialized, and does not evidence that it blocks a competing
holder.** That property is asserted separately in `drivr`'s suite by
`tests/test_scheduling_axes.py`, which spawns a second **process** and confirms it is refused.

## Where each run happened (D4)

Every run was dispatched into its **own detached git worktree**, allocated by the scheduler
outside the project directory and removed afterwards — `record.json` carries `worktree` and
`worktree_commit`. After all three, `git worktree list` in both repositories shows only the
primary tree and the worktree base directory is empty. Run 2 mutated its worktree and it was
still removed.

## Provenance

* **`drivr`** @ **`6332674`** on `main`, suite **319 passed**, 2026-08-17. No git remote —
  a reviewer must re-measure on this machine.
* Engine: `opencode` **1.18.10** at `/home/panchew/.opencode/bin/opencode`, host environment.
* Model: `ollama/qwen3-coder:30b`, Ollama on loopback (`localhost:11434` → 200;
  `host.docker.internal` → 000, the reverse of `B2.1`'s shape).
* Enrollment source: `.ai-project/registry/fleet-registry.yml` (E38.3) — 6 eligible, 9 excluded
  each with a reason, 2 recorded `section_4: invalid` and reported rather than benched.

## Files

`journal.ndjson` — one JSON object per dispatch, append-only.
`runs/<job_id>/stream.ndjson` — **the engine's own stdout, verbatim.** Every question about what
the engine emitted is answerable only at this layer.
`runs/<job_id>/verdict.txt` — the judgment's full evidence, readable without re-running it.
`runs/<job_id>/disposition.txt` — what the scheduler concluded, and why.
`runs/<job_id>/job.json`, `record.json` — the job as enqueued, and the dispatch record.
`serve.log`, `serve-started-at.txt` — that the scheduler was up before any work existed.
