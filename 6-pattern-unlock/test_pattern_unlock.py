import unittest

from pattern_unlock import PatternUnlock


class TestPatternUnlock(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]), '982843')
        self.assertEqual(PatternUnlock(11, [4, 2, 3, 7, 8, 9, 1, 2, 5, 6, 1]), '141421')

    def test_one_digit(self):
        self.assertEqual(PatternUnlock(1, [2]), '')

    def test_empty(self):
        self.assertEqual(PatternUnlock(0, []), '')

    def test_large_code(self):
        seq_digits = [6, 1, 9, 2, 1, 6, 5, 3, 8, 7, 2 ,6, 1, 9]
        self.assertEqual(PatternUnlock(len(seq_digits), seq_digits), '15717')


if __name__ == "__main__":
    unittest.main()
