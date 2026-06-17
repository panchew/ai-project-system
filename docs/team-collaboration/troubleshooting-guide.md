# Troubleshooting Guide

**Problem → Cause → Solution for common issues in team collaboration.**

---

## Epic Workflow Issues

### Problem: Contributor merged their PR without a Review Decision

**Cause:** The merge happened before a Review Decision (Accept) artifact was issued. This violates the authorization protocol.

**Solution:**
1. Do not revert unless the code is actually broken or out of scope.
2. The Phase Lead or Milestone Agent issues a post-hoc Review Decision (Accept) or (Reject).
   - If Accept: commit the Review Decision artifact dated before the merge and note the sequence anomaly.
   - If Reject: revert the merge, issue Review Decision (Reject), and require rework before re-merging.
3. Record a corrective note in the Milestone Chat.
4. Prevent recurrence: remind contributors that no merge may happen without a Review Decision artifact in the repository.

---

### Problem: Completion Notice was submitted but no Review Decision came back

**Cause (manual mode):** The Completion Notice was not pasted into the parent chat, or the Phase Lead missed it.

**Cause (agentic mode):** The daemon is not running, or the artifact file was committed to the wrong path.

**Solution (manual mode):**
1. Confirm the Completion Notice was pasted into the Milestone Chat (not just committed to the repo).
2. Ping the Phase Lead directly: "E1.1 Completion Notice is in Milestone Chat — awaiting your Review Decision."
3. SLA is 24 hours. If no response after 24 hours, escalate to HQ Agent.

**Solution (agentic mode):**
1. Check daemon status: `governance/bin/ai-project-daemon --project-root . status`
2. Verify the artifact file path matches the convention: `.ai-project/artifacts/completion-notices/<timestamp>__<epic_id>__completion-notice.md`
3. Confirm the YAML frontmatter is valid (no syntax errors — use a YAML linter if needed)
4. Check daemon logs for routing errors
5. If daemon is misconfigured, fall back to manual mode temporarily: paste the Completion Notice into the Milestone Chat directly

---

### Problem: Epic was rejected 3 times — now what?

**Cause:** The Epic has exhausted the Dev-QA retry limit (3 attempts).

**Solution:**
1. The Epic Agent (or Contributor) produces an **Escalation Report** explaining:
   - What was attempted in each of the 3 attempts
   - What the blocking issue is (spec gap, ambiguity, dependency)
   - What decision is needed to unblock
2. Submit the Escalation Report to the Milestone Chat
3. The Milestone Agent evaluates:
   - **Spec gap:** Amend the spec, reset retry counter, reauthorize
   - **Scope issue:** Reduce Epic scope, split into two Epics
   - **Dependency issue:** Block this Epic until the dependency resolves
4. If the Milestone Agent cannot resolve, escalate to Phase Lead, then CFO

Do not submit a 4th Completion Notice without explicit authorization.

---

### Problem: Two Epics are touching the same file and causing merge conflicts

**Cause:** Two Epics were planned with overlapping file scope, and one merged before the other.

**Solution:**
1. The later-merging Epic rebases its branch onto the updated milestone branch:
   ```bash
   git checkout epic/E1.2
   git rebase milestone/M1
   ```
2. Resolve any conflicts during the rebase
3. Re-run tests to confirm no regressions
4. Notify the Reviewer that a rebase occurred and request re-review of the conflict areas
5. Document the conflict resolution in the Completion Notice

**Prevention:** When planning parallel Epics, the Phase Lead should identify shared files and either sequence Epics (rather than parallelize) or scope them to avoid the same files.

---

## Authority & Decision Issues

### Problem: A Review Decision was issued by the wrong role

**Cause:** For example, a Contributor issued a Review Decision artifact, which they have no authority to do.

**Solution:**
1. Identify the correct role that should have issued the artifact
2. The correct role re-issues the Review Decision with proper frontmatter (`issuer_role`, `issuer_chat`)
3. The incorrectly-issued artifact should be renamed or removed from the artifacts directory to avoid confusion
4. If the decision content is correct (Accept/Reject), the re-issued artifact can repeat the same decision with corrected attribution

**Prevention:** Every artifact must include the correct `issuer_role` and `issuer_chat` fields. Reviewers issue PR comments, not Review Decision artifacts.

