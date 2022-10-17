import unittest

from tasks.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_constructor(self):
        hash_table = HashTable(17, 3)
        self.assertEqual(hash_table.size, 17)
        self.assertEqual(hash_table.step, 3)
        self.assertEqual(len(hash_table.slots), 17)
        self.assertTrue(all([slot is None for slot in hash_table.slots]))

    def test_hash_fun(self):
        hash_table = HashTable(17, 3)
        test_data = [
            'jfnaksdfnaskhdfnaskdnfalsjnfdlasndfkljansdklfnskndfkj',
            '0000000000000000000000000',
            '98459237645823645862384isudfIUBSDFUBUBSDFUBSDFb',
            '                                '
        ]
        for test_case in test_data:
            self.assertIsInstance(hash_table.hash_fun(test_case), int)
            self.assertGreaterEqual(hash_table.hash_fun(test_case), 0)
            self.assertLess(hash_table.hash_fun(test_case), hash_table.size)

    def test_seek_slot(self):
        hash_table = HashTable(17, 3)
        value = 'aaa'
        for i in range(16):
            hash_table.slots[i] = value
        self.assertEqual(hash_table.seek_slot(value), 16)
        hash_table.slots[16] = value
        self.assertIsNone(hash_table.seek_slot(value + value))

    def test_find(self):
        hash_table = HashTable(17, 3)
        self.assertIsNone(hash_table.find('value'))

    def test_put(self):
        hash_table = HashTable(17, 3)
        value = 'sdjfnskjfdnkjsndf'
        self.assertIsNone(hash_table.find(value))
        hash_table.put(value)
        self.assertEqual(hash_table.find(value), hash_table.hash_fun(value))

    def test_hash_fun_1(self):
        table = HashTable(17, 3)
        self.assertTrue(table.hash_fun("aaa") < table.size)
        self.assertTrue(
            table.hash_fun("aaaagadgadgadgadfgergerge43534525") < table.size)
        self.assertTrue(table.hash_fun(
            "aaaagadgasdgfdg4dgadgadfgergerge43534525") < table.size)
        self.assertTrue(table.hash_fun("534525") < table.size)
        self.assertTrue(table.hash_fun("z") < table.size)
        self.assertTrue(table.hash_fun("b") < table.size)

    def test_seek_slot_1(self):
        table = HashTable(7, 3)
        table.slots[0] = "a"
        table.slots[1] = "a"
        table.slots[2] = "a"
        table.slots[3] = "a"
        # table.slots[4] = "a"
        table.slots[5] = "a"
        table.slots[6] = "a"
        self.assertEqual(table.seek_slot("b"), 4)
        table.slots[4] = "a"
        self.assertEqual(table.seek_slot("b"), None)

        table = HashTable(9, 3)
        table.slots[0] = "a"
        table.slots[2] = "a"
        table.slots[3] = "a"
        table.slots[4] = "a"
        table.slots[5] = "a"
        table.slots[6] = "a"
        table.slots[7] = "a"
        table.slots[8] = "a"
        self.assertEqual(table.seek_slot("b"), 1)

    def test_put_1(self):
        table = HashTable(7, 3)
        for c in "abcdefz":
            self.assertIsNotNone(table.put(c))

        self.assertIsNone(table.put("safasf"))

    def test_find_1(self):
        table = HashTable(7, 3)
        for c in "abcdefz":
            table.put(c)

        self.assertIsNotNone(table.find("z"))
        self.assertIsNone(table.find("zzz"))


if __name__ == '__main__':
    unittest.main()
