---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-18T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-23
    severity: high
    title: Governance-mandated artifact echo (paste/display) is obsolete and paying rent in the costliest sessions — reconcile to reference-first handoff
decisions:
  - "An artifact on disk is passed by reference, never by paste or full-body display. The IDE-attach + one-line-intent workflow (open the artifact file, let the harness attach it, state intent in one line) is the canonical manual-mode handoff."
  - "Copy-paste transport remains documented as a fallback only, for genuinely disconnected setups without repo access (platform agnosticism preserved). Reference-first, paste-as-fallback — paste is not deleted."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

Closes the Creation Chat evaluation session of 2026-07-18 (token-economy concern raised
by the human while working M30 epics). Hands HQ one concern with a confirmed direction:
the framework's mandated artifact-echo surfaces (paste artifact bodies between chats;
display full chat starters in chat output) predate committed-file practice and the
IDE-attach workflow, and should be reconciled to a reference-first handoff model.

---

## Concerns for HQ Triage

### SN-23 — Governance-mandated artifact echo is obsolete; reconcile to reference-first handoff [HIGH]

**Detail:** Three governance surfaces mandate ingesting artifact bodies into chat
context beyond the committed file itself:

1. **`governance/AI-OPERATING-GUIDELINES.md` §3.1.1 (lines ~92–125):** the parent chat
   MUST present each Epic Execution Chat Starter as a full fenced code block in chat
   output, plus "Copy the entire chat starter above and paste…" boilerplate. The starter
   templates (`governance/templates/epic|milestone|phase-execution-chat-starter.md`)
   repeat this instruction. In current practice every starter is also a committed
   git-tracked file (all of P9-M30's starters are), so the full-body echo in the
   parent's output is pure duplication (~2.2–2.8K tokens per starter, measured word
   counts of the actual M30 starters).
2. **`governance/systems/artifact-communication-protocol.md` §Integration with Manual
   Mode (line ~408):** chats "paste \[artifacts] into parent chats via copy-paste."
   Every Delivery Notice body (~1.0–1.3K tokens, measured from M30's notices) is
   ingested in the child session and again as pasted input to the parent session.
3. **`governance/EPIC-EXECUTION-CHAT-STARTER.md` (line ~83):** "Produce Completion
   Notice … fill it in, and paste it into the Milestone Chat." Producing chats also
   habitually echo bodies of artifacts they have just written to file.

**Why it matters (grounded in E30.2's measured data, not estimates):** every token
echoed into a parent-chat session persists in its history and is re-read at cache rates
on every subsequent call. Parent-chat mixed sessions are the dominant cost sink (53% of
the ≈$623 measured window; per-call medians 129K/169K tokens at milestone/phase levels;
cache re-reads 48.5% of weighted cost). E30.3 explicitly declared conversation history
"beyond document control" (its Non-Goals forbid changing AOG/protocol rules) — but the
governance-mandated echo portion of that history IS document-controlled. This lever is
therefore complementary to E30.3's pack reduction and cannot be absorbed by it; it needs
its own scoped home.

**Workflow evidence (the human's observed practice, which triggered this note):** with
VS Code + the Claude Code extension, opening an artifact file attaches it to the chat by
reference; typing one line of intent (e.g. "Epic E35.1 Delivery Notice") completes the
handoff. The parent chat then reads the file selectively (frontmatter + Summary +
QA/DoD suffices under default-accept review, PSG §11.6). Transport — the problem the
paste protocol was written to solve (`artifact-communication-protocol.md` line 14 names
human transcription errors as the original problem) — is already solved by the
filesystem plus a one-line pointer. The audit trail is unaffected: the committed file
was always the record; paste was only ever transport.

**Honest bound on savings:** reference-first does not make ingestion free — the
consumer still reads the file once, selectively. The claim is "each artifact body
ingested once, where needed," not "never ingested." Eliminated outright: the parent's
full-starter output echo, the producer's echo of bodies it wrote to file, and
full-body paste where a selective read suffices.

**Required action:** Scope a "reference-don't-display" reconciliation covering, at
minimum: (a) AOG §3.1.1 — parent emits starter path + one-line summary instead of the
full code block when the starter is a committed file; (b) artifact-communication-protocol
§Manual Mode — paste replaced by reference handoff (IDE-attach or path + frontmatter
summary), paste retained as documented fallback for repo-less setups; (c) a rule that
producing chats do not echo bodies of artifacts they have written to file; consumers
read selectively. Any reduction claim carries before/after evidence via E30.1's
mechanism. HQ decides the home: M31 (natural session-hygiene companion to the G7
mixed-session finding) or a small M30 follow-up epic.

---

## Decisions Already Made

1. An artifact on disk is passed by reference, never by paste or full-body display. The
   IDE-attach + one-line-intent workflow is the canonical manual-mode handoff. (Human
   confirmed, 2026-07-18.)
2. Copy-paste transport remains documented as a fallback only, for genuinely
   disconnected setups without repo access — platform agnosticism preserved.
   Reference-first, paste-as-fallback. (Human confirmed, 2026-07-18.)

---

## Carry-Over Open Items

None.

---

## Next Action

HQ Chat should:
1. Triage SN-23 and decide the reconciliation's home — M31 (session-hygiene companion
   to G7) or a dedicated small follow-up epic; record the choice.
2. Ensure the scoped epic's spec names the three edit surfaces above and binds the
   before/after evidence requirement to E30.1's mechanism.
3. Keep E30.3's boundary intact — this work is complementary to pack reduction, not a
   resize of E30.3.
