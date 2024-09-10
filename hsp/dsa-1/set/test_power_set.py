import time
import unittest
from random import randint

from power_set import PowerSet


class TestPowerSet(unittest.TestCase):
    def test_constructor(self):
        power_set = PowerSet()
        self.assertEqual(power_set.size(), 0)
        self.assertEqual(power_set.storage, [])

    def test_put(self):
        power_set = PowerSet()
        power_set.put(123)
        self.assertEqual(power_set.storage, [123])
        self.assertEqual(power_set.size(), 1)
        power_set.put(123)
        self.assertEqual(power_set.storage, [123])
        self.assertEqual(power_set.size(), 1)
        power_set.put(1213)
        self.assertEqual(power_set.storage, [123, 1213])
        self.assertEqual(power_set.size(), 2)

    def test_get(self):
        power_set = PowerSet()
        power_set.put(123)
        self.assertTrue(power_set.get(123))
        self.assertFalse(power_set.get(1234))

    def test_remove(self):
        power_set = PowerSet()
        power_set.put(123)
        power_set.remove(1234)
        self.assertTrue(power_set.get(123))
        self.assertEqual(power_set.size(), 1)
        power_set.remove(123)
        self.assertFalse(power_set.get(123))
        self.assertEqual(power_set.size(), 0)

    def test_intersection(self):
        power_set1, power_set2 = PowerSet(), PowerSet()
        set1, set2 = set(), set()
        self.assertEqual(power_set1.intersection(power_set2).size(), 0)
        
        for _ in range(100):
            random_value = randint(0, 1000)
            power_set1.put(random_value)
            set1.add(random_value)

        for _ in range(100):
            random_value = randint(0, 1000)
            power_set2.put(random_value)
            set2.add(random_value)

        result_set = power_set1.intersection(power_set2)
        self.assertEqual(
            sorted(result_set.storage),
            sorted(list(set1.intersection(set2)))
        )

    def test_union(self):
        power_set1, power_set2 = PowerSet(), PowerSet()
        set1, set2 = set(), set()
        self.assertEqual(power_set1.union(power_set2).size(), 0)
        
        for _ in range(100):
            random_value = randint(0, 1000)
            power_set1.put(random_value)
            set1.add(random_value)

        for _ in range(100):
            random_value = randint(0, 1000)
            power_set2.put(random_value)
            set2.add(random_value)

        result_set = power_set1.union(power_set2)
        self.assertEqual(
            sorted(result_set.storage),
            sorted(list(set1.union(set2)))
        )

    def test_difference(self):
        power_set1, power_set2 = PowerSet(), PowerSet()
        set1, set2 = set(), set()
        self.assertEqual(power_set1.difference(power_set2).size(), 0)
        
        for _ in range(100):
            random_value = randint(0, 1000)
            power_set1.put(random_value)
            set1.add(random_value)

        for _ in range(100):
            random_value = randint(0, 1000)
            power_set2.put(random_value)
            set2.add(random_value)

        result_set = power_set1.difference(power_set2)
        self.assertEqual(
            sorted(result_set.storage),
            sorted(list(set1.difference(set2)))
        )

    def test_issubset(self):
        power_set1, power_set2 = PowerSet(), PowerSet()
        self.assertTrue(power_set1.issubset(power_set2))

        power_set1.put(123)
        power_set1.put(124)
        self.assertTrue(power_set1.issubset(power_set2))
        self.assertFalse(power_set2.issubset(power_set1))

        for i in range(100):
            random_value = randint(0, 1000)
            power_set1.put(random_value)
            if i < 50:
                power_set2.put(random_value)

        self.assertTrue(power_set1.issubset(power_set2))

    def test_speed(self):
        power_set1 = PowerSet()
        start_time = time.time()

        for i in range(0, 50_000):
            power_set1.put(i)
        self.assertLessEqual(time.time() - start_time, 2.0)


if __name__ == '__main__':
    unittest.main()
