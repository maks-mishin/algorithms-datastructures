def WordSearch(len_split: int, s: str, subs: str) -> list:
    if subs == "":
        return []

    array_after_splitting = []
    source_list_words = s.strip().split()

    current_string = ""
    for i in range(len(source_list_words)):
        current_word = source_list_words[i]

        if len(current_word) <= len_split:
            if len(current_string + ' ' + current_word) <= len_split:
                current_string += current_word + ' '
            else:
                array_after_splitting.append(current_string.strip())
                current_string = current_word + ' '
        else:
            if current_string != "":
                array_after_splitting.append(current_string.strip())

            while len(current_word) > len_split:
                word_part = current_word[:len_split]
                current_word = current_word[len_split:]
                array_after_splitting.append(word_part)
            current_string = current_word + ' '
    if current_string.strip() != "":
        array_after_splitting.append(current_string.strip())

    result_array = []
    for i in range(len(array_after_splitting)):
        if subs in array_after_splitting[i].split():
            result_array.append(1)
        else:
            result_array.append(0)
    return result_array
