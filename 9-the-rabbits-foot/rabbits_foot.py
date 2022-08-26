def TheRabbitsFoot(in_string: str, encode: bool) -> str:
    result_str = ''
    work_str = ''.join(in_string.split())
    len_in_string = len(work_str)
    sqrt_len = len_in_string ** (1/2)

    num_rows, num_columns = int(sqrt_len), int(sqrt_len) + 1
    if sqrt_len - int(sqrt_len) == 0.0:
        num_columns -= 1

    while num_rows * num_columns < len_in_string:
        num_rows += 1
    
    if encode:
        for i in range(num_columns):
            for j in range(num_rows):
                if j * num_columns + i < len_in_string:
                    result_str += work_str[j * num_columns + i]
            result_str += ' '
    if not encode:
        work_list = in_string.split()
        for i in range(num_columns):
            for encoded_word in work_list:
                if i < len(encoded_word):
                    result_str += encoded_word[i]
    return result_str.strip()
