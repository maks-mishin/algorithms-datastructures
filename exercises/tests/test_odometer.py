import unittest

from exercises.odometer import odometer


class TestOdometer(unittest.TestCase):
    def test_odometer(self):
        self.assertEqual(odometer([10, 1]), 10)
        self.assertEqual(odometer([10, 1, 10, 2, 10, 3]), 30)
        self.assertEqual(odometer([10, 1, 20, 2]), 30)
        self.assertEqual(odometer([30, 2, 10, 4]), 80)
        self.assertEqual(odometer([40, 4]), 160)


if __name__ == "__main__":
    unittest.main()
