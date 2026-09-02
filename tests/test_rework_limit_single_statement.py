"""Guard: the rework limit exists once, normatively, and every starter-shaped surface
reaches it.

Epic P12-M43-E43.3 — The Rework Limit: One Statement, an Itemized Set.

Background
----------
``P12-GH-1``: the only mechanism bounding rework loops lived in exactly one
starter-shaped surface (``governance/systems/milestone-execution-chat-starter.md``),
was absent from every template and from the normative tier (PSG/AOG), and carried two
contradictory extension semantics — ``:341`` said the limit *"resets"* (unbounded,
repeatable); SN-36/37 granted *exactly one further attempt, not a reset to three*. No
test detected any of it.

E43.3's answer: **one normative statement** in PROJECT-SYSTEM-GUIDELINES.md §11.6 "The
Rework Limit" — the 3-attempt maximum *and* what a written extension grants (+1, not a
reset). Every starter-shaped surface reaches it by **carrying** the statement (stating
both halves) or by **citing** it (pointing at the one normative home). The itemized
surface set is a list, never a count (W2: seven/eight/nine never reconciled — a list
carries the context a count cannot).

What this test asserts
---------------------
1. **The one normative statement exists in the normative tier.** PSG §11.6 states both
   halves — the 3-attempt maximum and the +1 extension ("one further attempt", "not a
   reset to three") — and defines rework exhaustion for E43.4.
2. **The "resets" extension semantics are gone from every surface's live body.** The
   drift condition (Binding Constraint 5: *reconcile into one, do not stack*) is
   resolved, not annotated. No starter-shaped surface may state that the limit resets.
3. **Every starter-shaped surface reaches the statement — carry or cite.** For each
   itemized surface: it either carries the statement (both halves present in the live
   body) or cites it (a pointer to PSG §11.6 "The Rework Limit"). The three templates
   are in the set — the template is what a chat is instantiated from, and P12-GH-1
   bites exactly there.
4. **No listed surface may fall out of coverage.** Remove a surface's carry/cite and
   this test fails for that surface (falsification), which is what makes "no test
   detects the omission" finally false.

Matching is literal-substring against **case-folded, whitespace-normalized** text,
following the same evidence-forced normalization as
``tests/test_merge_authorization_parent_performs.py`` and
``tests/test_acceptance_distinguishable_from_absence.py`` (markdown reflow and
emphasis must not produce false failures; deletion must still be caught — see the
detector self-tests).

If this test fails: the named surface no longer carries or cites the one statement, or
the "resets" semantics crept back. Restore the reach (see the P12-M43-E43.3 spec
§Scope of Work). Do not "fix" it by weakening the assertion.
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

    So a guard stays matchable across markdown reflow and emphasis changes. See this
    module's docstring for why the normalizations are required.
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


# ---------------------------------------------------------------------------
# The itemized surface set (D3) — a LIST, never a count (W2).
#
# Re-measured on this branch (P11-GH-2): ten starter-shaped surfaces reach a chat's
# operating contract. The four systems starters, the three templates starters, the two
# seeds, and the root canonical `EPIC-EXECUTION-CHAT-STARTER.md` (which E43.1 counted
# as one of its eight starter surfaces). P12-GH-1's "nine" (4 systems + 3 templates +
# 2 seeds) and E43.1's "eight" (4 systems + 3 templates + root canonical) each omitted
# a member of this list — exactly the W2 lesson: a count carries none of that context,
# a list carries all of it.
# ---------------------------------------------------------------------------
REWORK_SURFACES = (
    "systems/milestone-execution-chat-starter.md",
    "systems/hq-execution-chat-starter.md",
    "systems/epic-execution-chat-starter.md",
    "systems/phase-execution-chat-starter.md",
    "systems/system-hq-seed.md",
    "templates/milestone-execution-chat-starter.md",
    "templates/epic-execution-chat-starter.md",
    "templates/phase-execution-chat-starter.md",
    "templates/seed.md",
    "EPIC-EXECUTION-CHAT-STARTER.md",
)

SURFACE_PATHS = tuple(GOVERNANCE / s for s in REWORK_SURFACES)

NORMATIVE_TIER = "PROJECT-SYSTEM-GUIDELINES.md"

# ---------------------------------------------------------------------------
# The one normative statement (D1) — both halves, as stated in PSG §11.6.
# ---------------------------------------------------------------------------

# The limit half: a maximum of 3 attempts.
LIMIT_MARKERS = (
    "3 attempts",
    "third completion notice",
)

# The extension half: a written extension grants exactly ONE further attempt, not a
# reset to three.
EXTENSION_MARKERS = (
    "one further attempt",
    "not a reset to three",
)

# The exhaustion definition E43.4 triggers on.
EXHAUSTION_MARKER = "rework is exhausted"

# The drift semantics (D2) — the extension must NOT be stated as a reset. If any live
# body contains these, the two-contradictory-statements condition is back.
RESET_SEMANTICS = (
    "limit resets only if",
    "resets to three",
)

# ---------------------------------------------------------------------------
# Carry vs. cite (D4). A surface either CARRIES the statement (both halves present in
# its live body) or CITES it (a pointer to the one normative home). The templates
# carry or cite as recorded in the E43.3 record: the milestone system starter and the
# milestone template carry (the Milestone Chat is the surface that runs the loop);
# every other starter-shaped surface cites the one normative statement.
# ---------------------------------------------------------------------------
CARRY_SURFACES = (
    "systems/milestone-execution-chat-starter.md",
    "templates/milestone-execution-chat-starter.md",
)
CITE_SURFACES = tuple(s for s in REWORK_SURFACES if s not in CARRY_SURFACES)

# A citation reaches the statement by pointing at its normative home: the phrase
# "rework limit" plus a reference to PROJECT-SYSTEM-GUIDELINES.md §11.6.
CITE_MARKERS = ("rework limit", "11.6")


def _ids(param):
    return str(param)


# ---------------------------------------------------------------------------
# Sanity: every listed surface exists (guards against a path slip — the list is the
# deliverable, not an inherited number).
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_scanned_surface_exists(surface):
    """Sanity: the starter-shaped surface is present (guards against a path slip)."""
    assert surface.is_file(), (
        f"Expected starter-shaped surface at {surface.relative_to(REPO_ROOT)}. If it "
        "moved, update REWORK_SURFACES — do not drop the surface from the list."
    )


def test_normative_tier_exists():
    assert (GOVERNANCE / NORMATIVE_TIER).is_file()


# ---------------------------------------------------------------------------
# D1 — the one normative statement, in the normative tier, both halves.
# ---------------------------------------------------------------------------

def test_one_normative_statement_exists():
    """PSG §11.6 states both halves of the rework limit and the exhaustion definition."""
    text = normalize(live_text(GOVERNANCE / NORMATIVE_TIER))
    missing = [
        m for m in LIMIT_MARKERS + EXTENSION_MARKERS + (EXHAUSTION_MARKER,) if m not in text
    ]
    assert not missing, (
        f"{NORMATIVE_TIER} §11.6 is missing rework-limit marker(s) {missing}. The one "
        "normative statement must state the 3-attempt maximum AND the +1 extension "
        "('one further attempt, not a reset to three') and define rework exhaustion "
        "(E43.3, P12-M43)."
    )


# ---------------------------------------------------------------------------
# D2 — the drift is reconciled, not annotated: no live body may state that the limit
# resets.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_no_surface_states_the_reset_semantics(surface):
    """No starter-shaped surface's live body may say the limit resets."""
    text = normalize(live_text(surface))
    present = [p for p in RESET_SEMANTICS if p in text]
    assert not present, (
        f"{surface.relative_to(REPO_ROOT)} carries reset-extension semantics {present}. "
        "A written extension grants exactly ONE further attempt, not a reset to three "
        "(PSG §11.6; SN-36/37, stricter). The two statements are reconciled into one — "
        "they are not left standing (Binding Constraint 5)."
    )


