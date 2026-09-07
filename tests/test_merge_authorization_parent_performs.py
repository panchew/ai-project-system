"""Guard: no starter-shaped surface instructs a child to hold merge authorization.

Epic P12-M43-E43.1 — The Parent Performs the Merge.

Background
----------
``P9-GH-1`` and ``P10-GH-9`` record a child taking merge authorization directly and
bypassing its parent's Stage-2 review. E40.5 (P11-M40) patched that behaviourally — it
taught starter surfaces to push back ("do not simply comply"). A rule that says "do not
simply comply" still requires the party being bypassed to be the one who objects. E43.1
makes the bypass class **structurally unavailable**: the parent now performs the merge of
a child's branch (PROJECT-SYSTEM-GUIDELINES.md §11.6), so **a child never holds merge
authorization**. E40.5's guard survives, relabelled as a **backstop** — unavailable is
not impossible, and a backstop that fires is evidence.

What this test asserts
----------------------
1. **No starter-shaped surface instructs a child to merge its own branch.** The eight
   starter surfaces a chat reads as its operating contract (the sweep result from E40.5,
   forward-only — instantiated starters under ``docs/`` are historical records and are
   not scanned) must not carry child-addressed merge-instruction language.
2. **Each of those surfaces carries the backstop relabelling** — the E40.5 pushback is
   still present (asserted by ``test_merge_authorization_routing_guard.py`` with the same
   strictness) *and* is labelled a backstop with the reason.
3. **``merge-authorization.md`` is the parent's own record, not an instruction to a
   child** — its subject, fields and post-conditions name the parent (W4).
4. **The one normative statement exists in the normative tier** (PSG §11.6) — so a
   reader can say why a child *cannot* hold the authorization, not why it *should not*.

Matching is literal-substring against **case-folded, whitespace-normalized** text,
following the same evidence-forced normalization as
``tests/test_merge_authorization_routing_guard.py`` (markdown reflow and emphasis must
not produce false failures; deletion must still be caught — see the detector self-tests).

If this test fails: the named surface again instructs a child to merge its own branch,
or the re-authoring / backstop relabelling was reverted. Restore the parent-as-subject
wording (see the P12-M43-E43.1 spec §Scope of Work). Do not "fix" it by weakening the
assertion.
"""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
GOVERNANCE = REPO_ROOT / "governance"

_WHITESPACE = re.compile(r"\s+")


def normalize(text: str) -> str:
    """Case-fold and collapse whitespace runs to single spaces.

    So a guard stays matchable across markdown reflow and emphasis changes. See
    this module's docstring for why both normalizations are required.
    """
    return _WHITESPACE.sub(" ", text).lower()


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


# The starter surfaces a chat may read as its own operating contract — the sweep
# result from E40.5 (P11-M40), established by:
#   find governance -iname '*starter*'
# Re-derived on this branch (P11-GH-2): all eight still exist.
STARTER_SURFACES = (
    "templates/epic-execution-chat-starter.md",
    "systems/epic-execution-chat-starter.md",
    "EPIC-EXECUTION-CHAT-STARTER.md",
    "templates/milestone-execution-chat-starter.md",
    "systems/milestone-execution-chat-starter.md",
    "templates/phase-execution-chat-starter.md",
    "systems/phase-execution-chat-starter.md",
    "systems/hq-execution-chat-starter.md",
)

MERGE_AUTHORIZATION_TEMPLATE = "templates/merge-authorization.md"

NORMATIVE_TIER = "PROJECT-SYSTEM-GUIDELINES.md"

# The backstop relabelling E43.1 requires of every surviving E40.5 pushback: it is
# labelled a backstop, states the reason (the parent performs the merge), and records
# why a backstop survives (unavailable is not impossible).
BACKSTOP_MARKERS = (
    "backstop",
    "never holds merge authorization",
    "unavailable is not impossible",
)

# Merge-as-child-instruction language. If any of these appears in a starter surface or
# in the merge-authorization template, a child is being told it holds merge
# authorization (W4): the very bypass class P9-GH-1 / P10-GH-9 record.
CHILD_INSTRUCTION_PATTERNS = (
    "you merge the pr",
    "you may now merge",
    "you are authorized to merge this work",
    "what the coding agent must do after merging",
    "the coding agent receiving authorization",
    "the coding agent that merged the branch",
    "authorizes a coding agent to merge",
)

