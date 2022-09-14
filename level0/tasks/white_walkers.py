def make_digit_indexes(value: str) -> list:
    return [i for i in range(len(value)) if value[i].isdigit()]


def count_white_walkers(substring: str) -> int:
    return substring.count('=')


def white_walkers(value: str) -> bool:
    digit_indexes = make_digit_indexes(value)

    if len(digit_indexes) <= 1:
        return False

    count_pairs, count_walkers = 0, 0
    for i in range(len(digit_indexes) - 1):
        if (int(value[digit_indexes[i]]) +
                int(value[digit_indexes[i + 1]]) != 10):
            continue
        count_pairs += 1
        amount_white_walkers = count_white_walkers(
            value[digit_indexes[i]:digit_indexes[i + 1] + 1]
        )
        if amount_white_walkers == 3:
            count_walkers += 1
    return count_walkers == count_pairs
