# Source: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

import math


def make_list_digits_of_num(num):
    return list(map(int, list(str(num))))


def persistence(num):
    count_multiplications = 0
    if num < 10:
        return count_multiplications
    
    list_digits_of_num = make_list_digits_of_num(num)
    result_num = math.prod(list_digits_of_num)
    count_multiplications += 1

    while result_num >= 10:
        list_digits_of_num = make_list_digits_of_num(result_num)
        result_num = math.prod(list_digits_of_num)
        count_multiplications += 1
    return count_multiplications
