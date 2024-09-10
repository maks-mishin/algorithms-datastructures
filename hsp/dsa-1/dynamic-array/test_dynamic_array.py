import unittest

from dynamic_array import DynArray


class TestDynamicArray(unittest.TestCase):
    def test_constructor(self):
        da = DynArray()
        self.assertEqual(da.count, 0)
        self.assertEqual(da.min_capacity, 16)
        self.assertEqual(da.capacity, 16)

    def test_resize(self):
        da = DynArray()
        self.assertEqual(da.capacity, 16)
        da.resize(89)
        self.assertEqual(da.capacity, 89)

    def test_get_item(self):
        da = DynArray()
        try:
            item = da[0]
        except IndexError as ex:
            self.assertEqual(str(ex), 'Index is out of bounds')

        da.append(1)
        self.assertEqual(da[0], 1)

        try:
            item = da[-1]
        except IndexError as ex:
            self.assertEqual(str(ex), 'Index is out of bounds')

        try:
            item = da[len(da) + 1]
        except IndexError as ex:
            self.assertEqual(str(ex), 'Index is out of bounds')

    def test_len(self):
        da = DynArray()
        self.assertEqual(len(da), 0)
        da.append(1)
        self.assertEqual(len(da), 1)

    def test_append(self):
        da = DynArray()
        da.append(9)
        self.assertEqual(da[0], 9)
        self.assertEqual(len(da), 1)

    def test_insert_not_full_buffer(self):
        da = DynArray()
        inserted_position = 0
        inserted_value = 5
        da.insert(inserted_position, inserted_value)

        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 1)
        self.assertEqual(len(da), 1)
        self.assertEqual(da[inserted_position], inserted_value)

    def test_insert_overflow_buffer(self):
        da = DynArray()
        for i in range(16):
            da.append(i)
        self.assertEqual(da.capacity, 16)
        da.insert(0, 90)
        self.assertEqual(da[0], 90)
        self.assertEqual(da.capacity, 32)

    def test_insert_incorrect_position(self):
        da = DynArray()
        try:
            da.insert(9, 18)
        except IndexError as ex:
            self.assertEqual(
                str(ex), 'Index is out of bounds'
            )

    def test_delete_prev_buffer(self):
        da = DynArray()
        da.append(1)
        da.append(9)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(len(da), 2)
        da.delete(0)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(len(da), 1)

    def test_delete_reduce_buffer(self):
        da = DynArray()
        self.assertEqual(da.capacity, 16)
        for i in range(17):
            da.append(i)
        self.assertEqual(len(da), 17)
        self.assertEqual(da.capacity, 32)
        da.delete(0)
        self.assertEqual(len(da), 16)
        self.assertEqual(da.capacity, 32)
        da.delete(0)
        self.assertEqual(len(da), 15)
        self.assertEqual(da.capacity, 21)

    def test_delete_incorrect_position(self):
        da = DynArray()
        try:
            da.delete(-1)
        except IndexError as ex:
            self.assertEqual(str(ex), 'Index is out of bounds')


if __name__ == '__main__':
    unittest.main()
