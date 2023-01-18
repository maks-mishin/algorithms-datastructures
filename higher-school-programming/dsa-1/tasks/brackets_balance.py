from stack import Stack


def brackets_balance(in_string: str) -> bool:
    stack = Stack()
    for bracket in in_string:
        if bracket == '(':
            stack.push(bracket)
        if bracket == ')' and stack.size() == 0:
            return False
        if bracket == ')':
            stack.pop()
    return stack.size() == 0
