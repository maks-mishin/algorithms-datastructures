def print_even_numbers(input_list, i):
    """Печать только четных значений списка"""
    if i == len(input_list):
        print(flush=True)
        return
    if input_list[i] % 2 == 0:
        print(input_list[i], end=' ')
    print_even_numbers(input_list, i + 1)


def print_numbers_even_indexes(input_list, i):
    """Печать элементов списка с четными индексами"""
    if i == len(input_list):
        print(flush=True)
        return
    if i % 2 == 0:
        print(input_list[i], end=' ')
    print_numbers_even_indexes(input_list, i + 1)
