import unittest

from pattern_unlock import PatternUnlock


class TestPatternUnlock(unittest.TestCase):
    def test_pattern_unlock(self):
        self.assertEqual(PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]))
        self.assertEqual(PatternUnlock(11, [4, 2, 3, 7, 8, 9, 1, 2, 5, 6, 1]))


if __name__ == "__main__":
    unittest.main()
