from app.passage import get_passage
import unittest


class test_get_passage(unittest.TestCase):

    def test_single_word_chapter(self):
        response = {
            "query": "Colossians 1:1\u20132",
            "canonical": "Colossians 1:1\u20132",
            "parsed": [
                [
                    51001001,
                    51001002
                ]
            ],
            "passage_meta": [
                {
                    "canonical": "Colossians 1:1\u20132",
                    "chapter_start": [
                        51001001,
                        51001029
                    ],
                    "chapter_end": [
                        51001001,
                        51001029
                    ],
                    "prev_verse": 50004023,
                    "next_verse": 51001003,
                    "prev_chapter": [
                        50004001,
                        50004023
                    ],
                    "next_chapter": [
                        51002001,
                        51002023
                    ]
                }
            ],
            "passages": [
                "  [1] Paul, an apostle of Christ Jesus by the will of God, and Timothy our brother,\n\n  [2] To the saints and faithful brothers in Christ at Colossae:\n\n  Grace to you and peace from God our Father.\n\n"
            ]
        }
        gold = {
            "passages": [
                {
                "book": "Colossians",
                "chapter": {
                    "chapterNum": 1,
                    "verses": [
                    {
                        "verse": 1,
                        "text": "Paul, an apostle of Christ Jesus by the will of God, and Timothy our brother,"
                    },
                    {
                        "verse": 2,
                        "text": "To the saints and faithful brothers in Christ at Colossae:\n\n  Grace to you and peace from God our Father."
                    }
                    ]
                }
                }
            ]
        }
        output = get_passage(response).dict()
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
