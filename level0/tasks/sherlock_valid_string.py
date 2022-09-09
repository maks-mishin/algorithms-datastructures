def calc_chars_frequency(in_string: str) -> dict:
    result_dict = {c: in_string.count(c) for c in set(in_string)}
    return result_dict


def check_password_valid(chars_frequency: list) -> bool:
    result = all(x == chars_frequency[0] for x in chars_frequency)
    return result


def SherlockValidString(in_string: str) -> bool:
    dict_chars_frequency = calc_chars_frequency(in_string)
    chars_frequency = list(dict_chars_frequency.values())

    if check_password_valid(chars_frequency):
        return True

    low_frequency, high_frequency = min(chars_frequency), max(chars_frequency)
    if high_frequency - low_frequency > 1:
        return False

    filter_low = list(filter(lambda x: x == low_frequency, chars_frequency))
    filter_high = list(filter(lambda x: x == high_frequency, chars_frequency))

    if len(filter_low) == 1 and filter_low[0] == 1:
        return True
    if len(filter_high) == 1 and filter_high[0] - low_frequency == 1:
        return True
    return False
