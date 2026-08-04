"""Uniqueness check for Steering Note IDs (Bugfix B3.1).

Background
----------
Steering Note IDs are allocated by whichever agent writes the note, by reading
prior notes and incrementing. Correctness therefore depended entirely on the
author's attention, and SN-28 (2026-08-01) audited
``.ai-project/artifacts/steering-notes/`` and found 28 IDs across 23 notes with
**two double-claimed**:

* ``SN-23`` — ``2026-07-18__...__reference-dont-display.md`` and
  ``2026-07-20__...__P10-adoption-spine.md``
* ``SN-1`` — ``2026-06-12__creation-chat__steering-note.md`` and
  ``2026-07-31__layer-8-cfo__...__system-hq-routing-model.md``

P11-M36 resolved both, and **resolved them differently on purpose**. E36.1
recorded the allocation rule and the separating rule in
``governance/systems/creation-chat-guide.md`` §"Steering Note ID Allocation";
E36.2 then applied them: the Layer-8/CFO note was renumbered ``SN-1`` →
``SN-29``, while **``SN-23`` keeps its collision permanently** (see
``RATIFIED_COLLISIONS`` below).

A duplicate ID is untidy. A duplicate ID *cited by number in normative
documents*, where one of the two meanings is partly superseded, is a trap:
``AI-OPERATING-GUIDELINES.md`` and ``chat-hierarchy.md`` both cite "SN-23
Decision 2" meaning unrelated decisions, and the latter declares its one
superseded. This test is the only durable guard against the class — the
allocation rule and the citation fixes are documentation, and documentation
drifts.

Why the real-corpus check carries an allowlist rather than an ``xfail``
----------------------------------------------------------------------
It was originally marked ``xfail(strict=True)``, on the expectation that
clearing the collisions would turn it into an XPASS and force the marker's
removal. **That expectation was wrong.** HQ Ruling 2026-08-01 Decision 4 keeps
``SN-23`` colliding permanently, so the blanket check can never pass and could
never XPASS — the marker had no exit condition.

A blanket ``xfail`` is also the wrong shape on its merits: it tolerates *any*
collision, including a **third**, unratified one, which is the exact class this
guard exists to catch. So the marker is gone (P11-M36-E36.2) and the check is a
plain test carrying a **narrow, ruling-cited allowlist** — one entry, with its
authority recorded in code rather than only in a spec. A newly-introduced
duplicate fails the suite; ``test_synthetic_third_collision_fails_the_guard``
demonstrates that rather than asserting it.

The unit tests below run against temporary directories, so the detector itself
is proven independently of the corpus's state.

Sub-IDs
-------
Letter-suffixed sub-IDs (``SN-12a``, ``SN-12b`` in
``2026-06-25__creation-chat__steering-note.md``) are correctly-suffixed
sub-concerns of one concern, not collisions. They need no special-casing:
uniqueness is checked on the **exact ID string**, so ``SN-12``, ``SN-12a`` and
``SN-12b`` are three distinct IDs that coexist freely — while two notes both
claiming ``SN-12a`` *is* a collision and is caught. An earlier pass mis-flagged
these via a regex artifact (``SN-[0-9]*`` truncating the letter suffix);
matching whole strings avoids reintroducing it, and avoids the opposite error
of treating ``SN-12a`` as conflicting with ``SN-12``.

If this check fails: read the reported ID and the files claiming it, then apply
the rules recorded in ``governance/systems/creation-chat-guide.md`` §"Steering
Note ID Allocation". A bookkeeping defect never rewrites a citation in a
normative document, so renumber only where the ID is cited in project-internal,
non-normative artifacts, and date-qualify the citations otherwise. **Do not add
the new ID to the allowlist below to make the suite green** — allowlisting is a
ruled act, not a remedy an author reaches for while passing through.
"""

import shutil
from collections import defaultdict
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
STEERING_NOTES_DIR = REPO_ROOT / ".ai-project" / "artifacts" / "steering-notes"

