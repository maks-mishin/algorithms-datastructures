class BigInteger:
    def __init__(self, in_string: str) -> None:
        self.digits = []
        for i in range(len(in_string) - 1, -1, -1):
            self.digits.append(int(in_string[i]))

    def __lt__(self, other) -> bool:
        len_self, len_other = len(self.digits), len(other.digits)
        if len_self != len_other:
            return len_self < len_other

        for i in range(len_self - 1, -1, -1):
            if self.digits[i] != other.digits[i]:
                return self.digits[i] < other.digits[i]
        return False


def difference_big_integer(num_great: BigInteger, num_less: BigInteger) -> str:
    len_great = len(num_great.digits)
    while len(num_less.digits) < len_great:
        num_less.digits.append(0)

    # calculate difference
    difference_as_list = []
    for i in range(len_great):
        current_digit = num_great.digits[i] - num_less.digits[i]
        if current_digit < 0:
            current_digit += 10
            num_great.digits[i + 1] -= 1
        difference_as_list.append(current_digit)

    # remove leading zeros
    while len(difference_as_list) > 1 and difference_as_list[-1] == 0:
        difference_as_list.pop(-1)

    difference_as_str = ''
    for i in range(len(difference_as_list) - 1, -1, -1):
        difference_as_str += str(difference_as_list[i])
    return difference_as_str


def BigMinus(s1: str, s2: str) -> str:
    big_integer_1, big_integer_2 = BigInteger(s1), BigInteger(s2)

    if big_integer_1 < big_integer_2:
        return difference_big_integer(big_integer_2, big_integer_1)
    return difference_big_integer(big_integer_1, big_integer_2)
