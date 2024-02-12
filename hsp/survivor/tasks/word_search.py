def WordSearch(len_split: int, in_string: str, sub_string: str) -> list:
    if sub_string == "":
        return []

    array_after_splitting = []
    source_list_words = in_string.strip().split()

    current_string = ""
    for i in range(len(source_list_words)):
        current_word = source_list_words[i]

        if len(current_word) <= len_split:
            is_allow_add_word = len(current_string + current_word) <= len_split
            if is_allow_add_word:
                current_string += current_word + ' '
            if not is_allow_add_word:
                array_after_splitting.append(current_string.strip())
                current_string = current_word + ' '

        if not len(current_word) <= len_split:
            if current_string != "":
                array_after_splitting.append(current_string.strip())

            while len(current_word) > len_split:
                word_part = current_word[:len_split]
                current_word = current_word[len_split:]
                array_after_splitting.append(word_part)
            current_string = current_word + ' '

    if current_string.strip() != "":
        array_after_splitting.append(current_string.strip())

    return make_result_array(array_after_splitting, sub_string)


def make_result_array(string_array: list, sub_string: str) -> list:
    result_array = []

    for i in range(len(string_array)):
        if sub_string in string_array[i].split():
            result_array.append(1)
        if not sub_string in string_array[i].split():
            result_array.append(0)
    return result_array
