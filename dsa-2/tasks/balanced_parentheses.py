def generate_brackets_sequence(brackets_sequence, left, right, parens_list):
    current_parens_list = parens_list

    if not right:
        current_parens_list.append(brackets_sequence)
    if left:
        generate_brackets_sequence(
            brackets_sequence + '(', left - 1, right, current_parens_list
        )
    if right > left:
        generate_brackets_sequence(
            brackets_sequence + ')', left, right - 1, current_parens_list
        )
    return current_parens_list


def generate_all_correct_brackets_sequences(count_seq):
    """
    Функция генерации всех корректных сбалансированных комбинаций
    круглых скобок
    """
    return generate_brackets_sequence('', count_seq, count_seq, [])
