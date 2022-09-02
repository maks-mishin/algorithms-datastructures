import unittest

from exercises.conquest_campaign import ConquestCampaign


class TestConquestCampaign(unittest.TestCase):
    def test_conquest_campaign(self):
        self.assertEqual(ConquestCampaign(3, 3, 1, [2, 2]), 3)
        self.assertEqual(ConquestCampaign(3, 4, 2, [2, 2, 3, 4]), 3)
        self.assertEqual(ConquestCampaign(2, 2, 1, [1, 1]), 3)
        self.assertEqual(ConquestCampaign(2, 3, 2, [1, 1, 2, 3]), 2)
        self.assertEqual(ConquestCampaign(2, 3, 6, [1, 1, 1, 2, 1, 3, 2, 1, 2, 2, 2, 3]), 1)


if __name__ == "__main__":
    unittest.main()
