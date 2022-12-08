import unittest

from tasks.deque import Node, Deque


def check_elem_in_deque(deq: Deque, val) -> bool:
    node = deq.head.next
    while isinstance(node, Node):
        if node.value == val:
            return True
        node = node.next
    return False


def make_list_from_deq(deq: Deque) -> list:
    result_list = []
    node = deq.head.next
    while isinstance(node, Node):
        result_list.append(node.value)
        node = node.next
    result_list.pop()
    return result_list


class TestDeque(unittest.TestCase):
    def test_add_front(self):
        deq = Deque()
        deq.addFront(15)
        self.assertEqual(deq.size(), 1)
        self.assertTrue(check_elem_in_deque(deq, 15))
        self.assertEqual(
            make_list_from_deq(deq), [15]
        )

        deq.addFront(17)
        self.assertEqual(deq.size(), 2)
        self.assertTrue(check_elem_in_deque(deq, 17))
        self.assertEqual(
            make_list_from_deq(deq), [17, 15]
        )

    def test_add_tail(self):
        deq = Deque()
        deq.addTail(15)
        self.assertEqual(deq.size(), 1)
        self.assertTrue(check_elem_in_deque(deq, 15))
        self.assertEqual(
            make_list_from_deq(deq), [15]
        )

        deq.addTail(17)
        self.assertEqual(deq.size(), 2)
        self.assertTrue(check_elem_in_deque(deq, 17))
        self.assertEqual(
            make_list_from_deq(deq), [15, 17]
        )

    def test_remove_front(self):
        deq = Deque()
        deq.addFront(15)
        deq.addFront(18)
        deq.removeFront()
        self.assertEqual(deq.size(), 1)
        self.assertFalse(check_elem_in_deque(deq, 18))

        deq.removeFront()
        self.assertEqual(deq.size(), 0)
        self.assertFalse(check_elem_in_deque(deq, 15))

    def test_remove_tail(self):
        deq = Deque()
        deq.addTail(15)
        deq.addTail(18)
        deq.removeTail()
        self.assertEqual(deq.size(), 1)
        self.assertFalse(check_elem_in_deque(deq, 18))

        deq.removeTail()
        self.assertEqual(deq.size(), 0)
        self.assertFalse(check_elem_in_deque(deq, 15))


if __name__ == '__main__':
    unittest.main()
