class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(self.tail.next)
            if node.next is None:
                print(node.value, '-->', node.next)
            else:
                print(node.value, '-->', node.next.value)
            node = node.next

    def find(self, val):
        """Return the found node with given value"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return node

    def fild_all(self, val):
        """Return list of all found nodes with given value"""
        return []

    def delete(self, val, all=False):
        """Delete node or all nodes from linked list by given value."""

        deleted_node, prev_node = self.head, self.head
        while deleted_node is not None:
            if deleted_node.value == val and deleted_node == self.head:
                self.head = self.head.next
                break
            if deleted_node.value == val and deleted_node != self.head:
                prev_node.next = deleted_node.next
                deleted_node.next = None
            prev_node = deleted_node
            deleted_node = deleted_node.next

    def clean(self):
        """Clean linked list"""
        self.head = None

    def len(self):
        """Return length of linked list"""
        node = self.head
        len_list = 0
        while node is not None:
            len_list += 1
            node = node.next
        return len_list

    def insert(self, after_node, new_node):
        pass
