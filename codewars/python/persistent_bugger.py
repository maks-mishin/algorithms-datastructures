# Source: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

import operator
from functools import reduce


def persistence(num):
    count_multiplications = 0
    while num >= 10:
        num = reduce(operator.mul, [int(i) for i in str(num)], 1)
        count_multiplications += 1
    return count_multiplications
