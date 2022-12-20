import unittest

from tasks.stack import Stack


class TestStack(unittest.TestCase):
    def test_constructor(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        self.assertIsNone(stack.head.value)
        self.assertIsNone(stack.tail)

    def test_push(self):
        stack = Stack()
        stack.push(14)
        self.assertEqual(stack.head.next.value, 14)
        stack.push(16)
        self.assertEqual(stack.size(), 2)

    def test_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())
        stack.push(14)
        self.assertEqual(stack.pop(), 14)
        self.assertEqual(stack.size(), 0)

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        for i in range(1000):
            stack.push(i)
        self.assertEqual(stack.size(), 1000)

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(19)
        self.assertEqual(stack.peek(), 19)
        self.assertEqual(stack.size(), 1)


if __name__ == '__main__':
    unittest.main()
