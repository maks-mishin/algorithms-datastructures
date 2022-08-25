import random
import unittest

from sum_of_the import SumOfThe


class TestSumOfThe(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(SumOfThe(7, [10, -50, 100, -25, 90, -35, 90]), 90)
        self.assertEqual(SumOfThe(5, [5, -25, 10, -35, -45]), -45)
        self.assertEqual(SumOfThe(5, [10, -25, -45, -35, 5]), -45)
        self.assertEqual(SumOfThe(3, [3, 1, 2]), 3)

    def test_shuffle_examples_1(self):
        input_data = [10, -50, 100, -25, 90, -35, 90]
        result = 90
        for _ in range(100):
            random.shuffle(input_data)
            self.assertEqual(SumOfThe(len(input_data), input_data), result)

    def test_shuffle_examples_2(self):
        input_data = [5, -25, 10, -35, -45]
        result = -45
        for _ in range(100):
            random.shuffle(input_data)
            self.assertEqual(SumOfThe(len(input_data), input_data), result)

    def test_random_data(self):
        for _ in range(100):
            len_input_data = random.randint(1, 20)

            input_data = random.sample(range(-1000, 1000), len_input_data)
            result = sum(input_data)
            input_data.append(result)

            for _ in range(100):
                random.shuffle(input_data)
                self.assertEqual(SumOfThe(len(input_data), input_data), result)


if __name__ == "__main__":
    unittest.main()
