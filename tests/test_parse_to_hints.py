from app.parse_to_hints import (
    chapter_to_hints,
    verse_to_hints,
    Verse,
    Chapter,
)
import unittest


class test_parse_to_hints(unittest.TestCase):
    def test(self):
        passage = "  [12] Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,\n\n"
        chapter = 3
        initial_hint_size = 3
        remainder_size = 6
        gold = [
            Verse(
                **{
                    "verse": 12,
                    "hint": "Put on then,",
                    "rest": [
                        "as God's chosen ones, holy and",
                        "beloved, compassionate hearts, kindness, humility, meekness,",
                        "and patience,",
                    ],
                }
            ),
        ]
        gold = Chapter(chapter=chapter, verses=gold)
        output = chapter_to_hints(
            passage,
            chapter=chapter,
            initial_hint_size=initial_hint_size,
            remainder_size=remainder_size,
        )
        self.assertEqual(gold, output)


class test_chunks_to_hint(unittest.TestCase):
    def test_all_hint(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        initial_hint_size = -1
        remainder_size = None
        gold = Verse(
            **{
                "verse": 12,
                "hint": "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
                "rest": [],
            }
        )
        output = verse_to_hints(
            text=text,
            verse=verse,
            initial_hint_size=initial_hint_size,
            remainder_size=remainder_size,
        )
        self.assertEqual(gold, output)

    def test_hint_greater_than_verse(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        initial_hint_size = -1
        remainder_size = None
        gold = Verse(
            **{
                "verse": 12,
                "hint": "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
                "rest": [],
            }
        )
        output = verse_to_hints(
            text=text,
            verse=verse,
            initial_hint_size=initial_hint_size,
            remainder_size=remainder_size,
        )
        self.assertEqual(gold, output)

    def test_hint_size_and_remainder_size(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        initial_hint_size = 3
        remainder_size = 6
        gold = Verse(
            **{
                "verse": 12,
                "hint": "Put on then,",
                "rest": [
                    "as God's chosen ones, holy and",
                    "beloved, compassionate hearts, kindness, humility, meekness,",
                    "and patience,",
                ],
            }
        )
        output = verse_to_hints(
            text=text,
            verse=verse,
            initial_hint_size=initial_hint_size,
            remainder_size=remainder_size,
        )
        self.assertEqual(gold, output)

    def test_remainder_size_all(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        initial_hint_size = 3
        remainder_size = -1
        gold = Verse(
            **{
                "verse": 12,
                "hint": "Put on then,",
                "rest": [
                    "as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
                ],
            }
        )
        output = verse_to_hints(
            text=text,
            verse=verse,
            initial_hint_size=initial_hint_size,
            remainder_size=remainder_size,
        )
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
