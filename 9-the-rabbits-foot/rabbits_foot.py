def calc_matrix_size(len_in_string: int) -> int:
    sqrt_len = len_in_string ** (1/2)
    is_square_matrix = int(sqrt_len) ** 2 == len_in_string

    rows, columns = 0, 0
    if is_square_matrix:
        rows, columns = int(sqrt_len), int(sqrt_len)
    if not is_square_matrix:
        rows, columns = int(sqrt_len), int(sqrt_len) + 1

    while rows * columns < len_in_string:
        rows += 1
    return rows, columns


def encrypt(in_string: str) -> str:
    in_string_without_spaces = ''.join(in_string.split())
    len_in_string = len(in_string_without_spaces)
    list_no_spaces = list(in_string_without_spaces)
    rows, columns = calc_matrix_size(len_in_string)

    while len(list_no_spaces) < rows * columns:
        list_no_spaces.append('')

    result_str = ''
    for i in range(columns):
        for j in range(rows):
            result_str += list_no_spaces[j * columns + i]
        result_str += ' '
    return result_str.strip()


def decrypt(in_string: str) -> str:
    work_list = in_string.split()
    in_string_without_spaces = ''.join(work_list)
    len_in_string = len(in_string_without_spaces)
    rows, columns = calc_matrix_size(len_in_string)

    result_str = ''
    for i in range(columns):
        for encoded_word in work_list:
            if i < len(encoded_word):
                result_str += encoded_word[i]
    return result_str.strip()


def TheRabbitsFoot(in_string: str, encode: bool) -> str:
    if encode:
        return encrypt(in_string)
    return decrypt(in_string)
