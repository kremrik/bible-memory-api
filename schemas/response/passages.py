from pydantic import BaseModel, validator

from typing import Any, List


__all__ = ["BibleResponse", "AddPassageResponse"]


UUID = Any


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


class AddPassageResponse(BaseModel):
    user_id: UUID
    passage: str

    @validator("user_id")
    def convert_user_id(cls, uid):
        return str(uid)
