import unittest

from tasks.heap import Heap


class TestHeap(unittest.TestCase):
    def test_add(self):
        """Testing add to existing heap"""

        heap = Heap()
        heap.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)
        self.assertTrue(heap.Add(10))
        self.assertListEqual(
            heap.HeapArray,
            [11, 10, 4, 7, 9, 3, 1, 2, 5, 6, 8, None, None, None, None]
        )
        self.assertTrue(heap.Add(5))
        self.assertListEqual(
            heap.HeapArray,
            [11, 10, 5, 7, 9, 4, 1, 2, 5, 6, 8, 3, None, None, None]
        )

    def test_add_to_empty_heap(self):
        """Testing add to empty heap"""

        heap = Heap()
        heap.MakeHeap([], 0)
        self.assertTrue(heap.Add(11))
        self.assertListEqual(heap.HeapArray, [11])

    def test_cannot_add(self):
        """Cannot add if there is no place"""
        
        heap = Heap()
        heap.MakeHeap([], 0)
        self.assertTrue(heap.Add(10))
        self.assertFalse(heap.Add(11))

    def test_make_heap(self):
        """Test creating heap"""
        
        heap = Heap()
        array = [7, 11, 4, 9, 6, 3, 1, 2, 5, 8]
        heap.MakeHeap(array, 3)
        self.assertListEqual(
            heap.HeapArray,
            [11, 9, 4, 7, 8, 3, 1, 2, 5, 6, None, None, None, None, None]
        )

    def test_cannot_make_heap(self):
        """Cannot insert array if it's too big"""
        
        heap = Heap()
        array = list(range(16))
        heap.MakeHeap(array, 3)
        self.assertFalse(heap.HeapArray)

    def test_get_max(self):
        """Test get max value and re-build the heap"""
        
        heap = Heap()
        array = [7, 11, 4, 9, 6, 3, 1, 2, 5, 8]
        heap.MakeHeap(array, 3)
        self.assertEqual(heap.GetMax(), 11)
        self.assertListEqual(
            heap.HeapArray,
            [9, 8, 4, 7, 6, 3, 1, 2, 5, None, None, None, None, None, None]
        )
        self.assertEqual(heap.GetMax(), 9)
        self.assertListEqual(
            heap.HeapArray,
            [8, 7, 4, 5, 6, 3, 1, 2, None, None, None, None, None, None, None]
        )

    def test_get_max_from_empty(self):
        """Test should return -1 from empty heap"""

        heap = Heap()
        self.assertEqual(heap.GetMax(), -1)


if __name__ == '__main__':
    unittest.main()
