from typing import Optional, List, Union


class aBST:

    def __init__(self, depth: int):
        tree_size = 2 ** (depth + 1) - 1 if depth >= 0 else 0
        self.Tree: List[Union[int, None]] = [None] * tree_size

    def FindKeyIndex(self, key) -> Optional[int]:
        """
        Search index of key in array
        """
        def _find_key_index(index: int, key: int):
            if index >= len(self.Tree):
                return None

            node = self.Tree[index]
            if node is None:
                return -1 * index
            if key == node:
                return index
            if key > node:
                return _find_key_index(2 * index + 2, key)
            if key < node:
                return _find_key_index(2 * index + 1, key)

        return _find_key_index(0, key)

    def AddKey(self, key):
        """Add key to array"""
        key_index = self.FindKeyIndex(key)
        if key_index is None:
            return -1
        if key_index < 0:
            self.Tree[-key_index] = key
            return -key_index
        # If tree is empty
        if key_index == 0 and self.Tree[0] is None:
            self.Tree[0] = key
        return key_index
