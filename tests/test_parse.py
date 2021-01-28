from api.parse import (
    get_passage,
    Verse,
    Chapter,
    Book,
)
import unittest


class test_get_passage(unittest.TestCase):
    # TODO: clean up nasty test
    def test(self):
        passage = "  [1] If then you have been raised with Christ, seek the things that are above, where Christ is, seated at the right hand of God. [2] Set your minds on things that are above, not on things that are on earth.\n\n"
        book = "Colossians"
        chapter = 3
        gold = [
            Verse(
                **{
                    "verse": 1,
                    "text": "If then you have been raised with Christ, seek the things that are above, where Christ is, seated at the right hand of God."
                }
            ),
            Verse(
                **{
                    "verse": 2,
                    "text": "Set your minds on things that are above, not on things that are on earth."
                }
            )
        ]
        gold = Chapter(chapter=chapter, verses=gold)
        gold = Book(book=book, chapters=[gold])
        output = get_passage(passage, book=book, chapter=chapter)
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
