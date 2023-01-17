from typing import Optional, List, Any


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue: Any = val
        self.Parent: Optional[SimpleTreeNode] = parent
        self.Children: List[SimpleTreeNode] = []
        self.Level: int = 0


class SimpleTree:

    def __init__(self, root: Optional[SimpleTreeNode]):
        self.Root = root

    def AddChild(self, parent_node, new_child):
        if self.Root is None:
            self.Root = new_child
            return
        new_child.Parent = parent_node
        parent_node.Children.append(new_child)
        new_child.Level = parent_node.Level + 1

    def DeleteNode(self, node_to_delete):
        if node_to_delete.Parent is None:
            self.Root = None
            return
        node_to_delete.Parent.Children.pop(
            node_to_delete.Parent.Children.index(node_to_delete)
        )

    def GetAllNodes(self):
        if self.Root is None:
            return []
        return [self.Root] + self.GetNodesOfSubtree(self.Root)

    def GetNodesOfSubtree(self, node):
        ListOfNodes = []
        for childNode in node.Children:
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

    def FindNodesByValueOfSubtree(self, node, val):
        ListOfNodes = []
        for childNode in node.Children:
            if childNode.Children:
                ListOfNodes.extend(
                    self.FindNodesByValueOfSubtree(childNode, val)
                )
            if childNode.NodeValue == val:
                ListOfNodes.append(childNode)
        return ListOfNodes

    def MoveNode(self, original_node, new_parent):
        self.DeleteNode(original_node)
        self.AddChild(new_parent, original_node)
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

    def SetLevelToOneNode(self, current_level, current_node):
        for childNode in current_node.Children:
            if childNode.Children:
                self.SetLevelToOneNode(current_level + 1, childNode)
            childNode.Level = current_level + 1

    def _is_even_tree(self, node) -> bool:
        """
        @return True, если поддерево с корнем node является четным
        """
        count_nodes = len([node] + self.GetNodesOfSubtree(node))
        if count_nodes % 2 == 0 and node.Parent is not None:
            return True
        return False
    
    def EvenTrees(self):
        if self.Count() % 2 != 0:
            return []
        
        list_nodes_to_delete_edges = []
        for node in self.GetAllNodes():
            if not self._is_even_tree(node):
                continue
            list_nodes_to_delete_edges.append(node.Parent)
            list_nodes_to_delete_edges.append(node)
        return list_nodes_to_delete_edges
