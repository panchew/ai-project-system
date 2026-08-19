---
project: ai-project-system
phase: P12
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: P12 Phase Chat → M42
last_updated: 2026-08-19
severity: high
---

# Carry-Forward Note — P12-GH-2: `bin/ai-project-init` writes a placeholder agent when the real one is missing, its own validator accepts the placeholder, and the guarding test can only ever exercise the placeholder branch

**Found by HQ, 2026-08-19, while scoping P12** — by asking whether SN-31's four fail-open instances
were the complete set. They are not. **This is a fifth instance of the same disposition, at the
enrollment tier, and it is the one with a live victim.**

P11's closure declaration carries *"the two `bin/ai-project-init` defects, one with a live victim
(`social-stories-creator` still carries a 230-byte placeholder agent)"* as an inherited open item
**with no gap-record ID.** This note gives it one and states the mechanism, which the inherited line
does not.

---

## The mechanism, in three parts

**1. The source path is off by one `governance/` level.**

`install_hq_agent()` (`bin/ai-project-init:323-353`) reads:

```
local src_file="$project_dir/governance/agents/governance.agent.md"
```

`add_governance_submodule()` (`:274`, `:281`, `:294`) clones the **whole** `ai-project-system`
repository into `<project>/governance`. Inside this repository the agent lives at
`governance/agents/governance.agent.md` — **verified 2026-08-19, it is the only file of that name in
the tree.** So after a real submodule install the agent is at
`<project>/governance/governance/agents/governance.agent.md`, and the path `install_hq_agent` reads is
one level short. **The source is never found.**

**2. The fallback writes a stub, and the validator accepts it.**

```
# Create stub when governance agent is not yet available (e.g., during M8 work)
cat > "$dest_file" << 'EOF'
# HQ Chat Agent
This agent is under development in Milestone M8.
...
```

Then, immediately below (`:348-353`):

```
[[ -r "$dest_file" ]] || error ...        # readable  — the stub is
[[ -s "$dest_file" ]] || error ...        # non-empty — the stub is
head -n 1 "$dest_file" | grep -Eq '^(#|---)'   # header — the stub starts with "# HQ Chat Agent"
```

**The stub passes all three checks the script performs on the thing it just failed to install.** The
validator does not test for the property that matters — that the file is the governance agent — only
for properties a placeholder trivially satisfies. **This is the fail-open disposition in its purest
form: the evidence is absent, so a substitute is manufactured, and the check is written against the
substitute.**

The comment naming **Milestone M8** dates the fallback. M8 closed in P2. The temporary branch has
been the only reachable branch for at least nine phases.

**3. The test can only ever take the stub branch.**

`tests/test_init_agent_path.py` invokes the script with `--skip-submodule`, then asserts the file
exists, is non-empty, and begins with `#`. **Those are the same three properties the stub satisfies.**
The test was written for `P6-GH-11` (the `.github/agents/` → `.ai-project/agents/` path fix) and it
does that job correctly. It cannot detect this one, because the branch that would fail is
unreachable under its own invocation.

**This is structurally identical to `bin/ai-project-git-merge:447-460`**, where a test asserts the
`--admin` override succeeds against a branch that returned *"Branch protected."* In both cases the
suite records the fail-open path as expected behaviour. **Two of the phase's organizing instances are
protected by their own tests.**

---

## What is verified and what is inferred — stated because this project files that distinction

**Verified by reading, on `master` at `19c77ab`:** the source path at `:328`; the submodule clone
target at `:274`/`:281`/`:294`; the single location of `governance.agent.md` in this repository; the
three validation checks at `:348-353`; the stub body; the test's `--skip-submodule` invocation and its
three assertions.

**Verified by the record, not re-run here:** the live victim. P11's closure declaration states
`social-stories-creator` still carries a 230-byte placeholder agent. **HQ did not re-inspect that
repository.** M42 should, and should enumerate the fleet rather than the one known case.

**Inferred, not executed:** that a real (non-`--skip-submodule`) init today produces the stub. The
inference follows from the two verified paths and is consistent with the recorded victim, but **no
end-to-end init was run for this note.** M42 runs it. If the inference is wrong the finding shrinks to
the validator and the test, which are defects on their own terms.

---

## Second defect, same script, recorded so it is not separated from this one

`write_project_config()` (`:262`) writes `submodule_path: governance/`. **M38 established `.governance`
as the fleet convention (8 of 11 projects), and the three exceptions are exactly the projects init
created.** The M38 escalation recorded that init hard-codes the path with no flag. That is the second
of the "two `bin/ai-project-init` defects" P11 carried, and it is the reason the first one is
universal rather than occasional: **a project that follows the convention has its governance
somewhere init never looks.**

---

## Severity: High

**Higher than `P12-GH-1`, and higher than the inherited line implies.**

- **It fires silently on every install**, with no warning path a human would notice — the script
  reports success.
- **It has a live victim already**, before any agentic operation.
- **It is the enrollment tier**, so the failure is inherited by every project the framework onboards,
  including the first external adopter recorded in SN-31 Carry-Over 6.
- **P6-GH-15's shape, again:** *the initializer installs the wrong agent.* That was closed in P10-M34
  for a superseded-file reason. **The path defect underneath it was not.**

---

## Placement

**M42 — Fail-Closed Execution Tier.** It is a `bin/` defect of exactly the family M42 exists to close,
and it shares M42's design question: *what does this script do when the thing it needs is not there?*
The answer for all four of M42's items is the same — **stop, and say so** — and manufacturing a
substitute is the one answer that must not survive the milestone.

**M42 must also invert the test**, not delete it: the suite should fail if a stub is installable at
all.
