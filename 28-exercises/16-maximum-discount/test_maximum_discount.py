import unittest

from maximum_discount import MaximumDiscount


class TestTankRush(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(MaximumDiscount(7, [450, 300, 250, 200, 100, 150, 350]), 450)
        self.assertEqual(MaximumDiscount(5, [100, 100, 100, 100, 100]), 100)
        self.assertEqual(MaximumDiscount(3, [150, 200, 250]), 150)
        self.assertEqual(MaximumDiscount(1, [100]), 0)


if __name__ == "__main__":
    unittest.main()
