import unittest
from random import shuffle

from generate_bbst_array import GenerateBBSTArray


class TestGenerateBBSTArray(unittest.TestCase):
    def test_empty_array(self):
        test_list = []
        balanced_list = GenerateBBSTArray(test_list)
        self.assertIsNone(balanced_list)

    def test_get_balanced_array_depth_0(self):
        test_list = list(range(1, 2))
        balanced_list = GenerateBBSTArray(test_list)
        self.assertListEqual(balanced_list, [1])

    def test_get_balanced_array_depth_1(self):
        test_list = list(range(1, 4))
        shuffle(test_list)
        balanced_list = GenerateBBSTArray(test_list)
        self.assertListEqual(balanced_list, [2, 1, 3])

    def test_get_balanced_array_depth_2(self):
        test_list = list(range(1, 8))
        shuffle(test_list)
        balanced_list = GenerateBBSTArray(test_list)
        self.assertListEqual(balanced_list, [4, 2, 6, 1, 3, 5, 7])

    def test_get_balanced_array_depth_3(self):
        test_list = list(range(1, 16))
        shuffle(test_list)
        balanced_list = GenerateBBSTArray(test_list)
        self.assertListEqual(
            balanced_list,
            [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    )

    def test_get_balanced_array_depth_4(self):
        test_list = list(range(1, 32))
        shuffle(test_list)
        balanced_list = GenerateBBSTArray(test_list)
        self.assertListEqual(
            balanced_list,
            [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30,
             1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
        )


if __name__ == '__main__':
    unittest.main()
