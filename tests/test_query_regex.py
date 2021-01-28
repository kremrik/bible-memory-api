from api.query_regex import parse_query, bible_passage
import unittest


class test_parse_query(unittest.TestCase):
    def test_book(self):
        query = "Colossians"
        gold = bible_passage("Colossians")
        output = parse_query(query)
        self.assertEqual(gold, output)

    def test_numbered_book(self):
        query = "1 Corinthians"
        gold = bible_passage("1 Corinthians")
        output = parse_query(query)
        self.assertEqual(gold, output)

    def test_numbered_book_chapter(self):
        query = "1 Corinthians 1"
        gold = bible_passage("1 Corinthians", 1)
        output = parse_query(query)
        self.assertEqual(gold, output)

    def test_numbered_book_chapter_verse(self):
        query = "1 Corinthians 1:1"
        gold = bible_passage("1 Corinthians", 1, [1])
        output = parse_query(query)
        self.assertEqual(gold, output)

    def test_numbered_book_chapter_verses(self):
        query = "1 Corinthians 1:1-2"
        gold = bible_passage("1 Corinthians", 1, [1, 2])
        output = parse_query(query)
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
