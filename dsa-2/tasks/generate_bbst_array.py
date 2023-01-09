from typing import Optional, List


def FindKeyIndex(keys_array, key) -> Optional[int]:
    """Search index of key in array"""

    def _find_key_index(index: int, key: int):
        if index >= len(keys_array):
            return None

        node = keys_array[index]
        if node is None:
            return -1 * index
        if key == node:
            return index
        if key > node:
            return _find_key_index(2 * index + 2, key)
        if key < node:
            return _find_key_index(2 * index + 1, key)
    return _find_key_index(0, key)


def AddKey(keys_array, key):
    """Add key to array"""

    key_index = FindKeyIndex(keys_array, key)
    if key_index is None:
        return -1
    if key_index < 0:
        keys_array[-key_index] = key
        return -key_index
    # If tree is empty
    if key_index == 0 and keys_array[0] is None:
        keys_array[0] = key
    return key_index


def GenerateBBSTArray(keys_array: List[int]) -> Optional[List[int]]:
    def _generate_bbst_array(keys_array: List[int], result_keys_array: List[int]) -> None:
        if not keys_array:
            return
        index_mid_element = len(keys_array) // 2
        AddKey(result_keys_array, keys_array[index_mid_element])
        _generate_bbst_array(keys_array[:index_mid_element], result_keys_array)
        _generate_bbst_array(keys_array[index_mid_element + 1:], result_keys_array)

    if not keys_array:
        return None
    result_keys_array: List[Optional[int]] = [None] * len(keys_array)
    keys_array.sort()
    index_mid_element = len(keys_array) // 2
    # Set root node of overall tree
    result_keys_array[0] = keys_array[index_mid_element]
    _generate_bbst_array(keys_array[:index_mid_element], result_keys_array)
    _generate_bbst_array(keys_array[index_mid_element + 1:], result_keys_array)
    return result_keys_array