# Collisions that are ratified outcomes rather than outstanding defects: ID ->
# why it is exempt. Deliberately a mapping, so no entry can exist without its
# authority written next to it. Adding to this requires a ruling.
RATIFIED_COLLISIONS = {
    "SN-23": (
        "Claimed by both 2026-07-18__...__reference-dont-display.md and "
        "2026-07-20__...__P10-adoption-spine.md, permanently, by HQ Ruling "
        "2026-08-01 Decision 4. SN-23 is cited across the normative tier, and a "
        "bookkeeping defect never rewrites a citation in a normative document, "
        "so the citations were date-qualified — SN-23 (2026-07-18) vs SN-23 "
        "(2026-07-20) — and the collision left visible rather than laundered. "
        "Renumbering either note now would invalidate every citation that was "
        "corrected to disambiguate them."
    ),
}


def parse_front_matter(path):
    """A Markdown file's YAML front matter as a dict ({} if absent or unparseable)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def collect_ids(directory):
    """Map every ``concerns[].id`` under ``directory`` to the filenames claiming it.

    A file claiming the same ID twice appears twice: that is a collision too,
    and de-duplicating it here would hide one.
    """
    claims = defaultdict(list)
    for note in sorted(Path(directory).glob("*.md")):
        for concern in parse_front_matter(note).get("concerns") or []:
            if isinstance(concern, dict) and "id" in concern:
                claims[str(concern["id"])].append(note.name)
    return claims


def find_duplicates(directory):
    """IDs claimed more than once, mapped to every claiming filename."""
    return {i: files for i, files in collect_ids(directory).items() if len(files) > 1}


def unratified_duplicates(directory, ratified=RATIFIED_COLLISIONS):
    """Collisions that are actual defects — duplicates minus the ratified exceptions.

    Split out from ``find_duplicates`` so the allowlist applies at exactly one
    place and can be pointed at a synthetic corpus in a test.
    """
    return {i: f for i, f in find_duplicates(directory).items() if i not in ratified}


def display_path(path):
    """``path`` relative to the repo root, or unchanged if it lies outside it.

    The guard's message names the directory it scanned. That directory is not
    always inside the repo — ``test_synthetic_third_collision_fails_the_guard``
    points it at a copy under ``tmp_path`` — and a message builder must not be
    the thing that raises.
    """
    try:
        return path.relative_to(REPO_ROOT)
    except ValueError:
        return path


def format_duplicates(duplicates):
    """One line per colliding ID, naming every file that claims it."""
    return "\n".join(
        f"  {i} claimed by: {', '.join(files)}"
        for i, files in sorted(duplicates.items())
    )


def test_steering_note_ids_are_unique():
    """No unratified ID collision in the real corpus.

    The one tolerated exception is ``RATIFIED_COLLISIONS``; everything else is a
    defect. If this fails, fix the corpus — do not widen the allowlist.
    """
    duplicates = unratified_duplicates(STEERING_NOTES_DIR)
    assert not duplicates, (
        f"{len(duplicates)} unratified duplicate Steering Note ID(s) in "
        f"{display_path(STEERING_NOTES_DIR)}:\n"
        f"{format_duplicates(duplicates)}\n"
        f"Ratified exceptions (not reported above): "
        f"{', '.join(sorted(RATIFIED_COLLISIONS))}"
    )


def write_note(directory, name, ids):
    """Write a minimal Steering Note claiming ``ids``."""
    concerns = "\n".join(
        f"  - id: {i}\n    severity: medium\n    title: concern {i}" for i in ids
    )
    (directory / name).write_text(
        f"---\nartifact_type: steering_note\nconcerns:\n{concerns}\n---\n\n# Note\n",
        encoding="utf-8",
    )


def test_duplicate_across_two_notes_is_detected(tmp_path):
    write_note(tmp_path, "a.md", ["SN-40"])
    write_note(tmp_path, "b.md", ["SN-40"])
    assert find_duplicates(tmp_path) == {"SN-40": ["a.md", "b.md"]}


def test_duplicate_within_one_note_is_detected(tmp_path):
    write_note(tmp_path, "a.md", ["SN-41", "SN-41"])
    assert find_duplicates(tmp_path) == {"SN-41": ["a.md", "a.md"]}


def test_letter_suffixed_sub_ids_are_not_flagged(tmp_path):
    """``SN-12``, ``SN-12a`` and ``SN-12b`` are three distinct IDs, not a collision."""
    write_note(tmp_path, "a.md", ["SN-12", "SN-12a", "SN-12b"])
    assert find_duplicates(tmp_path) == {}


def test_repeated_sub_id_is_still_a_collision(tmp_path):
    """Sub-IDs are not exempt — two notes claiming ``SN-12a`` collide."""
    write_note(tmp_path, "a.md", ["SN-12a"])
    write_note(tmp_path, "b.md", ["SN-12a"])
    assert find_duplicates(tmp_path) == {"SN-12a": ["a.md", "b.md"]}


def test_distinct_ids_do_not_collide(tmp_path):
    write_note(tmp_path, "a.md", ["SN-42"])
    write_note(tmp_path, "b.md", ["SN-43", "SN-44"])
    assert find_duplicates(tmp_path) == {}


def test_failure_message_names_every_claimant(tmp_path):
    """B3.1's acceptance criterion: the message names the ID and *all* claiming files."""
    write_note(tmp_path, "a.md", ["SN-45"])
    write_note(tmp_path, "b.md", ["SN-45"])
    write_note(tmp_path, "c.md", ["SN-45"])
    message = format_duplicates(find_duplicates(tmp_path))
    assert "SN-45" in message
    for name in ("a.md", "b.md", "c.md"):
        assert name in message


