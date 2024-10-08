import unittest

from bidirect_linked_list import Node, LinkedList2
from test_linked_list import make_list_from_linked_list


class TestBidirectList(unittest.TestCase):
    def test_node(self):
        n1 = Node(14)
        self.assertEqual(n1.Value, 14)
        self.assertIsNone(n1.prev)
        self.assertIsNone(n1.next)

    def test_constructor(self):
        s_list = LinkedList2()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.assertEqual(s_list.len(), 0)

    def test_add_in_tail(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(14))
        self.assertEqual(s_list.head.Value, 14)
        self.assertEqual(s_list.tail.Value, 14)
        self.assertEqual(s_list.len(), 1)
        self.assertEqual(
            make_list_from_linked_list(s_list), [14]
        )

        s_list.add_in_tail(Node(16))
        s_list.add_in_tail(Node(10))
        self.assertEqual(s_list.head.Value, 14)
        self.assertEqual(s_list.tail.Value, 10)
        self.assertEqual(s_list.len(), 3)
        self.assertEqual(
            make_list_from_linked_list(s_list), [14, 16, 10]
        )

    def test_add_in_head(self):
        s_list = LinkedList2()
        s_list.add_in_head(Node(14))
        self.assertEqual(s_list.head.Value, 14)
        self.assertEqual(s_list.tail.Value, 14)
        self.assertEqual(s_list.len(), 1)
        self.assertEqual(
            make_list_from_linked_list(s_list), [14]
        )

        s_list.add_in_head(Node(16))
        s_list.add_in_head(Node(10))
        self.assertEqual(s_list.head.Value, 10)
        self.assertEqual(s_list.tail.Value, 14)
        self.assertEqual(s_list.len(), 3)
        self.assertEqual(
            make_list_from_linked_list(s_list), [10, 16, 14]
        )

    def test_len_list(self):
        s_list = LinkedList2()
        self.assertEqual(s_list.len(), 0)

        s_list.add_in_head(Node(12))
        s_list.add_in_tail(Node(14))
        self.assertEqual(s_list.len(), 2)

        s_list.delete(14)
        self.assertEqual(s_list.len(), 1)

    def test_clean_linked_list(self):
        s_list = LinkedList2()
        s_list.add_in_head(Node(12))
        s_list.add_in_tail(Node(14))
        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.assertEqual(s_list.len(), 0)

    def test_find_one_node(self):
        s_list = LinkedList2()
        self.assertIsNone(s_list.find(Node(15)))
        s_list.add_in_tail(Node(14))
        s_list.add_in_tail(Node(15))
        s_list.add_in_tail(Node(14))
        self.assertEqual(s_list.find(14).Value, 14)

    def test_find_all_nodes(self):
        s_list = LinkedList2()
        self.assertEqual(s_list.find_all(12), [])

        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))

        result_list = [
            node.Value for node in s_list.find_all(128)
        ]
        self.assertEqual(result_list, [128, 128, 128, 128])

    def test_delete_empty_list(self):
        s_list = LinkedList2()
        s_list.delete(14)
        self.assertEqual(
            make_list_from_linked_list(s_list), []
        )
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_delete_one(self):
        s_list = LinkedList2()

        s_list.add_in_tail(Node(14))
        s_list.delete(14)
        self.assertEqual(
            make_list_from_linked_list(s_list), []
        )
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_delete_one_from_two(self):
        s_list = LinkedList2()
        first, second = 12, 14
        s_list.insert(None, Node(first))
        s_list.add_in_head(Node(second))
        s_list.delete(first, all=False)
        self.assertEqual(
            make_list_from_linked_list(s_list), [second]
        )
        self.assertEqual(s_list.head.Value, second)
        self.assertEqual(s_list.tail.Value, second)

        s_list = LinkedList2()
        first, second = 12, 14
        s_list.insert(None, Node(first))
        s_list.insert(None, Node(second))
        s_list.delete(second, all=False)
        self.assertEqual(
            make_list_from_linked_list(s_list), [first]
        )
        self.assertEqual(s_list.head.Value, first)
        self.assertEqual(s_list.tail.Value, first)

    def test_delete_all_nodes(self):
        s_list = LinkedList2()
        s_list.delete(12, all=True)
        self.assertEqual(make_list_from_linked_list(s_list), [])
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))
        s_list.delete(55, all=True)
        self.assertEqual(
            make_list_from_linked_list(s_list),
            [12, 128, 128, 128]
        )
        self.assertEqual(s_list.head.Value, 12)
        self.assertEqual(s_list.tail.Value, 128)
        self.assertEqual(s_list.len(), 4)

    def test_insert(self):
        s_list = LinkedList2()
        s_list.insert(None, Node(12))
        self.assertEqual(
            make_list_from_linked_list(s_list), [12]
        )
        self.assertEqual(s_list.head.Value, 12)
        self.assertEqual(s_list.tail.Value, 12)

        s_list.insert(None, Node(14))
        self.assertEqual(
            make_list_from_linked_list(s_list), [12, 14]
        )
        self.assertEqual(s_list.head.Value, 12)
        self.assertEqual(s_list.tail.Value, 14)

        s_list.insert(Node(12), Node(77))
        self.assertEqual(
            make_list_from_linked_list(s_list),
            [12, 77, 14]
        )
        self.assertEqual(s_list.head.Value, 12)
        self.assertEqual(s_list.tail.Value, 14)

        s_list.insert(Node(14), Node(77))
        self.assertEqual(
            make_list_from_linked_list(s_list),
            [12, 77, 14, 77]
        )
        self.assertEqual(s_list.head.Value, 12)
        self.assertEqual(s_list.tail.Value, 77)


if __name__ == '__main__':
    unittest.main()
