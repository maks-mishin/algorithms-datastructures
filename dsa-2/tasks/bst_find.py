class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def __str__(self):
        return f'Node(key={str(self.NodeKey)})'


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком

    def __str__(self):
        return f'BSTFind(Node={str(self.Node)}, NodeHasKey={self.NodeHasKey}, ' \
               f'ToLeft={self.ToLeft})'


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        """
        Ищем в дереве узел и сопутствующую информацию по ключу
        return BSTFind
        """
        if self.Root is None:
            return BSTFind()

        FindResult = BSTFind()
        CurrentNode = self.Root
        while CurrentNode is not None:
            if CurrentNode.NodeKey == key:
                FindResult.Node = CurrentNode
                FindResult.NodeHasKey = True
                return FindResult
            if key < CurrentNode.NodeKey:
                if CurrentNode.LeftChild is None:
                    FindResult.Node = CurrentNode
                    FindResult.NodeHasKey = False
                    FindResult.ToLeft = True
                    break
                CurrentNode = CurrentNode.LeftChild
            if key > CurrentNode.NodeKey:
                if CurrentNode.RightChild is None:
                    FindResult.Node = CurrentNode
                    FindResult.NodeHasKey = False
                    FindResult.ToLeft = False
                    break
                CurrentNode = CurrentNode.RightChild
        return FindResult

    def AddKeyValue(self, key, val):
        """
        Добавляем ключ-значение в дерево.
        return False, если ключ уже есть
        """
        FindResult = self.FindNodeByKey(key)
        if FindResult.Node is None:
            self.Root = BSTNode(key=8, val=8, parent=None)
            return True
        if FindResult.NodeHasKey:
            return False
        ParentNode = FindResult.Node
        if FindResult.ToLeft:
            ParentNode.LeftChild = BSTNode(key, val, ParentNode)
        if not FindResult.ToLeft:
            ParentNode.RightChild = BSTNode(key, val, ParentNode)
        return True

    def FindMaxKey(self, FromNode):
        while FromNode.RightChild is not None:
            FromNode = FromNode.RightChild
        return FromNode.NodeKey

    def FindMinKey(self, FromNode):
        while FromNode.LeftChild is not None:
            FromNode = FromNode.LeftChild
        return FromNode.NodeKey

    def FinMinMax(self, FromNode, FindMax) -> BSTFind:
        """
        Ищем максимальный/минимальный ключ в поддереве.
        """
        if FindMax:
            return self.FindMaxKey(FromNode)
        return self.FindMinKey(FromNode)

    def DeleteLeaf(self, ParentNode, Node):
        if ParentNode.LeftChild == Node:
            ParentNode.LeftChild = None
        if ParentNode.RightChild == Node:
            ParentNode.RightChild = None

    def DeleteNodeWithLeftChild(self, ParentNode, Node):
        if ParentNode.LeftChild == Node:
            Node.LeftChild.Parent = ParentNode
            ParentNode.LeftChild = Node.LeftChild
        if ParentNode.RightChild == Node:
            Node.LeftChild.Parent = ParentNode
            ParentNode.RightChild = Node.LeftChild

    def DeleteNodeWithRightChild(self, ParentNode, Node):
        if ParentNode.LeftChild == Node:
            Node.RightChild.Parent = ParentNode
            ParentNode.LeftChild = Node.RightChild
        if ParentNode.RightChild == Node:
            Node.RightChild.Parent = ParentNode
            ParentNode.RightChild = Node.RightChild

    def DeleteCommonNode(self, ParentNode, Node):
        NodeSuccessor = Node.RightChild
        while NodeSuccessor is not None:
            NodeSuccessor = NodeSuccessor.LeftChild
        print('NodeSuccessor', NodeSuccessor)

    def DeleteNodeByKey(self, key):
        """
        Удаляем узел по ключу.
        return False, если узел не найден.
        """
        FoundNode = self.FindNodeByKey(key).Node
        if FoundNode is None:
            return False
        if FoundNode.Parent is None:
            self.Root = None
            return True
        # Если нет потомков у узла
        if not (FoundNode.LeftChild or FoundNode.RightChild):
            self.DeleteLeaf(FoundNode.Parent, FoundNode)
            return True
        # Если у узла один потомок
        if FoundNode.LeftChild and not FoundNode.RightChild:
            self.DeleteNodeWithLeftChild(FoundNode.Parent, FoundNode)
            return True
        if FoundNode.RightChild and not FoundNode.LeftChild:
            self.DeleteNodeWithRightChild(FoundNode.Parent, FoundNode)
            return True
        # Если два потомка у узла
        self.DeleteCommonNode(FoundNode.Parent, FoundNode)
        return True

    def CountNodesOfSubtree(self, FromNode, CountNodes):
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


tree = BST(node=BSTNode(8, 8, None))
for key in [4, 12, 2, 6, 1, 3, 5, 7, 10, 9, 11, 14, 13, 15]:
    tree.AddKeyValue(key, key)

print('count nodes before', tree.Count())
tree.DeleteNodeByKey(12)
print('count nodes after', tree.Count())
