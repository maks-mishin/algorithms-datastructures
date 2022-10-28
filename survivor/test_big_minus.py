import unittest
import random

from tasks.big_minus import BigMinus


class TestBigMinus(unittest.TestCase):
    def test_example(self):
        self.assertEqual(BigMinus('0', '0'), '0')
        self.assertEqual(BigMinus('10', '0'), '10')
        self.assertEqual(BigMinus('3', '7'), '4')
        self.assertEqual(
            BigMinus('10000000000000000', '9999999999999999'), '1'
        )
        self.assertEqual(
            BigMinus('1724612763481263846', '1724612763481263846'), '0'
        )
        self.assertEqual(BigMinus('1234567891', '1'), '1234567890')
        self.assertEqual(BigMinus('1', '1234'), '1233')

    def test_random(self):
        for _ in range(1000):
            num1 = random.randint(0, 10 ** 16)
            num2 = random.randint(0, 10 ** 16)
            result_str = str(abs(num1 - num2))
            self.assertEqual(BigMinus(str(num1), str(num2)), result_str)


if __name__ == '__main__':
    unittest.main()
