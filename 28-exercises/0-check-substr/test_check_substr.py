import unittest

from check_substr import CheckSubstr


class TestCheckSubstr(unittest.TestCase):
    def test_check_substr(self):
        dataset = ['1212', '12114', '1211', '1231233', '000100001000010020003',
            '', '012030000', '12345', '123', '', '1', '123'
        ]
        sub_strings = ['12', '4', '111', '1233', '111', '', '123', '234', '',
            '133', '1', '123'
        ]
        result = [True, True, False, True, False, True, False, True, True, 
            False, True, True
        ]
        for i in range(len(dataset)):
            self.assertEqual(CheckSubstr(dataset[i], sub_strings[i]), result[i])


if __name__ == "__main__":
    unittest.main()
