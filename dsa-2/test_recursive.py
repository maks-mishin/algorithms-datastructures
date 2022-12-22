import unittest

from tasks.find_second_max_elem import find_second_largest_elem
from tasks.balanced_parentheses import \
    generate_all_correct_brackets_sequences


class TestFindSecondLargest(unittest.TestCase):
    def test_two_same_max(self):
        self.assertEqual(
            find_second_largest_elem([2, 1, 2, 0, -1]), 2
        )
        self.assertEqual(
            find_second_largest_elem([0, 0, 0, 0]), 0
        )
        self.assertEqual(
            find_second_largest_elem([-1, -1, -1, -9]), -1
        )

    def test_positive(self):
        self.assertEqual(
            find_second_largest_elem([2, 1]), 1
        )
        self.assertEqual(
            find_second_largest_elem([5, 3, 6, 4, 2, 1]), 5
        )

    def test_negative(self):
        self.assertEqual(
            find_second_largest_elem([-5, -3, -6, -4, -2, -1]), -2
        )
        self.assertEqual(
            find_second_largest_elem([-1, -2]), -2
        )

    def test_common(self):
        self.assertEqual(
            find_second_largest_elem([1, 0, -1]), 0
        )


class TestGenerateBracketsSequence(unittest.TestCase):
    def test_brackets(self):
        self.assertEqual(
            generate_all_correct_brackets_sequences(1), ['()']
        )
        self.assertEqual(
            generate_all_correct_brackets_sequences(2), ['(())', '()()']
        )
        self.assertEqual(
            generate_all_correct_brackets_sequences(3),
            ['((()))', '(()())', '(())()', '()(())', '()()()']
        )


if __name__ == '__main__':
    unittest.main()
