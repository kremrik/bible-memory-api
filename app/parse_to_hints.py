from pydantic import BaseModel

import re
from typing import List


# __all__ = ["PassageResponse", "parse_to_hints"]


class Hint(BaseModel):
    verse: int
    hint: str
    rest: str


class PassageResponse(BaseModel):
    data: List[Hint]


def parse_to_hints(passage: str) -> PassageResponse:
    VERSE = re.compile(r"\[([\d+])\]")
    split_passage = VERSE.split(passage)

    verse = None
    hint = ""
    rest = ""

    for p in split_passage:
        p = p.strip()

        if not p:
            continue

        if p.isdigit():
            verse = int(p)
            continue

        chunks = p.split(", ")
        for c in chunks:
            pass


def chunks_to_hint(
    chunks: List[str], verse: int, hint_min: int
) -> Hint:
    if hint_min == -1:
        return Hint(
            verse=verse, hint=", ".join(chunks), rest=""
        )

    hint = ""
    rest = ""

    for idx, c in enumerate(chunks):
        if not hint:
            hint = c
            continue

        hint_size = hint.split()
        if len(hint_size) >= hint_min:
            rest = ", ".join(chunks[idx:])
            break

        hint = hint + ", " + c

    return Hint(verse=verse, hint=hint, rest=rest)
