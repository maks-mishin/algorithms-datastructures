class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node
        self.CountNodes = 1

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
        self.CountNodes += 1
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
        parent = node.Parent
        while parent is not None and node == parent.RightChild:
            node = parent
            parent = parent.Parent
        return parent

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
        FoundNode = self.FindNodeByKey(key).Node
        if FoundNode.NodeKey != key:
            return False
        NewNode = self.FindNewNode(FoundNode)
        NewChild = self.FindNewChild(NewNode)

        self.ConnectParentAndChild(NewNode, NewChild)
        if NewNode != FoundNode:
            FoundNode.NodeKey = NewNode.NodeKey
            FoundNode.NodeValue = NewNode.NodeValue
        self.CountNodes -= 1
        return True

    def Count(self):
        """Количество узлов в дереве"""
        if self.CountNodes and self.Root is None:
            self.CountNodes -= 1
        return self.CountNodes
