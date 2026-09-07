"""Fence-aware AOG section-numbering check (Epic E44.4, D5).

Background
----------
The AI-OPERATING-GUIDELINES.md carried, for ten phases, a section numbering
that could not be cited unambiguously: ``13`` and ``14`` each appeared twice,
two sections shared the title "Error Handling", and the order was
``1, 1A, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 10, 11, 12, 13, 14, 16, 15`` (E44.4,
X1). E44.4 renumbered the real sections to ``1..n`` in place and swept every
cross-reference; this check is the durable guard against the class returning.

The check must be fence-aware for the same reason the renumber was (X1):
a naive ``grep '^## '`` finds 29 headings of which only 20 (now 19) are real
sections — the rest are the ``## `` headings *inside the `````markdown example
blocks the document quotes*. A pass that renumbers, or a check that reads,
those fenced headings as sections is the exact defect this guard exists to
prevent.

The fence detector (``FENCE_LINE_RE``) must also handle the AOG's ``:134``
hazard — an indented four-backtick marker with a trailing stray backtick that
is a *prose illustration*, not a real delimiter. A toggle detector that treats
any backtick run as a fence counts 17 fence lines (odd) and desyncs there,
inverting its classification for the remaining ~900 lines *silently*. So the
check carries a **parity self-test**: an odd real-fence-line count is a loud
failure, because it means the detector is about to lie.

The scheme this check asserts (D2's recorded decision, spec option 2): ``1A``
is folded into section 1 as sub-part ``### 1.1``, so the ``## `` real sections
are a clean integer sequence ``1..n`` with no gaps, no duplicates, and unique
titles. ``Changelog`` is exempt (unnumbered by recorded decision).

If this check fails: the AOG's real sections have drifted from ``1..n`` —
re-read the AOG's ``## `` headings (fence-aware), restore the numbering, and
re-sweep any cross-references. Do not add the drifting section to an
allowlist; the check has exactly one exemption (``Changelog``) and it is
recorded.
"""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
AOG_PATH = REPO_ROOT / "governance" / "AI-OPERATING-GUIDELINES.md"

# A real fence delimiter: 0-3 leading spaces, a run of 3+ backticks, then at
# most an info-string (no backticks, per CommonMark) and trailing whitespace.
# Rejects the AOG's :134 illustration (indented four-backtick marker with a
# trailing stray backtick run) — it is prose, not a delimiter.
FENCE_LINE_RE = re.compile(r"^ {0,3}(`{3,})(?:[^\n`]*)?\s*$")

# A real ``## `` heading (level-2 ATX heading).
HEADING_RE = re.compile(r"^##\s+(.+)$")

# A numbered ``## `` heading's text (after ``## ``): ``<number>. <title>``.
NUMBERED_RE = re.compile(r"^(\d+)\s*\.\s+(.+)$")

# The one unnumbered real section, exempted by E44.4's recorded decision.
EXEMPT_HEADING = "Changelog"


def fence_line_numbers(text):
    """1-based line numbers of real fence delimiters in ``text``."""
    return [i for i, line in enumerate(text.splitlines(), 1)
            if FENCE_LINE_RE.match(line)]


def fenced_line_set(text):
    """Line numbers inside a real fence; raises on an odd fence-line count.

    An odd count is the detector-desync tell (the ``:134`` hazard): the AOG's
    real fences number 16 (even). A toggle detector that counted the stray
    illustration would report 17 (odd) and silently invert every later line —
    so the check fails loudly instead of trusting a wrong parse.
    """
    fences = fence_line_numbers(text)
    if len(fences) % 2 != 0:
        raise AssertionError(
            f"odd fence-line count ({len(fences)}) — the fence detector is "
            f"about to desync; non-triple/indented backtick markers are being "
            f"read as delimiters. Real fences must pair."
        )
    fenced = set()
    f = False
    start = None
    for lineno in fences:
        if not f:
            f = True
            start = lineno
        else:
            f = False
            fenced.update(range(start, lineno + 1))
    return fenced


