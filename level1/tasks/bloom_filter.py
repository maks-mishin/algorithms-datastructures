class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 0

    def hash1(self, in_string):
        index_bit = 0
        for symbol in in_string:
            index_bit = index_bit * 17 + ord(symbol)
        return index_bit % self.filter_len

    def hash2(self, in_string):
        index_bit = 0
        for symbol in in_string:
            index_bit = index_bit * 17 + ord(symbol)
        return index_bit % self.filter_len

    def add(self, in_string):
        self.bit_array |= self.hash1(in_string)
        self.bit_array |= self.hash2(in_string)

    def is_value(self, in_string):
        return (
            self.bit_array & self.hash1(in_string) == self.hash1(in_string) or
            self.bit_array & self.hash2(in_string) == self.hash2(in_string)
        )
