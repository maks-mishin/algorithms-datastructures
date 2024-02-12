def squirrel(number: int) -> int:
    factorial = 1
    for i in range(number):
        factorial *= i + 1
    while factorial > 10:
        factorial = factorial // 10
    return factorial