# Markers proving the re-authored template reads as the parent's own record of an act
# it performed itself — not an instruction to a child.
PARENT_RECORD_MARKERS = (
    "the parent performs the merge of a child's branch",
    "never holds merge authorization",
    "record of an act it performed",
)

# The one normative statement (D1), in the normative tier.
NORMATIVE_STATEMENT = "the parent performs the merge of a child's branch"

SURFACE_PATHS = tuple(GOVERNANCE / s for s in STARTER_SURFACES)


def _ids(param):
    return str(param)


# ---------------------------------------------------------------------------
# Sanity: every surface the check scans actually exists (guards against a path
# slip — the sweep result is a list, not an inherited number).
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_scanned_surface_exists(surface):
    """Sanity: the starter surface is present (guards against a path slip)."""
    assert surface.is_file(), (
        f"Expected starter surface at {surface.relative_to(REPO_ROOT)}. If it moved, "
        "update STARTER_SURFACES — do not drop the surface from the sweep."
    )


def test_merge_authorization_template_exists():
    assert (GOVERNANCE / MERGE_AUTHORIZATION_TEMPLATE).is_file(), (
        f"Expected template at {MERGE_AUTHORIZATION_TEMPLATE}. This is the re-authored "
        "surface of the epic — do not delete it."
    )


def test_normative_tier_exists():
    assert (GOVERNANCE / NORMATIVE_TIER).is_file()


# ---------------------------------------------------------------------------
# The primary guard: no starter-shaped surface instructs a child to merge its own
# branch.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_surface_carries_no_child_merge_instruction(surface):
    """No starter surface may tell a child it holds merge authorization."""
    text = normalize(live_text(surface))
    present = [p for p in CHILD_INSTRUCTION_PATTERNS if p in text]
    assert not present, (
        f"{surface.relative_to(REPO_ROOT)} carries merge-as-child-instruction "
        f"language {present}. The parent performs the merge of a child's branch "
        "(PSG §11.6); a child never holds merge authorization. Correct the wording "
        "to the parent as the actor (see the P12-M43-E43.1 spec)."
    )


# ---------------------------------------------------------------------------
# The backstop relabelling (D4): the E40.5 guard survives in every starter surface,
# labelled a backstop with the reason.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_surface_labels_the_guard_as_backstop(surface):
    """Every surviving pushback is a labelled backstop, with the reason in the text."""
    text = normalize(live_text(surface))
    missing = [m for m in BACKSTOP_MARKERS if m not in text]
    assert not missing, (
        f"{surface.relative_to(REPO_ROOT)} is missing backstop marker(s) {missing}. "
        "E40.5's guard survives but is relabelled as a backstop, stating the reason: "
        "the parent performs the merge of a child's branch, so a child never holds "
        "merge authorization — unavailable is not impossible, and a backstop that "
        "fires is evidence."
    )


# ---------------------------------------------------------------------------
# The re-authored template (D2): the parent is the subject; the child is nowhere.
# ---------------------------------------------------------------------------

def test_template_carries_no_child_merge_instruction():
    """merge-authorization.md must not address a child anywhere (W4)."""
    text = normalize(live_text(GOVERNANCE / MERGE_AUTHORIZATION_TEMPLATE))
    present = [p for p in CHILD_INSTRUCTION_PATTERNS if p in text]
    assert not present, (
        f"{MERGE_AUTHORIZATION_TEMPLATE} carries merge-as-child-instruction language "
        f"{present}. Re-author it so the parent is the subject — the epic field "
        "becomes a branch reference, and no field or section addresses the child "
        "(W4)."
    )


def test_template_names_the_parent_as_subject():
    """The re-authored template reads as the parent's own record of its act."""
    text = normalize(live_text(GOVERNANCE / MERGE_AUTHORIZATION_TEMPLATE))
    missing = [m for m in PARENT_RECORD_MARKERS if m not in text]
    assert not missing, (
        f"{MERGE_AUTHORIZATION_TEMPLATE} is missing parent-subject marker(s) "
        f"{missing}. Its subject, fields and post-conditions must name the parent "
        "(W4) — not merely omit the child."
    )


