from typing import Optional, List, Any


class SimpleTreeNode:

    def __init__(self, val, parent) -> None:
        self.NodeValue: Any = val
        self.Parent: Optional[SimpleTreeNode] = parent
        self.Children: List[SimpleTreeNode] = []
        self.Level: int = 0


class SimpleTree:

    def __init__(self, root: Optional[SimpleTreeNode]) -> None:
        self.Root = root

    def AddChild(self, parent_node: Optional[SimpleTreeNode],
                 new_child: SimpleTreeNode) -> None:
        if self.Root is None:
            self.Root = new_child
            return
        new_child.Parent = parent_node
        parent_node.Children.append(new_child)
        new_child.Level = parent_node.Level + 1

    def DeleteNode(self, node_to_delete: SimpleTreeNode) -> None:
        if node_to_delete.Parent is None:
            self.Root = None
            return
        node_to_delete.Parent.Children.pop(
            node_to_delete.Parent.Children.index(node_to_delete)
        )

    def GetAllNodes(self) -> List[Optional[SimpleTreeNode]]:
        if self.Root is None:
            return []
        return [self.Root] + self._get_nodes_of_subtree(self.Root)

    def _get_nodes_of_subtree(self, node) -> List[Optional[SimpleTreeNode]]:
        list_of_nodes = []
        for childNode in node.Children:
            if childNode.Children:
                list_of_nodes.extend(
                    self._get_nodes_of_subtree(childNode)
                )
            list_of_nodes.append(childNode)
        return list_of_nodes

    def FindNodesByValue(self, val) -> List[Optional[SimpleTreeNode]]:
        if self.Root is None:
            return []
        found_nodes = self.find_nodes_by_value_of_subtree(self.Root, val)
        if self.Root.NodeValue == val:
            found_nodes.append(self.Root)
        return found_nodes

    def find_nodes_by_value_of_subtree(self, node, val) ->\
            List[Optional[SimpleTreeNode]]:
        list_of_nodes = []
        for childNode in node.Children:
            if childNode.Children:
                list_of_nodes.extend(
                    self.find_nodes_by_value_of_subtree(childNode, val)
                )
            if childNode.NodeValue == val:
                list_of_nodes.append(childNode)
        return list_of_nodes

    def MoveNode(self, original_node: SimpleTreeNode,
                 new_parent: SimpleTreeNode) -> None:
        self.DeleteNode(original_node)
        self.AddChild(new_parent, original_node)
        self._set_nodes_level()

    def Count(self) -> int:
        return len(self.GetAllNodes())

    def LeafCount(self) -> int:
        return len(
            [node for node in self.GetAllNodes() if not node.Children]
        )

    def _set_nodes_level(self) -> None:
        if self.Root is None:
            return
        self.Root.Level = 0
        self._set_level_to_one_node(0, self.Root)

    def _set_level_to_one_node(self, current_level: int,
                               current_node: SimpleTreeNode) -> None:
        for childNode in current_node.Children:
            if childNode.Children:
                self._set_level_to_one_node(current_level + 1, childNode)
            childNode.Level = current_level + 1

    def _is_even_tree(self, node) -> bool:
        """
        @return True, если поддерево с корнем node является четным
        """
        count_nodes = len([node] + self._get_nodes_of_subtree(node))
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
