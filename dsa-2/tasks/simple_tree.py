class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.Level = 0


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        if self.Root is None:
            self.Root = NewChild
            return
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
        NewChild.Level = ParentNode.Level + 1

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is None:
            self.Root = None
            return
        NodeToDelete.Parent.Children.pop(
            NodeToDelete.Parent.Children.index(NodeToDelete)
        )

    def GetAllNodes(self):
        if self.Root is None:
            return []
        return [self.Root] + self.GetNodesOfSubtree(self.Root)

    def GetNodesOfSubtree(self, Node):
        ListOfNodes = []
        for childNode in Node.Children:
            if childNode.Children:
                ListOfNodes.extend(
                    self.GetNodesOfSubtree(childNode)
                )
            ListOfNodes.append(childNode)
        return ListOfNodes

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []
        FoundNodes = self.FindNodesByValueOfSubtree(self.Root, val)
        if self.Root.NodeValue == val:
            FoundNodes.append(self.Root)
        return FoundNodes

    def FindNodesByValueOfSubtree(self, Node, val):
        ListOfNodes = []
        for childNode in Node.Children:
            if childNode.Children:
                ListOfNodes.extend(
                    self.FindNodesByValueOfSubtree(childNode, val)
                )
            if childNode.NodeValue == val:
                ListOfNodes.append(childNode)
        return ListOfNodes

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
        self.SetNodesLevel()

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return len(
            [node for node in self.GetAllNodes() if not node.Children]
        )

    def SetNodesLevel(self):
        if self.Root is None:
            return
        self.Root.Level = 0
        self.SetLevelToOneNode(0, self.Root)

    def SetLevelToOneNode(self, currentLevel, currentNode):
        for childNode in currentNode.Children:
            if childNode.Children:
                self.SetLevelToOneNode(currentLevel + 1, childNode)
            childNode.Level = currentLevel + 1
