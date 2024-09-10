import unittest

from queue import Queue


class TestQueue(unittest.TestCase):
    def test_constructor(self):
        qu = Queue()
        self.assertEqual(qu.size(), 0)

    def test_enqueue(self):
        qu = Queue()
        qu.enqueue(16)
        self.assertEqual(qu.size(), 1)
        qu.enqueue(17)
        self.assertEqual(qu.size(), 2)

    def test_dequeue(self):
        qu = Queue()
        qu.enqueue(16)
        qu.enqueue(16)
        qu.dequeue()
        qu.dequeue()
        self.assertEqual(qu.size(), 0)

    def test_size(self):
        qu = Queue()
        for value in range(100):
            qu.enqueue(value)
        self.assertEqual(qu.size(), 100)


if __name__ == '__main__':
    unittest.main()
