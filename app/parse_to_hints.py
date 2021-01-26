from pydantic import BaseModel

import re
from typing import List


class Verse(BaseModel):
    verse: int
    hint: str
    rest: List[str]


class Chapter(BaseModel):
    chapter: int
    verses: List[Verse]


def chapter_to_hints(
    passage: str,
    chapter: int,
    initial_hint_size: int,
    remainder_size: int,
) -> Chapter:
    VERSE = re.compile(r"\[([\d]+)\]")
    split_passage = [
        v.strip()
        for v in VERSE.split(passage)
        if v.strip()
    ]

    verse_numbers = [int(n) for n in split_passage[0::2]]
    verse_text = split_passage[1::2]
    verses = list(zip(verse_numbers, verse_text))

    verse_obj = [
        verse_to_hints(
            text=t,
            verse=v,
            initial_hint_size=initial_hint_size,
            remainder_size=remainder_size,
        )
        for v, t in verses
    ]

    return Chapter(chapter=chapter, verses=verse_obj)


def verse_to_hints(
    text: str,
    verse: int,
    initial_hint_size: int,
    remainder_size: int,
) -> Verse:
    chunks = text.split()
    hint = ""
    rest = []

    if (
        initial_hint_size == -1
        or initial_hint_size >= len(chunks)
    ):
        hint = text
        return Verse(verse=verse, hint=hint, rest=rest)

    hint = " ".join(chunks[0:initial_hint_size])

    if remainder_size == -1:
        rest = [" ".join(chunks[initial_hint_size:])]
        return Verse(verse=verse, hint=hint, rest=rest)

    rest = [
        " ".join(chunks[i : i + remainder_size])
        for i in range(
            initial_hint_size,
            len(chunks),
            remainder_size,
        )
    ]

    return Verse(verse=verse, hint=hint, rest=rest)
