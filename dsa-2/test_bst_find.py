import random
import unittest

from tasks.bst_find import BST, BSTFind, BSTNode


class TestBST(unittest.TestCase):
    def setUp(self):
        self.node_9 = BSTNode(9, 9, None)

        self.bst = BST(self.node_9)

        self.bst.AddKeyValue(4, 4)
        self.bst.AddKeyValue(3, 3)
        self.bst.AddKeyValue(6, 6)
        self.bst.AddKeyValue(5, 5)
        self.bst.AddKeyValue(7, 7)
        self.bst.AddKeyValue(17, 17)
        self.bst.AddKeyValue(22, 22)
        self.bst.AddKeyValue(20, 20)

    def test_add(self):
        self.assertTrue(self.bst.AddKeyValue(30, 30))
        self.assertFalse(self.bst.AddKeyValue(4, 4))
        self.assertFalse(self.bst.AddKeyValue(3, 3))
        self.assertFalse(self.bst.AddKeyValue(6, 6))
        self.assertFalse(self.bst.AddKeyValue(5, 5))
        self.assertFalse(self.bst.AddKeyValue(7, 7))
        self.assertFalse(self.bst.AddKeyValue(17, 17))
        self.assertFalse(self.bst.AddKeyValue(22, 22))
        self.assertFalse(self.bst.AddKeyValue(20, 20))

    def test_find(self):
        # check field "Node"
        self.assertIsNotNone(self.bst.FindNodeByKey(1).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(2).Node)
        self.assertEqual(3, self.bst.FindNodeByKey(1).Node.NodeKey)
        self.assertEqual(3, self.bst.FindNodeByKey(2).Node.NodeKey)

        self.assertEqual(7, self.bst.FindNodeByKey(8).Node.NodeKey)
        self.assertEqual(20, self.bst.FindNodeByKey(21).Node.NodeKey)

        self.assertIsNotNone(self.bst.FindNodeByKey(9).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(4).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(3).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(6).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(5).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(7).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(17).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(22).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(20).Node)

        # check field "NodeHasKey"
        self.assertTrue(self.bst.FindNodeByKey(9).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(4).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(3).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(6).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(5).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(7).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(17).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(22).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(20).NodeHasKey)

        self.assertFalse(self.bst.FindNodeByKey(1).NodeHasKey)
        self.assertFalse(self.bst.FindNodeByKey(2).NodeHasKey)
        self.assertFalse(self.bst.FindNodeByKey(25).NodeHasKey)
        self.assertFalse(self.bst.FindNodeByKey(8).NodeHasKey)

        # check field "ToLeft"
        self.assertFalse(self.bst.FindNodeByKey(9).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(4).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(3).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(6).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(5).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(7).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(17).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(22).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(20).ToLeft)

        self.assertTrue(self.bst.FindNodeByKey(1).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(50).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(8).ToLeft)
        self.assertTrue(self.bst.FindNodeByKey(2).ToLeft)
        self.assertTrue(self.bst.FindNodeByKey(19).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(21).ToLeft)

    def test_find1(self):
        bst = BST(None)
        self.assertTrue(bst.AddKeyValue(1, 1))
        self.assertTrue(bst.AddKeyValue(2, 2))
        self.assertTrue(bst.AddKeyValue(3, 3))

        self.assertEqual(1, bst.FindNodeByKey(1).Node.NodeKey)
        self.assertEqual(2, bst.FindNodeByKey(1).Node.RightChild.NodeKey)
        self.assertIsNone(bst.FindNodeByKey(1).Node.LeftChild)
        self.assertEqual(1, bst.Root.NodeKey)
        self.assertEqual(2, bst.FindNodeByKey(2).Node.NodeKey)
        self.assertEqual(3, bst.FindNodeByKey(2).Node.RightChild.NodeKey)
        self.assertEqual(3, bst.FindNodeByKey(3).Node.NodeKey)

        self.assertTrue(bst.AddKeyValue(100, 100))
        self.assertTrue(bst.AddKeyValue(50, 50))

        self.assertEqual(100, bst.FindNodeByKey(3).Node.RightChild.NodeKey)
        self.assertEqual(50, bst.FindNodeByKey(100).Node.LeftChild.NodeKey)

        self.assertFalse(bst.AddKeyValue(100, 100))
        self.assertIsNone(bst.FindNodeByKey(50).Node.RightChild)

    def test_find2(self):
        random_list = [i for i in range(100)]
        random.shuffle(random_list)

        bst = BST(None)

        for i in random_list:
            bst.AddKeyValue(i, i)

        for i in random_list:
            self.assertTrue(i == bst.FindNodeByKey(i).Node.NodeKey)
            self.assertTrue(bst.FindNodeByKey(i).NodeHasKey)

        bst = BST(None)

        random_list = [30, 6, 12, 27, 3, 9, 21, 24, 15, 18]
        for i in random_list:
            bst.AddKeyValue(i, i)

        check_list = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23,
                      25, 26]

        for i in check_list:
            self.assertFalse(bst.FindNodeByKey(i).NodeHasKey)

        self.assertEqual(3, bst.FindNodeByKey(1).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(1).ToLeft)

        self.assertEqual(3, bst.FindNodeByKey(2).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(2).ToLeft)

        self.assertEqual(3, bst.FindNodeByKey(4).Node.NodeKey)
        self.assertFalse(bst.FindNodeByKey(4).ToLeft)

        self.assertEqual(3, bst.FindNodeByKey(5).Node.NodeKey)
        self.assertFalse(bst.FindNodeByKey(5).ToLeft)

        self.assertEqual(9, bst.FindNodeByKey(7).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(7).ToLeft)

        self.assertEqual(9, bst.FindNodeByKey(8).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(8).ToLeft)

        self.assertEqual(9, bst.FindNodeByKey(10).Node.NodeKey)
        self.assertFalse(bst.FindNodeByKey(10).ToLeft)

        self.assertEqual(9, bst.FindNodeByKey(11).Node.NodeKey)
        self.assertFalse(bst.FindNodeByKey(11).ToLeft)

        self.assertEqual(15, bst.FindNodeByKey(13).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(13).ToLeft)

        self.assertEqual(15, bst.FindNodeByKey(14).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(14).ToLeft)

        self.assertEqual(18, bst.FindNodeByKey(16).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(16).ToLeft)

        self.assertEqual(18, bst.FindNodeByKey(17).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(17).ToLeft)

        self.assertEqual(18, bst.FindNodeByKey(19).Node.NodeKey)
        self.assertFalse(bst.FindNodeByKey(19).ToLeft)

        self.assertEqual(18, bst.FindNodeByKey(20).Node.NodeKey)
        self.assertFalse(bst.FindNodeByKey(20).ToLeft)

        self.assertEqual(24, bst.FindNodeByKey(22).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(22).ToLeft)

        self.assertEqual(24, bst.FindNodeByKey(23).Node.NodeKey)
        self.assertTrue(bst.FindNodeByKey(23).ToLeft)

        self.assertEqual(24, bst.FindNodeByKey(25).Node.NodeKey)
        self.assertFalse(bst.FindNodeByKey(25).ToLeft)

        self.assertEqual(24, bst.FindNodeByKey(26).Node.NodeKey)
        self.assertFalse(bst.FindNodeByKey(26).ToLeft)

    def test_minmax(self):
        # Max from Root
        self.assertEqual(22, self.bst.FinMinMax(self.bst.Root, True).NodeValue)
        # Min from Root
        self.assertEqual(3, self.bst.FinMinMax(self.bst.Root, False).NodeValue)

        # Max from subtree (NodeKey = 17)
        self.assertEqual(22,
                         self.bst.FinMinMax(self.bst.FindNodeByKey(17).Node,
                                            True).NodeValue)
        # Min from subtree (NodeKey = 4)
        self.assertEqual(3, self.bst.FinMinMax(self.bst.FindNodeByKey(4).Node,
                                               False).NodeValue)

    def test_delete(self):
        self.assertEqual(9, self.bst.Count())
        self.assertIsNotNone(self.bst.FindNodeByKey(7).Node)
        self.assertTrue(self.bst.DeleteNodeByKey(7))
        self.assertEqual(8, self.bst.Count())

        self.assertFalse(self.bst.DeleteNodeByKey(7))
        self.assertEqual(8, self.bst.Count())

        self.assertTrue(self.bst.AddKeyValue(7, 7))
        self.assertEqual(9, self.bst.Count())

        self.assertFalse(self.bst.DeleteNodeByKey(23))

    def test_count(self):
        self.assertEqual(9, self.bst.Count())

    def test_zero_tree(self):
        bst = BST(None)

        self.assertEqual(0, bst.Count())

        self.assertTrue(self.bst.DeleteNodeByKey(9))
        self.assertFalse(self.bst.FindNodeByKey(9).NodeHasKey)
        self.assertEqual(17, self.bst.Root.NodeKey)
        self.assertEqual(8, self.bst.Count())

        self.assertTrue(self.bst.AddKeyValue(9, 9))
        self.assertEqual(9, self.bst.Count())

        self.assertTrue(self.bst.FindNodeByKey(5).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(9))
        self.assertFalse(self.bst.FindNodeByKey(9).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(4))
        self.assertFalse(self.bst.FindNodeByKey(4).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(3))
        self.assertFalse(self.bst.FindNodeByKey(3).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(6))
        self.assertFalse(self.bst.FindNodeByKey(6).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(5))
        self.assertFalse(self.bst.FindNodeByKey(5).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(7))
        self.assertFalse(self.bst.FindNodeByKey(7).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(17))
        self.assertFalse(self.bst.FindNodeByKey(17).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(22))
        self.assertFalse(self.bst.FindNodeByKey(22).NodeHasKey)

        self.assertTrue(self.bst.DeleteNodeByKey(20))
        self.assertFalse(self.bst.FindNodeByKey(20).NodeHasKey)

        self.assertEqual(0, self.bst.Count())


if __name__ == '__main__':
    unittest.main()
