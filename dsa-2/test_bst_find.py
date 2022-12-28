import random
import unittest

from tasks.bst_find import BST, BSTFind, BSTNode


class TestBST(unittest.TestCase):
    def test_find_node_by_key(self):
        tree = BST(node=BSTNode(8, 8, None))
        for key in [4, 12, 2, 6, 1, 3, 5, 7, 10, 9, 11, 14, 13, 15]:
            tree.AddKeyValue(key, key)

    def test_add_key_value(self):
        tree1 = BST(node=None)
        tree1.AddKeyValue(8, 8)
        self.assertIsNotNone(tree1.Root)
        self.assertEqual(tree1.Root.NodeKey, 8)
        self.assertEqual(tree1.Root.NodeValue, 8)
        self.assertEqual(tree1.Root.Parent, None)
        tree1.AddKeyValue(4, 4)

    def test_find_min_max(self):
        tree = BST(node=BSTNode(8, 8, None))
        self.assertEqual(tree.FinMinMax(tree.Root, True), 8)
        self.assertEqual(tree.FinMinMax(tree.Root, False), 8)

        for key in [4, 12, 2, 6, 1, 3, 5, 7, 10, 9, 11, 14, 13, 15]:
            tree.AddKeyValue(key, key)

        self.assertEqual(tree.FinMinMax(tree.Root, FindMax=False), 1)
        self.assertEqual(tree.FinMinMax(tree.Root, FindMax=True), 15)
        self.assertEqual(
            tree.FinMinMax(tree.Root.LeftChild, FindMax=False), 1
        )
        self.assertEqual(
            tree.FinMinMax(tree.Root.RightChild, FindMax=True), 15
        )

    def test_delete_node_by_key(self):
        pass

    def test_count(self):
        tree = BST(node=None)
        self.assertEqual(tree.Count(), 0)
        tree = BST(node=BSTNode(8, 8, None))
        self.assertEqual(tree.Count(), 1)
        for key in [4, 12, 2, 6, 1, 3, 5, 7, 10, 9, 11, 14, 13, 15]:
            tree.AddKeyValue(key, key)
        self.assertEqual(tree.Count(), 15)


if __name__ == '__main__':
    unittest.main()