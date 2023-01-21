import unittest

from tasks.bidirect_list_dummy_nodes import Node, DoublyLinkedList


def make_list_from_linked_list(s_list: DoublyLinkedList):
    result_list = []
    node = s_list.head.next
    while node.Value is not None:
        result_list.append(node.Value)
        node = node.next
    return result_list


class TestLinkedListDummy(unittest.TestCase):
    def test_constructor(self):
        s_list = DoublyLinkedList()
        self.assertEqual(s_list.len(), 0)
        self.assertIsNone(s_list.head.Value)
        self.assertIsNone(s_list.tail.Value)
        self.assertIsNone(s_list.head.prev)
        self.assertIsNone(s_list.tail.next)
        self.assertTrue(s_list.head.next == s_list.tail)
        self.assertTrue(s_list.tail.prev == s_list.head)

    def test_add_in_tail(self):
        s_list = DoublyLinkedList()
        s_list.add_in_tail(Node(15))
        self.assertEqual(s_list.len(), 1)
        self.assertEqual(s_list.head.next.Value, 15)
        self.assertEqual(s_list.tail.prev.Value, 15)

        s_list.add_in_tail(Node(29))
        self.assertEqual(s_list.len(), 2)
        self.assertEqual(s_list.head.next.Value, 15)
        self.assertEqual(s_list.tail.prev.Value, 29)

    def test_add_in_head(self):
        s_list = DoublyLinkedList()
        s_list.add_in_head(Node(15))
        self.assertEqual(s_list.len(), 1)
        self.assertEqual(s_list.head.next.Value, 15)
        self.assertEqual(s_list.tail.prev.Value, 15)

        s_list.add_in_head(Node(29))
        self.assertEqual(s_list.len(), 2)
        self.assertEqual(s_list.head.next.Value, 29)
        self.assertEqual(s_list.tail.prev.Value, 15)

    def test_len_list(self):
        s_list = DoublyLinkedList()
        self.assertEqual(s_list.len(), 0)

        s_list.add_in_head(Node(12))
        s_list.add_in_tail(Node(14))
        self.assertEqual(s_list.len(), 2)

        s_list.delete(14)
        self.assertEqual(s_list.len(), 1)

    def test_clean_linked_list(self):
        s_list = DoublyLinkedList()
        s_list.add_in_head(Node(12))
        s_list.add_in_tail(Node(14))
        s_list.clean()
        self.assertIsNone(s_list.head.Value)
        self.assertIsNone(s_list.tail.Value)
        self.assertEqual(s_list.len(), 0)

    def test_find_one_node(self):
        s_list = DoublyLinkedList()
        self.assertIsNone(s_list.find(Node(15)))
        s_list.add_in_tail(Node(14))
        s_list.add_in_tail(Node(15))
        s_list.add_in_tail(Node(14))
        self.assertEqual(s_list.find(14).Value, 14)

    def test_find_all_nodes(self):
        s_list = DoublyLinkedList()
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

    def test_delete_one(self):
        s_list = DoublyLinkedList()
        s_list.add_in_tail(Node(14))
        s_list.delete(14)
        self.assertEqual(s_list.len(), 0)
        self.assertIsNone(s_list.head.next.Value)
        self.assertIsNone(s_list.tail.prev.Value)
        self.assertEqual(
            make_list_from_linked_list(s_list), []
        )

        s_list = DoublyLinkedList()
        s_list.add_in_tail(Node(14))
        s_list.add_in_tail(Node(18))
        s_list.delete(18)
        self.assertEqual(s_list.len(), 1)
        self.assertEqual(s_list.head.next.Value, 14)
        self.assertEqual(s_list.tail.prev.Value, 14)
        self.assertEqual(
            make_list_from_linked_list(s_list), [14]
        )

        s_list = DoublyLinkedList()
        s_list.add_in_tail(Node(18))
        s_list.add_in_head(Node(16))
        s_list.delete(16)
        self.assertEqual(s_list.len(), 1)
        self.assertEqual(s_list.head.next.Value, 18)
        self.assertEqual(s_list.tail.prev.Value, 18)
        self.assertEqual(
            make_list_from_linked_list(s_list), [18]
        )

    def test_delete_all(self):
        s_list = DoublyLinkedList()
        s_list.add_in_tail(Node(14))
        s_list.add_in_tail(Node(14))
        s_list.add_in_tail(Node(14))
        s_list.add_in_tail(Node(14))
        s_list.delete(14, all=True)
        self.assertEqual(
            make_list_from_linked_list(s_list), []
        )
        self.assertEqual(s_list.len(), 0)

    def test_insert(self):
        s_list = DoublyLinkedList()
        s_list.insert(None, Node(89))
        self.assertEqual(
            make_list_from_linked_list(s_list), [89]
        )
        s_list.insert(Node(89), Node(18))
        self.assertEqual(
            make_list_from_linked_list(s_list), [89, 18]
        )
        s_list.insert(None, Node(16))
        self.assertEqual(
            make_list_from_linked_list(s_list), [89, 18, 16]
        )


if __name__ == '__main__':
    unittest.main()
