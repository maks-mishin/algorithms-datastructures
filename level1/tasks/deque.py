class Node:
    def __init__(self, val=None):
        self.value = val
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super(DummyNode, self).__init__()


class Deque:
    def __init__(self):
        self.head, self.tail = DummyNode(), DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def delete_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.count -= 1

    def addFront(self, item):
        new_node = Node(item)
        new_node.prev = self.head
        new_node.next = self.head.next
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self.count += 1

    def addTail(self, item):
        new_node = Node(item)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self.count += 1

    def removeFront(self):
        if self.count == 0:
            return None
        front_value = self.head.next.value
        self.delete_node(self.head.next)
        return front_value

    def removeTail(self):
        if self.count == 0:
            return None
        tail_value = self.tail.prev.value
        self.delete_node(self.tail.prev)
        return tail_value

    def size(self):
        return self.count
