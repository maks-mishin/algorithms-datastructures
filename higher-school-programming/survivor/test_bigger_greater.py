import unittest

from tasks.bigger_greater import BiggerGreater


class TestBiggerGreater(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(BiggerGreater('ая'), 'яа')
        self.assertEqual(BiggerGreater('нклм'), 'нкмл')
        self.assertEqual(BiggerGreater('вибк'), 'викб')
        self.assertEqual(BiggerGreater('вкиб'), 'ибвк')

    def test_empty(self):
        self.assertEqual(BiggerGreater(''), '')

    def test_same_chars(self):
        self.assertEqual(BiggerGreater('ffffffff'), '')

    def test_already_magic(self):
        self.assertEqual(BiggerGreater('za'), '')


if __name__ == '__main__':
    unittest.main()