def real_headings(text):
    """(lineno, heading_text) for every ``## `` heading outside a real fence."""
    fenced = fenced_line_set(text)
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("## ") and i not in fenced:
            m = HEADING_RE.match(line)
            if m:
                out.append((i, m.group(1)))
    return out


def aog_section_errors(text):
    """The AOG's numbering defects as an itemized list, or an empty list.

    Reported per defect, never as a bare count: duplicate numbers, a
    non-monotonic sequence (out-of-order, a gap, or an extra section), and
    duplicate titles each produce their own line.
    """
    headings = real_headings(text)
    numbered = []
    for lineno, heading in headings:
        m = NUMBERED_RE.match(heading)
        if m:
            numbered.append((lineno, int(m.group(1)), m.group(2)))
        elif heading.strip() != EXEMPT_HEADING:
            # A real, numbered-scheme section without a number is a drift.
            # (Changelog is the recorded exemption.)
            return [f"line {lineno}: real section with no number: {heading!r}"]

    numbers = [n for _, n, _ in numbered]
    titles = [t for _, _, t in numbered]

    errors = []
    # Duplicate numbers, itemized by value and line.
    seen = {}
    for lineno, n, _ in numbered:
        if n in seen:
            errors.append(
                f"duplicate section number {n}: lines {seen[n]} and {lineno}"
            )
        else:
            seen[n] = lineno
    # Monotonicity: ascending 1..n, no gaps, no out-of-order. Equality to the
    # identity range detects duplicates too, but the itemized check above
    # reports them by value; this line reports the order/gap defect.
    if numbers != list(range(1, len(numbers) + 1)):
        errors.append(
            f"section numbers not monotonic 1..n: {numbers!r} "
            f"(order, gap, or extra section)"
        )
    # Duplicate titles, itemized.
    seen_titles = {}
    for lineno, _, t in numbered:
        if t in seen_titles:
            errors.append(
                f"duplicate section title {t!r}: lines "
                f"{seen_titles[t]} and {lineno}"
            )
        else:
            seen_titles[t] = lineno
    return errors


def test_aog_sections_are_1_to_n_with_unique_numbers_and_titles():
    """The real AOG's ``## `` real sections are ``1..n``, unique by number and title.

    Fence-aware: the document's quoted example bodies (``## Completion
    Verification``, ``## Epic Review Seal``, …) are inside real fences and are
    read as examples, never as sections. Fails loudly if the real fence-line
    count is odd (the detector-desync tell).
    """
    errors = aog_section_errors(AOG_PATH.read_text(encoding="utf-8"))
    assert not errors, (
        "AI-OPERATING-GUIDELINES.md section numbering has drifted:\n"
        + "\n".join(f"  - {e}" for e in errors)
    )


def test_fence_line_count_is_even():
    """The parity self-test on the real corpus: 16 real fence lines (even)."""
    fences = fence_line_numbers(AOG_PATH.read_text(encoding="utf-8"))
    assert len(fences) % 2 == 0, f"odd fence-line count: {len(fences)}"


def test_odd_fence_count_fails_loudly():
    """A detector desync (an unpaired fence) is a loud failure, not silent
    wrong output. Reintroduce the ``:134`` hazard's shape: a backtick run that
    is really a prose illustration, counted as a delimiter, unbalances the
    pair — the check must refuse to trust its own parse."""
    # One real opener with no closer: an odd real-fence-line count.
    text = "```\ncode that never closes\n## 1. Real\n"
    with pytest.raises(AssertionError, match="odd fence-line count"):
        fenced_line_set(text)
    # The AOG's own hazard line, naively counted, would make the count odd.
    naive = "```\n```\n    ````markdown name=<artifact-filename>.md`` `\n"
    assert fence_line_numbers(naive) == [1, 2], (
        "the correct detector must not count the indented illustration as a "
        "fence delimiter"
    )


def test_synthetic_duplicate_number_fails(tmp_path):
    """A reintroduced duplicate section number fails the check (falsification)."""
    text = (
        "## 1. One\n\n## 2. Two\n\n## 2. Two Again\n\n## 3. Three\n"
    )
    errors = aog_section_errors(text)
    assert any("duplicate section number 2" in e for e in errors)


