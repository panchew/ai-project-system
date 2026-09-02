"""Guard: a clean delivery can no longer be accepted by silence.

Epic P12-M43-E43.2 — Acceptance Distinguishable from Absence.

Background
----------
PSG §11.6's default-accept made *silence* the sole carrier of acceptance, so
*reviewed and clean* was indistinguishable from *nobody looked* from the record
alone. W3 narrows the live gap to the manual case, which rested on an attendance
presumption ("the human's key is present at the session by construction") — a
presumption about attendance, not evidence of review. The milestone spec's fourth
state (a duplicated role: with two sessions holding one role, "the session" does not
denote) and its auditability property require that whatever replaces silence be **a
signal some identified party emitted**, never an absence attributed to a role — so
duplication leaves evidence rather than vanishing into two indistinguishable silences.

E43.2's answer: a clean delivery is accepted by an **in-chat acknowledgment that
names the party that reviewed and accepted** (role + session identity) — a positive,
attributable signal recorded with the parent's merge. **Silence accepts nothing.**
Default-accept is tweaked, not retired: a clean delivery still produces **no new
artifact** — the signal rides the acknowledgment that already exists.

What this test asserts
----------------------
1. **No surface that states the default-accept model may say a clean delivery is
   accepted by silence.** The itemized set of surfaces whose live body states the
   acceptance model must not carry the old model's phrasing ("by silence",
   "silence-accept", "accept-by-silence") — otherwise a delivery could still be
   accepted with no emitted signal.
2. **Each of those surfaces carries the attributable-signal model**: the acceptance
   is carried by the acknowledgment **naming the party that reviewed**, and
   **silence accepts nothing**.
3. **The normative tier carries the full attribution** — role + session identity /
   an identified party — in PSG §11.6, AOG §12, and the reconciled
   `chat-hierarchy.md` corollary.
4. **The signal's boundary is stated, not implied (D4)**: PSG §11.6 says the
   acknowledgment does **not** make the review good — review-happened is not
   review-correct.
5. **`chat-hierarchy.md:201-205` is reconciled (D3)**: the attendance presumption
   ("present at the session by construction") is gone; the manual/agentic line
   survives (an agentic instance's silence is not an acknowledgment and does not
   by itself accept a delivery).

Matching is literal-substring against **case-folded, whitespace-normalized** text,
following the same evidence-forced normalization as
``tests/test_merge_authorization_parent_performs.py`` (markdown reflow and emphasis
must not produce false failures; deletion must still be caught — see the detector
self-tests).

If this test fails: the named surface again states that silence accepts a clean
delivery, or its acknowledgment lost the attribution. Restore the attributable-
acknowledgment wording (see the P12-M43-E43.2 spec §Scope of Work). Do not "fix" it
by weakening the assertion.
"""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
GOVERNANCE = REPO_ROOT / "governance"

_WHITESPACE = re.compile(r"\s+")
_EMPHASIS = re.compile(r"\*+")


def normalize(text: str) -> str:
    """Case-fold, strip emphasis, and collapse whitespace runs to single spaces.

    So a guard stays matchable across markdown reflow and emphasis changes
    (``**not**`` must match ``not``; a reflowed line must match the same text on
    one line). See this module's docstring for why the normalizations are required.
    """
    return _EMPHASIS.sub("", _WHITESPACE.sub(" ", text)).lower()


# Live text is the operating contract, not the file's history. A changelog row may
# quote a marker (it must — it records what the change did), so scanning the whole
# file would let a changelog satisfy a guard that the live body no longer does — a
# false green. The guard binds the text a chat reads as its contract, so the scan
# stops at the first history section.
_CHANGELOG_HEADERS = ("## changelog", "## amendment history", "## amendment")


def live_text(path: Path) -> str:
    """The file's text up to (not including) its first history section."""
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        if line.strip().lower() in _CHANGELOG_HEADERS:
            return "\n".join(lines[:i])
    return "\n".join(lines)


# The itemized set of surfaces whose live body states the default-accept model
# (itemized, never counted — W2). Re-derived on this branch (P11-GH-2) from
#   rg -l "accepted by silence|by silence" governance/
# plus the two normative documents that carry the model. Each now states the
# attributable-acknowledgment model; the guard binds them all.
ACCEPTANCE_SURFACES = (
    "PROJECT-SYSTEM-GUIDELINES.md",
    "AI-OPERATING-GUIDELINES.md",
    "systems/chat-hierarchy.md",
    "systems/artifact-communication-protocol.md",
    "systems/roles-authorization-team-governance.md",
    "systems/milestone-execution-chat-starter.md",
    "systems/phase-execution-chat-starter.md",
    "systems/hq-execution-chat-starter.md",
    "systems/start-a-project.md",
    "EPIC-EXECUTION-CHAT-STARTER.md",
    "templates/completion-notice-epic.md",
    "templates/epic-review-seal.md",
    "templates/merge-authorization.md",
    "templates/README.md",
    "templates/milestone-execution-chat-starter.md",
    "templates/phase-execution-chat-starter.md",
    "diagrams/artifact-flow.md",
)

