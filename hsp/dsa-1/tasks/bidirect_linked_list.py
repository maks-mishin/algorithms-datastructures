class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        """Add new node to end of list"""
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        """Return the found node with given value"""
        node = self.head
        while node is not None:
            if node.Value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """Return list of all found nodes with given value"""
        result_list = []
        node = self.head
        while node is not None:
            if node.Value == val:
                result_list.append(node)
            node = node.next
        return result_list

    def delete_one_node(self, deleted_node):
        """Delete one node from linked list by pointer"""
        if deleted_node == self.head and deleted_node.next is None:
            self.head, self.tail = None, None
            return
        if deleted_node == self.head and deleted_node.next is not None:
            self.head = self.head.next
            self.head.prev = None
            return
        if deleted_node == self.tail and deleted_node.prev is not None:
            self.tail = deleted_node.prev
            self.tail.next = None
            return
        deleted_node.prev.next = deleted_node.next
        deleted_node.next.prev = deleted_node.prev

    def delete(self, val, all=False):
        """Delete node or all of nodes from linked list by given value"""
        if self.head is None:
            return

        delete_nodes = []
        if not all:
            delete_nodes = [self.find(val)]
        if all:
            delete_nodes = self.find_all(val)

        for delete_node in delete_nodes:
            self.delete_one_node(delete_node)

    def clean(self):
        """Clean linked list"""
        self.__init__()

    def len(self):
        """Return length of linked list"""
        node = self.head
        len_list = 0
        while node is not None:
            len_list += 1
            node = node.next
        return len_list

    def insert(self, after_node, new_node):
        """Insert node into linked list"""
        if after_node is None and self.head is None:
            self.add_in_head(new_node)
            return
        if after_node is None and self.head is not None:
            self.add_in_tail(new_node)
            return

        node = self.head
        while node is not None:
            if node.value != after_node.value:
                node = node.next
                continue
            new_node.next = node.next
            new_node.prev = node

            if node.next is not None:
                node.next.prev = new_node
            if node.next is None:
                self.tail = new_node
            node.next = new_node
            break

    def add_in_head(self, new_node):
        """Insert new node in head of linked list"""

        if self.head is None:
            self.tail = new_node
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
