import unittest

from word_search import WordSearch


class TestWordSearch(unittest.TestCase):
    def test_word_search(self):
        result = WordSearch(12, "1) stroka razbivaetsya na nabor strok cherez vyravnivanie po zadannoj shirine.", "strok")
        self.assertEqual(result, [0, 0, 0, 1, 0, 0, 0])

        result_1 = WordSearch(12, "строка разбивается на набор строк через выравнивание по заданной ширине.", "строк")
        self.assertEqual(result_1, [0, 0, 0, 1, 0, 0, 0])

        result_2 = WordSearch(5, "This is a minimum valuable product", "This")
        self.assertEqual(result_2, [1, 0, 0, 0, 0, 0, 0, 0])

        result = WordSearch(3, "строка разбивается", "строк")
        self.assertEqual(result, [0, 0, 0, 0, 0, 0])
        self.assertEqual(WordSearch(10, '', 'о'), [])
        self.assertEqual(WordSearch(0, 'привет как дела', ''), [])


if __name__ == "__main__":
    unittest.main()