SURFACE_PATHS = tuple(GOVERNANCE / s for s in ACCEPTANCE_SURFACES)

# The old model's phrasing. If any of these appears in a surface's live body, a
# clean delivery is again accepted by silence with no emitted signal (E43.2's
# problem, restated). "by silence" subsumes "accepted by silence" / "accept by
# silence" after whitespace normalization, so it is the sole required absent token;
# the two compounds are listed for the detector's failure messages.
OLD_MODEL_PATTERNS = (
    "by silence",
    "silence-accept",
    "accept-by-silence",
)

# The attributable-signal model every surface must carry: the acceptance is carried
# by the acknowledgment naming the party that reviewed, and silence accepts nothing.
ATTRIBUTION_MARKERS = (
    "party that reviewed",
    "silence accepts nothing",
)

# The full attribution — role + session identity / an identified party — is
# normative in the three surfaces that state the model's definition.
NORMATIVE_ATTRIBUTION_MARKERS = (
    "role + session identity",
    "identified party",
)
NORMATIVE_TIER = (
    "PROJECT-SYSTEM-GUIDELINES.md",
    "AI-OPERATING-GUIDELINES.md",
    "systems/chat-hierarchy.md",
)

# D4 — what the signal does NOT claim (PSG §11.6).
NOT_CLAIM_MARKERS = (
    "does not make the review good",
    "review happened",
)

# The property that makes *reviewed and clean* distinguishable from *nobody looked*
# from the record alone.
RECORD_ALONE_MARKER = "from the record alone"
NO_NEW_ARTIFACT_MARKER = "no new artifact"

# D3 — the attendance presumption the corollary must no longer rest on, and the
# manual/agentic line it must keep.
ATTENDANCE_PRESUMPTION = "present at the session by construction"
AGENTIC_LINE_MARKER = "agentic instance's silence is not an acknowledgment"


def _ids(param):
    return str(param)


# ---------------------------------------------------------------------------
# Sanity: every scanned surface exists (guards against a path slip — the sweep is
# a list, not an inherited number).
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_scanned_surface_exists(surface):
    """Sanity: the acceptance-model surface is present (guards against a path slip)."""
    assert surface.is_file(), (
        f"Expected surface at {surface.relative_to(REPO_ROOT)}. If it moved, "
        "update ACCEPTANCE_SURFACES — do not drop the surface from the sweep."
    )


# ---------------------------------------------------------------------------
# The primary guard: no surface that states the acceptance model may say a clean
# delivery is accepted by silence.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_no_surface_states_silence_accepts(surface):
    """No acceptance-model surface may accept a clean delivery by silence."""
    text = normalize(live_text(surface))
    present = [p for p in OLD_MODEL_PATTERNS if p in text]
    assert not present, (
        f"{surface.relative_to(REPO_ROOT)} carries old-model phrasing {present}. "
        "A clean delivery is accepted by an acknowledgment that names the party "
        "that reviewed and accepted (role + session identity) — silence accepts "
        "nothing (PSG §11.6). Correct the wording to the attributable model (see "
        "the P12-M43-E43.2 spec §Scope of Work)."
    )


@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_surface_carries_the_attributable_signal(surface):
    """Each surface names the party that reviewed, and states silence accepts nothing."""
    text = normalize(live_text(surface))
    missing = [m for m in ATTRIBUTION_MARKERS if m not in text]
    assert not missing, (
        f"{surface.relative_to(REPO_ROOT)} is missing attributable-signal marker(s) "
        f"{missing}. The acceptance is carried by an acknowledgment that names the "
        "party that reviewed and accepted; silence accepts nothing (PSG §11.6)."
    )


# ---------------------------------------------------------------------------
# The normative tier: full attribution (role + session identity), the D4 boundary,
# and the record-alone property.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("surface", NORMATIVE_TIER, ids=_ids)
def test_normative_tier_carries_full_attribution(surface):
    """PSG / AOG / chat-hierarchy carry the full attribution form."""
    text = normalize(live_text(GOVERNANCE / surface))
    assert any(m in text for m in NORMATIVE_ATTRIBUTION_MARKERS), (
        f"{surface} is missing the full-attribution form "
        f"({NORMATIVE_ATTRIBUTION_MARKERS}). The signal names the party that "
        "reviewed and accepted by role + session identity — an emission by an "
        "identified party (PSG §11.6)."
    )


