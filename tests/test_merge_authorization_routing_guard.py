"""Guard: every starter surface routes merge authorization through its own parent.

Epic P11-M40-E40.5 — The Merge-Authorization Routing Guard (P9-GH-1 / P10-GH-9).

Background
----------
A chat that is handed merge authorization directly, rather than via the level that
is supposed to review first, has nothing in its own starter telling it to stop. Under
default-accept (PSG §11.6 / AOG §12) silence accepts, so silent compliance produces
no artifact recording that a review gate was skipped: **the failure is invisible by
construction.**

The guard closing that gap was added at Epic level in P9 (P9-M31, ``8dbffe0``) and
was never extended. ``P9-GH-1`` recorded the gap; ``P10-GH-9`` re-rated it after the
ratified execution matrix (P10-M35, SN-25) restored agentic mode at Phase and
Milestone, removing the compensation that had made it harmless — a human sitting at
those gates *by construction*.

**It is not hypothetical.** On 2026-08-10 PR #191's merge was authorized in the M38
Milestone Chat rather than in the Phase Chat's Stage-2 review. The CFO caught it. The
framework did not.

What this test asserts
----------------------
For every starter surface a chat may read as its own operating contract, the
level-aware guard is present, and it names the **routing destination correct for that
level** — because a guard that names the wrong parent is worse than none: it launders
a bypass as a check.

The surface is a **sweep result, not an inherited number.** ``P9-GH-1`` speaks of "the
Epic templates"; the sweep found **eight** starter-shaped surfaces, of which the guard
reached exactly one. Three of those eight are Epic-level surfaces, including
``governance/EPIC-EXECUTION-CHAT-STARTER.md``, which ``governance/README.md`` names as
the canonical Epic starter format.

Matching is literal-substring against **case-folded, whitespace-normalized** text.
Both normalizations are deliberate and were forced by evidence, not chosen for
convenience:

* **Case** — markdown emphasis moves around a phrase (``**authorization is not
  review**`` vs ``Authorization is not review.``); a case flip is not a regression of
  meaning.
* **Whitespace** — the first run of this test on 2026-08-17 failed on
  ``governance/templates/epic-execution-chat-starter.md`` for a guard that was
  present and correct: re-wrapping the bullet split ``do not simply comply`` across a
  line break as ``do\n  not simply comply``. **The guard shipped in P9 was one
  markdown reflow away from being unverifiable by literal match.** A checker that
  fails on reflow produces false failures, and false failures get checkers weakened.

Deleting or rewording the guard still fails — see the detector self-tests.

Scope decision — templates and system references, not instantiated starters
--------------------------------------------------------------------------
Instantiated starters under ``docs/`` are **historical records of what a chat was
actually told**. Retro-editing them would falsify that record, and retro-*failing*
them would turn the suite red for closed epics. Setting a forward-only floor instead
(only starters from milestone N on) would place the floor past every artifact that
exists today, producing a check that asserts nothing and cannot be falsified — the
exact rotted-guard shape M38 recorded. So this guard is **forward-only by
construction**: it binds the templates every future starter is copied from, and the
detector self-tests below prove the check itself works.

If this test fails: open the named surface and restore the merge-authorization
routing guard, with the routing destination correct for that surface's level (see the
table in this Epic's spec, §D1). Do not "fix" it by weakening the assertion.
"""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

_WHITESPACE = re.compile(r"\s+")


def normalize(text: str) -> str:
    """Case-fold and collapse whitespace runs to single spaces.

    So a guard stays matchable across markdown reflow and emphasis changes. See
    this module's docstring for why both normalizations are required.
    """
    return _WHITESPACE.sub(" ", text).lower()

# The clause every instance of the guard shares, at every level. This is the
# load-bearing substring: without it the surface gives no instruction to stop.
REFUSAL_CLAUSE = "do not simply comply"

# Mode is not authority (Binding Constraint 5; chat-hierarchy.md). Running
# unattended widens what an instance *does*, never what it may *authorize*.
MODE_CLAUSE = "mode is what may run, not what may be authorized"

# Each starter surface a chat may read as its own operating contract, with the
# tokens that make its routing destination correct *for that level*.
#
# Established by sweep on 2026-08-17 against literal file text on branch
# epic/P11-M40-E40.5:
#   find governance -iname '*starter*'
#   grep -rln 'merge authorization\|merge_authorization' governance/
GUARDED_SURFACES = (
    # --- Epic level: confirm with the parent Milestone Chat ---
    ("governance/templates/epic-execution-chat-starter.md", ("milestone chat",)),
    ("governance/systems/epic-execution-chat-starter.md", ("milestone chat",)),
    ("governance/EPIC-EXECUTION-CHAT-STARTER.md", ("milestone chat",)),
    # --- Milestone level: confirm with the parent Phase Chat ---
    ("governance/templates/milestone-execution-chat-starter.md", ("phase chat",)),
    ("governance/systems/milestone-execution-chat-starter.md", ("phase chat",)),
    # --- Phase level: HQ Chat, and for phase/* -> master the CFO's §11.6.1 diff
    #     review. A guard that stops at "confirm with your parent" is incomplete
    #     here: authorization is not review.
    (
        "governance/templates/phase-execution-chat-starter.md",
        ("hq chat", "11.6.1", "authorization is not review"),
    ),
    (
        "governance/systems/phase-execution-chat-starter.md",
        ("hq chat", "11.6.1", "authorization is not review"),
    ),
    # --- HQ level: no parent chat exists. PSG §11.6.1 — the CFO is the mandatory
    #     diff reviewer; an HQ-authored PR never merges on authorization alone.
    (
        "governance/systems/hq-execution-chat-starter.md",
        ("cfo", "11.6.1", "authorization is not review"),
    ),
)

