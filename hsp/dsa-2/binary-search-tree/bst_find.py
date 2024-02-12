from typing import Optional, Any, List


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild: Optional[BSTNode] = None
        self.RightChild: Optional[BSTNode] = None

    def __repr__(self):
        return f'Node(key={self.NodeKey})'


class BSTFind:

    def __init__(self):
        self.Node: Optional[BSTNode] = None
        self.NodeHasKey = False
        self.ToLeft = False

    def __repr__(self) -> str:
        return f'BSTFind(Node: {self.Node}, ' \
               f'HasKey: {self.NodeHasKey}, ' \
               f'ToLeft: {self.ToLeft})'


class BST:

    def __init__(self, node: Optional[BSTNode]) -> None:
        self.Root = node

    def MakeFindResult(self, Node, HasKey, ToLeft) -> BSTFind:
        FindResult = BSTFind()
        FindResult.Node = Node
        FindResult.NodeHasKey = HasKey
        FindResult.ToLeft = ToLeft
        return FindResult

    def FindNodeByKey(self, key) -> BSTFind:
        """
        Ищем в дереве узел и сопутствующую информацию по ключу
        return BSTFind
        """
        if self.Root is None:
            return BSTFind()

        current_node = self.Root
        while current_node is not None:
            if current_node.NodeKey == key:
                return self.MakeFindResult(current_node, True, False)
            if key < current_node.NodeKey and not current_node.LeftChild:
                return self.MakeFindResult(current_node, False, True)
            if key < current_node.NodeKey and current_node.LeftChild:
                current_node = current_node.LeftChild
            if key > current_node.NodeKey and not current_node.RightChild:
                return self.MakeFindResult(current_node, False, False)
            if key > current_node.NodeKey and current_node.RightChild:
                current_node = current_node.RightChild
        return BSTFind()

    def AddKeyValue(self, key: int, val: Any) -> bool:
        """
        Добавляем ключ-значение в дерево.
        return False, если ключ уже есть
        """
        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey:
            return False
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        node_to_insert = BSTNode(key, val, find_result.Node)
        if find_result.ToLeft:
            find_result.Node.LeftChild = node_to_insert
        if not find_result.ToLeft:
            find_result.Node.RightChild = node_to_insert
        return True

    def FindMaxKey(self, from_node: Optional[BSTNode]) -> Optional[BSTNode]:
        while from_node.RightChild is not None:
            from_node = from_node.RightChild
        return from_node

    def FindMinKey(self, from_node: Optional[BSTNode]) -> Optional[BSTNode]:
        while from_node.LeftChild is not None:
            from_node = from_node.LeftChild
        return from_node

    def FinMinMax(self,
                  from_node: Optional[BSTNode],
                  find_max: bool) -> Optional[BSTNode]:
        """
        Ищем максимальный/минимальный ключ в поддереве.
        """
        if find_max:
            return self.FindMaxKey(from_node)
        return self.FindMinKey(from_node)

    def FindSuccessorNode(self, node) -> Optional[BSTNode]:
        if node.right_child is not None:
            return self.FinMinMax(node.right_child, False)
        return None

    def FindNewNode(self, node):
        if node.left_child is None or node.right_child is None:
            return node
        if not (node.left_child is None or node.right_child is None):
            return self.FindSuccessorNode(node)
        return None

    def FindNewChild(self, node):
        if node.left_child is not None:
            return node.left_child
        if node.left_child is None:
            return node.right_child
        return None

    def ConnectParentAndChild(self, new_node, new_child):
        if new_child is not None:
            new_child.parent = new_node.parent
        if new_node.parent is None:
            self.Root = new_child
            return
        if new_node == new_node.parent.left_child:
            new_node.parent.left_child = new_child
        if new_node == new_node.parent.right_child:
            new_node.parent.right_child = new_child

    def DeleteNodeByKey(self, key: int) -> bool:
        node = self.FindNodeByKey(key).Node
        if node.NodeKey != key:
            return False
        node_successor = self.FindNewNode(node)
        new_child = self.FindNewChild(node_successor)

        self.ConnectParentAndChild(node_successor, new_child)
        if node_successor != node:
            node.NodeKey = node_successor.NodeKey
            node.NodeValue = node_successor.NodeValue
        return True

    def _count_nodes_of_subtree(self,
                                from_node: Optional[BSTNode],
                                count_nodes: int):
        """Рекурсивный подсчет количества узлов поддерева"""
        current_count_nodes = count_nodes
        if from_node.LeftChild is not None:
            current_count_nodes = self._count_nodes_of_subtree(
                from_node.LeftChild, current_count_nodes
            )
        if from_node.RightChild is not None:
            current_count_nodes = self._count_nodes_of_subtree(
                from_node.RightChild, current_count_nodes
            )
        return current_count_nodes + 1

    def Count(self) -> int:
        """Количество узлов в дереве"""

        def _count(node: Optional[BSTNode]):
            if node is None:
                return 0
            return _count(node.LeftChild) + _count(node.RightChild) + 1

        return _count(self.Root)

    def WideAllNodes(self) -> List[BSTNode]:
        if self.Root is None:
            return []

        result_list_nodes: List[BSTNode] = [self.Root]
        for node in result_list_nodes:
            if node.LeftChild is not None:
                result_list_nodes.append(node.LeftChild)
            if node.RightChild is not None:
                result_list_nodes.append(node.RightChild)
        return result_list_nodes

    def DeepAllNodes(self, order_type: int) -> Optional[List[BSTNode]]:
        if order_type == 0:
            return self._get_all_nodes_in_order([], self.Root)
        if order_type == 1:
            return self._get_all_nodes_post_order([], self.Root)
        if order_type == 2:
            return self._get_all_nodes_pre_order([], self.Root)
        return None

    def _get_all_nodes_in_order(self,
                                result_list_nodes: List[BSTNode],
                                node: Optional[BSTNode]):
        if node is not None:
            self._get_all_nodes_in_order(result_list_nodes, node.LeftChild)
            result_list_nodes.append(node)
            self._get_all_nodes_in_order(result_list_nodes, node.RightChild)
        return result_list_nodes

    def _get_all_nodes_post_order(self,
                                  result_list_nodes: List[BSTNode],
                                  node: Optional[BSTNode]):
        if node is not None:
            self._get_all_nodes_post_order(result_list_nodes, node.LeftChild)
            self._get_all_nodes_post_order(result_list_nodes, node.RightChild)
            result_list_nodes.append(node)
        return result_list_nodes

    def _get_all_nodes_pre_order(self,
                                 result_list_nodes: List[BSTNode],
                                 node: Optional[BSTNode]):
        if node is not None:
            result_list_nodes.append(node)
            self._get_all_nodes_pre_order(result_list_nodes, node.LeftChild)
            self._get_all_nodes_pre_order(result_list_nodes, node.RightChild)
        return result_list_nodes
