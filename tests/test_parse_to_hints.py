from app.parse_to_hints import (
    parse_to_hints,
    chunks_to_hint,
)
import unittest


@unittest.skip("not ready yet")
class test_parse_to_hints(unittest.TestCase):
    def test(self):
        passage = "  [12] Put on then, as God;s chosen ones, holy and beloved, \
            compassionate hearts, kindness, humility, meekness, and patience,\n\n"
        gold = [
            {
                "verse": 12,
                "hint": "Put on then,",
                "rest": "as God's chosen ones,",
            },
            {
                "verse": 12,
                "hint": "holy and beloved,",
                "rest": "compassionate hearts, kindness, humility, meekness, and patience",
            },
        ]
        output = parse_to_hints(passage).__dict__["data"]
        self.assertEqual(gold, output)


class test_chunks_to_hint(unittest.TestCase):
    def test_all_hint(self):
        chunks = [
            "Put on then",
            "as God's chosen ones",
            "holy and beloved",
            "compassionate hearts",
            "kindness",
            "humility",
            "meekness",
            "and patience",
        ]
        verse = 12
        hint_min = -1
        gold = {
            "verse": 12,
            "hint": "Put on then, as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience",
            "rest": "",
        }
        output = chunks_to_hint(
            chunks=chunks, verse=verse, hint_min=hint_min
        ).__dict__
        self.assertEqual(gold, output)

    def test_first_chunk_is_enough_hint(self):
        chunks = [
            "Put on then",
            "as God's chosen ones",
            "holy and beloved",
            "compassionate hearts",
            "kindness",
            "humility",
            "meekness",
            "and patience",
        ]
        verse = 12
        hint_min = 3
        gold = {
            "verse": 12,
            "hint": "Put on then",
            "rest": "as God's chosen ones, holy and beloved, compassionate hearts, kindness, humility, meekness, and patience",
        }
        output = chunks_to_hint(
            chunks=chunks, verse=verse, hint_min=hint_min
        ).__dict__
        self.assertEqual(gold, output)

    def test_combine_chunks_for_hint(self):
        chunks = [
            "Put on then",
            "as God's chosen ones",
            "holy and beloved",
            "compassionate hearts",
            "kindness",
            "humility",
            "meekness",
            "and patience",
        ]
        verse = 12
        hint_min = 4
        gold = {
            "verse": 12,
            "hint": "Put on then, as God's chosen ones",
            "rest": "holy and beloved, compassionate hearts, kindness, humility, meekness, and patience",
        }
        output = chunks_to_hint(
            chunks=chunks, verse=verse, hint_min=hint_min
        ).__dict__
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
