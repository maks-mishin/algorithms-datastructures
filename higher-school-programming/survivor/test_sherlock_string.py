import unittest

from tasks.sherlock_valid_string import SherlockValidString,\
    calc_chars_frequency, check_password_valid


class TestSherlockString(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(SherlockValidString('ab'), True)
        self.assertEqual(SherlockValidString('xzy'), True)
        self.assertEqual(SherlockValidString('xyza'), True)
        self.assertEqual(SherlockValidString('xyzaa'), True)
        self.assertEqual(SherlockValidString('xyzaaa'), False)
        self.assertEqual(SherlockValidString('xxyyaaa'), True)
        self.assertEqual(SherlockValidString('xxyya'), True)

    def test_invalid_string(self):
        self.assertEqual(SherlockValidString('xyzxaaa'), False)
        self.assertEqual(SherlockValidString('xxyyyaaa'), False)
        self.assertEqual(SherlockValidString('xxyyzabc'), False)
        self.assertEqual(SherlockValidString('xxyyza'), False)
        self.assertEqual(SherlockValidString('xyzzzzz'), False)

    def test_make_dict(self):
        self.assertEqual(calc_chars_frequency('xyzaa'), {
            'x': 1, 'y': 1, 'z': 1, 'a': 2
        })

    def test_check_password(self):
        self.assertEqual(check_password_valid([2, 2, 2]), True)
        self.assertEqual(check_password_valid([2, 2, 1]), False)


if __name__ == '__main__':
    unittest.main()