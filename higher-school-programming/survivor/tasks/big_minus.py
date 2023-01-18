class BigInteger:
    """Class for working with large numbers"""
    def __init__(self, in_string: str) -> None:
        self.digits = [int(num) for num in reversed(list(in_string))]

    def __lt__(self, other) -> bool:
        len_self, len_other = len(self.digits), len(other.digits)
        if len_self != len_other:
            return len_self < len_other

        for self_digit, other_digit in zip(
                reversed(self.digits), reversed(other.digits)
        ):
            if self_digit != other_digit:
                return self_digit < other_digit
        return False


def difference_big_integer(lhs: BigInteger, rhs: BigInteger) -> str:
    num_great, num_less = lhs, rhs
    if lhs < rhs:
        num_great, num_less = rhs, lhs

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

    return ''.join([str(i) for i in reversed(difference_as_list)])


def BigMinus(first_num: str, second_num: str) -> str:
    return difference_big_integer(
        BigInteger(first_num), BigInteger(second_num)
    )
