"""Uniqueness check for Steering Note IDs (Bugfix B3.1).

Background
----------
Steering Note IDs are allocated by whichever agent writes the note, by reading
prior notes and incrementing. There is no registry and no allocation rule, so
correctness depends entirely on the author's attention. SN-28 (2026-08-01)
audited ``.ai-project/artifacts/steering-notes/`` and found 28 IDs across 23
notes with **two double-claimed**:

* ``SN-23`` — ``2026-07-18__...__reference-dont-display.md`` and
  ``2026-07-20__...__P10-adoption-spine.md``
* ``SN-1`` — ``2026-06-12__creation-chat__steering-note.md`` and
  ``2026-07-31__layer-8-cfo__...__system-hq-routing-model.md``

A duplicate ID is untidy. A duplicate ID *cited by number in normative
documents*, where one of the two meanings is partly superseded, is a trap:
``AI-OPERATING-GUIDELINES.md`` and ``chat-hierarchy.md`` both cite "SN-23
Decision 2" meaning unrelated decisions, and the latter declares its one
superseded. This test is the only durable guard against the class — the
allocation rule and the citation fixes are documentation, and documentation
drifts.

Why the real-corpus check is ``xfail``
--------------------------------------
Both collisions exist right now, so the check fails on arrival. Per the B3.1
spec that is expected and is **not** a reason to weaken it. The marker is
``strict=True`` deliberately: once P11-M36 (E36.1/E36.2) clears the collisions
the check will XPASS, and a strict xfail turns an unexpected pass into a
failure. That forces M36 to remove the marker rather than leaving a
permanently-tolerated failure in the suite — a mechanical completion signal
rather than a judgment call.

The unit tests below run against temporary directories and are **not** xfailed,
so the detector itself is proven regardless of the corpus's state.

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

If this check fails: read the reported ID and the files claiming it, then follow
SN-28's remediation — a bookkeeping defect never rewrites a citation in a
normative document, so renumber only where the ID is cited in project-internal,
non-normative artifacts, and date-qualify the citations otherwise.
"""

from collections import defaultdict
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
STEERING_NOTES_DIR = REPO_ROOT / ".ai-project" / "artifacts" / "steering-notes"

KNOWN_COLLISIONS_REASON = (
    "SN-23 and SN-1 are each double-claimed (SN-28). Cleared by P11-M36 "
    "(E36.1 citation fix, E36.2 renumber); strict=True so this fails as an "
    "XPASS once they are, forcing this marker's removal."
)


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


def format_duplicates(duplicates):
    """One line per colliding ID, naming every file that claims it."""
    return "\n".join(
        f"  {i} claimed by: {', '.join(files)}"
        for i, files in sorted(duplicates.items())
    )


@pytest.mark.xfail(strict=True, reason=KNOWN_COLLISIONS_REASON)
def test_steering_note_ids_are_unique():
    """No ID is claimed by two Steering Notes in the real corpus."""
    duplicates = find_duplicates(STEERING_NOTES_DIR)
    assert not duplicates, (
        f"{len(duplicates)} duplicate Steering Note ID(s) in "
        f"{STEERING_NOTES_DIR.relative_to(REPO_ROOT)}:\n"
        f"{format_duplicates(duplicates)}"
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


def test_both_known_collisions_are_reported():
    """Not just the first — SN-28 names two, and fail-fast would hide one."""
    duplicates = find_duplicates(STEERING_NOTES_DIR)
    assert set(duplicates) == {"SN-23", "SN-1"}, (
        f"expected exactly the two SN-28 collisions, found: {sorted(duplicates)}"
    )
