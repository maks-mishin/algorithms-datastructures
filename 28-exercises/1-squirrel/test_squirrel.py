import unittest

from squirrel import squirrel


class TestSquirrel(unittest.TestCase):
    def test_squirrel(self):
        self.assertEqual(squirrel(3), 6)
        self.assertEqual(squirrel(0), 1)
        self.assertEqual(squirrel(7), 5)


if __name__ == "__main__":
    unittest.main()
