def UFO(n: int, data: list, octal: bool) -> list:
    base = 8 if octal else 16

    decimal_nums = []
    for num in data:
        current_num = ''.join(reversed(str(num)))
        decimal_num = 0

        for power, digit in enumerate(current_num):
            decimal_num += int(digit) * base ** power
        decimal_nums.append(decimal_num)
    return decimal_nums
