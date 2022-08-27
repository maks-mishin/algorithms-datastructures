import unittest

from printing_costs import PrintingCosts


class TestPrintingCosts(unittest.TestCase):
    def test_all_table(self):
        in_string = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        total_cost = 1757
        self.assertEqual(PrintingCosts(in_string), total_cost)

    def test_examples(self):
        data = [
            ['', 0],
            ['         ', 0],
            ['      1  3  !', 51],
            ['№', 23],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(PrintingCosts(dataset[0]), dataset[1])


if __name__ == '__main__':
    unittest.main()
