from app.parse_to_hints import (
    chapter_to_hints,
    verse_to_hints,
    Hint
)
import unittest


class test_parse_to_hints(unittest.TestCase):
    def test(self):
        passage = "  [12] Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,\n\n"
        hint_min = 3
        gold = [
            Hint(**{
                "verse": 12,
                "hint": "Put on then",
                "rest": "as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
            }),
        ]
        output = chapter_to_hints(passage, hint_min=hint_min)
        self.assertEqual(gold, output)


class test_chunks_to_hint(unittest.TestCase):
    def test_all_hint(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        hint_min = -1
        gold = {
            "verse": 12,
            "hint": "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
            "rest": "",
        }
        gold = Hint(**gold)
        output = verse_to_hints(
            text=text, verse=verse, hint_min=hint_min
        )
        self.assertEqual(gold, output)

    def test_first_chunk_is_enough_hint(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        hint_min = 3
        gold = {
            "verse": 12,
            "hint": "Put on then",
            "rest": "as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
        }
        gold = Hint(**gold)
        output = verse_to_hints(
            text=text, verse=verse, hint_min=hint_min
        )
        self.assertEqual(gold, output)

    def test_combine_chunks_for_hint(self):
        text = "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,"
        verse = 12
        hint_min = 4
        gold = {
            "verse": 12,
            "hint": "Put on then, as God's chosen ones",
            "rest": "holy and beloved, compassionate hearts, kindness, humility, meekness, and patience,",
        }
        gold = Hint(**gold)
        output = verse_to_hints(
            text=text, verse=verse, hint_min=hint_min
        )
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