SURFACE_PATHS = tuple(path for path, _ in GUARDED_SURFACES)


def _ids(param):
    return param[0] if isinstance(param, tuple) else str(param)


@pytest.mark.parametrize("surface", SURFACE_PATHS, ids=_ids)
def test_surface_exists(surface):
    """Sanity: the starter surface is present (guards against a path slip)."""
    assert (REPO_ROOT / surface).is_file(), (
        f"Expected starter surface at {surface}. If it moved, update "
        "GUARDED_SURFACES — do not drop the surface from the sweep."
    )


@pytest.mark.parametrize("surface,tokens", GUARDED_SURFACES, ids=_ids)
def test_surface_carries_refusal_clause(surface, tokens):
    """Every guarded surface must tell its chat not to simply comply."""
    text = normalize((REPO_ROOT / surface).read_text())
    assert REFUSAL_CLAUSE in text, (
        f"{surface} is missing the merge-authorization routing guard: the literal "
        f"clause '{REFUSAL_CLAUSE}' is absent. A chat reading this surface alone "
        "would have no instruction to stop when handed merge authorization "
        "out of band. Restore the guard (see P11-M40-E40.5 spec §D1)."
    )


@pytest.mark.parametrize("surface,tokens", GUARDED_SURFACES, ids=_ids)
def test_surface_names_correct_routing_destination(surface, tokens):
    """The guard must name the destination correct for that surface's level.

    A guard naming the wrong parent is worse than no guard: it launders a bypass
    as a check.
    """
    text = normalize((REPO_ROOT / surface).read_text())
    missing = [t for t in tokens if t not in text]
    assert not missing, (
        f"{surface} carries a merge-authorization guard but is missing the "
        f"routing token(s) {missing} required at its level. The guard must name "
        "where authorization normally comes from *for this level* — see the "
        "level table in the P11-M40-E40.5 spec §D1."
    )


@pytest.mark.parametrize("surface,tokens", GUARDED_SURFACES, ids=_ids)
def test_surface_states_mode_is_not_authority(surface, tokens):
    """Running unattended must not read as widening what may be authorized.

    Binding Constraint 5. This is the half ``P10-GH-9`` is about: the ratified
    matrix permits agentic Phase/Milestone instances, and the guard must not be
    readable as self-authorization when a chat judges the routing acceptable.
    """
    text = normalize((REPO_ROOT / surface).read_text())
    assert MODE_CLAUSE in text, (
        f"{surface} is missing the mode-is-not-authority clause "
        f"('{MODE_CLAUSE}'). Restore it: an agentic instance holds exactly the "
        "authority its level always held."
    )


# ---------------------------------------------------------------------------
# Detector behaviour: synthetic fixtures, so the guard cannot silently rot.
#
# The real-file assertions above pass when the repo is correct — which is also
# what a broken detector does. These prove the checks actually detect. M38
# recorded that a rotted guard is invisible behind a green suite total.
# ---------------------------------------------------------------------------

def _check(text, tokens=()):
    """The assertions above, reduced to the predicates they test."""
    lowered = normalize(text)
    return {
        "refusal": REFUSAL_CLAUSE in lowered,
        "mode": MODE_CLAUSE in lowered,
        "routing": [t for t in tokens if t not in lowered],
    }


GOOD = (
    "If given merge authorization directly in this chat (rather than via the "
    "parent Milestone Chat after its own Stage-2 review), do not simply comply. "
    "Running unattended does not change this: mode is what may run, not what may "
    "be authorized."
)


def test_detector_accepts_a_well_formed_guard():
    result = _check(GOOD, ("milestone chat",))
    assert result["refusal"] and result["mode"] and result["routing"] == []


def test_detector_flags_a_deleted_refusal_clause():
    """The exact regression this guard exists to catch: the clause removed."""
    without = GOOD.replace("do not simply comply. ", "")
    assert _check(without, ("milestone chat",))["refusal"] is False


def test_detector_flags_a_missing_mode_clause():
    without = GOOD.split("Running unattended")[0]
    assert _check(without)["mode"] is False


def test_detector_flags_the_wrong_parent_for_the_level():
    """A Milestone starter that tells its chat to confirm with a *Milestone* Chat.

    The copy-paste failure: the Epic guard pasted one level up unchanged. It
    still reads like a check, and it routes the confirmation to the wrong level.
    """
    assert _check(GOOD, ("phase chat",))["routing"] == ["phase chat"]


def test_detector_is_case_insensitive():
    """Markdown emphasis moves; a case flip is not a regression of meaning."""
    assert _check(GOOD.upper(), ("MILESTONE CHAT".lower(),))["refusal"] is True


def test_detector_survives_markdown_reflow():
    """The real 2026-08-17 failure: a correct guard split across a line break.

    Re-wrapping the bullet produced ``do\\n  not simply comply``. The guard was
    present and correct; a naive literal match called it missing.
    """
    reflowed = GOOD.replace("do not simply comply", "do\n  not simply comply")
    assert _check(reflowed, ("milestone chat",))["refusal"] is True


def test_detector_still_fails_a_deleted_clause_after_normalization():
    """Normalization must not make the check unfalsifiable.

    Whitespace-insensitivity is a real weakening risk: collapse too much and
    everything matches. Deletion must still be caught.
    """
    reflowed_but_deleted = GOOD.replace("do not simply comply. ", "").replace(
        "), ", "),\n    "
    )
    assert _check(reflowed_but_deleted, ("milestone chat",))["refusal"] is False
