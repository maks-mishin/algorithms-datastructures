import unittest

from unmanned import Unmanned


class TestTrafficLight(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]), 12)
        self.assertEqual(Unmanned(5, 1, [[1, 5, 5]]), 9)
        self.assertEqual(Unmanned(154, 1, [[145, 2, 2]]), 155)
        self.assertEqual(Unmanned(
            20, 3, [[7, 4, 2], [9, 2, 4], [13, 5, 4]]), 30
        )
        self.assertEqual(Unmanned(10, 2, [[11, 5, 5], [15, 2, 2]]), 10)
        self.assertEqual(Unmanned(10, 2, [[4, 5, 5], [15, 2, 2]]), 11)


if __name__ == "__main__":
    unittest.main()
