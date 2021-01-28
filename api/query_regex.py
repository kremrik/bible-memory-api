import pyparsing as pp

from collections import namedtuple
from typing import List


__all__ = ["parse_query", "bible_passage"]


bible_passage = namedtuple(
    typename="bible_passage", 
    field_names=["book", "chapter", "verses"],
    defaults=[None, None, []]
)


book_part = pp.Word(pp.alphas)
book_num = pp.Optional(pp.Char(pp.nums))
full_book = pp.Combine(book_num + pp.Optional(pp.White()) + book_part)

chapter = pp.Word(pp.nums)
verses = pp.Combine(pp.Word(pp.nums) + pp.Optional("-") + pp.Optional(pp.Word(pp.nums)))
chapter_and_verses = chapter + pp.Optional(":") + pp.Optional(verses)

passage = full_book + pp.Optional(chapter_and_verses)


def parse_query(query: str) -> bible_passage:
    tokens = query_to_tokens(query)
    return tokens_to_nt(tokens)


def query_to_tokens(query: str) -> List[str]:
    tokenized = passage.parseString(query)
    return list(tokenized)


def tokens_to_nt(tokens: List[str]) -> bible_passage:
    book = tokens[0]
    if len(tokens) == 1:
        return bible_passage(book=book)

    chapter = int(tokens[1])
    if ":" in tokens:
        verses = [int(v) for v in tokens[-1].split("-")]
        return bible_passage(book=book, chapter=chapter, verses=verses)

    return bible_passage(book=book, chapter=chapter)
