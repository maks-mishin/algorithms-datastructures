from stack import Stack


def calc_one_operation(stack: Stack, operation: str):
    rhs = stack.pop()
    lhs = stack.pop()
    if operation == '+':
        stack.push(lhs + rhs)
    if operation == '-':
        stack.push(lhs - rhs)
    if operation == '*':
        stack.push(lhs * rhs)
    if operation == '/':
        stack.push(lhs / rhs)


def calc_postfix_expression(expression: str):
    stack1, stack2 = Stack(), Stack()
    for symbol in reversed(expression.split()):
        stack1.push(symbol)

    while stack1.size() > 0:
        if stack1.peek().isdigit():
            print(stack1.peek())
            stack2.push(int(stack1.pop()))
            continue
        calc_one_operation(stack2, stack1.peek())
        stack1.pop()
    return stack2.pop()
