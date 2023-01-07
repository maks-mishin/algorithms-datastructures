# Source: https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

def decimal_to_roman(input_num):
    all_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman_num = ''

    for decimal, roman in all_roman:
        while input_num >= decimal:
            roman_num += roman
            input_num -= decimal
    return roman_num
