class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        """Add new node to end of list"""
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        """Debug print"""
        node = self.head
        while node is not None:
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
        return None

    def find_all(self, val):
        """Return list of all found nodes with given value"""
        result_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                result_list.append(node)
            node = node.next
        return result_list

    def delete(self, val, all=False):
        """Delete node or all nodes from linked list by given value."""
        deleted_node, prev_node = self.head, self.head

        while deleted_node is not None:
            if deleted_node.value == val and deleted_node == self.head:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
                if not all:
                    break
                deleted_node = self.head
                continue
            if deleted_node.value == val and deleted_node == self.tail:
                prev_node.next = None
                self.tail = prev_node

            if deleted_node.value == val:
                prev_node.next = deleted_node.next
                deleted_node.next = None
                if not all:
                    break
                deleted_node = prev_node.next
                continue
            prev_node = deleted_node
            deleted_node = deleted_node.next

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
        """Insert node in linked list"""
        if after_node is None:
            new_node.next = self.head
            self.head = new_node
            return

        # insert after arbitrary node
        node, prev_node = self.head, self.head

        while node is not None:
            prev_node = node
            node = node.next

            if (
                    prev_node.value == after_node.value and
                    prev_node == self.tail
            ):
                new_node.next = node
                prev_node.next = new_node
                self.tail = new_node
            if prev_node.value == after_node.value:
                new_node.next = node
                prev_node.next = new_node