# ---------------------------------------------------------------------------
# The one normative statement (D1), in the normative tier.
# ---------------------------------------------------------------------------

def test_one_normative_statement_says_the_parent_merges():
    """PSG §11.6 states, in one place, that the parent performs the merge."""
    text = normalize(live_text(GOVERNANCE / NORMATIVE_TIER))
    assert NORMATIVE_STATEMENT in text, (
        f"{NORMATIVE_TIER} is missing the one normative statement '{NORMATIVE_STATEMENT}'. "
        "A reader must be able to say why a child cannot hold merge authorization — "
        "not merely why it should not."
    )


# ---------------------------------------------------------------------------
# Detector behaviour: synthetic fixtures, so the guard cannot silently rot.
#
# The real-file assertions above pass when the repo is correct — which is also
# what a broken detector does. These prove the checks actually detect.
# ---------------------------------------------------------------------------

PARENT_GOOD = (
    "A Merge Authorization is the parent's own record of an act it performed itself: "
    "the merge of a child's branch. The parent performs the merge of a child's branch "
    "(PSG 11.6). The child never holds merge authorization. This is a backstop: "
    "unavailable is not impossible."
)


def _check_surface(text):
    lowered = normalize(text)
    return {
        "child_instructions": [p for p in CHILD_INSTRUCTION_PATTERNS if p in lowered],
        "backstop": [m for m in BACKSTOP_MARKERS if m not in lowered],
    }


def _check_template(text):
    lowered = normalize(text)
    return {
        "child_instructions": [p for p in CHILD_INSTRUCTION_PATTERNS if p in lowered],
        "parent_markers": [m for m in PARENT_RECORD_MARKERS if m not in lowered],
    }


def test_detector_accepts_a_parent_record():
    assert _check_template(PARENT_GOOD)["parent_markers"] == []
    assert _check_template(PARENT_GOOD)["child_instructions"] == []
    assert _check_surface(PARENT_GOOD)["backstop"] == []


def test_detector_flags_a_child_addressed_template():
    """The exact W4 defect the re-authoring removes: the template addressed to a child."""
    child_addressed = (
        "A Merge Authorization is the explicit 'you may now merge' signal issued to a "
        "Coding Agent. Post-Merge Instruction: what the Coding Agent must do after "
        "merging: delete the epic branch, produce a Delivery Notice."
    )
    result = _check_template(child_addressed)
    assert "you may now merge" in result["child_instructions"]
    assert "what the coding agent must do after merging" in result["child_instructions"]


def test_detector_flags_a_child_merge_instruction_in_a_starter():
    """The canonical-starter defect: 'You merge the PR' told the child to merge."""
    result = _check_surface("Step 3: You merge the PR (on the Milestone Agent's instruction).")
    assert "you merge the pr" in result["child_instructions"]


def test_detector_flags_a_missing_backstop_label():
    """Undoing the relabelling removes the backstop reason from a surface."""
    without_label = PARENT_GOOD.replace("This is a backstop: ", "")
    assert "backstop" in _check_surface(without_label)["backstop"]


def test_detector_flags_a_missing_normative_statement():
    """The normative-tier assertion's predicate: absence of the statement fails."""
    psg_text = "Default-accept is defined at the parent-chat to child gate."
    assert NORMATIVE_STATEMENT not in normalize(psg_text)
    with_statement = (
        "The parent performs the merge of a child's branch. A child never holds "
        "merge authorization."
    )
    assert NORMATIVE_STATEMENT in normalize(with_statement)


def test_detector_is_case_insensitive_and_reflow_safe():
    """The 2026-08-17 lesson: a correct guard must not false-fail on reflow."""
    reflowed = PARENT_GOOD.replace(
        "the child never holds merge authorization", "the child\n  never holds merge authorization"
    ).upper()
    assert _check_surface(reflowed)["backstop"] == []
    assert _check_template(reflowed)["parent_markers"] == []


def test_detector_still_fails_a_deleted_marker_after_normalization():
    """Normalization must not make the check unfalsifiable."""
    deleted = PARENT_GOOD.replace("The child never holds merge authorization. ", "").replace(
        "), ", "),\n    "
    )
    assert "never holds merge authorization" in _check_surface(deleted)["backstop"]