import random
import unittest
from string import ascii_letters

from tasks.native_cache import NativeCache


def random_string():
    number = random.randint(3, len(ascii_letters))
    return ''.join(random.sample(ascii_letters, number))


class TestNativeCacheEmptySlots(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_cache = NativeCache(self.size)
        self.key = random_string()
        self.value = random_string()
        self.empty_slots = [None] * self.size
        self.hits = [0] * self.size

    def test_check_native_cache(self):
        self.assertIsInstance(self.s_cache, NativeCache)
        self.assertEqual(len(self.s_cache.slots), self.size)
        self.assertEqual(len(self.s_cache.values), self.size)
        self.assertEqual(len(self.s_cache.hits), self.size)
        self.assertListEqual(self.s_cache.slots, self.empty_slots)
        self.assertListEqual(self.s_cache.values, self.empty_slots)
        self.assertListEqual(self.s_cache.hits, self.hits)
        self.assertFalse(self.s_cache.is_full())
        for index in range(self.size):
            self.assertIsNone(self.s_cache.slots[index])
            self.assertIsNone(self.s_cache.values[index])
            self.assertEqual(self.s_cache.hits[index], 0)

    def test_hash_fun_empty_slots(self):
        hash = self.s_cache.hash_fun(self.key)
        check_hash = sum([ord(sym) for sym in self.key]) % self.size
        self.assertEqual(hash, check_hash)

    def test_is_key_empty_slots(self):
        is_key = self.s_cache.is_key(self.key)
        self.assertFalse(is_key)

    def test_is_full_empty_slots(self):
        self.assertFalse(self.s_cache.is_full())

    def test_put_in_empty_slots(self):
        self.s_cache.put(self.key, self.value)
        self.assertIn(self.key, self.s_cache.slots)
        self.assertIn(self.value, self.s_cache.values)

    def test_get_in_empty_slots(self):
        value = self.s_cache.get_value(self.key)
        self.assertIsNone(value)
        for index in range(self.size):
            self.assertEqual(self.s_cache.hits[index], 0)


class TestNativeCacheFullSlots(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_cache = NativeCache(self.size)
        self.new_key = random_string()
        self.new_value = random_string()
        for _ in range(self.size):
            key = random_string()
            value = random_string()
            self.s_cache.put(key, value)

    def test_check_native_cache_full_slots(self):
        self.assertIsInstance(self.s_cache, NativeCache)
        self.assertEqual(len(self.s_cache.slots), self.size)
        self.assertEqual(len(self.s_cache.values), self.size)
        self.assertEqual(len(self.s_cache.hits), self.size)
        self.assertTrue(self.s_cache.is_full())
        for index in range(self.size):
            self.assertIsNotNone(self.s_cache.slots[index])
            self.assertIsNotNone(self.s_cache.values[index])
            # self.assertEqual(self.s_cache.hits[index], 0)

    def test_hash_fun_full_slots(self):
        hash = self.s_cache.hash_fun(self.new_key)
        check_hash = sum([ord(sym) for sym in self.new_key]) % self.size
        self.assertEqual(hash, check_hash)

    def test_is_key_full_slots(self):
        is_not_key = self.s_cache.is_key(self.new_key)
        self.assertFalse(is_not_key)
        is_key = self.s_cache.is_key(random.choice(self.s_cache.slots))
        self.assertTrue(is_key)

    def test_is_full_full_slots(self):
        self.assertTrue(self.s_cache.is_full())

    def test_put_in_full_slots(self):
        self.s_cache.put(self.new_key, self.new_value)
        self.assertIn(self.new_key, self.s_cache.slots)
        self.assertIn(self.new_value, self.s_cache.values)
        self.assertEqual(len(self.s_cache.slots), self.size)
        self.assertEqual(len(self.s_cache.values), self.size)
        self.assertEqual(len(self.s_cache.hits), self.size)

    def test_get_value_hit_put_in_full_slots(self):
        for i in range(1, 10):
            for index in range(self.size - 1):
                key = self.s_cache.slots[index]
                # проверяем get_hit()
                self.assertEqual(self.s_cache.get_hit(key), i - 1)
                # проверяем get_value()
                value = self.s_cache.get_value(key)
                self.assertIsNotNone(value)
                self.assertIn(value, self.s_cache.values)
            # проверяем, корректно ли учитывается
            # количество обращений к ключам
            for index in range(self.size - 1):
                self.assertEqual(self.s_cache.hits[index], i)
            # к последнему ключу не обращались, поэтому ноль
            self.assertEqual(self.s_cache.hits[-1], 0)
        # проверяем, правильно ли работает схема вытеснения
        self.s_cache.put(self.new_key, self.new_value)
        min_hit = min(self.s_cache.hits)
        index = self.s_cache.hits.index(min_hit)
        self.assertEqual(min_hit, self.s_cache.hits[-1])
        self.assertEqual(self.new_key, self.s_cache.slots[index])
        self.assertEqual(self.new_value, self.s_cache.values[index])
        self.assertEqual(self.s_cache.hits[index], 0)


if __name__ == '__main__':
    unittest.main()
