import unittest

from bloom_filter import BloomFilter


class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.test_strings = [
            '0123456789', '1234567890', '2345678901',
            '3456789012', '4567890123', '5678901234',
            '6789012345', '7890123456', '8901234567',
            '9012345678'
        ]
        self.filter = BloomFilter(32)

    def test_hash1(self):
        for in_string in self.test_strings:
            self.assertTrue(
                self.filter.hash1(in_string) >= 0 and
                self.filter.hash1(in_string) < self.filter.filter_len
            )

    def test_hash2(self):
        for in_string in self.test_strings:
            self.assertTrue(
                self.filter.hash2(in_string) >= 0 and
                self.filter.hash2(in_string) < self.filter.filter_len
            )

    def test_add(self):
        for in_string in self.test_strings:
            before = self.filter.bit_array
            self.filter.add(in_string)
            self.assertEqual(self.filter.bit_array, before | self.filter.hash1(in_string) | self.filter.hash2(in_string))

    def test_is_value(self):
        for in_string in self.test_strings:
            self.filter.add(in_string)
            self.assertTrue(
                self.filter.is_value(in_string)
            )


if __name__ == '__main__':
    unittest.main()
