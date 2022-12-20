def generate_brackets_sequence(p, left, right, parens=None):
    if parens is None:
        parens = []

    if left:
        generate_brackets_sequence(p + '(', left - 1, right, parens)
    if right > left:
        generate_brackets_sequence(p + ')', left, right - 1, parens)
    if not right:
        parens.append(p)
    return parens


def generate_all_correct_brackets_sequences(count_seq):
    """
    Функция генерации всех корректных сбалансированных комбинаций
    круглых скобок
    """
    return generate_brackets_sequence('', count_seq, count_seq)
