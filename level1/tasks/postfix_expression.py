from stack import Stack


def calc_postfix_expression(expression: str):
    stack1, stack2 = Stack(), Stack()
    for symbol in reversed(expression.split()):
        stack1.push(symbol)
    while stack1.size() > 0:
        if stack1.peek().isdigit():
            stack2.push(int(stack1.pop()))
            continue
        if stack1.peek() == '+':
            stack2.push(
                stack2.pop() + stack2.pop()
            )
        if stack1.peek() == '*':
            stack2.push(
                stack2.pop() * stack2.pop()
            )
        stack1.pop()
    return stack2.pop()
