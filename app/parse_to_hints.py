from pydantic import BaseModel

import re
from typing import List


class Hint(BaseModel):
    verse: int
    hint: str
    rest: str


def chapter_to_hints(passage: str, hint_min: int) -> List[Hint]:
    VERSE = re.compile(r"\[([\d]+)\]")
    split_passage = [v.strip() for v in VERSE.split(passage) if v.strip()]
    
    verse_numbers = [int(n) for n in split_passage[0::2]]
    verse_text = split_passage[1::2]
    verses = list(zip(verse_numbers, verse_text))

    return [
        verse_to_hints(text=t, verse=v, hint_min=hint_min)
        for v, t in verses
    ]


def verse_to_hints(
    text: str, verse: int, hint_min: int
) -> Hint:
    if hint_min == -1:
        return Hint(verse=verse, hint=text, rest="")

    chunks = text.split(", ")
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
