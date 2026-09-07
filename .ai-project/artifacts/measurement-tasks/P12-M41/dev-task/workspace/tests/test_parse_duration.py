"""The directional check for TASK-DEV-1. Committed before any run.

Twenty cases. The score is how many of them pass — mechanical, not a quality judgment.
"""

import pytest

from durations import parse_duration


@pytest.mark.parametrize(
    "text,expected",
    [
        ("45s", 45),
        ("0s", 0),
        ("007s", 7),
        ("90m", 5400),
        ("1h30m", 5400),
        ("2d4h", 187200),
        ("1w", 604800),
        ("1w1d1h1m1s", 694861),
        ("  1h  ", 3600),
        ("100h", 360000),
    ],
)
def test_valid_durations(text, expected):
    assert parse_duration(text) == expected


def test_returns_an_int():
    assert isinstance(parse_duration("1m"), int)


@pytest.mark.parametrize(
    "text",
    [
        "",
        "90",
        "h",
        "5y",
        "-5s",
        "30m1h",
        "1h1h",
        "1h 30m",
    ],
)
def test_invalid_durations_raise_value_error(text):
    with pytest.raises(ValueError):
        parse_duration(text)


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        parse_duration(90)
