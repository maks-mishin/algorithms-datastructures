# Source: https://contest.yandex.ru/contest/26365/problems/B/

import unittest


def zipper(n: int, nums_arr1: str, nums_arr2: str) -> str:
    list_1 = list(map(int, nums_arr1.split()))
    list_2 = list(map(int, nums_arr2.split()))
    result_arr = []
    for i in range(n):
        result_arr.append(list_1[i])
        result_arr.append(list_2[i])
    return ' '.join(map(str, result_arr))


class TestZipper(unittest.TestCase):
    def test_zipper(self):
        self.assertEqual(zipper(3, '1 2 3', '4 5 6'), '1 4 2 5 3 6')
        self.assertEqual(zipper(1, '1', '2'), '1 2')
        self.assertEqual(zipper(3, '1 8 9', '2 3 1'), '1 2 8 3 9 1')

if __name__ == "__main__":
    unittest.main()