def test_files_without_front_matter_are_ignored(tmp_path):
    (tmp_path / "plain.md").write_text("# not a steering note\n", encoding="utf-8")
    assert find_duplicates(tmp_path) == {}


def test_real_corpus_is_parseable():
    """Guard the guard: if parsing silently yields nothing, the check above is vacuous."""
    claims = collect_ids(STEERING_NOTES_DIR)
    assert len(claims) > 20, f"expected the full SN corpus, parsed only {len(claims)} IDs"


def test_real_corpus_collisions_are_exactly_the_ratified_set():
    """Every surviving collision is allowlisted, and every allowlist entry is still needed.

    SN-28 named two collisions and fail-fast would have hidden one, which is why
    this check reports the whole set rather than the first. Post-M36 the set is
    exactly one — ``SN-23``, ratified by HQ Ruling 2026-08-01 Decision 4 — because
    E36.2 renumbered the Layer-8/CFO note ``SN-1`` → ``SN-29``.

    Equality, not containment, is the point: it fails from *both* sides. A new
    collision fails it (as it fails the guard above), and so does an allowlist
    entry whose collision no longer exists — a stale exemption is a blanket
    waiting to happen, so removing the note must also mean removing the entry.
    """
    duplicates = find_duplicates(STEERING_NOTES_DIR)
    assert set(duplicates) == set(RATIFIED_COLLISIONS), (
        f"expected exactly the ratified collision(s) "
        f"{sorted(RATIFIED_COLLISIONS)}, found: {sorted(duplicates)}"
    )


def test_synthetic_third_collision_fails_the_guard(tmp_path, monkeypatch):
    """A *third*, unratified collision fails the suite — demonstrated, not asserted.

    This is what separates a narrow allowlist from a blanket exemption, so it is
    shown against the real corpus rather than a toy one: copy it, confirm the
    guard passes on the copy, introduce one duplicate, and confirm the guard's
    own assertion fires and names the offending ID.

    The synthetic duplicate claims ``SN-29`` — the ID E36.2 allocated — so this
    also covers the concrete risk the allocation rule runs: a note filed between
    planning and execution quietly claiming the ID someone else was about to use.
    """
    corpus = tmp_path / "steering-notes"
    shutil.copytree(STEERING_NOTES_DIR, corpus)
    monkeypatch.setattr(f"{__name__}.STEERING_NOTES_DIR", corpus)

    # The copy is clean, so any failure below is caused by the note added next.
    test_steering_note_ids_are_unique()

    write_note(corpus, "zz-synthetic-third-collision.md", ["SN-29"])

    with pytest.raises(AssertionError, match="SN-29"):
        test_steering_note_ids_are_unique()

    # The ratified collision is still tolerated: this is an exception, not an
    # amnesty, and the new ID is reported alone.
    assert set(unratified_duplicates(corpus)) == {"SN-29"}
    assert "SN-23" in find_duplicates(corpus)
