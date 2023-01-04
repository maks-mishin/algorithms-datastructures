from typing import Optional, Any, Tuple, List


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

        CurrentNode = self.Root
        while CurrentNode is not None:
            if CurrentNode.NodeKey == key:
                return self.MakeFindResult(CurrentNode, True, False)
            if key < CurrentNode.NodeKey and not CurrentNode.LeftChild:
                return self.MakeFindResult(CurrentNode, False, True)
            if key < CurrentNode.NodeKey and CurrentNode.LeftChild:
                CurrentNode = CurrentNode.LeftChild
            if key > CurrentNode.NodeKey and not CurrentNode.RightChild:
                return self.MakeFindResult(CurrentNode, False, False)
            if key > CurrentNode.NodeKey and CurrentNode.RightChild:
                CurrentNode = CurrentNode.RightChild
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

    def FindMaxKey(self, FromNode: Optional[BSTNode]) -> Optional[BSTNode]:
        while FromNode.RightChild is not None:
            FromNode = FromNode.RightChild
        return FromNode

    def FindMinKey(self, FromNode: Optional[BSTNode]) -> Optional[BSTNode]:
        while FromNode.LeftChild is not None:
            FromNode = FromNode.LeftChild
        return FromNode

    def FinMinMax(self,
                  FromNode: Optional[BSTNode],
                  FindMax: bool) -> Optional[BSTNode]:
        """
        Ищем максимальный/минимальный ключ в поддереве.
        """
        if FindMax:
            return self.FindMaxKey(FromNode)
        return self.FindMinKey(FromNode)

    def FindSuccessorNode(self, node) -> Optional[BSTNode]:
        if node.RightChild is not None:
            return self.FinMinMax(node.RightChild, False)
        return None

    def FindNewNode(self, Node):
        if Node.LeftChild is None or Node.RightChild is None:
            return Node
        if not (Node.LeftChild is None or Node.RightChild is None):
            return self.FindSuccessorNode(Node)
        return None

    def FindNewChild(self, Node):
        if Node.LeftChild is not None:
            return Node.LeftChild
        if Node.LeftChild is None:
            return Node.RightChild
        return None

    def ConnectParentAndChild(self, NewNode, NewChild):
        if NewChild is not None:
            NewChild.Parent = NewNode.Parent
        if NewNode.Parent is None:
            self.Root = NewChild
            return
        if NewNode == NewNode.Parent.LeftChild:
            NewNode.Parent.LeftChild = NewChild
        if NewNode == NewNode.Parent.RightChild:
            NewNode.Parent.RightChild = NewChild

    def DeleteNodeByKey(self, key: int) -> bool:
        Node = self.FindNodeByKey(key).Node
        if Node.NodeKey != key:
            return False
        NodeSuccessor = self.FindNewNode(Node)
        NewChild = self.FindNewChild(NodeSuccessor)

        self.ConnectParentAndChild(NodeSuccessor, NewChild)
        if NodeSuccessor != Node:
            Node.NodeKey = NodeSuccessor.NodeKey
            Node.NodeValue = NodeSuccessor.NodeValue
        return True

    def _count_nodes_of_subtree(self,
                                FromNode: Optional[BSTNode],
                                CountNodes: int):
        """Рекурсивный подсчет количества узлов поддерева"""
        CurrentCountNodes = CountNodes
        if FromNode.LeftChild is not None:
            CurrentCountNodes = self._count_nodes_of_subtree(
                FromNode.LeftChild, CurrentCountNodes
            )
        if FromNode.RightChild is not None:
            CurrentCountNodes = self._count_nodes_of_subtree(
                FromNode.RightChild, CurrentCountNodes
            )
        return CurrentCountNodes + 1

    def Count(self):
        """Количество узлов в дереве"""

        def _count(node: Optional[BSTNode]):
            if node is None:
                return 0
            return _count(node.LeftChild) + _count(node.RightChild) + 1

        return _count(self.Root)

    def WideAllNodes(self):
        if self.Root is None:
            return []

        ListOfNodes = [self.Root]
        for node in ListOfNodes:
            if node.LeftChild is not None:
                ListOfNodes.append(node.LeftChild)
            if node.RightChild is not None:
                ListOfNodes.append(node.RightChild)
        return ListOfNodes

    def DeepAllNodes(self, OrderType):
        if OrderType == 0:
            return self._get_all_nodes_in_order([], self.Root)
        if OrderType == 1:
            return self._get_all_nodes_post_order([], self.Root)
        if OrderType == 2:
            return self._get_all_nodes_pre_order([], self.Root)

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