def test_psg_states_what_the_signal_does_not_claim():
    """PSG §11.6 states the D4 boundary: review-happened is not review-correct."""
    text = normalize(live_text(GOVERNANCE / "PROJECT-SYSTEM-GUIDELINES.md"))
    missing = [m for m in NOT_CLAIM_MARKERS if m not in text]
    assert not missing, (
        f"PSG §11.6 is missing the not-claim marker(s) {missing}. The signal "
        "distinguishes review-happened from nobody-looked; it does not make the "
        "review good (E39.3's overclaim refused)."
    )


def test_psg_distinguishes_from_the_record_alone():
    """PSG §11.6 states the record-alone property and the no-new-artifact property."""
    text = normalize(live_text(GOVERNANCE / "PROJECT-SYSTEM-GUIDELINES.md"))
    assert RECORD_ALONE_MARKER in text, (
        "PSG §11.6 must state that *reviewed and clean* is distinguishable from "
        "*nobody looked* from the record alone."
    )
    assert NO_NEW_ARTIFACT_MARKER in text, (
        "PSG §11.6 must preserve default-accept's cheapness: a clean delivery "
        "still produces no new artifact."
    )


# ---------------------------------------------------------------------------
# D3 — chat-hierarchy.md:201-205 reconciled with the amended §11.6.
# ---------------------------------------------------------------------------

def test_chat_hierarchy_corollary_reconciled():
    """The manual/agentic corollary agrees with §11.6 and drops the attendance presumption."""
    text = normalize(live_text(GOVERNANCE / "systems" / "chat-hierarchy.md"))
    assert ATTENDANCE_PRESUMPTION not in text, (
        "chat-hierarchy.md still rests default-accept on the attendance presumption "
        "('present at the session by construction'). Presence is not evidence of "
        "review — the acknowledgment naming who reviewed is (E43.2, P12-M43)."
    )
    missing = [m for m in ATTRIBUTION_MARKERS + (AGENTIC_LINE_MARKER,) if m not in text]
    assert not missing, (
        "chat-hierarchy.md's corollary is missing reconciled marker(s) "
        f"{missing}. The manual case rests on the attributable acknowledgment; the "
        "manual/agentic line survives — an agentic instance's silence is not an "
        "acknowledgment and does not by itself accept a delivery."
    )


# ---------------------------------------------------------------------------
# Detector behaviour: synthetic fixtures, so the guard cannot silently rot.
#
# The real-file assertions above pass when the repo is correct — which is also
# what a broken detector does. These prove the checks actually detect.
# ---------------------------------------------------------------------------

MODEL_GOOD = (
    "A clean delivery is accepted by an in-chat acknowledgment that names the "
    "party that reviewed and accepted (role + session identity). Silence accepts "
    "nothing. A clean delivery still produces no new artifact."
)


def _check_surface(text):
    lowered = normalize(text)
    return {
        "old_model": [p for p in OLD_MODEL_PATTERNS if p in lowered],
        "attribution": [m for m in ATTRIBUTION_MARKERS if m not in lowered],
    }


def test_detector_accepts_the_attributable_model():
    assert _check_surface(MODEL_GOOD) == {"old_model": [], "attribution": []}


def test_detector_flags_a_revert_to_silence_accept():
    """The exact defect E43.2 removes: 'accepted by silence' restored."""
    result = _check_surface(
        "A clean delivery is accepted by silence. The merge plus the in-chat "
        "acknowledgment is the acceptance record."
    )
    assert "by silence" in result["old_model"]


def test_detector_flags_a_missing_attribution():
    """Acceptance without a named reviewing party reproduces the defect at one remove."""
    result = _check_surface(
        "A clean delivery is accepted. Silence accepts nothing. The merge plus "
        "the in-chat acknowledgment is the acceptance record."
    )
    assert "party that reviewed" in result["attribution"]


def test_detector_flags_the_attendance_presumption():
    """chat-hierarchy's D3 predicate: the presumption restored fails the reconciliation."""
    presumption = (
        "That model presumes a manual instance, where the human's key is present "
        "at the session by construction."
    )
    assert ATTENDANCE_PRESUMPTION in normalize(presumption)
    text = normalize(
        MODEL_GOOD
        + " An agentic instance's silence is not an acknowledgment, and does not "
        "by itself accept a delivery."
    )
    assert ATTENDANCE_PRESUMPTION not in text


def test_detector_is_case_insensitive_and_reflow_safe():
    """The 2026-08-17 lesson: a correct guard must not false-fail on reflow."""
    reflowed = MODEL_GOOD.replace(
        "names the\n  party that reviewed", "names the party that\nreviewed"
    ).upper()
    assert _check_surface(reflowed)["old_model"] == []
    assert _check_surface(reflowed)["attribution"] == []


def test_detector_still_fails_a_deleted_marker_after_normalization():
    """Normalization must not make the check unfalsifiable."""
    deleted = MODEL_GOOD.replace(" Silence accepts nothing.", "").replace(
        "accepted and accepted", "accepted\n  and accepted"
    )
    assert "silence accepts nothing" in _check_surface(deleted)["attribution"]