def test_synthetic_out_of_order_fails(tmp_path):
    """A section numbered ``16`` landing before ``15`` fails (out-of-order)."""
    text = (
        "## 1. One\n## 2. Two\n## 4. Four\n## 3. Three\n"
    )
    errors = aog_section_errors(text)
    assert any("not monotonic" in e for e in errors)


def test_synthetic_gap_fails(tmp_path):
    """A missing number in the middle of the sequence fails (gap)."""
    text = "## 1. One\n## 3. Three\n"
    errors = aog_section_errors(text)
    assert any("not monotonic" in e for e in errors)


def test_synthetic_duplicate_title_fails(tmp_path):
    """Two sections sharing a title fail the check."""
    text = "## 1. Error Handling\n## 2. Error Handling\n"
    errors = aog_section_errors(text)
    assert any("duplicate section title" in e for e in errors)


def test_synthetic_fenced_headings_are_ignored():
    """``## `` lines inside a real fence are example bodies, never sections."""
    text = (
        "## 1. One\n\n"
        "```markdown\n"
        "## Completion Criteria Evaluation\n"
        "```\n\n"
        "## 2. Two\n"
    )
    errors = aog_section_errors(text)
    assert errors == []


def test_synthetic_clean_sequence_passes():
    """A clean ``1..n`` sequence passes; only ``Changelog`` is exempt."""
    text = (
        "## 1. Purpose\n"
        "### 1.1 Canonical Happy Path\n"
        "## 2. Core Principles\n"
        "## Changelog\n"
    )
    errors = aog_section_errors(text)
    assert errors == []


def test_real_corpus_is_fence_aware_not_naive():
    """Guard the guard: the naive (fence-blind) read would report a different
    section set than the fence-aware read — the distinction is real on the
    current corpus, not a theoretical one."""
    text = AOG_PATH.read_text(encoding="utf-8")
    fenced = fenced_line_set(text)
    naive = [i for i, line in enumerate(text.splitlines(), 1)
             if line.startswith("## ")]
    aware = {i for i, _ in real_headings(text)}
    assert len(naive) != len(aware), "fence-awareness is vacuous on this corpus"
    assert len(aware) < len(naive)
    assert all(i in fenced for i in set(naive) - aware), (
        "every heading the fence-aware read excludes must be inside a real fence"
    )


def test_falsified_against_the_real_corpus(tmp_path, monkeypatch):
    """Falsify the guard on the real AOG, in both directions (E44.4 D5).

    The real corpus passes; reintroduce a duplicate section number and the
    guard fails, naming the collision; reintroduce an out-of-order section
    (16 before 15) and it fails on monotonicity; restore and it is green.
    """
    text = AOG_PATH.read_text(encoding="utf-8")
    # The copy is clean, so any failure below is caused by the mutation added.
    assert aog_section_errors(text) == []

    # Direction 1 — a reintroduced duplicate number (make a copy where a real
    # section shares the number of another).
    duplicate = text.replace(
        "## 15. Exit Ritual (Mandatory)",
        "## 14. Exit Ritual (Mandatory)",
        1,
    )
    errors = aog_section_errors(duplicate)
    assert any("duplicate section number 14" in e for e in errors)

    # Direction 2 — a reintroduced out-of-order section (16 before 15), which
    # is out-of-order without being a duplicate. Swap the two tail sections'
    # numbers so Exit Ritual reads 16 and Error Handling reads 15.
    reordered = (
        text.replace(
            "## 15. Exit Ritual (Mandatory)",
            "## 16. Exit Ritual (Mandatory)",
            1,
        ).replace(
            "## 16. Error Handling",
            "## 15. Error Handling",
            1,
        )
    )
    errors = aog_section_errors(reordered)
    assert any("not monotonic" in e for e in errors)

    # Direction 3 — a reintroduced duplicate title (the historical defect).
    titled = text.replace(
        "## 11. Evolution",
        "## 11. Error Handling",
        1,
    )
    errors = aog_section_errors(titled)
    assert any("duplicate section title" in e for e in errors)

    # Restore is green — the guard's own assertion on the unmutated corpus.
    assert aog_section_errors(text) == []