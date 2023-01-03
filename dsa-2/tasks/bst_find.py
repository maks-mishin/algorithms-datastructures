class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None

    def __str__(self):
        return f'Node(key={self.NodeKey})'

class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def MakeFindResult(self, Node, HasKey, ToLeft):
        FindResult = BSTFind()
        FindResult.Node = Node
        FindResult.NodeHasKey = HasKey
        FindResult.ToLeft = ToLeft
        return FindResult

    def FindNodeByKey(self, key):
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

    def AddKeyValue(self, key, val):
        """
        Добавляем ключ-значение в дерево.
        return False, если ключ уже есть
        """
        FindResult = self.FindNodeByKey(key)
        if FindResult.NodeHasKey:
            return False
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True
        if FindResult.ToLeft:
            FindResult.Node.LeftChild = BSTNode(key, val, FindResult.Node)
        if not FindResult.ToLeft:
            FindResult.Node.RightChild = BSTNode(key, val, FindResult.Node)
        return True

    def FindMaxKey(self, FromNode):
        while FromNode.RightChild is not None:
            FromNode = FromNode.RightChild
        return FromNode

    def FindMinKey(self, FromNode):
        while FromNode.LeftChild is not None:
            FromNode = FromNode.LeftChild
        return FromNode

    def FinMinMax(self, FromNode, FindMax) -> BSTFind:
        """
        Ищем максимальный/минимальный ключ в поддереве.
        """
        if FindMax:
            return self.FindMaxKey(FromNode)
        return self.FindMinKey(FromNode)

    def FindSuccessorNode(self, node):
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

    def DeleteNodeByKey(self, key):
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

    def CountNodesOfSubtree(self, FromNode, CountNodes):
        """Рекурсивный подсчет количества узлов поддерева"""
        CurrentCountNodes = CountNodes
        if FromNode.LeftChild is not None:
            CurrentCountNodes = self.CountNodesOfSubtree(
                FromNode.LeftChild, CurrentCountNodes
            )
        if FromNode.RightChild is not None:
            CurrentCountNodes = self.CountNodesOfSubtree(
                FromNode.RightChild, CurrentCountNodes
            )
        return CurrentCountNodes + 1

    def Count(self):
        """Количество узлов в дереве"""
        if self.Root is not None:
            return self.CountNodesOfSubtree(self.Root, 0)
        return 0

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
        if self.Root is None:
            return []
        if OrderType == 0:
            return self.InOrder([], self.Root)
        if OrderType == 1:
            return self.PostOrder([], self.Root)
        if OrderType == 2:
            return self.PreOrder([], self.Root)
        return []

    def InOrder(self, ListOfNodes, Node):
        if Node:
            self.InOrder(ListOfNodes, Node.LeftChild)
            ListOfNodes.append(Node)
            self.InOrder(ListOfNodes, Node.RightChild)
        return ListOfNodes

    def PostOrder(self, ListOfNodes, Node):
        if Node:
            self.PostOrder(ListOfNodes, Node.LeftChild)
            self.PostOrder(ListOfNodes, Node.RightChild)
            ListOfNodes.append(Node)
        return ListOfNodes

    def PreOrder(self, ListOfNodes, Node):
        if Node:
            ListOfNodes.append(Node)
            self.PostOrder(ListOfNodes, Node.LeftChild)
            self.PostOrder(ListOfNodes, Node.RightChild)
        return ListOfNodes
