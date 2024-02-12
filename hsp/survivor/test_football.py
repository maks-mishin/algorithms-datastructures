import unittest

from tasks.football import Football


class TestFootball(unittest.TestCase):
    def test_operation_first(self):
        self.assertTrue(Football([1, 3, 2], 3))
        self.assertTrue(Football([1, 7, 5, 3, 9], 5))

    def test_operation_second(self):
        self.assertTrue(Football([3, 2, 1], 3))
        self.assertTrue(Football([1, 4, 3, 2, 5], 5))

    def test_no_order(self):
        self.assertFalse(Football([9, 5, 3, 7, 1], 5))
        self.assertFalse(Football([1, 2, 3], 3))


if __name__ == '__main__':
    unittest.main()
