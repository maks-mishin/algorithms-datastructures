class Node:
    def __init__(self, val=None):
        self.value = val
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super(DummyNode, self).__init__()


class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = DummyNode(), DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def find(self, val):
        """Return the found node with given value"""
        node = self.head.next
        while isinstance(node, Node):
            if node.Value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """Return list of all found nodes with given value"""
        result_list = []
        node = self.head.next
        while isinstance(node, Node):
            if node.Value == val:
                result_list.append(node)
            node = node.next
        return result_list

    def delete_one_node(self, deleted_node):
        """Delete one node from linked list by pointer"""
        deleted_node.next.prev = deleted_node.prev
        deleted_node.prev.next = deleted_node.next
        self.count -= 1

    def delete(self, val, all=False):
        """Delete node or all of nodes from linked list by given value"""
        delete_nodes = self.find_all(val) if all else [self.find(val)]
        for delete_node in delete_nodes:
            self.delete_one_node(delete_node)

    def clean(self):
        """Clean linked list"""
        self.__init__()

    def len(self):
        """Return length of linked list"""
        return self.count

    def insert_after(self, after_node, new_node):
        new_node.prev = after_node
        new_node.next = after_node.next
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self.count += 1

    def insert_before(self, before_node, new_node):
        """Insert node into linked list before given node 'before_node'"""
        new_node.next = before_node
        new_node.prev = before_node.prev
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self.count += 1

    def insert(self, after_node, new_node):
        """Insert node into linked list after given node 'after_node'"""
        if after_node is None and self.count == 0:
            self.add_in_head(new_node)
            return
        if after_node is None and self.count > 0:
            self.add_in_tail(new_node)
            return

        node = self.head.next
        while isinstance(node, Node):
            if node.Value != after_node.value:
                node = node.next
                continue
            self.insert_after(node, new_node)
            break

    def add_in_head(self, new_node):
        """Insert new node in head of linked list"""
        self.insert_after(self.head, new_node)

    def add_in_tail(self, item):
        """Add new node to end of list"""
        self.insert_before(self.tail, item)
