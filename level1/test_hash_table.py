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
        value = 'sdjfnskjfdnkjsndf'
        self.assertEqual(hash_table.seek_slot(value), hash_table.hash_fun(value))

    def test_find(self):
        hash_table = HashTable(17, 3)
        self.assertIsNone(hash_table.find('value'))

    def test_put(self):
        hash_table = HashTable(17, 3)
        value = 'sdjfnskjfdnkjsndf'
        self.assertIsNone(hash_table.find(value))
        hash_table.put(value)
        self.assertEqual(hash_table.find(value), hash_table.hash_fun(value))


if __name__ == '__main__':
    unittest.main()
