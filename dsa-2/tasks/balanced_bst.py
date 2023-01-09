from typing import Optional, List


class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева
        self.TreeArray = None

    def FindKeyIndex(self, key) -> Optional[int]:
        """Search index of key in array"""

        def _find_key_index(index: int, key: int):
            if index >= len(self.TreeArray):
                return None

            node = self.TreeArray[index]
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
            self.TreeArray[-key_index] = key
            return -key_index
        # If tree is empty
        if key_index == 0 and self.TreeArray[0] is None:
            self.TreeArray[0] = key
        return key_index

    def GenerateTree(self, array: List[int]) -> Optional[List[int]]:
        def _generate_tree(array: List[int],
                           result_array: List[int],
                           parent: Optional[BSTNode]) -> Optional[BSTNode]:
            if not array:
                return
            index_mid_element = len(array) // 2
            self.AddKey(array[index_mid_element])
            node = BSTNode(
                key=array[index_mid_element],
                parent=parent
            )
            node.Level = parent.Level + 1
            node.LeftChild = _generate_tree(
                array[:index_mid_element], result_array, node
            )
            node.RightChild = _generate_tree(
                array[index_mid_element + 1:], result_array, node
            )
            return node

        if not array:
            return None

        self.TreeArray: List[Optional[int]] = [None] * len(array)
        array.sort()
        index_mid_element = len(array) // 2
        self.TreeArray[0] = array[index_mid_element]
        root_node = BSTNode(
            key=array[index_mid_element],
            parent=None
        )
        root_node.LeftChild = _generate_tree(
            array[:index_mid_element], self.TreeArray, root_node
        )
        root_node.RightChild = _generate_tree(
            array[index_mid_element + 1:], self.TreeArray, root_node
        )
        self.Root = root_node

    def _get_subtree_height(
            self, node: Optional[BSTNode], current_height: int) -> int:
        if node is None:
            return 0
        return current_height + 1 + self._get_subtree_height(
            node.LeftChild, current_height
        ) + self._get_subtree_height(
            node.RightChild, current_height
        )

    def IsBalanced(self, root_node: Optional[BSTNode]) -> bool:
        if root_node is None:
            return True
        left_subtree_height = self._get_subtree_height(
            root_node.LeftChild, 0
        )
        right_subtree_height = self._get_subtree_height(
            root_node.RightChild, 0
        )
        return abs(left_subtree_height - right_subtree_height) <= 1
