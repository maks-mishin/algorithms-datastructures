import unittest

from ufo import UFO


class TestUfo(unittest.TestCase):
    def test_example(self):
        self.assertEqual(UFO(2, [1234, 1777], True), [668, 1023])
        self.assertEqual(UFO(2, [1234, 1777], False), [4660, 6007])
        self.assertEqual(UFO(1, [7], True), [7])
        self.assertEqual(UFO(1, [9], False), [9])

if __name__ == '__main__':
    unittest.main()
