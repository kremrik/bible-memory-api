from app.query_peg import get_book_and_chapter  # type: ignore  # noqa E501
from schemas.response.passages import (
    BibleResponse,
    Chapter,
    Passage,
    Verse,
)

import re
from typing import List


__all__ = ["get_passage", "BibleResponse"]


def get_passage(response: dict) -> BibleResponse:
    psgs = passages(response)
    return BibleResponse(passages=psgs)


def passages(response: dict) -> List[Passage]:
    queries = response["canonical"].split("; ")
    psgs = response["passages"]
    qrys_and_psgs = list(zip(queries, psgs))

    passages_ = []

    for qry_, psg_ in qrys_and_psgs:
        canonical = qry_.strip()
        book_, chapter_ = get_book_and_chapter(qry_)
        verses_ = verses(psg_)
        chapter = Chapter(chapterNum=chapter_, verses=verses_)
        passage = Passage(
            canonical=canonical, book=book_, chapter=chapter
        )
        passages_.append(passage)

    return passages_


VERSE = re.compile(r"\[([\d]+)\]")


def verses(passage: str) -> List[Verse]:
    split_passage = [
        v.strip() for v in VERSE.split(passage) if v.strip()
    ]

    verse_numbers = [int(n) for n in split_passage[0::2]]
    verse_text = split_passage[1::2]
    verses = list(zip(verse_numbers, verse_text))
    verse_obj = [Verse(verse=v[0], text=v[1]) for v in verses]

    return verse_obj
