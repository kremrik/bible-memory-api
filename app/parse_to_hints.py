from pydantic import BaseModel

import re
from typing import List


class Verse(BaseModel):
    verse: int
    hint: str
    rest: str


class Chapter(BaseModel):
    chapter: int
    verses: List[Verse]


def chapter_to_hints(passage: str, chapter: int, hint_min: int) -> Chapter:
    VERSE = re.compile(r"\[([\d]+)\]")
    split_passage = [v.strip() for v in VERSE.split(passage) if v.strip()]
    
    verse_numbers = [int(n) for n in split_passage[0::2]]
    verse_text = split_passage[1::2]
    verses = list(zip(verse_numbers, verse_text))

    verse_objs = [
        verse_to_hints(text=t, verse=v, hint_min=hint_min)
        for v, t in verses
    ]

    return Chapter(chapter=chapter, verses=verse_objs)


def verse_to_hints(
    text: str, verse: int, hint_min: int
) -> Verse:
    # TODO: handle situation where no commas exist in verse

    if hint_min == -1:
        return Verse(verse=verse, hint=text, rest="")

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

    return Verse(verse=verse, hint=hint, rest=rest)
