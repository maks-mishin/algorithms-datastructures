def calc_matrix_size(len_in_string: int) -> int:
    sqrt_len = len_in_string ** (1/2)
    is_square_matrix = int(sqrt_len) ** 2 == len_in_string

    rows = int(sqrt_len)
    columns = int(sqrt_len) if is_square_matrix else int(sqrt_len) + 1

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
    if in_string.strip() == '':
        return ''

    work_list = in_string.split()
    len_in_string = len(''.join(work_list))
    rows, columns = calc_matrix_size(len_in_string)

    list_no_spaces = [list(word) for word in work_list]
    
    for i in range(len(list_no_spaces)):
        while len(list_no_spaces[i]) < columns:
            list_no_spaces[i].append('')

    result_str = ''
    for i in range(columns):
        for encoded_word in list_no_spaces:
            result_str += encoded_word[i]
    return result_str.strip()


def TheRabbitsFoot(in_string: str, encode: bool) -> str:
    if encode:
        return encrypt(in_string)
    return decrypt(in_string)
