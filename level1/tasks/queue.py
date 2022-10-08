class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super().__init__()


class Stack:
    def __init__(self):
        self.head, self.tail = DummyNode(), None
        self.count = 0

    def size(self):
        return self.count

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
        self.count += 1

    def pop(self):
        if self.count == 0:
            return None
        popped_node = self.head.next
        self.head.next = popped_node.next
        self.count -= 1
        return popped_node.value

    def peek(self):
        if self.count == 0:
            return None
        return self.head.next.value


class Queue:
    def __init__(self):
        self.stack_left = Stack()
        self.stack_right = Stack()
        self.count = 0

    def move_elements(self):
        while self.stack_left.size() > 0:
            self.stack_right.push(
                self.stack_left.pop()
            )

    def enqueue(self, value):
        self.stack_left.push(value)
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        if self.stack_right.size() == 0:
            self.move_elements()
        self.count -= 1
        return self.stack_right.pop()

    def size(self):
        return self.count
