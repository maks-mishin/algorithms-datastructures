import unittest

from simple_tree import SimpleTreeNode, SimpleTree


class TestSimpleTree(unittest.TestCase):
    def setUp(self) -> None:
        self.root = SimpleTreeNode(9, None)
        self.tree = SimpleTree(self.root)

        self.node_4 = SimpleTreeNode(4, None)
        self.node_3 = SimpleTreeNode(3, None)
        self.node_6 = SimpleTreeNode(6, None)
        self.node_5 = SimpleTreeNode(5, None)
        self.node_7 = SimpleTreeNode(7, None)
        self.tree.AddChild(self.root, self.node_4)
        self.tree.AddChild(self.node_4, self.node_3)
        self.tree.AddChild(self.node_4, self.node_6)
        self.tree.AddChild(self.node_6, self.node_5)
        self.tree.AddChild(self.node_6, self.node_7)

        self.node_17 = SimpleTreeNode(17, None)
        self.node_22 = SimpleTreeNode(22, None)
        self.node_20 = SimpleTreeNode(20, None)
        self.tree.AddChild(self.root, self.node_17)
        self.tree.AddChild(self.node_17, self.node_22)
        self.tree.AddChild(self.node_22, self.node_20)

    def test_constructor(self):
        tree = SimpleTree(root=None)
        self.assertIsNone(tree.Root)
        self.assertEqual(
            tree.Count(), 0
        )
        self.assertEqual(
            tree.LeafCount(), 0
        )
        self.assertEqual(
            tree.FindNodesByValue(12), []
        )
        self.assertEqual(
            tree.GetAllNodes(), []
        )
        tree = SimpleTree(root=SimpleTreeNode(12, None))
        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.LeafCount(), 1)

    def test_add_child(self):
        root_node = SimpleTreeNode(0, None)
        tree = SimpleTree(root=root_node)
        add_node = SimpleTreeNode(12, root_node)
        tree.AddChild(root_node, add_node)
        self.assertEqual(tree.Count(), 2)
        self.assertEqual(tree.LeafCount(), 1)
        self.assertIn(add_node, root_node.Children)
        self.assertEqual(add_node.Parent, root_node)
        self.assertEqual(add_node.Level, root_node.Level + 1)

    def test_delete_node(self):
        self.tree.DeleteNode(self.node_4)
        self.assertNotIn(
            self.node_4, self.tree.Root.Children
        )

    def test_get_all_nodes(self):
        all_nodes = self.tree.GetAllNodes()
        self.assertIn(self.node_4, all_nodes)

    def test_find_nodes_by_value(self):
        node_4 = SimpleTreeNode(4, None)
        tree = SimpleTree(root=node_4)
        nodes = tree.FindNodesByValue(4)
        self.assertIn(node_4, nodes)


    def test_move_node(self):
        self.assertNotIn(self.node_6, self.tree.Root.Children)
        self.tree.MoveNode(self.node_6, self.root)
        self.assertIn(self.node_6, self.tree.Root.Children)
        self.assertEqual(self.tree.LeafCount(), 4)
        self.assertEqual(self.tree.Count(), 9)

    def test_count_nodes(self):
        self.assertEqual(self.tree.Count(), 9)

    def test_count_leaves(self):
        self.assertEqual(self.tree.LeafCount(), 4)


if __name__ == '__main__':
    unittest.main()