# ---------------------------------------------------------------------------
# D3/D4 — every listed surface reaches the statement: carry OR cite.
# ---------------------------------------------------------------------------

def _reach_state(text):
    """Return the reach mechanisms a surface's live body satisfies."""
    mechanisms = []
    if any(m in text for m in LIMIT_MARKERS) and any(m in text for m in EXTENSION_MARKERS):
        mechanisms.append("carry")
    if all(m in text for m in CITE_MARKERS):
        mechanisms.append("cite")
    return mechanisms


@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_surface_reaches_the_statement(surface):
    """Each starter-shaped surface carries the statement or cites the one normative home."""
    text = normalize(live_text(surface))
    mechanisms = _reach_state(text)
    assert mechanisms, (
        f"{surface.relative_to(REPO_ROOT)} neither carries the rework-limit statement "
        f"(markers {LIMIT_MARKERS} + {EXTENSION_MARKERS}) nor cites the one normative "
        "home ({CITE_MARKERS}). Every starter-shaped surface must reach the single "
        "statement — the template is what a chat is instantiated from, and P12-GH-1 "
        "bites exactly there (E43.3, P12-M43)."
    )


@pytest.mark.parametrize("surface", CARRY_SURFACES, ids=_ids)
def test_carry_surface_states_both_halves(surface):
    """The two carry surfaces state both halves: the limit AND the +1 extension."""
    text = normalize(live_text(GOVERNANCE / surface))
    missing = []
    if not any(m in text for m in LIMIT_MARKERS):
        missing.extend(LIMIT_MARKERS)
    if not any(m in text for m in EXTENSION_MARKERS):
        missing.extend(EXTENSION_MARKERS)
    assert not missing, (
        f"{surface} is a carry surface and is missing statement marker(s) {missing}. "
        "It must state both halves — the 3-attempt maximum and that a written "
        "extension grants one further attempt, not a reset to three."
    )


