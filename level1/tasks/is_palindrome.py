from deque import Deque


def is_palindrome(in_string: str) -> bool:
    deq = Deque()
    for i in range(len(in_string) // 2):
        deq.addFront(in_string[i])
        deq.addTail(in_string[-i - 1])
    while deq.size() > 0:
        if deq.removeFront() != deq.removeTail():
            return False
    return True
