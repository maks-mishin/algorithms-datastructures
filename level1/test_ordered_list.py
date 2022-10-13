from random import randint
import unittest

from tasks.ordered_list import OrderedList, OrderedListString


class TestOrderedList(unittest.TestCase):
    def test_constructor(self):
        ol = OrderedList(True)
        self.assertTrue(ol.is_ascending())
        self.assertEqual(
            [node.value for node in ol.get_all()], []
        )
        self.assertEqual(ol.len(), 0)

        ol = OrderedList(True)
        self.assertTrue(ol.is_ascending())
        self.assertEqual(
            [node.value for node in ol.get_all()], []
        )
        self.assertEqual(ol.len(), 0)

    def test_compare(self):
        ol = OrderedList(True)
        self.assertEqual(ol.compare(1, 2), -1)
        self.assertEqual(ol.compare(2, 1), 1)
        self.assertEqual(ol.compare(2, 2), 0)

        ol = OrderedList(False)
        self.assertEqual(ol.compare(1, 2), -1)
        self.assertEqual(ol.compare(2, 1), 1)
        self.assertEqual(ol.compare(2, 2), 0)

    def test_add_asc(self):
        ol = OrderedList(True)
        compare_list = []
        for _ in range(1000):
            new_value = randint(0, 999)
            ol.add(new_value)
            compare_list.append(new_value)
        self.assertEqual(
            [node.value for node in ol.get_all()],
            sorted(compare_list)
        )
        self.assertEqual(ol.len(), len(compare_list))

    def test_add_desc(self):
        ol = OrderedList(False)
        compare_list = []
        for _ in range(1000):
            new_value = randint(0, 999)
            ol.add(new_value)
            compare_list.append(new_value)
        self.assertEqual(
            [node.value for node in ol.get_all()],
            list(reversed(sorted(compare_list)))
        )
        self.assertEqual(ol.len(), len(compare_list))

    def test_find_asc(self):
        ol = OrderedList(True)
        ol.add(14)
        self.assertEqual(ol.find(14).value, 14)
        self.assertIsNone(ol.find(15))
        ol.add(18)
        ol.add(17)
        self.assertEqual(ol.find(18).value, 18)

    def test_find_desc(self):
        ol = OrderedList(False)
        ol.add(14)
        self.assertEqual(ol.find(14).value, 14)
        self.assertIsNone(ol.find(15))
        ol.add(18)
        ol.add(17)
        self.assertEqual(ol.find(18).value, 18)

    def test_delete_asc(self):
        ol = OrderedList(True)
        ol.add(14)
        ol.delete(14)
        self.assertEqual(
            ol.get_all(), []
        )
        self.assertEqual(ol.len(), 0)

    def test_delete_desc(self):
        ol = OrderedList(False)
        ol.add(14)
        ol.delete(14)
        self.assertEqual(
            ol.get_all(), []
        )
        self.assertEqual(ol.len(), 0)

    def test_clean(self):
        ol = OrderedList(True)
        ol.add(14)
        ol.add(18)
        ol.clean(True)
        self.assertTrue(ol.is_ascending())
        self.assertEqual(ol.get_all(), [])

        ol.add(14)
        ol.add(18)
        ol.clean(False)
        self.assertFalse(ol.is_ascending())
        self.assertEqual(ol.get_all(), [])


class TestOrderedListString(unittest.TestCase):
    def test_compare(self):
        ol = OrderedListString(True)
        self.assertEqual(
            ol.compare('  123  ', '  ksdlkfkl '), -1
        )


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
