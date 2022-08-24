import unittest

from mad_max import MadMax


class TestMadMax(unittest.TestCase):
    def test_mad_max(self):
        result = MadMax(9, [4, 2, 9, 5, 1, 3, 7, 6, 8])
        self.assertEqual(result, [1, 2, 3, 4, 9, 8, 7, 6, 5])
        self.assertEqual(MadMax(3, [1, 1, 1]), [1, 1, 1])
        self.assertEqual(MadMax(4, [5, 1, 7, 9, 1]), [1, 1, 9, 7, 5])


if __name__ == "__main__":
    unittest.main()
