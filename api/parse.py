from pydantic import BaseModel

import re
from typing import List


class Verse(BaseModel):
    verse: int
    text: str


class Chapter(BaseModel):
    chapter: int
    verses: List[Verse]


class Book(BaseModel):
    book: str
    chapters: List[Chapter]


def get_passage(passage: str, book: str, chapter: int) -> Chapter:
    VERSE = re.compile(r"\[([\d]+)\]")
    split_passage = [
        v.strip()
        for v in VERSE.split(passage)
        if v.strip()
    ]

    verse_numbers = [int(n) for n in split_passage[0::2]]
    verse_text = split_passage[1::2]
    verses_raw = list(zip(verse_numbers, verse_text))
    verses = [Verse(verse=v, text=t) for v, t in verses_raw]

    chapter = Chapter(chapter=chapter, verses=verses)
    return Book(book=book, chapters=[chapter])
