import unittest

from exercises.synchronizing_tables import SynchronizingTables


class TestConquestCampaign(unittest.TestCase):
    def test_example(self):
        result = SynchronizingTables(3, [50, 1, 1024], [20000, 100000, 90000])
        self.assertEqual(result, [90000, 20000, 100000])
    
    def test_one_element(self):
        self.assertEqual(SynchronizingTables(1, [300], [1000]), [1000])


if __name__ == "__main__":
    unittest.main()
