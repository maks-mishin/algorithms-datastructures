import unittest

from tasks.shop_olap import ShopOLAP, make_dict


class TestPatternUnlock(unittest.TestCase):
    def test_example(self):
        data = [
            'платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4'
        ]
        res = ['платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2']
        self.assertEqual(ShopOLAP(len(data), data), res)

    def test_same_goods(self):
        data = ['сумка 1', 'сумка 7', 'сумка 14']
        self.assertEqual(ShopOLAP(len(data), data), ['сумка 22'])

    def test_make_dict(self):
        data = [
            'платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4'
        ]
        res = {'платье1': 6, 'сумка32': 2, 'сумка23': 2, 'сумка128': 4}
        self.assertEqual(make_dict(data), res)


if __name__ == "__main__":
    unittest.main()
