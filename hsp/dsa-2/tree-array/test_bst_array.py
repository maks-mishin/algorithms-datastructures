import unittest

from bst_array import aBST


class TestABST(unittest.TestCase):
    def test_constructor(self):
        test_sizes_tree = [0, 1, 3, 7, 15, 31]
        test_depths = [-1, 0, 1, 2, 3, 4]
        for depth, size in zip(test_depths, test_sizes_tree):
            tree = aBST(depth)
            self.assertEqual(
                len(tree.Tree), size
            )

    def test_find_key_index(self):
        tree = aBST(1)
        tree.Tree = [1]
        self.assertEqual(tree.FindKeyIndex(1), 0)
        self.assertIsNone(tree.FindKeyIndex(2))
        tree = aBST(2)
        self.assertEqual(tree.FindKeyIndex(8), 0)
        tree.Tree = [8, None, None]
        self.assertEqual(tree.FindKeyIndex(4), -1)
        self.assertEqual(tree.FindKeyIndex(12), -2)

    def test_add_key(self):
        tree = aBST(4)
        for key in [8, 4, 12, 2, 6, 1, 3, 5, 7, 10, 9, 11, 14, 13, 15]:
            tree.AddKey(key)
            self.assertIn(key, tree.Tree)


if __name__ == '__main__':
    unittest.main()