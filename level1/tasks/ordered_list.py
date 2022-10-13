class Node:
    def __init__(self, val=None):
        self.value = val
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super(DummyNode, self).__init__()


class OrderedList:
    def __init__(self, asc):
        self.head, self.tail = DummyNode(), DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
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

    def insert_after(self, after_node, new_node):
        new_node.prev = after_node
        new_node.next = after_node.next
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self.count += 1

    def insert_asc(self, new_node):
        node = self.head.next
        while (
                type(node) is Node and
                self.compare(node.value, new_node.value) == -1
        ):
            node = node.next
        self.insert_after(node.prev, new_node)

    def insert_desc(self, new_node):
        node = self.head.next
        while (
                type(node) is Node and
                self.compare(node.value, new_node.value) == 1
        ):
            node = node.next
        self.insert_after(node.prev, new_node)

    def add(self, value):
        new_node = Node(value)
        if self.is_ascending():
            self.insert_asc(new_node)
            return
        self.insert_desc(new_node)

    def find(self, val):
        node = self.head.next
        while type(node) is Node:
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
        deleted_node.next.prev = deleted_node.prev
        deleted_node.prev.next = deleted_node.next
        self.count -= 1

    def clean(self, asc):
        self.__ascending = asc
        self.__init__(asc)

    def len(self):
        return self.count

    def get_all(self):
        result_list = []
        node = self.head.next
        while type(node) is Node:
            result_list.append(node)
            node = node.next
        return result_list


class OrderedListString(OrderedList):
    def __init__(self, asc):
        super(OrderedListString, self).__init__(asc)

    def compare(self, v1, v2):
        v1, v2 = v1.strip(), v2.strip()
        return super(OrderedListString, self).compare(v1, v2)