---

### Problem: CFO wants to override a Milestone Agent rejection, but it's already committed

**Cause:** A Review Decision (Reject) was issued and committed, but CFO believes the rejection was incorrect.

**Solution:**
1. CFO issues an explicit override statement in HQ Chat: "I am overriding the Milestone Agent's rejection of E1.1. The contributor's deviation was authorized by me retroactively. Treat E1.1 as accepted."
2. The HQ Agent or Milestone Agent issues a new Review Decision (Accept) referencing the CFO override
3. Both the rejection and the override are left in the repository — do not delete the rejection artifact (audit trail)
4. The contributor proceeds to merge on the new acceptance

---

### Problem: Production was deployed without CFO authorization

**Cause:** A deployment skipped the CFO production gate.

**Solution:**
1. Assess the risk of the deployment: is the code safe? Were there regressions?
2. If safe: CFO issues a retroactive Deployment Authorization noting the sequence anomaly
3. If unsafe: CFO evaluates whether to roll back
4. Corrective action: determine how the gate was bypassed and close the process gap
5. If an agent bypassed the gate: review the agent's configuration and add the production gate as a hard constraint

This is the most serious governance violation in the system. It must be escalated to CFO immediately and documented.

---

## Artifact Format Issues

### Problem: YAML frontmatter in a Completion Notice has a syntax error

**Cause:** Invalid YAML (unescaped quotes, wrong indentation, missing colon).

**Solution:**
1. Fix the YAML before the daemon (or parent chat) tries to parse it
2. Validate with a YAML linter: `python3 -c "import yaml, sys; yaml.safe_load(sys.stdin)" < artifact.md`
3. Common issues:
   - Strings with colons must be quoted: `title: "feat: Add X"` not `title: feat: Add X`
   - Timestamps must be ISO-8601: `2026-06-01T10:00:00Z`
   - Lists require proper indentation (2 spaces per level)
4. After fixing, re-commit the artifact. If in agentic mode, the daemon will retry.

---

### Problem: Delivery Notice was not produced after merge

**Cause:** The contributor merged the PR and closed their chat session without producing a Delivery Notice.

**Solution:**
1. The contributor (or Phase Lead on their behalf) produces the Delivery Notice retroactively
2. Use the merge commit hash and timestamp from `git log` to fill in `merge_details`
3. Commit the Delivery Notice to the milestone branch directly (the epic branch is already deleted)
4. Notify the Milestone Chat that the Delivery Notice has been produced

---

## Escalation Issues

### Problem: Escalation sent to CFO but no response after 2 business days

**Cause:** CFO did not see the escalation, or the escalation was not urgent enough to surface.

**Solution:**
1. Resend the escalation marked as **URGENT** in HQ Chat
2. If the escalation is blocking multiple team members, quantify the impact: "This blocks 2 developers and delays Milestone M2 completion"
3. If the CFO has a designated backup or deputy, escalate to them
4. If the project is in crisis (critical production issue, security incident), use your organization's emergency escalation path outside the AI Project System

---

### Problem: Two team members disagree about the correct interpretation of an Epic spec

**Cause:** The spec contains ambiguous language that two people interpret differently.

**Solution:**
1. Do not proceed on either interpretation unilaterally
2. Both parties document their interpretations briefly (2-3 sentences each) in the Milestone Chat
3. The Milestone Agent (or Phase Lead) makes the authoritative interpretation
4. If the Milestone Agent's interpretation requires a spec change, the spec is amended and the amendment is committed as an artifact
5. The contributor proceeds on the authoritative interpretation

---

## Cross-References

- [FAQ](faq.md) — common questions answered
- [Contributor Guide](contributor-guide.md) — correct Epic workflow
- [Reviewer Guide](reviewer-guide.md) — review process
- [Phase Lead Guide](phase-lead-guide.md) — escalation to CFO
- [CFO Quick Start](cfo-quick-start.md) — production gate and override authority
- [Decision Matrices](decision-matrices.md) — who has authority for each decision
- [Governance: Artifact Communication Protocol](../../governance/systems/artifact-communication-protocol.md) — artifact schemas and rules
- [Governance: Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md) — expedited bugfix path
