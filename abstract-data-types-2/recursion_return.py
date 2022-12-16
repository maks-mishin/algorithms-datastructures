def power(base, exponent):
    """Возведение числа base в степень exponent"""
    if exponent == 1:
        return base
    return base * power(base, exponent - 1)


def sum_digits(num):
    """Вычисление суммы цифр числа"""
    if num < 10:
        return num
    last_digigt = num % 10
    num //= 10
    return last_digigt + sum_digits(num)


def list_length(input_list):
    """Вычисление длины списка"""
    if len(input_list) <= 1:
        return len(input_list)
    input_list.pop(0)
    return list_length(input_list) + 1


def is_palindrom(input_str, symbol_index, str_len):
    """Проверка, является ли строка палиндромом"""
    if str_len <= 1:
        return True
    if input_str[symbol_index] == input_str[-symbol_index - 1]:
        return is_palindrom(input_str, symbol_index + 1, str_len - 1)
    return False
