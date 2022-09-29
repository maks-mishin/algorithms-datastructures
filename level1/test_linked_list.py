import unittest

from tasks.linked_list import LinkedList, Node
from tasks.sum_linked_lists import sum_linked_lists


def make_list_from_linked_list(s_list: LinkedList) -> list:
    result_list = []
    node = s_list.head
    while node is not None:
        result_list.append(node.value)
        node = node.next
    return result_list


class TestLinkedList(unittest.TestCase):
    def test_add_in_tail(self):
        s_list1 = LinkedList()
        s_list1.add_in_tail(Node(12))

    def test_len_list(self):
        s_list = LinkedList()
        self.assertEqual(s_list.len(), 0)

        s_list.add_in_tail(Node(12))
        self.assertEqual(s_list.len(), 1)

        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(12))
        self.assertEqual(s_list.len(), 3)

    def test_clean_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))

        s_list.clean()
        self.assertIsNone(s_list.head)

    def test_find_node_in_empty_list(self):
        s_list = LinkedList()
        self.assertIsNone(s_list.find(55))

    def test_find_node(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))
        self.assertEqual(s_list.find(55).value, 55)

    def test_find_all_nodes(self):
        s_list = LinkedList()
        self.assertEqual(s_list.find_all(12), [])

        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))

        result_list = [
            node.value for node in s_list.find_all(128)
        ]
        self.assertEqual(result_list, [128, 128, 128, 128])

    def test_delete_all_nodes(self):
        s_list = LinkedList()
        s_list.delete(12, all=True)
        self.assertEqual(make_list_from_linked_list(s_list), [])

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

    def test_insert_node(self):
        s_list = LinkedList()
        s_list.insert(None, Node(77))
        self.assertEqual(
            make_list_from_linked_list(s_list),
            [77]
        )

        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.insert(None, Node(77))
        self.assertEqual(
            make_list_from_linked_list(s_list),
            [77, 12]
        )

        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(55))
        s_list.add_in_tail(Node(128))


class TestSumTwoLists(unittest.TestCase):
    def test_sum_equal(self):
        s_list1 = LinkedList()
        s_list2 = LinkedList()

        s_list1.add_in_tail(Node(11))
        s_list1.add_in_tail(Node(14))
        s_list1.add_in_tail(Node(20))

        s_list2.add_in_tail(Node(10))
        s_list2.add_in_tail(Node(34))
        s_list2.add_in_tail(Node(19))

        self.assertEqual(
            make_list_from_linked_list(
                sum_linked_lists(s_list1, s_list2)
            ), [21, 48, 39]
        )

    def test_sum_not_equal(self):
        s_list1 = LinkedList()
        s_list2 = LinkedList()

        s_list1.add_in_tail(Node(11))
        s_list1.add_in_tail(Node(14))
        s_list1.add_in_tail(Node(20))

        s_list2.add_in_tail(Node(10))
        s_list2.add_in_tail(Node(34))

        self.assertEqual(sum_linked_lists(s_list1, s_list2), None)


if __name__ == '__main__':
    unittest.main()
