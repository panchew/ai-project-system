"""Reference solution — proves TASK-DEV-1 is solvable. NEVER instantiated into a run."""

import re

_UNITS = [("w", 604800), ("d", 86400), ("h", 3600), ("m", 60), ("s", 1)]
_GROUP = re.compile(r"(\d+)([wdhms])")


def parse_duration(text):
    if not isinstance(text, str):
        raise TypeError("parse_duration accepts str only")
    stripped = text.strip()
    if not stripped:
        raise ValueError("empty duration")
    order = {unit: i for i, (unit, _) in enumerate(_UNITS)}
    seconds = 0
    pos = 0
    last = -1
    while pos < len(stripped):
        m = _GROUP.match(stripped, pos)
        if not m:
            raise ValueError(f"invalid duration: {text!r}")
        count, unit = int(m.group(1)), m.group(2)
        if order[unit] <= last:
            raise ValueError(f"units out of order or repeated: {text!r}")
        last = order[unit]
        seconds += count * dict(_UNITS)[unit]
        pos = m.end()
    return seconds
