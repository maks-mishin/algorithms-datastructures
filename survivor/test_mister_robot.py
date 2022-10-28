import unittest

from tasks.mister_robot import MisterRobot


class TestMisterRobot(unittest.TestCase):
    def test_mister_robot(self):
        self.assertEqual(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]), True)
        self.assertEqual(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]), True)
        self.assertEqual(MisterRobot(5, [4, 1, 5, 2, 3]), False)
        self.assertEqual(MisterRobot(5, [1, 4, 3, 2, 5]), False)


if __name__ == "__main__":
    unittest.main()
