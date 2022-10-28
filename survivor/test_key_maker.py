import unittest

from tasks.key_maker import Keymaker, keymaker_math
from tasks.key_maker import verify_keymaker, toggle_door


class TestKeymaker(unittest.TestCase):
    def test_keymaker(self):
        self.assertEqual(Keymaker(5), '10010')
        self.assertEqual(Keymaker(10), '1001000010')

    def test_keymaker_math(self):
        self.assertEqual(keymaker_math(5), '10010')
        self.assertEqual(keymaker_math(10), '1001000010')

    def test_verify_keymaker(self):
        self.assertTrue(verify_keymaker(5))
        self.assertTrue(verify_keymaker(50))

    def test_toggle_door(self):
        self.assertEqual(toggle_door('1'), '0')
        self.assertEqual(toggle_door('0'), '1')


if __name__ == '__main__':
    unittest.main()