@pytest.mark.parametrize("surface", CITE_SURFACES, ids=_ids)
def test_cite_surface_points_at_the_statement(surface):
    """Each cite surface points at the one normative home."""
    text = normalize(live_text(GOVERNANCE / surface))
    missing = [m for m in CITE_MARKERS if m not in text]
    assert not missing, (
        f"{surface} is a cite surface and is missing citation marker(s) {missing}. It "
        "must point at PROJECT-SYSTEM-GUIDELINES.md §11.6 'The Rework Limit' — the "
        "one normative statement."
    )


# ---------------------------------------------------------------------------
# Detector behaviour: synthetic fixtures, so the guard cannot silently rot.
# ---------------------------------------------------------------------------

STATEMENT_GOOD = (
    "Rework limit: a parent may reject a delivery a maximum of 3 attempts. If a third "
    "completion notice is still not acceptable, the parent does not issue a fourth "
    "rejection-and-retry. A written extension grants exactly one further attempt, not "
    "a reset to three. Rework is exhausted when the 3-attempt maximum plus any written "
    "+1 has been spent without an acceptable delivery."
)


def _check_surface(text):
    lowered = normalize(text)
    return {
        "reach": _reach_state(lowered),
        "reset": [p for p in RESET_SEMANTICS if p in lowered],
    }


def _check_normative(text):
    lowered = normalize(text)
    return {
        "missing": [
            m for m in LIMIT_MARKERS + EXTENSION_MARKERS + (EXHAUSTION_MARKER,)
            if m not in lowered
        ]
    }


def test_detector_accepts_the_statement():
    assert _check_surface(STATEMENT_GOOD)["reach"] == ["carry"]
    assert _check_surface(STATEMENT_GOOD)["reset"] == []
    assert _check_normative(STATEMENT_GOOD)["missing"] == []


def test_detector_flags_the_reset_semantics():
    """The exact D2 defect: 'the limit resets only if' restored."""
    drifted = STATEMENT_GOOD.replace(
        "A written extension grants exactly one further attempt, not a reset to three.",
        "The 3-attempt limit resets only if you explicitly grant an extension in "
        "writing.",
    )
    result = _check_surface(drifted)
    assert "resets to three" in result["reset"] or "limit resets only if" in result["reset"]
    assert "carry" not in result["reach"]


def test_detector_flags_a_missing_extension_half():
    """A carry surface stating only the limit (no +1) fails the carry assertion."""
    half = STATEMENT_GOOD.replace(
        " A written extension grants exactly one further attempt, not a reset to three.",
        "",
    )
    assert "carry" not in _check_surface(half)["reach"]


def test_detector_accepts_a_cite():
    cite = (
        "The rework limit and its extension semantics are normative in "
        "PROJECT-SYSTEM-GUIDELINES.md §11.6 'The Rework Limit' and are reached here by "
        "citation."
    )
    assert _check_surface(cite)["reach"] == ["cite"]


def test_detector_flags_a_surface_with_neither_carry_nor_cite():
    """The exact P12-GH-1 shape: a starter surface with no rework mention at all."""
    bare = (
        "You are a Milestone Execution Chat. Produce Epic specs and Epic Execution "
        "Chat Starters."
    )
    assert _check_surface(bare)["reach"] == []


def test_detector_flags_a_missing_normative_statement():
    missing = _check_normative(
        "The acceptance record is the parent's merge plus the in-chat acknowledgment."
    )
    assert "3 attempts" in missing["missing"]
    assert "one further attempt" in missing["missing"]


def test_detector_is_case_insensitive_and_reflow_safe():
    reflowed = STATEMENT_GOOD.replace(
        "not a\n  reset to three", "not a reset to three"
    ).upper()
    assert _check_surface(reflowed)["reach"] == ["carry"]
    assert _check_surface(reflowed)["reset"] == []


def test_detector_still_fails_a_deleted_marker_after_normalization():
    deleted = STATEMENT_GOOD.replace(
        " A written extension grants exactly one further attempt, not a reset to three.",
        "",
    ).replace("rework", "rework\n  ")
    assert "carry" not in _check_surface(deleted)["reach"]