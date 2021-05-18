from pydantic import BaseModel

from typing import List


class Verse(BaseModel):
    verse: int
    text: str


class Chapter(BaseModel):
    chapterNum: int
    verses: List[Verse]


class Passage(BaseModel):
    book: str
    chapter: Chapter


class BibleResponse(BaseModel):
    passages: List[Passage]
