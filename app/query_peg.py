# type: ignore


from pyparsing import (
    Char,
    Combine,
    Optional,
    Word,
    alphas,
    nums,
)

from collections import namedtuple


__all__ = ["get_book_and_chapter", "BookAndChapter"]


book_num = Char(nums)
book_name = Combine(
    Word(alphas)
    + Optional(  # noqa W503
        Combine(Char(" ") + Word(alphas))
    )
)
book = Combine(
    Optional(book_num) + Optional(Char(" ")) + book_name
)
chapter = Word(nums)
passage = book("book") + Optional(chapter)("chapter")


BookAndChapter = namedtuple(
    "BookAndChapter",
    ["book", "chapter"],
    defaults=[None, None],
)


def get_book_and_chapter(psg_str: str) -> BookAndChapter:
    parsed = passage.parseString(psg_str).asDict()
    return BookAndChapter(**parsed)
