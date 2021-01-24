from app.parse_to_hints import (
    chapter_to_hints,
    verse_to_hints,
    Verse,
    Chapter
)
import unittest


class test_parse_to_hints(unittest.TestCase):
    def test(self):
        passage = "  [12] Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,\n\n"
        chapter = 3
        hint_min = 3
        gold = [
            Verse(**{
                "verse": 12,
                "hint": "Put on then,",
                "rest": "as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
            }),
        ]
        gold = Chapter(chapter=chapter, verses=gold)
        output = chapter_to_hints(passage, chapter=chapter, hint_min=hint_min)
        print(output)
        self.assertEqual(gold, output)


class test_chunks_to_hint(unittest.TestCase):
    def test_all_hint(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        hint_min = -1
        gold = Verse(**{
            "verse": 12,
            "hint": "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
            "rest": "",
        })
        output = verse_to_hints(
            text=text, verse=verse, hint_min=hint_min
        )
        self.assertEqual(gold, output)

    def test_first_chunk_is_enough_hint(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        hint_min = 3
        gold = Verse(**{
            "verse": 12,
            "hint": "Put on then,",
            "rest": "as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
        })
        output = verse_to_hints(
            text=text, verse=verse, hint_min=hint_min
        )
        self.assertEqual(gold, output)

    def test_combine_chunks_for_hint(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        hint_min = 4
        gold = Verse(**{
            "verse": 12,
            "hint": "Put on then, as God's chosen ones,",
            "rest": "holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
        })
        output = verse_to_hints(
            text=text, verse=verse, hint_min=hint_min
        )
        self.assertEqual(gold, output)

    def test_no_commas(self):
        text = "On account of these the wrath of God is coming."
        verse = 6
        hint_min = 4
        gold = Verse(**{
            "verse": 6,
            "hint": "On account of these",
            "rest": "the wrath of God is coming.",
        })
        output = verse_to_hints(
            text=text, verse=verse, hint_min=hint_min
        )
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
