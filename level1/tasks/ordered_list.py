class Node:
    def __init__(self, val=None):
        self.value = val
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head, self.tail = None, None
        self.count = 0
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def is_ascending(self):
        return self.__ascending

    def delete_node(self, deleted_node):
        prev, next = deleted_node.prev, deleted_node.next
        if prev is None:
            self.head = next
        if prev is not None:
            prev.next = next
            deleted_node.prev = None
        if next is None:
            self.tail = prev
        if next is not None:
            next.prev = prev
            deleted_node.next = None

    def insert_after(self, after_node, new_node):
        next_node = after_node.next
        after_node.next = new_node
        new_node.next = next_node
        new_node.prev = after_node
        if next_node is not None:
            next_node.prev = new_node
            return
        self.tail = new_node

    def insert_before(self, before_node, new_node):
        prev_node = before_node.prev
        before_node.prev = new_node
        new_node.next = before_node
        new_node.prev = prev_node
        if prev_node is not None:
            prev_node.next = new_node
            return
        self.head = new_node

    def insert_asc(self, new_node):
        node = self.head
        while (
                node.next is not None and
                self.compare(node.value, new_node.value) <= 0
        ):
            node = node.next
        if self.compare(node.value, new_node.value) <= 0:
            self.insert_after(node, new_node)
            return
        self.insert_before(node, new_node)

    def insert_desc(self, new_node):
        node = self.head
        while (
                node.next is not None and
                self.compare(node.value, new_node.value) >= 0
        ):
            node = node.next
        if self.compare(node.value, new_node.value) <= 0:
            self.insert_before(node, new_node)
            return
        self.insert_after(node, new_node)

    def add(self, value):
        new_node = Node(value)
        self.count += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        if self.is_ascending():
            self.insert_asc(new_node)
            return
        self.insert_desc(new_node)

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value > val and self.is_ascending():
                return None
            if node.value < val and not self.is_ascending():
                return None
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        deleted_node = self.find(val)
        if deleted_node is not None:
            self.delete_node(deleted_node)
            self.count -= 1

    def clean(self, asc):
        self.__ascending = asc
        self.__init__(asc)
        self.head, self.tail = None, None

    def len(self):
        return self.count

    def get_all(self):
        result_list = []
        node = self.head
        while node is not None:
            result_list.append(node)
            node = node.next
        return result_list


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1, v2 = v1.strip(), v2.strip()
        return super(OrderedStringList, self).compare(v1, v2)
